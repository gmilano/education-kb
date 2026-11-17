#!/usr/bin/env python3
"""p870 -- 869-G2: the duplicate-ROW rate over ALL counted rows, not just the 152 stale ones
868-G2's marking run happened to touch.

Population is the count gate's own, imported rather than re-guessed: a table counts only when
its header line is one of the signatures declared in derive-counts.py SHELVES.  Reading them
with `ast` (868-G2's trick) means this instrument cannot drift from the gate it reports against.

For each (shelf, address) pair carrying more than one row it publishes whether the rows AGREE
on licence and on region -- because 869-G2 is explicit that two rows that DISAGREE are worse
than two rows that repeat.
"""
import ast, collections, re, sys

SRC = "ingest/derive-counts.py"
tree = ast.parse(open(SRC).read())
SHELVES = None
for n in ast.walk(tree):
    if isinstance(n, ast.Assign):
        for t in n.targets:
            if isinstance(t, ast.Name) and t.id == "SHELVES":
                SHELVES = ast.literal_eval(n.value)
assert SHELVES, "SHELVES not found in %s" % SRC

ADDR = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
# the licence vocabulary this base actually uses, longest-first so AGPL-3.0 never reads as GPL-3.0
LICS = ["AGPL-3.0","LGPL-3.0","LGPL-2.1","GPL-3.0","GPL-2.0","Apache-2.0","BSD-3-Clause",
        "BSD-2-Clause","MPL-2.0","EPL-2.0","ECL-2.0","CC0-1.0","CC-BY-SA-4.0","CC-BY-4.0",
        "MulanPSL-2.0","Unlicense","Zlib","WTFPL","MIT","NOASSERTION","NO GRANT","NONE"]
REGIONS = ["North America","EMEA","APAC","LATAM","Global","refused","REFUSED"]

def lic_of(row):
    for l in LICS:
        if l.lower() in row.lower():
            return l
    return "-"

def reg_of(row):
    found = [r for r in REGIONS if r.lower() in row.lower()]
    if not found: return "-"
    # 'refused' is a posture, not a region; report it only when no real region is present
    real = [r for r in found if r.lower() not in ("refused",)]
    return real[0] if real else "refused"

out = []
totals = collections.Counter()
for rel, sigs, excluded in SHELVES:
    sigset = set(sigs)
    lines = open(rel).read().split("\n")
    rows_by_addr = collections.defaultdict(list)
    counted_rows = 0
    in_tbl = False
    for ln in lines:
        s = ln.strip()
        if s in sigset:
            in_tbl = True; continue
        if in_tbl:
            if not s.startswith("|"):
                in_tbl = False; continue
            if re.match(r"^\|[\s:|-]+\|$", s):   # the --- separator
                continue
            m = ADDR.search(s)
            if not m:
                continue
            counted_rows += 1
            rows_by_addr[m.group(1)].append(s)
    totals[rel] = counted_rows
    dups = {a: r for a, r in rows_by_addr.items() if len(r) > 1}
    for a, rws in sorted(dups.items()):
        lics = sorted({lic_of(r) for r in rws})
        regs = sorted({reg_of(r) for r in rws})
        out.append((rel, a, len(rws),
                    "AGREE" if len(lics) == 1 else "DISAGREE", "|".join(lics),
                    "AGREE" if len(regs) == 1 else "DISAGREE", "|".join(regs)))

print("shelf\taddress\trows\tlicence\tlicence_values\tregion\tregion_values")
for r in out:
    print("\t".join(str(x) for x in r))

sys.stderr.write("\n=== per-shelf ===\n")
grand_rows = grand_extra = 0
for rel, sigs, exc in SHELVES:
    d = [o for o in out if o[0] == rel]
    extra = sum(o[2] - 1 for o in d)
    grand_rows += totals[rel]; grand_extra += extra
    sys.stderr.write("%-24s counted_rows=%4d  dup_addresses=%2d  extra_rows=%2d  rate=%.2f%%\n"
                     % (rel, totals[rel], len(d), extra,
                        100.0 * extra / totals[rel] if totals[rel] else 0))
sys.stderr.write("%-24s counted_rows=%4d  dup_addresses=%2d  extra_rows=%2d  rate=%.2f%%\n"
                 % ("TOTAL", grand_rows, len(out), grand_extra,
                    100.0 * grand_extra / grand_rows if grand_rows else 0))
lic_dis = [o for o in out if o[3] == "DISAGREE"]
reg_dis = [o for o in out if o[5] == "DISAGREE"]
sys.stderr.write("licence DISAGREE: %d\nregion  DISAGREE: %d\n" % (len(lic_dis), len(reg_dis)))
