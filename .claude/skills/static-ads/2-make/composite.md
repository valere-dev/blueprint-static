# composite.py — real product + exact text on any image

`python3 scripts/composite.py IN.png OUT.png spec.json`

Used for: every `seedream_comp` ad (scene by Seedream, everything else by script), every `pure_comp` ad (text-only templates on a flat colour),
the A25 method (text on the edited template), and recomposites (text moved on an existing scene: the run-1 `recomp` engine, e.g. #73 centring).
It never misspells, never squashes the product, never invents a logo — which is why it is the safety net of the whole chain.

## Coordinate system
All positions and sizes are **fractions** of the image: `x` of width W, `y` of height H, `size` = font height as a fraction of **H**.
The same spec works at 1024×1024, 1024×1792 or 2048×2048.

## Drawing order
1. `rects` (solid rectangles) → 2. `band` → 3. `texts` (in list order) → 4. `strikes` → 5. products (`jar`, then `jars`).
Products are drawn last, so they sit on top of text and rects.

## Top-level keys

| Key | Type | Meaning |
|---|---|---|
| `bg` | `"#hex"` | only for `pure_comp`: srun.py creates a 1024×1024 canvas of this colour (`size` [w,h] optional) |
| `rects` | `[[x0, y0, x1, y1, "#hex"], …]` | solid rectangles (white band for a headline, a tag, an underline rule). S58: `[[0, 0, 1, 0.17, "#FFFFFF"]]` top white band; S11 v5: `[[0.045, 0.85, 0.40, 0.8525, "#E07A2B"]]` thin orange rule |
| `band` | `{"y0", "y1", "color"}` | full-width band |
| `texts` | list of text blocks | below |
| `strikes` | `[[x0, y0, x1, y1, "#hex"], …]` | straight lines, width = max(3 px, 0.6 % of H): crossed prices. S74: `[[0.415, 0.79, 0.512, 0.79, "#FFFFFF"]]` over "$100" |
| `jar` | product block | one product |
| `jars` | list of product blocks | more products (D6: as many as the template's placements) |

## Product block (`jar` / items of `jars`)
| Key | Meaning |
|---|---|
| `x` | horizontal **centre** of the product |
| `y` | **bottom edge** of the product (where it stands) |
| `h` | product height; width follows the cutout's real aspect ratio (C6 — never squashed) |
| `noshadow` | `true` → no contact shadow (a product floating, or used as a head: S11 head jar) |
| `src` | optional other cutout (multi-product brands); default = brand.json `product_cutout` |
The contact shadow is a soft black ellipse (alpha 70) under the base (C10). The cutout must be an RGBA PNG/WebP with a clean transparent background
(Wildhorn: `/srv/wildhorn-lp/p6/jar-30.webp`, 416×793).

## Text block
| Key | Default | Meaning |
|---|---|---|
| `y` | — | top of the first line |
| `size` | — | font size as fraction of H (0.11 = huge headline, 0.06 headline, 0.04 subline, 0.018–0.025 small print) |
| `font` | `Montserrat` | `Anton`, `Montserrat` (variable), `Oswald` (variable), `Fredoka`, `DejaVu` (Bold — has ✓ ✕ → ★ glyphs) + any brand.json `fonts` |
| `weight` | 800 | variable-font weight (Montserrat/Oswald): 500 regular-ish, 700 bold, 800 heavy |
| `runs` | — | `[[text, "#hex"], [text, "#hex", weight], …]` — coloured/weighted segments on the same lines (word-wrapped together) |
| `t` + `color` | — | simple alternative to `runs` |
| `align` | `center` | `center` (around `cx`) or `left` (from `x`) |
| `cx` | 0.5 | centre axis when centred — put it on the template's anchor (C9: #73 text on the eggplant's axis, `cx: 0.515`) |
| `x` | 0.05 | left edge when `align: left` |
| `maxw` | 0.9 | wrap width (fraction of W) |
| `lh` | 1.18 | line height multiplier |
| `box` | — | `"#hex"` → a filled box behind each line (white-on-red labels, "IS BACK ON THE MENU ;)" on red) |
| `shadow` | false | 3 px dark drop shadow (text on photos) |
| `sunscreen` | false | soft embossed look (own layer, blurred brown shadow, slight blur) — a fallback for painted text; Nano Banana Pro paints it better (A10, D5) |

Rules for text blocks:
- One block per template text slot, same order and same count (B1). Copy positions and sizes from the template (C9): measure the template at full resolution.
- Keep the template's spacing between headline and secondary text (C9 — #73 failed twice on this).
- No emoji (D9). Use DejaVu for ✓ ✕; give the glyph its own block and the words their own block (S11 v5 pattern below) so each uses the right font.
- Wording identical to `texts` in the spec — the review page shows `texts`, the image shows `composite`; they must match.
- Prices/numbers only from brand.json (B20).

## Examples (real, validated)

### Text-only post (S4, pure_comp)
```json
{"bg": "#FF5A00", "texts": [
 {"y": 0.10, "size": 0.068, "font": "Montserrat", "weight": 500, "align": "left", "x": 0.075, "maxw": 0.86, "lh": 1.32,
  "runs": [["we", "#FFFFFF", 800], [" want", "#FFFFFF", 800], [" 5", "#FFFFFF", 800], [" men", "#FFFFFF", 800], [" who", "#111111", 500],
           [" realized", "#FFFFFF", 800], [" that “it's just a dad bod” isn't a personality.", "#111111", 500]]},
 {"y": 0.555, "size": 0.068, "font": "Montserrat", "weight": 500, "align": "left", "x": 0.075, "maxw": 0.86, "lh": 1.32,
  "runs": [["wildhorn.", "#FFFFFF", 800], [" t up or shut up.", "#111111", 500]]},
 {"y": 0.80, "size": 0.068, "font": "Montserrat", "weight": 800, "align": "left", "x": 0.075, "maxw": 0.86, "runs": [["are u one of them?", "#FFFFFF", 800]]}]}
```

### Poster with price block and crossed price (S74, seedream_comp)
```json
{"jar": {"x": 0.82, "y": 0.97, "h": 0.36}, "texts": [
  {"y": 0.022, "size": 0.095, "font": "Anton", "runs": [["BEER BELLY?", "#FFE500"]]},
  {"y": 0.128, "size": 0.05, "font": "Montserrat", "weight": 800, "runs": [["CAN'T RELATE.", "#FFFFFF"]]},
  {"y": 0.66, "size": 0.04, "font": "Anton", "align": "left", "x": 0.06, "runs": [["SPECIAL DEAL", "#FFFFFF"]]},
  {"y": 0.72, "size": 0.12, "font": "Anton", "align": "left", "x": 0.06, "runs": [["$49.95", "#FFE500"]]},
  {"y": 0.75, "size": 0.05, "font": "Anton", "align": "left", "x": 0.42, "runs": [["$100", "#FFFFFF"]]},
  {"y": 0.88, "size": 0.05, "font": "Anton", "align": "left", "x": 0.06, "runs": [["THIS WEEK ONLY", "#FFFFFF"]]}],
 "strikes": [[0.415, 0.79, 0.512, 0.79, "#FFFFFF"]]}
```

### Two-weight headline + side copy + tag (S79, seedream_comp, man boobs — "try 1 is perfect")
```json
{"jar": {"x": 0.79, "y": 0.96, "h": 0.36}, "rects": [[0.33, 0.85, 0.63, 0.92, "#FFFFFF"]], "texts": [
  {"y": 0.04, "size": 0.062, "font": "Montserrat", "weight": 500, "runs": [["MORE CHEST DAY ", "#FFFFFF", 500], ["WON'T", "#FFFFFF", 800]]},
  {"y": 0.115, "size": 0.062, "font": "Montserrat", "weight": 800, "runs": [["FIX YOUR MAN BOOBS", "#FFFFFF"]]},
  {"y": 0.28, "size": 0.042, "font": "Montserrat", "weight": 500, "align": "left", "x": 0.57, "maxw": 0.4, "runs": [["It's not a gym problem.", "#FFFFFF"]]},
  {"y": 0.41, "size": 0.042, "font": "Montserrat", "weight": 800, "align": "left", "x": 0.57, "maxw": 0.4, "runs": [["It's a testosterone problem.", "#F26B1D"]]},
  {"y": 0.862, "size": 0.045, "font": "Montserrat", "weight": 800, "align": "left", "x": 0.36, "runs": [["THE FIX →", "#F26B1D"]]}]}
```

### Headline on a white top band, product in her raised hand (S58)
```json
{"rects": [[0, 0, 1, 0.17, "#FFFFFF"]], "jar": {"x": 0.82, "y": 0.72, "h": 0.36},
 "texts": [{"y": 0.045, "size": 0.062, "font": "Montserrat", "weight": 800, "align": "left", "x": 0.03, "runs": [["Make her eat the sheets", "#111111"]]}]}
```
(The template's 🥵🌶️ were dropped: emoji can't be composited — D9. The sell version of S58 is try 1, made by OpenAI with the emoji drawn.)

### Two products + shadowed text on a painting (S11 round 3: head jar without shadow)
```json
{"jars": [{"x": 0.6, "y": 0.42, "h": 0.30, "noshadow": true}, {"x": 0.86, "y": 0.97, "h": 0.24}], "texts": [
  {"y": 0.55, "size": 0.075, "font": "Oswald", "weight": 700, "align": "left", "x": 0.05, "runs": [["FALLING IN LOVE", "#F2E6D0"]], "shadow": true},
  {"y": 0.635, "size": 0.075, "font": "Oswald", "weight": 700, "align": "left", "x": 0.05, "runs": [["WITH THIS JAR", "#F2E6D0"]], "shadow": true}]}
```

### Check marks with DejaVu + text in Oswald (S11 v5, validated — A25)
```json
{"jar": {"x": 0.845, "y": 0.985, "h": 0.19}, "rects": [[0.045, 0.85, 0.40, 0.8525, "#E07A2B"]], "texts": [
  {"y": 0.622, "size": 0.059, "font": "Oswald", "weight": 700, "align": "left", "x": 0.045, "maxw": 0.95, "runs": [["FALLING IN LOVE", "#EDE6DA"]]},
  {"y": 0.68,  "size": 0.059, "font": "Oswald", "weight": 700, "align": "left", "x": 0.045, "maxw": 0.95, "runs": [["WITH THIS JAR", "#EDE6DA"]]},
  {"y": 0.745, "size": 0.040, "font": "Oswald", "weight": 700, "align": "left", "x": 0.045, "maxw": 0.95, "runs": [["WAS THE BEST DECISION", "#E07A2B"]]},
  {"y": 0.789, "size": 0.040, "font": "Oswald", "weight": 700, "align": "left", "x": 0.045, "maxw": 0.95, "runs": [["I EVER MADE.", "#E07A2B"]]},
  {"y": 0.857, "size": 0.018, "font": "Oswald", "weight": 500, "align": "left", "x": 0.045, "maxw": 0.72, "runs": [["IT MELTED MY BEER BELLY AND MY WOMAN", "#EDE6DA"]]},
  {"y": 0.878, "size": 0.018, "font": "Oswald", "weight": 500, "align": "left", "x": 0.045, "maxw": 0.72, "runs": [["FELL FOR ME ALL OVER AGAIN.", "#EDE6DA"]]},
  {"y": 0.909, "size": 0.017, "font": "DejaVu", "align": "left", "x": 0.045, "runs": [["✓", "#E07A2B"]]},
  {"y": 0.909, "size": 0.018, "font": "Oswald", "weight": 500, "align": "left", "x": 0.078, "runs": [["FLATTER BEER BELLY", "#EDE6DA"]]},
  {"y": 0.931, "size": 0.017, "font": "DejaVu", "align": "left", "x": 0.045, "runs": [["✓", "#E07A2B"]]},
  {"y": 0.931, "size": 0.018, "font": "Oswald", "weight": 500, "align": "left", "x": 0.078, "runs": [["MORE ENERGY", "#EDE6DA"]]},
  {"y": 0.953, "size": 0.017, "font": "DejaVu", "align": "left", "x": 0.045, "runs": [["✓", "#E07A2B"]]},
  {"y": 0.953, "size": 0.018, "font": "Oswald", "weight": 500, "align": "left", "x": 0.078, "runs": [["FEEL LIKE HER HERO", "#EDE6DA"]]}]}
```

### Text centred on the template's anchor + label boxes (run 1 #69 / #73 recomposites)
```json
{"jar": {"x": 0.5, "y": 0.86, "h": 0.36}, "texts": [
  {"y": 0.06, "size": 0.08, "font": "Anton", "runs": [["SHE SAYS DESSERT", "#FFFFFF"]], "shadow": true},
  {"y": 0.16, "size": 0.08, "font": "Anton", "box": "#E01B1B", "runs": [["IS BACK ON THE MENU ;)", "#FFFFFF"]]}]}
```
```json
{"texts": [{"y": 0.27, "size": 0.12, "font": "Anton", "cx": 0.515, "runs": [["NO MORE", "#FFFFFF"]], "shadow": true},
           {"y": 0.525, "size": 0.03, "font": "Montserrat", "weight": 800, "cx": 0.515, "runs": [["ORGAN SUPPLEMENTS HAVE EVOLVED", "#FFFFFF"]], "shadow": true}],
 "jar": {"x": 0.2, "y": 0.97, "h": 0.30}}
```

## Workflow to write a composite spec
1. Open the template at full resolution; for each text slot note top `y`, height (→ `size`), alignment, colour, weight, font family look.
2. Pick the closest font (Anton = condensed poster caps; Oswald = condensed; Montserrat = geometric sans; Fredoka = rounded/playful).
3. Product: where does the template's product stand (bottom edge → `y`), centre (`x`), height (`h`)? Same scale as theirs (C17).
4. Render, open the output at full resolution, compare side by side with the template (spacing, overlap, centring), adjust, re-render. Re-renders are free (no API call).
