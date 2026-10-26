#!/usr/bin/env python3
"""Measure what the 40-line window costs, over every payload this base has
graded with it. Re-reads each payload first-hand at HEAD and grades it with
BOTH readers."""
import csv, importlib.util, os, sys, concurrent.futures as cf
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

def load(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    sv = sys.argv; sys.argv = [sv[0]]
    s.loader.exec_module(m); sys.argv = sv
    return m

old = load("p453v", os.path.join(ROOT, "compose/code/p453-vocabulary-ledger/verify.py"))
new = load("p454f", os.path.join(HERE, "family_title.py"))
vs  = load("vs", os.path.join(HERE, "value_sweep.py"))

# Population: every address+path this base has recorded a payload family for.
CELLS = {}
for tsv, a, p in [
    ("evidence/declared-vs-payload.2026-10-26-p453.tsv", 0, 4),
    ("evidence/carried-cell-licence-value.2026-10-26-p454.tsv", 3, 6),
]:
    with open(os.path.join(ROOT, tsv)) as f:
        rd = csv.reader(f, delimiter="\t"); next(rd)
        for r in rd:
            if len(r) > max(a, p) and r[a] and r[p]:
                CELLS[(r[a], r[p])] = tsv

print(f"population: {len(CELLS)} distinct (address, payload_path) pairs", file=sys.stderr)

RAW = {"github.com": "https://raw.githubusercontent.com/{s}/HEAD/{p}",
       "gitlab.com": "https://gitlab.com/{s}/-/raw/HEAD/{p}"}

def regrade(key):
    addr, path = key
    host = addr.split("/")[0]; slug = "/".join(addr.split("/")[1:])
    t = RAW.get(host)
    if not t:
        return addr, path, "FORGE", "FORGE", 0
    body, code, size = old.fetch(t.format(s=slug, p=path))
    if code != "200" or not body:
        return addr, path, "UNREACHABLE", "UNREACHABLE", 0
    return addr, path, old.family(body), new.family(body), size

rows = []
with cf.ThreadPoolExecutor(max_workers=8) as ex:
    for i, r in enumerate(ex.map(regrade, CELLS), 1):
        rows.append(r)
        if i % 50 == 0:
            print(f"  {i}/{len(CELLS)}", file=sys.stderr)

OUT = os.path.join(ROOT, "evidence", "family-reader-delta.2026-10-26-p454.tsv")
with open(OUT, "w") as f:
    f.write("address\tpayload_path\tfamily_40line_window\tfamily_title_block\tbytes\tagree\n")
    for a, p, o, n, s in rows:
        f.write(f"{a}\t{p}\t{o}\t{n}\t{s}\t{'AGREE' if o == n else 'DIFFER'}\n")

d = [r for r in rows if r[2] != r[3]]
print(f"\n=== reader delta: {len(d)} of {len(rows)} payloads grade DIFFERENTLY ===")
for a, p, o, n, s in sorted(d):
    print(f"  {a:50s} {p:14s} 40line={o:14s} title={n:18s} {s:>7d} B")
print("\n=== direction of the disagreement ===")
for k, v in Counter((o, n) for _, _, o, n, _ in d).most_common():
    print(f"  40line={k[0]:16s} -> title={k[1]:18s} {v:3d}")
print(f"\nwrote {OUT}")
