# Engines — chain, prompts, refusals, methods

All calls run on the VPS. Keys are read from files, never written anywhere: OpenAI `/etc/secrets/openai_api_key`, kie.ai `/etc/secrets/kie_api_key`
(overridable with `OPENAI_KEY_FILE` / `KIE_KEY_FILE`).

## The chain (D5, D7)

| Need | Engine | Script | Output |
|---|---|---|---|
| Default: clone the template with our product | OpenAI `gpt-image-2`, `images/edits`, `quality=high`, `1024x1024`, Image 1 = product photo, Image 2 = template | `remix.py` (via `srun.py engine=openai`) | full ad |
| Template is text on a flat background | none — script only | `composite.py` (via `srun.py engine=pure_comp`) | full ad, exact typography |
| OpenAI refuses (sexual, bare chest) or the scene has skin/lingerie | Seedream `bytedance/seedream-v4-edit` on kie.ai, the **template** as the only reference | `kie_gen.py --model seedream` (via `srun.py engine/fallback=seedream_comp`) | **scene only** → `composite.py` adds the real product + exact text |
| Text must be PAINTED INTO the scene (sunscreen letters, clay, chalk) | Nano Banana Pro on kie.ai (`nano-banana-pro`, 2K) | `kie_gen.py --model nano` | scene with painted text; product composited if needed |
| Template = real photo with a product pasted in (A25) | Seedream minimal edit of the template → gpt-image-2 masked edit of the product box → script text | `kie_gen.py --aspect …` → `jarswap.py` → `composite.py` | full ad, template look kept |
| Legacy run-1 fallback | Flux 2 Pro (`flux-2/pro-image-to-image`, 1K) on kie.ai | `kie_gen.py --model flux` | scene → composite |

**Seedream never renders a full ad** (D7): it garbles labels and writes prompt words on the image ("crossed" on S74, headline printed on the label).
`seedream_full` is banned in lint and refused by srun.py. Seedream = scene only, "No text, no product, no logo."

Order of choice for each spec, decided at spec time, not at refusal time:
1. Text-only template → `pure_comp`.
2. Real photo + pasted product, or a failed ad whose template is that → A25 method.
3. Sexual/skin template → `engine="openai", fallback="seedream_comp", sexual=True` with `sd_prompt` + `composite` filled (lint requires them).
   If OpenAI already refused this kind of image before (bare/soft male chest close-ups), go straight to `engine="seedream_comp"`.
4. Painted text treatment → Nano Banana Pro.
5. Everything else → `openai` (it accepts suggestive food objects: banana, glazed donut).

## The fixed prompt blocks (verbatim originals, then the generic form)

### Wildhorn LOCK (verbatim, `sam-batch/srun.py`)
```
IMAGE 1 = product reference: the WILDHORN Wild American Bison capsule jar. Reproduce it exactly as in Image 1: amber glass jar, matte black lid, cream label with the WILDHORN wordmark and horn logo, WILD AMERICAN BISON, the bison illustration, Untamed Bison Nutrition, black band NATURAL TESTOSTERONE SUPPORT* / 30 CAPSULES. Real proportions, real 3D object with contact shadow and the scene's light.
IMAGE 2 = the template ad to clone 1:1: same layout, composition, render style, palette, typography treatment, spacing and the SAME AMOUNT OF TEXT.
```
### Wildhorn CONS (verbatim, `sam-batch/srun.py`)
```
USE CASE + CONSTRAINTS: Square 1:1 Meta feed ad, agency-grade. If the template is vertical, re-flow into the square without dropping elements and keep the template's spacing between text blocks. Render ONLY the listed text, spelled exactly, once — nothing added. Nothing from the template's product world may remain (product, brand, logo, flavor, packaging). Anatomically correct, adults over 25. CRITICAL: the WILDHORN jar, when present, is an exact replica of Image 1.
```
History: the batch-09 LOCK ended "Real proportions, never stretched." — "real 3D object with contact shadow and the scene's light" was added after Loom 9 #65 (C10);
CONS gained "keep the template's spacing between text blocks" after Loom 8/9 #73 (C9). The protocols-page version (protocol 3) also said
"Do not redesign, relabel or re-letter it" and "No other brand names or logos, no watermark".

### Generic form (what `scripts/srun.py` builds from brand.json)
```
IMAGE 1 = product reference: {product_lock} Real proportions, real 3D object with contact shadow and the scene's light.
IMAGE 2 = the template ad to clone 1:1: same layout, composition, render style, palette, typography treatment, spacing and the SAME AMOUNT OF TEXT.
...
USE CASE + CONSTRAINTS: Square 1:1 Meta feed ad, agency-grade. If the template is vertical, re-flow into the square without dropping elements and keep the template's spacing between text blocks. Render ONLY the listed text, spelled exactly, once — nothing added. Nothing from the template's product world may remain (product, brand, logo, flavor, packaging). Anatomically correct, adults over 25. CRITICAL: the {NAME} {product_noun}, when present, is an exact replica of Image 1. {lock_extra}
```
`product_lock` = one sentence that names every visible element of the packaging in reading order (shape, material, lid, label colour, wordmark,
icon, product line, illustration, claim band, count). `lock_extra` = the D8 sentence ("Any brand mark outside the jar label is the horn icon ONLY (two curved horns), NO letters.").
In the Sam batch round 4 the D8 sentence was appended to every `visual` instead (`HORN` constant) — same effect.

### Body (between LOCK and CONS), from the spec
`PIXEL INVENTORY (KEEP / SWAP — follow exactly)` → `TEMPLATE DNA` → `SCENE LOGIC` → `PRODUCT PLACEMENT (copy the template)` → `CHANGES (visual)` → `TEXT (exactly, nothing else)`.
See spec-format.md. A real full prompt (S23) is ~2,300 characters.

### Prompt-writing rules (F1–F13 in 3-improve/rules.md)
- Say what NOT to draw when the template's subject differs (F1). Name the render style + "NOT photoreal" (F2). Describe our avatar + "do NOT copy the template's person" (F3).
- "NO product / NO jar" written explicitly when the template has none (F7). "A bison, NOT a cow, no spots" (F8). Wrapping elements off the wordmark (F9).
- Text: every string in quotes, slot by slot, same count as the template; style cue words before each ("Headline cream serif:").
- Corrections: CHANGE + PRESERVE; for "wording only" pass the liked try as Image 2 (`tpl_abs`) and change only the named slot (A22).

## Seedream rules (kie.ai `bytedance/seedream-v4-edit`)
- **Reference**: in `seedream_comp`, srun.py passes the TEMPLATE as `--product` (the only reference image). The prompt describes the scene to produce from it.
- **Prompt shape** (`sd_prompt`): style + scene + our avatar + exact empty zones for the script layer + "No text, no product, no logo." Real examples:
  - S74: "Flat solid orange (#D9643A) poster background. Two rounded-corner square photos side by side, placed ONLY between 30% and 62% of the image height: LEFT a man's big round soft beer belly above dark shorts, RIGHT the same body lean with a flat toned stomach above dark shorts. Top 30% and bottom 38% completely empty plain orange. No text, no product, no logo."
  - S58: "UGC phone photo, white wall: a woman with wet dark hair and glasses biting a pale green bed sheet, eyes squeezed shut, her right hand raised up beside her face with the fingers curled as if holding a bottle, empty. The top 18% of the image is plain white. No text, no product."
  - S79: "Pure black background. On the left half, a side view of an overweight man's soft, puffy, fatty chest (pronounced gynecomastia shape, soft sagging pecs) glowing in thermal orange-red light, dramatic. Right half and top 18% empty black. No text, no product."
- **Hands that will hold the product**: render them empty, "fingers curled as if holding a bottle", at the spot where composite.py will place the cutout (S58, S55 "palm up, empty").
- **Aspect**: Seedream on kie reads `input.image_size`, not `aspect_ratio`. Default `square_hd`; keep a vertical template vertical with `--aspect portrait_16_9` (spec field `aspect`). (kie_gen.py patches the request.)
- **Prompt length**: kie_gen.py truncates prompts to 4,900 characters.
- **Credits**: `kie6.credits()` gives the balance; the jobs runner prints credits before/after. Cost per image not recorded in the sources — check the balance before a large run.

## The A25 method — when the template is a photo with a product pasted in
Use it when (a) the template is a real photo/painting with their product composited on it (a head replaced by a jar, a product floating on a photo),
or (b) an ad failed ≥ 2 times by regeneration. It reproduces the template's exact look because the template itself is edited.

1. **Minimal Seedream edit of the template** (keep the ratio):
   ```bash
   python3 $SKILL/scripts/kie_gen.py s_11_sd --prompt prompts/s_11_sd6.txt --product $SAC_BATCH/templates/<template> --model seedream --aspect portrait_16_9
   ```
   Prompt pattern (S11, verbatim `s_11_sd6.txt`): "Edit Image 1 with the smallest possible change. Keep EVERYTHING pixel-identical: the same bedroom, the same warm moody
   film-grain photo look, the same woman in the same lingerie and pose, the same big jar sitting on her neck in place of her head (DO NOT touch that jar, DO NOT give her a
   human head: the jar stays her head, exactly as it is), the same lamp, the same framing. Change ONLY these things: 1. The man: same pose, same body, same loving look up at
   the jar, but he is now late 40s with short greying hair (grey at the temples) and grey stubble. 2. Remove the small jar at the bottom right: replace it with the same plain
   dark background. 3. Remove all the text at the bottom: the bottom area becomes clean, empty, dark, the same dark gradient."
   The file trail shows the order that worked: `s_11_sd5` (edit + swap the jar in one Seedream pass) → `s_11_sd6` (edit only, their jar untouched) →
   `s_11_sd7` (Seedream jar swap) → `s_11_jar.png` made with `jarswap.py` = the one composited into v5. So: keep their product in place in the Seedream pass
   and swap it with the masked edit (inferred from file names and timestamps, 01/10 22:24–22:53).
2. **Masked product swap** with gpt-image-2 (only the box changes; hands/hair excluded from the box; pasted back feathered):
   ```bash
   python3 $SKILL/scripts/jarswap.py base.png swapped.png X0 Y0 X1 Y1 --context "Surreal ad trick: the jar REPLACES the person head and sits directly on the neck, like a head. NO hands, NO fingers, NO hair, NO face anywhere in the masked area; behind the jar only the plain wall of the room."
   ```
   It crops a 4:5 tile around the box (box height × 1.25), resizes to 1024×1280, sends tile + product photo + mask (transparent = editable) to
   `images/edits` (quality high), resizes back and pastes only the box (+6 px, Gaussian-feathered 8 px).
3. **Exact text by script**: `composite.py swapped.png final.png comp.json` (S11: `prompts/s_11_comp5.json`, Oswald + DejaVu ✓).
4. Copy the result to `out/<key>_vN.png` so it becomes a counted try; log the calls in `calls.jsonl` by hand (the S11 A25 calls were not logged — see 3-improve/stats.md).

## Masked edits in general (`jarswap.py`)
Use for any "swap only this object" fix on an otherwise validated image (wrong product label, misspelled logo on a sign) — it cannot drift the rest of the image.
Give a box with a small margin; keep hands out of the box or say "NO hands" in `--context`.

## Refusals and failure modes seen
| Symptom | Engine | Cause | Fix |
|---|---|---|---|
| HTTP 400 moderation_blocked / "flagged as sensitive" | OpenAI | sexual scenes; bare or soft male chest close-ups even without the template (batch-01 c0123, c0262; #60 #62) | fallback `seedream_comp` (D1); for chest: clothes/objects on OpenAI or Seedream scene (S79) — never water down the idea |
| Label garbled, prompt words written on the image ("crossed") | Seedream full ad | Seedream can't spell | scene only + composite (D7) |
| Wordmark misspelled ("WILLDHORN", "WIILDHORN") on signs/logos outside the label | OpenAI | small/standalone wordmarks | icon only (D8) — sentence in every prompt |
| Template's person/props leak (young model, their bottle in his hand, sequin skirts) | OpenAI | Image 2 copied too literally | inventory SWAP every prop (C5/F11), describe our avatar (F3) |
| Our product added where the template has none | OpenAI | generic lock implies a product | "NO product" explicitly (F7) |
| Jar squashed / covering the hero | OpenAI | template slot shape | real proportions in LOCK; product in its slot (C6) |
| Fallback dropped a product placement | pipeline | composite spec incomplete | D6 lint (product count vs placement) |
| "OK" printed, no image | pipeline | wrong template extension | D10 checks (template exists, new file counted) |
| Emoji rendered as boxes | composite | font lacks emoji | no emoji in composite (D9); DejaVu for ✓ ✕ |
| 500/502/503/504/429 | OpenAI | transient | remix.py retries 3× with 20 s pauses |

## Timing and cost (from the logs)
- gpt-image-2 high, 1024×1024: ~105–111 s per image (log.jsonl, 01/10). One call ≈ 1.5–3k input tokens (images ~1.5–2.7k) + ~7k image output tokens.
- Budget estimate used on 01/10: 790 images ≈ $240 → ~$0.30 per high-quality image (estimate, not a billed figure — check the OpenAI usage page).
- Parallelism: up to 6 concurrent `remix.py` jobs were used (`xargs -P 6`). Seedream/kie: ~1–3 min per scene (polling every 6 s, 600 s timeout).
- Transcription of review Looms: `mr-transcribe`, ~$0.006/min.

## Aspect ratios
- Output: square 1:1 Meta feed (1024×1024) by default; a vertical template is re-flowed into the square without dropping elements (CONS).
- Exception (A25): when the template's own image is edited, keep its ratio (9:16 stays 9:16) — Seedream `portrait_16_9`.
- `composite.py` works in fractions of W/H, so the same spec works at any size.

## A complete real prompt (Sam S23, OpenAI, validated first try)
Image 1 = `product-jar.jpg`, Image 2 = `templates/09-15_c0037_Happy-Mammoth-US.jpg`. Prompt sent (verbatim, `sam-batch/prompts/s_23.txt`):
```
IMAGE 1 = product reference: the WILDHORN Wild American Bison capsule jar. Reproduce it exactly as in Image 1: amber glass jar, matte black lid, cream label with the WILDHORN wordmark and horn logo, WILD AMERICAN BISON, the bison illustration, Untamed Bison Nutrition, black band NATURAL TESTOSTERONE SUPPORT* / 30 CAPSULES. Real proportions, real 3D object with contact shadow and the scene's light.
IMAGE 2 = the template ad to clone 1:1: same layout, composition, render style, palette, typography treatment, spacing and the SAME AMOUNT OF TEXT.

PIXEL INVENTORY (KEEP / SWAP — follow exactly):
- KEEP vertical split: left black space with a big full moon, right a body close-up
- SWAP legs → a man's round beer belly in side profile (t-shirt lifted)
- KEEP condensed white headline on the moon side, black italic on the body side
- SWAP bottle → WILDHORN jar on the orange half circle
- KEEP tiny disclaimer

TEMPLATE DNA: Cellulite legs → a round beer belly in side profile. Their bottle → our jar on the orange circle.
SCENE LOGIC: Space / studio split — applies.
PRODUCT PLACEMENT (copy the template): Bottom center on an orange half circle, like the template.

CHANGES (visual): Vertical split. LEFT: black space with a huge round full moon. RIGHT: a man's round beer belly in side profile, t-shirt lifted, matching the moon's curve. Bottom center: the WILDHORN jar on an orange half circle. Tiny disclaimer under it.

TEXT (exactly, nothing else):
- Left, white condensed caps: "THIS SHAPE" / "BELONGS" / "ON THE" / "MOON"
- Right, black italic condensed: "NOT ON" / "YOUR" / "BEER BELLY"
- Tiny: "Individual results may vary"

USE CASE + CONSTRAINTS: Square 1:1 Meta feed ad, agency-grade. If the template is vertical, re-flow into the square without dropping elements and keep the template's spacing between text blocks. Render ONLY the listed text, spelled exactly, once — nothing added. Nothing from the template's product world may remain (product, brand, logo, flavor, packaging). Anatomically correct, adults over 25. CRITICAL: the WILDHORN jar, when present, is an exact replica of Image 1.
```

## Painted text with Nano Banana Pro (run 1 #65, A10/D5)
The template wrote "train him before you drain him" on a woman's back in thick sunscreen cream. A flat composited font failed (Loom 8). The batch-09 spec
(`engine="openai_on_scene"`, `b9specs.py`) kept the batch-08 Seedream scene as Image 2 ("IMAGE 2 = the scene to keep exactly; only add what is listed below");
the output folder shows a Seedream and a Nano Banana Pro attempt (`b9_65_seedream_v1`, `b9_65_nano_v1`, 01/10 19:03–19:04) and the checkpoint records #65 as made
"via nano-banana-pro". The instruction asks for the letters as a material:
"Write on her bare back in THICK raised white sunscreen cream: puffy glossy bubbly letters with soft shadows and drips, like the cream was squeezed from a tube.
Place the WILDHORN jar standing on the white lounger cushion at the bottom-left." Text: "melt his" / "beer belly before" / "you drain him" (no deadline: the template
has none, B6). Nano Banana Pro is the engine for this kind of in-scene lettering (perfect spelling); `composite.py` `sunscreen: true` is only an approximation.
Loom 9: "great, but less great than the example — the 3D of the product on the table and the texture of the text" → C10.

## kie.ai batch runner (several scenes at once)
`kie6.py` also runs a jobs file with threads (credits printed before/after):
```bash
cat > jobs.json <<'J'
[{"id": "s_55_sd", "model": "bytedance/seedream-v4-edit", "prompt": "…scene only… No text, no product, no logo.", "aspect": "square_hd",
  "refs": ["/root/workspace/<brand>-remix/batch/templates/<template>"], "tag": "v1"}]
J
python3 $SKILL/scripts/kie6.py jobs.json 3      # → $SAC_WORKDIR/out/_kie/<id>_<tag>.png + log.jsonl
```
For Seedream the reference key is `image_urls` (kie_gen.py sets it); for `aspect` other than square on Seedream use `kie_gen.py --aspect` (it writes `image_size`).
Single-ad calls should go through srun.py/kie_gen.py so they are named `<key>_sd_vN.png` and counted.
