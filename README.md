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

## Status

- Brand kit: **v1.5 locked** (`edenvia/BRAND-KIT.md`, `edenvia/brand.json`). Angle A8 lymphatic bloating; three sub-angles signed at gate 1 (legs/belly, puffy face, man's belly).
- Step 1: **done and signed off** — Lymphoria (lymphoria.co), 35 statics decoded (`edenvia/research/lymphoria/`).
- Step 2: families 1 (us vs them, 10) and 2 (before-after / timeline, 8) **briefed** — `edenvia/briefs/`, 18 briefs, lint OK. Gate 2 pending: the VPS session generates family 1, the founder validates (Loom 1 → rules), family 2 is retouched against those rules before it is generated, then families 3–9.
- Steps 3–5 run on the founder's VPS (`VPS-SETUP.md`).

## How the scripts find the brand

```
export SAC_WORKDIR=/path/to/blueprint-static/edenvia
python3 .claude/skills/static-ads/scripts/lint.py <spec file>
```

Everything produced by the system (specs, prompts, pages, rules, briefs) is in English.
