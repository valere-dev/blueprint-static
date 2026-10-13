#!/usr/bin/env python3
"""Build the kgen job list for batch U: one line per template whose prompt exists. Image 2 = studio pouch unless the prompt says 'No product'."""
import os,sys
from PIL import Image
R="/home/adanalysis/workspace/blueprint-static/edenvia"; T=f"{R}/batch/templates-U"; P=f"{R}/batch/prompts/kie-U"
STUDIO=f"{R}/assets/product/library/studio_pouch-ice-bowl-glass-straw-v2.png"
def asp(w,h):
    r=w/h; return min([('1:1',1),('4:5',0.8),('9:16',9/16),('2:3',2/3),('3:2',1.5),('16:9',16/9)],key=lambda a:abs(a[1]-r))[0]
done={f.split('_v')[0] for f in os.listdir(f"{R}/out") if f.startswith('u_')}
for f in sorted(x for x in os.listdir(T) if not x.endswith('.tsv')):
    n=int(f[1:4]); pr=f"{P}/u{n:03d}.txt"
    if not os.path.exists(pr) or f"u_{n:03d}" in done: continue
    im=Image.open(f"{T}/{f}"); refs=f"{T}/{f}" + ('' if 'No product' in open(pr).read() else f" {STUDIO}")
    print(f"{n} {pr} {refs} --aspect {asp(*im.size)} --prefix u")
