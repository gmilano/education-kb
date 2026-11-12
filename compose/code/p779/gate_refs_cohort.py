#!/usr/bin/env python3
"""p779: gate-refs, resolved by PASS COHORT.

gate-refs base-wide answers "how big is the unfalsifiable population". It does
not answer "is the convention real", because these shelves are append-only: a
row written at p300 could not have followed a convention invented at p777.
This splits every shelf at its `## ` section boundaries, attributes each section
to the pass number in its own heading, and reports the falsifiable share per
cohort. If the convention is real, the share must be high in the recent cohorts
and near zero in the old ones. If it is aspirational, it is low everywhere.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_refs import SHELVES, is_data_row, classify, has_ref

PASS = re.compile(r"`p(\d{1,4})`")

def run(root):
    coh = {}
    for sh in SHELVES:
        p = os.path.join(root, sh)
        if not os.path.exists(p): continue
        cur = None
        for line in open(p, encoding="utf-8", errors="replace"):
            if line.startswith("## "):
                m = PASS.search(line)
                cur = int(m.group(1)) if m else None
            if not is_data_row(line): continue
            pos, neg = classify(line)
            if not (pos or neg): continue
            d = coh.setdefault(cur, [0,0])
            d[0] += 1
            if has_ref(line): d[1] += 1
        # end shelf
    known = sorted([k for k in coh if k is not None])
    print(f"{'cohort':>10} {'lic rows':>9} {'with ref':>9} {'share':>8}")
    print("-"*40)
    # bucket
    buckets = [("p770-p778", range(770,779)), ("p750-p769", range(750,770)),
               ("p700-p749", range(700,750)), ("p600-p699", range(600,700)),
               ("p400-p599", range(400,600)), ("p1-p399",   range(1,400))]
    for name, rng in buckets:
        t = s = 0
        for k in rng:
            if k in coh: t += coh[k][0]; s += coh[k][1]
        if t: print(f"{name:>10} {t:>9} {s:>9} {100.0*s/t:>7.1f}%")
    if None in coh:
        t,s = coh[None]
        print(f"{'unattributed':>10} {t:>9} {s:>9} {100.0*s/t:>7.1f}%")
    print("-"*40)
    print(f"{'passes seen':>10} {len(known)}  (min p{min(known)}, max p{max(known)})")
    print("\nper-pass, the ten most recent attributed cohorts:")
    for k in known[-10:]:
        t,s = coh[k]
        print(f"  p{k}: {t:>6} licence rows, {s:>5} with ref  ({100.0*s/t:>5.1f}%)")

run(sys.argv[1])
