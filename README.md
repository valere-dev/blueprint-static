# blueprint-static — Edenvia static ads system

Home of the static-ads production system for **Edenvia** (edenvia.com), reproduced 1:1 from the
Blueprint built for Wildhorn (blueprint.machineroom.app). Same method, same skill, same review loop,
same rules — only the brand input changes.

## Layout

| Path | What |
|---|---|
| `.claude/skills/static-ads/` | The generic skill, installed as shipped (SKILL.md, 1-understand/, 2-make/, 3-improve/, scripts/). Its `brand.json` stays the blank template. Adapted in place as the founder's reviews add rules; never duplicated. |
| `edenvia/` | The brand working folder (`SAC_WORKDIR`). `BRAND-KIT.md` + `brand.json` are the only brand input the skill reads. `assets/` holds logos, product photo and cutout. Batches, specs, outputs, pages and feedback will live here. |

The Wildhorn-filled example (`wildhorn-static-ads`) and the Blueprint pages stay in the founder's Drive
as reference; they are not copied into this repo.

## Status

- Brand kit: **draft v0.1**, awaiting the founder's verdicts (see the open items at the end of `edenvia/BRAND-KIT.md`).
- Step 1 (market research on one competitor's 35 ads): not started — competitor not chosen.

## How the scripts find the brand

```
export SAC_WORKDIR=/path/to/blueprint-static/edenvia
python3 .claude/skills/static-ads/scripts/lint.py <spec file>
```

Everything produced by the system (specs, prompts, pages, rules, briefs) is in English.
