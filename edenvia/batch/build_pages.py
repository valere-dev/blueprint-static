#!/usr/bin/env python3
"""Edenvia — the two founder pages of blueprint step 4 (2-make/review-and-pages.md, "Comparison page and demo link"):
  pages/compare.html  template | our ad, one pair per row, grouped by concept family, angle + headline under each pair (R6)
  pages/demo.html     a grid with ONLY our final images (no templates, no angle names, no technical text)
Sell version = latest try, or sell_override.json. Thumbs: pages/ex/web/*.webp (900 px) linking the full PNG in pages/ex/.
usage: SAC_WORKDIR=<repo>/edenvia python3 build_pages.py
"""
import html, json, os, shutil, sys, re, glob
SKILL = os.environ.get("SKILL", "/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads")
sys.path.insert(0, SKILL + "/scripts")
import sac_config as C
from pages_common import HEAD, CSS, load_specs, load_json, web, outs_for, restyle

B = C.BATCH; EX = f"{C.PAGES}/ex"; os.makedirs(EX, exist_ok=True); KP = os.environ.get("SAC_KEY_PREFIX", "s")
BATCH_T = KP in ("t", "u"); TD = {"t": "templates-T", "u": "templates-U"}.get(KP); PD = {"t": "kie-T", "u": "kie-U"}.get(KP); DIG = 3 if KP == "u" else 2
FAMILY = {1: "US vs THEM / comparison"}            # family per batch round (B01-clone-plan.md §8.1); round 1 = family 1
HEADLINES = {1: "3 Leg-Swelling Fixes. 1 Pair Of Heavy Legs. Here's The Truth.", 2: "Lose The Fluid, Not More Weight.",
             3: "Edenvia's HYDROGEN vs Detox Tea", 4: "What comes with ANOTHER D!ET · What comes with EDENVIA",
             5: "DIETED FOR YEARS: LEGS STILL SWOLLEN? LOOK AT YOUR DRAINAGE.", 6: "Belt Buckle vs. Keg — Guess who's on EDENVIA",
             7: "OLD ME / NEW ME · FOR HEAVY, SWOLLEN LEGS", 8: "Your current leg-swelling routine may be letting you down.",
             9: "HYDROGEN + MAGNESIUM + MINERALS — The Glass That Changes Everything.", 10: "DIETING · DIETING WITH EDENVIA"}
SO = load_json(f"{B}/sell_override.json", {})
if BATCH_T:   # batch T: no specs; one row per template file, caption = the prompt's text line
    specs = []
    for f in sorted(x for x in os.listdir(f"{B}/{TD}") if not x.endswith(".tsv")):
        n = int(f[1:1 + DIG]); pr = open(f"{B}/prompts/{PD}/{KP}_{n:02d}.txt" if KP == "t" else f"{B}/prompts/{PD}/{KP}{n:03d}.txt").read()
        m = re.search(r"Text, exactly and nothing else[^:]*:\s*(.*)", pr, re.S); cap = (m.group(1) if m else pr).replace("\n", " ")[:220]
        specs.append({"num": n, "tpl_abs": f"{B}/{TD}/{f}", "angle": f.split("_")[1], "texts": [cap]})
else:
    specs = sorted(load_specs().values(), key=lambda s: s["num"])
EXTRA = """.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start}.pair figure{margin:0;position:relative}
.pair img{width:100%;display:block;border-radius:10px;background:#000}.cap{margin:10px 0 0;font-size:15px}.cap b{color:var(--acc)}
h2{font:700 24px Oswald,sans-serif;text-transform:uppercase;margin:30px 0 6px}@media(max-width:800px){.pair{grid-template-columns:1fr}}"""

rows = ""; fam_done = set(); sells = []
for s in specs:
    n = s["num"]; key = f"{KP}_{n:0{DIG}d}"; tf = s.get("tpl_abs") or f"{B}/templates/{s['tpl']}"
    outs = outs_for(key)
    if not outs: continue
    sell = outs[SO.get(str(n), len(outs)) - 1]; sells.append((n, sell))
    shutil.copy(sell, f"{EX}/{key}_sell.png")
    fam = ("Batch U — every remaining template of the swipe file (270)" if KP == "u" else "Batch T — 25 templates drawn at random across all 9 families") if BATCH_T else FAMILY.get(1)
    if fam not in fam_done: rows += f'<h2>{html.escape(fam)}</h2>'; fam_done.add(fam)
    rows += (f'<section class="row" id="s{n}"><div class="num">{KP.upper()}{n}</div><div class="pair">'
             f'<figure><span class="lb">Template</span><img src="{web(tf, key + "_tpl")}" loading="lazy"></figure>'
             f'<figure><span class="lb a">Edenvia</span><a href="ex/{key}_sell.png" target="_blank"><img src="{web(sell, key + "_sell")}" loading="lazy"></a></figure></div>'
             f'<p class="cap"><b>{html.escape(s["angle"].split(" — ")[0])}</b> · {html.escape(s["texts"][0] if BATCH_T else HEADLINES.get(n, s["texts"][0]))}</p></section>')
os.makedirs(C.PAGES, exist_ok=True)
head = HEAD.format(title="Edenvia — batch 01, template vs ad", css=CSS + EXTRA)
open(f"{C.PAGES}/compare{"-" + KP.upper() if BATCH_T else ""}.html", "w").write(head + f'<body><div class="wrap"><h1>Edenvia — {"batch " + KP.upper() if BATCH_T else "batch 01"} · template | ad</h1>'
    f'<p>{"Every remaining template of the swipe file" if KP == "u" else "25 random templates across all families" if BATCH_T else "Concept family 1"}, {len(sells)} ads. Left: the template. Right: our ad (click for full size). Angle and headline under each pair.</p>{rows}</div></body></html>')
grid = "".join(f'<a href="ex/{KP}_{n:0{DIG}d}_sell.png" target="_blank"><img src="{web(p, f"{KP}_{n:0{DIG}d}_sell")}" loading="lazy" alt=""></a>' for n, p in sells)
open(f"{C.PAGES}/demo{"-" + KP.upper() if BATCH_T else ""}.html", "w").write(HEAD.format(title="Edenvia ads", css=CSS) + f'<body><div class="wrap"><h1>Edenvia ads</h1><div class="g">{grid}</div></div></body></html>')
restyle()
print(f"compare.html + demo.html: {len(sells)} ads")
