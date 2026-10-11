#!/usr/bin/env python3
"""Swap a product in an existing image for the brand's product, touching ONLY a masked box
(gpt-image-2 masked edit on a 4:5 tile around the box, pasted back feathered). Used by the A25 method.
Usage: jarswap.py base.png out.png x0 y0 x1 y1 [--context "extra instruction for this ad"] [--product photo.jpg]
  box = base-image pixels of the product to replace (give a little margin).
Example (Wildhorn S11, where the jar IS the woman's head):
  jarswap.py s_11_base.png s_11_jar.png X0 Y0 X1 Y1 --context "Surreal ad trick: the jar REPLACES the person head and sits directly on the neck, like a head. NO hands, NO fingers, NO hair, NO face anywhere in the masked area; behind the jar only the plain wall of the room."

Generic copy of /root/workspace/wh-remix/jarswap.py: the Wildhorn version hard-coded the jar description and the S11 head
trick in the prompt; here the description comes from brand.json product_lock and the ad-specific trick from --context."""
import sys, io, os, base64, argparse
import requests
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C

p = argparse.ArgumentParser(); p.add_argument("src"); p.add_argument("out"); p.add_argument("box", nargs=4, type=int)
p.add_argument("--context", default=""); p.add_argument("--product", default=C.PRODUCT_PHOTO)
a = p.parse_args()
src, out = a.src, a.out; x0, y0, x1, y1 = a.box
base = Image.open(src).convert("RGB"); BW, BH = base.size
# tile around the box (4:5), clamped to the image
bw, bh = x1 - x0, y1 - y0; th = int(bh * 1.25); tw = int(th * 0.8)
th = min(th, BH); tw = min(tw, BW)
cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
tx0 = max(0, min(BW - tw, cx - tw // 2)); ty0 = max(0, min(BH - th, cy - th // 2))
tile = base.crop((tx0, ty0, tx0 + tw, ty0 + th)).resize((1024, 1280), Image.LANCZOS)
s = 1024 / tw
mask = Image.new("RGBA", (1024, 1280), (0, 0, 0, 255))   # opaque = keep, transparent = edit
ImageDraw.Draw(mask).rectangle([(x0 - tx0) * s, (y0 - ty0) * s, (x1 - tx0) * s, (y1 - ty0) * s], fill=(0, 0, 0, 0))


def png(im):
    b = io.BytesIO(); im.save(b, "PNG"); b.seek(0); return b


prompt = (f"Image 1 is a photo. In the transparent masked area there is a product: replace it with the exact {C.PRODUCT_NOUN} from Image 2 "
          f"({C.PRODUCT_LOCK}). Same position, same size, same slight tilt, same lighting and grain as the photo. "
          + (a.context.strip() + " " if a.context else "") + "Change nothing outside the mask.")
key = C.key(C.OPENAI_KEY_FILE)
ext = os.path.splitext(a.product)[1].lower()
r = requests.post("https://api.openai.com/v1/images/edits", headers={"Authorization": f"Bearer {key}"},
                  data={"model": "gpt-image-2", "prompt": prompt, "quality": "high", "size": "1024x1280"},
                  files=[("image[]", ("tile.png", png(tile), "image/png")),
                         ("image[]", ("product" + ext, open(a.product, "rb"), "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png")),
                         ("mask", ("mask.png", png(mask), "image/png"))], timeout=600)
if r.status_code != 200: sys.exit(f"ERREUR {r.status_code}: {r.text[:500]}")
ed = Image.open(io.BytesIO(base64.b64decode(r.json()["data"][0]["b64_json"]))).convert("RGB").resize((tw, th), Image.LANCZOS)
# paste back only the box, feathered
m = Image.new("L", (tw, th), 0); pad = 6
ImageDraw.Draw(m).rectangle([x0 - tx0 - pad, y0 - ty0 - pad, x1 - tx0 + pad, y1 - ty0 + pad], fill=255)
m = m.filter(ImageFilter.GaussianBlur(8))
base.paste(ed, (tx0, ty0), m); base.save(out); print("ok", out)
