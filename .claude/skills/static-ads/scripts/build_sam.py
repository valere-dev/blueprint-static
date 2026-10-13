#!/usr/bin/env python3
"""REVIEW page: only the ads still to review (validated ones hidden), each with template + every try + decode + inventory + prompt,
plus the hit-rate table (this batch vs an optional baseline). Writes $SAC_PAGES/review.html.
Generic copy of /root/workspace/wh-remix/sam-batch/build_sam.py (it wrote /srv/blueprint/sam.html and patched tabs into every page)."""
import json, os, html, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C
from pages_common import page, load_specs, load_json, web, outs_for, restyle

B = C.BATCH; EX = f"{C.PAGES}/ex"; os.makedirs(EX, exist_ok=True)
KP = os.environ.get("SAC_KEY_PREFIX", "s")
specs = sorted(load_specs().values(), key=lambda s: s["num"])
base = load_json(os.environ.get("SAC_BASELINE", f"{C.WORKDIR}/stats_baseline.json"), None)   # optional: previous run's stats.py output
calls = [json.loads(l) for l in open(f"{B}/calls.jsonl")] if os.path.exists(f"{B}/calls.jsonl") else []
val = load_json(f"{B}/validated.json", {})
rows = ""; done = 0
for s in specs:
    n = s["num"]; key = f"{KP}_{n:02d}"; tf = s.get("tpl_abs") or f"{B}/templates/{s['tpl']}"
    if val.get(str(n), "").startswith("✅"): continue  # validated ads never shown again (D3)
    outs = outs_for(key); done += bool(outs)
    figs = f'<figure><span class="lb">Template</span><img src="{web(tf, key + "_tpl")}" loading="lazy"></figure>' if os.path.exists(tf) else ""
    for i, o in enumerate(outs, 1):
        shutil.copy(o, f"{EX}/{key}_v{i}.png")
        lab = "Try " + str(i) + (" (current)" if i == len(outs) else "")
        figs += f'<figure><span class="lb {"a" if i == len(outs) else ""}">{lab}</span><a href="ex/{key}_v{i}.png" target="_blank"><img src="{web(o, key + "_v" + str(i))}" loading="lazy"></a></figure>'
    if not outs: figs += '<figure><span class="lb a">Try 1</span><div class="wait">Generating…</div></figure>'
    st = val.get(str(n), "⏳ To review")
    pf = f"{B}/prompts/{key}.txt"
    rows += (f'<section class="row" id="s{n}"><div class="num">S{n} <span>{html.escape(st)}</span></div><div class="strip">{figs}</div>'
             f'<div class="info"><div><b>Why it works</b>{html.escape(s["why"])}</div><div><b>Template DNA</b>{html.escape(s["dna"])}</div>'
             f'<div><b>Scene & placement</b>{html.escape(s["scene"])}<br>{html.escape(s["placement"])}</div><div><b>Text</b>{"<br>".join(html.escape(t) for t in s["texts"])}</div></div>'
             f'<details><summary>Pixel inventory (KEEP / SWAP)</summary><ul>{"".join("<li>" + html.escape(x) + "</li>" for x in s["inventory"])}</ul></details>'
             f'<details><summary>Backend prompt</summary><pre>{html.escape(open(pf).read() if os.path.exists(pf) else "Rendered by script (exact typography).")}</pre></details></section>')
validated = [k for k, v in val.items() if v.startswith("✅")]
first = [k for k, v in val.items() if v.startswith("✅") and "first try" in v.lower()]
hr = f"{round(100*len(validated)/max(1,len(calls)),1)} %" if val else "waiting for review"
ft = f"{round(100*len(first)/max(1,len(val)),1)} %" if val else "waiting for review"
bcol = lambda k, suf="": (f"{base[k]}{suf}" if base and k in base else "—")
stats = f"""<section class="stats"><h2>Hit rate</h2><div class="tw"><table>
<tr><th></th><th>Baseline</th><th>This batch (so far)</th></tr>
<tr><td>Image generations</td><td>{bcol('generations')}</td><td>{len(calls)}</td></tr>
<tr><td>Generations per validated ad</td><td>{bcol('gens_per_validated')}</td><td>{round(len(calls)/max(1,len(validated)),2) if validated else '—'}</td></tr>
<tr><td><b>Hit rate</b> (validated ads ÷ generations)</td><td>{bcol('hit_rate_pct', ' %')}</td><td><b>{hr}</b></td></tr>
<tr><td><b>Validated on the first try</b> (of reviewed)</td><td>{bcol('first_try_pct', ' %')}</td><td><b>{ft}</b></td></tr></table></div></section>"""
body = (f"<h1>{html.escape(C.NAME)} — to review</h1><p>Every ad built with the full rulebook (3-improve/rules.md) and the pixel inventory (A13). "
        f"{done}/{len(specs)} generated. Validated ads are hidden. Record a Loom ad by ad (say the S number).</p>{stats}{rows}")
os.makedirs(C.PAGES, exist_ok=True)
open(f"{C.PAGES}/review.html", "w").write(page(f"{C.NAME} review", "review", body)); restyle()
print(done, len(specs), len(calls))
