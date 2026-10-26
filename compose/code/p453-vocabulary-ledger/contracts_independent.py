#!/usr/bin/env python3
"""Independent re-implementation of the load-bearing contracts.

make hooks was DENIED (Code from External), 8th in 9 passes, so these are read
from the gate sources and re-implemented rather than run. This is a mitigation,
NOT a substitute: 5 controls of 62.
"""
import re, sys, os
os.chdir("/tmp/education-kb")

VOCAB = ["North America", "EMEA", "APAC", "LATAM", "Global"]      # check_headings.py:17
CANON = re.compile(r"^## +Opportunities by region\s*$", re.M)     # check_headings.py:18
H2 = re.compile(r"^## (?!#)", re.M)
SHELVES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "compose/patterns.md", "intel/open-gaps.md"]
fail = 0

# --- C1: frontmatter keys + CLOSED region vocabulary on every shelf ---------
for f in SHELVES:
    src = open(f).read()
    m = re.match(r"^---\n(.*?\n)---\n", src, re.S)
    if not m:
        print(f"C1 FAIL {f}: no frontmatter"); fail += 1; continue
    fm = dict(re.findall(r"^(\w+): *(.+?)\s*$", m.group(1), re.M))
    missing = [k for k in ("industry", "region", "updated") if k not in fm]
    if missing:
        print(f"C1 FAIL {f}: missing {missing}"); fail += 1
    if fm.get("region") not in VOCAB:
        print(f"C1 FAIL {f}: region {fm.get('region')!r} out of vocabulary"); fail += 1
    if fm.get("updated") != "2026-10-26":
        print(f"C1 FAIL {f}: updated={fm.get('updated')}"); fail += 1
print(f"C1 frontmatter+region vocabulary: {len(SHELVES)} shelves checked")

# --- C2: market.md -- EXACTLY ONE canonical block, 5 children, no extras ----
src = open("intel/market.md").read()
hits = CANON.findall(src)
if len(hits) != 1:
    print(f"C2 FAIL: {len(hits)} canonical blocks"); fail += 1
else:
    s = CANON.search(src).end()
    n = H2.search(src, s)
    block = src[s:n.start() if n else len(src)]
    kids = [k.strip() for k in re.findall(r"^### +(?!#)(.+?)\s*$", block, re.M)]
    region_kids = [k for k in kids if not re.match(r"^[\U0001F300-\U0001FAFF]|`", k)]
    oov = [k for k in region_kids if k not in VOCAB]
    miss = [v for v in VOCAB if v not in region_kids]
    print(f"C2 market.md: 1 canonical block, {len(region_kids)} region children, "
          f"{len(oov)} out-of-vocab, {len(miss)} missing")
    if oov: print(f"   C2 FAIL out-of-vocab: {oov}"); fail += 1
    if miss: print(f"   C2 FAIL missing: {miss}"); fail += 1
    if "LATAM" in region_kids and any(v not in region_kids for v in ("North America","EMEA","APAC")):
        print("   C2 FAIL LATAM-ONLY"); fail += 1

# --- C3: newest-FIRST -- p453 block precedes p452 on every shelf ------------
for f in SHELVES:
    src = open(f).read()
    a, b = src.find("`p453`"), src.find("`p452`")
    if a == -1:
        print(f"C3 FAIL {f}: no p453 block"); fail += 1
    elif b != -1 and a > b:
        print(f"C3 FAIL {f}: p453 does not precede p452"); fail += 1
print("C3 newest-first insertion: 9 shelves checked")

# --- C4: append-only byte containment on the two trending shelves ----------
for f, pre in (("agents/trending.md", "/tmp/claude-0/pre-agents-trending.md"),
               ("repos/trending.md", "/tmp/claude-0/pre-repos-trending.md")):
    body = open(pre).read().split("---\n", 2)[2].lstrip("\n")
    if body not in open(f).read():
        print(f"C4 FAIL {f}: prior body not contained verbatim"); fail += 1
    else:
        print(f"C4 {f}: prior body {len(body)} B contained verbatim")

# --- C5: no table-header-shaped row written as DATA ------------------------
# A row is a defect only when EVERY cell is a generic field name and it is not
# followed by a separator row -- p452 took three cuts to get this right (its
# cut 1 flagged all 812 legitimate headers, cut 2 flagged 42 transposed tables).
GENERIC = {"nombre", "repo", "licencia", "name", "license", "licence", "repository",
           "description", "descripcion", "url", "region", "notes", "tier"}
defects = 0
for f in SHELVES:
    lines = open(f).read().splitlines()
    for i, l in enumerate(lines):
        if not l.strip().startswith("|"):
            continue
        cells = [c.strip().strip("*`").lower() for c in l.strip().strip("|").split("|")]
        if len(cells) < 2 or not all(c in GENERIC for c in cells if c):
            continue
        nxt = lines[i+1] if i+1 < len(lines) else ""
        if not re.match(r"^\s*\|[\s:|-]+\|?\s*$", nxt):
            print(f"C5 FAIL {f}:{i+1}: header-shaped row as data: {l.strip()[:70]}")
            defects += 1
print(f"C5 table-header-as-data: {defects} defects")
fail += defects

print("\n" + ("ALL CONTRACTS GREEN (5 of 62 controls)" if fail == 0 else f"{fail} CONTRACT DEFECTS"))
sys.exit(1 if fail else 0)
