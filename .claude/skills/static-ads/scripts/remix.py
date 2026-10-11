#!/usr/bin/env python3
"""Clone a static ad template with the brand's product via OpenAI gpt-image-2 (images/edits).
Usage: remix.py NAME --prompt prompts/NAME.txt [--concept template.png] [--product photo.jpg] [--n 1] [--quality high] [--model gpt-image-2] [--size 1024x1024]
Image 1 = product photo (always). Image 2 = template (layout reference).
Output: $SAC_WORKDIR/out/NAME_v<k>.png ; log line in $SAC_WORKDIR/log.jsonl ; optional copy into $SAC_PUB.
Prints 'ERREUR ...' and exits non-zero on failure (srun.py greps for it; D10 also checks a new file exists).

Generic copy of /root/workspace/wh-remix/remix.py (Wildhorn): the Wildhorn version also published into
/srv/wildhorn-lp/remix and rebuilt a gallery; here publishing is optional (SAC_PUB) and no gallery is built."""
import argparse, base64, json, os, shutil, sys, time, fcntl
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C

W = C.WORKDIR; OUT = C.ensure_out(); PUB = C.PUB
p = argparse.ArgumentParser(); p.add_argument("name"); p.add_argument("--prompt", required=True)
p.add_argument("--concept"); p.add_argument("--product", default=C.PRODUCT_PHOTO, help="brand product photo (Image 1)")
p.add_argument("--n", type=int, default=1); p.add_argument("--quality", default="high")
p.add_argument("--model", default="gpt-image-2"); p.add_argument("--size", default="1024x1024")
a = p.parse_args()
key = C.key(C.OPENAI_KEY_FILE)
prompt = open(a.prompt).read()
files = [("image[]", ("product" + os.path.splitext(a.product)[1], open(a.product, "rb"), "image/jpeg" if a.product.lower().endswith((".jpg", ".jpeg")) else "image/png"))]
if a.concept:
    ext = os.path.splitext(a.concept)[1].lower()
    files.append(("image[]", (os.path.basename(a.concept), open(a.concept, "rb"), "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png")))
t = time.time(); r = None
for attempt in range(3):
    try:
        for _, (_, fh, _) in files: fh.seek(0)
        r = requests.post("https://api.openai.com/v1/images/edits", headers={"Authorization": f"Bearer {key}"},
                          data={"model": a.model, "prompt": prompt, "n": a.n, "quality": a.quality, "size": a.size}, files=files, timeout=600)
        if r.status_code in (500, 502, 503, 504, 429) and attempt < 2: time.sleep(20); continue
        break
    except requests.exceptions.RequestException as e:
        if attempt == 2: sys.exit(f"ERREUR reseau apres 3 essais: {e}")
        time.sleep(20)
if r.status_code != 200: sys.exit(f"ERREUR {r.status_code}: {r.text[:800]}")   # moderation refusals land here (400 moderation_blocked)
d = r.json(); outs = []
k0 = len([f for f in os.listdir(OUT) if f.startswith(a.name + "_v")])
for i, im in enumerate(d["data"]):
    fn = f"{a.name}_v{k0+i+1}.png"; path = f"{OUT}/{fn}"
    open(path, "wb").write(base64.b64decode(im["b64_json"])); outs.append(fn)
    if PUB:
        os.makedirs(PUB, exist_ok=True); shutil.copy(path, f"{PUB}/{fn}")
if PUB:
    if a.concept: shutil.copy(a.concept, f"{PUB}/{a.name}_concept{os.path.splitext(a.concept)[1]}")
    shutil.copy(a.prompt, f"{PUB}/{a.name}_prompt.txt")
log = {"name": a.name, "outs": outs, "concept": bool(a.concept), "model": a.model, "quality": a.quality, "secs": round(time.time()-t),
       "usage": d.get("usage"), "ts": time.strftime("%Y-%m-%d %H:%M")}
with open(f"{W}/log.jsonl", "a") as f: fcntl.flock(f, fcntl.LOCK_EX); f.write(json.dumps(log) + "\n")
print(json.dumps(log))
