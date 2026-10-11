#!/usr/bin/env python3
"""Batch pipeline: LINT (blocking) -> engine chain -> composite. Logs every call for the hit-rate.
usage: srun.py SPECFILE NUM

Generic copy of /root/workspace/wh-remix/sam-batch/srun.py (Wildhorn Sam batch).
Paths come from sac_config (SAC_WORKDIR / SAC_BATCH / BRAND_JSON).  Outputs: $SAC_WORKDIR/out/<prefix>_NN_vK.png
Engines: openai | pure_comp | seedream_comp   (seedream_full exists only for history; lint bans it, D7).
"""
import json, glob, os, sys, subprocess, importlib.util, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C
from lint import lint
import adformat, atexit   # D15 output format

S_DIR = C.SCRIPTS; W = C.WORKDIR; B = C.BATCH; OUT = C.ensure_out()
os.makedirs(f"{B}/prompts", exist_ok=True)
KEY_PREFIX = os.environ.get("SAC_KEY_PREFIX", "s")      # output names: s_01_v1.png ...
sp = importlib.util.spec_from_file_location("s", sys.argv[1]); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
errs = lint(m.S)
if errs: print("LINT FAILED — nothing sent:\n" + "\n".join(errs)); sys.exit(1)

# LOCK + CONS = the two fixed prompt blocks (verbatim Wildhorn originals are quoted in 2-make/engines.md).
LOCK = (f"IMAGE 1 = product reference: {C.PRODUCT_LOCK} Real proportions, real 3D object with contact shadow and the scene's light.\n"
        "IMAGE 2 = the template ad to clone 1:1: same layout, composition, render style, palette, typography treatment, spacing and the SAME AMOUNT OF TEXT.")
CONS = ("USE CASE + CONSTRAINTS: Meta ad in the TEMPLATE'S OWN FORMAT (D15: a square stays 1:1, 4:5 stays 4:5, a 9:16 Story stays 9:16), agency-grade; keep the template's spacing between text blocks. Render ONLY the listed text, spelled exactly, once — nothing added. "
        f"Nothing from the template's product world may remain (product, brand, logo, flavor, packaging). Anatomically correct, adults over 25. CRITICAL: the {C.NAME} {C.PRODUCT_NOUN}, when present, is an exact replica of Image 1.")
if C.BRAND.get("lock_extra"): CONS += " " + C.BRAND["lock_extra"]    # e.g. D8: any brand mark outside the label = icon only
CALLS = f"{B}/calls.jsonl"


def log_call(n, engine, ok):
    with open(CALLS, "a") as f:
        f.write(json.dumps({"num": n, "engine": engine, "ok": ok, "ts": time.strftime("%Y-%m-%d %H:%M:%S")}) + "\n")


def out_next(key):
    k0 = len(glob.glob(f"{OUT}/{key}_v*.png")); return f"{OUT}/{key}_v{k0+1}.png"


def comp(src, key, spec):
    spec = dict(spec, template=tf)   # D15: composite in the template format
    cj = f"{B}/prompts/{key}_comp.json"; json.dump(spec, open(cj, "w"))
    subprocess.run(["python3", f"{S_DIR}/composite.py", src, out_next(key), cj], check=True)


n = int(sys.argv[2]); s = next(x for x in m.S if x["num"] == n); key = f"{KEY_PREFIX}_{n:02d}"
tf = s.get("tpl_abs") or f"{B}/templates/{s['tpl']}"; JAR = C.PRODUCT_PHOTO
txt = "\n".join("- " + t for t in s["texts"])
if not os.path.exists(tf): sys.exit(f"#{n}: D10 TEMPLATE MISSING {tf}")
N0 = len(glob.glob(f"{OUT}/{key}_v*.png"))
from PIL import Image as _Im
FMT = adformat.target_size(*_Im.open(tf).size)          # D15: 1080x1080 / 1080x1350 / 1080x1920 / template ratio at 1080 wide
GEN_SIZE = "1024x1024" if FMT[0] == FMT[1] else ("1536x1024" if FMT[0] > FMT[1] else "1024x1536")
def _d15():   # every file this run created is cropped/resized to the template's format (never stretched)
    for f in sorted(glob.glob(f"{OUT}/{key}_v*.png"), key=os.path.getmtime)[N0:]:
        old, new = adformat.normalize(f, tf)
        if old != new: print(f"#{n}: D15 {os.path.basename(f)} {old[0]}x{old[1]} -> {new[0]}x{new[1]}")
atexit.register(_d15)
inv = "\n".join("- " + x for x in s["inventory"])
full = (f"{LOCK}\n\nPIXEL INVENTORY (KEEP / SWAP — follow exactly):\n{inv}\n\nTEMPLATE DNA: {s['dna']}\nSCENE LOGIC: {s['scene']}\nPRODUCT PLACEMENT (copy the template): {s['placement']}\n\n"
        f"CHANGES (visual): {s['visual']}\n\nTEXT (exactly, nothing else):\n{txt}\n\n{CONS}")
eng = s["engine"]
if eng == "pure_comp":
    from PIL import Image
    bg = f"{B}/prompts/{key}_bg.png"; Image.new("RGB", tuple(s["composite"].get("size", (1024, 1024))), s["composite"]["bg"]).save(bg)
    comp(bg, key, s["composite"]); log_call(n, "script", True); print(f"#{n}: pure composite OK"); sys.exit()
if eng == "openai":
    open(f"{B}/prompts/{key}.txt", "w").write(full)
    r = subprocess.run(["timeout", "600", "python3", f"{S_DIR}/remix.py", key, "--prompt", f"{B}/prompts/{key}.txt", "--concept", tf, "--product", JAR, "--size", GEN_SIZE],
                       capture_output=True, text=True)
    ok = r.returncode == 0 and "ERREUR" not in r.stdout + r.stderr and len(glob.glob(f"{OUT}/{key}_v*.png")) > N0  # D10: OK only if a new file exists
    if not ok and "ERREUR" not in r.stdout + r.stderr: print((r.stderr or r.stdout)[-300:])
    log_call(n, "openai", ok)
    print(f"#{n}: openai {'OK' if ok else 'REFUSED -> ' + s.get('fallback', '')}")
    if ok: sys.exit()
    eng = s.get("fallback", "")
    if eng == "seedream_comp" and not ("sd_prompt" in s and "composite" in s):
        sys.exit(f"#{n}: fallback seedream_comp has no sd_prompt/composite — write them (D6 parity: every KEEP placement) and rerun")
if eng == "seedream_full":   # kept for history only: lint blocks it (D7 — garbles labels, writes prompt words)
    sys.exit(f"#{n}: D7 seedream_full is banned")
if eng == "seedream_comp":
    open(f"{B}/prompts/{key}_sd.txt", "w").write(s["sd_prompt"])
    args = ["timeout", "700", "python3", f"{S_DIR}/kie_gen.py", f"{key}_sd", "--prompt", f"{B}/prompts/{key}_sd.txt", "--product", tf, "--model", "seedream"]
    if s.get("aspect"): args += ["--aspect", s["aspect"]]          # A25: keep the template's ratio (e.g. portrait_16_9)
    n_sd = len(glob.glob(f"{OUT}/{key}_sd_v*.png"))
    r = subprocess.run(args, capture_output=True, text=True)
    ok = "ERREUR" not in r.stdout + r.stderr and len(glob.glob(f"{OUT}/{key}_sd_v*.png")) > n_sd; log_call(n, "seedream", ok)
    if ok:
        f = sorted(glob.glob(f"{OUT}/{key}_sd_v*.png"), key=os.path.getmtime)[-1]; comp(f, key, s["composite"])
    else:
        print((r.stderr or r.stdout)[-300:])
    print(f"#{n}: seedream+comp {'OK' if ok else 'FAILED'}")
