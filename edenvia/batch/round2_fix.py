#!/usr/bin/env python3
"""Round 2 QC fixes (after round2.py): S1 pouch too big for the gold column, S8 counter patch visible, S10 held cutout misplaced.
S1: the old product area is filled with the surrounding navy, then the studio pouch at the column's size (bigger than the old, inside the frame).
S8: the old AI pouch is removed by a masked gpt-image-2 edit (empty counter, no product in the prompt — 1 API call), then the studio cutout.
S10: the studio pouch at the illustrated pouch's exact slot, the T-shirt filled behind it, and HER OWN illustrated fingers re-overlaid on top
     (skin-colour mask of the frozen pixels, D21) so the gesture stays (A8). The library hand cutout exists for the founder's call (C23)."""
import base64, glob, io, json, os, subprocess, sys, time
import numpy as np, requests
from PIL import Image, ImageDraw, ImageFilter
R = "/home/adanalysis/workspace/blueprint-static/edenvia"; SKILL = "/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads"
OUT = f"{R}/out"; B = f"{R}/batch"; T = f"{B}/templates"; STAND = f"{R}/assets/product/cutouts/pouch-standing-studio.png"
sys.path.insert(0, SKILL + "/scripts"); import sac_config as C

def nxt(n): return f"{OUT}/s_{n:02d}_v{len(glob.glob(f'{OUT}/s_{n:02d}_v*.png')) + 1}.png"
def log(n, eng, note): open(f"{B}/calls.jsonl", "a").write(json.dumps({"num": n, "engine": eng, "ok": True, "ts": time.strftime("%Y-%m-%d %H:%M:%S"), "note": "R2 fix: " + note}) + "\n")
def comp(n, base, spec):
    out = nxt(n); cj = f"{B}/prompts/s_{n:02d}_r2fix.json"; json.dump(spec, open(cj, "w"))
    subprocess.run(["python3", f"{SKILL}/scripts/composite.py", base, out, cj], check=True, capture_output=True); return out

# ---- S1: base = v2 (round-1 sell). Old pouch x 0.68–0.92, y 0.27–0.52; frame x 0.655–0.965, label 'EDENVIA' at y 0.248.
im = Image.open(f"{OUT}/s_01_v2.png").convert("RGB"); W, H = im.size
navy = im.getpixel((int(0.70 * W), int(0.60 * H))); ImageDraw.Draw(im).rectangle([int(0.672 * W), int(0.262 * H), int(0.93 * W), int(0.528 * H)], fill=navy)
tmp = f"{B}/prompts/s_01_r2fix_base.png"; im.save(tmp)
out = comp(1, tmp, {"template": f"{T}/10-11_c0021_PrimalEdgeBison.webp", "jar": {"x": 0.80, "y": 0.52, "h": 0.258, "src": STAND}}); log(1, "script", "studio pouch sized to the column"); print("S1", os.path.basename(out))

# ---- S8: base = v2. Masked edit of the old pouch box (x 0.13–0.51, y 0.54–0.86 of 1080x1446) → empty counter; then the studio cutout.
base = Image.open(f"{OUT}/s_08_v2.png").convert("RGB"); BW, BH = base.size
x0, y0, x1, y1 = int(0.125 * BW), int(0.535 * BH), int(0.515 * BW), int(0.862 * BH)
bw, bh = x1 - x0, y1 - y0; th = min(int(bh * 1.25), BH); tw = min(int(th * 0.8), BW); cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
tx0 = max(0, min(BW - tw, cx - tw // 2)); ty0 = max(0, min(BH - th, cy - th // 2))
tile = base.crop((tx0, ty0, tx0 + tw, ty0 + th)).resize((1024, 1280), Image.LANCZOS); s = 1024 / tw
mask = Image.new("RGBA", (1024, 1280), (0, 0, 0, 255)); ImageDraw.Draw(mask).rectangle([(x0 - tx0) * s, (y0 - ty0) * s, (x1 - tx0) * s, (y1 - ty0) * s], fill=(0, 0, 0, 0))
def png(i): b = io.BytesIO(); i.save(b, "PNG"); b.seek(0); return b
prompt = ("Photo of a kitchen counter. In the transparent masked area there is a product pouch: REMOVE it completely and show what is behind it — the white subway-tile wall continuing with the same grout lines, "
          "and the white marble counter continuing with the same reflections and morning light. Empty counter, no product, no object, no text. Change nothing outside the mask.")
r = requests.post("https://api.openai.com/v1/images/edits", headers={"Authorization": f"Bearer {C.key(C.OPENAI_KEY_FILE)}"},
                  data={"model": "gpt-image-2", "prompt": prompt, "quality": "high", "size": "1024x1280"},
                  files=[("image[]", ("tile.png", png(tile), "image/png")), ("mask", ("mask.png", png(mask), "image/png"))], timeout=600)
if r.status_code != 200: sys.exit(f"ERREUR {r.status_code}: {r.text[:400]}")
ed = Image.open(io.BytesIO(base64.b64decode(r.json()["data"][0]["b64_json"]))).convert("RGB").resize((tw, th), Image.LANCZOS)
m = Image.new("L", (tw, th), 0); ImageDraw.Draw(m).rectangle([x0 - tx0 - 6, y0 - ty0 - 6, x1 - tx0 + 6, y1 - ty0 + 6], fill=255); m = m.filter(ImageFilter.GaussianBlur(8))
base.paste(ed, (tx0, ty0), m); tmp = f"{B}/prompts/s_08_r2fix_base.png"; base.save(tmp); log(8, "openai", "masked edit: old pouch removed from the counter")
out = comp(8, tmp, {"template": f"{T}/10-11_c0259_GoliAshwagandha.webp", "jar": {"x": 0.32, "y": 0.85, "h": 0.33, "src": STAND}}); log(8, "script", "studio pouch on the cleaned counter"); print("S8", os.path.basename(out))

# ---- S10: base = v2. Old illustrated pouch x 0.615–0.975, y 0.512–0.742 (1080x1920); hands wrap its lower corners.
base = Image.open(f"{OUT}/s_10_v2.png").convert("RGB"); W, H = base.size; orig = base.copy()
bx = (int(0.612 * W), int(0.505 * H), int(0.978 * W), int(0.745 * H))
shirt = base.getpixel((int(0.60 * W), int(0.62 * H))); ImageDraw.Draw(base).rectangle(bx, fill=shirt)
tmp = f"{B}/prompts/s_10_r2fix_base.png"; base.save(tmp)
mid = comp(10, tmp, {"template": f"{T}/10-11_c0376_MarsMen.webp", "jar": {"x": 0.795, "y": 0.742, "h": 0.236, "src": STAND, "noshadow": True}})
res = Image.open(mid).convert("RGB")
# her own fingers back on top: skin-coloured pixels of the frozen base inside the old pouch box (+ margin)
reg = (bx[0] - 30, bx[1], bx[2] + 30, bx[3] + 40); crop = orig.crop(reg); hsv = np.asarray(crop.convert("HSV"), dtype=np.int16)
skin = ((hsv[..., 0] < 30) | (hsv[..., 0] > 235)) & (hsv[..., 1] > 40) & (hsv[..., 2] > 60)
sm = Image.fromarray((skin * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.MinFilter(7)).filter(ImageFilter.GaussianBlur(1))
res.paste(crop, reg[:2], sm); res.save(mid); log(10, "script", "studio pouch in her hands, illustrated fingers re-overlaid (D21/A8)"); print("S10", os.path.basename(mid))
