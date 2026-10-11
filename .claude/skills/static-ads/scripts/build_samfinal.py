#!/usr/bin/env python3
"""FINAL page: every ad, template + every try + the SELL VERSION (orange frame) and stats; exports sell versions to $SAC_BATCH/sell/.
Sell version = sell_override.json[num] (1-based try index) if present, else the latest try (A20 frozen try / A26 latest verdict wins).
Writes $SAC_PAGES/final.html.
Generic copy of /root/workspace/wh-remix/sam-batch/build_samfinal.py.  Fix vs original: the original skipped validated ads
('SKIP_VALIDATED' line) although its title says 'all ads, every version'; here SAC_FINAL_ALL=1 (default) shows them all."""
import json, os, html, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C
from pages_common import page, load_specs, load_json, web, outs_for

B = C.BATCH; EX = f"{C.PAGES}/ex"; os.makedirs(EX, exist_ok=True); os.makedirs(f"{B}/sell", exist_ok=True)
KP = os.environ.get("SAC_KEY_PREFIX", "s"); SHOW_ALL = os.environ.get("SAC_FINAL_ALL", "1") == "1"
specs = load_specs()
val = load_json(f"{B}/validated.json", {})
calls = [json.loads(l) for l in open(f"{B}/calls.jsonl")] if os.path.exists(f"{B}/calls.jsonl") else []
SELL_OVERRIDE = load_json(f"{B}/sell_override.json", {})
rows = ""
for n in sorted(specs):
    s = specs[n]; key = f"{KP}_{n:02d}"; tf = s.get("tpl_abs") or f"{B}/templates/{s['tpl']}"
    outs = outs_for(key)
    if not outs: continue
    if not SHOW_ALL and val.get(str(n), "").startswith("✅"): continue
    sell_i = SELL_OVERRIDE.get(str(n), len(outs))
    sell = outs[sell_i - 1]; shutil.copy(sell, f"{B}/sell/{C.FILE_PREFIX}_S{n:02d}.png")
    figs = f'<figure><span class="lb">Template</span><img src="{web(tf, key + "_tpl")}" loading="lazy"></figure>' if os.path.exists(tf) else ""
    for i, o in enumerate(outs, 1):
        shutil.copy(o, f"{EX}/{key}_v{i}.png")
        is_sell = (i == sell_i)
        figs += (f'<figure class="{"sell" if is_sell else ""}"><span class="lb {"a" if is_sell else ""}">{"SELL VERSION" if is_sell else "Try " + str(i)}</span>'
                 f'<a href="ex/{key}_v{i}.png" target="_blank"><img src="{web(o, key + "_v" + str(i))}" loading="lazy"></a></figure>')
    st = val.get(str(n), "⏳ To review")
    rows += f'<section class="row" id="s{n}"><div class="num">S{n} <span>{html.escape(st)}</span></div><div class="strip">{figs}</div><p class="why">{html.escape(s["why"])}</p></section>'
ok = [k for k, v in val.items() if v.startswith("✅")]
first = [k for k, v in val.items() if v.startswith("✅") and "first try" in v.lower()]
stats = f"""<section class="stats"><h2>Hit rate</h2><div class="tw"><table><tr><th></th><th>This batch</th></tr>
<tr><td>Generations</td><td>{len(calls)}</td></tr>
<tr><td>Validated on the first try (of reviewed)</td><td>{len(first)}/{len(val)} = {round(100*len(first)/max(1,len(val)),1)} %</td></tr>
<tr><td>Validated so far</td><td>{len(ok)}/{len(specs)}</td></tr>
<tr><td>Generations per validated ad</td><td>{round(len(calls)/max(1,len(ok)),2) if ok else '—'}</td></tr></table></div></section>"""
body = (f"<h1>{html.escape(C.NAME)} — all {len(specs)} ads, every version</h1><p>Each row: the template, every try, and the <b>SELL VERSION</b> "
        f"(orange frame) = the one to launch. Sell PNGs: <code>{html.escape(B)}/sell/</code>.</p>{stats}{rows}")
open(f"{C.PAGES}/final.html", "w").write(page(f"{C.NAME} final", "final", body))
print(len(specs), "ads", len(calls), "calls", len(ok), "ok of", len(val))
