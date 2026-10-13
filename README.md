# blueprint-static — Edenvia static ads system

Home of the static-ads production system for **Edenvia** (edenvia.com), reproduced 1:1 from the
Blueprint built for Wildhorn (blueprint.machineroom.app). Same method, same skill, same review loop,
same rules — only the brand input changes.

## Layout

| Path | What |
|---|---|
| `.claude/skills/static-ads/` | The generic skill, installed as shipped (SKILL.md, 1-understand/, 2-make/, 3-improve/, scripts/). Its `brand.json` stays the blank template. Adapted in place as the founder's reviews add rules; never duplicated. |
| `edenvia/` | The brand working folder (`SAC_WORKDIR`). `BRAND-KIT.md` + `brand.json` are the only brand input the skill reads. `assets/` holds logos, product photo and cutout; `avatars/` the founder's 9 avatar sheets; `research/<competitor>/` step 1; `batch/templates/` the step-2 templates (D10 naming) and `batch/B01-clone-plan.md`; `briefs/` one hand-off brief JSON per template (worksheet §9) that `scripts/brief2spec.py` turns into specs on the VPS; `pages/` review pages. Specs, outputs and feedback are produced on the VPS (see `VPS-SETUP.md`). |

The Wildhorn-filled example (`wildhorn-static-ads`) and the Blueprint pages stay in the founder's Drive
as reference; they are not copied into this repo.

## Status (2026-10-11)

**Read `SOP.md` first** — the current process (one kie call per ad, `edenvia/batch/pipeline2.py`), the founder's rules, the costs, the state of every batch
and the bootstrap prompt for a new session. The skill under `.claude/skills/static-ads/` is the original Wildhorn method, kept for reference; its
generation pipeline (briefs → specs → lint → OpenAI direct → cutout pasting) was retired by the founder on 2026-10-11.

- Batch U (the whole swipe file, 270 templates): **v1 validated by the founder** — `edenvia/batch/validated-U/` (269 PNG).
- Family 1 (10) and batch T (25): generated, see `edenvia/pages/`.
