# QC checklist — full resolution, every image, before the reviewer sees it

Built from every failure seen in run 1 (79 ads, 9 Looms + QC logs) and the Sam batch (83 ads, 4 Looms + QC round 3, which caught 13 defects
before review). Open each image at **full resolution** (never a thumbnail — small text becomes unreadable at 768 px), next to its template.
QC is done in the main context, never by a subagent: a summary loses exactly the details this list checks.

Fail any line → fix (redo with CHANGE + PRESERVE, recomposite, or masked swap), re-QC, and log the defect in the QC log of the round.

## 0. Spec review (before generating)
- [ ] `why` names the scroll-stop trick; `dna` lists everything of their product world; `scene` says why the scene is there (A1 A2 A3).
- [ ] Inventory ≥ 5 lines covering setting, each prop, each person, light, camera, each text block, product spot (A13).
- [ ] Angle: the template's natural angle, from the research; core problem fused if the template's angle is outside our research; kept if it is one of ours (A5 A14 A31).
- [ ] Every text line names the core problem explicitly where the template names its problem (A24, B2).
- [ ] Text count = template count; nothing added — no tagline, CTA, disclaimer, context line, deadline (B1 B6 B13).
- [ ] Lines the template already has that work for our buyer are kept word for word (A6 A19).
- [ ] Stranger test on the headline: what it is + what it does (B14). Simplest words (B15).
- [ ] Numbers/prices/guarantee only from brand.json; no invented stat (B16 B20).
- [ ] No banned words (Autoship/subscription, jargon, competitor names, compliance bans) — lint confirms (B4 B7 B8).
- [ ] Sexual template: innuendo decoded and kept, tied to our angle; fallback with sd_prompt + composite (A4 D1).
- [ ] Fallback composite holds every KEEP placement (D6). Template file exists with the right extension (D10) and is the canonical template of that ad number (`tpl == sorted(templates)[num-1]` unless `tpl_abs` on purpose) (D13 — six Sam specs pointed at another ad's template).
- [ ] Twists/puns are literally true for our problem (A27). Known references swapped for ones he knows (B17). Routine lines = a routine he has because of the problem (B18); his body, his words (B19).
- [ ] Enemy = the research mechanism, product = its killer (A28). If their visual mechanism can't apply to our product, keep the idea with ours (A29).
- [ ] Redo of a liked version: same side, framing, complete body — only the named element changes (A20 A22 C13).

## 1. Product
- [ ] Identical to the product photo: shape, lid, label layout, label text, colours, illustration (C6, LOCK).
- [ ] Real proportions — not squashed, not stretched; same scale as the template's product slot (C6 C17).
- [ ] Real 3D object: contact shadow, the scene's light, sits ON the surface (C10).
- [ ] Placement and gesture = the template's: held with fingers wrapped around it, upright, label to camera; on the lounger/sofa; in front of the face; in her hand (A8 C11).
- [ ] Count = the template's count (two jars if they had two; none if they had none) (C7 D6).
- [ ] Never covers the template's hero visual (C6).
- [ ] Wrapping elements (tape, ribbon, hands) don't cover the wordmark/illustration (F9).

## 2. Text
- [ ] Every string exactly as in the spec: no typo, no extra word, no duplicated line ("beer bell belly" on S55), no prompt words printed ("crossed" on S74) (D7).
- [ ] No text where the template has none; nothing printed on the product label by the model.
- [ ] Brand marks outside the label are the OFFICIAL logo file pasted by script (D19), no AI-drawn mark left, no ghost of the old one — zoom on every logo, sign, badge, cap: no "WILLDHORN"/"WIILDHORN" (D8; failed on S8 S18 S35 S43 and run-1 #2 #35).
- [ ] Placement: same position, size and spacing as the template; centred on the template's anchor; small text not glued to the headline (C9).
- [ ] Template's text treatment reproduced (sunscreen bubbles, handwriting, clay letters) (A10).
- [ ] No emoji boxes (□) in composited text (D9). ✓ ✕ rendered (DejaVu).
- [ ] Signed review format keeps a first name + initial only if the template is signed (B12).
- [ ] Each fact said once (the guarantee written twice on c0232).

## 3. Image vs angle
- [ ] The image SHOWS the problem or the result the text talks about (belly text → belly visible, not an arm) (C1 A2).
- [ ] Nothing of their product world survives: material, flavour, symbol (hair), body part (arm), logo/brand slot, innuendo object, packaging (A2 A7).
- [ ] No leftover props of their customer (their bottle in a hand, sequin skirts, kids' beds) (A12 C5 F11).
- [ ] Before/after: one problem state vs one solved state, difference obvious at first glance; progression faces the result, left → right (A16 A23 C12).
- [ ] Before image = maximum pain (problem huge, pushing toward the result); result image = the most colourful, rewarding one (C18).
- [ ] Split body: one body, same skin/shorts/pose, navel exactly on the cut (A9).
- [ ] Visual matches the line's meaning (sexual line → sexual image; the staging acts out the line: she initiates → she is on top) (A4 A32).
- [ ] Shock level ≥ the template's (A15).
- [ ] The scene is where OUR problem shows (no shower/bed copied for their reason) and on the direct benefit, not an indirect consequence (A3 A18).
- [ ] The copied action fits our product's real form (no powder for capsules) (A17 A30).
- [ ] Ingredient visual: recognizable silhouettes, fresh and appetizing, no veins/blood, not brown, not raw, nothing that reads as a killed animal or excrement; never a generic capsule (C2 C15).
- [ ] The format reveals what the product is made of in one second (C15); the source reads as itself (a bison, NOT a cow) (C16).
- [ ] Nothing ambiguous: no killed animal, no excrement look, no powder pile, no blood (C14).

## 4. People
- [ ] Every customer shown is the avatar's age and look (45–60, greying for Wildhorn) — including sexual scenes; not the template's model (A11 F3).
- [ ] Hands: five fingers, natural grip, object fully visible; faces not uncanny; everyone clearly adult (C11, CONS).
- [ ] Bare/soft male chest close-ups avoided on OpenAI (blocked) — shown through clothes/objects or via Seedream (F5).

## 5. Style and format
- [ ] Same render style as the template (Pixar stays Pixar, painting stays painting, UGC stays UGC) (C5 F2).
- [ ] Template's visual code kept on every panel, the result included (glow, accent colour) (C4).
- [ ] What made the template a winner is still there AND it is clear (C3).
- [ ] Square 1:1 re-flow dropped no element; or, for A25 ads, the template's own ratio is kept.
- [ ] Compliance (brand.json `compliance`): no fake testimonial presented as real, no forbidden claim number, no doctors/celebrities, no before/after body presented as a real customer.

## 6. The one-second test (last)
Look at it for one second as the avatar, never having heard of the brand: problem? promise? product? If any is missing → fail (B14, protocol 4).

## QC log format (per round, appended to the protocols page)
| Ad | Problem found | Fix applied | Rule |
|---|---|---|---|
| S35 | logo misspelled WILLDHORN on the sign | redo with icon-only sentence | D8 |
| S74 | Seedream wrote "crossed" + headline on the label | scene only + composite | D7 |

A defect seen twice in a QC log becomes a rule (and a lint check if it can be). A defect the reviewer catches that QC should have caught → add the check here.

## Defect catalogue — every defect QC (or the reviewer) found on Wildhorn, with the fix that worked
| Where | Defect | Fix that worked | Rule |
|---|---|---|---|
| B2 #2 | model drew the template's arm while the text says belly | say what NOT to draw; draw our body part | F1, A2 |
| B2 #4 | photoreal output on a Pixar template | name the style: "Pixar-style 3D, NOT photoreal" | F2, C5 |
| B2 #10 | template's young man copied | describe our avatar + "do NOT copy the template's person" | F3, A11 |
| B2 #13 | before/after barely different | concrete cues: belt holes, shirt tucked | C12, F4 |
| B2 #16 | jar squashed into the template's slot | real proportions; shrink the slot, not the jar | C6 |
| B2 #123/#262, B7 #62, c0123, c0262 | OpenAI blocked bare/soft male chest close-ups (even without the template) | show it through clothes/objects; or Seedream scene + composite | F5, D1 |
| B3 #22 | jar placed in front of the hero (split belly) | hero fully visible, jar small in its slot | C6, F6 |
| B4 #33 #35 | jar added where the template has no product | write "NO jar / NO product" explicitly | C7, F7 |
| B4 #38 | template's cow kept under the jar | "a bison, NOT a cow, no spots" | F8, C16 |
| B4 #26 | measuring tape hid the wordmark | wrapping elements stay off the label | F9 |
| B4 #35 | "WIILDHORN" | spell the wordmark letter by letter | F10 |
| B5 #35 | small wordmark "WILLDHORN" twice | small logo slot → icon only | D8, C7 |
| B7 #35 #61 | organs raw and glossy | (then) freeze-dried wording → (now) fresh, clean, appetizing, no veins | C2 |
| B8 #57 | text added at the bottom; jar not in her hand | nothing added; copy the gesture | B13, A8 |
| B8 #73 | text not centred on the eggplant | composite `cx` on the anchor | C9 |
| B9 #73 | small text glued to the headline | template's spacing between blocks | C9 |
| B9 #65 | flat text instead of sunscreen letters; product not 3D on the lounger | Nano Banana Pro letters; real 3D product with contact shadow | A10, C10 |
| c0232 (blueprint batch 01) | guarantee written twice | each fact once | B20 |
| c0245 (blueprint batch 01) | "Not reindeer" = implicit competitor reference | "Not farmed organs" | brand `banned` |
| Sam R2 S29 | apostrophe broke the text | re-render; check punctuation in quotes | QC |
| Sam R2 S38 | avatar too young | re-render with `OLD` | A11 |
| Sam R3 S8 S18 S35 S43 | "WILLDHORN" on signs/logos outside the label | icon-only sentence in every prompt; lint bare wordmark lines | D8 |
| Sam R3 S71 | cowboy still holding THEIR bottle | inventory SWAP every prop | C5, F11 |
| Sam R3 S47 | Barbie sequin skirts left on our man | inventory SWAP every prop | C5, F11 |
| Sam R3 S55 | typo "beer bell belly"; man too young | text by script; avatar age | D7, A11 |
| Sam R3 S58 S74 S79 | Seedream full ad: garbled label, "crossed" written, headline on the label | Seedream scene only + composite | D7 |
| Sam R3 S58 | emoji rendered as boxes in composited text | no emoji in composite | D9 |
| Sam R3 (2 ads) | crossed-price strike misplaced; text shadow too heavy | adjust `strikes` / `shadow` and re-render (free) | composite |
| Sam R3 S42 redo | pipeline printed "OK" 3× with no image (template .png vs real .jpg) | template exists check + count new files | D10 |
| Sam R3 S29 S33 S35, QC S55 S79, R4 S80 | spec pointed at another ad's template (found by the 2026-10-02 audit) | `tpl == sorted(templates)[num-1]` | D13 |
