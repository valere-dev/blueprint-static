#!/usr/bin/env python3
"""File one or more ad images into the swipe-file family folder and append to its INDEX.md.

Usage:
  python3 file_ad.py --swipefile <root> --family F3 --confidence probable --cue "reframe sentence" a.webp b.png
The classification itself is done by the sort-ad skill (vision + decision tree); this script only files.
"""
import argparse, json, os, shutil, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
FAMILIES = json.load(open(os.path.join(HERE, '..', 'families.json')))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--swipefile', required=True, help='root folder of the sorted swipe file')
    ap.add_argument('--family', required=True, help='F1..F9 or NH')
    ap.add_argument('--confidence', default='sure', choices=['sure', 'probable', 'uncertain'])
    ap.add_argument('--cue', default='', help='the one cue that decided the family')
    ap.add_argument('--runner-up', default='', help='second family when not sure')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('images', nargs='+')
    a = ap.parse_args()

    fam = a.family.upper()
    if fam not in FAMILIES:
        sys.exit(f'unknown family {a.family}; expected one of {", ".join(FAMILIES)}')
    dst_dir = os.path.join(a.swipefile, FAMILIES[fam]['folder'])
    if not os.path.isdir(a.swipefile):
        sys.exit(f'swipefile root not found: {a.swipefile}')
    os.makedirs(dst_dir, exist_ok=True)
    index = os.path.join(dst_dir, 'INDEX.md')
    today = datetime.date.today().isoformat()

    for src in a.images:
        if not os.path.isfile(src):
            print(f'SKIP (not a file): {src}'); continue
        name = os.path.basename(src)
        dst = os.path.join(dst_dir, name)
        if os.path.exists(dst):
            print(f'SKIP (already there): {dst}'); continue
        line = f'- {name} — {fam} {FAMILIES[fam]["name"]} — {a.confidence}' \
               + (f' — cue: {a.cue}' if a.cue else '') \
               + (f' — runner-up: {a.runner_up}' if a.runner_up else '') + f' — {today}'
        if a.dry_run:
            print(f'DRY: {src} -> {dst}\n     {line}'); continue
        shutil.copy2(src, dst)
        new_index = not os.path.exists(index)
        with open(index, 'a') as f:
            if new_index:
                f.write(f'# {FAMILIES[fam]["folder"]}\n{FAMILIES[fam]["definition"]}\n')
            txt = open(index).read()
            if '## Sorted by sort-ad' not in txt:
                f.write('\n## Sorted by sort-ad\n')
            f.write(line + '\n')
        print(f'OK: {dst}')

if __name__ == '__main__':
    main()
