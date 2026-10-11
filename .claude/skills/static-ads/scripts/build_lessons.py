#!/usr/bin/env python3
"""RULES page from a markdown rulebook (default: the skill's 3-improve/rules.md, or $SAC_RULES, e.g. a brand LESSONS.md).
Every '## ' heading = a table; every '- ID · rule · origin' line = a row (the LESSONS.md format).
Rules in 3-improve/rules.md use '### ID — title' blocks instead: those are rendered as rows too.
Writes $SAC_PAGES/lessons.html.
Generic copy of /root/workspace/wh-remix/build_lessons.py (it read LESSONS.md, CSS from /srv/blueprint/protocols.html)."""
import html, re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C
from pages_common import page

SRC = os.environ.get("SAC_RULES", os.path.join(C.SCRIPTS, "..", "3-improve", "rules.md"))
md = open(SRC).read()
body = ""; inlist = False; cur = None


def flush():
    global cur, body
    if cur:
        rid, title, lines = cur
        txt = html.escape(" ".join(l.strip() for l in lines if l.strip()))
        txt = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", txt)
        body += f"<tr><td><b>{html.escape(rid)}</b></td><td><b>{html.escape(title)}</b><br>{txt}</td></tr>"
    cur = None


for line in md.splitlines():
    if line.startswith("# "):
        flush(); body += f"<h1>{html.escape(line[2:])}</h1>"
    elif line.startswith("## "):
        flush()
        if inlist: body += "</table></div></section>"
        body += f'<section><h2>{html.escape(line[3:])}</h2><div class="tw"><table><tr><th>ID</th><th>Rule</th></tr>'; inlist = True
    elif line.startswith("### ") and inlist:
        flush(); m = re.match(r"###\s+(\S+)\s+[—-]\s+(.*)", line)
        cur = (m.group(1), m.group(2), []) if m else (line[4:], "", [])
    elif line.startswith("- ") and inlist and cur is None and " · " in line:
        parts = [p.strip() for p in line[2:].split(" · ")]
        rid, rule, orig = (parts + ["", ""])[:3]
        body += f"<tr><td><b>{html.escape(rid)}</b></td><td>{html.escape(rule)}<br><small>{html.escape(orig)}</small></td></tr>"
    elif cur is not None:
        cur[2].append(line)
    elif line.strip() and not line.startswith("#") and not inlist:
        body += f"<p>{html.escape(line)}</p>"
flush()
if inlist: body += "</table></div></section>"
os.makedirs(C.PAGES, exist_ok=True)
open(f"{C.PAGES}/lessons.html", "w").write(page("Rules", "lessons", body))
print("ok", SRC)
