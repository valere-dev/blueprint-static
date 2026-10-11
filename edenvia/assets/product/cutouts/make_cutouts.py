#!/usr/bin/env python3
"""Build the product cutouts from the founder's photo library (rule C23): the pouch cut from the photo whose light and hold match the slot,
droplets kept. rembg BiRefNet-general for the pouch; the hand is recovered by a skin-colour mask (BiRefNet drops it) and cut at the wrist.
Outputs (RGBA PNG) in this folder + a *_check.jpg (on black | on white) for QC:
  pouch-standing-studio.png   from library/studio_pouch-ice-bowl-glass-straw-v2.png   (front-on, droplets, stands on a surface)
  pouch-held-hand-kitchen.png from library/hand_pouch-kitchen.jpg                      (upright pouch held in a hand, daylight)
  tablets-flatlay.png         from library/flatlay_pouch-tablets-drops.png             (nine tablets + drops)
usage: python3 make_cutouts.py   (≈1 min on CPU; models cached in ~/.rembg)"""
import os, numpy as np
from PIL import Image, ImageFilter
from rembg import remove, new_session
HERE = os.path.dirname(os.path.abspath(__file__)); LIB = os.path.join(os.path.dirname(HERE), "library")
sess = new_session("birefnet-general")

def feather(im, px=1):
    a = im.getchannel("A").filter(ImageFilter.GaussianBlur(px)); im.putalpha(a); return im

def trim(im):
    return im.crop(im.getchannel("A").getbbox())

def check(im, name):
    w, h = im.size; c = Image.new("RGB", (w * 2 + 20, h), (128, 128, 128))
    for i, col in enumerate([(0, 0, 0, 255), (255, 255, 255, 255)]):
        bg = Image.new("RGBA", im.size, col); bg.alpha_composite(im); c.paste(bg.convert("RGB"), (i * (w + 20), 0))
    c.thumbnail((1600, 1000)); c.save(os.path.join(HERE, name + "_check.jpg"), quality=85)

# 1. standing pouch (studio)
src = Image.open(f"{LIB}/studio_pouch-ice-bowl-glass-straw-v2.png").convert("RGB").crop((640, 560, 1320, 1560))
out = remove(src, session=sess); a = np.asarray(out.getchannel("A"), dtype=np.uint8).copy()
# BiRefNet stops ~40 px above the slab: extend the pouch straight down to the slab line (y 885 of the crop) within the pouch's own width
ref = a[800]; xs = np.where(ref > 128)[0]
if len(xs): a[800:886, xs.min():xs.max() + 1] = np.maximum(a[800:886, xs.min():xs.max() + 1], 255)
out.putalpha(Image.fromarray(a)); out = trim(feather(out)); out.save(f"{HERE}/pouch-standing-studio.png"); check(out, "pouch-standing-studio"); print("standing", out.size)

# 2. held pouch with the hand (kitchen): BiRefNet pouch mask ∪ skin mask, cut at the wrist
src = Image.open(f"{LIB}/hand_pouch-kitchen.jpg").convert("RGB").crop((520, 340, 1200, 1230))
pouch = remove(src, session=sess); a_p = np.asarray(pouch.getchannel("A"), dtype=np.uint8)
hsv = np.asarray(src.convert("HSV"), dtype=np.int16); H, S, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]
skin = ((H < 32) | (H > 230)) & (S > 35) & (V > 40)             # warm hue, saturated enough: the hand (shadowed skin included), not the white kitchen
skin[:, :] &= np.arange(src.height)[:, None] < 790                 # below ≈ y 790 of the crop = the sleeve/wrist → dropped
skin[:420, :95] = False                                            # the cabinet handle at the far left matched the skin hue → dropped
skin_img = Image.fromarray((skin * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.MinFilter(31))   # closing: fills the shadow holes
skin_img = skin_img.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
alpha = np.maximum(a_p, np.asarray(skin_img, dtype=np.uint8))
held = src.convert("RGBA"); held.putalpha(Image.fromarray(alpha)); held = trim(held)
held.save(f"{HERE}/pouch-held-hand-kitchen.png"); check(held, "pouch-held-hand-kitchen"); print("held", held.size)

# 3. tablets (flat lay)
src = Image.open(f"{LIB}/flatlay_pouch-tablets-drops.png").convert("RGB").crop((1180, 1080, 1960, 1720))
out = trim(feather(remove(src, session=sess))); out.save(f"{HERE}/tablets-flatlay.png"); check(out, "tablets-flatlay"); print("tablets", out.size)
