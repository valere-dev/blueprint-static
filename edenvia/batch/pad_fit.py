#!/usr/bin/env python3
"""D15 finishing without a crop: bring an uncropped OpenAI master (2:3) to the template's format by EXTENDING the background
instead of cutting content. The missing width (4:5, 3:4 from 2:3) or height (9:16 from 2:3) is filled by replicating the edge
rows/columns of the master (flat or gradient backgrounds extend invisibly; never a stretch of the content, never a crop).
Use it when the smart crop of adformat.normalize() would cut text or an element (QC round 1: S1 badge/headline, S4/S10 side text).
usage: pad_fit.py RAW_MASTER TEMPLATE OUT   (e.g. out/_raw/s_01_v2.png templates/… out/s_01_v2.png)
"""
import os, sys
from PIL import Image
sys.path.insert(0, os.environ.get("SKILL", "/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads") + "/scripts")
import adformat

raw, tpl, out = sys.argv[1:4]
im = Image.open(raw).convert("RGB"); W, H = im.size
tw, th = adformat.target_size(*Image.open(tpl).size); r = tw / th
if W / H < r:        # master too tall for the format -> add width (left/right bands)
    nw = round(H * r); pad = nw - W; L = pad // 2; R = pad - L
    canvas = Image.new("RGB", (nw, H))
    canvas.paste(im.crop((0, 0, 1, H)).resize((L, H)), (0, 0)); canvas.paste(im, (L, 0)); canvas.paste(im.crop((W - 1, 0, W, H)).resize((R, H)), (L + W, 0))
    how = f"+{pad}px width"
else:                # master too wide -> add height (top/bottom bands)
    nh = round(W / r); pad = nh - H; T = pad // 2; B = pad - T
    canvas = Image.new("RGB", (W, nh))
    canvas.paste(im.crop((0, 0, W, 1)).resize((W, T)), (0, 0)); canvas.paste(im, (0, T)); canvas.paste(im.crop((0, H - 1, W, H)).resize((W, B)), (0, T + H))
    how = f"+{pad}px height"
canvas.resize((tw, th), Image.LANCZOS).save(out, "PNG")
print(f"{os.path.basename(out)}: {W}x{H} {how} -> {tw}x{th} (edge-extended, no crop)")
