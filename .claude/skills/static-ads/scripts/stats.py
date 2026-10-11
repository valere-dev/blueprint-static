#!/usr/bin/env python3
"""Batch stats from calls.jsonl + validated.json (+ optional rounds.json). Writes $SAC_BATCH/stats.json and prints a table.
usage: stats.py [--ads N]        N = number of ads in the batch (default: number of specs found)

Definitions (3-improve/stats.md):
  generations         = every engine call logged by srun.py (ok or not; refusals count — they cost time)
  hit_rate_pct        = validated ads / generations
  gens_per_validated  = generations / validated ads
  first_try_pct       = ads whose verdict says 'first try' / ads reviewed
  after_one_fix_pct   = ads validated in <= 2 review rounds / ads
  final_pct           = validated / ads
  avg_rounds          = mean review rounds to validation (validated ads)
Rounds per ad: rounds.json {num: rounds} if it exists, else classified from the verdict text (the Wildhorn Sam batch convention):
  'first try' -> 1 ; 'redo 1' | '(redo)' | 'both tries' | '= sell' -> 2 ; 'after fix' | 'try 1 validated' -> 3 ; anything else -> 4 (+ warning)."""
import json, os, sys, collections, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C
from pages_common import load_json, load_specs

B = C.BATCH
calls = [json.loads(l) for l in open(f"{B}/calls.jsonl")] if os.path.exists(f"{B}/calls.jsonl") else []
val = load_json(f"{B}/validated.json", {})
rounds_file = load_json(f"{B}/rounds.json", None)
n_ads = int(sys.argv[sys.argv.index("--ads") + 1]) if "--ads" in sys.argv else len(load_specs()) or len(val)


def rounds_of(k, v):
    if rounds_file and k in rounds_file: return int(rounds_file[k])
    t = v.lower()
    if "first try" in t: return 1
    if re.search(r"redo 1|\(redo\)|both tries|= sell", t): return 2
    if re.search(r"after fix|try 1 validated", t): return 3
    print(f"warning: S{k} verdict '{v}' not classified -> 4 rounds (add it to rounds.json)", file=sys.stderr); return 4


ok = {k: v for k, v in val.items() if v.startswith("✅")}
r = {k: rounds_of(k, v) for k, v in ok.items()}
dist = collections.Counter(r.values())
gens = len(calls)
out = {"ads": n_ads, "reviewed": len(val), "validated": len(ok), "generations": gens,
       "refused_or_failed": sum(1 for c in calls if not c.get("ok")),
       "engines": dict(collections.Counter(f"{c['engine']}:{'ok' if c.get('ok') else 'fail'}" for c in calls)),
       "hit_rate_pct": round(100 * len(ok) / max(1, gens), 1),
       "gens_per_validated": round(gens / max(1, len(ok)), 2),
       "first_try_pct": round(100 * dist.get(1, 0) / max(1, len(val)), 1),
       "after_one_fix_pct": round(100 * (dist.get(1, 0) + dist.get(2, 0)) / max(1, n_ads), 1),
       "final_pct": round(100 * len(ok) / max(1, n_ads), 1),
       "avg_rounds": round(sum(r.values()) / max(1, len(r)), 2),
       "rounds_distribution": {str(k): dist[k] for k in sorted(dist)}}
json.dump(out, open(f"{B}/stats.json", "w"), indent=1)
for k, v in out.items(): print(f"{k:22} {v}")
