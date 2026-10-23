#!/usr/bin/env python3
"""Run the Gap 406-A cross-check and print the agreement matrix + evidence TSV."""
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crosscheck import (LIVE_SHELVES, UNCLASSIFIED_SHELVES, classify_string, decay,
                        grade, load_i2_absent, load_sweep, shelf_lines, substring_inflation)

ROOT = sys.argv[1]
sweep = load_sweep(os.path.join(ROOT, "evidence/carried-existence.2026-10-23-p406.tsv"))
orig, folded = load_i2_absent(os.path.join(ROOT, "evidence/dead-citation-reprobe.2026-10-21-p372.tsv"))
live = shelf_lines(ROOT, LIVE_SHELVES)
graded = grade(sweep, orig, folded, live)

print("== AGREEMENT MATRIX over p406's 59 ABSENT-OR-PRIVATE addresses ==")
for mech, n in collections.Counter(r["mechanism"] for r in graded).most_common():
    print(f"  {n:3d}  {mech}")

print("\n== every row NOT in 'AGREE-OFF-LIVE-SHELVES' ==")
print(f"{'address':48} {'shape':18} {'inI2':5} {'fold':4} {'orig':4} {'ci':3} mechanism / first hit")
for r in graded:
    if r["mechanism"] == "AGREE-OFF-LIVE-SHELVES":
        continue
    print(f"{r['address']:48} {r['shape']:18} {r['in_i2_population']:5} "
          f"{r['i2_fires_folded']:4} {r['i2_fires_original']:4} {r['i2_fires_caseless']:3} "
          f"{r['mechanism']}  {r['first_hit']}")

print("\n== the sweep's non-addresses (p372's classifier refutes them as decay) ==")
nonaddr = [r for r in graded if r["shape"] != "ADDRESS"]
for r in nonaddr:
    print(f"  {r['shape']:20} {r['address']}")
print(f"  -> {len(nonaddr)} of 59")

res, unres, pub, corr = decay(sweep, len(nonaddr))
print(f"\n== decay ==\n  resolved={res} unresolved={unres} graded={res+unres}")
print(f"  p406 published : {pub*100:.2f} %")
print(f"  contaminants off both sides ({len(nonaddr)}): {corr*100:.2f} %")

print("\n== substring inflation in p406's attribution (`if a in body`) ==")
pairs = substring_inflation(sweep)
print(f"  {len(pairs)} swept address(es) are a proper substring of another swept address")
for a, b in pairs[:20]:
    print(f"    {a!r} inside {b!r}")

print("\n== shelves classified by NEITHER of p372's tuples ==")
for s in UNCLASSIFIED_SHELVES:
    print(f"  {s}")

# evidence TSV
out = os.path.join(ROOT, "evidence/i2-sweep-crosscheck.2026-10-23-p407.tsv")
with open(out, "w", encoding="utf-8") as fh:
    fh.write("# p407-i2-sweep-crosscheck — Gap 406-A: do gate-dead-citation I2 and\n")
    fh.write("# p406-carried-existence AGREE on the 59 ABSENT-OR-PRIVATE addresses?\n")
    fh.write("# Join key is FOLDED (p406 publishes folded, p372 publishes shelf casing).\n")
    fh.write("# i2_fires_* = occurrences of I2's detector on the three LIVE shelves:\n")
    fh.write("#   folded = detector fed p406's folded address (the repair this gap invites)\n")
    fh.write("#   original = detector fed p372's own casing (what ships today)\n")
    fh.write("#   caseless = detector made case-insensitive (the ceiling of a link test)\n")
    fh.write("address\tshape\ton_live_shelf\tin_i2_population\t"
             "i2_fires_folded\ti2_fires_original\ti2_fires_caseless\tmechanism\tfirst_hit\n")
    for r in graded:
        fh.write("\t".join(str(r[k]) for k in (
            "address", "shape", "on_live_shelf", "in_i2_population", "i2_fires_folded",
            "i2_fires_original", "i2_fires_caseless", "mechanism", "first_hit")) + "\n")
print(f"\nwrote {out} ({len(graded)} rows)")
