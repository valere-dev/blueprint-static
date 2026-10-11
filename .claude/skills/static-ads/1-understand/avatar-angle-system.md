# Avatar & Angle System

How to find the customer and the angle, check them, and lock them before any ad is briefed.
This merges four sources into one pipeline:
- the **May doc system** (8 Google Docs, "MARK BUILDS BRANDS" method): Avatar Builder, Avatar Check,
  The Bridge, Angle Sniper, Angle Expansion Map, Necessary Beliefs, Offer Brief;
- **Evolve's Avatar OS** (desires → core avatar → sub-avatars → angles, "fuck demographics");
- **Crafter's** sub-desire by exclusion and the 7-question sub-avatar questionnaire;
- the **angle card** (Brand File schema) used by the clone machine.

Templates live on the VPS: `/root/claude-vault/knowledge/product-research/templates/`
(avatar-sheet, avatar-check, bridge, angle-sniper, angle-expansion-map, offer-brief) and the master
avatar prompt `prompts/deep-avatar-research-prompt.md`. Filled examples per product:
`product-research/products/<slug>/`.

---

## 1. The pipeline

```
VOICE OF CUSTOMER + 5–6 competitor ads
        │
        ▼
MASTER AVATAR (13 sections)  ──►  AVATAR CHECK (1 page, UNKNOWN allowed)
        │
        ▼
SUB-AVATARS by exclusion (3–10)  ──►  7-question card each
        │
        ▼
THE BRIDGE (pain → mechanism → identity, one sentence)
        │
        ▼
ANGLE EXPANSION MAP (awareness × desire grid, 25 cells) ──► pick 5
        │
        ▼
ANGLE SNIPER (5 locks) for each of the 5  ──►  ANGLE CARD (full fields)  ──►  briefs
        │
        ▼
NECESSARY BELIEFS (≤ 6 "I believe that…") — the spine of landing pages
```

Rules that apply to every document:
- Reading level of an 11-year-old (6th grade). One short sentence per box.
- `UNKNOWN` / `N/A` when there is no data. Never invent. Generic = start again; specific = ready.
- Verbatim beats paraphrase. "The customer must feel you read their diary."

---

## 2. Master avatar (the "Avatar Builder")

**Input:** 5–6 long competitor ads, customer videos or TikTok-shop scripts targeting the same core pain
(weight the ads ~80 % and web research ~20 %), plus scraped VOC (Reddit, Amazon 1★/5★, YouTube and
TikTok comments, Trustpilot).

**Instruction that matters:** do not summarize the ads. Reconstruct the CUSTOMER behind them. Mark what
is stated / strongly implied / inferred.

**13 output sections:**
1. Executive summary — who they are, what they feel, what drives the purchase.
2. Core avatar — daily life with the problem, how often they notice it, what triggers anxiety, how it
   touches confidence, identity, appearance, health fears.
3. Emotional landscape — primary and secondary emotions, secret fears, unspoken embarrassment,
   worst-case scenarios, what they fear others notice.
4. The problem beneath the problem — what it really means to them.
5. Desired transformation — become, feel, avoid, preserve, regain.
6. What they already tried — each item + why it disappointed.
7. Beliefs, myths, decision drivers — held, wanted-confirmed, blocking, accelerating.
8. Objections — in their own voice.
9. Buying triggers — moments, realizations, events that make them buy.
10. Messaging insights — strongest emotional, fear, hope, credibility, "why now", objection angles.
11. Exact customer voice — 20 phrases they say, 20 private fears, 20 desires.
12. Segments — sub-types and how their psychology differs.
13. Strategic takeaways — deepest truth, most powerful lever, biggest mistake marketers make, biggest
    gap to differentiate.

**Evolve's 5 avatar categories** (use them to read the material, strongest first):
1. **Desires** — "I want X / I need Y" (one surface desire per avatar, always know which core desire feeds it).
2. **Experiences** — situational ("turned 40", "had a baby") and product-based ("tried magnesium,
   didn't work" — always capture the OUTCOME).
3. **Emotions** — dig "why?" until you reach a primary emotion (joy, sadness, fear, disgust, anger,
   surprise).
4. **Behaviours / habits** — "researches everything before buying", "sucks his belly in at the mirror".
   They touch the ego ("I'm the kind of person who…") and predict other behaviours.
5. **Demographics** — last, usually implied by the others. Never a starting point.

Beliefs are not a sixth category: they are the output of the other four. Spot a belief ("I can't lose
weight") → dig into what created it → use it for hooks.

---

## 3. Avatar Check (60-second validation)

One page. Every box one specific sentence, or UNKNOWN.

| Box | Good (specific) | Bad (generic) |
|---|---|---|
| Name + 1 line | "Mike, 52, keeps his T-shirt on at the pool, tried keto twice and 3 fat burners" | "Men over 45 who want to lose weight" |
| Deep desire | Status + Sex: to be looked at again by his wife | "Health" |
| Top emotional pain (the feeling, not the symptom) | Shame when his kids poke his belly | "Belly fat" |
| Past failed attempt + why | Gym 4×/week for a year: chest stayed soft, so he concluded "it's my age" | "Diets" |
| Daily-life moment (where you'd film) | Sucking it in for the family photo | "Every day" |
| Identity he's buying | "The dad who still looks like he used to" | "A healthy man" |
| Product (1 line) | Freeze-dried wild bison organs, 2 capsules a day | — |
| Mechanism (plain) | "It's not fat, it's estrogen: his body converts T to estrogen after 40" | — |
| Why it works when others didn't | Diets fight calories; this targets the conversion | — |
| Timeline | Day 7 sleeps better / week 2 shirts fit / day 21 belt moves | "Fast results" |
| Bridge sentence | pain → identity in one line | — |
| Demand pull | Permanent (the belly comes back every summer) | — |

---

## 4. Sub-avatars by exclusion (Crafter × Evolve, house rule)

**House rule:** sub-avatar = WHEN (trigger) + WHY (cause) + WHAT THEY ALREADY TRIED (+ emotion now →
emotion wanted). Demographics only as a filter, and expressed on screen through the actor, not the copy.

The 4 exclusion levers (each added qualifier "opens a fresher conversation" and lowers sophistication):
1. **Who** — sex, age, ethnicity (filter only).
2. **What exactly** — "fat on the back of the arms", not "weight loss".
3. **When** — the trigger: turned 40, after a baby, after menopause, after GLP-1, after a scary number.
4. **Why** — the cause (hormonal, stress, habit) + the motivation (please a partner, keep up with kids).
Plus the strongest sharpener: **"…without [the failure of what I tried]"** (eye bags → eye bags without a
retinol that burns my skin).

Nesting ladder example: be more beautiful → better skin → no more eye bags (retinol) → caused by
menopause → without burning, because I already tried retinol and have sensitive skin.

**The 7 questions** (one card per sub-avatar):
1. Who are they (situation, not age)?
2. Their pain (in their words)?
3. Their desire (which angle, which core desire)?
4. Emotions they feel now?
5. Emotions they want to feel once it's solved?
6. Objections to our product?
7. What they currently use or are considering?

**Two gates:**
- Niche but shared: many people must have it (check volume: TAM estimate, thread volume). Drop
  problems unique to one person ("no microscopic audience pockets").
- A non-customer must NOT feel concerned by the hook. If they could, it's too broad.

How many: 1 core avatar (desire-based) until ~$100k/month, with depth in sub-avatars (3–10 per core).
"Out-avatar them, don't out-market them." 2–4 weeks per core avatar before pivoting, and only after 5+
sub-avatars are exhausted.

Examples of good sub-avatars seen in the market:
- Men on GLP-1 losing muscle and getting "Ozempic face" (Mars Men, Primal Viking, Ancestral all built a
  dedicated landing page).
- The wife who scrolls Facebook and diagnoses her tired, irritable husband (buys by proxy) — nearly
  untouched in the testosterone market (only Zapply targeted her openly).
- Men "considering TRT" (Mars Men: "Don't take T. Make T.").
- Men whose labs are "normal" but who don't feel normal (Primal Viking).
- Prediabetic men whose erections faded (Primal Storm's September pivot).
- Women in perimenopause / postpartum (Ancestral's shift: 13 of its 30 recent ads).

---

## 5. The Bridge (where the pain meets the product)

"The gold." Four sections, one sentence per box:

1. **Starting state** — pain in their words · deeper pain underneath · dominant emotion (one word) ·
   the belief keeping them stuck · what they tried + why it failed.
2. **The shift (mechanism, cause → effect, no features)** — real cause · what the solution missed ·
   what ours does differently · chain reaction (3–4 steps) · proof · how fast they'll notice (honest:
   day 3 / week 1 / week 4 / month 3).
3. **Destination** — new physical reality (observable) · new emotional state · new identity · new
   daily-life scene · new belief (old → new).
4. **Bridge sentence** — compress STARTING STATE → MECHANISM → DESTINATION into one line. Write 3, keep
   the best. It is the spine of every ad for that avatar.

Example (bison): "You've been fighting your belly with diets because nobody told you it's estrogen —
fix the conversion and you'll tuck your shirt in again."

---

## 6. Angle Expansion Map (25+ angles from one avatar)

A grid of awareness × desire, one hook per cell, 6th-grade reading level, N/A if the cell makes no sense.

| Awareness ↓ / Desire → | Health | Sex / attraction | Status / identity | Relationships | Wealth / time |
|---|---|---|---|---|---|
| Unaware | | | | | |
| Problem-aware | | | | | |
| Solution-aware | | | | | |
| Product-aware | | | | | |
| Most-aware | | | | | |

Then pick the **5 strongest** hooks → each becomes one Angle Sniper + one ad concept to test.

Filled micro-example (bison, problem-aware row):
- Health: "That gut isn't fat. It's a hormone problem."
- Sex: "She stopped reaching for you. It's not you, it's your estrogen."
- Status: "Shirt stays on at the pool? It's not your discipline."
- Relationships: "Your kids poke your belly. Here's what's really in there."
- Wealth/time: "$1,750 of supplements and the belly never moved."

**Desire elevation** (Evolve): move the product up the desire chain to reach less saturated markets,
but stay authentic. Dog harness example: Control ("master your dog's pulling instantly", real winner)
→ Health ("why are you still choking your dog?", real winner) → Status → Sex. The trap is the inverse:
dragging a status product down to comfort.

---

## 7. Angle Sniper (5 locks — one angle = one ad)

Lock all five BEFORE writing. If you want two options on a line, that's two Angle Snipers.
1. **The angle (the wedge)** — the entry point inside the desire, not the desire ("the 3 a.m. wake-up",
   "what your dentist won't tell you").
2. **Main desire** — one only.
3. **Extra desire** — the secondary emotional pull (main = health, extra = status).
4. **Awareness level** — one only (decides the hook style).
5. **Sub-avatar** — exactly who in the master avatar.

Then: **The target** (one sentence combining the five locks) · **What this angle is NOT** (who/what it
excludes, against scope creep) · **Hook check** (3 hooks written from the locks).

---

## 8. The angle card (full fields, feeds the clone machine)

The angle is the OUTCOME the customer wants, in his words. One card per angle, up to 10.

```
## Angle N: [outcome, ≤ 8 words]
- Mechanism (from the map):
- Primary desire (one of the 13):
- Sub-avatar (who · trigger · cause · tried · emotion now → wanted):
- Time-of-day anchor (3 a.m. / 10 a.m. / 6 p.m. / after meals…):
- Symptom words (≥ 5 customer phrases, 1st/3rd person):
- What he types at night (search query):
- Felt metaphor (the state as an image):
- Problem scenes (≥ 4 lost life scenes — objects, behaviour):
- Payoff scenes (≥ 4 regained scenes):
- Who notices (who · scene · what they say · what's at stake):
- Timeline from real reviews (first felt day · week 1 honest · d7 · d14 · d30 · d90):
- Angle-specific failed tries:
- Objection + answer:
- Sincerity line (a real limitation):
- Guarantee line ("<outcome> — or you're refunded"):
- Humour target (ritual or situation, never the body — or none):
- Visual bans → substitutes:
- Hook seeds (3–5: type — line):
- Dead hooks for this angle (already burned):
- Headline bank (verbatim, sourced):
- Destination (landing page / quiz URL):
```
Every empty field goes to the generator as `[MISSING]`; it must flag it, never fill it.

Why the time-of-day anchor and the witness matter: the clone machine picks the cheapest angle for a
source ad by matching **witness, clock and setting**. A source ad with a foreman noticing at work in the
afternoon transplants best onto "energy back by 10 a.m.", not onto "sleep through the night".

---

## 9. Necessary beliefs (Agora / E5 method)

"Be argument creators, not copy creators." Marketing = moving the prospect's existing beliefs to the
ones that make him buy, through a unique mechanism, before the offer appears.

Write ≤ 6 beliefs, each as "I believe that…". The universal ladder used by the blueprint skill:
1. The problem is solvable.
2. Classic solutions fail (and why).
3. This source/origin is legitimate.
4. The mechanism works.
5. This product is different from the others that use it.
6. Trying it is risk-free.

Each static installs ONE belief at ONE awareness level; a landing page installs all six in order.

---

## 10. Validating an angle (before it costs money, and after)

### Before testing (research evidence)
| Signal | Strong | Weak |
|---|---|---|
| Competitor weight | Several ads on it, ≥ 1 running 60–200+ days, duplicated, with its own landing page | One recent ad |
| Landing page built for it | A dedicated advertorial/listicle/PDP per angle ("one landing per villain") | Sent to the generic PDP |
| VOC volume | Repeated 10–50+ times, 100+ likes, high-upvote threads | A single comment |
| Product can honour it | Mechanism on the map reaches it | Needs a new causal link |
| Visible today | A discomfort felt now (3 p.m. crash, hair in the shower) | Prevention ("protect your future") |
| Specific outcome | "Jeans button again" | "Feel better" |

Rule from the Wildhorn angle lock: an angle that carried 10 of 15 internal top sellers and 100 % of the
competitor's active ads (with 2 dedicated landing pages) is "validated" — that was the evidence bar
for "beer belly = estrogen".

### After testing (the numbers)
- Judge on spend and CPA/ROAS, never on hook rate alone.
- Never kill before 72 h. An angle × persona fit needs 7–8+ creatives; a hypothesis dies only after
  20–30 creatives. A source that loses on 3 angles is dropped; an angle that loses on 3 sources is
  dropped.
- If a well-researched angle flops, suspect execution first (hook, format), not the angle. Sometimes
  the angle is just something people don't care about ("doctor designed" for a humidifier).
- Winner = ROAS above break-even and ≥ 10–15 % of monthly spend; for subscriptions, confirm with
  month-2 rebill.

---

## 11. Validated avatar for reference (bison organs, US men)

- American man 45–65 (core 45–54, extension 35–44), married, beer belly / man boobs / soft chest.
- Tried: gym 4×/week, keto, fasting, Amazon fat burners, ashwagandha, tongkat, shilajit, zinc, T-boosters,
  beef liver caps. Spent $1,000–2,000. Nothing moved.
- Daily shame: sucks the belly in at the mirror, never tucks his shirt, keeps the T-shirt on at the pool
  and in bed, wife and colleagues notice.
- Beliefs to break: "it's age" (the doctor said so), "it's my discipline", "organ supplements don't work
  (I tried)".
- Proof objects he wants: old jeans fit, belt buckle visible, tucking his shirt without thinking, seeing
  his feet, keeping up with grandkids, "feel like myself again".
- Hiding behaviours (validated in review): sucking it in, baggy shirts, shirt on at the pool, endless
  diets — NOT compression shirts.
- Identity: Americana, ranch/western, anti-medical-establishment, wild over industrial.
- Audience data (competitor reach): 98 % men; 35–44 > 45–54 > 25–34 > 55–64.
- Desire map of the testosterone market (testo-map, July): 1. shirt off without shame (most monetized) ·
  2. desired again by his wife (most emotional; proof = her sentence) · 3. energy and drive back (volume)
  · 4. keep his edge · 5. fix it without needles (anti-TRT) · 6. animal organs (source belief).

Use it as the reference standard for what "specific enough" looks like for any new brand.
