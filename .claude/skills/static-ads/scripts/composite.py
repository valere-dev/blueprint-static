#!/usr/bin/env python3
"""Hybrid compositor: put the REAL product cutout and EXACT text on a generated (or blank) scene.
usage: composite.py IN OUT spec.json
spec = {"rects": [[x0,y0,x1,y1,"#hex"], ...],                       # solid rectangles painted first (fractions of W/H)
        "band": {"y0":0.70,"y1":1.0,"color":"#FFFFFF"},             # optional full-width band
        "texts": [{"y":0.74,"size":0.045,"font":"Montserrat","weight":800,"color":"#111",
                   "runs":[["Seriously man, try X already and ","#111"],["get rid","#3DA63D"],[" of them!","#111"]]}],
        "strikes": [[x0,y0,x1,y1,"#hex"]],                          # strike-through lines (crossed prices)
        "jar":  {"x":0.5,"y":0.88,"h":0.22},                        # product: x = center, y = BOTTOM edge, h = height (fractions)
        "jars": [{...}, {...}]}                                     # extra products; each may set "noshadow": true or "src": other cutout
Full option reference: 2-make/composite.md.

Generic copy of /root/workspace/wh-remix/composite.py (Wildhorn: fonts in wh-remix/fonts, cutout /srv/wildhorn-lp/p6/jar-30.webp).
Changes: fonts dir + cutout from brand.json; optional per-product "src"; text-only specs work unchanged."""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C

F = C.FONTS.rstrip("/") + "/"
JAR = C.PRODUCT_CUTOUT
FONT_FILES = {"Anton": "Anton-Regular.ttf", "Montserrat": "Montserrat.ttf", "Oswald": "Oswald.ttf", "Fredoka": "Fredoka.ttf",
              "DejaVu": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"}   # DejaVu = glyphs like ✓ ✕ → that brand fonts lack
FONT_FILES.update(C.BRAND.get("fonts", {}))   # brand.json may add {"Name": "File.ttf" or "/abs/path.ttf"}


def font(name, px, weight=800):
    _m = FONT_FILES[name]; f = ImageFont.truetype(_m if _m.startswith("/") else F + _m, px)
    try: f.set_variation_by_axes([weight])   # variable fonts (Montserrat, Oswald) take the weight axis
    except Exception: pass
    return f


src, out, spec = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3]))
import adformat   # D15: fit the scene to the ad format first (1080 wide: 1:1, 4:5, 9:16 or the template ratio)
im = Image.open(src).convert("RGBA"); im = adformat.fit(im, adformat.target_size(*(Image.open(spec["template"]).size if spec.get("template") else im.size)))
W, H = im.size; d = ImageDraw.Draw(im)
for r in spec.get("rects", []): d.rectangle([int(r[0]*W), int(r[1]*H), int(r[2]*W), int(r[3]*H)], fill=r[4])
b = spec.get("band")
if b: d.rectangle([0, int(b["y0"]*H), W, int(b["y1"]*H)], fill=b["color"])
for t in spec.get("texts", []):
    if t.get("sunscreen"):   # soft embossed look: text drawn on its own layer, blurred brown drop shadow, slight blur
        layer = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    else:
        layer = None
    f = font(t.get("font", "Montserrat"), int(t["size"]*H), t.get("weight", 800))
    runs = t.get("runs") or [[t["t"], t.get("color", "#000")]]
    # wrap runs into lines within maxw
    maxw = t.get("maxw", 0.9)*W; words = []
    for rr in runs:
        txt, col = rr[0], rr[1]; run_w = rr[2] if len(rr) > 2 else None
        for i, w in enumerate(txt.split(" ")):
            words.append([w, col, run_w])
    lines, cur, cw = [], [], 0
    sp = d.textlength(" ", font=f)
    for w, col, run_w in words:
        if not w: continue
        ww = d.textlength(w, font=f)
        if cur and cw + ww > maxw: lines.append(cur); cur, cw = [], 0
        cur.append((w, col, run_w)); cw += ww + sp
    if cur: lines.append(cur)
    y = int(t["y"]*H); lh = int(t["size"]*H*t.get("lh", 1.18))
    fw = {}

    def fnt(rw):
        k = rw or t.get("weight", 800)
        if k not in fw: fw[k] = font(t.get("font", "Montserrat"), int(t["size"]*H), k)
        return fw[k]
    for ln in lines:
        lw = sum(d.textlength(w, font=fnt(rw)) for w, _, rw in ln) + sp*(len(ln)-1)
        x = (t.get("cx", 0.5)*W - lw/2) if t.get("align", "center") == "center" else t.get("x", 0.05)*W
        if t.get("box"):
            pad = int(t["size"]*H*0.22); asc = f.getbbox("Hg")
            d.rectangle([x-pad, y+asc[1]-pad*0.6, x+lw+pad, y+asc[3]+pad*0.6], fill=t["box"])
        if t.get("shadow"):
            xs = x
            for w, col, rw in ln:
                d.text((xs+3, y+3), w, font=fnt(rw), fill=(0, 0, 0, 140)); xs += d.textlength(w, font=fnt(rw)) + sp
        for w, col, rw in ln:
            d.text((x, y), w, font=fnt(rw), fill=col); x += d.textlength(w, font=fnt(rw)) + sp
        y += lh
    if layer is not None:
        sh = layer.split()[3].filter(ImageFilter.GaussianBlur(4)).point(lambda a: int(a*0.35))
        shadow = Image.new("RGBA", im.size, (60, 30, 10, 0)); shadow.putalpha(sh)
        im = Image.alpha_composite(im, shadow.transform(im.size, Image.AFFINE, (1, 0, -2, 0, 1, -4)))
        im = Image.alpha_composite(im, layer.filter(ImageFilter.GaussianBlur(1.1)))
    d = ImageDraw.Draw(im)
for s_ in spec.get("strikes", []):
    d = ImageDraw.Draw(im); d.line([s_[0]*W, s_[1]*H, s_[2]*W, s_[3]*H], fill=s_[4], width=max(3, int(H*0.006)))
for j in ([spec["jar"]] if spec.get("jar") else []) + spec.get("jars", []):
    if j:
        jar = Image.open(j.get("src", JAR)).convert("RGBA"); jh = int(j["h"]*H); jw = int(jar.width*jh/jar.height)   # C6: real proportions
        jar = jar.resize((jw, jh), Image.LANCZOS)
        x = int(j["x"]*W - jw/2); y = int(j["y"]*H - jh)
        shadow = Image.new("RGBA", im.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(shadow)
        sd.ellipse([x+jw*0.1, y+jh-jh*0.03, x+jw*0.9, y+jh+jh*0.04], fill=(0, 0, 0, 70))   # contact shadow (C10)
        if not j.get("noshadow"): im = Image.alpha_composite(im, shadow)
        im.alpha_composite(jar, (x, y))
im.convert("RGB").save(out, "PNG"); print("ok", out)
