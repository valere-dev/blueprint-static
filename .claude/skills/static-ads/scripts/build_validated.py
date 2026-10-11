#!/usr/bin/env python3
"""VALIDATED grid: text-free page with the sell version of every ✅ ad (renumbered 01..N in S order) + $SAC_BATCH/validated/<Prefix>_NN.png.
Re-exports every sell version first (sell_override.json applies to validated ads too — A26).
Writes $SAC_PAGES/validated.html (images only: shareable demo link, no templates, no angle names).
Generic copy of /root/workspace/wh-remix/sam-batch/build_validated.py (it patched an existing /srv/blueprint/wildhorn-ads/index.html)."""
import json, os, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C
from pages_common import HEAD, CSS, load_json, outs_for

B = C.BATCH; P = f"{C.PAGES}/validated"; KP = os.environ.get("SAC_KEY_PREFIX", "s")
val = load_json(f"{B}/validated.json", {})
SO = load_json(f"{B}/sell_override.json", {})
os.makedirs(f"{B}/sell", exist_ok=True)
for k in val:
    n = int(k); outs = outs_for(f"{KP}_{n:02d}")
    if outs: shutil.copy(outs[SO.get(k, len(outs)) - 1], f"{B}/sell/{C.FILE_PREFIX}_S{n:02d}.png")
ok = sorted(int(k) for k, v in val.items() if v.startswith("✅") and os.path.exists(f"{B}/sell/{C.FILE_PREFIX}_S{int(k):02d}.png"))
shutil.rmtree(f"{B}/validated", ignore_errors=True); os.makedirs(f"{B}/validated")
shutil.rmtree(P, ignore_errors=True); os.makedirs(P)
for i, n in enumerate(ok, 1):
    src = f"{B}/sell/{C.FILE_PREFIX}_S{n:02d}.png"
    shutil.copy(src, f"{B}/validated/{C.FILE_PREFIX}_{i:02d}.png")
    subprocess.run(["convert", src, "-resize", "1080x1920>", "-quality", "82", f"{P}/{i:02d}.webp"], check=True)
imgs = "".join(f'<a href="validated/{i:02d}.webp" target="_blank"><img src="validated/{i:02d}.webp" loading="lazy" alt=""></a>' for i in range(1, len(ok) + 1))
html = HEAD.format(title=f"{C.NAME} ads", css=CSS) + f'<body><div class="wrap"><h1>{C.NAME} ads <span style="color:var(--acc);font-size:18px">{len(ok)}</span></h1><div class="g">{imgs}</div></div></body></html>'
open(f"{C.PAGES}/validated.html", "w").write(html); print(len(ok), "validated")
