#!/usr/bin/env python3
"""Edenvia batch 01 — round 2 of family 1 (VPS-SETUP.md §3c, Loom 1): the product re-placed from the founder's photo library (C23)
on every validated layout, pixels otherwise kept (D21); S2's offer button becomes "-50%" (B23). Nothing else moves.
Base = the sell version of round 1 (latest try). Each ad gets ONE new try: the base image + the library cutout pasted over the
old product at the same spot, the same size or bigger (never smaller, C23), contact shadow, colour grade matched where the scene is
dark. S4 has no product (the template has none, C7): no new try. Calls are script-only (no API cost).
usage: SAC_WORKDIR=<repo>/edenvia python3 round2.py
"""
import glob, json, os, re, subprocess, sys, time
from PIL import Image, ImageDraw, ImageFont
R = "/home/adanalysis/workspace/blueprint-static/edenvia"; SKILL = "/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads"
OUT = f"{R}/out"; B = f"{R}/batch"; T = f"{B}/templates"; TF = f"{B}/templates-pool-full"; CUT = f"{R}/assets/product/cutouts"
STAND = f"{CUT}/pouch-standing-studio.png"; HELD = f"{CUT}/pouch-held-hand-kitchen.png"
sys.path.insert(0, SKILL + "/scripts"); from pages_common import outs_for

def nxt(n):
    return f"{OUT}/s_{n:02d}_v{len(glob.glob(f'{OUT}/s_{n:02d}_v*.png')) + 1}.png"

def comp(n, base, spec, note):
    spec = dict(spec); out = nxt(n); cj = f"{B}/prompts/s_{n:02d}_r2.json"; json.dump(spec, open(cj, "w"))
    subprocess.run(["python3", f"{SKILL}/scripts/composite.py", base, out, cj], check=True)
    open(f"{B}/calls.jsonl", "a").write(json.dumps({"num": n, "engine": "script", "ok": True, "ts": time.strftime("%Y-%m-%d %H:%M:%S"), "note": "R2: " + note}) + "\n")
    print(f"S{n}: {os.path.basename(out)} — {note}"); return out

def sell(n):
    return outs_for(f"s_{n:02d}")[-1]

# Product placements (fractions): x = centre, y = bottom edge, h = height. Measured on the round-1 sell versions so the new cutout
# covers the old product completely (same size or bigger), library pouch = studio shot (front-on, droplets), aspect 0.69.
P = {
    1: dict(tpl=f"{T}/10-11_c0021_PrimalEdgeBison.webp", jar={"x": 0.80, "y": 0.52, "h": 0.33, "src": STAND}, note="pouch in the gold column, studio cutout"),
    3: dict(tpl=f"{TF}/10-11_03_c0178_Blueprint.jpg", jar={"x": 0.25, "y": 0.585, "h": 0.40, "src": STAND}, note="pouch under the headline, studio cutout, bigger"),
    5: dict(tpl=f"{TF}/10-11_05_c0192_Blueprint.png", jar={"x": 0.50, "y": 0.858, "h": 0.335, "src": STAND}, note="pouch between the diagrams, studio cutout"),
    6: dict(tpl=f"{TF}/10-11_06_c0196_Blueprint.png", jar={"x": 0.19, "y": 0.56, "h": 0.33, "src": STAND, "brightness": 0.86, "contrast": 1.05}, note="floating pouch top-left, studio cutout graded to the dark scene"),
    7: dict(tpl=f"{T}/10-11_c0233_ArcticGlowBalm.webp", jar={"x": 0.74, "y": 0.64, "h": 0.30, "src": STAND}, note="pouch on the right half, studio cutout"),
    9: dict(tpl=f"{T}/10-11_c0310_Overload.webp", jar={"x": 0.85, "y": 0.88, "h": 0.265, "src": STAND}, note="pouch bottom right, studio cutout"),
}
for n, p in P.items():
    comp(n, sell(n), {"template": p["tpl"], "jar": p["jar"]}, p["note"])

# S8: the AI pouch (x 0.14–0.50, y 0.55–0.85 of 1080x1446) is wider than a same-height studio pouch → first hide it behind a strip of the
# counter copied from its right (tiles + marble, same rows), then paste the studio cutout at the old height.
base = Image.open(sell(8)).convert("RGB"); W, H = base.size
patch = base.crop((int(0.505 * W), int(0.546 * H), int(0.545 * W), int(0.86 * H))).resize((int(0.37 * W), int(0.314 * H)), Image.LANCZOS)
base.paste(patch, (int(0.135 * W), int(0.546 * H))); tmp = f"{B}/prompts/s_08_r2_base.png"; base.save(tmp)
comp(8, tmp, {"template": f"{T}/10-11_c0259_GoliAshwagandha.webp", "jar": {"x": 0.32, "y": 0.85, "h": 0.33, "src": STAND}}, "pouch on the counter, studio cutout (old AI pouch hidden behind a counter strip)")

# S10: the pouch is held at the chest → the hand comes from the library too (C23): held cutout (hand + pouch, kitchen daylight) over the
# illustrated pouch and hands. Placed so the pouch covers the old one (x 0.615–0.985, y 0.51–0.74 of 1080x1920); the hand overhangs right.
comp(10, sell(10), {"template": f"{T}/10-11_c0376_MarsMen.webp", "jar": {"x": 0.85, "y": 0.845, "h": 0.345, "src": HELD, "noshadow": True}},
     "held pouch + hand from the library over the illustrated pouch")

# S2: offer button "FLAT 20% OFF" slot → "-50%" (B23). The round-1 button (black rounded, x 0.32–0.70, y 0.842–0.918) is repainted and relabelled.
base = Image.open(sell(2)).convert("RGB"); W, H = base.size; d = ImageDraw.Draw(base)
box = (int(0.318 * W), int(0.840 * H), int(0.702 * W), int(0.920 * H)); d.rounded_rectangle(box, radius=int(0.022 * H), fill="#111111")
f = ImageFont.truetype(f"{R}/assets/fonts/Montserrat.ttf", int(0.052 * H))
try: f.set_variation_by_axes([800])
except Exception: pass
tw = d.textlength("-50%", font=f); d.text(((box[0] + box[2]) / 2 - tw / 2, box[1] + (box[3] - box[1]) * 0.17), "-50%", font=f, fill="#FFFFFF")
out = nxt(2); base.save(out, "PNG")
open(f"{B}/calls.jsonl", "a").write(json.dumps({"num": 2, "engine": "script", "ok": True, "ts": time.strftime("%Y-%m-%d %H:%M:%S"), "note": "R2: button -50% (B23)"}) + "\n")
print(f"S2: {os.path.basename(out)} — button -50%")
print("S4: unchanged (no product in the template, C7)")
