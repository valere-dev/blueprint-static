"""Shared helpers for the page builders (review / final / validated / all-ads / lessons).
The Wildhorn builders read their CSS from /srv/blueprint/batch-04.html; it is embedded here so a new brand needs nothing on /srv.
Pages are written to $SAC_PAGES (default $SAC_WORKDIR/pages). Images: $SAC_PAGES/ex/ (full PNG) and $SAC_PAGES/ex/web/ (webp thumbs).
Serving them (Caddy vhost, noindex header, clean URLs) is a separate, explicit step — see 2-make/review-and-pages.md."""
import glob, os, subprocess, importlib.util, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C

CSS = """:root{--bg:#0F0C0A;--line:#3A322B;--acc:#E0662C;--card:#1A1613}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:#fff;font:16px/1.5 Inter,system-ui,sans-serif}
.wrap{max-width:1400px;margin:0 auto;padding:24px 16px 80px}h1{font:700 42px/1.05 Oswald,sans-serif;text-transform:uppercase;margin:18px 0 6px}
.tabs{display:flex;gap:6px;border-bottom:1px solid var(--line);flex-wrap:wrap;margin-bottom:20px}.tabs a{color:#fff;text-decoration:none;font-weight:700;padding:10px 16px;border-radius:10px 10px 0 0}.tabs a.on{background:var(--acc)}
.row{border-top:2px solid var(--acc);padding:18px 0 30px}.num{font:700 34px Oswald,sans-serif;color:var(--acc);line-height:1;margin-bottom:10px}
.wait{aspect-ratio:1/1;border:1px dashed var(--line);border-radius:10px;display:flex;align-items:center;justify-content:center}
.lb{position:absolute;top:8px;left:8px;font:700 12px Oswald,sans-serif;letter-spacing:1px;text-transform:uppercase;padding:4px 9px;border-radius:5px;background:#3A322B;z-index:2}.lb.a{background:var(--acc)}
.info{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px}.info div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px;font-size:15px}.info b{display:block;color:var(--acc);font-size:13px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px}
details{margin-top:12px;background:#000;border:1px solid var(--line);border-radius:10px;padding:10px 14px}summary{cursor:pointer;font-weight:700}pre{white-space:pre-wrap;font:13px/1.5 ui-monospace,Menlo,monospace;margin:10px 0 0}
@media(max-width:800px){.info{grid-template-columns:1fr 1fr}}.num span{font:600 16px Inter,sans-serif;color:#fff;margin-left:10px}.strip{display:flex;gap:10px;overflow-x:auto;padding-bottom:6px}.strip figure{flex:0 0 min(300px,46vw);margin:0;position:relative}.strip img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#000;border-radius:10px;display:block}
.strip figure.sell img{outline:4px solid var(--acc)}.why{margin:10px 0 0;font-size:14px}.stats{background:var(--card);border:1px solid var(--acc);border-radius:14px;padding:18px;margin:18px 0}.stats td,.stats th{padding:8px;border-bottom:1px solid var(--line);text-align:left}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%}td,th{vertical-align:top}details ul{margin:8px 0;padding-left:20px}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;align-items:start}.g img{width:100%;display:block;border-radius:10px;background:#000}"""
HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow"><title>{title}</title>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Oswald:wght@700&display=swap" rel="stylesheet"><style>{css}</style></head>')
TABS = [("review", "To review"), ("final", "Final — every version"), ("validated", "Validated"), ("lessons", "Rules")]


def tabs(on):
    return '<div class="tabs">' + "".join(f'<a href="{h}"{" class=on" if h == on else ""}>{t}</a>' for h, t in TABS) + "</div>"


def page(title, on, body):
    return HEAD.format(title=title, css=CSS) + f'<body><div class="wrap">{tabs(on)}{body}</div></body></html>'


def load_specs(batch=None):
    """All s*specs.py of the batch, later files override earlier ones (a redo spec replaces the original by num)."""
    batch = batch or C.BATCH; specs = {}
    for f in sorted(glob.glob(f"{batch}/s*specs.py")):
        sp = importlib.util.spec_from_file_location("s", f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
        for s in m.S: specs[s["num"]] = s
    return specs


def load_json(path, default):
    return json.load(open(path)) if os.path.exists(path) else default


def web(src, name):
    """webp thumbnail (900px) for pages; full PNGs stay linked at full resolution."""
    d = f"{C.PAGES}/ex/web"; os.makedirs(d, exist_ok=True); o = f"{d}/{name}.webp"
    if not os.path.exists(o) or os.path.getmtime(o) < os.path.getmtime(src):
        from PIL import Image   # PIL instead of ImageMagick `convert` (not installed on nutraflow1, no root — 2026-10-11)
        im = Image.open(src).convert("RGB"); im.thumbnail((900, 900)); im.save(o, "WEBP", quality=78)
    return f"ex/web/{name}.webp"


def outs_for(key):
    """Every try of an ad, in try order (v1, v2, ...). Try N = file key_vN.png. (The Wildhorn builders sorted by mtime.)"""
    import re
    fs = glob.glob(f"{C.OUT}/{key}_v*.png")
    return sorted(fs, key=lambda f: int(re.search(r"_v(\d+)\.png$", f).group(1)))
