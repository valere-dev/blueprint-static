# New Brand Worksheet — run the whole analysis for brand X, then hand off

Copy this file to the brand's kit folder (e.g. `/root/workspace/<brand>-kit/ANALYSIS.md`) and fill it
top to bottom. Rules: one short sentence per box, verbatim quotes in quotes with their source, `UNKNOWN`
or `[MISSING]` instead of a guess, everything in English. Two sign-off gates: after §7 (angles + avatar)
and after the first concept family of §9.

The output of this worksheet is the **Brand Kit** + one **decoded brief per template**, which the
production half of this skill (`2-make/`, start with `2-make/PIPELINE.md`) consumes. The generator never researches; if a fact is not here, it
does not exist.

---

## §1. Product sheet (the only source of facts)

```
Brand:                         Product name:
Website / PDP URL:
Physical product: form · count · dose · ingredients (with amounts) · ritual (when/how taken)
Functional product (what it DOES, 1 line):
Packaging (for image fidelity): container · colour · lid · label text lines, exactly as printed
Product photo path (Image 1 of every generation):
Price: one-time $… · crossed price $… · subscription $… every … days
Bundles: …
Offer framing allowed in ads (e.g. "Buy 1 Get 1 Free", "50 % off for life"):
Guarantee: length · wording · conditions:
Allowed proof (exact numbers + footnote): e.g. "50,000+ customers", "93 %* … (*12-week survey)"
Real authorities available (founder on camera? expert? institution? culture?):
Real reviews / comments we can quote (paths):
Banned claims / words (site + ads):
Compliance level: ads (aggressive ok?) · site (structure-function only):
Never mention in ads (e.g. autoship, subscription mechanics):
Brand-mark rule (wordmark spelling, icon-only slots):
```

## §2. Mechanism map (see product-mechanism-angle.md)

```
M1 [name] (enemy → fix) :: angle | angle | angle
M2 …
```
For each mechanism: enemy name · action name · belief-bridge fact (+ source) · chain (3–5 links +
sources) · A + B = C · elimination triad · failed solutions it explains · analogy · mechanism visual ·
banned terms → rewrites · freshness (shops scaling on it) · belief (plausibility) · differentiation case
(format transplant / desire transplant / core swap).

Refused angles (no mechanism reaches them): …

## §3. Research log

| # | Source | Query / scope | Tool | Credits/$ | Rows | Status | Saved at |
|---|---|---|---|---|---|---|---|
| 1 | Competitor A Meta library | domain, all, total_impressions, top 250 + latest 100 | Apify | $… | … | ✅ / ⚠ failed (why) | /root/workspace/... |
| 2 | Competitor A statics | newest 30 + minDaysRunning ≥ … | TrendTrack | … | … | | |
| 3 | Reddit VOC | "anyone tried [solution] reddit"… | Apify | … | … | | |
| 4 | Amazon reviews | ours + N competitors, 1–5★ | Apify | … | … | | |

Budget agreed for this research: TrendTrack … credits (floor ≥ 1,000) · Apify $… · OpenAI $… .
Every failure is reported here, never hidden.

## §4. Competitor table

| Brand | Domain | Same product / same desire | Ads (active/total) | Videos % | Top angles (≈ share) | Mechanism | Offer | Guarantee | Main LPs | Trend (ads / traffic) |
|---|---|---|---|---|---|---|---|---|---|---|

Routing per competitor (angle → landing page): …
Weaknesses (sourced numbers): …
Sophistication level of the market (1–5) and why (what their top-10 scaling ads do): …

## §5. Market research report (structure fixed — research-playbook.md §7)

1. Top 5 angles (# · angle · idea incl. mechanism · weight)
2. 5 secondary angles
3. Top 5 headlines (verbatim + source)
4. Headline bank: Pain & mechanism · Comparison · Product · Story · Urgency
5. Video hooks (verbatim)
6. Avatar (age, situation, visible problem, tried + spent, shame behaviours)
7. What proves it to them (proof objects)
8. Winning formats (static/video split)
9. Their offer
10. Their weaknesses
11. Recommendation: 3 angles + 10 headlines to attack first

## §6. Avatar

### 6.1 Master avatar (13 sections — avatar-angle-system.md §2)
Executive summary · core avatar · emotional landscape · problem beneath the problem · desired
transformation · what they tried (+ why it failed) · beliefs/myths · objections (their voice) · buying
triggers · messaging insights · exact voice (20 phrases / 20 fears / 20 desires) · segments · strategic
takeaways.

### 6.2 Avatar Check (one page)
| Box | Sentence |
|---|---|
| Name + 1 line | |
| Deep desire | |
| Top emotional pain (feeling) | |
| Past failed attempt + why | |
| Daily-life moment (where we'd film) | |
| Identity he/she is buying | |
| Product (1 line) | |
| Mechanism (plain) | |
| Why it works when others didn't | |
| Timeline (day 3 / week 2 / month 1) | |
| Bridge sentence | |
| Demand pull (permanent / seasonal) | |

### 6.3 Sub-avatars (3–10)
| # | Trigger (when) | Cause (why) | What exactly | Already tried | Emotion now → wanted | Objection | Uses now | Volume check |
|---|---|---|---|---|---|---|---|---|

### 6.4 Bridge sentence (3 versions, keep 1)
1. 2. 3.

### 6.5 Necessary beliefs (≤ 6, "I believe that…")

## §7. Angle map + angle cards  ⛔ SIGN-OFF GATE 1

### 7.1 Angle Expansion Map (awareness × desire, 25 cells) → pick 5

### 7.2 Top 5 angles
| ID | Angle (outcome, ≤ 8 words) | Mechanism | Main / extra desire | Awareness | Sub-avatar | Evidence (ads · days · LPs · VOC count) | Destination |
|---|---|---|---|---|---|---|---|
| A1 | | | | | | | |
| A2 | | | | | | | |
| A3 | | | | | | | |
| A4 | | | | | | | |
| A5 | | | | | | | |

### 7.3 Angle cards (one per angle — fields in avatar-angle-system.md §8)
Each card must include the headline bank (≥ 5 verbatim lines with sources), problem scenes, payoff
scenes, who notices, timeline, objection, guarantee line, visual bans, dead hooks.

### 7.4 Brand-specific defaults (decide now, they drive template assignment)
- King angle (the default to fuse into off-angle templates):
- Avatar look for every person shown as the customer (age, look):
- Proof objects (what he/she is proud to see):
- Hiding behaviours (validated):
- Words to always use / never use (e.g. "beer belly" not "belly"):
- Aggression level the founder wants:

**Sign-off:** founder validated §5–§7 on [date]. After this, research is LOCKED.

## §8. Templates and the clone plan

### 8.1 Template intake
| Template id | File | Source (brand · days live · copies) | Format | Aspect | Family |
|---|---|---|---|---|---|

Families: 1 us vs them · 2 before-after/timeline · 3 problem reframe · 4 mechanism/ingredients ·
5 origin/source · 6 offer/bundle/price · 7 bold claim + product · 8 meme/humour/UGC · 9 off-avatar
re-skin.
Rule: accept every template; one ad per template; volume = number of templates.

### 8.2 Clone plan
| Template | Family | Angle carried | Assigned angle | Change distance (witness/clock/setting/body/belief) | Headline source line | Notes |
|---|---|---|---|---|---|---|

Coverage check: every family covers every top angle across its templates (each template still gets the
angle it naturally carries).

Already-made check: skip any (template × angle × headline) already in `creatives.jsonl`.

## §9. Hand-off brief — one per template (what `2-make/` receives)  ⛔ SIGN-OFF GATE 2

Send the first concept family only; wait for validation before the rest.

```json
{
  "brand": "BRAND",
  "ad_id": "BRAND_B01_C0021_V1",
  "template": {
    "id": "c0021",
    "path": "/root/workspace/<brand>-kit/templates/c0021.png",
    "source": "Competitor · 206 days live · 7 copies",
    "family": "1 US vs THEM / comparison",
    "aspect": "1:1",
    "production_method": "full illustration | real photo + pasted product | screenshot UI | text painted in scene | text-only | collage/table | skin scene",
    "refusal_risk": "none | sexual | body"
  },
  "decode": {
    "scroll_stop_trick": "one sentence",
    "angle_carried": "what the template's own angle is",
    "hidden_reading": "innuendo / joke / social mechanism, or none",
    "scene_logic": "why the scene is where it is → our scene",
    "visual_trick": "the trick to copy literally",
    "shape_or_function_equivalent": "e.g. round moon ↔ round belly, or none",
    "verb_of_the_scene": "pour / hold / hide / measure …",
    "structure_type": "before/after | split body | progression L→R | table | UI | single scene",
    "shock_level": "calm | cheeky | gross | shocking",
    "render_style": "e.g. flat vector, Pixar 3D, photo, watercolour",
    "text_treatment": "e.g. handwriting, sunscreen bubbles, bold sans"
  },
  "strategy": {
    "angle_id": "A1",
    "angle": "outcome in customer words",
    "mechanism_id": "M1",
    "sub_avatar": "trigger + cause + tried",
    "awareness": "problem-aware",
    "belief_installed": "one of the 6 beliefs"
  },
  "inventory": [
    {"zone": "setting", "template": "kid's bedroom", "action": "SWAP", "ours": "living room, game night", "reason": "scene logic"},
    {"zone": "product_spot", "template": "bottom right, 20 % width", "action": "KEEP", "ours": "our jar, same spot and size", "reason": "placement"}
  ],
  "text_slots": [
    {"slot": "headline", "template_text": "…", "ours": "…", "source": "bank line / template words kept", "same_length": true},
    {"slot": "subline", "template_text": "…", "ours": "…", "source": "…"}
  ],
  "text_slot_count": 2,
  "proof_allowed": ["50,000+ men", "60-day guarantee"],
  "people": {"customer_look": "45-60, greying", "other_people": "…"},
  "visual_bans": ["…"],
  "compliance_flags": [{"line": "…", "risk": "body claim", "decision": "kept as symbol / rewritten"}],
  "missing": ["[MISSING] real review first name", "…"]
}
```

Hard rules restated for the hand-off:
- `text_slot_count` = the template's count. No added tagline, context line, disclaimer or deadline.
- The headline is a bank line (or the template's own words if the template already carries our angle),
  adapted only for our facts.
- Every KEEP placement of the product appears in the inventory (and must exist in the final image).
- Nothing from their product world survives (material, symbol, body part, logo, innuendo object).
- If the founder already validated a try of this template, attach it as the new template and list only
  the changes he named.

## §10. Brand Kit folder (saved once, reused for every batch)

```
<brand>-kit/
  research.md          §5 report (angles, headline bank, video hooks, avatar)
  mechanisms.md        §2 map + cards
  avatar.md            §6
  angles.md            §7 (top 5 + cards + brand defaults)
  product.md           §1 (exact price, offer, guarantee, allowed claims, banned words)
  product-photo.jpg    Image 1 of every generation
  templates/           intake files, sorted by family
  briefs/              §9 JSON per template
  creatives.jsonl      every ad made: concept · angle · headline · json · image (never make one twice)
  LESSONS.md           every review verdict: what worked + why, what failed + root cause + new rule
```

New batch later = reload the kit, accept the new templates, run §8–§9 only. No new research, no
TrendTrack, unless the founder asks for it.

## §11. Review loop (after every founder review)

For each reviewed ad, log in `LESSONS.md`:
| Ad | Verdict (his words) | Why it worked → repeat / Root cause → new rule | Rule id |
|---|---|---|---|
Validated tries are frozen. His latest verdict wins. A rule that is added applies to every future batch
and to the decode checklist (template-reading.md).

## §12. Final status (end every working session with it)

| Request | Status |
|---|---|
| Product sheet | ✅ / 🔨 / ⏳ (reason) |
| Mechanism map | |
| Research (competitors + VOC) | |
| Market research report | |
| Avatar + sub-avatars | |
| Top 5 angles + cards — signed off | |
| Template intake + families | |
| Clone plan | |
| Briefs, family 1 — signed off | |
| Briefs, remaining families | |
| Brand kit saved | |
