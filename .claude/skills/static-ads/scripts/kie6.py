#!/usr/bin/env python3
"""kie.ai helper (upload refs, create task, poll, download). Imported by kie_gen.py; also runnable on a jobs file.
usage: kie6.py <jobs.json> [threads]
jobs = [{"id": "NAME", "model": "nano-banana-pro", "prompt": "...", "aspect": "1:1",
         "resolution": "2K", "refs": ["/path.png"], "tag": "v1"}]
Output: $SAC_WORKDIR/out/_kie/<id>_<tag>.png + log.jsonl (full prompt, model, task id).

Generic copy of /root/workspace/wildhorn-lp/p6/gen/kie6.py: OUT, upload path and log date are no longer Wildhorn-specific.
Key: read from KIE_KEY_FILE (default /etc/secrets/kie_api_key) — never printed."""
import json, os, sys, time, urllib.request, base64, mimetypes, threading, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C

KEY = C.key(C.KIE_KEY_FILE)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
BASE = "https://api.kie.ai/api/v1"; UPL = "https://kieai.redpandaai.co/api/file-base64-upload"
OUT = os.path.join(C.OUT, "_kie")
LOG = OUT + "/log.jsonl"; LOCK = threading.Lock(); UPC = {}
UPLOAD_PATH = "images/" + C.FILE_PREFIX.lower()
IMGKEYS = {"gpt-image-2-image-to-image": ["input_urls"], "flux-2/pro-image-to-image": ["input_urls"],
           "nano-banana-pro": ["image_input"], "nano-banana-2": ["image_input", "image_urls"]}


def post(url, obj, t=90):
    r = urllib.request.Request(url, data=json.dumps(obj).encode(), headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(r, timeout=t) as f: return json.load(f)


def get(url):
    r = urllib.request.Request(url, headers={"Authorization": "Bearer " + KEY, "User-Agent": UA})
    with urllib.request.urlopen(r, timeout=60) as f: return json.load(f)


def credits(): return get(BASE + "/chat/credit").get("data")


def upload(p):
    with LOCK:
        if p in UPC: return UPC[p]
    mime = mimetypes.guess_type(p)[0] or "image/png"
    out = post(UPL, {"base64Data": f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode(),
                     "uploadPath": UPLOAD_PATH, "fileName": os.path.basename(p)}, 180)
    u = (out.get("data") or {}).get("downloadUrl")
    if not u: raise RuntimeError("upload " + str(out)[:200])
    with LOCK: UPC[p] = u
    return u


def one(job):
    os.makedirs(OUT, exist_ok=True)
    model = job["model"]; refs = [upload(p) for p in job.get("refs", [])]
    inp = {"prompt": job["prompt"], "aspect_ratio": job.get("aspect", "1:1"), "output_format": "png"}
    if job.get("resolution"): inp["resolution"] = job["resolution"]
    if refs:
        for k in IMGKEYS.get(model, ["image_urls"]): inp[k] = refs
    t0 = time.time(); out = post(BASE + "/jobs/createTask", {"model": model, "input": inp})
    tid = (out.get("data") or {}).get("taskId")
    if out.get("code") != 200 or not tid: raise RuntimeError("create " + str(out)[:300])
    while time.time() - t0 < 600:
        time.sleep(6); d = get(BASE + "/jobs/recordInfo?taskId=" + tid).get("data") or {}
        st = (d.get("state") or "").lower()
        if st in ("success", "succeeded", "completed"):
            urls = json.loads(d.get("resultJson") or "{}").get("resultUrls") or []; break
        if st in ("fail", "failed", "error"): raise RuntimeError("fail " + str(d.get("failMsg") or d.get("failCode"))[:300])
    else: raise RuntimeError("timeout " + tid)
    from PIL import Image
    files = []
    for i, u in enumerate(urls):
        raw = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=180).read()
        name = f"{job['id']}_{job.get('tag','v1')}" + (f"_{i}" if i else "")
        src = f"{OUT}/{name}.src"; open(src, "wb").write(raw)
        im = Image.open(src); im.load(); im = im.convert("RGB"); png = f"{OUT}/{name}.png"; im.save(png, "PNG"); os.remove(src)
        files.append({"file": png, "size": list(im.size), "sha256": hashlib.sha256(open(png, "rb").read()).hexdigest()[:16]})
    return tid, files, round(time.time() - t0), {k: v for k, v in inp.items() if k != "prompt"}


def main():
    jobs = json.load(open(sys.argv[1])); th = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    c0 = credits(); print("credits before", c0, flush=True)
    q = list(jobs)

    def worker():
        while True:
            with LOCK:
                if not q: return
                j = q.pop(0)
            for attempt in (1, 2):
                try:
                    tid, files, dt, params = one(j)
                    rec = {"id": j["id"], "tag": j.get("tag", "v1"), "model": "kie.ai " + j["model"], "tid": tid, "files": files, "t": dt,
                           "prompt": j["prompt"], "refs": j.get("refs", []), "params": params, "date": time.strftime("%Y-%m-%d")}
                    break
                except Exception as e:
                    rec = {"id": j["id"], "tag": j.get("tag", "v1"), "model": j["model"], "err": str(e)[:300], "attempt": attempt}
            with LOCK:
                open(LOG, "a").write(json.dumps(rec) + "\n"); print(json.dumps({k: v for k, v in rec.items() if k != "prompt"}), flush=True)
    ts = [threading.Thread(target=worker) for _ in range(th)]
    [t.start() for t in ts]; [t.join() for t in ts]
    c1 = credits(); print("credits after", c1, "used", c0 - c1, flush=True)


if __name__ == "__main__": main()
