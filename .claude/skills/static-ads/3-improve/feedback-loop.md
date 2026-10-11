# The feedback loop — from a Loom to a permanent rule

The loop is why the Sam batch hit 71 % first-try validation after run 1's 0 %. Every review becomes rules; rules become
lint checks where possible; the next batch is generated against all of them. The rulebook only grows.

```
review page ──► reviewer records a Loom (ad by ad, says the S number)
     ▲                         │
     │                         ▼
 regenerate ◄── rules.md + lint.py ◄── verdict table (WIN → why → repeat · MISS → root cause → rule)
 (redo + 10 new)                        │
                                        ▼
                         validated.json · sell_override.json · protocols log · stats
```

---

## 1. Ingest the Loom

```bash
cd $SAC_WORKDIR
bash $SKILL/scripts/ingest_loom.sh "<loom url>" s5     # yt-dlp + scripts/transcribe.py (OpenAI Whisper API, R15)
```
- Transcription = `scripts/transcribe.py` (OpenAI whisper-1 API, ~$0.006/min; replaces `mr-transcribe`, R15). Transcript lines are `MM:SS  text`. Never local whisper on the VPS (it saturated the server for 3 days in Sept 2026).
- If the reviewer pastes the video file or a transcript, save it as `feedback/loom-<id>.txt` the same way.
- After transcription, the mp4 is heavy media: archive it (`mr-archive push`) or delete it once the transcript is verified; the `.txt` stays.
- Read the transcript **in full**, in the main context (never delegate the reading of a review: nuance is the whole point).
- Speech-to-text garbles ad numbers and brand words ("Pierre Bailey" = beer belly, "Manboub" = man boobs, "S66" said for S56,
  "67" said for 57). Resolve every number against the review page order and the ad content before writing a verdict.

## 2. Build the verdict table (one row per ad mentioned)

| Ad | Try | Verbatim gist | Verdict | Why (WIN) / Root cause (MISS) | Rule | Lint? |
|---|---|---|---|---|---|---|
| S23 | 1 | "really great understanding" | ✅ first try | found an object with the same SHAPE as the problem (moon ↔ belly) | E6 | — |
| S15 | 1 | "could be a shoelace brand" | ❌ | moved the scene to an indirect consequence; dropped the blunt benefit | A18 | no |

Verdict vocabulary (it feeds `validated.json` and the stats):
- `✅ Validated (first try)` — validated on the first review of the first try.
- `✅ Validated (redo 1)` / `✅ Validated (redo)` / `✅ Validated (both tries)` / `✅ Validated (try 1 = sell)` — validated at the 2nd review.
- `✅ Loom N (after fix)` / `✅ Loom N — try 1 validated, keep it` — validated at the 3rd review.
- `❌ <reason>` — to redo. `⏳ To review` — not reviewed yet.
- Ads he does not mention: ask, or keep `⏳`. Never assume a silent ad is validated. (S62 was never mentioned until Sam Loom 4.)
- If an ad needed more than 3 reviews, write the round count to `rounds.json` (`{"11": 4}`) so stats stay exact.

## 3. For every WIN: why → repeat
Write the mechanism that made it work, in one sentence a future batch can apply to another template. If it is new, add an
`E` rule to 3-improve/rules.md (E1–E13 exist). A win without a "why" is lost knowledge: the reviewer explicitly asks for it
("feedback loop what you did on the 6", "find what you did right and try to do it more").

## 4. For every MISS: root cause → permanent rule → lint check if mechanizable
1. **Root cause, not symptom.** "Brown organs" is the symptom; the root cause was over-correcting an earlier rule ("not gross") into dried shapes.
   "Jar not on her head" was a symptom; the root cause was a fallback that silently dropped a placement (→ D6 parity check).
2. **Rule.** Phrase it brand-agnostically with the Wildhorn case as evidence. Extend an existing rule if it is a refinement (C2 was rewritten when S17 contradicted it — the history line stays), otherwise a new ID continuing the series.
3. **Lint.** If a regex or a count can catch it, add it to `scripts/lint.py` (generic) or to `brand.json` `banned` / `visual_checks` (brand-specific). Examples that became lint: D6 jar count, D7 seedream_full, D8 bare wordmark line, D9 emoji, B6 invented deadline, A13 inventory ≥ 5, B20 prices.
4. **Prompt.** If it is a generation habit (logo misspelled), put the fix into the fixed prompt blocks (`lock_extra` in brand.json) so every ad carries it.
5. **Redo spec.** The redo spec quotes the Loom in its `why` field ("Loom 3: try 1 (capsules) was the right idea…") so the review page shows the reviewer you heard him.

### 4b. Writing the rule (template)
```
### C19 — <imperative title> — added from <Loom id> <date>
**Rule:** <what to do, brand-agnostic, with placeholders {CORE_PROBLEM} {PRODUCT} …>
**Evidence:** <ad> <try> "<his words>" (<Loom id> [mm:ss]) → <what fixed it> → "<his verdict>" (<next Loom>).
**Enforced:** lint | prompt | QC | process
```
- One rule = one behaviour. If the new lesson refines an existing rule, extend that rule's text and add a history line instead of a new ID (C2 freeze-dried → fresh).
- Next free IDs: after the highest ID in both rulebooks (`3-improve/rules.md` here and the wildhorn-static-ads skill's `/root/claude-vault/skills/wildhorn-static-ads/wildhorn/lessons-wildhorn.md`).
- Add the rule to the index table at the end of rules.md and, if linted, to the lint coverage table.

### 4c. Extending the linter (hypothetical examples — not rules)
Brand-specific → `brand.json` (no code): a new ban `"banned": {"\\bketo\\b": "avatar already failed keto — don't sell it"}`; a new visual check
`{"if": "\\bpowder\\b", "msg": "A30 we sell capsules, never powder"}`.
Generic → `scripts/lint.py`, inside `lint()`, with the rule ID first in the message (this F7 check is a candidate listed in rules.md, not yet in lint):
```python
        if s.get("template_has_no_product") and not re.search(r"\bNO (product|jar)\b", visual, re.I):
            errs.append(f"#{n}: F7 template has no product — write 'NO product' explicitly in visual")
```
Then: `python3 -m py_compile scripts/lint.py`, run lint on the current round's spec file AND on one older spec file to see what the new check would have caught
(older files are expected to fail newer rules — that is the point), and record the check in rules.md "Lint coverage".

## 5. Update the records
- `validated.json` — every verdict (latest verdict wins, A26). Keep a timestamped backup before rewriting (`validated.json.bak-HHMM`).
- `sell_override.json` — `{num: try_index}` whenever he picks a try that is not the latest (S9→1, S35→2, S42→1, S58→1, S79→1). Frozen forever (A20).
- Protocols log — append the round's two tables ("what worked and why" / "every miss, root cause, permanent fix") on top of the protocols page, newest first.
- Rules page — rebuild (`build_lessons.py`).
- Stats — `stats.py` after every round; report first-try %, after-one-fix %, hit rate, generations per validated ad.

## 6. Regenerate (D11–D12)
- Redo every ❌ ad changing only what he named (A20/A22), passing a validated try as `tpl_abs` when he liked its layout.
- Apply every dictated fix to every other ad where it fits (D11), against the full rulebook (D11).
- Add the next 10 new ads (D12). Lint → generate → full-res QC → review page. Then wait for the next Loom.

## 7. Report to the reviewer
A short table per round: `ad → verdict → what changed`, the new rules (IDs), the stats line, the review link. No victory lap.

---

## Case studies — every round, in order

### Run 1 (Wildhorn, 79 templates, 9 batches): 0 % first try, 30.3 % of generations validated, 2.5 rounds/ad, 3.3 generations/final ad

**L1 — batch 01 written feedback (Adrien, no transcript).** Misses: features instead of benefits (#3), added bottom line (#4), too much text (#5), text squeezed the bar (#6),
"men over 40" instead of the problem (#7), unclear routine (#8), vague loser lines (#9), "conversion" (#11), changed text although same angle (#14),
their headline structure better (#16 verb + body part + deadline), aggressive line kept word for word wins (#17 "Drains beer belly in 14 days"), "X? Try us" not adapted (#18),
"your 12 supplements" nobody gets it (#25), customer problem turned into a product problem (#29), sexual concept made non-sexual (#57), great template badly adapted (#63),
too many "supplements failed you" overall. → B1 B2 B3 B4 B6 B10 A6 B18 B19 B17 A4 A1 A33.

**L2 — batch 02.** Wins: #9 Wojak vs Chad "exceptional" (E8); #13 much better (C12); #14 #18 #19 #20 well adapted (A6, B5, C1). Misses: #10 lost the Mars Men illustrated style (C5);
#11 joke less logical for the belly (A27); #16 jar crushed (C6). Process: show the first generation next to the new one (D3), feedback loop on good and bad (D4), generate the next 10 (D12).

**L3 — batch 03.** Wins: #6 changed the scene to show the problem, kept the format (C1); #21 same words, same gag, two nouns (E9); #22 concede the pleasure (B11) — "I would not have put a product" (C7);
#24 enemy = mechanism (A28); #25 one word swapped, "apply it everywhere" (E10, D11); #27 #28 #29 better. Misses: #2 changed the side, ugly armless body, logo wrong (C13, A20, D8);
#8 man-boobs angle not hit (B18); #23 not readable as a beer belly, text off, competitor logo replaced by a product photo (C1, C7, A20); #26 hair on a non-hair product (A2).
Process: show all versions B1→B4 (D3); next version with all the data since the beginning (D11).

**L4 — batch 04.** Wins: #8 "amazing — deep into the avatar" (B18, E12); #23 text "on point" (A28); #26 perfect (A2 applied); #29 #30 #31 #32 #34 great (B19, B3, B11, A2).
Misses: #2 drew an arm while we sell belly/man boobs (A2 body part); #16 forgot the little orange light on the result (C4, C18); #23 should have replaced the competitor's "Lab" slot (C7);
#35 #36 #37 #39 imported their product world — jerky look, brisket, milk pour, chocolate (A2, C2); #37 "we killed the bison… looks like bison shit" (C2, C14, A29); #38 vague rival + vague problem (B5); #40 generic capsule (C2).

**L5 — batch 05.** Wins: #2 #16 #23 fixed (A2, C4, C7); #36 capsules flanking the jar "really smart" (E11); #37 source → jar with our own mechanism (A29, E11); #40 organs inside the capsule (E3);
#41 #42 #46 #49 perfect — their habit → ours, offer slots → our real offer (A2, B20). Misses: #35 format doesn't say "bison organs" in one second (C15); #38 bison hard to recognize (C16);
#39 organs not recognizable (C2); #43/#44 "one notch tighter" not meaningful (B9); #47 asked for a radically different version (C8).

**L6 — batch 06.** Wins: #39 "exactly what I was thinking" — understand the difference maker (E11); #44 B6 "even better than the example" (B9); #47 "the most aggressive — the greatest" (B10);
#52 #53 #55 #56 great (B5); #57 hard ad adapted well. Misses: #35 clearer but lost the winning principle (C3); #51 mentioned Autoship (B7); #54 compression shirt (B8); #58 same angle → the bottle should get fat (A6, C6).

**L7 — batch 07.** Wins: #35 "really understood the game" (C3); #51 #64 #66 #67 great; #70 organs in the capsule "exactly what I imagined" (E3). Misses: #57 not sexual enough / not clearly weight loss (A4, B14);
#61 missed the vulva innuendo (A4, A7); #62 watered down to pass GPT — "go for another model" (D1, B10); #63 changed Step 2 (A6); #65 "shirt off since day 21" unreadable + invented timeline (B6);
#68 "belly" not "beer belly" (B2); #69 visual didn't match the sexual line (A4); #70 shower copied for no reason (A3). Process: add it to the list of things to solve (D4). → LESSONS.md + blocking lint created here.

**L8 — batch 08.** Wins: #62 #63 #72 #78 great/amazing (E1, E2). Misses: #57 product not in her hand + text added (A8, B13); #61/#69 kept their innuendo object (A7); #65 invented deadline, flat font, jar off the lounger (B6, A10, A8);
#70/#71/#76 organs look like meat; foot not on the scale (C2, A20); #73 text not centred on the eggplant (C9); #74 not on the beer-belly angle (A24); #75 kept the kids' beds (A12);
#77 two different bodies (A9); #79 young man, jar not in front of the face, no name on a review format (A11, A8, B12). Process: "you should have a notepad" (D4).

**L9 — batch 09 (last of run 1).** Wins: #57 #61 #71 #76 #79 validated; #72 B9 amazing (E4). Misses: #65 less good than the example — 3D product and text texture (C10); #69 still doesn't make sense (A7);
#70 organs a bit disgusting, no veins (C2); #73 small text too close to the headline, failed again (C9); #77 navel not on the cut (A9); #57 product a bit small (C17).
Key instruction: "#75 — you could have done this from the first try… every pixel of the scene" → **A13 pixel inventory**, mandatory and linted.

### Sam batch (83 new templates, 10 at a time, rulebook + lint from the start): 71 % first try, 87 % after one fix, 100 % final, 62 % of generations validated, 1.4 rounds/ad, 1.6 generations/validated ad

**SL1 — round 1 (S1–S10): 6/10 first try.** Wins: S1 bananas → shrinking belts (flip their object); S3 puzzle jar with organs + one job per organ; S4 text-only by script (zero text errors);
S5/S6 hidden-hormone checklist mapped onto our mechanism; S10 same buyer → their words (E5, A6). Misses: S2 GLP-1 faces missed the belly (A14); S7 button popping tamer than worms (A15);
S8 silhouettes faced away (A16; SL2: before image more aggressive, C18); S9 "You can't farm this" unclear to a stranger (B14). Question: S10 "why sexual and not beer belly?" → A6 then, A14/A31 now.

**SL2 — round 2 (S2–S40): 26/34 new ads first try.** Wins: S12 S16 S20 S21 S22 S27 S32 S36–S38 (E7); S23 moon (E6); S7 S9 now validated (A15, B14); S28 arcade fusion (E13); S32 "so aggressive" (B10).
Misses: S11 jar not on her head — fallback dropped a placement (D6, A21); S14 flipped a line that already worked (A19); S15 shoelaces (A18); S17 brown organs (C2 rewritten);
S18 capsules next to the beer instead of the pour (A17); S24 "felt the difference" too soft (B16); S29 words too complicated (B15); S33 bed copied + phone badly held (A3, C11); S35 "Outperform your 30s" (A14, A24).

**SL3 — round 3 (redos + S41–S83): 31/43 new ads first try; QC fixed 13 before he saw them** (logo misspelled ×4 → D8; template leftovers ×2 → C5/F11; Seedream full ads ×4 → D7; emoji box → D9).
Wins: S15 S17 S24 S33 fixed by the round-2 rules (A18, C2, B16, A3+C11); S21 S44–S49 S51 S53 S54 S59–S61 S63 S71–S73 first pass. Misses: S11 the woman's FACE is the product (A21);
S18 S58 S79 regenerated tries he had validated (A20); S18 powder makes no sense for capsules (A30); S29 style changed when only wording was wrong (A22 — root cause found later: the spec pointed at S31's template, D13); S74 two lean bellies (A23); S50 sexual fruit (A23);
S42 S52 S56 S80 off-angle or vague (A24); S57 missed the woman angle (A24); S55 she initiates → she should be on top (A32); S79 man boobs, not belly (A31); S42 redo "OK" with no image (D10).

**SL4 — round 4 (the 12 left).** Wins: S14 S18 S29 S50 S52 S56 S57 S74 S80 — the round-3 rules fixed them first time (A19 A30 A22 A23 A24); S62 watercolor copied as is (E7); S42 try 1 validated (A26).
Miss: S11 for the 3rd time — kept regenerating a scene; "review the ad by screenshot and understand the model they use" → **A25** (edit the template minimally, masked product swap, text by script, keep 9:16).

**SL5 — S11 only (no transcript).** "Great job on the last one" — A25 worked. 83/83 validated.

---

### Edenvia Loom 1 (E-L1, 2026-10-11, written feedback in chat, family 1 = S1–S10): 10/10 generated first pass, 6 fixed at QC before showing, founder: product wrong on all, copy OK

| # | Loom | Ad | Founder said | W/M/P | Rule |
|---|---|---|---|---|---|
| E1 | E-L1 | all | "les images produits ne sont pas bonnes" + reference folder of 27 real product photos | M | **C23** (new), C22 |
| E2 | E-L1 | S2 | template shows a % off, we put a price: "il faut mettre -50" | M | **B23** (new), E11 |
| E3 | E-L1 | all | "trop de variations et pas assez d'analyse concrète du mécanisme derrière" | P | A13, E11, B23 |
| E4 | E-L1 | all | copywriting "ça va, c'est pas dégueu" | W | B-series as is |
| E5 | E-L1 | all | "sinon c'est bien" — layouts validated | W | frozen (A26) |

System observations NOT raised by the founder, logged for the next review, not rules (the founder's verdict wins, A26): S6 lost the two-sided opposition of the arm-wrestling template (one man, one beer); S4 and S10 show a heavier and a slimmer woman, which reads as weight loss instead of fluid; S2 draws the calf filling as fat lumps. Ask at Loom 2 whether the "fluid, not fat" line must be visible in every A8 body.

Redo list for round 2 (D11): all 10 get the product re-placed from the library (C23) — pixels otherwise kept (D21); S2 offer button → "-50%" (B23). Nothing else moves.

**Round 2 done on the VPS (2026-10-11):** library fetched (26 photos), three cutouts (standing / held with hand / tablets), product re-placed by script on S1 S3 S5 S6 S7 S8 S9, S2 button → -50%, S10 by a masked edit in the template's ink style (a photo hand on a drawing read as a sticker), S4 untouched. Two masked gpt-image-2 edits in total (≈ $0.60). QC log: `edenvia/batch/qc-log-r2.md`. Question for Loom 2: on illustrated templates, photo cutout or drawn-from-the-photo?

## Loom coverage matrix

Every distinct piece of feedback in every transcript (`feedback/loom-b2…b9.txt`, `loom-s1…s4.txt`) plus the two reviews without a transcript
(L1 = batch-01 written feedback on /protocols; SL5 = Sam Loom 5 verdict on /protocols) → the rule that encodes it.
Type: **W** win (repeat) · **M** miss (rule) · **P** process instruction · **V** plain verdict (validation only, no lesson).
Rules marked † were **added from the Loom audit** (they existed only as page notes or not at all in LESSONS.md).

| # | Loom | ts | Ad | Feedback (paraphrase) | T | Rule |
|---|---|---|---|---|---|---|
| 1 | L1 | — | #3 | benefits were product features | M | B3 |
| 2 | L1 | — | #4 | added bottom line repeats the ad | M | B1 |
| 3 | L1 | — | #5 | too much text under it; one strong closing line | M | B1 |
| 4 | L1 | — | #6 | extra text squeezed the bottom bar | M | B1, C9 |
| 5 | L1 | — | #7 | say who it's for by problem, not "men over 40" | M | B2 |
| 6 | L1 | — | #8 | routine problem not clear, extra line | M | B18† |
| 7 | L1 | — | #9 | loser lines not precise | M | B10, E8† |
| 8 | L1 | — | #11 | mentioned "conversion" | M | B4 |
| 9 | L1 | — | #14 | changed the text although same angle | M | A6 |
| 10 | L1 | — | #16 | their headline (verb + body part + deadline) was better | M | A6 |
| 11 | L1 | — | #17 | keep "Drains beer belly in 14 days" word for word — aggressive wins | M | A6, B10 |
| 12 | L1 | — | #18 | "X? Try us." not adapted | M | A6 |
| 13 | L1 | — | #25 | "your 12 supplements" — nobody gets it; swap the known reference | M | B17† |
| 14 | L1 | — | #29 | customer problem became a product problem | M | B19† |
| 15 | L1 | — | #57 | sexual concept, adaptation wasn't | M | A4 |
| 16 | L1 | — | #63 | great template, badly adapted — decode first | M | A1 |
| 17 | L1 | — | all | too many "supplements failed you"; favor aggressive angles | M | A33† |
| 18 | L2 | 00:00 | #9 | exceptional — tell me how you reached it | W | E8† |
| 19 | L2 | 00:48 | #10 | adapt to the same style; Mars Men style was better | M | C5 |
| 20 | L2 | 01:28 | #11 | not bad, but "size matters" is less logical for the belly; make a fitting version | M | A27† |
| 21 | L2 | 01:28 | #11 | you could have kept the two sentences | M | A6, B1 |
| 22 | L2 | 02:20 | #13 | much better adapted | W | C12† |
| 23 | L2 | 02:40 | #14 | well adapted | W | A6 |
| 24 | L2 | 02:40 | #15 | not bad | V | — (verdict) |
| 25 | L2 | 03:03 | #16 | bottle a little crushed; find why you missed it | M | C6 |
| 26 | L2 | 03:15 | #17 | was it because I told you, or can you do it on other ads? | P | D11† |
| 27 | L2 | 03:28 | #18 | perfect | W | A6, E2 |
| 28 | L2 | 03:49 | #19 | excellent, well adapted (rhythm kept, rival swapped) | W | B5, B17† |
| 29 | L2 | 04:19 | #20 | good | W | C1 |
| 30 | L2 | 04:19 | all | redo the ones that don't work, generate 20–30, show the first generation for comparison | P | D3, D12† |
| 31 | L2 | 04:40 | all | feedback loop on what improved and on what's bad | P | D4 |
| 32 | L3 | 00:13 | #2 | why change the side? body without the arm is ugly; first was better | M | C13†, A20 |
| 33 | L3 | 00:20 | #2 | logo wrong on the second one | M | D8, F10 |
| 34 | L3 | 00:26 | all | quality-check that everything fits the angle | P | D2, A24 |
| 35 | L3 | 00:43 | #6 | great work — feedback loop what you did | W | C1 |
| 36 | L3 | 01:17 | #8 | didn't hit the man-boobs angle | M | B18† |
| 37 | L3 | 01:38 | #10 | good | W | C5 |
| 38 | L3 | 01:47 | #11 | like it more | W | A27† |
| 39 | L3 | 01:57 | #16 | good; more color on the result image | M | C4, C18† |
| 40 | L3 | 02:29 | #21 | really great — understand why | W | E9† |
| 41 | L3 | 03:16 | #22 | amazing | W | B11 |
| 42 | L3 | 03:28 | #22 | I would not have put a product (template has none) | M | C7, F7 |
| 43 | L3 | 03:52 | #23 | show better that it's a beer belly | M | C1 |
| 44 | L3 | 04:09 | #23 | text does not correspond; first batch was better | M | A2, A20 |
| 45 | L3 | 04:29 | #23 | their logo slot replaced by a product image | M | C7 |
| 46 | L3 | 04:48 | #24 | great | W | A28† |
| 47 | L3 | 04:53 | #25 | great implementation — apply it everywhere | W | E10†, D11† |
| 48 | L3 | 05:19 | #26 | great, but added hair on a non-hair product | M | A2 |
| 49 | L3 | 05:42 | #27 | way better (no added text) | W | B1 |
| 50 | L3 | 05:59 | #28 | better (same angle, their words) | W | A6 |
| 51 | L3 | 06:06 | #29 | better idea; see if you can upgrade | W | B19† |
| 52 | L3 | 06:26 | all | when you remake, show batch 1, 2, 3, 4 — all versions | P | D3 |
| 53 | L3 | 06:45 | #30 | new version with all data from this Loom and from the beginning | P | D11† |
| 54 | L3 | 06:54 | all | keep adding every improvement; redo the bad ones; do 30–40 | P | D4, D12† |
| 55 | L4 | 00:00 | #2 | made an arm while we sell man boobs/belly — why not follow the angle | M | A2, F1 |
| 56 | L4 | 00:23 | #8 | amazing, deep into the avatar and the angle | W | B18†, E12† |
| 57 | L4 | 00:51 | #16 | follow the example: little orange light on the result, forgotten | M | C4 |
| 58 | L4 | 01:26 | #23 | perfect, chest understood; no man boob shown → less understandable | M | C1 |
| 59 | L4 | 01:34 | #23 | replace the competitor's "Lab" brand slot with ours | M | C7, A2 |
| 60 | L4 | 01:45 | #23 | text "you release estrogen" on point — feedback it | W | A28† |
| 61 | L4 | 02:01 | #26 | perfect, understood; identify the hair next time | W | A2 |
| 62 | L4 | 02:26 | #29 | better, great improvement — feedback how you got there | W | B19† |
| 63 | L4 | 02:50 | #30 | great, really understood the ad | W | B3, E12† |
| 64 | L4 | 03:20 | #31 | great | W | B11 |
| 65 | L4 | 03:29 | #32 #34 | great, angle adapted to the product | W | A2, E11† |
| 66 | L4 | 04:18 | #35 | not as pretty as the ingredient one; a bit disgusting | M | C2, C14† |
| 67 | L4 | 04:52 | #36 | great, but the brisket in the background isn't our product | M | A2 |
| 68 | L4 | 05:06 | #37 | adapted perfectly, but "we killed the bison… looks like bison shit"; not colostrum; show it's organs | M | C2, C14†, A29† |
| 69 | L4 | 06:30 | #38 | be precise: clear rival (fat burner / T-booster) + clear problem | M | B5 |
| 70 | L4 | 07:37 | #39 | chocolate brand → don't put chocolate in our product; B1 more logical | M | A2, A20 |
| 71 | L4 | 07:55 | #39 | I would make organs falling into the bottle | M | E11† |
| 72 | L4 | 08:41 | #40 | nobody cares about a capsule; show the organs inside it; think visually ahead | M | C2 |
| 73 | L5 | 00:00 | #2 | last one great | W | A2 |
| 74 | L5 | 00:17 | #16 | great | W | C4 |
| 75 | L5 | 00:30 | #23 | perfect, great improvement | W | C7 |
| 76 | L5 | 00:59 | #35 | find a format where people instantly understand it's bison organs | M | C15† |
| 77 | L5 | 01:11 | #36 | perfect, really smart | W | E11† |
| 78 | L5 | 01:29 | #37 | showed what the product is; mechanism different, same idea | W | A29†, E11† |
| 79 | L5 | 01:39 | #38 | perfect, but show the bison better | M | C16† |
| 80 | L5 | 01:54 | #39 | wrong: heart, liver, organs falling into the bottle and capsule | M | C2, E11† |
| 81 | L5 | 02:19 | #40 | great — literally see the organs in the capsule | W | E3 |
| 82 | L5 | 02:36 | #41 #42 | perfect | W | A2, B20† |
| 83 | L5 | 03:06 | #43 | "one notch tighter" not understandable | M | B9 |
| 84 | L5 | 03:36 | #44 | makes sense, don't like the example | M | B9 |
| 85 | L5 | 03:45 | #46 #49 | great | V | — (verdict) |
| 86 | L5 | 04:05 | #47 | great but weird; make a completely different version | M | C8 |
| 87 | L6 | 00:00 | #35 | more understandable but lost the winning principle; keep both; real organs | M | C3 |
| 88 | L6 | 00:45 | #39 | love it, what I was thinking — understand the difference maker | W | E11† |
| 89 | L6 | 01:15 | #44 | B6 even better than the example; my customer isn't that smart | W | B9, B14, E12† |
| 90 | L6 | 01:45 | #47 | B6 more aggressive, the greatest | W | B10, E12† |
| 91 | L6 | 02:15 | #51 | never mention Autoship; "50% off for life" was great | M | B7 |
| 92 | L6 | 02:45 | #52 | great | V | — (verdict) |
| 93 | L6 | 03:15 | #53 | smart comparison | W | B5 |
| 94 | L6 | 03:25 | #54 | the avatar doesn't use compression shirts | M | B8 |
| 95 | L6 | 04:09 | #55 #56 | great, understood the mechanism | W | A6 |
| 96 | L6 | 04:42 | #57 | hard ad, adapted well; try it for the beer belly | W | A14 |
| 97 | L6 | 05:11 | #58 | same angle → make the bottle fat; don't touch the product design | M | A6, C6 |
| 98 | L6 | 05:55 | #59 #60 | great | V | — (verdict) |
| 99 | L7 | 00:00 | #35 | really understood the game | W | C3 |
| 100 | L7 | 00:09 | #35 | reads as a supplement (a bit annoying) | M | C15† |
| 101 | L7 | 00:37 | #51 | great | W | B7 |
| 102 | L7 | 00:55 | #57 | B1 not sexual enough | M | A4 |
| 103 | L7 | 01:05 | #57 | B7 not easily understood that it's for weight loss | M | B14 |
| 104 | L7 | 01:23 | #58 | great, but their product design is better | M | C10 |
| 105 | L7 | 01:45 | #61 | didn't understand the ad: the pineapple is a vulva | M | A4, A7 |
| 106 | L7 | 02:41 | #62 | should have copied the ad; GPT refused → use another model | M | D1 |
| 107 | L7 | 03:08 | #62 | not aggressive enough | M | B10 |
| 108 | L7 | 03:34 | #63 | failed the angle: lose the beer belly + let no one hit was perfect | M | A6 |
| 109 | L7 | 04:02 | #63 | re-read the template, find why; add it to the list to solve | P | A1, D4 |
| 110 | L7 | 04:43 | #64 | first was bad, B7 great | W | E7 |
| 111 | L7 | 05:15 | #65 | missing the angle; be more aggressive | M | B10 |
| 112 | L7 | 05:40 | #65 | "shut up since day 21" — for what? one sentence must say what it's about | M | B6, B14 |
| 113 | L7 | 05:59 | #65 | no deadline in the template → don't invent one | M | B6 |
| 114 | L7 | 06:12 | #66 #67 | great | V | — (verdict) |
| 115 | L7 | 06:58 | #68 | beer belly, not belly | M | B2 |
| 116 | L7 | 07:37 | #69 | sexual visual but we don't understand; the visual must fit the line | M | A4 |
| 117 | L7 | 08:35 | #70 | shower copied for no reason (template = hair loss in the drain) | M | A3 |
| 118 | L7 | 09:13 | #70 | organs in the capsule — exactly what I imagined | W | E3 |
| 119 | L8 | 00:02 | #57 | woman's hand great, but product not properly in her hand | M | A8, C11 |
| 120 | L8 | 00:12 | #57 | you added text at the bottom | M | B13 |
| 121 | L8 | 00:27 | #61 | pineapple kept: it was for a vaginal probiotic — adapt it | M | A7 |
| 122 | L8 | 00:51 | #61/62 | love how you're speaking to her | W | E2 |
| 123 | L8 | 01:01 | #61 | didn't respect the template style | M | C5 |
| 124 | L8 | 01:13 | #62 #63 | great / amazing — feedback the 63 | W | E1, E2 |
| 125 | L8 | 01:53 | all | you should have a notepad (rulebook) | P | D4 |
| 126 | L8 | 01:59 | #65 | no deadline in the example → none | M | B6 |
| 127 | L8 | 02:14 | #65 | the line ("before you drain him") was great | W | A6 |
| 128 | L8 | 02:17 | #65 | product on the sofa/lounger like the example | M | A8 |
| 129 | L8 | 02:24 | #65 | wrote on the body flat; it was bubbles (sunscreen) | M | A10, D5 |
| 130 | L8 | 02:57 | #60s | great, keep the upgrade | V | — (verdict) |
| 131 | L8 | 03:17 | #69 | more sexual; pineapple → sperm taste; fit the product and the end goal | M | A7, A4 |
| 132 | L8 | 03:59 | #70 | good; organs of the first image better; foot on the scale like the first image | M | C2, A20 |
| 133 | L8 | 04:56 | #71 | more visible organs, looks like meat | M | C2 |
| 134 | L8 | 05:34 | #72 | great | W | E2 |
| 135 | L8 | 05:49 | #73 | text not centred on the eggplants; double-check placement | M | C9 |
| 136 | L8 | 06:24 | #74 | make it the beer-belly angle | M | A24 |
| 137 | L8 | 07:07 | #75 | put beer-belly elements, not the kids' bed | M | A12 |
| 138 | L8 | 07:38 | #76 | organs, organs, organs | M | C2 |
| 139 | L8 | 07:55 | #77 | same body half fat half lean; not the same guy | M | A9 |
| 140 | L8 | 08:34 | #78 | perfect | W | E2 |
| 141 | L8 | 08:52 | #79 | older guy (avatar) | M | A11 |
| 142 | L8 | 09:04 | #79 | product in front of the face | M | A8 |
| 143 | L8 | 09:18 | #79 | customer review → put a name | M | B12 |
| 144 | L9 | 00:00 | all | for every improvement find the mistakes and double-check them | P | D2, D4 |
| 145 | L9 | 00:12 | #57 | great; product size a bit small | M | C17† |
| 146 | L9 | 00:24 | #61 | great | W | A7 |
| 147 | L9 | 00:43 | #65 | idea great but example better: 3D product on the table, text texture | M | C10 |
| 148 | L9 | 01:17 | #69 | better but still doesn't make sense | M | A7 |
| 149 | L9 | 01:23 | #70 | organs less disgusting, no veins | M | C2 |
| 150 | L9 | 01:53 | #71 | validated | V | — (verdict) |
| 151 | L9 | 02:00 | #73 | small text too close to the big text — failed again | M | C9 |
| 152 | L9 | 02:06 | #74 | keep B8 | P | A20, A26 |
| 153 | L9 | 02:20 | #72 | B9 amazing | W | E4 |
| 154 | L9 | 02:27 | #75 | you could have done this from the first try: every pixel, then what to change | M | A13 |
| 155 | L9 | 02:54 | #76 | great | V | — (verdict) |
| 156 | L9 | 02:54 | #77 | better, but the navel must be perfectly aligned | M | A9 |
| 157 | L9 | 03:15 | #79 | perfect, the older guy | W | A11 |
| 158 | L9 | 03:31 | all | first try next time; deep analysis of why everything is there | P | A13, A1 |
| 159 | SL1 | 00:00 | S2 | not on the beer-belly angle | M | A14 |
| 160 | SL1 | 00:18 | S3–S6 | great | W | E5 |
| 161 | SL1 | 00:38 | S7 | more shocking, like their worms | M | A15 |
| 162 | SL1 | 00:53 | S8 | great; face the result, left to right | M | A16 |
| 163 | SL1 | 01:13 | S9 | not understandable on first read | M | B14 |
| 164 | SL1 | 01:20 | S10 | great — why sexual and not beer belly? | P | A14, A31† |
| 165 | SL2 | 00:00 | S7 | count the first as a success; more shocking anyway | P | A26, A15 |
| 166 | SL2 | 00:23 | S8 | more aggressive on the belly; go to the right | M | A16, C18† |
| 167 | SL2 | 00:50 | S9 | try 1 and try 2 both great — validate | W | A26, B14 |
| 168 | SL2 | 01:32 | S11 | girl with the jar on her head like the example — easy, explain why you failed | M | D6, A21 |
| 169 | SL2 | 02:14 | S12 S13 | great | W | E7 |
| 170 | SL2 | 02:51 | S14 | should have copied: "lost my waistline" is our angle | M | A19 |
| 171 | SL2 | 03:25 | S15 | shoelaces — could be a shoelace brand | M | A18 |
| 172 | SL2 | 04:04 | S16 | perfect | W | E7 |
| 173 | SL2 | 04:27 | S17 | their organs are cleaner, you want to eat them; why brown? | M | C2, C14† |
| 174 | SL2 | 05:03 | S18 | pour beer inside; lack of understanding of the whole concept | M | A17 |
| 175 | SL2 | 05:28 | S19–S22 | great | W | E7 |
| 176 | SL2 | 06:17 | S23 | really great understanding — find what you did right | W | E6 |
| 177 | SL2 | 06:34 | S24 | more aggressive benefit claim on the 93 % | M | B16 |
| 178 | SL2 | 07:10 | all | every one of the things I tell you must become an improvement | P | D4 |
| 179 | SL2 | 07:15 | S25–S27 | great | W | E7 |
| 180 | SL2 | 07:45 | S28 | I like the way you adapted it | W | E13†, A14 |
| 181 | SL2 | 08:20 | S29 | simpler words: "flat belly again" | M | B15 |
| 182 | SL2 | 08:54 | S30 S31 | great | V | — (verdict) |
| 183 | SL2 | 09:24 | S32 | so aggressive, I like it | W | B10 |
| 184 | SL2 | 09:32 | S33 | phone badly held | M | C11 |
| 185 | SL2 | 09:49 | S33 | calories idea great | W | E7 |
| 186 | SL2 | 09:53 | S33 | bed is there because it's a sleep product — why copy it? | M | A3 |
| 187 | SL2 | 10:27 | S34 | great | V | — (verdict) |
| 188 | SL2 | 10:36 | S35 | "outperform your 30s" — speak about the beer belly | M | A14, A24 |
| 189 | SL2 | 11:06 | S36–S38 | great | W | E7 |
| 190 | SL2 | 11:36 | all | lots of improvement, some things really wrong — improve | P | D4 |
| 191 | SL3 | 00:05 | S11 | double-check all ads, go deeper | P | D2 |
| 192 | SL3 | 00:13 | S11 | the girl's face IS the product; painting/cartoon style; maybe outside GPT | M | A21, D5, A25 |
| 193 | SL3 | 00:49 | S15 | great, adapted perfectly — feedback loop it | W | A18 |
| 194 | SL3 | 01:06 | S17 | great; why not on the first try? | W | C2, D11† |
| 195 | SL3 | 01:28 | S18 | no powder with capsules; pour beer into the glass | M | A30† |
| 196 | SL3 | 01:47 | S18 | try 1 was way better | M | A20 |
| 197 | SL3 | 01:54 | S18 | logo failed on try 1 and try 3 | M | D8 |
| 198 | SL3 | 02:46 | S24 | great — feedback it | W | B16 |
| 199 | SL3 | 03:00 | S29 | changed the style on try 3; keep try 2's style with the better wording | M | A22, D13† |
| 200 | SL3 | 03:43 | S33 | makes way more sense | W | A3, C11 |
| 201 | SL3 | 04:13 | S35 | logo misspelled again; like try 2 | M | D8, A26 |
| 202 | SL3 | 04:34 | S41 S21 | great | V | — (verdict) |
| 203 | SL3 | 05:04 | S42 | didn't respect the formula; say it's for losing the beer belly | M | A24 |
| 204 | SL3 | 05:35 | S42 | I like try 1 more | P | A26 |
| 205 | SL3 | 06:00 | S44–S49 | great; S47 style much better | W | E7 |
| 206 | SL3 | 07:26 | S50 | fat fruit vs skinny fruit, not sexual | M | A23 |
| 207 | SL3 | 07:56 | S51 S53 S54 | great | V | — (verdict) |
| 208 | SL3 | 08:12 | S52 | brain performance off-angle → fat guy vs lean guy; stay on the angle | M | A24 |
| 209 | SL3 | 09:16 | S55 | woman should be on top since she initiates | M | A32† |
| 210 | SL3 | 09:32 | S55 | text perfect; product should be better | M | C10 |
| 211 | SL3 | 09:53 | S56 | reads like a hangover product; show the belly | M | A24 |
| 212 | SL3 | 10:34 | S57 | woman angle: they initiate less with a beer belly; more sexual | M | A24, A4 |
| 213 | SL3 | 11:04 | S58 | try 1 best: copied the angle and how she held it | M | A20, A8 |
| 214 | SL3 | 11:25 | S59–S73 | great; S67 good understanding of the joke | W | E7, E13† |
| 215 | SL3 | 14:59 | S74 | two lean images — should be fat vs lean | M | A23 |
| 216 | SL3 | 15:22 | S75–S78 | great | V | — (verdict) |
| 217 | SL3 | 15:56 | S79 | highlight the man boobs, not the belly; try 1 perfect | M | A31†, A20 |
| 218 | SL3 | 16:25 | S80 | "after-40 changes" not understandable | M | A24, B15 |
| 219 | SL3 | 16:49 | S81–S83 | great | V | — (verdict) |
| 220 | SL3 | 17:25 | all | make all the improvements; feedback loop a lot | P | D4 |
| 221 | SL4 | 00:03 | S11 | still failed: review it by screenshot, understand the model they used | M | A25 |
| 222 | SL4 | 00:16 | S14 | great | W | A19 |
| 223 | SL4 | 00:21 | S18 | great (beer poured) | W | A17, A30† |
| 224 | SL4 | 00:40 | S29 | great | W | A22 |
| 225 | SL4 | 00:49 | S42 | first try was great, I validate — don't change it | P | A26 |
| 226 | SL4 | 00:58 | S50 S52 | great | W | A23, A24 |
| 227 | SL4 | 01:07 | S56 | background doesn't make sense, but it goes | M | A3 |
| 228 | SL4 | 01:25 | S57 | adapted the angle properly | W | A24 |
| 229 | SL4 | 01:32 | S62 | great | W | E7 |
| 230 | SL4 | 01:37 | S74 S80 | great | W | A23, A24 |
| 231 | SL5 | — | S11 | great job on the last one | W | A25 |

**Coverage: 231 feedback items (124 misses · 73 wins · 20 process instructions · 14 plain verdicts) · 0 without a rule.** The 14 plain verdicts (V) carry no lesson; they only update `validated.json`.
Rules with † were written from the Loom audit. 24 of them are shared with the Wildhorn skill (same IDs as `/root/claude-vault/skills/wildhorn-static-ads/wildhorn/lessons-wildhorn.md`): A27–A31 · B17–B19 · C12–C18 · D11–D13 · E8–E13. Three exist only in this skill: **A32** (staging acts out the line), **A33** (favor aggressive angles), **B20** (real facts only). F1–F13 consolidate the QC logs (not Loom feedback); R1–R14 restate the blueprint system rules.

When a new Loom arrives, append its rows here (same columns). A row with an empty Rule column is a failure of the loop.

## Transcription garble dictionary (Wildhorn Looms — check every Loom for the same kind)
| Transcript says | Meant |
|---|---|
| "Pierre Bailey", "be a belly", "b-reli", "bubbly" | beer belly |
| "Manboub", "man boob's angle" | man boobs |
| "Marsman" | Mars Men (template source) |
| "Ingrinos lab", "nose lab" | "The Angry Nose Lab" (competitor brand slot on #23) |
| "the ATS 2", "day 2" | ad #2 |
| "the 67" (while showing #57), "S66" (while showing S56), "S42" (while showing S72), "history one/two" (S31/S32), "story 6/7" (S36/S37) | the ad on screen — resolve by page order |
| "python core" | (unclear) — #57's object; resolved from the image on screen |
| "drain the sexual thing" | the "drain him" line of #65 |
| "Jean-Mathafas" | (noise) |
| "cell version" | sell version |
| "a notepad" | a rulebook (LESSONS.md) |
Rule: never act on a garbled word without checking the ad on screen at that timestamp; when unsure, ask once in the round report.
