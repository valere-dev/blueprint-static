#!/usr/bin/env python3
"""Nutraflow white restyle of $SAC_PAGES (edenvia/pages): links nutraflow.css + favicons into every page and adds the
Nutraflow brand bar with the site nav. Re-runnable (idempotent): run it after every page (re)build.
Works on any other site served under nutraflow.app too (e.g. output.nutraflow.app): point it at that site's folder; it copies
nutraflow.css, the logo and the favicons there and builds the nav from the folder's own pages.
usage: python3 edenvia/batch/nutraflow_restyle.py [site dir] [--tag "Creative Blueprint · Edenvia"]"""
import glob, os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.normpath(os.path.join(HERE, "..", "pages"))
args = [a for a in sys.argv[1:]]; TAG = "Creative Blueprint · Edenvia"
if "--tag" in args: i = args.index("--tag"); TAG = args[i + 1]; del args[i:i + 2]
P = os.path.abspath(args[0]) if args else SRC
ASSETS = ["nutraflow.css", "nutraflow-logo-dark.png", "favicon-32.png", "favicon-16.png", "apple-touch-icon.png"]
if P != SRC:
    for a in ASSETS: shutil.copy(os.path.join(SRC, a), os.path.join(P, a))
EDENVIA = [("index.html", "Blueprint"), ("review.html", "Review"), ("compare.html", "Template | ad"), ("demo.html", "Demo"),
           ("step1-lymphoria-decode.html", "Step 1 · Decode"), ("step2-gate2-family1.html", "Gate 2 · F1"), ("step2-gate2-family2.html", "Gate 2 · F2")]


def title_of(f):
    m = re.search(r"<title>(.*?)</title>", open(f, encoding="utf-8", errors="replace").read(), re.S)
    return (m.group(1).strip() if m else os.path.basename(f))[:40]


NAV = EDENVIA if P == SRC else [(os.path.basename(f), title_of(f)) for f in sorted(glob.glob(os.path.join(P, "*.html")))]
NAV = NAV[:12]
LINK = ('<link rel="stylesheet" href="nutraflow.css"><link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">'
        '<link rel="icon" type="image/png" sizes="16x16" href="favicon-16.png"><link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">')


def brand(cur):
    nav = "".join(f'<a href="{h}"{" class=on" if h == cur else ""}>{t}</a>' for h, t in NAV)
    return ('<div class="nf-brand"><a href="index.html" title="Nutraflow"><img class="nf-logo" src="nutraflow-logo-dark.png" alt="Nutraflow"></a>'
            f'<span class="nf-divider"></span><span class="nf-tag">{TAG}</span><nav class="nf-nav">{nav}</nav></div>')


def restyle(path):
    h = open(path, encoding="utf-8").read(); cur = os.path.basename(path)
    h = re.sub(r'<div class="nf-brand">.*?</nav></div>', "", h, count=1, flags=re.S)        # drop an old bar (re-run)
    h = h.replace(LINK, "")
    if "</head>" in h: h = h.replace("</head>", LINK + "</head>", 1)
    else: h = h.replace("</style>", "</style>" + LINK, 1)                                   # artifact-style page without <head>
    m = re.search(r"<body[^>]*>", h)
    if m: h = h[:m.end()] + brand(cur) + h[m.end():]
    else: h = re.sub(r"(<header>|<div class=\"wrap\">)", lambda x: brand(cur) + x.group(1), h, count=1)
    open(path, "w", encoding="utf-8").write(h)
    return cur


for f in sorted(glob.glob(os.path.join(P, "*.html"))): print("restyled", restyle(f))
