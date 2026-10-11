#!/usr/bin/env python3
"""Simplified generator (2026-10-11, after Loom 1): ONE kie.ai call per ad, short prompt, template + product photos as references.
usage: kgen.py NUM PROMPT.txt REF1 [REF2 ...] [--model gpt|nano|seedream] [--aspect 1:1|2:3|3:2|9:16|4:5]
Output: out/s_NN_vK.png (next try number) + a line in batch/calls.jsonl with the credits used. Models/costs (Adrien, 2026-10): gpt = gpt-image-2
on kie, 10 credits; nano = Nano Banana Pro, 18 credits (refusals, text edits); seedream = 6 credits (last resort)."""
import argparse, glob, json, os, shutil, sys, time
R = "/home/adanalysis/workspace/blueprint-static/edenvia"; SKILL = "/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads"
sys.path.insert(0, SKILL + "/scripts"); import kie6 as k
MODELS = {"gpt": "gpt-image-2-image-to-image", "nano": "nano-banana-pro", "seedream": "bytedance/seedream-v4-edit"}
p = argparse.ArgumentParser(); p.add_argument("num", type=int); p.add_argument("prompt"); p.add_argument("refs", nargs="+")
p.add_argument("--model", default="gpt"); p.add_argument("--aspect", default="1:1"); p.add_argument("--prefix", default="s"); a = p.parse_args()
model = MODELS[a.model]; k.IMGKEYS.setdefault("bytedance/seedream-v4-edit", ["image_urls"])
key = f"{a.prefix}_{a.num:02d}"; out = f"{R}/out/{key}_v{len(glob.glob(f'{R}/out/{key}_v*.png')) + 1}.png"
job = {"id": key, "model": model, "prompt": open(a.prompt).read(), "aspect": a.aspect, "refs": a.refs, "tag": "k" + str(int(time.time()))}
if a.model == "nano": job["resolution"] = "2K"
c0 = k.credits(); t = time.time()
try: tid, files, dt, params = k.one(job)
except Exception as e: sys.exit(f"ERREUR kie {model}: {e}")
c1 = k.credits(); shutil.copy(files[0]["file"], out)
open(f"{R}/batch/calls.jsonl", "a").write(json.dumps({"num": a.num, "engine": "kie " + a.model, "ok": True, "ts": time.strftime("%Y-%m-%d %H:%M:%S"), "credits": c0 - c1, "secs": round(time.time() - t), "size": files[0]["size"], "params": params}) + "\n")
print(f"{a.prefix.upper()}{a.num:02d}: {os.path.basename(out)} {files[0]['size']} — {c0 - c1} credits ({c1} left), {round(time.time() - t)} s")
