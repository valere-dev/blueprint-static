# 2-make — clone winning templates into the brand's own ads (the production pipeline)

**Clone a winner: same skeleton, new flesh. Change the minimum.**
A template that already wins on Meta has solved the hard part (the scroll-stop trick, the layout, the proof, the emotion). Our job is to keep
all of that and swap only what belongs to THEIR product and THEIR customer for ours — then let a review loop catch what we misread, and turn
every miss into a permanent rule so it never happens twice.

Built from the Wildhorn production (wild bison organ capsules, Oct 2026):
- **Run 1** — 79 templates, no rulebook: **0 %** validated on the first try, 30 % of generations validated, 2.5 review rounds per ad, 3.3 generations per final ad.
- **Sam batch** — 83 new templates, with the rulebook + blocking lint + pixel inventory: **71 %** first try, **87 %** after one fix, **100 %** final,
  62 % of generations validated, 1.4 rounds per ad, 1.6 generations per validated ad.

The difference between the two runs is entirely this protocol. Follow it step by step.

---

## 0. Where this folder sits

| Part | Role |
|---|---|
| `BRAND-KIT.md` + `brand.json` (skill root) | The brand's facts, voice, offer, proof, avatar, bans — the only input. Blank template here; filled example in the wildhorn-static-ads skill. |
| `1-understand/` | Upstream. Research, mechanisms, avatar, top-5 angles, headline bank, template reading, and one **hand-off brief per template** (`1-understand/new-brand-worksheet.md` §9). Run it first for a new brand. |
| **`2-make/`** (this folder) | Briefs/templates → specs → generation → QC → review pages. Brand-agnostic. |
| `3-improve/` | Loom → verdicts → rules → lint → stats (`3-improve/feedback-loop.md`, `3-improve/rules.md`, `3-improve/stats.md`). |
| wildhorn-static-ads (separate skill) | The same skill with the Wildhorn brand already loaded (`wildhorn/` folder there: brand facts, Adrien's taste, winners, failures). Same rule IDs as `3-improve/rules.md`. |
| **ad-blueprint-gpt-image-2** | Older: JSON blueprints + paste-ready ChatGPT prompts from a URL (H1–H16 headline library, 21 formats). Its Section 18 "Template Clone Protocol" is superseded by this skill; its Section 8 prompt-craft principles are folded into `3-improve/rules.md` §F. |

Work location: the VPS (`ssh vps-claude`). Skill folder: `/root/claude-vault/skills/static-ads/` (call it `$SKILL`; scripts in `$SKILL/scripts/`). Each brand gets its own
working folder (`/root/workspace/<brand>-remix`, `$SAC_WORKDIR`). Never generate on the Mac; never write into `/srv/**` or another brand's workspace
directly; secrets are read from `/etc/secrets/openai_api_key` and `/etc/secrets/kie_api_key` (paths only, never values).

---

## 1. Philosophy (read once, apply everywhere)

1. **The template is the brief.** Its words, layout, gesture, verb, shock level, render style, text treatment and amount of text are what won. Keep them.
2. **Change the minimum.** The best ads changed two nouns ("same words, same gag") or one word ("Minoxidil → T-boosters"). Every extra change is a new risk.
3. **Decode before you write.** Why does it stop the scroll? Why is the scene there? What is the hidden (often sexual) meaning? What belongs to THEIR product?
4. **Inventory every pixel.** KEEP or SWAP for every element, with the reason, before any prompt. This one step took first-try validation from 0 % to 60–76 %.
5. **Their product world never survives.** Material, flavour, symbol, body part, brand slot, innuendo object, packaging, props of their customer.
6. **The image shows our customer's problem or result**, in his words, at his age, on his angle — named explicitly.
7. **Real facts only.** Price, offer, guarantee, stats come from the brand file. Never invent a number, a deadline, a signature.
8. **The product is sacred.** Exact replica, real proportions, in the template's spot and gesture. Logos outside the label = the official logo file, pasted by script (D19).
9. **Never water an ad down to pass a filter.** Switch engine, render the scene only, composite the real product and exact text.
10. **The reviewer's verdict is law, the latest one wins, and a validated try is frozen.**
11. **Every miss becomes a rule; every win gets a "why".** The rulebook only grows. Lint enforces what can be checked mechanically.

---

## 2. Quick start

```bash
ssh vps-claude
export SKILL=/root/claude-vault/skills/static-ads
export SAC_WORKDIR=/root/workspace/<brand>-remix          # out/, batch/, brand.json, feedback/, pages/
mkdir -p $SAC_WORKDIR/{batch/templates,batch/prompts,out,feedback,pages}
cp $SKILL/brand.json $SAC_WORKDIR/brand.json   # blank template: fill it from BRAND-KIT.md
cd $SAC_WORKDIR

# specs (by hand, or drafted from 1-understand hand-off briefs)
python3 $SKILL/scripts/brief2spec.py batch/s1specs.py /root/workspace/<brand>-kit/briefs/*.json
python3 $SKILL/scripts/lint.py batch/s1specs.py                   # must print LINT OK

# generate ad N (lint → engine chain → composite; logs batch/calls.jsonl)
python3 $SKILL/scripts/srun.py batch/s1specs.py 1
for n in $(seq 1 10); do echo $n; done | xargs -P 5 -I{} python3 $SKILL/scripts/srun.py batch/s1specs.py {}

# pages, stats, Loom
python3 $SKILL/scripts/build_sam.py            # pages/review.html (only ads to review)
python3 $SKILL/scripts/build_samfinal.py       # pages/final.html + batch/sell/
python3 $SKILL/scripts/build_validated.py      # pages/validated.html + batch/validated/
python3 $SKILL/scripts/stats.py --ads 10
bash $SKILL/scripts/ingest_loom.sh "<loom url>" s1
```

---

## 3. The pipeline, step by step

### Step 1 — Brand intake (once per brand)
- If the brand has no analysis yet, run **`1-understand/`** first (`1-understand/new-brand-worksheet.md`) (product sheet, mechanism map, avatar, top-5 angles, headline bank; founder sign-off).
- Fill `BRAND-KIT.md`, then `brand.json` from it (`BRAND-KIT.md`, section "brand.json — key by key"): product lock sentence, product photo + cutout, wordmark + icon, offer + allowed prices, proof
  claims, avatar (age/look, core problem, hiding behaviours, what he tried, pleasure he keeps, proud proof), mechanism, angles (one default),
  competitors, banned words, compliance, angle keyword, visual checks.
- Product photo = Image 1 of every OpenAI call (sharp, label readable). Cutout = RGBA for composite.py (clean edges).
- Write the spec constants: avatar look (`OLD`), ingredient look, capsule look, icon-only sentence, `STD` keep-lines.
- The research is locked after this step (R5): batches never re-research.

### Step 2 — Template collection
- The reviewer provides the templates (or the `1-understand/new-brand-worksheet.md` §8 intake). Accept every template (R1); sort into concept families (R2); one ad per template (R4).
- Copy into `batch/templates/` with names whose sorted order is the ad order; real extensions (D10). Ad number = rank in that list (D13, linted).
- Batch size per review round: **10** (plus the redos) (D12).

### Step 3 — Template DNA read (per template, full resolution)
Write, before anything else:
- **why** — the scroll-stop trick in one sentence (A1).
- **dna** — everything that exists because of THEIR product: material/texture/flavour, symbol, body part, brand slot, copy formula, innuendo object,
  packaging — and its replacement (A2, A7).
- **scene** — why the scene is where it is; does the reason hold for us? If not, the place where OUR problem shows (A3, A18).
- **sexual reading** — what the objects/words really mean; ours stays as sexual and tied to our angle (A4).
- **visual trick / verb / shape** — the trick to copy literally (A21), the action (A17, A30), a shape/function equivalent for our problem (E6).
- **production method** — illustration, photo, text-only, photo + pasted product (→ A25), painted text (→ D5).
- **structure** — before/after (A23), split body (A9), progression (A16), table/UI (E13); **shock level** (A15); **render style** (C5); **text treatment** (A10).

### Step 4 — Angle choice
- Pick the research angle the template naturally carries (A5). Same angle as ours → keep their words and their visual mechanism (A6, A19).
- Template on one of our angles (man boobs, drive) → stay on it (A31). Template on an angle outside our research → fuse with the default core problem (A14).
- Spread angles inside each concept family (R3); favour the most aggressive ones (A33).
- Every headline names the core problem explicitly (A24, B2). Stranger test (B14).

### Step 5 — Spec with the KEEP/SWAP pixel inventory
- One dict per ad in `batch/sNspecs.py` (2-make/spec-format.md). Required: `why dna scene placement inventory(≥5) visual texts engine`.
- Inventory first: setting, each prop, each person, light, camera, each text block, product spot → `KEEP …` / `SWAP X → Y (reason)` (A13).
- `placement` copies the template's product spot and gesture (A8, C17). `texts` = one line per template text slot, same count, exact strings (B1, B13).
- Copy rules: benefits vs what he tried (B3), clear rival + clear problem (B5), no jargon (B4), no Autoship (B7), his real behaviours (B8),
  proud proof (B9), aggression = precision (B10), concede the pleasure (B11), simplest words (B15), stats as benefit claims (B16),
  twists literally true (A27), villain = mechanism (A28), known reference swapped (B17), routines because of the problem (B18), his words (B19),
  real facts only (B20). Deadline only if the template has one (`template_has_deadline`) (B6). Signature only if it has one (`template_has_signature`) (B12).
- Engine per spec (Step 7). Sexual/skin templates: `sexual=True`, `fallback="seedream_comp"`, `sd_prompt`, `composite` with EVERY product placement (D1, D6).
- From 1-understand hand-off briefs: `brief2spec.py` drafts the fields; you rewrite `visual` and do the judgment (`2-make/spec-format.md` "Input from 1-understand").

### Step 6 — Lint (blocking)
`python3 $SKILL/scripts/lint.py batch/sNspecs.py` — any error = nothing is sent (srun.py re-lints the whole file every call).
It checks: required fields, inventory ≥ 5, placement, banned words (generic + brand), competitor names, signed quotes (B12), invented deadlines (B6),
core-problem keyword (B2), ingredient visual checks (C2), sexual → fallback (D1), scene engines → sd_prompt + composite (D1/D7), product count parity (D6),
`seedream_full` banned (D7), bare wordmark text lines (D8), emoji in composite (D9), prices (B20), template rank (D13). Read the warnings too.

### Step 7 — Engine chain (2-make/engines.md)
| Template | Engine |
|---|---|
| Text on a flat background | `pure_comp` — composite.py only (zero spelling risk) |
| Normal | `openai` — gpt-image-2 images/edits, quality high, 1024², Image 1 = product photo, Image 2 = template; prompt = LOCK → inventory → DNA → scene → placement → changes → text → CONS |
| Sexual / skin / bare chest | `openai` + `fallback="seedream_comp"`, or straight `seedream_comp`: Seedream renders the scene only (no text, no product), composite.py adds the real product + exact text |
| Text painted into the scene | Nano Banana Pro (`kie_gen.py --model nano`) |
| Photo with a pasted product, or failed twice by regeneration | **A25 method**: Seedream minimal edit of the template itself (keep ratio, `--aspect portrait_16_9`) → `jarswap.py` masked product swap → composite.py text |
srun.py prints `OK` only if a new file exists (D10); refusals fall back automatically when the recipe is filled, otherwise it stops and says so.

### Step 8 — Composite (2-make/composite.md)
Fractions of W/H; product `x` = centre, `y` = bottom edge, `h` = height (real aspect kept); one text block per template slot, positions and spacing measured
on the template (C9); DejaVu for ✓ ✕; no emoji (D9); strikes for crossed prices; `noshadow` for floating/head products. Re-renders are free — iterate until it matches.

### Step 9 — Full-resolution QC (2-make/qc-checklist.md)
Every image, at full resolution, next to its template, in the main context (never a subagent, never a thumbnail). Product identical and to scale,
text exact (zoom on every logo: icon only), image shows the problem, nothing of their world left, avatar age, hands, before/after obvious,
style kept, one-second test. Fix before the reviewer sees it; log each fix in the round's QC log (Sam round 3 caught 13 defects this way).

### Step 10 — Review page (2-make/review-and-pages.md)
`build_sam.py` → only ads still to review, each with template + every try + decode + inventory + backend prompt. Thumbnails link full PNGs.
Serve it on a `<name>.machineroom.app` handle inside the wildcard block (noindex, clean URLs). Send the link; ask for a Loom, ad by ad, saying the number.

### Step 11 — Loom review
The reviewer records one Loom per round. Don't answer piecemeal during the review; wait for the whole Loom.

### Step 12 — Verdict ingest (3-improve/feedback-loop.md §1–2)
`ingest_loom.sh` (yt-dlp + mr-transcribe API) → read the full transcript yourself → resolve garbled numbers/words against the page →
verdict table per ad → `validated.json` (vocabulary: "✅ Validated (first try)", "✅ Validated (redo 1)", "✅ Loom N (after fix)", "❌ reason") →
`sell_override.json` for every "try N was better" (frozen, A20; latest verdict wins, A26).

### Step 13 — Redo
Redo every ❌ changing only what was named (A20); a liked layout becomes Image 2 via `tpl_abs` (A22); bring back elements he preferred from earlier tries;
apply each dictated fix to every other ad it fits (D11); build against the full rulebook (D11); add the next 10 new templates (D12). Lint → generate → QC.

### Step 14 — Feedback loop (3-improve/feedback-loop.md §3–5)
For every WIN: the mechanism that made it work → an E rule if new. For every MISS: root cause (not symptom) → permanent rule (new ID or an extension,
with Evidence) → lint check if mechanizable (generic in lint.py, brand-specific in brand.json) → prompt block if it is a generation habit.
Append the round to the protocols log; add the Loom's rows to the coverage matrix (every feedback item → a rule; no empty cell).

### Step 15 — Rules + lint update
`3-improve/rules.md` (generic, shared IDs with wildhorn-static-ads) and the brand's own LESSONS file. Rebuild the rules page (`build_lessons.py`).
Never delete or weaken a rule; refine it and keep the history line (C2 freeze-dried → fresh).

### Step 16 — Stats (3-improve/stats.md)
`stats.py` after every round: first-try %, after-one-fix %, final %, hit rate, generations per validated ad, rounds per ad, refusals by engine.
Report them with the review link. A drop = look for the rule the misses share.

---

## 3b. What the reviewer says → what it means → what to do

Founders review fast and in their own words. These phrases came back again and again in the Wildhorn Looms; map them before acting.

| He says | It means | Do |
|---|---|---|
| "Great" / "great job" / "perfect" | validated | ✅ in validated.json; write the WHY if he asks for a feedback loop on it (E rules) |
| "Try one was better" / "I like the try two" | that try is the sell version and frozen | `sell_override.json` → that try; never regenerate it (A20, A26) |
| "Keep the B8" / "do not change" | frozen | same as above |
| "You can put it as a success" | validated even if he asks for an improvement | ✅ + optional improved version as a new try, sell stays |
| "Make me another version" | a different IDEA, not new wording | new concept on the same template (C8) |
| "Change only the wording" / "respect the style of try 2" | layout and type are right | `tpl_abs` = that try, change only the slot (A22) |
| "Not on the angle" / "I don't know why you get out of the angle" | the headline doesn't name the core problem, or the image doesn't show it | name it in every line + show it (A24, C1); check A31 if the template is on another of our angles |
| "Not aggressive enough" / "make it more shocking" | precision on the deepest pain; match their shock | B10, A15, C18 |
| "I don't understand on the first read" | stranger test failed | name the thing + what it does, simplest words (B14, B15) |
| "Why did you put X? It's their product" | template DNA leak | A2 / A7 / C5 — and add the object to the inventory checklist |
| "Why is it in the shower/bed?" | scene copied for their reason | A3 / A18 |
| "You should have just copied it" | the template already worked for our buyer | A6 / A19 — word for word |
| "Use another model" / "GPT didn't let you" | refusal watered the ad down | D1 / D7: scene engine + composite, never sanitize |
| "Look at how they made it" / "understand the model they use" | production method mismatch | A25 |
| "Find why you failed and never do it again" | root cause + permanent rule, not a patch | 3-improve/feedback-loop.md §4 |
| "Do it again on the other ads" / "apply it everywhere" | the fix is a principle | D11 |
| "Make me the ones that don't go and the next 10" | round cadence | D12 |

## 3c. Worked examples (end to end)

**S23 — validated first try ("really great understanding").** Template (Happy Mammoth): split image, moon texture vs cellulite legs, "this belongs on the
moon". Decode: the pun is a SHAPE match. Our problem has a shape too: a round beer belly ↔ a full round moon (E6). Inventory: KEEP the split, the black
space + moon, the two type treatments, the tiny disclaimer; SWAP legs → round beer belly in profile, bottle → jar on the orange half circle. Texts: same 3
slots ("THIS SHAPE / BELONGS / ON THE / MOON" · "NOT ON / YOUR / BEER BELLY" · disclaimer). One OpenAI call. Full prompt in 2-make/engines.md.

**S11 — 4 reviews, then validated (the costliest ad, and where D6, A21, A25 came from).** Template (Primal Viking): a couple in bed; the woman's HEAD is the
product jar; second jar bottom right; big text block. Round 2: OpenAI refused (sexual) → Seedream scene + composite placed only ONE jar → "you should have
put the girl with the jar on her head" → **D6** (lint counts products vs placement). Round 3: two jars, but photoreal with a jar on top of her head →
"the face of the girl IS the product… painting style" → **A21**. Round 4: still regenerating whole scenes → "review the ad, understand the model they use" →
**A25**: Seedream edited the template itself minimally (aged the man, removed the small jar and the text, kept 9:16), `jarswap.py` swapped only their head jar
for ours with a masked gpt-image-2 edit, composite.py wrote the text (Oswald + DejaVu ✓). Loom 5: "great job on the last one".

**S18 — the action and the product form.** Template (Cowboy Colostrum): a spoon pours powder into his coffee. Round 1: capsules next to a beer (objects,
not the action) → **A17**. Round 2: organ powder poured into the beer — but we sell capsules → "no powder involved" → **A30**; and the logo was misspelled on
tries 1 and 3 → **D8**. Round 3: beer poured from a bottle into his pint, capsules beside the open jar, horn icon only → "great".

**S74 — Seedream must never write.** Template (RYZE): two stomach photos, "BEER BELLY? CAN'T RELATE.", deal block. OpenAI refused; the full-ad Seedream
fallback wrote "crossed" on the image and put the headline on the label → **D7**. Re-done as a Seedream scene with empty bands + composite text/price/strike.
Then the reviewer: "two lean bellies — it should be fat on one, lean on the other" → **A23**. Final: one fat, one lean, real jar, exact deal block → "great".

**#75 (run 1) — the origin of the pixel inventory.** A kids'-bedtime template was adapted keeping the kids' beds; the redo inventoried every element and
swapped only what belonged to their customer (game-night props, a tired dad, an older man) → "amazing… you could have done this from the first try" → **A13**.
The Sam batch made it mandatory and linted: first-try validation went from 0 % to 60–76 % per round.

## 3d. Where this sits in the blueprint (blueprint.machineroom.app, steps 0–5)
The brand-level process on the blueprint site is the frame; this skill is its steps 2–5 done at production quality.
| Blueprint step | Who | Output |
|---|---|---|
| 0 · The engine | this skill (+ ad-blueprint-gpt-image-2 for URL-only prompt blueprints) | — |
| 1 · Market research (35 competitor ads + video transcripts + TrendTrack) | `1-understand/` | top 5 angles, headline bank, avatar, formats, offer, weaknesses — founder sign-off |
| 5A · Brand kit (saved once) | `1-understand/` → `BRAND-KIT.md` + `brand.json` | research, product sheet, product photo, creatives log |
| 2 · Concepts: 1:1 adaptation, one ad per template, angles spread per family | `1-understand/` briefs → specs in `2-make/` (Steps 2–5) | specs |
| 3 · Generation + QC | this skill (Steps 6–9) | images, QC log |
| 4 · Delivery: comparison site + demo link | this skill (Step 10, review-and-pages.md) | review / final / validated pages |
| 5B · More concepts (new templates, no new research) | this skill, reloading the kit | next batch, same loop |
System rules R1–R14 from the site are in 3-improve/rules.md §R (any template accepted, sort by family, one ad per template, research once,
side by side, English, only research angles, headlines from research unless the template's words already carry the angle, decode protocol, same amount of text).

## 4. The 30 non-negotiable rules
(Full list with evidence: 3-improve/rules.md — A1–A33, B1–B20, C1–C18, D1–D13, E1–E13, F1–F13, R1–R14.)

1. **A13 Pixel inventory first** — every element KEEP/SWAP with a reason before any prompt; lint requires ≥ 5 lines.
2. **A1 Decode why it works** — the scroll-stop trick in one sentence.
3. **A2 Template DNA** — nothing of their product world survives (material, symbol, body part, logo/brand slot, copy formula).
4. **A3 Scene logic** — why is the scene there? Move it only to where OUR problem directly shows (A18), never to an indirect consequence.
5. **A4 Sexual reading** — decode the innuendo; ours is as sexual and tied to our angle; the visual carries the line's meaning.
6. **A6 Same angle → their words and their visual mechanism** — copy word for word; A19: read the line as our customer before changing it.
7. **A7 Re-derive category objects** — their innuendo object becomes our equivalent; A29: keep the idea with our own mechanism.
8. **A8 Placement and gesture copied** — fingers around it, on the lounger, in front of the face; C17 same size as theirs.
9. **A11 Avatar age everywhere** — every customer shown is our avatar, sexual scenes included.
10. **A14 / A31 Angle** — default core problem fused into off-research angles; a template already on one of our angles keeps only that angle.
11. **A15 Match the shock level**; A16 progressions face the result left → right; C18 before = maximum pain, after = maximum reward.
12. **A17 / A30 Copy the action** — the template's verb, in a form our product really has (capsules aren't powder).
13. **A20 Validated try is frozen** — redos change only what was named; liked layout = `tpl_abs` (A22); C13 never redraw an illustration that worked.
14. **A21 Copy the visual trick literally** — her face IS the product → our product IS her face, same render style.
15. **A23 Before/after stays before/after** — one problem state, one solved state; C12 difference obvious at first glance.
16. **A24 Name the core problem in every headline/bubble** — nothing that reads as another category.
17. **A25 Use the template's production method** — photo + pasted product → edit the template minimally, masked product swap, script text, keep the ratio.
18. **A26 Latest verdict wins** — sell_override.json, never touched again.
19. **B1 / B13 Same amount of text** — nothing added, not even a tie-in line.
20. **B2 Name the problem, not an age, and in full** ("beer belly", not "belly", not "men over 40").
21. **B6 No invented deadline**; B20 no invented price, stat or number — brand.json only.
22. **B10 Aggression = precision on the deepest pain**; B9 proof object he is proud to see; B8 his real hiding behaviours.
23. **B14 Stranger test** + B15 simplest words.
24. **C1 The image shows the problem or the result.**
25. **C2 / C14 / C15 Ingredient visual** — recognizable, fresh, appetizing, never generic, never ambiguous (no killed animal, dung, blood); the format reveals the source in one second.
26. **C5 Keep the render style**, swap their person and every leftover prop (F11).
27. **C6 Product = exact replica at real proportions**, never covering the hero; C7 no product where the template has none.
28. **C9 Text placement and spacing = the template's**, centred on its anchor.
29. **D1 / D7 Never water down; Seedream = scene only** — refused ads → scene engine + real product + exact text by script; D6 fallback parity.
30. **D8 Icon only outside the label; D10 OK = a new file on disk; D13 the template is the ad number's template; D2 full-res QC before showing.**

---

## 5. The anti-regression system

The rulebook only grows. Five mechanisms make sure a lesson learned once is applied forever:

1. **One rulebook, phrased for any brand** — `3-improve/rules.md` (+ the brand's LESSONS file). Every rule has its Evidence (the ad + the Loom). Rules are
   extended or refined, never deleted; contradictions are resolved explicitly (table at the end of 3-improve/rules.md). IDs are shared with wildhorn-static-ads.
2. **Blocking lint** — `scripts/lint.py` runs before any generation (srun.py calls it on the whole spec file). Generic checks in code; brand checks
   (bans, competitors, angle keyword, ingredient regexes, prices) in brand.json. A rule that can be expressed as a regex or a count must be in lint.
3. **Mandatory decode fields** — `why`, `dna`, `scene`, `placement`, `inventory` force the thinking before the prompt.
4. **Frozen tries** — `sell_override.json` + `tpl_abs`: what the reviewer validated can't be regenerated away. Latest verdict wins.
5. **Protocols log + coverage matrix** — every round's wins (why → repeat) and misses (root cause → rule) are logged; every piece of feedback maps
   to a rule (3-improve/feedback-loop.md: 231 items from 14 reviews, 0 uncovered).

Before each batch: re-read 3-improve/rules.md (or at least §4 above + the rules added since the last batch), lint every spec, and check the D13/D10 template paths.

---

## 6. Running a batch (commands)

```bash
export SKILL=/root/claude-vault/skills/static-ads SAC_WORKDIR=/root/workspace/<brand>-remix; cd $SAC_WORKDIR

# Round N: write batch/sNspecs.py (redos of round N-1 + 10 new), then
python3 $SKILL/scripts/lint.py batch/sNspecs.py
ls batch/templates | nl | sed -n '<first>,<last>p'      # the template of each ad number (D13 — lint checks it too)
for n in <numbers>; do python3 $SKILL/scripts/srun.py batch/sNspecs.py $n; done 2>&1 | tee batch/logs-rN.txt
#   openai OK | REFUSED -> seedream_comp | seedream+comp OK | pure composite OK | LINT FAILED | D10 TEMPLATE MISSING

# QC at full resolution (Read each out/s_NN_vK.png next to its template); fix:
#   - wording only:   new spec with tpl_abs=<liked try>, change only the slot (A22)
#   - one object:     python3 $SKILL/scripts/jarswap.py out/s_NN_vK.png out/s_NN_v{K+1}.png X0 Y0 X1 Y1 --context "..."
#   - text position:  edit composite JSON, re-run composite.py on the same scene (free)
python3 $SKILL/scripts/build_sam.py && python3 $SKILL/scripts/stats.py
# send the review link → Loom → ingest → validated.json / sell_override.json → rules → next round
```

Parallelism: up to 5–6 OpenAI calls at once (`xargs -P`); ~110 s per image at high quality; ≈ $0.30 per image (estimate). Seedream scenes 1–3 min.
Log manual calls (A25 steps, jarswap fixes) in `batch/calls.jsonl` by hand so stats stay true.

Report to the reviewer after each round: review link · table `ad → last verdict → what changed → rule` · stats line · new rule IDs.

---

## 7. Stats to report (3-improve/stats.md)
| Metric | Wildhorn run 1 | Wildhorn Sam batch |
|---|---|---|
| First-try validation | 0 % | 71 % |
| After one fix | — | 87 % |
| Final | 100 % after 9 rounds | 100 % |
| % of generations validated (hit rate) | 30 % | 62 % |
| Generations per validated ad | 3.3 | 1.6 |
| Review rounds per ad | 2.5 | 1.4 |
Compute with `stats.py` from `calls.jsonl` + `validated.json` (+ `rounds.json`). Use the verdict-based first-try number.

---

## 8. Working with the reviewer (Adrien and any founder)
- Everything about this material is in **English** (pages, prompts, specs, replies).
- **Copy, angle choice, QC and Loom reading happen in the main context** — never delegated: a subagent summary loses the nuance these steps are about.
  Delegate only mechanical work (file searches, log reading, bulk renders).
- He reviews by number in a Loom; he doesn't read code. Give him links and tables, never commands.
- "Propose/list improvements" = text only; don't build without an explicit yes. "Another version" = another idea (C8).
- Validated ads leave the review page. Show every version of a redone ad so he sees the improvement (D3).
- He asks "why did it work?" as often as "why did it fail?" — answer both, in one sentence each, with the rule ID.
- End each round with a checklist table `request → status` (✅ done and verified / 🔨 in progress / ⏳ blocked + reason).

---

## 9. Boundaries and safety
- Write only in the brand's working folder and this skill's folder. Live pages under `/srv/**` and the Caddyfile are changed only on purpose,
  with the VPS conventions (wildcard handle, noindex header, clean URLs, snapshot + directive-count diff + `caddy validate` before reload).
- Never print or store API key values; scripts read `/etc/secrets/*` paths.
- Heavy media (Loom mp4s, template archives, exports) go to Backblaze B2 via `mr-archive`; text, specs and logs stay on the VPS.
- Transcription = `mr-transcribe` (OpenAI API). Never run local whisper in bulk.
- Compliance: no fake testimonials presented as real, no forbidden claim numbers, no doctors/celebrities, no body before/after presented as a real customer (brand.json `compliance`).

---

## 10. Map of the references

| File | Read it when |
|---|---|
| `3-improve/rules.md` | Before every batch. All rules A1–A33, B1–B20, C1–C18, D1–D13, E1–E13, F1–F13, R1–R14, generalized, each with Evidence; resolved conflicts. |
| `3-improve/feedback-loop.md` | After every Loom. Ingest → verdict table → wins/misses → rules → records → redo; case studies of every round (run 1 L1–L9, Sam SL1–SL5); the Loom coverage matrix (231 items → rules). |
| `2-make/spec-format.md` | Writing specs. Every field, srun.py prompt assembly, shared constants, 7 real specs (openai, fusion, pure_comp, seedream_comp, tpl_abs redo, sexual fallback D6 failure + A25 fix, timeline unlock), 1-understand brief → spec mapping. |
| `2-make/engines.md` | Choosing/debugging an engine. Chain, LOCK/CONS verbatim + generic, Seedream rules and real prompts, the A25 method step by step, masked edits, refusals and failure modes, timing/cost, aspect ratios. |
| `2-make/composite.md` | Writing a composite JSON. Every option with real validated examples. |
| `2-make/qc-checklist.md` | Before showing any image. Spec review + product/text/angle/people/style checks + one-second test + QC log format. |
| `2-make/review-and-pages.md` | Numbering, the pages, verdict files, sell version logic, exports, serving pages on the VPS. |
| `3-improve/stats.md` | Metric definitions, benchmarks, how to compute, measurement caveats, targets for a new brand. |
| `BRAND-KIT.md` | Starting a new brand: every fact to collect (voice, product, label, offer, proof, avatar, angles, bans, logo, fonts, product photo + cutout), brand.json key by key, what is Wildhorn-only. |
| `2-make/first-batch.md` | The new brand's first batch: hand-off from `1-understand/`, working folder, spec constants, templates, first 10 ads, what to expect, pre-flight checklist. |
| `scripts/README.md` | What each script does, what changed vs the Wildhorn originals, every constant to set per brand. |

Source material (read-only, Wildhorn): `/root/workspace/wh-remix/LESSONS.md`, `/root/workspace/wh-remix/sam-batch/` (specs s1–s4, srun.py, validated.json,
sell_override.json, calls.jsonl), `/root/workspace/wh-remix/feedback/loom-*.txt`, `https://blueprint.machineroom.app` (/protocols, /lessons, /sam-final),
checkpoint `/root/workspace/_checkpoints/wildhorn-batch-test.md`.

---

## 11. Session checklists

**Start of a session on an existing batch**
1. `~/.claude/bin/checkpoint <project>` (Mac) or read the brand's checkpoint on the VPS — never re-explore from scratch.
2. Read `3-improve/rules.md` rules added since the last batch (and the brand LESSONS file).
3. `cat batch/validated.json batch/sell_override.json`; `stats.py` — know where the batch stands.
4. Check no other session is working on the same folder (`ls -lt batch/ out/ | head`).

**End of every round (the report to the reviewer)**
```
Review link: https://<brand>-review.machineroom.app/review
| Ad | Last verdict | What changed | Rule |
|----|--------------|--------------|------|
| S18 | ❌ powder in the beer | beer poured into the pint, capsules beside, icon only | A30, D8 |
Stats: first try 71 % · after one fix 87 % · hit rate 62 % · 1.6 generations / validated ad
New rules: A30 (product form), D13 (template rank)
Next: Loom on S11 S18 …
```
Then write the checkpoint (state, files, next step) so the next session starts in one read.
