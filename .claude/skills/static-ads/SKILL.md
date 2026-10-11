---
name: static-ads
description: >
  Make winning static ads for ANY brand, from analysis to finished files, with a review loop that never
  regresses. Everything needed is inside: find the angles (product → mechanism → angle, avatar, research
  winners, decode templates), clone winning templates into the brand's own ads (spec, checker, image
  engines, real product pasted by script, full-size QC), review 10 at a time by Loom, and turn every
  comment into a permanent rule. The only input it needs from you is the brand kit (voice, facts,
  offer, product photo). Use for: "make ads for <brand>", "clone these templates", "new batch",
  "analyze this ad / competitor", "find the angles", "here is my Loom", "redo the ads", "fais-moi des
  ads", "nouveau batch", "trouve les angles". For Wildhorn, use wildhorn-static-ads (same skill, brand
  already loaded).
---

# Static Ads — winning static ads for any brand

**What it does:** takes ads that already win (templates) and turns them into the brand's own ads with
its real product, then learns from every review so the next batch is better.

**Proven:** on Wildhorn, the first batch had 0 % of ads accepted on the first try. After this system:
**71 % first try, 87 % after one fix, 100 % final**, 1.4 review rounds per ad instead of 2.5.

**The only thing you bring:** the brand kit (`BRAND-KIT.md` + `brand.json`) and the templates to clone.

---

## The 6 steps

| # | Step | What happens | Open |
|---|---|---|---|
| 1 | **Brand kit** | Fill the brand's voice, facts, offer, proof, avatar, banned words, product photo. Never invent a fact: unknown = `[MISSING]`, ask. | `BRAND-KIT.md`, `brand.json` |
| 2 | **Understand** | Product → mechanisms → angles. Who buys (avatar). Find ads that win (research). Decode each template: what it says, its visual trick, how it was made. | `1-understand/` |
| 3 | **Make** | One spec per template (what to KEEP, what to SWAP). The checker blocks bad specs. Generate, paste the real product + exact text by script, check every ad at full size. | `2-make/` |
| 4 | **Review** | 10 ads per batch on a review page. The founder records a Loom. Transcribe it, write each verdict. | `2-make/review-and-pages.md` |
| 5 | **Improve** | Every comment becomes a permanent rule (and an automatic check when possible). Fix the misses, keep the wins frozen. | `3-improve/` |
| 6 | **Measure** | First-try rate, after-one-fix rate, final rate, rounds per ad. Compare with the last batch. | `3-improve/stats.md` |

Then repeat from step 3 with the next 10.

---

## The 12 golden rules (everything else is detail)

1. **Clone a winner: same skeleton, new flesh.** Change the minimum. The template already works.
2. **Read the template as OUR customer would.** If a line already works for us, copy it word for word.
3. **Copy the visual trick, and how it was made.** A photo with a pasted product → edit that photo and
   swap only the product. Keep the format (9:16 stays 9:16).
4. **The product is always the real one.** The real cutout and the exact text are pasted by script;
   an AI never draws the label or the text alone.
5. **Every line carries the brand's core problem in plain words** (Wildhorn: "beer belly", never just
   "belly"). Simplest words win.
6. **Real facts only.** Price, offer, stats, guarantee come from `brand.json`. Never invent a number.
7. **Our customer, not theirs.** Our avatar's age and look; remove every prop of their brand.
8. **The picture must act out the line.** Before/after stays before/after; if she initiates, she leads.
9. **Logo outside the label = the icon only.** AI misspells brand names.
10. **A validated version is frozen.** Redo only what was criticized. The founder's latest verdict wins.
11. **"OK" means a new file exists on disk.** Check the template path, check the output, then QC at full size.
12. **Every review comment becomes a rule.** Rules are only added, never deleted. The checker blocks repeats.

The full rulebook (97 rules + prompt craft + system rules, each with the case it came from):
`3-improve/rules.md`.

---

## Where to look

| You need to… | Open |
|---|---|
| Start a new brand from zero | `BRAND-KIT.md`, then `1-understand/new-brand-worksheet.md` |
| Find mechanisms and angles | `1-understand/product-mechanism-angle.md`, `1-understand/avatar-angle-system.md` |
| Find winning ads to clone | `1-understand/research-playbook.md`, `1-understand/competitor-case-studies.md` |
| Understand why an ad works | `1-understand/ad-dna.md`, `1-understand/frameworks-evolve-crafter.md`, `1-understand/copy-analysis.md` |
| Decode a template before cloning | `1-understand/template-reading.md` |
| See the analysis workflows in full | `1-understand/WORKFLOWS.md` |
| Write a spec | `2-make/spec-format.md` |
| Pick the image engine / handle a refusal | `2-make/engines.md` |
| Paste the product and text | `2-make/composite.md` |
| Check an ad before showing it | `2-make/qc-checklist.md` |
| See the full production pipeline | `2-make/PIPELINE.md` |
| Turn a Loom into rules | `3-improve/feedback-loop.md` |
| All the rules | `3-improve/rules.md` |
| Compute the stats | `3-improve/stats.md` |
| Run the scripts | `scripts/README.md` |

---

## How to work with the founder

- Never make them type commands or read code. They review images and record Looms; you do the rest.
- Show ads 10 at a time, numbered, with every try visible and the version to launch highlighted.
- After each Loom: a table of every ad and its verdict, what was fixed, and the new rules.
- Everything in English.
