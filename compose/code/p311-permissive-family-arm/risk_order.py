#!/usr/bin/env python3
"""p311 — the fixture queue, ordered by what a wrong answer COSTS.

🔴 THE FINDING.  `family_coverage.py` prints its queue *"in descending cell
order"* and `ACTION p310-R` item 1 read that as a risk ranking: `MIT` and
`Apache-2.0` were *"the single highest-value hour available"* because they hold
`7 884` cells between them.  🟢 The hour was spent and the answer is **ZERO
defects across 9 classifiers**.

🔵 **Cell count is BLAST RADIUS, not risk**, and risk is `P(defect) × cost`.
Both terms point away from the top of that queue:

**`P(defect)`.**  A family's cell count is a measure of how much of this base was
written while looking at it.  `MIT` and `Apache-2.0` are the two families every
rung here was authored and hand-checked against; they were the implicit test
corpus all along.  🟡 This pass does NOT claim an inverse relationship from the
history — per FAMILY the rates are `2/4` above 1 000 cells against `4/6` below,
which at `n=10` is flat, and saying otherwise would be exactly the unbounded
claim `ACTION p310-R` item 3 asks this base to gate.  What the history DOES say
is narrower and enough: **every defect ever found here was found on a family
nobody had looked at recently**, and the two biggest were clean on first contact.

**`cost`.**  This is the term that is not flat, and it is not close.  A wrong
answer BETWEEN permissive families is a cosmetic imprecision — read `MIT` as
`Apache-2.0` and a studio ships either way.  A wrong answer that reports a
NONCOMMERCIAL grant as permissive ships a client into breach, and `p310` records
the direction: *"`p309`'s defect EXCLUDED usable supply; this one ADMITS unusable
supply into a client deliverable."*  🔴 **Every `DEFECT-COMMERCIAL` in this
base's history was on a noncommercial family, and the two noncommercial families
still without a payload sit at positions 7 and 12 of the 12-long queue.**

🟢 So the repair is not to re-sort by cost alone — cells are a real quantity and
`85 %` of them are now exercised, which was worth an hour.  It is that the queue
must print BOTH columns, because a single-axis queue gets read as a risk ranking
whatever its author intended.
"""
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, ".."))
P310 = os.path.join(CODE, "p310-family-coverage")

# 🔵 Consequence classes. A family is graded by WHAT A STUDIO LOSES if an
# instrument reports it as something more permissive than it is.
#
# 🔴 `CRITICAL` is reserved for grants a studio may NOT ship at all, because that
# is the only error no downstream review catches: the deliverable looks clean.
# 🔵 The copyleft grades are NOT about shipping — a studio can ship GPL — but
# about an obligation a client did not price (source disclosure, per-file or
# whole-work). `LOW` says the error is real and recoverable: attribution text.
CRITICAL = "CRITICAL  may not be shipped at all — a permissive answer is breach"
HIGH = "HIGH      whole-work source obligation a client did not price"
MEDIUM = "MEDIUM    file-level or weak-copyleft obligation"
LOW = "LOW       attribution or notice detail; ships either way"

CONSEQUENCE = {
    # noncommercial and reserved — the only class a studio cannot ship
    "CC-BY-NC-4.0": CRITICAL, "CC-BY-NC-SA-4.0": CRITICAL,
    "CC-BY-NC-ND-4.0": CRITICAL, "PolyForm-Noncommercial-1.0.0": CRITICAL,
    "proprietary": CRITICAL,
    # 🔴 p311: an UNBOUNDED subjective restriction is at least as bad as a named
    # noncommercial one — a studio cannot bound its obligations under
    # *«don't be a dick ... not limited to»*, and clause 1b prohibits resale.
    "DBAD-1.1": CRITICAL,
    # strong copyleft
    "AGPL-3.0": HIGH, "GPL-3.0": HIGH, "GPL-2.0": HIGH,
    # weak / file-level copyleft
    "LGPL-3.0": MEDIUM, "MPL-2.0": MEDIUM, "EPL-2.0": MEDIUM, "ECL-2.0": MEDIUM,
    # permissive
    "MIT": LOW, "Apache-2.0": LOW, "BSD-3-Clause": LOW, "BSD-2-Clause": LOW,
    "ISC": LOW, "0BSD": LOW, "Unlicense": LOW, "CC0-1.0": LOW,
    "CC-BY-4.0": LOW, "CC-BY-SA-4.0": LOW,
}
RANK = {CRITICAL: 0, HIGH: 1, MEDIUM: 2, LOW: 3}

# 🔵 The defect history, as DATA rather than as an argument. Each entry is
# (family, pass that ran the arm, defects it found). A family with no arm is
# absent — an unrun family has no rate, which is the whole point of the census.
HISTORY = [
    ("MIT", "p311", 0), ("Apache-2.0", "p311", 0),
    ("MPL-2.0", "p311", 0), ("GPL-2.0", "p311", 0),
    ("AGPL-3.0", "p309", 1), ("GPL-3.0", "p309", 1),
    ("CC-BY-SA-4.0", "p309", 0), ("proprietary", "p310", 0),
    ("CC-BY-4.0", "p310", 1), ("CC0-1.0", "p310", 1),
    ("CC-BY-NC-4.0", "p310", 1), ("PolyForm-Noncommercial-1.0.0", "p310", 1),
]


def _census():
    """p310's census, IMPORTED. The cell counts are derived from the shelves and
    this file does not keep a copy of them."""
    spec = importlib.util.spec_from_file_location(
        "p311_census", os.path.join(P310, "family_coverage.py"))
    mod = importlib.util.module_from_spec(spec)
    sink, sys.stdout = sys.stdout, io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.stdout = sink
    return mod


def queue(root):
    """[(family, cells, consequence, covered_by_or_None)] — every published family."""
    cen = _census()
    counts, _missing = cen.published(root)
    covered = cen.corpus_families()
    out = []
    for fam, cells in counts.items():
        out.append((fam, cells, CONSEQUENCE.get(fam, LOW),
                    covered.get(fam, (None, None))[0]))
    return out


def by_cells(rows):
    return sorted(rows, key=lambda r: -r[1])


def by_risk(rows):
    """Consequence first, cells as the tie-break within a consequence class."""
    return sorted(rows, key=lambda r: (RANK[r[2]], -r[1]))


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(CODE, "..", "..")
    rows = queue(os.path.normpath(root))
    total = sum(r[1] for r in rows)
    cov = [r for r in rows if r[3]]
    unc = [r for r in rows if not r[3]]
    cov_cells = sum(r[1] for r in cov)

    print("# p311 — the fixture queue on BOTH axes. `family_coverage.py` prints the")
    print("# left one; `ACTION p310-R` item 1 read it as the right one.")
    print("#")
    print("# coverage, the way p310 reported it .... %2d/%d FAMILIES = %3.0f%%"
          % (len(cov), len(rows), 100.0 * len(cov) / len(rows)))
    print("# coverage, weighted by CELLS ........... %5d/%d CELLS   = %3.0f%%"
          % (cov_cells, total, 100.0 * cov_cells / total))
    print("# 🔵 p310 published `36%` (8/22 families). By cells it was `24%`. One")
    print("#    family, `MIT`, is %.0f%% of every licence cell this base publishes, so"
          % (100.0 * dict((r[0], r[1]) for r in rows).get("MIT", 0) / total))
    print("#    a family-count average weights it equal to `CC-BY-NC-ND-4.0`'s 14.")
    print()

    print("# %-30s %6s  %s" % ("DESCENDING CELLS (the queue as printed)", "cells", "consequence"))
    for fam, cells, cons, by in by_cells(rows):
        mark = "🟢" if by else "🔴"
        print("  %s %-28s %6d  %s" % (mark, fam, cells, cons.split()[0]))
    print()

    print("# 🔴 UNCOVERED ONLY, re-ordered by WHAT A WRONG ANSWER COSTS:")
    print("# %-28s %6s  %s" % ("family", "cells", "consequence"))
    for fam, cells, cons, _by in by_risk(unc):
        print("  🔴 %-28s %6d  %s" % (fam, cells, cons))
    print()

    crit = [r for r in unc if r[2] == CRITICAL]
    cells_in_order = [r[0] for r in by_cells(unc)]
    if crit:
        print("# 🔴 %d UNCOVERED family(ies) a studio MAY NOT SHIP, holding %d cells:"
              % (len(crit), sum(r[1] for r in crit)))
        for fam, cells, _c, _b in by_risk(crit):
            print("#    %-24s %4d cells — position %d of %d in the descending-cell queue"
                  % (fam, cells, cells_in_order.index(fam) + 1, len(unc)))
        print("# 🔵 Every `DEFECT-COMMERCIAL` this base has found was on a")
        print("#    noncommercial family (p310: CC-BY-NC-4.0, PolyForm). These are the")
        print("#    two noncommercial families with no payload, and the cell axis puts")
        print("#    them last.")
    print()

    print("# 🟡 the defect history, as a MEASUREMENT with its n stated:")
    hi = [h for h in HISTORY if dict((r[0], r[1]) for r in rows).get(h[0], 0) >= 1000]
    lo = [h for h in HISTORY if dict((r[0], r[1]) for r in rows).get(h[0], 0) < 1000]
    cells_of = dict((r[0], r[1]) for r in rows)
    for label, grp in (("families >=1000 cells", hi), ("families  <1000 cells", lo)):
        d = sum(h[2] for h in grp)
        c = sum(cells_of.get(h[0], 0) for h in grp)
        print("#   %-22s n=%d  arms run=%d  defects=%d  cells=%5d  -> 1 defect per %s cells"
              % (label, len(grp), len(grp), d, c, ("%d" % (c // d)) if d else "—"))
    print("# 🔵 Per FAMILY the two rates are 2/4 and 4/6 — FLAT at n=10, and this")
    print("#    file does not claim otherwise. The asymmetry is in the COST column,")
    print("#    which is not a sample: it is a property of the grants themselves.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
