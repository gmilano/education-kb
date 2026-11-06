#!/usr/bin/env python3
"""p678 filing gate — discharges ACTION p677-B.

For every ledger row whose filed_on names shelf files, assert the address
actually appears in each named file. No network, no model, zero cost.
Exit 1 if any claim is false.
"""
import csv, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
LEDGER = os.path.join(ROOT, 'evidence', 'address-ledger.tsv')

def load(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def main(only_pass=None):
    rows = load(LEDGER)
    cache = {}
    checked = ok = bad = 0
    failures = []
    for r in rows:
        filed = (r.get('filed_on') or '-').strip()
        if filed in ('', '-'):
            continue
        if only_pass and r.get('first_seen_pass') != only_pass:
            continue
        addr = r['address'].strip()
        for cell in [s.strip() for s in filed.split(',') if s.strip()]:
            # a cell may be "path" or "path:anchor" -- the anchor is a note, not part of the path
            shelf = cell.split(':', 1)[0].strip()
            p = os.path.join(ROOT, shelf)
            if shelf not in cache:
                try:
                    cache[shelf] = open(p, encoding='utf-8').read().lower()
                except FileNotFoundError:
                    cache[shelf] = None
            body = cache[shelf]
            checked += 1
            if body is None:
                bad += 1; failures.append((addr, shelf, 'SHELF FILE MISSING')); continue
            if addr.lower() in body:
                ok += 1
            else:
                bad += 1; failures.append((addr, shelf, 'ADDRESS ABSENT from the file its cell names'))
    scope = only_pass or 'ALL PASSES'
    print(f"filing gate ({scope}): {checked} claims checked, {ok} true, {bad} FALSE")
    for a, s, why in failures:
        print(f"  FALSE  {a:<48} -> {s:<28} {why}")
    # controls: a claim that must pass and a claim that must fail
    top = cache.get('agents/top.md') or open(os.path.join(ROOT,'agents/top.md'),encoding='utf-8').read().lower()
    assert 'moodlehq/wiki-rag' in top, "CONTROL-POSITIVE FAILED: known-filed address not found"
    assert 'zzqxnonsense/p678-control' not in top, "CONTROL-NEGATIVE FAILED: nonsense address found"
    print("controls: positive PASS, negative PASS")
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
