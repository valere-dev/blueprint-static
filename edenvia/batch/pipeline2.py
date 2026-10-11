#!/usr/bin/env python3
"""Pipeline v2 (after Loom 2, 2026-10-11): analyse → prompt (JSON) → text validator → kie generation → vision QC → auto-redo.
usage: pipeline2.py NUM [NUM ...] [--prefix u] [--force]      (NUM = template numbers of batch U; --force rewrites the prompt)
       pipeline2.py --qc NUM [NUM ...]                       (vision QC only on the existing sell version; prints verdicts)
Refs on every call: template + studio pouch + official logo (+ rival asset when the template compares two products).
Costs: prompt ≈ 3k tokens gpt-5.4-mini; QC ≈ 2k tokens; image 6 kie credits. Logs: batch/pipeline2.log.jsonl"""
import base64, glob, json, os, re, shutil, subprocess, sys, time
from openai import OpenAI
R = "/home/adanalysis/workspace/blueprint-static/edenvia"; B = f"{R}/batch"; SKILL = "/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads"
sys.path.insert(0, SKILL + "/scripts"); import sac_config as C
client = OpenAI(api_key=C.key(C.OPENAI_KEY_FILE)); MODEL = "gpt-5.4-mini"
STUDIO = f"{R}/assets/product/library/studio_pouch-ice-bowl-glass-straw-v2.png"; LOGO = f"{R}/assets/logo/edenvia-logo-blue-nobg.png"
RIVAL = {k: f"{R}/assets/product/rival/{k}.png" for k in ("pills", "gummies", "drops")}
BRIEF = open(f"{B}/BRIEF-for-prompts.md").read()
PRICES = {"$39.00", "$79.99", "$78.00", "$239.97", "$117.00", "$399.95", "-50%", "50%"}
NICHE = r"\b(hair|chin|gut|sugar|sugars|collagen|biotin|acne|app|snack|protein|caffeine|coffee|creatine|menopause|parasite|parasites|testosterone|libido|sleep|focus|dopamine|vape|vapes|skin|wrinkle|wrinkles|teeth|breath|energy drink|fiber|fibre|shilajit|boron|zinc|tongkat|ashwagandha|taurine|vitamin)\b"
LOG = f"{B}/pipeline2.log.jsonl"

SYS = f"""You write ONE gpt-image-2 prompt that clones a Meta static ad template for Edenvia. Answer in JSON only:
{{"analysis": "<format, family, mechanism, and the ROLE of each zone: rival/ours, before/after, pain/desire>",
 "needs_rival": "pills"|"gummies"|"drops"|"none",   // "none" unless the template compares two products or an old routine vs ours
 "template_lines": ["<every text line of the template, verbatim>"],
 "our_lines": ["<every text line of OUR ad, same count and order, rewritten for the avatar>"],
 "prompt": "<the full prompt>"}}
{BRIEF}
HARD RULES (each one cost a rejected ad):
1. COMPARISON templates (us vs them, old me / new me, before / after a product, X vs Y, 'other brands'): the LEFT/old/bad side shows the RIVAL product (Image 4, a generic unbranded bottle) and what the avatar SUFFERS (heavy legs by 5 p.m., sock marks, bathroom runs, pricier, nothing changes); the RIGHT/new/good side shows the Edenvia pouch and what she WANTS (lighter legs by evening, slimmer ankles, boots zip, one glass a day, cheaper). Edenvia is NEVER on the losing side. Never the same product on both sides.
2. The pouch is ONLY the one in Image 2 (studio photo) — never another sachet, bottle or design. The logo outside the label is ONLY the file in Image 3 (the word Edenvia with the atom icon). Never invent a logo, badge or certification mark.
3. EVERY text line is rewritten for the avatar. No line of the template survives unchanged, no word of another niche (hair, chin, gut, sugar, collagen, biotin, acne, app, snack, protein, sleep, focus…). Headline always names heavy, swollen legs / puffiness / water retention (or the sub-angle).
4. SELL, don't describe: action verbs (drains, flushes, triggers), urgency, the avatar's desire — never "helps support"; our list of benefits is at least as long as the template's. Features of the template's product (ingredients, dosages) become OUR benefits; the only ingredients ever named: hydrogen, magnesium, minerals.
5. Offers: only the allowed prices/percentages; a discount code becomes a discount, a price or a benefit; a free-month or gift offer becomes "FREE Cellular Recovery Protocol". Year = 2026.
6. Organic / UGC templates (screenshot, phone photo, note, tweet) stay organic: same raw look, no studio product added unless the template shows one.
PROMPT FORMAT: start with "Image 1 is the ad template to clone 1:1 (same layout, composition, render style, fonts, text sizes and positions, same amount of text)." then "Image 2 is our product: the Edenvia Molecular Hydrogen pouch — reproduce it exactly — the label reads GENERATES 8PPM OF HYDROGEN PER TABLET (the digit is 8, not 6) — label readable, water droplets, lit by the scene. Image 3 is the official Edenvia logo: use it wherever the template shows a brand logo, never redraw it." (+ "Image 4 is the rival product for the losing side." when needs_rival != none). Then "Changes:" (what is swapped and the role of each zone), then "Text, exactly and nothing else:" with our_lines, then "Do NOT draw:". Under 260 words."""

def b64(p): return "data:image/" + p.rsplit(".", 1)[1].lower().replace("jpg", "jpeg") + ";base64," + base64.b64encode(open(p, "rb").read()).decode()
def log(**kw):
    open(LOG, "a").write(json.dumps(dict(kw, ts=time.strftime("%Y-%m-%d %H:%M:%S")), ensure_ascii=False) + "\n"); return True
def tfile(n):
    return next(f for f in glob.glob(f"{B}/templates-U/U{n:03d}_*") if not f.endswith(".tsv"))

def validate(j):
    errs = []
    tl = [re.sub(r"\W+", " ", l).strip().lower() for l in j.get("template_lines", [])]
    for l in j.get("our_lines", []):
        k = re.sub(r"\W+", " ", l).strip().lower()
        if len(k) > 12 and k in tl: errs.append(f"line unchanged from the template: {l!r}")
        for m in re.findall(NICHE, l, re.I): errs.append(f"other-niche word {m!r} in {l!r}")
        for p in re.findall(r"\$\s?\d[\d,]*(?:\.\d\d)?|\b\d{1,2}\s?%", l):
            if p.replace(" ", "") not in PRICES and not re.search(r"\b(8|93|4\.9)\b", p): errs.append(f"offer not allowed: {p!r} in {l!r}")
        if re.search(r"\b(code|coupon|promo)\b", l, re.I): errs.append(f"discount code in {l!r}")
        if re.search(r"\b2025\b", l): errs.append(f"year 2025 in {l!r}")
    if j.get("needs_rival", "none") not in ("none", "pills", "gummies", "drops"): errs.append("needs_rival invalid")
    return errs

def write_prompt(n, force=False):
    out = f"{B}/prompts/kie-U/u{n:03d}.json"
    if os.path.exists(out) and not force: return json.load(open(out))
    t = tfile(n); msgs = [{"role": "system", "content": SYS}, {"role": "user", "content": [{"type": "text", "text": f"Template U{n:03d}. Write the JSON."}, {"type": "image_url", "image_url": {"url": b64(t), "detail": "high"}}]}]
    for attempt in range(3):
        r = client.chat.completions.create(model=MODEL, messages=msgs, response_format={"type": "json_object"})
        j = json.loads(r.choices[0].message.content); errs = validate(j)
        log(num=n, step="prompt", attempt=attempt, errs=errs)
        if not errs: break
        msgs += [{"role": "assistant", "content": json.dumps(j)}, {"role": "user", "content": "Validator errors — fix them all and return the full JSON again:\n- " + "\n- ".join(errs)}]
    j["validator_errors"] = errs; json.dump(j, open(out, "w"), indent=1, ensure_ascii=False); open(f"{B}/prompts/kie-U/u{n:03d}.txt", "w").write(j["prompt"]); return j

QC_SYS = """You are the QC of a Meta static ad for Edenvia, a molecular-hydrogen effervescent tablet sold to women 40-55 with heavy, swollen, puffy legs and ankles (water retention, lymphatic bloating). That IS the niche: text about swollen legs, puffiness, water retention, ankles, drainage is CORRECT. Image 1 = the generated ad, Image 2 = the ONLY correct product (studio pouch), Image 3 = the official logo, Image 4 = the template it clones.
Be LENIENT: reject only on a clear, concrete defect visible in Image 1. These are CORRECT by design, never reject them: a generic unbranded rival bottle/jar ("WATER PILLS", "DETOX GUMMIES", "LYMPH DROPS") on the losing/old side; pain lines on the losing side (heavy by 5 p.m., sock marks, bathroom runs, pricier, nothing changes); a layout re-flowed to fit the format; a logo that is the word Edenvia with an atom icon in blue or white.
Answer in JSON:
{"pouch_ok": bool (false ONLY if an Edenvia pouch has a clearly different design than Image 2: other colours, other shape, a bottle/jar/box, label missing MOLECULAR HYDROGEN, or the digit 6 instead of 8 in 8PPM),
 "logo_ok": bool (false ONLY if there is a standalone brand mark that is NOT 'Edenvia' with an atom icon, e.g. another brand's name, a drawn seal or certification badge),
 "comparison_ok": bool (false ONLY if the ad compares two sides and the Edenvia pouch sits on the losing/old/bad side, or both sides show Edenvia),
 "text_ok": bool (false ONLY if a line is clearly about another niche — hair, skin, gut, sugar, acne, app, snack, protein, sleep, focus — or contains '2025', garbled letters or a different brand name),
 "anatomy_ok": bool (false ONLY on a visible deformity: extra limbs, broken hands, melted faces),
 "layout_ok": bool (false ONLY if text or product is cut by the edge or the image is empty/blank),
 "issues": ["<one short actionable line per real defect; empty if none>"]}"""

def qc(n, img):
    t = tfile(n)
    r = client.chat.completions.create(model=MODEL, response_format={"type": "json_object"}, messages=[{"role": "system", "content": QC_SYS},
        {"role": "user", "content": [{"type": "text", "text": f"QC of U{n:03d}."}] + [{"type": "image_url", "image_url": {"url": b64(p), "detail": "high"}} for p in (img, STUDIO, LOGO, t)]}])
    j = json.loads(r.choices[0].message.content); j["pass"] = all(j.get(k, False) for k in ("pouch_ok", "comparison_ok", "text_ok", "anatomy_ok", "layout_ok"))   # logo_ok advisory
    return j

def aspect(t):
    from PIL import Image
    w, h = Image.open(t).size; r = w / h
    return min([("1:1", 1), ("4:5", .8), ("9:16", 9 / 16), ("2:3", 2 / 3), ("3:2", 1.5)], key=lambda a: abs(a[1] - r))[0]

def generate(n, j, extra=""):
    t = tfile(n); refs = [t, STUDIO, LOGO] + ([RIVAL[j["needs_rival"]]] if j.get("needs_rival", "none") != "none" else [])
    pf = f"{B}/prompts/kie-U/u{n:03d}_run.txt"; open(pf, "w").write(j["prompt"] + ("\n\nFIX from QC: " + extra if extra else ""))
    r = subprocess.run(["python3", f"{B}/kgen.py", str(n), pf, *refs, "--aspect", aspect(t), "--prefix", "u", "--model", "gpt"], capture_output=True, text=True)
    outs = sorted(glob.glob(f"{R}/out/u_{n:03d}_v*.png"), key=lambda f: int(re.search(r"_v(\d+)", f).group(1)))
    ok = r.returncode == 0 and "ERREUR" not in r.stdout + r.stderr
    log(num=n, step="gen", ok=ok, out=os.path.basename(outs[-1]) if outs else None, msg=(r.stdout + r.stderr).strip()[-200:])
    return outs[-1] if ok and outs else None

def run(n, force=False):
    j = write_prompt(n, force)
    if j.get("validator_errors"): print(f"U{n:03d}: prompt still has validator errors {j['validator_errors']}", flush=True)
    extra = ""
    for attempt in range(2):
        img = generate(n, j, extra)
        if not img: print(f"U{n:03d}: generation failed", flush=True); return
        q = qc(n, img); log(num=n, step="qc", attempt=attempt, img=os.path.basename(img), **{k: v for k, v in q.items()})
        if q["pass"]: print(f"U{n:03d}: PASS {os.path.basename(img)} (try {attempt + 1}, rival={j.get('needs_rival')})", flush=True); return
        extra = "; ".join(q["issues"]); print(f"U{n:03d}: try {attempt + 1} rejected — {extra}", flush=True)
    print(f"U{n:03d}: FLAGGED after 2 tries — {extra}", flush=True)

if __name__ == "__main__":
    a = sys.argv[1:]; force = "--force" in a; qc_only = "--qc" in a
    nums = [int(x) for x in a if x.isdigit()]
    import concurrent.futures as cf
    if qc_only:
        def one(n):
            outs = sorted(glob.glob(f"{R}/out/u_{n:03d}_v*.png"), key=lambda f: int(re.search(r"_v(\d+)", f).group(1)))
            if not outs: return n, {"pass": False, "issues": ["no output"]}
            q = qc(n, outs[-1]); log(num=n, step="qc-only", img=os.path.basename(outs[-1]), **q); return (n, q)
        with cf.ThreadPoolExecutor(12) as ex:
            for n, q in ex.map(one, nums): print(f"U{n:03d}: {'PASS' if q['pass'] else 'FAIL'} {q.get('issues')}", flush=True)
    else:
        with cf.ThreadPoolExecutor(10) as ex: list(ex.map(lambda n: run(n, force), nums))
