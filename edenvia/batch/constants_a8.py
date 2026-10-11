# Edenvia — shared spec constants for angle A8 (lymphatic bloating). DRAFT 2026-10-11; gate 1 signed the same day with three
# sub-angles (brand.json v1.5 angle_keyword): A8-L heavy legs / puffy belly (king), A8-F puffy face & jawline, A8-M the man's belly.
# Not a spec file: no ads here. The first spec file (s1specs.py) starts with `from constants_a8 import *`
# (or copies these lines), so every ad carries the same, latest wording of A11/F3 (avatar), C2 (ingredient look),
# D6 (container), D8/D19 (icon) and the generic KEEP lines. Facts come from brand.json; these constants only hold
# the VISUAL wording. Update here, never in a single spec.
#
# Sources: edenvia/brand.json v1.3 (avatar.who, product.ingredient_visual, product.capsule_visual, product.not,
# product_noun, icon_description, lock_extra), edenvia/avatars/lymphatic-bloating.md (Step 1), BRAND-KIT.md §2, §10.

# A11 / F3 — the customer shown is OUR avatar, never the template's person. One look per sub-angle; OLD = the king (A8-L).
OLD_L = ("a woman in her mid-40s with a soft build, shoulder-length brown hair, no make-up look, tired after a day on her feet; "
       "her legs and ankles are visibly swollen, heavy and puffy (sometimes her arms too), the kind of legs she hides under long skirts "
       "and wide trousers — a real woman 35–55, never a young fitness model, never slim-legged. Do NOT copy the template's person.")
OLD_F = ("a woman in her late 40s with a soft, puffy face, a softened jawline and the beginning of a double chin, shoulder-length hair "
         "tied back, no make-up look, seen in a bathroom-mirror or phone-selfie framing — never a young model, never a sharp-jawed face. "
         "Do NOT copy the template's person.")
OLD_M = ("a man in his late 40s to 50s with short greying hair and stubble, a round, hard belly pushing over his belt under a tucked or "
         "untucked shirt, otherwise ordinary build — the uncle at the BBQ, never a gym model, never obese. Do NOT copy the template's person.")
OLD = OLD_L

# C2 — what the product's "ingredient" looks like: an effervescent tablet, never a capsule / pill / powder.
TABLET = ("a round, flat, white, matte effervescent tablet with no coating and no imprint, as in the brand packshot — "
          "never a capsule, never a gel cap, never a pill in a blister, never a powder scoop")

# C2 / product fact — the ritual made visible: one tablet in a clear glass of water.
GLASS = ("a clear glass of clear water at room temperature with one white effervescent tablet fizzing at the bottom and fine hydrogen "
         "bubbles rising; the water stays clear and clean — never cloudy, never foamy, never coloured, never hot water, never tea or coffee, "
         "never a hydrogen-water bottle or generator")

# D6 — the container word: the real pouch cutout is pasted by script (golden rule 4). The model never redraws the label.
POUCH = ("the Edenvia Molecular Hydrogen stand-up pouch exactly as in Image 1 (white fading to sky blue, water droplets, "
         "zip seal) — a pouch of 30 effervescent tablets; never a bottle, jar, tub or blister")

# D8 / D19 — icon-only sentence, appended to every `visual`. Matches brand.json lock_extra + icon_description.
ICON = (" Leave every brand-logo spot outside the label EMPTY (plain background, no icon, no letters): the official Edenvia "
        "atom icon (two crossed elliptical orbit rings with two small round dots, NO letters) is pasted there by script afterwards.")

# Generic KEEP lines (clone a winner: same skeleton, new flesh).
STD = ["KEEP the template's background, palette and lighting",
       "KEEP the template's text positions, sizes and fonts",
       "KEEP the template's composition and framing"]

# A8 vocabulary the copy must carry (B2, brand.json angle_keyword.required_any) — the core problem in her own words:
A8_WORDS = {"A8-L": ["heavy, swollen legs", "puffy legs", "it's not a fat problem", "it was never fat", "water retention", "puffiness", "feel lighter"],
            "A8-F": ["puffy face", "double chin", "jawline"],
            "A8-M": ["blame the beer", "belly that isn't fat", "where did your gut go", "keg"]}
