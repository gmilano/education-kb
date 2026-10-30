#!/usr/bin/env python3
"""derive-foundations.py -- Gap 544-E. Derive repos/foundations.md's shelf count.

p544 measured that this page's count is not derivable: 180 data rows across 31 tables,
several of them censuses, against a header figure of "seventy-two" that is pass arithmetic
(58 + 11 + 3) frozen at p534. This script makes the figure derivable by reading a DECLARED
disposition per table from ingest/foundations-disposition.tsv.

It reports two DIFFERENT quantities and never conflates them:
  rows      -- data rows in SHELF-disposition tables
  addresses -- distinct github.com/owner/repo in those rows (a row may name an upstream
               AND its fork, so addresses can exceed rows)

  systems   -- addresses minus DECLARED alias relations (ingest/foundations-alias.tsv).
               Gap 545-C, closed at p545: the relations are swept, not inferred.

Exit 0 green, 1 on a disagreement with the header, 2 on an undeclared table.
usage: python3 -I ingest/derive-foundations.py [repo-root]
"""
import os
import re
import sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
page = os.path.join(root, "repos", "foundations.md")
manifest = os.path.join(root, "ingest", "foundations-disposition.tsv")

lines = open(page, encoding="utf-8").read().split("\n")
heads = [(i, l) for i, l in enumerate(lines) if re.match(r"^#{2,3} ", l)]
heads.append((len(lines), "EOF"))

SEP = re.compile(r"^\|[\s:|-]+\|")


def tables_of(start, end):
    """Split a section into tables; a table is a run of | lines. First run line is its header."""
    out, cur = [], None
    for i in range(start + 1, end):
        l = lines[i]
        if l.startswith("|"):
            if cur is None:
                cur = {"line": i + 1, "rows": []}      # this line is the header
            elif SEP.match(l) and set(l.replace("|", "").strip()) <= set("-: "):
                pass                                    # separator
            else:
                cur["rows"].append(l)
        else:
            if cur:
                out.append(cur)
                cur = None
    if cur:
        out.append(cur)
    return out


# --- load declared dispositions, keyed by (section heading text, table ordinal) ----------
declared = {}
head_texts = {l for _, l in heads}
for raw in open(manifest, encoding="utf-8"):
    # A comment is a '#' line with NO tab in it. The keys themselves are markdown headings
    # and so also begin with '#': p545's first run skipped all 31 of them for that reason
    # and derived zero. Recorded because the bug is invisible when the result is a number.
    if not raw.strip() or (raw.lstrip().startswith("#") and "\t" not in raw):
        continue
    heading, ordinal, disp, note = (raw.rstrip("\n").split("\t") + ["", "", "", ""])[:4]
    # Keyed on the heading's own TEXT. p545's first draft keyed on line numbers and broke
    # on the first edit of the page it describes; the text survives edits above it.
    if heading not in head_texts:
        print(f"RED  manifest names a heading the page no longer carries:\n     {heading[:100]}")
        sys.exit(2)
    declared[(heading, int(ordinal))] = (disp, note)

# --- walk the page ------------------------------------------------------------------------
counts = {"SHELF": 0, "CENSUS": 0, "METRIC": 0, "SUMMARY": 0}
shelf_rows, shelf_addrs, undeclared = 0, set(), []
ADDR = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

for k in range(len(heads) - 1):
    s, h = heads[k]
    e = heads[k + 1][0]
    for t_i, t in enumerate(tables_of(s, e)):
        key = (h, t_i)
        if key not in declared:
            undeclared.append(f"L{t['line']} table#{t_i} under {h[:70]}")
            continue
        disp, _ = declared[key]
        counts[disp] = counts.get(disp, 0) + len(t["rows"])
        if disp == "SHELF":
            shelf_rows += len(t["rows"])
            for r in t["rows"]:
                shelf_addrs |= {a.rstrip(".") for a in ADDR.findall(r)}

print(f"repos/foundations.md  tables declared={len(declared)}")
for d in ("SHELF", "CENSUS", "METRIC", "SUMMARY"):
    print(f"  {d:8s} rows = {counts.get(d, 0)}")
# --- collapse declared alias relations onto addresses -> systems -------------------------
alias_file = os.path.join(root, "ingest", "foundations-alias.tsv")
aliases = {}
if os.path.exists(alias_file):
    for raw in open(alias_file, encoding="utf-8"):
        if not raw.strip() or (raw.lstrip().startswith("#") and "\t" not in raw):
            continue
        canonical, alias, sha, basis = (raw.rstrip("\n").split("\t") + [""] * 4)[:4]
        aliases[alias] = canonical
# an alias only collapses if BOTH ends are actually on the shelf; a relation naming an
# address this page does not hold is a stale declaration, not a reason to subtract.
collapsed = {a for a, c in aliases.items() if a in shelf_addrs and c in shelf_addrs}
stale = {a for a in aliases if a not in shelf_addrs}
systems = len(shelf_addrs) - len(collapsed)

print(f"  DERIVED shelf rows      = {shelf_rows}")
print(f"  DERIVED distinct addrs  = {len(shelf_addrs)}")
print(f"  DERIVED systems         = {systems}  (addrs minus {len(collapsed)} declared alias relation(s))")
if stale:
    print(f"  AMBER {len(stale)} declared alias relation(s) name an address not on the shelf:")
    for a in sorted(stale):
        print(f"        {a}")

if undeclared:
    print("RED  undeclared tables -- declare them in ingest/foundations-disposition.tsv:")
    for u in undeclared:
        print("   ", u)
    sys.exit(2)

# --- compare against the header ------------------------------------------------------------
m = re.search(r"\*\*(?:Pass\s+`p\d+`\s*·\s*)?\*?\*?([A-Z][a-z-]+(?:[ -][a-z-]+)*)\*{0,2}\s+(?:foundational|load-bearing)", "\n".join(lines[:60]))
claim = re.search(r"derived shelf rows:\s*\*\*(\d+)\*\*", "\n".join(lines[:60]), re.I)
if claim:
    if int(claim.group(1)) != shelf_rows:
        print(f"RED  header claims {claim.group(1)}, table derives {shelf_rows} -- rewrite the header.")
        sys.exit(1)
    print("GREEN header agrees with its tables.")
else:
    print("AMBER header carries no derived figure yet; write one as 'derived shelf rows: **N**'.")
sys.exit(0)
