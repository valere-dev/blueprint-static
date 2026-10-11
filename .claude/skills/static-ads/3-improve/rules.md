# Rules — the anti-regression rulebook (generalized)

Source of truth for every batch. Built from `/root/workspace/wh-remix/LESSONS.md` (A1–A26, B1–B16, C1–C11, D1–D10, E1–E7),
the protocols page (`/srv/blueprint/protocols.html`: QC logs, golden rules, feedback tables), the blueprint system rules
(`/srv/blueprint/index.html` R1–R14) and a line-by-line audit of every review Loom transcript. Nothing from the Wildhorn rulebook was dropped;
wording is generalized, the original case stays as **Evidence**.

**One rulebook, shared IDs.** The Wildhorn edition of this skill (wildhorn-static-ads, `/root/claude-vault/skills/wildhorn-static-ads/wildhorn/lessons-wildhorn.md`) and this
generic rulebook use the SAME IDs for the same rules. Rules marked **added from Loom audit** (A27–A31, B17–B19, C12–C18, D11–D13, E8–E13) were written there
from the 2026-10-02 audit and are generalized here. Rules marked **added in this skill** (A32, A33, B20) and the sections **F** (prompt craft, from the QC
logs) and **R** (blueprint system rules) exist only here; the next new rule in each series continues after the highest ID of both files
(A36+, B23+, C23+, D22+, E14+, F14+).

How to read a rule
- **Rule**: the instruction, brand-agnostic. Placeholders: `{BRAND}` brand name · `{PRODUCT}` the product · `{PRODUCT_NOUN}` jar/pouch/bottle ·
  `{AVATAR}` the buyer persona · `{CORE_PROBLEM}` the default pain (Wildhorn: beer belly) · `{MECHANISM}` the research villain (estrogen) ·
  `{INGREDIENT}` what the product is made of (bison organs) · `{RIVAL}` what he already uses (fat burners) · `{PLEASURE}` what he won't give up (beer) · `{ICON}` the brand icon (horn).
- **Evidence**: the Wildhorn ad and review that created it. Loom ids: `L1` = batch-01 written feedback (no transcript) · `L2…L9` = `feedback/loom-b2…b9.txt` (run 1, ads #1–#79) ·
  `SL1…SL4` = `feedback/loom-s1…s4.txt` (Sam batch, ads S1–S83) · `SL5` = Sam Loom 5 (no transcript; verdict recorded on /protocols).
  "QC Bn" = my own full-resolution QC log on batch n.
- **Enforced**: `lint` (blocks generation), `prompt` (written into LOCK/CONS or the spec), `QC` (full-res checklist, 2-make/qc-checklist.md), `process`.

Precedence when two rules seem to collide: a later, more specific rule refines an earlier one; the rulebook is only extended, never shortened.
Known collisions and their resolution are listed at the end ("Resolved conflicts").

---

## A. Decode — before writing anything

### A1 — Decode why the template works
**Rule:** Before any prompt, write the scroll-stop trick in one sentence (visual joke, reframe, shame, desire, proof object, shock, scarcity…). Ask why every element is there.
**Evidence:** L1 #63 "great template, badly adapted" → decode first. L9 [03:31] "make a deep analysis of every ad so you understand why everything is there". Wildhorn Loom O2 [07:49] O74 "great, but I would have copied the template more — do it again": our try kept the idea but moved the man to the edge, changed his framing and the prop cluster → redo = layout, framing, pose, prop cluster and colours copied 1:1, only their product/customer swapped.
**Enforced:** lint (field `why` required) + process.

### A2 — Template DNA: never import their product world
**Rule:** List everything that exists only because of what THEY sell — their product, material/texture/flavor (chocolate pour, colostrum milk, brisket), packaging, brand logo or brand slot ("The Angry Nose Lab"), the symbol of their product (hair ribbon), the body part of their problem (arm, nose, hair), their copy formula — and swap each one for OUR equivalent ({INGREDIENT}, our result symbol, our problem zone, our wordmark, the same copy slots filled with our facts).
**Evidence:** L4 #2 arm (B4) while we sell belly/man boobs; #23 competitor "Nose Lab" kept; #26 hair kept on a non-hair product (L3 [05:19]); #36 brisket in the background; #39 chocolate (a chocolate brand's ad). Protocol 0 table.
**Enforced:** lint (field `dna`) + QC.

### A3 — Scene logic
**Rule:** Ask why the scene is where it is (shower because hair falls in the drain; kid's bedroom because the product is for kids' sleep; bed because it is a sleep product). If the reason doesn't hold for {PRODUCT}, move to the place where OUR problem shows. The setting must fit the claim.
**Evidence:** L7 #70 shower copied for no reason (template = hair loss). SL2 S33 bed copied (template = sleep product) → kitchen, pushing a beer away. SL4 S56 "background doesn't make sense, but it goes".
**Enforced:** lint (field `scene`) + QC.

### A4 — Sexual / innuendo reading
**Rule:** Decode the hidden meaning (pineapple = vulva/taste, cream-filled log = phallus, eggplant, "drain him"). Our version is just as sexual AND tied to our angle; the visual carries the same meaning as the line. Never sanitize it into something meaningless. Mark the spec `sexual: True`.
**Evidence:** L1 #57 "concept is sexual, adaptation wasn't". L7 #57 not sexual enough, #61 missed the vulva innuendo, #69 visual didn't match the sexual line. L8 #69.
**Enforced:** lint (`sexual` → needs a fallback engine) + QC.

### A5 — Pick the angle the template naturally carries, from the research
**Rule:** Choose among the research's top angles the one the template already carries (for Wildhorn: beer belly, man boobs, wild vs farmed, "tested 3", anti-waste; drive for sexual templates). Never invent a promise or mechanism the research doesn't have.
**Evidence:** L1 review; blueprint R8 "only the research angles"; batch-02 #2 talked about muscle — not our mechanism.
**Enforced:** spec field `angle` + QC.

### A6 — Same angle as the template → keep their words AND their visual mechanism
**Rule:** When the template already speaks to our buyer on our angle, copy its lines word for word (swap only the subject/brand) and copy its visual mechanism applied to {PRODUCT} (their bottle gets fat → our {PRODUCT_NOUN} gets fat, label untouched).
**Evidence:** L1 #14 changed text although same angle; #16/#17/#18 headline structure/words were better. L2 #14. L6 #58 should have made the bottle fat. L7 #63 "Lose the beer belly / Let no one hit" — Step 2 changed = fail.
**Enforced:** QC + spec (`inventory` KEEP lines).

### A7 — Re-derive every category-bound element, innuendo objects included
**Rule:** Every element tied to THEIR product category is re-derived for ours. An innuendo object keeps its function but changes object (vaginal-probiotic pineapple → for a men's product: banana, glazed donut ring with the {PRODUCT_NOUN} through it). When their visual mechanism depends on their product (milking for colostrum), keep the idea (source → product) with OUR product's own mechanism.
**Evidence:** L8 #61/#69 pineapple kept; L9 #61 great after the fix, #69 "better but still doesn't make sense". L5 #37 "mechanism different than the example but still the same idea".
**Enforced:** QC.

### A8 — Copy the template's placement and gesture exactly
**Rule:** The product sits where theirs sits and is held the way theirs is held: fingers wrapped around it (not floating on a palm), on the lounger/sofa, in front of the face, in the woman's hand. Field `placement` copies the template.
**Evidence:** L8 #57 not properly in the woman's hand; #65 product should be on the lounger; #79 product in front of the face. SL3 S58 try 1 "properly copied the way she held the bottle".
**Enforced:** lint (field `placement` required) + QC.

### A9 — Split-body templates: one body cut exactly in half
**Rule:** One single body, same skin, same shorts, same pose; problem half vs solved half meeting on the centre line — the navel sits exactly on the cut.
**Evidence:** L8 #77 two different bodies; L9 #77 "the hole in the belly should be perfectly aligned".
**Enforced:** prompt + QC.

### A10 — Reproduce the template's special text treatment
**Rule:** Sunscreen bubbles, clay letters, handwriting, marker on glass: reproduce the treatment, never a flat font (painted text → Nano Banana Pro or `composite.py` `sunscreen`).
**Evidence:** L8 #65 wrote flat text on the body where the template had sunscreen bubbles.
**Enforced:** spec + engine choice (D5) + QC.

### A11 — Avatar age everywhere
**Rule:** Every person shown as the customer is {AVATAR} (Wildhorn: 45–60, greying) — sexual scenes included. Describe age and look in the prompt and forbid copying the template's person.
**Evidence:** L8 #79 young man; L9 #79 "perfect, the older guy". QC B2 #10 copied the template's young man. Sam QC S38/S42/S55 avatar age fixes.
**Enforced:** prompt (`OLD` string in specs) + QC.

### A12 — Replace the setting's props with props of OUR problem
**Rule:** Props tell the story: swap their customer's furniture for objects of our problem ({PLEASURE} cans, pizza, jeans that won't button, a scale) — not their props (kids' beds).
**Evidence:** L8 #75 kept the kids' beds of a bedtime-battle template.
**Enforced:** inventory SWAP lines + QC.

### A13 — The pixel inventory (#75 method, first-try rule)
**Rule:** Before any prompt, inventory EVERY element of the template — setting, each prop, each person, light, camera angle, every text block, product spot — and mark each KEEP or SWAP→our equivalent, with the reason. The prompt is written from this inventory. Minimum 5 lines.
**Evidence:** L9 [02:27] "#75 — you could have done this from the first try… every pixel of the scene, then what to change for the customer avatar". Sam batch first-try rate went 0 % → 71 % with it.
**Enforced:** lint (`inventory` ≥ 5).

### A14 — The core problem is the default; fuse other angles with it
**Rule:** {CORE_PROBLEM} is the default angle. When a template carries an angle outside our research (GLP-1 face, sleep, energy…), FUSE it: their mechanism + our core pain. Pure-drive ads stay allowed for drive templates but must make sense for the {CORE_PROBLEM} buyer. (See A31 for templates already on one of our secondary angles.)
**Evidence:** SL1 S2 GLP-1 faces missed the belly; S10 "why sexual and not beer belly?". SL2 S35 "Outperform your 30s" off-angle; S28 arcade = fusion done right (one extra stat row).
**Enforced:** QC + lint (angle keyword, A24/B2).

### A15 — Match the template's shock level
**Rule:** If their image is gross or shocking (worms out of a belly), ours is equally shocking for our problem (belly melting like wax) — never a tame substitute.
**Evidence:** SL1 S7 button popping was tamer than worms; SL2 S7 "let's make it more shocking".
**Enforced:** QC.

### A16 — Progressions read left → right toward the result
**Rule:** Silhouettes/profiles in a progression face the result (to the right), timeline left to right.
**Evidence:** SL1 S8; SL2 S8 "make it go to the right".
**Enforced:** prompt + QC.

### A17 — Copy the action, not just the objects
**Rule:** The verb of the scene is part of the winner: if the template POURS the product into the drink he already has, ours pours into his {PLEASURE}. (Check A30: the action must fit our product's real form.)
**Evidence:** SL2 S18 capsules next to the beer; the template pours powder into coffee.
**Enforced:** inventory + QC.

### A18 — Scene moves stay ON the benefit
**Rule:** Move the scene only to where OUR problem is DIRECTLY visible (belly in the mirror, belly on the scale, jeans button), never to an indirect consequence that could sell another product (shoelaces). The headline keeps the template's formula with our blunt benefit ("Smoother poops" → "Flatter bellies").
**Evidence:** SL2 S15 "could be a shoelace brand"; SL3 S15 "adapted perfectly to the problem".
**Enforced:** QC.

### A19 — Read the line as our customer before changing it
**Rule:** If the template's line already works for our buyer read as-is ("Lost my waistline — last seen 3 weeks ago" = he got slim), copy it word for word. Flipping a line that already works = fail.
**Evidence:** SL2 S14 flipped it; SL4 S14 "great" after copying.
**Enforced:** QC.

### A20 — A validated try is frozen
**Rule:** When the reviewer validates a try (or says an earlier try was better), that try is FROZEN: never regenerate it; a redo changes only what he named. Pass the validated try as `tpl_abs` (it becomes Image 2). Earlier elements he preferred (organs of version 1, foot on the scale) are brought back, not reinvented.
**Evidence:** SL3 S18/S58/S79 regenerated tries he liked; L3 #2 "first one was way better" (redrew a validated illustration); L3 #23 "first batch was better"; L8 #70 organs and scale of the first image were better; L9 #74 keep B8.
**Enforced:** process (sell_override.json) + spec `tpl_abs`.

### A21 — Copy the template's core visual trick literally
**Rule:** If a person's face IS the product, our {PRODUCT_NOUN} IS that face, in the same render style. Don't reinterpret the trick (jar on top of her head, photoreal) — reproduce it.
**Evidence:** SL2 S11 jar not on her head; SL3 S11 "the face of the girl is the product".
**Enforced:** inventory + QC.

### A22 — "Change only the wording" = same layout, type and style pixel for pixel
**Rule:** Use the liked try as the template (`tpl_abs`) and change only the words.
**Evidence:** SL3 S29 try 3 changed style when only the wording was wrong; SL4 S29 "great".
**Enforced:** spec `tpl_abs` + QC.

### A23 — A before/after template stays a before/after
**Rule:** One problem state vs one solved state — never two solved states. Object/fruit metaphors map to the problem's shape (bloated pear vs slim pear), not to the template's sexual symbol.
**Evidence:** SL3 S74 two lean bellies; S50 sexual orange instead of a belly metaphor; SL4 S50/S74 "great".
**Enforced:** inventory + QC.

### A24 — Every headline and bubble names the core problem
**Rule:** Name {CORE_PROBLEM} explicitly; anything that could read as another category (hangover, brain, generic win, "after-40 changes") is off-angle. Switching to the partner angle = her desire tied to his {CORE_PROBLEM}.
**Evidence:** SL3 S42 (must say it's for losing the beer belly), S52 (brain), S56 (reads like a hangover product), S80 ("after-40 changes" not understandable), S57 (woman angle). L8 #74 "Bigger. Harder." → "Flatter. Harder." SL4 all fixed.
**Enforced:** lint (angle keyword) + QC.

### A25 — Work out HOW the template was made, then use the same method
**Rule:** Before re-prompting a failed ad, identify the production method of the template. If it is a real photo with a product pasted in (simple composite), don't regenerate the scene: (1) Seedream edits the template itself with the smallest change (age the person, clear the text, nothing else); (2) `jarswap.py` swaps only their product for ours with a masked gpt-image-2 edit (mask excludes hands/hair); (3) text added by `composite.py`. Keep the template's aspect ratio (9:16 stays 9:16: `kie_gen.py --aspect portrait_16_9`).
**Evidence:** SL4 S11 "review the ad by screenshot and understand the model they use"; failed 3 times by regenerating; SL5 "great job on the last one".
**Enforced:** process (2-make/engines.md → A25 method).

### A26 — The latest verdict wins
**Rule:** His most recent verdict overrides earlier ones, even on a try he rejected before. Record it in `sell_override.json` and never touch it again.
**Evidence:** SL4 S42 "the first try was great, I validate it… do not change". SL2 S7/S9 "you can put it as a success".
**Enforced:** process (sell_override.json, validated.json).

### A27 — A twist must make literal sense for our problem — added from Loom audit
**Rule:** A pun or reversal built for their product ("size doesn't matter, thickness does" = penis) is rebuilt so it is literally true for {CORE_PROBLEM} ("Size doesn't matter… unless it's your beer belly!"). If the logic only worked for their product, rebuild the twist.
**Evidence:** L2 #11 [01:28] "a little less logical for the beer belly… make a version that corresponds better"; L3 #11 "I like the 11 more"; reused as S77, first try.
**Enforced:** QC.

### A28 — The villain is the research mechanism; the product is its killer — added from Loom audit
**Rule:** When the template has an enemy (a hormone, a deficiency, a habit) or personifies one (obituary, wanted poster, "X is not the problem"), the enemy becomes {MECHANISM} and {PRODUCT} is what beats it. Keep the template's sentence; swap symptom → {CORE_PROBLEM}, cause → {MECHANISM}.
**Evidence:** L3 #21 "The beer belly is not the problem. The estrogen driving it is." ("really great job"); L3 #24 "Estrogen was found dead" ("great"); L4 #23 "You're not fat. Your belly is estrogen." ("the text is really good"); S52 "This is not beer. This is estrogen."
**Enforced:** QC.

### A29 — Their image mechanism can't apply to our product → keep the IDEA with our own mechanism — added from Loom audit
**Rule:** If the template's visual mechanism depends on their product (colostrum is milked; organs can't be), keep the idea ("from the source straight into the product") and show it our way (rancher's board of tagged ingredients + the living source).
**Evidence:** L4 #37 "looks like we killed the bison… we are not selling colostrum" → L5 #37 "the mechanism has to be different than the example, but still the same idea… great job".
**Enforced:** QC.

### A30 — Product-form check: the copied action must fit our product's real form — added from Loom audit
**Rule:** Translate the template's consumption ritual (powder into coffee, scoop, shot) into our real form (Wildhorn = 2 capsules a day). The drink in the scene stays the drink HE already has, poured as itself; never invent a powder/liquid we don't sell.
**Evidence:** SL3 S18 [01:28] "if you put powder it makes no sense because there's no powder involved… the product are capsules" → try-1 idea (capsules beside) + beer poured into the pint → SL4 "great". Refines A17.
**Enforced:** QC.

### A31 — A template already on one of our core angles keeps ONLY that angle — added from Loom audit
**Rule:** If the template highlights one of OUR research angles (man boobs, drive), ours highlights only that angle; A14 fusion never overrides A6 (same angle → copy).
**Evidence:** SL3 S79 [15:47] "I will highlight the man boobs more than the beer belly… in the example they highlight only the man boobs. Try one is perfect." SL1 S10 drive template kept on drive.
**Enforced:** QC.

### A32 — The staging acts out the line — added in this skill (beyond the Wildhorn audit)
**Rule:** People and gestures perform what the headline says (she initiates → she is on top). Check pose and roles against the text before generating.
**Evidence:** SL3 S55 [09:16] "you should have put the woman on top since she's initiating… but it's good like this".
**Enforced:** QC.

### A33 — Favor the most aggressive angles; ration the soft one — added in this skill (beyond the Wildhorn audit)
**Rule:** Spread toward the sharpest pains (Wildhorn: beer belly, man boobs). The softer "supplements failed you" angle is used sparingly.
**Evidence:** L1 "#All: too many 'supplements failed you'"; protocol 2 "most aggressive angles first".
**Enforced:** process (angle spread per batch).

### A34 — Keep the template's term when our avatar uses it himself — added from Oct08 Loom
**Rule:** If the template names the problem with a word {AVATAR} already uses about himself ("dad bod", "gut", "man boobs"), keep that word exactly. A19 (read the line as our customer) wins over A24/B2 ("name {CORE_PROBLEM} everywhere") for that one term; the rest of the copy stays on {CORE_PROBLEM}. Put the kept term in the spec as `template_term` so the linter knows.
**Evidence:** Oct08 Loom — O08: I swapped the template's "Why You Can't Lose Your Dad Bod" to "…Your Beer Belly"; Adrien: keep "Dad Bod" (our avatar says it). Redo = text change only, image kept.
**Enforced:** lint (`template_term` present in the texts → the B2 core-problem check is skipped for that ad) + process.


### A35 — The angle is the core angle only — added from Loom O2
**Rule:** The ad's angle is ONLY one of the brand's core angles (Wildhorn: beer belly, libido, man boobs). Secondary benefits (sleep, focus, recovery, joints, energy) never carry an ad: not the headline, not the testimonial quote, not the scene or the pose. When the template sells one of those, swap it for {CORE_PROBLEM} and change the scene/pose so it SHOWS {CORE_PROBLEM} (a squat is a joints pose; a beer belly is shown hanging over the belt, out of breath). A secondary benefit may only sit in a list next to the core one.
**Evidence:** Wildhorn Loom O2 (09/10) — O99 "why you make better sleep? I don't want better sleep angle" (DAY 30 quote → "THE FIRST THING I NOTICED WAS MY BELT."); O47 "it's about stiff joints, so the guy is in this position, but for beer belly it should be something else"; O60 / O71 / O72 "make it more about beer belly" (DIALED IN BUT STILL GOT A BEER BELLY? · LOSE THE BEER BELLY. · BYE BYE BEER BELLY).
**Enforced:** lint warning (brand.json `angle_warn`, Wildhorn: `sleep` in the copy) + decode (angle field) + QC.
---

## B. Copy

### B1 — Same amount of text as the template
**Rule:** Same number of text slots, same length. No added context line, tagline, disclaimer or CTA the template doesn't have.
**Evidence:** L1 #4 added bottom line repeated the ad; #5 too much text; #6 extra text squeezed the bottom bar. Blueprint R10 (context line) was a mistake → replaced by R12.
**Enforced:** prompt (CONS "Render ONLY the listed text") + QC.

### B2 — Name the customer's problem, not an age; name it fully
**Rule:** "For stubborn {CORE_PROBLEM}", not "For men over 40". Say the full problem ("beer belly"), never the vague word ("belly").
**Evidence:** L1 #7; L7 #68 "beer belly, not the belly".
**Enforced:** lint (`men over N"`, brand `angle_keyword`).

### B3 — Benefits = the result he wants vs what he already tried
**Rule:** Never product features. Results he feels, compared with {RIVAL}.
**Evidence:** L1 #3; L2 #3 "much better"; L4 #30 arrows = results he feels + "she notices first".
**Enforced:** QC.

### B4 — No mechanism jargon
**Rule:** No word the avatar doesn't use ("conversion", "aromatase"). Say it so anyone gets it.
**Evidence:** L1 #11.
**Enforced:** lint (generic `conversion`; brand `banned`).

### B5 — Clear rival product + clear everyday problem
**Rule:** Fill the copy formula with a rival he really uses and a problem he really has ("3 fat burners a day just to button my jeans").
**Evidence:** L4 #38 vague rival + vague problem ("pills every morning" — for what?). L6 #53 smart comparison.
**Enforced:** QC.

### B6 — One-read clarity; a timeline only if the template has one
**Rule:** Every line says what it is about in one read. Add a deadline/timeline ONLY if the template has one — never invent one.
**Evidence:** L7 #65 "shirt off since day 21" — off for what?; L8 #65 "when there's no deadline, don't have the deadline".
**Enforced:** lint (digits+days unless `template_has_deadline=True`).

### B7 — Never mention Autoship / subscription
**Rule:** Use the offer framing of the template ("50% off for life") without naming the subscription.
**Evidence:** L6 #51.
**Enforced:** lint (generic).

### B8 — The avatar's real hiding behaviours
**Rule:** He hides by sucking in, baggy shirts, shirt on at the pool, endless diets — use behaviours from the research, not assumed ones (compression shirts).
**Evidence:** L6 #54 compression shirt (validated anyway, "misunderstanding about our avatar").
**Enforced:** lint (brand `banned`).

### B9 — Proof object = something he is proud to see
**Rule:** His old jeans fit, seeing his feet — not a technical detail ("1 notch tighter").
**Evidence:** L5 #43/#44 "one notch tighter is not understandable"; L6 #44 B6 "even better than the example… my customer is not that smart".
**Enforced:** QC.

### B10 — Aggression = precision on the deepest pain
**Rule:** Go to his most private shame (bedroom lights on). Not aggressive enough = fail.
**Evidence:** L6 #47 "the greatest"; L7 #62 "way not aggressive enough"; L7 #65 "be more aggressive"; L1 #9 loser lines brutally specific.
**Enforced:** QC.

### B11 — Concede the pleasure, attack its consequence
**Rule:** "{PLEASURE} is fun. {CORE_PROBLEM} isn't." Name what he won't give up and attack the side effect.
**Evidence:** L3 #22 "amazing"; L4 #31 keep your beer.
**Enforced:** QC.

### B12 — Signed-review format keeps a name; never add a signature the template lacks
**Rule:** If the template is a signed customer review, keep the format with a first name + initial. Never add a signature when the template has none. (Set `template_has_signature=True` in the spec — the linter otherwise blocks signed quotes.)
**Evidence:** L8 #79 "it was a customer review, you should have put the name"; compliance: no fake testimonials presented as real.
**Enforced:** lint.

### B13 — "Same amount" means nothing added at all
**Rule:** Not even a small tie-in line.
**Evidence:** L8 #57 added a line at the bottom.
**Enforced:** prompt + QC.

### B14 — Stranger test
**Rule:** A buyer who never heard of {BRAND} must understand WHAT it is and WHAT it does on the first read. Name the thing.
**Evidence:** SL1 S9 "You can't farm this" too abstract → "Wild Bison Organs. Never Farmed."; L7 #57 not easily understood that it's for weight loss.
**Enforced:** QC.

### B15 — Simplest words win
**Rule:** If a plainer phrase exists, use it ("see your belt buckle again" → "a flat belly again").
**Evidence:** SL2 S29; SL3 S80 "after-40 changes hit different" not understandable.
**Enforced:** QC.

### B16 — Stats are benefit claims phrased like the template
**Rule:** "92% reported clearer minds" → "93% saw their {CORE_PROBLEM} shrink*", with the survey footnote. Only real stats (B20).
**Evidence:** SL2 S24 "felt the difference" too soft; SL3 S24 "great".
**Enforced:** QC.

### B17 — Known-reference swap: their famous rival → the one OUR avatar already knows — added from Loom audit
**Rule:** Minoxidil, Ozempic, coffee, edibles, energy drinks → what the avatar already uses ({RIVAL}, T-boosters, GLP-1 shots, {PLEASURE}). Change only that word.
**Evidence:** L3 #25 "This jar is putting T-BOOSTERS out of the game" ("really great… apply it everywhere"); L2 #19 "You can't feel a beef liver pill" ("excellent"); L1 #25 "your 12 supplements — nobody gets it"; S42 minoxidil → fat burners; S47 fibermaxxing → organ-maxxing.
**Enforced:** QC.

### B18 — A "your X routine" line names a routine he has BECAUSE of the problem — added from Loom audit
**Rule:** Before copying a "your X routine" line, check the avatar really has that routine; pick the one he has because of the problem (hiding the chest: baggy tees, hoodie). The headline names the problem the routine fails at.
**Evidence:** L1 #8 "problem not clear"; batch-02 #8 "belly-fat routine doesn't exist in his life"; L3 #8 "I'm not sure we hit the angle"; L4 #8 "Your hide-the-chest routine may be letting you down" = "amazing, deep into the avatar and the angle".
**Enforced:** QC.

### B19 — Keep the transformation about HIS body, in his words — added from Loom audit
**Rule:** Use the phrase he says about himself and rhyme it into our world ("FROM 'DAD BOD' TO 'BISON BOD'"); never turn the customer's problem into a product problem ("from farmed to wild").
**Evidence:** L1 #29 "customer problem became a product problem"; L3 #29 "the idea is way better"; L4 #29 "great improvement… more on the bod part".
**Enforced:** QC.

### B20 — Real facts only: offer, price, guarantee, stats — added in this skill (beyond the Wildhorn audit)
**Rule:** Offer, price, guarantee and proof numbers come from `brand.json` only. Never invent a price, bonus, timeframe or statistic; if the template has a stat we don't have, keep the voice and drop the number. Say each fact once (guarantee not twice).
**Evidence:** L5 [02:36] #41–#49 "perfect" — their offer slots filled with our real offer, nothing invented; S55 spec "no invented numbers"; checkpoint c0232 guarantee written twice; PRODUCT.md bans "+60% T".
**Enforced:** lint (`prices_allowed`, brand `banned`) + QC.

### B21 — Censor the word for Meta: always S*X — added from Oct08 Loom
**Rule:** In any ad copy for Meta, the word "sex" is always written S*X (S*x in sentence case, s*x in lower case): headline, bubble, whiteboard, button, caption — every place it appears, and in the copy file. Never the plain word.
**Evidence:** Oct08 Loom — O04 (whiteboard UGC): "THE ONLY S*X ED LESSON ANY MAN NEEDS", "S*x + Wildhorn = mind blowing", "REGULAR S*X", "S*X ON WILDHORN". Redone as a text-only edit of the validated try (presenter, whiteboard and handwriting kept).
**Enforced:** lint (word `sex`, case-insensitive, in `texts` and the composite spec → error "write S*X").

### B22 — Never the word "drive" — added from Loom O1
**Rule:** Never write "drive" in the ad copy — not "drive", not "S*X drive", not "drive is back": the founder finds it too far from the angle. Say "libido" ("stamina" may sit next to it), or go to {CORE_PROBLEM} / fat. Minimal swap, rest of the ad untouched: "MORE DRIVE" → "MORE LIBIDO", "BOOST YOUR DRIVE & STAMINA" → "BOOST YOUR LIBIDO & STAMINA"; a pure-libido template headline goes to testosterone ("The drive is back" → "The testosterone is back", his words).
**Evidence:** Wildhorn Loom O1 (08/10) — O15 "not my angle… the testosterone is back", O23 "I don't like the drive word, too far from my angle: beer belly, fat or libido", O30 "we want beer belly or libido". 9 more to-review ads had it (O56 O60 O68 O70 O77 O82 O85 O86 O90) → text-only fix.
**Enforced:** lint (word `drive` in any quoted copy of `texts` / composite → error; spec `b22_exempt` only for ads validated before the rule) + QC.

---

## C. Visual

### B23 — Offer-slot parity: a percentage stays a percentage, a price stays a price — added from Edenvia Loom 1 (2026-10-11)
**Rule:** The offer slot keeps the template's *mechanic*, filled with our real numbers (B20). "FLAT 20% OFF" → "-50%" (our $39 vs $79.99 = 51 % off, rounded down to a number we can defend), never "NOW $39.00". A price slot gets our price, a "was/now" pair gets both our prices, a "% off" gets our percentage, a "buy 2 get 1" gets our real bundle or the slot is dropped. Same for proof slots: a star count stays a star count, a customer count stays a count. The brief's `reason` must say which mechanic is kept.
**Evidence:** Edenvia Loom 1 (E-L1 #2) on S2 c0138: "il y a le pourcentage de réduction sur la template et il y a juste le prix. Il faut mettre -50. On ne va pas mettre le prix dans le numéro 2." General remark in the same Loom: "trop de variations et pas assez d'analyse concrète du mécanisme derrière" (→ A13 inventory, E11 mechanism kept 1:1).
**Enforced:** lint (brief2spec: a `template_text` with `%` whose `ours` has no `%` fails; a `template_text` with `$` whose `ours` has no `$` fails).

### C1 — The image shows the avatar's problem or result
**Rule:** Keep the format; rewrite the scene until {CORE_PROBLEM} (or the result) is visible.
**Evidence:** L2 #6 "Beef vs Spaghetti" didn't show the belly → L3 #6 great; L3 #23 "show better that it's a beer belly"; L4 #23 "you didn't put the man boob, so less understandable".
**Enforced:** QC.

### C2 — The ingredient visual is recognizable, fresh and appetizing
**Rule:** Make the invisible visible: never a generic capsule — {INGREDIENT} visible inside transparent capsules or labelled. Ingredient pieces are recognizable silhouettes (Wildhorn: heart, lobed liver, bean kidney, oval testicle), fresh and appetizing like a premium butcher counter, clean, no visible veins/arteries, no blood, never brown/dried/raw-looking, never anything that reads as "the animal was killed" or as excrement. If the template shows its ingredient, copy that rendering exactly. "Organs, organs, organs."
**Evidence:** L4 #35 disgusting, #37 "we killed the bison… looks like bison shit", #40 generic capsule; L5 #39 not recognizable; L7 #70 capsule panel "exactly what I imagined"; L8 #71 "looks like meat", #76 "organs, organs, organs"; L9 #70 "nobody wants the veins"; SL2 S17 brown organs looked like dung → fresh; SL3 S17 great. (Rule history: freeze-dried matte → superseded by fresh/appetizing at SL2.)
**Enforced:** lint (brand `visual_checks`) + QC.

### C3 — Keep what made the template a winner AND make it clear
**Rule:** Never trade the winning principle for clarity or the reverse (billboard MADE OF real ingredient + labels).
**Evidence:** L6 #35 B6 clear but lost the principle; L7 #35 "you really understood the game".
**Enforced:** QC.

### C4 — Follow the example's visual code, including on the result
**Rule:** Glows, colour accents and highlights of the template apply to every panel, the result included; the result panel is the most rewarding image of the ad.
**Evidence:** L3 #16 "more color on the result"; L4 #16 "the little orange light on the result, you forgot it"; L5 #16 great.
**Enforced:** QC.

### C5 — Keep the template's render style, use our avatar, remove every leftover prop
**Rule:** Pixar stays Pixar, sketch stays sketch, painting stays painting; their person becomes our avatar; every prop of their customer/product is swapped (a cowboy still holding THEIR bottle, sequin skirts on our man = fail).
**Evidence:** L2 #10 lost the Mars Men illustrated style; QC B2 #4 photoreal instead of Pixar; L8 [01:01] "you didn't respect the template style"; Sam QC R3 S71/S47 leaked props.
**Enforced:** prompt (name the style, F2) + QC.

### C6 — The product is an exact replica at real proportions and never hides the hero
**Rule:** Real proportions, never squashed or stretched; label untouched (even when the product "gets fat", A6). When the template's hero is an object, the hero stays fully visible and the product goes where the template's product slot is.
**Evidence:** L2 #16 bottle crushed; QC B3 #22 jar in front of the split belly; L6 #58 "try not to touch the product design".
**Enforced:** prompt LOCK + composite (keeps aspect) + QC.

### C7 — No product in the template → none; logo slot → the official logo file, pasted by script (D19)
**Rule:** Add no product where the template has none (write "NO product" explicitly). A brand-logo slot gets the official logo file pasted by script (D19) — never a product photo, never a logo drawn by the model.
**Evidence:** L3 #22 "I would not have put a product"; L3 #23 logo replaced by a product photo; QC B4 #33 #35 jar added; QC B5 #35 small wordmark misspelled.
**Enforced:** prompt + D8 lint + QC.

### C8 — "Another version" = another idea
**Rule:** When asked for another version, change the idea, not the wording.
**Evidence:** L5 #47 "make me a version completely different".
**Enforced:** process.

### C9 — Text placement matches the template
**Rule:** Same spacing between headline and secondary text, text centred on the template's anchor (the eggplant's axis), same position, size and block size as the template. Check at full resolution.
**Evidence:** L8 #73 not centred on the eggplant; L9 #73 "small text too close to the big text — failed again"; L1 #6 keep every block at the template's size.
**Enforced:** composite `cx`/`y` + QC.

### C10 — Product rendering quality = the template's
**Rule:** Real 3D object on the surface with contact shadow and matching light; the template's text texture.
**Evidence:** L9 #65 "the 3D of the product on the table and the texture of the text" were better in the example; L7 #58 "the design they made for the product is better".
**Enforced:** prompt LOCK ("real 3D object with contact shadow") + composite shadow + QC.

### C11 — Hands hold objects naturally
**Rule:** Fingers wrapped around the phone/{PRODUCT_NOUN}, object fully visible and upright — check at full resolution.
**Evidence:** SL2 S33 phone badly held.
**Enforced:** QC.

### C12 — Before/after difference obvious at first glance — added from Loom audit
**Rule:** Concrete cues (belt holes, shirt tucked, belly profile) so the change reads in one second. A barely different pair = fail.
**Evidence:** QC B2 #13 barely different → fix → L2 #13 "much better adapted". Protocol 4 QC line.
**Enforced:** prompt + QC.

### C13 — Never redraw an illustration that worked: same side, same framing, complete body — added from Loom audit
**Rule:** When a version's drawing was right, the redo keeps its side, framing and anatomy; only the named element changes (see A20).
**Evidence:** L3 #2 B3 "why did you change the side… the body without the arm is really bad, the first one was way better" → B5 same side, arm hanging naturally.
**Enforced:** spec `tpl_abs` + QC.

### C14 — Nothing ambiguous: no killed animal, no excrement, no powder pile, no blood — added from Loom audit
**Rule:** The ingredient and its source are shown so nothing can be misread as death, dung or dirt. The source animal is always alive and proud.
**Evidence:** L4 #37 "it kind of looks like we killed the bison… what the bison shit"; L4 #35 "a bit disgusting"; SL2 S17 brown organs "like dung"; protocol 0 "powder pile looks like poop".
**Enforced:** QC (+ C2 lint wording).

### C15 — Format test: the format itself reveals what the product is made of in one second — added from Loom audit
**Rule:** Pick the FORMAT that makes the source obvious in one second (butcher-chart animal with its tagged ingredients, slab of tagged organs) — a texture alone is not enough.
**Evidence:** L5 #35 capsule wall "think of a format where people will instantly understand it's bison organs"; L7 #35 "we do understand this is a supplement, a bit annoying".
**Enforced:** QC.

### C16 — The source must read as itself — added from Loom audit
**Rule:** The animal/plant/ingredient source is drawn with its identifying features and named against its look-alike in the prompt (Wildhorn: "a wild American bison — hump, dark shaggy fur, short curved horns — NOT a cow, no spots").
**Evidence:** L5 #38 "I would have shown better the bison, it's hard to understand it's a bison"; QC B4 #38 kept the template's cow under the jar.
**Enforced:** prompt (F8) + QC.

### C17 — Product size = the template's product size — added from Loom audit
**Rule:** The product is as large and readable as the template's product; composite `jar.h` matches the template's product height.
**Evidence:** L9 #57 B9 "the product size is a bit hard… it's so much smaller".
**Enforced:** composite `h` / prompt + QC.

### C18 — Before = maximum pain, after = maximum reward — added from Loom audit
**Rule:** The problem image is the most aggressive version (huge {CORE_PROBLEM}, arm visible, body pushing toward the result); the result image is the most colourful, rewarding one.
**Evidence:** SL2 S8 "you should have been more aggressive on the belly on the first image… put the arm… go to the right"; L3 #16 "put more color on the last image, on the result".
**Enforced:** QC.

### C19 — Show the avatar before the result; real grip on the product — added from Oct08 Loom
**Rule:** When the ad sells a transformation (drive, body, {CORE_PROBLEM}), the man shown is {AVATAR} as he is today — an ordinary man of the avatar's age with a normal dad body (soft, slight belly OK, no abs) — never already fit or ripped like the template's model. Any {PRODUCT_NOUN} held in the hands gets a real grip (C11): fingers wrapped round its sides, thumbs on the edges, label facing camera, its weight in his hands — never floating between the hands or pinched by the fingertips.
**Evidence:** Oct08 Loom — O02 ("SHE BEGGED ME NOT TO STOP" painted torso): our try 1 kept a lean, muscular body and the hands barely held the jar. Redo = 45–60 greying man with a dad body, both hands wrapped round the jar, same layout and painted text.
**Enforced:** prompt (inventory + CHANGES) + QC.


### C20 — Brand colours, never a palette coded for another audience — added from Loom O2
**Rule:** Every ad is recoloured to the brand palette (brand.json `colors`; Wildhorn ad kit: burnt orange #E0662C, cream #F2E6D0, near-black #0F0C0A, plus the jar's amber and black). Keep the layout, swap only the colours. A template coded for another audience (Wildhorn: pink bars, badges, stars, brackets, banners, CTA — female-coded) is ALWAYS recoloured, even when it is a winner; pink only if the ad itself targets women (spec `ad_for_women`).
**Evidence:** Wildhorn Loom O2 (09/10) — O88 "stop with the pink, pink is for girls"; [09:51] "try to put the colour of the brand, that's one thing you do bad"; O29 and O62 "change the colour"; O85 "less pink, more for the avatar".
**Enforced:** lint (brand.json `palette_banned`, Wildhorn: `pink`/`magenta` in the visual prompt, inventory, texts or composite → error; negated mentions and `SWAP pink X ->` pass; spec `c20_exempt` only for renders made before the rule) + QC.

### C21 — Settings and props belong to the avatar — added from Loom O2
**Rule:** The room, decor and props are {AVATAR}'s (Wildhorn: a 45-60 married man): never a girl's bedroom (pink bedding, cushions, vanity products), never feminine or "cute" seasonal decor. Swap them for a neutral masculine equivalent of the same function (plain navy/charcoal bedding, dark wood, garage, kitchen counter, beer bottles, leather) — same composition.
**Evidence:** Wildhorn Loom O2 (09/10) — O96 mirror selfie kept the template's pink girl's bedroom: "change the room, it's not a girl"; O64 "change the pumpkin behind" (decorative mini pumpkins → unlabeled beer bottles).
**Enforced:** pixel inventory (A13: every room/prop line is a KEEP or SWAP decision) + QC.

### C22 — Our product looks as real as theirs — added from Loom O2
**Rule:** Product realism = the template's (extends C10). When the generated {PRODUCT_NOUN} looks CG or flat next to the template's photographed product, paste the real cutout from the brand kit (Wildhorn: `/srv/blueprint/kit/files/wildhorn-jar-cutout.png`) by script: right size and perspective, colour grade and rim light matched to the scene, contact shadow and ground occlusion. QC it side by side with the template's product at full res before showing it.
**Evidence:** Wildhorn Loom O2 (09/10) — O84 (two jars on a log): "put the product more realistically — compared to theirs it's shit" (their three bottles were real photos; ours were clean renders).
**Enforced:** post step (cutout composite) + QC (side-by-side product check).
---

## D. Production

### C23 — The product comes from the brand's photo library, lit by the scene — added from Edenvia Loom 1 (2026-10-11)
**Rule:** Extends C22. A flat web packshot cutout dropped into a scene reads as a sticker. Every product placement starts from the brand's **product library** (`brand.json` → `product_library`, an INDEX.md describes each photo): choose the photo whose light, angle and hold match the template slot (standing on a surface → studio shot; held at chest → the hand/people shot cropped to the pouch and hand; "what's inside" → the tablets flat lay), cut it from THAT photo, and keep the props that sell the format (water droplets on the pouch, a glass of water, the tablets, ice). Match colour grade, add contact shadow. Never scale the pouch below the size of the template's product. When the template's product is held by a person, the hand comes from the library photo too, not from the generator.
**Evidence:** Edenvia Loom 1 (feedback-loop.md E-L1 #1): "les images produits ne sont pas bonnes" — all 10 of batch 01 used the same packshot cutout, small, unlit, no droplets; the founder's reference folder shows the pouch beaded with water, next to a glass and the tablets, held naturally.
**Enforced:** QC (side-by-side product check against the library photo) + lint warning when `composite` has a product and the spec names no `product_source`.

### D1 — Never water down an ad to pass a filter: switch engine and composite
**Rule:** When OpenAI refuses (sexual), switch engine and COMPOSITE the real product photo + exact text by script. Never sanitize the idea. (Run 1 used Flux 2 Pro via kie.ai; the current chain is D5/D7.)
**Evidence:** L7 #62 "you should have just copied the ad… go for another model that lets you, you have the API key"; L8 #62 "great".
**Enforced:** lint (`sexual` needs a fallback; scene engines need composite + sd_prompt).

### D2 — QC every image at full resolution before showing it
**Rule:** Against this file and 2-make/qc-checklist.md. Never a thumbnail.
**Evidence:** B1 review; L3 [00:26] "do a quality check on the ads"; L9 [00:00] "find what mistakes you did and double check on them".
**Enforced:** process.

### D3 — Review page shows only ads to review, with every version
**Rule:** Validated ads are hidden; each row shows the template, the first version and every later try (B1 → B2 → …), the current one highlighted.
**Evidence:** L2 [04:19] "give me the example of the first generation so I see the improvement"; L3 [06:26] "the batch 1, 2, 3, 4… all the batches"; L4/L6 "remove the validated ones".
**Enforced:** build_sam.py.

### D4 — Every review is logged here first
**Rule:** For each Loom: what worked and WHY (to repeat), what failed + root cause + new rule; rules added here first, then lint if mechanizable, then generate.
**Evidence:** L2 [04:40] "feedback loop on the good… and on what is bad"; L7 [04:09] "add this to the list of things to solve"; L8 [01:53] "you should have a notepad"; SL2 [07:10] "every one of the things I tell you must be an improvement"; SL3 [17:25] "feedback loop a lot".
**Enforced:** process (3-improve/feedback-loop.md).

### D5 — Engine chain by need
**Rule:** OpenAI gpt-image-2 first (accepts suggestive food objects: banana, glazed donut) → Nano Banana Pro via kie.ai when text must be PAINTED INTO the scene (sunscreen letters: perfect spelling) → Seedream via kie.ai for scenes with skin/lingerie (rendered with NO text and NO product) → `composite.py` for the real product + exact text.
**Evidence:** B9 (#65 #69 #79); SL3 S11 "maybe go out of GPT to do it".
**Enforced:** spec `engine`/`fallback` + srun.py.

### D6 — Fallback parity
**Rule:** When an ad falls back to another engine + composite, every inventory line must survive — every KEEP placement (product on her head AND bottom right) exists in the composite spec.
**Evidence:** SL2 S11 the fallback dropped the head jar silently.
**Enforced:** lint (composite product count vs placement).

### D7 — Seedream renders the scene only
**Rule:** Seedream never renders a full ad (it garbles labels and writes prompt words like "crossed" on the image). Scene only: no text, no product; product + text always composited. Engine `seedream_full` is banned.
**Evidence:** Sam QC R3 S55 S58 S74 S79.
**Enforced:** lint + srun.py.

### D8 — The model never draws a standalone brand mark
**Rule:** The image model never draws a brand mark outside the product label: it misspells small wordmarks ("WILLDHORN", "WIILDHORN") and turns an icon into a letter (horns on a "W"). The prompt leaves the logo spot EMPTY (`lock_extra`) and the official logo file is pasted by script afterwards (D19).
**Evidence:** QC B4 #35, B5 #35; Sam QC R3 S8 S18 S35 S43; SL3 S18 "logo failed on try 1 and try 3", S35 "logo again".
**Enforced:** lint (bare wordmark text line) + prompt.

### D9 — No emoji in composited text
**Rule:** Fonts render emoji as boxes. Keep emoji only when the image model draws them; use DejaVu for ✓ ✕ → glyphs.
**Evidence:** Sam QC R3 S58.
**Enforced:** lint.

### D10 — "OK" means a new file exists on disk
**Rule:** Check the template path before generating; count output files after; any other "OK" is a lie.
**Evidence:** SL3 S42 redo reported "OK" 3 times with no image (wrong template extension .png vs .jpg).
**Enforced:** srun.py.

### D11 — Every correction generalizes — added from Loom audit
**Rule:** A fix the reviewer dictates on one ad becomes a rule applied to every other ad it fits and to every future ad — and every redo or new ad is built against the FULL rulebook since round 1, not only the latest Loom.
**Evidence:** L2 #17 "it's because I told you what to do — could you do it again now on other ads"; L3 #25 "apply it everywhere"; L3 [06:45] "another version with all the data from this Loom and all the data from the beginning"; L4 #40 "implement all the next results about that"; SL2 S24 "I want everything I tell you to be an improvement"; SL3 S17 "why didn't you catch it on the first try".
**Enforced:** process + lint (all checks always on).

### D12 — Review cadence: each round = redo every rejected ad + the next 10 new templates — added from Loom audit
**Evidence:** L2 [04:19] "make me the ones that don't go, and generate the 20 to 30"; L3 [06:54] "make me a new batch of the ones I told you are bad, and let's do 30 to 40". The Sam batch ran 10 at a time.
**Enforced:** process.

### D13 — Template path sanity: each spec's template is the canonical template of that ad number — added from audit
**Rule:** Before generating, check `tpl == sorted(templates)[num-1]` (the S-number is the template's rank in the sorted templates folder) unless `tpl_abs` is set on purpose (a validated try used as Image 2).
**Evidence:** the 2026-10-02 audit of the Wildhorn Sam batch found six specs (S29 R3, S33 R3, S35 R3, S55 QC, S79 QC, S80 R4) pointing at another ad's template; "S29 try 3 changed the style" (SL3) was in fact generated from S31's template.
**Enforced:** lint (when `$SAC_BATCH/templates/` exists; opt out with `SAC_NO_D13=1`).

### D15 — Output format: width 1080, the template's format — added from Oct08 Loom
**Rule:** Every finished ad is 1080 px wide. Square template → 1080×1080. Story/TikTok template (9:16) → 1080×1920 and it stays a Story. 4:5 → 1080×1350. Any other ratio → the template's ratio at 1080 wide. A template within 3 % of a standard ratio snaps to it. Get the size by cropping/resizing the 2K master — never regenerate for size.
**Refinement (Edenvia batch 01, 2026-10-11):** gpt-image-2 renders only 1:1, 2:3 or 3:2, and it does NOT obey letterbox/pillarbox notes in the prompt (S1, S4, S8, S10: badge, headline or side text cut by the crop, twice). When the smart crop of the 2:3 master would cut content, finish the ad by EXTENDING the background instead (edge rows/columns replicated: `edenvia/batch/pad_fit.py`) — never a stretch, never a regeneration for size. srun.py keeps every uncropped master in `out/_raw/` for that purpose.
**Evidence:** Oct08 Loom (format note for all ads, now and future). Check run on the 10 Oct08 finals: all already at 1080×1080 / 1080×1350 / 1080×1920.
**Enforced:** `adformat.py` (target_size / fit / check) called by the runner after every generation and by the compositor before drawing (oct08 orun.py + ocomp.py; skill `scripts/srun.py` + `scripts/composite.py`).

### D16 — Review page: our ad big on top — added from Oct08 Loom
**SUPERSEDED by D20 (Loom O1, 08/10): side by side at the same size.** Old rule: On every review page, each row starts with OUR ad, big (latest try, labelled "Try N — to review", up to ~720 px wide, sharp, click → full size); earlier tries and the template come smaller underneath. The reviewer must be able to read every word without clicking. Image performance rules stay (first image eager + fetchpriority high, the rest lazy + async, webp q80 at 2× display, width/height set).
**Evidence:** Oct08 Loom — Adrien could not read the text on the 270 px thumbnails of /oct08.
**Enforced:** page builder (build_oct08.py) + process.

### D17 — Brand marks outside the label are replaced by script after generation — added from Oct08 batch 2, updated Loom O1
**Rule:** After every generation, every brand mark outside the {PRODUCT_NOUN} label (corner logo, badge, sign, receipt, sticker) is erased and replaced by script with the brand's official logo file from the brand kit (brand.json `logo_files`: a light version for dark backgrounds, a dark version for light ones) (D19). Never keep the mark the model drew. QC zooms on every mark at full res. Until 08/10 the horn-icon SVG was pasted instead — rejected in Loom O1 ("the W with the horns is not great… put my logo").
**Evidence:** Oct08 batch 2 (Wildhorn) — 13 of 89 ads had the mark drawn as W+horns (O33 O38 O39 O41 O43 O51 O59 O66 O69 O84 O91…); all fixed by pasting the kit SVG (0 credits).
**Enforced:** post step (oct08 `o2logo.py`, official logo file) + QC.

### D18 — 4:5 on kie gpt-image-2 = a 3:4 render cropped: keep text out of the crop zone, refit, never blind-crop — added from Oct08 batch 2 (lead decision)
**Rule:** kie's gpt-image-2 refuses 4:5 and returns 3:4, so a 4:5 ad loses about 6 % at the top and 6 % at the bottom. The prompt asks for a plain safe strip top and bottom (no text, band, button or product there). If the least-content crop still cuts a headline, a bottom band or a bubble, refit: re-crop the same render with a chosen window, or rebuild the band by script. Never ship a blind crop; QC checks both edges of every 4:5.
**Evidence:** Oct08 batch 2 — O13 (offer band), O16 (headline + price line), O96 (first caption bubble) were cut by the 3:4 → 4:5 crop; fixed by refit / script band (0 credits).
**Enforced:** runner prompt (oct08 `o2run.py` 4:5 FRAMING line) + `o2pad.py` refit + QC.

### D19 — The brand mark is the founder's REAL logo, pasted by script — added from Loom O1
**Rule:** Wherever the template shows a brand mark outside the product label, paste the brand's official logo file from the brand kit (brand.json `logo_files`: a light version for dark backgrounds, a dark version for light ones) by script: same position as their logo, about the width of their logo, never upscaled past the file's native size, tilted with the surface when the slot is tilted (receipt). White/light version on dark backgrounds, dark version on light ones. The model never draws it (no AI wordmark, no generic icon). Erase the old mark first (inpaint on texture, row-patch on smooth backgrounds, texture clone on hair/skin), then zoom at full res for leftovers.
**Evidence:** Wildhorn Loom O1 [02:52] "I don't know why you're not putting my logo… the W with the horns is not great" — 20 to-review ads re-done by script, 0 credits (O33 O36 O39 O41 O43 O51 O56 O59 O66 O69 O71 O77 O80 O81 O83 O84 O90 O91 O93 O95). First pass left ghosts (O33 O59 O71 O77 O80 O81): erase box measured, not guessed.
**Enforced:** post step (oct08 `o2logo.py`) + D8 lint + QC.

### D20 — Review page: template and our ad side by side, same size, number order — added from Loom O1
**Rule:** Each row = a big readable ad ID ("O15" — not a font where O looks like 0), then the TEMPLATE and OUR AD side by side at the SAME width (~420 px each on desktop so the row fits one screen; stacked full width on a phone), labelled "Template" | "Try N". Ads in strict number order, never grouped by angle. Nothing else in the row: no QC verdict, no table, no copy dump. A redo row adds the founder's Loom note and shows the new try next to the previous tries, same size, newest first. Tabs To review (N) / Validated (N). Image-perf rules stay (first image eager + fetchpriority high + preload, rest lazy + async, webp q80 at 2x, width/height set); no horizontal scroll at 375 px.
**Evidence:** Wildhorn Loom O1 [03:05] "can you put the image same size like the template, what is this mess… why the numbers are not great… why QC pass… a tableau in the middle"; [02:44] "I don't understand why it goes from 30 to 38" (angle grouping broke the number order).
**Enforced:** page builder (oct08 `build_oct08.py`) + browser check (`pagechk2.js`: order sorted, equal widths, 0 JS errors, no horizontal scroll).

### D21 — After a text edit, keep the base pixels; take only the changed text boxes — added from Loom O1 redo round (lead)
**Rule:** A Nano Banana text edit re-draws the whole image and garbles small text it was not asked to touch (the {PRODUCT_NOUN} label). After every text edit, merge: base try pixel-for-pixel + only the changed text boxes from the edit (boxes with ≥ 10 px plain margin around the line, or the old letters ghost through). QC the label at full res.
**Evidence:** Wildhorn 'drive' fixes 08/10 — the jar label was garbled on 6 of 12 edits (O15 O60 O68 O70 O82 O86); O90 ghosted with a tight box.
**Enforced:** post step (oct08 `o2merge.py`) + QC.

---

## E. What worked — repeat it

### E1 — Keep both lines and the social mechanism; swap only who transformed
**Evidence:** L8 #63 "Step 1 Lose the beer belly / Step 2 Let no one hit" — "amazing". Kept both lines word for word except the subject, kept the social mechanism (everyone wants you, your partner guards you).

### E2 — Exact copy when the template already speaks our angle; real product composited; symbol swap
**Evidence:** L8 #62 #78 #72 (hair → measuring tape); #62 exact copy through another engine when GPT refused.

### E3 — Capsule packed with small whole ingredient pieces = the reference ingredient visual
**Evidence:** L7 #70 B7 "exactly what I imagined"; L5 #40 "literally see the organs in the capsule".

### E4 — Full pixel inventory → swap only what belongs to their customer
**Evidence:** L9 #75 #72 #79 (B9): game-night props, tired dad, older man.

### E5 — Inventory + flipping their object for our angle = first-try validation
**Evidence:** SL1: 6/10 first try (S1 bananas → shrinking belts, S3 puzzle jar of organs, S5/S6 estrogen signs, S4 text-only by script, S10 same buyer → their words).

### E6 — Find an object with the same SHAPE as our problem
**Evidence:** SL2 S23 round moon ↔ round beer belly: the visual pun survives intact — "really great understanding". Look for shape/function equivalents first.

### E7 — Exact structure + one-word angle swap + our proof props
**Evidence:** SL2 S12 S16 S20 S21 S22 S27 S32 S36–S38: 26/34 validated first try in round 2. SL3 S41–S83: 31/43 first try. SL4 S62 watercolor copied as is, angle swapped.

### E8 — Life scenes from HIS life with the problem — added from Loom audit
**Evidence:** L2 #9 Wojak vs Chad "exceptional… tell me how you reached it": each line a concrete, brutally specific scene of his life with a beer belly (sucks in his gut for photos, wife stopped grabbing his waist, shirt on at the pool) vs the proud mirror scenes.

### E9 — Same words, same gag, two nouns changed — added from Loom audit
**Evidence:** L3 #21 "really great job — understand why": the template's sentence kept word for word, symptom → beer belly, cause → estrogen; the product hangs from the belt buckle like it hung from the chin hair. Golden rule 1 "change as little as possible".

### E10 — Minimal change, maximum fidelity: one word swapped for a rival he knows — added from Loom audit
**Evidence:** L3 #25 "really great implementation… apply it everywhere": everything identical, Minoxidil → T-boosters.

### E11 — The template's mechanism kept 1:1, filled with our literal content in recognizable form — added from Loom audit
**Evidence:** L6 #39 B6 "exactly what I was thinking… understand the difference maker": the pour kept, tagged heart/liver/kidney/testicle falling into the jar. L5 #36 capsules flanking the jar ("really smart"), L5 #37 source → jar with our own mechanism (A29).

### E12 — Deep in the avatar: routine, proof and shame are HIS — added from Loom audit
**Evidence:** L4 #8 B4 hide-the-chest routine ("amazing"); L6 #44 B6 old jeans ("even better than the example"); L6 #47 B6 bedroom lights on ("the greatest"); L4 #30 "she notices first".

### E13 — Fusion without breaking the format — added from Loom audit
**Evidence:** SL2 S28 arcade kept their whole UI and added one row "BELLY FAT" ("I like the way you adapted it"); SL3 S67 "really good understanding of the joke".

---

## F. Prompt craft — from the QC logs (protocols page), not from a Loom

### F1 — Say what NOT to draw when the template's subject differs from ours
**Evidence:** QC B2 #2 model copied the template's arm while the text says belly.
### F2 — Name the render style explicitly ("Pixar-style 3D, NOT photoreal"; "oil-painting look, NOT photoreal")
**Evidence:** QC B2 #4; SL3 S11.
### F3 — Describe our avatar's age and look, and write "do NOT copy the template's person"
**Evidence:** QC B2 #10; spec constant `OLD = "a man in his late 40s with short greying hair and light grey stubble"`.
### F4 — Demand an OBVIOUS before/after difference with concrete cues (→ C12)
**Evidence:** QC B2 #13.
### F5 — OpenAI blocks close-ups of a bare or soft male chest
**Rule:** Show that problem through clothes/objects (tight shirt, gaping buttons, shirt on a hanger) on OpenAI, or render the scene on Seedream and composite (S79 thermal chest). Never send the chest template itself to OpenAI.
**Evidence:** QC B2 #123/#262, B7 #62, batch-01 c0123/c0262 blocked even without the template; SL S79 seedream_comp validated.
### F6 — When the template's hero is an object, keep it fully visible; the product goes small in its slot (→ C6)
**Evidence:** QC B3 #22.
### F7 — Write "NO {PRODUCT_NOUN} / NO product" explicitly when the template has none (→ C7)
**Evidence:** QC B4 #33 #35.
### F8 — Name the object to swap AND what it must not be ("a bison, NOT a cow, no spots")
**Evidence:** QC B4 #38 kept the template's cow.
### F9 — Wrapping elements (tape, ribbon) stay off the label wordmark and illustration
**Evidence:** QC B4 #26.
### F10 — Spell the wordmark letter by letter in the prompt; small logo → icon only (→ D8)
**Evidence:** QC B4 #35 "WIILDHORN", B5 #35 "WILLDHORN".
### F11 — Every inventory SWAP covers every prop of their customer and product (→ C5)
**Evidence:** Sam QC R3 S71 (cowboy holding their bottle), S47 (Barbie sequin skirts on Ken).
### F12 — Corrections use CHANGE + PRESERVE ("Change only X. Preserve product, label text, headline, layout, lighting.")
**Evidence:** blueprint Step 3; old skill Section 8 principle 5. A20/A22 are the strong form.
### F13 — Fixed prompt order: LOCK → PIXEL INVENTORY → TEMPLATE DNA → SCENE LOGIC → PRODUCT PLACEMENT → CHANGES → TEXT (exactly, nothing else) → CONSTRAINTS
**Evidence:** srun.py; protocol 3. The LOCK always ends the constraints too ("CRITICAL: the product… exact replica of Image 1").

---

## R. System rules (blueprint site, process level)

- **R1** Any template is accepted, whatever its niche or product; never skip one because it doesn't look like our angles.
- **R2** Sort first: templates grouped into concept families, then run family by family.
- **R3** Spread the research's winning angles inside each concept family; every ad maps to one top angle (no "other" group).
- **R4** Volume = number of templates (79 in = 79 ads out). Extra headline variations only on request. (Supersedes the earlier "every template × all angles × 2 headlines".)
- **R5** Research once: after step 1 the brand kit is locked; no new research per batch.
- **R6** Side by side: the comparison page always shows each ad next to its template, desktop and mobile.
- **R7** English: site, prompts, briefs.
- **R8** Only the research angles: rewrite a template until it fits one; never create a 6th group.
- **R9** Headlines come from the research (top-5 or headline bank, adapted only for our facts). In clone mode A6/A19 take precedence: when the template's own words already carry our angle, keep them.
- **R10** (replaced by R12) one-second context line — dropped: it broke B1.
- **R11** Decode protocol before writing: why it works → best-fitting angle → humor/emotion between image and text.
- **R12** Same amount of text as the template (= B1).
- **R13** Speak the customer's problem, not the product (= B2, B3, B4).
- **R14** Keep the winner's mechanism: same angle → their words; cheeky stays cheeky; known reference → one he knows (= A6, A4, B17).
- **R15** Loom transcription = the OpenAI Whisper API through `scripts/transcribe.py` (whisper-1, timecoded `MM:SS  text` lines into `feedback/loom-<id>.txt`), called by `scripts/ingest_loom.sh`. Same output and same next step as the old `mr-transcribe`. Never local whisper on the VPS (it saturated the server for 3 days in Sept 2026). Added 2026-10-11 on nutraflow1 (Edenvia), where `mr-transcribe` and `yt-dlp` were missing; tooling = `pip install --user yt-dlp openai` (VPS-SETUP.md §5).

---

## Resolved conflicts (read before applying an old spec)

| Collision | Resolution |
|---|---|
| C2 said "FREEZE-DRIED look (matte, dry)" (QC B7) and later "fresh, appetizing, never freeze-dried/brown" (SL2 S17) | Fresh/appetizing wins (latest review). Old specs using "freeze-dried" now fail lint — that is intended. |
| R9 "headline = research headline bank" vs A6/A19 "keep the template's words" | Clone mode: template words when they already carry our angle (A6/A19); otherwise the research bank (R9). |
| A14 "core problem is the default, fuse" vs SL3 S79 / SL1 S10 | A31: a template already on one of our angles (man boobs, drive) stays on it. A14 applies to angles outside our research. |
| B12 "keep a first name on review formats" vs the old lint pattern that blocked any signed quote | Spec flag `template_has_signature=True` lets a signed quote through; without it the signature is blocked (compliance: no fake testimonials added). |
| D1 "Flux 2 Pro" vs D5/D7 "Seedream scene + composite" | Flux was the run-1 fallback; current chain = OpenAI → seedream_comp (+ Nano Banana Pro for painted text). Flux remains available in kie_gen.py. |
| SL3/SL4 S11 "not realistic, painting or cartoon style" vs A25 text "S11 was a real photo with the product pasted on" (the validated v5 edited the template itself, prompt: "the same slightly faded film-photo realism") | Whatever the words, A25 wins: edit the template itself minimally so its exact look is kept, swap only the product. Don't re-render the style from a description. |
| A24/B2 "name {CORE_PROBLEM} everywhere" vs a template term our avatar uses (Oct08 O08 "Dad Bod") | A34: keep the avatar's own term from the template (A19 wins for that term); the rest of the copy stays on {CORE_PROBLEM}. |

---

## Index — which rules to apply at which step

| Pipeline step | Rules |
|---|---|
| Template intake | R1 R2 R4 · D10 D13 (file name/extension = ad number) |
| Decode (why / DNA / scene / sexual / trick / method) | A1 A2 A3 A4 A7 A21 A25 A27 A29 · E6 |
| Angle choice | A5 A6 A14 A19 A31 A33 A35 · R3 R8 R9 |
| Pixel inventory | A13 A8 A9 A12 A16 A17 A23 A30 · C5 C7 C17 C19 · F11 |
| Copy (texts) | B1–B22 · A24 A27 A28 A34 · R12–R14 |
| Visual (CHANGES block) | C1–C23 · A10 A11 A15 A32 · F1–F9 |
| Engine choice + fallback | D1 D5 D6 D7 · A25 · F5 |
| Prompt assembly | F10 F12 F13 · D8 (lock_extra) · C6 C10 (LOCK) |
| Composite | D6 D9 D15 D17 D19 D21 · C6 C9 C10 C17 C22 C23 · B20 B23 (offer slots) |
| QC | D2 + every rule above (2-make/qc-checklist.md) |
| Review page | D3 D20 (D16 superseded) |
| After the Loom | A20 A22 A26 · C8 C13 · D4 D11 D12 |

## Lint coverage (what `scripts/lint.py` blocks today)
| Rule | Check |
|---|---|
| A1 A2 A3 | `why`, `dna`, `scene` present |
| A35 | brand.json `angle_warn` (Wildhorn: `sleep`) in the quoted copy → warning (non-blocking) |
| A8 | `placement` present |
| A13 | `inventory` list with ≥ 5 lines |
| B2 | generic `men over N"`; brand `angle_keyword` (vague word without the full problem, on the default angle) |
| B4 B7 | `conversion`, `autoship`, `subscription` (generic) + brand `banned` (e.g. aromatase) |
| B6 | digits + days / "day N" / "by week" in texts unless `template_has_deadline` |
| B8 + compliance + competitors | brand `banned`, `competitors` |
| B12 | signed quote pattern unless `template_has_signature` |
| B20 | every `$` amount in texts/composite ∈ brand `prices_allowed` |
| B21 | the word `sex` (case-insensitive) in texts/composite → "write S*X" |
| B22 | the word `drive` in any quoted copy (texts/composite) → "say libido" (skipped for specs with `b22_exempt`) |
| A34 | spec `template_term` found in the texts → the B2 core-problem check is skipped for that ad |
| C2 (+C14 wording) | brand `visual_checks` (generic capsule, raw/bloody, veins, non-recognizable, freeze-dried/brown) |
| D1 | `sexual` on OpenAI needs a `fallback`; scene engines need `composite` + `sd_prompt` (error for primary/sexual, warning otherwise) |
| D6 | product count in `composite` ≥ placements named in `placement` |
| D7 | `seedream_full` banned |
| D8 | a text line that is only the bare wordmark |
| D9 | emoji in `composite` |
| C20 | brand.json `palette_banned` (Wildhorn: `pink`, `magenta`) in visual / inventory / texts / composite → error, unless negated, inside `SWAP … ->`, or spec `ad_for_women` / `c20_exempt` |
| D13 | `tpl` = sorted(templates)[num-1] unless `tpl_abs` |
Not linted (QC only): A4–A7, A9–A12, A14–A33 except the above, B1 B3 B5 B9–B11 B13–B19, C1 C3–C19 C21 C22, D2–D5, D10 (checked by srun.py at run time), D11 D12, D15 (enforced by adformat.py at run time), D16, D17 D19 D21 (post-step scripts + QC), D20 (page builder), E, F, R.
Candidates for the next lint checks: A24 on every line (not only the default-angle plain word), B1 text count vs a `text_slot_count` field, C17 product `h`
vs a measured template product height, F7 "NO product" present when `placement` says the template has none.

### D14 — One validated mapping file decides the final version of every ad
**Rule:** The final version of every ad comes from ONE validated mapping file (ad → exact file + Loom quote), never from "latest file" or a per-round meta file. Every review round must be in it; an ad with no validation evidence is removed, not kept. Exports and campaign packs are built only from that file, replaced in place, never re-sorted.
**Evidence:** Campaign packs audit 04/10: round 9 was skipped (no meta.json), so 9 ads showed rejected B8 versions (57, 61 banana, 65, 79 older man…), 2 never-validated ads (69, 73) were live, and S-08 showed an unreviewed try.
**Enforced:** stats.py reads the validated mapping; campaign builder uses a frozen layout and stops if an ad is missing.
