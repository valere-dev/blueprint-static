#!/usr/bin/env python3
"""Fallback / scene generator via kie.ai when OpenAI moderation blocks, or when a model is better at the job.
usage: kie_gen.py NAME --prompt P [--concept TEMPLATE] [--product IMG] [--model seedream|flux|nano] [--aspect ASPECT]
  seedream = bytedance/seedream-v4-edit  (scene only: NEVER a full ad — D7)
  flux     = flux-2/pro-image-to-image   (legacy fallback of run 1, D1)
  nano     = nano-banana-pro             (best at PAINTING text into a scene: sunscreen letters, D5)
  --aspect: for seedream it is written to input.image_size (kie's seedream ignores aspect_ratio), e.g. square_hd, portrait_16_9.
Refs order: --product first, then --concept.  In seedream_comp the TEMPLATE is passed as --product (the only reference: the scene to edit).
Writes $SAC_WORKDIR/out/NAME_vN.png like remix.py and logs to $SAC_WORKDIR/log.jsonl.  Prints 'ERREUR ...' on failure.

Generic copy of /root/workspace/wh-remix/kie_gen.py (it imported /root/workspace/wildhorn-lp/p6/gen/kie6.py; here kie6.py sits next to it)."""
import argparse, json, os, sys, time, shutil, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C

W = C.WORKDIR; OUT = C.ensure_out()
spec = importlib.util.spec_from_file_location("kie6", os.path.join(C.SCRIPTS, "kie6.py")); k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)
MODELS = {"seedream": "bytedance/seedream-v4-edit", "flux": "flux-2/pro-image-to-image", "nano": "nano-banana-pro"}
k.IMGKEYS["bytedance/seedream-v4-edit"] = ["image_urls"]
p = argparse.ArgumentParser(); p.add_argument("name"); p.add_argument("--prompt", required=True); p.add_argument("--concept")
p.add_argument("--product", default=C.PRODUCT_PHOTO); p.add_argument("--model", default="seedream"); p.add_argument("--aspect")
a = p.parse_args()
model = MODELS.get(a.model, a.model)
refs = [a.product] + ([a.concept] if a.concept else [])
job = {"id": a.name, "model": model, "prompt": open(a.prompt).read()[:4900], "aspect": "1:1", "refs": refs, "tag": a.model}
if model in ("nano-banana-pro", "flux-2/pro-image-to-image"): job["resolution"] = "2K" if model == "nano-banana-pro" else "1K"
if model == "bytedance/seedream-v4-edit": job["aspect"] = "square_hd"
if a.aspect: job["aspect"] = a.aspect
if a.aspect and "seedream" in model:  # seedream on kie reads image_size, not aspect_ratio
    _post = k.post

    def _p(url, body, *r, **kw):
        if "createTask" in url: body["input"]["image_size"] = a.aspect
        return _post(url, body, *r, **kw)
    k.post = _p
t = time.time()
try:
    tid, files, dt, inp = k.one(job)
except Exception as e:
    sys.exit(f"ERREUR kie {model}: {e}")
k0 = len([f for f in os.listdir(OUT) if f.startswith(a.name + "_v")])
fn = f"{a.name}_v{k0+1}.png"; shutil.copy(files[0]["file"], f"{OUT}/{fn}")
open(f"{W}/log.jsonl", "a").write(json.dumps({"name": a.name, "outs": [fn], "model": "kie " + model, "secs": round(time.time()-t), "ts": time.strftime("%Y-%m-%d %H:%M")}) + "\n")
print(json.dumps({"name": a.name, "out": fn, "model": model}))
