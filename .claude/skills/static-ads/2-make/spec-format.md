# Spec format — one Python dict per ad

Specs live in `$SAC_BATCH/sNspecs.py` (one file per round: `s1specs.py` round 1, `s2specs.py` round 2 incl. redos, `s3fixspecs.py` QC fixes…).
Each file defines `S = [dict, ...]`. Later files override earlier ones by `num` (the page builders load them in name order).
Specs are Python, not JSON, so shared strings (avatar look, ingredient rendering) are constants reused across ads.
**Every spec is linted before anything is sent** (`python3 scripts/lint.py sNspecs.py`; srun.py also lints the whole file and refuses to run on any error).

## Fields

| Field | Required | What it holds | Rule |
|---|---|---|---|
| `num` | yes | ad number (S number on every page and in the Loom) | — |
| `tpl` | yes* | template filename inside `$SAC_BATCH/templates/` — exact extension (D10: a `.png` that is really `.jpg` made the pipeline report "OK" with no image); must be the template of THIS ad number = `sorted(templates)[num-1]` (D13, linted) | D10 D13 |
| `tpl_abs` | no | absolute path that replaces `tpl` as Image 2 — used to pass a **validated/liked try** as the template for a redo | A20 A22 |
| `angle` | yes (practice) | research angle id + name, e.g. `"A1 Beer belly (visual pun)"`; the angle-keyword lint only fires on angles starting with `angle_prefix` | A5 A14 |
| `why` | **lint** | why the template works, one sentence; for redos it starts with the Loom quote ("Loom 3: …") | A1 |
| `dna` | **lint** | everything that belongs to THEIR product and what it becomes ("Mars tube → our jar; cellulite legs → round beer belly") | A2 A7 |
| `scene` | **lint** | scene logic: why the scene is there and whether it applies ("Kraft-paper backdrop — applies." / "bed because sleep product → kitchen") | A3 A18 |
| `placement` | **lint** | product placement copied from the template ("Two jars side by side bottom right, overlapping slightly"); counted by D6 | A8 D6 |
| `inventory` | **lint ≥ 5** | the pixel inventory: list of `KEEP …` / `SWAP X → Y` lines covering setting, every prop, every person, light, camera, every text block, product spot | A13 |
| `visual` | **lint** | the CHANGES block: full scene description written from the inventory, incl. what NOT to draw and the render style | F1 F2 |
| `texts` | **lint** | one line per text slot of the template, same count, exact strings in quotes, with style hints ("Headline: …", "Tiny: …") | B1 B13 |
| `engine` | **lint** | `openai` · `pure_comp` · `seedream_comp` (never `seedream_full`) | D5 D7 |
| `fallback` | when sexual | engine used if OpenAI refuses — `seedream_comp` (or `none`) | D1 |
| `sexual` | when relevant | `True` if the template is suggestive → lint requires a fallback with sd_prompt + composite | A4 D1 |
| `sd_prompt` | with seedream_comp | the Seedream prompt: scene only, the template is the reference, **"No text, no product, no logo."**, and where to leave empty space for text/product | D7 |
| `composite` | with seedream_comp / pure_comp | composite.py spec (2-make/composite.md): product position(s), every text, rects, strikes, `bg` for pure_comp | D6 D9 |
| `aspect` | no | Seedream `image_size` to keep the template's ratio (`portrait_16_9`) | A25 |
| `template_has_deadline` | no | `True` only if the template itself shows a day count/timeline → unlocks digits+days in texts | B6 |
| `template_has_signature` | no | `True` only if the template is a signed review → unlocks "— First L." quotes | B12 |

\* `tpl` or `tpl_abs`.

## How srun.py turns a spec into a prompt (OpenAI)
```
{LOCK}

PIXEL INVENTORY (KEEP / SWAP — follow exactly):
- <inventory lines>

TEMPLATE DNA: <dna>
SCENE LOGIC: <scene>
PRODUCT PLACEMENT (copy the template): <placement>

CHANGES (visual): <visual>

TEXT (exactly, nothing else):
- <texts lines>

{CONS}
```
Image 1 = product photo, Image 2 = template (or `tpl_abs`). LOCK and CONS: 2-make/engines.md.

## Writing rules for specs
- Write the **inventory first**, then derive `visual` and `texts` from it. A spec whose `visual` mentions something absent from the inventory is suspect.
- `texts` style hints are words, not code: the image model reads "Headline cream:" as a style cue. Keep emoji only for OpenAI-drawn text (never inside `composite`, D9).
- Use shared constants for the avatar and the ingredient so every ad gets the same, latest wording:
  ```python
  OLD = "a man in his late 40s with short greying hair and light grey stubble"                      # A11 / F3
  ORGANS = ("fresh, clean, appetizing bison organs like a premium butcher counter — a deep-red heart, a glossy lobed liver, two kidneys, an oval testicle — "
            "recognizable silhouettes, clean edges, no blood puddles, no visible veins, you want to eat them")   # C2 (round-3 wording)
  CAPS = "transparent capsules packed with tiny recognizable deep-red organ pieces (mini hearts, mini kidneys, mini livers)"   # C2 / E3
  HORN = " Leave every brand-logo spot outside the jar label EMPTY (no horns, no icon, no letters): the official logo is pasted by script."             # D8 (appended to visual)
  STD = ["KEEP the template's background, palette and lighting", "KEEP the template's text positions, sizes and fonts", "KEEP the template's composition and framing"]
  def ad(num, angle, why, dna, scene, placement, inventory, visual, texts, engine="openai", fallback="seedream_comp", **kw):
      return dict(num=num, tpl=T[num], angle=angle, why=why, dna=dna, scene=scene, placement=placement,
                  inventory=inventory, visual=visual, texts=texts, engine=engine, fallback=fallback, **kw)
  ```
- For a new brand, replace those constants first (brand.json holds the facts; the constants hold the visual wording).
- A redo spec keeps everything validated and changes only what the reviewer named (A20). Put the Loom quote at the start of `why`.

---

## Example 1 — `openai`, new ad validated first try (Sam S23, "really great understanding", E6)
```python
ad(23, "A1 Beer belly (visual pun)",
   "Split image: moon texture vs cellulite = 'this belongs on the moon, not on you'. Ours: a full ROUND moon vs a round beer belly — same shape.",
   "Cellulite legs → a round beer belly in side profile. Their bottle → our jar on the orange circle.",
   "Space / studio split — applies.",
   "Bottom center on an orange half circle, like the template.",
   ["KEEP vertical split: left black space with a big full moon, right a body close-up",
    "SWAP legs → a man's round beer belly in side profile (t-shirt lifted)",
    "KEEP condensed white headline on the moon side, black italic on the body side",
    "SWAP bottle → WILDHORN jar on the orange half circle",
    "KEEP tiny disclaimer"],
   "Vertical split. LEFT: black space with a huge round full moon. RIGHT: a man's round beer belly in side profile, t-shirt lifted, matching the moon's curve. "
   "Bottom center: the WILDHORN jar on an orange half circle. Tiny disclaimer under it.",
   ["Left, white condensed caps: \"THIS SHAPE\" / \"BELONGS\" / \"ON THE\" / \"MOON\"",
    "Right, black italic condensed: \"NOT ON\" / \"YOUR\" / \"BEER BELLY\"",
    "Tiny: \"Individual results may vary\""]),
```
Why it worked: shape equivalent first (the template's pun survives), five-line inventory, our product on their product's exact spot, same text count.

## Example 2 — `openai` with an angle fusion (Sam S28 arcade, E13 / A14)
```python
ad(28, "Testosterone + beer belly (fused)",
   "Retro arcade stats: you now vs you 10 years ago + 'insert X, restore your score'. Same angle as ours → keep words, add our belly stat (A14).",
   "Mars tube → our jar.", "Black arcade screen — applies.", "Bottom left like the tube.",
   ["KEEP black background, neon pixel arcade font", "KEEP yellow title, 2 columns with dotted underlines", "KEEP purple big scores + green stat rows",
    "SWAP last row → belly fat (high now, low then)", "SWAP tube → WILDHORN jar", "KEEP blue/orange insert line"],
   "Black screen, neon pixel arcade typography exactly like Image 2. Two columns of stats. The WILDHORN jar bottom-left with a soft glow.",
   ["Title yellow: \"TESTOSTERONE STATS\"", "Columns: \"YOU NOW\" · \"YOU 10 YEARS AGO\"", "Scores purple: \"1000\" · \"5000\"",
    "Left rows green: \"200 ENERGY\" / \"250 STRENGTH\" / \"300 MOTIVATION\" / red \"900 BELLY FAT\"",
    "Right rows green: \"1,050 ENERGY\" / \"1,750 STRENGTH\" / \"1,200 MOTIVATION\" / \"50 BELLY FAT\"",
    "Blue: \"INSERT WILDHORN.\"", "Orange: \"RESTORE YOUR SCORE.\""]),
```

## Example 3 — `pure_comp`: text-only template rendered by script (Sam S4, validated first try)
```python
dict(num=4, tpl="09-14_c0012_Mars-Men.jpg", angle="A1 Beer belly (identity)", engine="pure_comp",
 why="Text-only recruitment post: calls out an excuse men hide behind and turns it into identity ('isn't a personality') + brand slogan pun. "
     "Ours: the 'dad bod' excuse; keep 't up or shut up' — our label literally says Natural Testosterone Support.",
 dna="Pure text on solid orange. Only the excuse changes.", scene="No scene.", placement="No product (template has none).",
 inventory=["KEEP solid orange #FF5A00 background", "KEEP mixed weights: bold white words + regular black words", "KEEP 3 paragraphs, lowercase",
  "SWAP excuse 'i'm just tired' → 'it's just a dad bod'", "SWAP 'mars men.' → 'wildhorn.'", "KEEP 'are u one of them?'"],
 visual="Solid orange background, text only, rendered by script for exact typography.",
 texts=["\"we want 5 men who realized that “it's just a dad bod” isn't a personality.\"", "\"wildhorn. t up or shut up.\"", "\"are u one of them?\""],
 composite={"bg": "#FF5A00", "texts": [
  {"y": 0.10, "size": 0.068, "font": "Montserrat", "weight": 500, "align": "left", "x": 0.075, "maxw": 0.86, "lh": 1.32,
   "runs": [["we", "#FFFFFF", 800], [" want", "#FFFFFF", 800], [" 5", "#FFFFFF", 800], [" men", "#FFFFFF", 800], [" who", "#111111", 500],
            [" realized", "#FFFFFF", 800], [" that “it's just a dad bod” isn't a personality.", "#111111", 500]]},
  {"y": 0.555, "size": 0.068, "font": "Montserrat", "weight": 500, "align": "left", "x": 0.075, "maxw": 0.86, "lh": 1.32,
   "runs": [["wildhorn.", "#FFFFFF", 800], [" t up or shut up.", "#111111", 500]]},
  {"y": 0.80, "size": 0.068, "font": "Montserrat", "weight": 800, "align": "left", "x": 0.075, "maxw": 0.86, "runs": [["are u one of them?", "#FFFFFF", 800]]}]}),
```
Use pure_comp whenever the template is text on a flat background: zero spelling risk, one "generation", exact weights per word.

> Examples 4–5 come from `s4specs.py`, whose `ad()` helper takes the template filename as 2nd argument: `ad(num, tpl, angle, why, dna, scene, placement, inventory, visual, texts, engine="openai", fallback="none", **kw)` and appends `HORN` to `visual`.

## Example 4 — `seedream_comp` (scene by Seedream, real product + text + price by script) — Sam S74 redo, validated at Sam Loom 4
```python
ad(74, "09-18_c0122_RYZE.png", "A1 (same angle)", "Loom 3: it must be ONE fat belly next to ONE lean belly — before vs after.",
   "Two stomachs → fat vs lean male stomach.", "Orange poster.", "Bottom right.",
   ["KEEP orange background", "KEEP yellow + white headline", "SWAP left photo → a fat round beer belly", "SWAP right photo → a lean flat stomach",
    "KEEP deal block", "SWAP pouch → real jar by script"],
   "Orange poster, two photos: left fat belly, right lean belly.",
   ["\"BEER BELLY?\"", "\"CAN'T RELATE.\"", "\"SPECIAL DEAL\" / \"$49.95\" + struck \"$100\" / \"THIS WEEK ONLY\""],
   engine="seedream_comp",
   sd_prompt="Flat solid orange (#D9643A) poster background. Two rounded-corner square photos side by side, placed ONLY between 30% and 62% of the image height: "
             "LEFT a man's big round soft beer belly above dark shorts, RIGHT the same body lean with a flat toned stomach above dark shorts. "
             "Top 30% and bottom 38% completely empty plain orange. No text, no product, no logo.",
   composite={"jar": {"x": 0.82, "y": 0.97, "h": 0.36}, "texts": [
    {"y": 0.022, "size": 0.095, "font": "Anton", "runs": [["BEER BELLY?", "#FFE500"]]},
    {"y": 0.128, "size": 0.05, "font": "Montserrat", "weight": 800, "runs": [["CAN'T RELATE.", "#FFFFFF"]]},
    {"y": 0.66, "size": 0.04, "font": "Anton", "align": "left", "x": 0.06, "runs": [["SPECIAL DEAL", "#FFFFFF"]]},
    {"y": 0.72, "size": 0.12, "font": "Anton", "align": "left", "x": 0.06, "runs": [["$49.95", "#FFE500"]]},
    {"y": 0.75, "size": 0.05, "font": "Anton", "align": "left", "x": 0.42, "runs": [["$100", "#FFFFFF"]]},
    {"y": 0.88, "size": 0.05, "font": "Anton", "align": "left", "x": 0.06, "runs": [["THIS WEEK ONLY", "#FFFFFF"]]}],
    "strikes": [[0.415, 0.79, 0.512, 0.79, "#FFFFFF"]]}),
```
The sd_prompt reserves empty bands (top 30 %, bottom 38 %) where composite.py writes the text and places the real jar. The first Seedream attempt
(`seedream_full`) wrote "crossed" on the ad and put the headline on the label → D7.

## Example 5 — redo with `tpl_abs`: "change only the wording" (Sam S29, Loom 3 → validated Loom 4, A22)
```python
ad(29, "09-16_c0056_Zapply.jpg", "A1 Beer belly",
   "Loom 3: try 2's layout and typography were right; only the wording should change. Use try 2 itself as Image 2 and change only the subline.",
   "Image 2 = our own validated try 2.", "Same.", "Same as try 2.",
   ["KEEP try 2 exactly: layout, fonts, sizes, colors, jar, pills", "SWAP only the subline under SUPPLEMENT", "KEEP the 5 pills", "KEEP disclaimer", "KEEP white/orange split"],
   "Reproduce Image 2 exactly, pixel for pixel in layout and typography. Change ONLY the two-line subline under the black SUPPLEMENT bar.",
   ["Subline (same font and size as Image 2): \"UNLESS YOU WANT\" / \"A FLAT BELLY AGAIN.\"", "(unchanged pills include: Flatter Beer Belly)"],
   tpl_abs=O + "s_29_v2.png"),       # O = $SAC_WORKDIR/out/
```

## Example 6 — sexual template with fallback: the D6 failure and its fix (Sam S11)
Round 2 spec (OpenAI refused → fallback). The placement says TWO jars, the composite has ONE — the head jar vanished silently (Sam Loom 2: "you fucked it up"):
```python
ad(11, "A1 + drive (fused, cheeky)", "Couple in bed, the jar literally on her head = he fell back in love; checklist of payoffs. ...",
   "Viking jars → our jars (on her head + bottom right).", "Bedroom intimacy — applies.",
   "One WILDHORN jar balanced on the woman's head, one more at the bottom right, like the template.",
   [...6 inventory lines...], "...", [...texts...],
   sexual=True, fallback="seedream_comp",
   sd_prompt="Warm dim bedroom, tasteful: a lean man in his late 40s ... The bottom-left third of the image is dark and empty for text. No text, no product.",
   composite={"jar": {"x": 0.86, "y": 0.97, "h": 0.24}, "texts": [...]}),      # ← 1 jar: lint now fails "D6 fallback parity — placement needs 2 jar(s)"
```
Round 3 redo (parity fixed, painted style, head jar without shadow):
```python
   composite={"jars": [{"x": 0.6, "y": 0.42, "h": 0.30, "noshadow": True}, {"x": 0.86, "y": 0.97, "h": 0.24}], "texts": [...]}
```
Still rejected (Sam Loom 3/4) because the method was wrong, not the parity: the template was a photo with the product pasted as her head. The validated v5 followed
**A25** (2-make/engines.md): Seedream minimal edit of the template itself (`s_11_sd6.txt`: age the man, remove the small jar and the text, keep everything else
pixel-identical, 9:16) → `jarswap.py` on the head jar → `composite.py` with `prompts/s_11_comp5.json` (Oswald headline, DejaVu ✓ marks, jar bottom right, orange rule).

## Example 7 — template with its own timeline (B6 unlock)
```python
ad(14, "A1 (same angle — copy)", "Loom 2 fail: 'Lost my waistline — last seen 3 weeks ago' ALREADY works for our man (he got slim). I flipped a line that worked. A19: copy word for word.",
   "3 Ryze pouches → 3 jars; price starburst → ours.", "Warm studio pedestal — applies.", "Three WILDHORN jars on the wooden pedestal, center one forward.",
   STD + ["KEEP headline word for word", "KEEP orange script subline word for word", "SWAP 3 pouches → 3 WILDHORN jars", "KEEP red starburst price badge"],
   "Warm peach background with thin decorative line circles. A round wooden pedestal with three WILDHORN jars, the center one in front. Red starburst badge overlapping the center jar.",
   ["Headline: \"LOST MY\" / \"WAISTLINE\"", "Orange italic script: \"Last Seen 3 Weeks Ago\"", "Badge: crossed \"$100\" / \"$49.95\""],
   template_has_deadline=True),
```

## Before you run a spec file
1. `python3 scripts/lint.py $SAC_BATCH/sNspecs.py` → must print `LINT OK`. Read warnings too.
2. Check every `tpl` exists with the right extension (`ls $SAC_BATCH/templates/`).
3. Re-read each spec against 2-make/qc-checklist.md section "Spec review" (angle in the headline, text count, placement, avatar age).

---

## Input from 1-understand: the hand-off brief → spec

The **`1-understand/`** folder of this skill does the research and the template reading. Its
`1-understand/new-brand-worksheet.md` §9 produces one JSON **hand-off brief per template** (template, decode, strategy, KEEP/SWAP inventory,
text slots, proof, bans, compliance, missing facts). `2-make/` accepts that brief as its input; don't redo the analysis here.

Draft the specs mechanically, then do the judgment work by hand:
```bash
python3 $SKILL/scripts/brief2spec.py $SAC_BATCH/s1specs.py /root/workspace/<brand>-kit/briefs/*.json     # --start N to number from N
python3 $SKILL/scripts/lint.py $SAC_BATCH/s1specs.py
```

| Brief field (§9) | Spec field | How |
|---|---|---|
| `template.path` | `tpl_abs` | absolute path used as Image 2 (copy the file into `$SAC_BATCH/templates/` and use `tpl` if you prefer relative names) |
| `template.aspect` | `aspect` | non-square → Seedream `image_size` (`9:16`→`portrait_16_9`, `3:4`/`4:5`→`portrait_4_3`, `16:9`→`landscape_16_9`) |
| `template.production_method` | `engine` / method | `text-only` → `pure_comp`; `skin scene` → fallback `seedream_comp`; `real photo + pasted product` → **A25 method** (engines.md); `text painted in scene` → Nano Banana Pro (D5); else `openai` |
| `template.refusal_risk` | `sexual`, `fallback`, `sd_prompt`, `composite` | `sexual`/`body` → `fallback="seedream_comp"` + scene prompt + composite recipe (D1, D6, D7) |
| `decode.scroll_stop_trick` (+ `hidden_reading`, `visual_trick`) | `why` | one sentence + the trick to copy literally (A1, A4, A21) |
| `decode.scene_logic` | `scene` | (A3, A18) |
| `decode.verb_of_the_scene` | `visual` | "copy the action" (A17, A30) |
| `decode.render_style`, `decode.text_treatment` | `visual` | name the style, "not another style" (C5, F2, A10) |
| `decode.shape_or_function_equivalent`, `structure_type`, `shock_level` | `inventory` / `visual` | E6, A9/A16/A23, A15 — check they appear in the inventory |
| `strategy.angle_id` + `angle` | `angle` | the lint's angle-keyword check keys on the id prefix |
| `inventory[]` (zone, template, action, ours, reason) | `inventory` | `KEEP zone: template (reason)` / `SWAP zone: template → ours (reason)` — **≥ 5 lines** (A13) |
| `inventory[]` SWAP rows on product/material/symbol/body part/logo/innuendo/person zones | `dna` | "their thing → ours; …" (A2, A7) |
| `inventory[zone=product_spot]` | `placement` | copied from the template (A8); every KEEP product placement must also exist in `composite` (D6) |
| `text_slots[].ours` | `texts` | one line per slot, exact string in quotes; count must equal `text_slot_count` (B1) |
| `text_slots[].template_text` with a day/week count | `template_has_deadline=True` | only then may our text carry a timeline (B6) |
| `proof_allowed` | — | the only numbers allowed in `texts` (B20); prices also in brand.json `prices_allowed` |
| `people.customer_look` | `visual` (+ the `OLD` constant) | (A11, F3) |
| `visual_bans` | `visual` | "Do NOT draw: …" (F1, F8) |
| `compliance_flags` | comment above the spec | decide before generation; brand.json `banned` for anything mechanizable |
| `missing` | comment `# MISSING` | **blocking**: do not generate an ad with an unresolved missing fact (B20) |

After the draft: rewrite `visual` as one coherent scene description (the draft concatenates inventory lines), write `sd_prompt` and `composite`
for every fallback/scene ad, add the shared constants (`OLD`, ingredient strings, `HORN`), lint, then generate the first concept family only
(1-understand sign-off gate 2).

---

## Starter file for a new round (`$SAC_BATCH/s1specs.py`)
```python
# <Brand> — round 1 (S1–S10). Every spec carries the full pixel inventory (A13) BEFORE the prompt. Lint: python3 $SKILL/scripts/lint.py <this file>
import os
B = os.environ.get("SAC_BATCH", os.path.join(os.environ.get("SAC_WORKDIR", "."), "batch"))
TEMPLATES = sorted(f for f in os.listdir(f"{B}/templates") if not f.startswith("."))
T = {i + 1: f for i, f in enumerate(TEMPLATES)}            # ad number = rank (D13)
O = os.path.join(os.environ.get("SAC_WORKDIR", "."), "out") + "/"   # for tpl_abs redos: O + "s_29_v2.png"

OLD = "<avatar: age, hair, stubble, build — never the template's model>"             # A11 / F3
INGREDIENT = "<how the ingredient must look: recognizable, fresh, appetizing, no …>"  # C2 / C14 / C15
CAPS = "<capsule/pack shot showing the ingredient inside>"                           # C2 / E3
ICON = " Any brand mark outside the label is the <icon> ONLY, NO letters."           # D8 (also brand.json lock_extra)
STD = ["KEEP the template's background, palette and lighting", "KEEP the template's text positions, sizes and fonts", "KEEP the template's composition and framing"]

def ad(num, angle, why, dna, scene, placement, inventory, visual, texts, engine="openai", fallback="none", **kw):
    return dict(num=num, tpl=kw.pop("tpl", T[num]), angle=angle, why=why, dna=dna, scene=scene, placement=placement,
                inventory=inventory, visual=visual + ICON, texts=texts, engine=engine, fallback=fallback, **kw)

S = [
ad(1, "A1 <angle>",
   "<the scroll-stop trick in one sentence>",
   "<their thing → ours; their product → our product>",
   "<why the scene is there — applies / moved to where our problem shows>",
   "<product spot + gesture, copied from the template>",
   STD + ["KEEP …", "SWAP … → …", "SWAP … → …"],
   "<one coherent scene description written from the inventory; render style named; what NOT to draw>",
   ["Headline: \"…\"", "Subline: \"…\""]),
]
```
Redo rounds: a new file (`s2specs.py`) holding the redos (same `num`, Loom quote first in `why`, `tpl_abs` when a liked try is the base) + the next 10 new ads.
Never edit a spec in place after it generated: the review page must keep showing what produced each try.
