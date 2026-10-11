#!/usr/bin/env python3
"""ALL-ADS page: several finished sets (e.g. run 1 finals + batch 2 validated) on one images-only page.
usage: build_all.py "Title A=/path/to/folderA" "Title B=/path/to/folderB" ...   (each folder: *.png, sorted by name)
Writes $SAC_PAGES/all-ads/index.html + jpg (1080 wide, click) and webp thumbs.
Generic copy of /root/workspace/wh-remix/build_all.py (Wildhorn: run1-final/Wildhorn_*.png + sam-batch/validated/Wildhorn_*.png -> /srv/blueprint/all-ads)."""
import glob, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C
from pages_common import HEAD, CSS

P = f"{C.PAGES}/all-ads"
SETS = []
for i, arg in enumerate(sys.argv[1:], 1):
    title, folder = arg.split("=", 1)
    SETS.append((f"b{i}", title, sorted(glob.glob(f"{folder}/*.png"))))
if not SETS: sys.exit(__doc__)
body = ""
for d, title, files in SETS:
    os.makedirs(f"{P}/{d}", exist_ok=True)
    for f in glob.glob(f"{P}/{d}/*"): os.remove(f)
    cells = ""
    for i, f in enumerate(files, 1):
        n = f"{i:02d}"
        subprocess.run(["convert", f, "-resize", "1080x1920>", "-quality", "92", f"{P}/{d}/{n}.jpg"], check=True)
        subprocess.run(["convert", f, "-resize", "600x1070>", "-quality", "80", f"{P}/{d}/{n}.webp"], check=True)
        cells += f'<a href="{d}/{n}.jpg" target="_blank"><img src="{d}/{n}.webp" loading="lazy" alt=""></a>'
    body += f'<h2>{title} <span style="color:var(--acc);font-size:16px">{len(files)} ads</span></h2><div class="g">{cells}</div>'
total = sum(len(s[2]) for s in SETS)
html = HEAD.format(title=f"{C.NAME} Ads", css=CSS) + f'<body><div class="wrap"><h1>{C.NAME} ads <span style="color:var(--acc);font-size:18px">{total} ads</span></h1>{body}</div></body></html>'
open(f"{P}/index.html", "w").write(html); print(total, [len(s[2]) for s in SETS])
