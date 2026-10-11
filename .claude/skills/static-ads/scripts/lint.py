"""Anti-regression linter: run on every spec before any generation. Exit 1 = nothing is sent.

Generic copy of /root/workspace/wh-remix/lint.py (Wildhorn).  Generic checks are hard-coded here;
brand-specific checks come from brand.json (BRAND_JSON env var), keys:
  "banned":            {regex: reason}            extra banned words in texts+visual (e.g. competitor names, compliance bans)
  "competitors":       [names]                    blocked anywhere in texts+visual
  "angle_keyword":     {"loose": r"\\bbelly\\b", "required_any": "beer belly|belly fat|...", "angle_prefix": "A1",
                        "msg": "B2 say 'beer belly', not just 'belly'"}
  "visual_checks":     [{"if": regex, "unless": regex (optional), "msg": "..."}]   applied to the 'visual' field
  "prices_allowed":    ["$49.95", "$100"]         any $ amount in texts must be one of these (B20)
  D13 (built in): if $SAC_BATCH/templates/ exists, spec tpl must equal sorted(templates)[num-1] unless tpl_abs is set (SAC_NO_D13=1 to skip)
Usage: python3 lint.py SPECFILE.py   (SPECFILE defines S = [dict, ...])"""
import re, sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sac_config import BRAND, WORDMARK, PRODUCT_NOUN, BATCH

BANNED = {r"\bauto-?ship": "B7 never mention Autoship", r"\bsubscription": "B7 never mention subscription",
          r"\bconversion\b": "B4 no mechanism jargon",
          r"men over \d+\"": "B2 name the problem, not the age"}
BANNED.update(BRAND.get("banned", {}))
for c in BRAND.get("competitors", []):
    BANNED[re.escape(c)] = "no competitor names"
FAKE_SIGNED = r"\"[^\"]*— ?[A-Z][a-z]+ [A-Z]\.\""   # B12: a signed quote is only allowed when the template has one
REQUIRED = ["why", "dna", "scene", "visual", "texts", "engine"]
AK = BRAND.get("angle_keyword")
VCHECKS = BRAND.get("visual_checks", [])
PRICES = BRAND.get("prices_allowed")
PALETTE_BANNED = BRAND.get("palette_banned", {})   # C20: {regex: why} colours that do not fit the avatar (Wildhorn: pink) -> error unless spec ad_for_women / c20_exempt
ANGLE_WARN = BRAND.get("angle_warn", {})           # A35: {regex: why} off-angle claim words in the copy (Wildhorn: sleep) -> warning
TPL_DIR = os.path.join(BATCH, "templates")
TEMPLATES = sorted(f for f in os.listdir(TPL_DIR) if not f.startswith(".")) if os.path.isdir(TPL_DIR) else []
D13_ON = bool(TEMPLATES) and os.environ.get("SAC_NO_D13") != "1"


WARN = []


def lint(specs):
    errs = []; WARN.clear()
    for s in specs:
        n = s.get("num")
        texts = " ".join(s.get("texts", []))
        visual = s.get("visual", "")
        for f in REQUIRED:
            if f not in s: errs.append(f"#{n}: missing field '{f}' (A1-A3 decode)")
        blob = texts + " " + visual
        # B21 (Oct08 Loom): the word sex is always censored for Meta -> S*X (texts + composited text)
        _w = re.search(r"\bsex\b", " ".join(s.get("texts", [])) + " " + json.dumps(s.get("composite", {}), ensure_ascii=False), re.I)
        if _w: errs.append(f"#{n}: B21 write S*X, never '{_w.group(0)}' (Meta censors it)")
        # --- B22 (Loom O1, 2026-10-08): never the word "drive" in ad copy (S*X drive too) -> libido, or the beer-belly / fat angle ---
        if not s.get("b22_exempt"):
            for _tx in list(s.get("texts", [])) + [json.dumps(s.get("composite", {}), ensure_ascii=False)]:
                _hit = [q for q in (re.findall(r'"([^"]*)"', _tx) or [_tx]) if re.search(r"\bdrive\b", q, re.I)]
                if _hit: errs.append(f"#{n}: B22 never the word 'drive' (S*X drive too) - say libido, or go beer belly / fat (matched '{_hit[0].strip()[:60]}')"); break
        for pat, why in BANNED.items():
            if re.search(pat, blob, re.I): errs.append(f"#{n}: {why} — matched /{pat}/")
        if re.search(FAKE_SIGNED, blob) and not s.get("template_has_signature"):
            errs.append(f"#{n}: B12 signed testimonial but the template has no signature (set template_has_signature=True if it does)")
        for vc in VCHECKS:
            if re.search(vc["if"], visual, re.I) and not (vc.get("unless") and re.search(vc["unless"], visual, re.I)):
                errs.append(f"#{n}: {vc['msg']}")
        if s.get("sexual") and s.get("engine", "").startswith("openai") and not s.get("fallback"):
            errs.append(f"#{n}: D1 sexual template on OpenAI without a fallback engine")
        # D1/D6/D7: a scene engine needs the full composite recipe. Primary engine or sexual ad (refusal is likely) = error;
        # a plain openai ad with an unfilled seedream_comp fallback = warning (srun.py stops at refusal instead of guessing).
        scene_primary = s.get("engine") in ("flux", "seedream_comp")
        scene_fallback = s.get("fallback") == "seedream_comp"
        missing = [k for k in ("composite", "sd_prompt") if k not in s]
        if missing and (scene_primary or (scene_fallback and s.get("sexual"))):
            errs.append(f"#{n}: D1/D7 scene engine needs {' + '.join(missing)} (scene only, then real product + exact text by script)")
        elif missing and scene_fallback:
            WARN.append(f"#{n}: fallback seedream_comp not filled ({' + '.join(missing)}) — a refusal will stop this ad")
        _kept = s.get("template_term")   # A34: a template term our avatar uses (e.g. "Dad Bod") is kept; it overrides the B2 core-problem check
        if _kept and _kept.lower() in texts.lower(): pass
        elif AK and re.search(AK["loose"], texts, re.I) and not re.search(AK["required_any"], texts, re.I) \
                and s.get("angle", "").startswith(AK.get("angle_prefix", "")):
            errs.append(f"#{n}: {AK.get('msg', 'B2 name the core problem explicitly')}")
        if not s.get("template_has_deadline") and re.search(r"\b\d+\s*days?\b|day \d+|by week", texts, re.I):
            errs.append(f"#{n}: B6 deadline added but the template has none")
        if not isinstance(s.get("inventory"), list) or len(s.get("inventory", [])) < 5:
            errs.append(f"#{n}: A13 missing pixel inventory (>=5 KEEP/SWAP lines)")
        if "placement" not in s:
            errs.append(f"#{n}: A8 missing 'placement' (copied from the template)")
        if s.get("composite") and PRODUCT_NOUN.lower() in str(s.get("placement", "")).lower():
            want = 2 if re.search(r"\band (?:one|another)\b|\btwo\b|one more|another", s.get("placement", ""), re.I) else 1
            have = len(s["composite"].get("jars", [])) + (1 if s["composite"].get("jar") else 0)
            if have < want: errs.append(f"#{n}: D6 fallback parity — placement needs {want} {PRODUCT_NOUN}(s), composite has {have}")
        if D13_ON and not s.get("tpl_abs") and isinstance(n, int) and 1 <= n <= len(TEMPLATES) and s.get("tpl") != TEMPLATES[n - 1]:
            errs.append(f"#{n}: D13 tpl '{s.get('tpl')}' is not the template of ad {n} ('{TEMPLATES[n - 1]}') — set tpl_abs if intended")
        if "seedream_full" in (s.get("engine", ""), s.get("fallback", "")):
            errs.append(f"#{n}: D7 seedream_full banned — use seedream_comp (scene only + composite)")
        for tx in s.get("texts", []):
            if re.match(r"\s*(Top |Small )?(wordmark|logo)[^:]*:\s*\"?" + re.escape(WORDMARK) + r"\"?\s*$", tx, re.I):
                errs.append(f"#{n}: D8 standalone {WORDMARK} wordmark — leave the logo spot empty; the official logo file is pasted by script (D19)")
        comp_txt = json.dumps(s.get("composite", {}), ensure_ascii=False)
        if re.search(r"[\U0001F300-\U0001FAFF]", comp_txt):
            errs.append(f"#{n}: D9 emoji in composited text")
        # C20 (Loom O2): brand colours only; palette words that miss the avatar (brand.json palette_banned) -> error
        if PALETTE_BANNED and not s.get("c20_exempt") and not s.get("ad_for_women"):
            _inv = s.get("inventory") if isinstance(s.get("inventory"), list) else []
            _vb = re.sub(r"SWAP[^>]*->", " ", " ".join([visual, " ".join(_inv), texts, str(s.get("sd_prompt", "")), json.dumps(s.get("composite", {}))]))
            for _pat, _why in PALETTE_BANNED.items():
                for _m in re.finditer(_pat, _vb, re.I):
                    _cl = re.split(r"[,.;:—()\n]", _vb[max(0, _m.start() - 40):_m.start()])[-1]
                    if not re.search(r"\b(no|not|never|without|nothing|zero)\b", _cl, re.I):
                        errs.append(f"#{n}: C20 {_why} (matched '{_m.group(0)}')"); break
        # A35 (Loom O2): the angle stays on the core angles; off-angle claim words in the copy (brand.json angle_warn) -> warning
        for _pat, _why in ANGLE_WARN.items():
            _hit = [q for _tx in s.get("texts", []) for q in (re.findall(r'"([^"]*)"', _tx) or [_tx]) if re.search(_pat, q, re.I)]
            if _hit: WARN.append(f"#{n}: A35 {_why} ('{_hit[0].strip()[:50]}')")
        if PRICES is not None:
            allowed = {p.replace(" ", "") for p in PRICES}
            for p in re.findall(r"\$\s?\d[\d,]*(?:\.\d\d)?", texts + " " + comp_txt):
                if p.replace(" ", "") not in allowed:
                    errs.append(f"#{n}: B20 price {p} is not in brand.json prices_allowed")
    return errs


if __name__ == "__main__":
    import importlib.util
    sp = importlib.util.spec_from_file_location("s", sys.argv[1]); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    e = lint(m.S)
    for w in WARN: print("warning:", w)
    print("\n".join(e) if e else f"LINT OK — {len(m.S)} ads pass all checks")
    sys.exit(1 if e else 0)
