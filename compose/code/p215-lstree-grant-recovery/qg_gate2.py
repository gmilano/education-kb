"""ACTION QG, tightened: a GRANT CELL is a table row (or a sentence) that makes a
claim about the repo's grant -- either a licence token or an absence marker.
A prose mention with no grant claim is not a cell and is not an error.
"""
import os
import re

KB = "/home/user/education-kb"
CURRENT_STATE = ["agents/top.md", "repos/foundations.md", "verticals/solutions.md",
                 "intel/market.md", "compose/patterns.md", "intel/trends.md"]
APPEND_ONLY = ["agents/trending.md", "repos/trending.md"]

RECOV = {}
with open("qd_recoveries.tsv") as fh:
    next(fh)
    for line in fh:
        slug, grant, path, nb, ch = line.rstrip("\n").split("\t")
        RECOV[slug] = grant

GRANT = re.compile(r"(MIT|Apache-2\.0|AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-3\.0|LGPL-2\.1|"
                   r"ECL-2\.0|BSD-[23]-Clause|MPL-2\.0|ISC|Unlicense)", re.I)
ABSENCE = re.compile(r"(sin licencia|no licence|no license|\bABSENT\b|ungranted|"
                     r"NONE\b|none found|sin archivo|NO grant|without a grant|"
                     r"no public grant|absent `?LICENSE)", re.I)

rows = []
for rel in CURRENT_STATE + APPEND_ONLY:
    p = os.path.join(KB, rel)
    if not os.path.exists(p):
        continue
    with open(p, encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh, 1):
            for slug in RECOV:
                if slug.lower() not in line.lower():
                    continue
                g = sorted(set(m.group(0).upper() for m in GRANT.finditer(line)))
                a = sorted(set(m.group(0) for m in ABSENCE.finditer(line)))
                if not g and not a:
                    continue          # a mention, not a cell
                rows.append((slug, RECOV[slug], rel, i, g, a, line.strip()))

cs = [r for r in rows if r[2] in CURRENT_STATE]
ao = [r for r in rows if r[2] in APPEND_ONLY]

wrong_absence, wrong_family, ok = [], [], []
for r in cs:
    slug, truth, rel, i, g, a, text = r
    tfam = truth.split(" ")[0].upper()
    if tfam in g:
        ok.append(r)
    elif a:
        wrong_absence.append(r)
    elif g:
        wrong_family.append(r)

print("repos established this pass           : %d" % len(RECOV))
print("grant-CLAIM lines touching them       : %d  (current-state %d, append-only %d)"
      % (len(rows), len(cs), len(ao)))
print()
print("=" * 72)
print("CLASS A -- current-state cells asserting ABSENCE for a repo that HAS a grant: %d"
      % len(wrong_absence))
print("=" * 72)
for slug, truth, rel, i, g, a, text in wrong_absence:
    print("\n%-46s TRUTH %s" % (slug, truth))
    print("  %s:%d   absence marker %s" % (rel, i, a))
    print("  | %s" % text[:185])

print()
print("=" * 72)
print("CLASS B -- current-state cells naming a DIFFERENT family: %d" % len(wrong_family))
print("=" * 72)
for slug, truth, rel, i, g, a, text in wrong_family:
    print("\n%-46s TRUTH %s  cell says %s" % (slug, truth, g))
    print("  %s:%d" % (rel, i))
    print("  | %s" % text[:185])

print()
print("CLASS C -- current-state cells already carrying the right family: %d" % len(ok))
for slug, truth, rel, i, g, a, text in ok:
    print("   %-44s %-12s %s:%d" % (slug, truth, rel, i))

affected = sorted({r[0] for r in wrong_absence + wrong_family})
print()
print("REPOS WITH >=1 WRONG CURRENT-STATE CELL: %d of %d" % (len(affected), len(RECOV)))
for s in affected:
    n = len([r for r in wrong_absence + wrong_family if r[0] == s])
    print("   %-46s %d cell(s)" % (s, n))
print()
print("QG limb 1 threshold : 1+ further stale cell at the next correction")
print("QG limb 1 observed  : %d  ->  %s"
      % (len(wrong_absence) + len(wrong_family),
         "FIRES" if (wrong_absence or wrong_family) else "does not fire"))
