#!/usr/bin/env python3
"""p587 — RETAINED AS A NEGATIVE CONTROL. DO NOT WIRE THIS INTO A GATE.

WHAT THIS IS.  A naive cross-page licence reconciliation sweep, written at p587
to close `586-A`, which asserted that "a `grep` of every curated page for each
repo address, run before commit" did not exist in this base.

WHY IT IS A NEGATIVE CONTROL AND NOT AN INSTRUMENT.

  1. `586-A` WAS FALSE.  The step exists and BLOCKS COMMITS:
       gate-shelf-consistency  ->  compose/code/p308-shelf-consistency/
       Makefile:660, 59 controls, listed in HOOK_GATES at Makefile:128,
       enforced by ingest/pre-commit.
     Two further sweeps exist: compose/code/p121-stale-token-crosspage/
     crosspage.py (p121, licence tokens) and ingest/crosspage-figure-claims.py
     (p538, numeric claims).  p121's successor says so in its own docstring,
     nine lines in.  This file is the FOURTH rediscovery of that instrument.

  2. ITS OUTPUT WAS 100% FALSE POSITIVES.  Over 679 addresses on the curated
     pages it reported 10 licence contradictions.  Hand-audited: 0 were base
     defects.  All 10 had one shape -- a table row naming ONE repo URL and TWO
     licences, the second belonging to a platform or comparator named in the
     same row:

       compose/patterns.md:1647   | Canvas (AGPL-3.0) | bruchris/canvas-lms-mcp
                                  | **MIT** |      <- AGPL is CANVAS. Row correct.
       compose/patterns.md:1648   | Open edX (AGPL-3.0) | openedx/XBlock
                                  | Apache-2.0 |   <- the row calls this "the key fact"
       README.md:5282             okpy/ok correction narrative; the MIT in that
                                  sentence belongs to `gradethis`
       verticals/solutions.md:336 openSIS-Classic already reads "NONE ... BLOCK"

     Three "corrections" were drafted from this output and WITHDRAWN at audit.

  3. p308's control list, verbatim from Makefile:661, covers "comparators,
     possessives, quoted claims, dual grants, paired rows" -- the exact four
     classes above, enumerated ~280 passes earlier.

THE LESSON, which is why the file is kept: READ ingest/ AND THE Makefile GATE
LIST BEFORE BUILDING AN INSTRUMENT.  The three refinements below (same-line ->
table rows only -> single-address rows -> one-row-one-claim) took the count from
108 to 47 to 10 and never reached 0, because the remaining class cannot be
separated by row shape alone.  p308 solved that with 59 controls.  Use p308.

Run:  python3 -I ingest/p587-crosspage-naive.py .
"""
import re, sys, os, collections

CURATED = ["agents/top.md","repos/foundations.md","verticals/solutions.md",
           "intel/market.md","intel/trends.md","compose/patterns.md","README.md"]
ADDR = re.compile(r'github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?=[)\s/#,`"\']|$)')
LIC = re.compile(r'\b(MIT|Apache-2\.0|BSD-3-Clause|BSD-2-Clause|ECL-2\.0|CC0-1\.0|CC-BY-SA-4\.0|'
                 r'AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-3\.0|MPL-2\.0|BUSL-1\.1|EPL-2\.0|'
                 r'NOASSERTION|Unlicense|WTFPL)', re.I)
CANON = {"apache-2.0":"Apache-2.0","mit":"MIT","bsd-3-clause":"BSD-3-Clause",
         "bsd-2-clause":"BSD-2-Clause","ecl-2.0":"ECL-2.0","cc0-1.0":"CC0-1.0",
         "cc-by-sa-4.0":"CC-BY-SA-4.0","agpl-3.0":"AGPL-3.0","gpl-3.0":"GPL-3.0",
         "gpl-2.0":"GPL-2.0","lgpl-3.0":"LGPL-3.0","mpl-2.0":"MPL-2.0",
         "busl-1.1":"BUSL-1.1","epl-2.0":"EPL-2.0","noassertion":"NOASSERTION",
         "unlicense":"Unlicense","wtfpl":"WTFPL"}
root = sys.argv[1] if len(sys.argv) > 1 else "."
pages = collections.defaultdict(set)      # addr -> pages
claims = collections.defaultdict(set)     # (addr) -> {(page, licence)}
SKIP_OWNERS = {"topics","features","orgs","collections","sponsors","apps","marketplace","settings","trending","about","search"}

for page in CURATED:
    p = os.path.join(root, page)
    if not os.path.exists(p): continue
    for line in open(p, encoding="utf-8", errors="replace"):
        found = []
        for m in ADDR.finditer(line):
            owner, repo = m.group(1), m.group(2).rstrip('.')
            if owner.lower() in SKIP_OWNERS or not repo or repo.endswith('.md'): continue
            found.append(f"{owner}/{repo}")
        for addr in found:
            pages[addr].add(page)
        # Attribute a licence token to an address ONLY from an unambiguous row:
        # a table row (leading pipe) naming exactly ONE address. A row naming
        # several addresses cannot tell us which licence belongs to which, and
        # prose lines list repos and licences in unrelated order. Both are skipped:
        # attributing there is what produced 108 false contradictions on the first run.
        if not line.lstrip().startswith('|'): continue
        uniq = set(found)
        if len(uniq) != 1: continue
        addr = uniq.pop()
        # One row = ONE claim. These tables put the licence in its own early column
        # and then discuss it in the prose column ("ECL-2.0 is an Apache-2.0
        # derivative", "LGPL-3.0, API reports NOASSERTION"). Taking every token in
        # the row turns that commentary into a fake disagreement, so the claim is
        # the FIRST licence token in the EARLIEST pipe-field that holds one.
        for field in line.split('|'):
            lm = LIC.search(field)
            if lm:
                claims[addr].add((page, CANON[lm.group(1).lower()]))
                break

print(f"addresses on curated pages: {len(pages)}")
multi = {a: ps for a, ps in pages.items() if len(ps) > 1}
print(f"addresses appearing on more than one curated page: {len(multi)}")

print("\n=== CONTRADICTIONS: one address, different licence tokens on different pages ===")
n = 0
for addr in sorted(claims):
    by_lic = collections.defaultdict(set)
    for page, lic in claims[addr]:
        by_lic[lic].add(page)
    if len(by_lic) > 1:
        n += 1
        print(f"\n{addr}")
        for lic, ps in sorted(by_lic.items()):
            print(f"   {lic:14s} <- {', '.join(sorted(ps))}")
print(f"\ncontradictory addresses: {n}")
