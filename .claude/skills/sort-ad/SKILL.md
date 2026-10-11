---
name: sort-ad
description: >
  Sort any static ad (image file, Drive file, screenshot, or a description) into one of Adrien's 9
  concept families (F1 us-vs-them … F9 off-avatar), with a confidence level and the one visual cue
  that decided it. Also translates the external swipe-file codes (UVT, BA, PS, FB, ST, NH, OS, BC,
  MEME) into families. Can file the image into the swipe-file folder and update its INDEX.
  Use for: "trie cette ad", "dans quelle famille", "classe ces statics", "sort this ad",
  "which family is this", "range ça dans le swipe file", or a batch of images to classify.
---

# Sort an ad into a concept family

**Input:** one or more ads — a local image path, a Drive file id, a pasted screenshot, or a text
description of the ad (headline + what the picture shows). Optionally a code (UVT, BA, …).

**Output per ad:** `family`, `confidence` (sure / probable / uncertain), `cue` (the one thing that
decided it), `runner-up` (second family when confidence is not "sure"), `format` (one of the 28
template formats when recognisable). Then, if asked, the file is copied into
`<swipefile>/<family-folder>/` and appended to that folder's `INDEX.md` by `scripts/file_ad.py`.

Rules: never invent what you cannot see. If the image is unreadable, say so and ask for a clearer
one instead of guessing. One ad = one family. The family is decided by **the dominant visual
mechanic**, not by the headline's topic and not by the angle (angles are a separate axis).

---

## Step 1 — read the ad

Look at the image at full size. Note, in this order:
1. **Structure**: how many panels, is there a split, a row, a timeline, a table, a product card?
2. **Headline**: copy it word for word.
3. **Subject**: a person, a body, a product, an object, a meme character, a screenshot of a phone?
4. **Proof elements**: prices, badges, stars, quotes, signatures, stats, dates.
5. **Tone**: serious / clinical, humorous / meme, native / editorial, salesy.

## Step 2 — walk the decision tree (first match wins)

Ask the questions in this order. Stop at the first "yes".

| # | Question | Family |
|---|---|---|
| 1 | Is the main content an **offer**: price, strike-through, bundle chooser, "special deal", "last call", challenge-with-guarantee, "how many should you buy", "selling out"? | **F6 offer / bundle / price** |
| 2 | Is the ad built on **two sides opposed**: rival vs us, ✓/✗ list, comparison table, "I use X / I use Y", "guess who's on", same person twice as rival-vs-us, "gym alone vs gym with"? | **F1 us vs them** |
| 3 | Does it show **the same body / person / object at two or more moments** (day 0 → day 21, week 0/2/4, before/after, shrinking silhouettes, "bye-bye X")? | **F2 before-after / timeline** |
| 4 | Is the copy a **reframe** — "X is not the problem, Y is", "it's not fat, it's estrogen", "it's not a discipline problem", "scam?" exposé — and the visual serves that sentence (big text, crossed-out word, the symptom re-labelled)? | **F3 problem reframe** |
| 5 | Does the picture **show the mechanism**: anatomical cut, thermal / x-ray, ingredients laid out or inside the capsule, product-as-puzzle, "it's all in here", symptom checklist on a body? | **F4 mechanism / anatomy / ingredients** |
| 6 | Is it about **where it comes from**: the ranch, the animal, wild vs farmed as origin story, "what's inside", real food on a table, sourcing, "the full system of 4 organs"? | **F5 origin / ranch / real food** |
| 7 | Is it a **meme** (wojak, chad, Barbie/Ken, starter pack, "said no wife ever", muppet, cat), a joke, or **UGC** (TikTok captions, selfie day 0/day 90, unboxing, phone screenshot, a review in the customer's own voice)? | **F8 meme / humor / UGC** |
| 8 | Is it **one frontal claim + the product as hero**: "over 40?", "zero waste", "do not take this without warning your wife", hand holding the product with one stat, celebrity/athlete holding it, "men 40+ 50+ 60+"? | **F7 bold claim + hero product** |
| 9 | Is it clearly **another niche or another avatar** (wrong gender, wrong age, another product category, a layout that needs a full re-skin before it can be used)? | **F9 off-avatar, re-skin last** |

If nothing matches by question 8, it is F9 (re-skin last) or the image needs a second look.

### Tie-breakers

- **Offer beats everything.** A before/after with a price card is F6.
- **Comparison beats timeline.** "Rival vs us" with two bodies is F1; the *same* body over time is F2.
- **Reframe is a sentence, not a picture.** If the picture carries the idea (anatomy, thermal), it is F4; if the sentence carries it ("it's not X, it's Y"), it is F3.
- **Mechanism vs origin.** Inside the body or inside the capsule → F4. Where the ingredient was raised or grown → F5.
- **Meme vs bold claim.** If you can name the meme format, F8. If it is a plain product shot with one line, F7.
- **UGC vs signed review.** TikTok-style, phone UI, selfie → F8. A clean typeset quote with a name + initial on a product background → F7 (signed review is a hero-product format). Unsure → F8, confidence "uncertain".
- **A stat is a claim.** "91% reported less snoring", "+13.2% collagen", "86% experienced less bloating" with the product → F7 (hand-holding-product-with-one-stat format). A stat shown as before → after ("56% before / 92% after") → F2.
- **Negative hook is a tone, not a family.** "DON'T try this", "Why you'll regret buying", "We're sorry", "Zero stars", "WARNING", a list of vices crossed out: classify by the picture. Crossed-out words → F3; review quote or warning + product hero → F7; phone-style caption photo → F8; week 1/3/5 → F2. Say "negative hook" in the cue.
- **Native / advertorial teaser** ("Why men over 40 can't…", "Read the solution →", long copy + "tap to learn more", news-style card): no own family. Classify by what the copy does: a sentence that re-labels the symptom onto a cause ("your skin isn't the problem, your gut is") → F3; otherwise by what the picture does (usually F2 or F7). Confidence "probable" at best, say "native look".
- **Off-avatar wins over mechanic.** An ad goes to F9 when the *promise itself* belongs to another avatar or niche (acne / skincare, menopause, cellulite, dress size, female hair loss, women's intimate health, kids), whatever its mechanic. A woman as the model is not enough: a woman holding "SALE 30%" stays F6. Every F9 verdict carries **re-skin as F<n>** = the family the ad becomes once re-skinned (so F9 can be mined by mechanic later).
- **Price vs badge.** An explicit strike-through price ($36 → $27), a price card, or a "buy 2 get 1" bar directly under the headline → F6. A small "up to 40% off" roundel in a corner or a closing "47% off today" line is a footer: the ad keeps its own family (F7, F2…), name the footer in the cue.
- **Folder and file names are hints only.** "Bundle Offer Ad.jpg" with no price on the image → F7; "MOF - US VS Them.jpg" that is a cellulite problem/solution split → F9. The image wins; say so in the cue when they disagree.

## Step 3 — confidence

- **sure**: one question answered yes with no competing cue.
- **probable**: one clear match but a second family has a real cue (name it as runner-up).
- **uncertain**: two families compete equally, or the image is partly unreadable. Give the runner-up and the cue that would settle it.

## Step 4 — code aliases (external swipe file)

When the ad comes with one of these codes, use it as a prior, not as the verdict. Still run the tree; if the tree disagrees with the code, report both.

| code | meaning | default family |
|---|---|---|
| UVT | Us vs Them | F1 (sure) |
| BA | Before / After | F2 (sure) |
| PS | Problem / Solution | F3 (sure) |
| FB | Feature / Benefit | F4 (probable) |
| OS | Offer Stack | F6 (sure) |
| BC | Bold Claim | F7 (sure) |
| MEME | Meme | F8 (sure) |
| ST | Stat (a number as the hook: "91% of users…", "+13.2%") | F7 (sure); F2 if the stat is shown before → after |
| NH | Negative Hook ("DON'T try this", "We're sorry", "Zero stars", "WARNING", crossed-out list) | no family of its own; run the tree (seen: F7 ×4, F3 ×2, F2 ×1, F8 ×1) |

## Step 5 — report, then file

Report one line per ad, in English (chat stays in the founder's language):

```
<file> → F<n> <family name> — <confidence> — cue: <what decided it> — runner-up: F<m> (<why>) — format: <one of the 28, or "—"> — re-skin as F<k> (F9 only)
```

For a batch, add a one-line tally per family at the end.

To file the image into the swipe file (only when asked, or when the request is "range / sort into the zip"):

```
python3 .claude/skills/sort-ad/scripts/file_ad.py --swipefile <root folder> --family F<n> --confidence <sure|probable|uncertain> --cue "<cue>" <image path> [<image path> ...]
```

The script copies the file into the family folder (keeps the original filename, never overwrites),
appends a line to that folder's `INDEX.md` under `## Sorted by sort-ad`, and refuses an unknown
family. Family folder names are in `families.json`.

## Reference

- `families.json` — the 9 families: folder name, one-line definition, visual cues, Adrien's template ids.
- Full definitions, the 28 formats and the angle axis: `edenvia/batch/adrien-concept-catalogue.md`.
- The sorted swipe file (131 ads) shipped as `Adrien-swipefile-complete-131.zip`; its README shows the same mapping applied.

## Worked examples (from the 131)

- `c0325` WEEK 0 / WEEK 2 / WEEK 4, same torso three times → Q3 yes → **F2, sure**, cue: same body on a timeline.
- `c0178` "Wildhorn vs 12 Pills", jar on one side, pile of pills on the other → Q2 yes → **F1, sure**.
- `c0323` "HOW MANY SHOULD YOU ACTUALLY BUY", three bottle packs with prices → Q1 yes → **F6, sure**.
- `c0157` "IT'S NOT FAT. IT'S ESTROGEN." big text, plain background → Q4 yes → **F3, sure**, cue: reframe sentence carries the idea.
- `c0188` "THIS IS WHAT'S INSIDE EACH CAPSULE", organs around a capsule → Q5 (inside the capsule) → **F4, probable**, runner-up F5 (organs read as origin).
- `c0305` "WILD BISON. WILD HUSBAND ;)" couple photo, wink → Q7 humor → **F8, sure**.
- `c0271` "DO NOT TAKE THIS WITHOUT WARNING YOUR WIFE", jar centred on red box → Q8 → **F7, sure**.
- A skincare before/after on a 25-year-old woman → Q3 says F2, but Q9 applies (wrong avatar and niche) → **F9, probable**, runner-up F2, note "re-skin as F2 later".
- `29_ST_100` "91% of Users Reported Less Snoring", hand holding the strip, 4 callouts, "$0.67 per night" badge → price is a footer, not the content → Q8 → **F7, sure**, cue: one stat + product in hand.
- `32_ST_4640` "56% before / 92% after 8hours" → the stat is a before/after → **F2, probable**, runner-up F7.
- `12_NH_5376` four symptoms crossed out above a row of bottles → Q4 crossed-out words → **F3, probable**, cue: negative hook, strike-through = "bye-bye X"; runner-up F7.
- `13_NH_5397` "WARNING: taking this will get her addicted to you in bed", couple, pouch, 3 check badges → **F7, sure**, cue: same skeleton as Wildhorn c0271.
- `08_NH_1844` hand holding the box, phone-caption "DON'T try this… you've been warned" → **F8, sure**, cue: UGC caption photo.
