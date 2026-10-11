#!/usr/bin/env python3
"""ACTION W — score a census against rows known to be CORRECT.

THE RULE p122 EARNED. p122 built its prose census three times; each build
flagged defects and verification destroyed almost all of them (25->7, 11->1,
59->3, a false-positive rate reaching 95 %). The lesson it wrote down:

    a census may not publish a defect rate until it has been scored against
    rows known to be CORRECT. An instrument never shown a correct row it
    mishandles has not been calibrated, and its rate is a property of the
    instrument, not of the KB.

HOW THE GOLD LABEL AVOIDS CIRCULARITY. The gold label does not come from the
instrument under test, and it does not come from prose. A claim is GOLD-CORRECT
when the live tree grants that licence in SOME grant file -- established by
reading EVERY grant file (ACTION Z) on the repository's REAL default branch
(ACTION Y). The model under test then reads only PART of that same evidence.
So the calibration measures exactly one thing: what the narrower model loses.

The gold set is deliberately restricted to the rows where the two models can
disagree at all -- addresses carrying MORE THAN ONE grant file, or a single
file that is itself a split grant. On a repository with one plain LICENSE both
models read the same byte and agree trivially; including those rows would pad
the denominator and flatter the narrower model.

TWO NARROWER MODELS ARE SCORED, because this KB ran both:
  ONE-TOKEN  the p114-p122 model: probe a fixed path priority, stop at the
             first file that returns 200, compare that single token.
  MAIN-ONLY  the pre-p122 branch guess: look only on main, then master.

usage: calibrate.py CLAIMS_TSV GRANTS_TSV HEADS_TSV
"""
import sys
from collections import defaultdict

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from join_grant_set import grant_tokens, norm  # noqa: E402

# The path priority of scan_licences.sh (p122), in its exact order.
ONE_TOKEN_ORDER = [
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md",
    "COPYING", "COPYING.txt", "LICENSE.rst", "LICENSE-MIT", "license.txt",
]


def one_token(rows):
    """What the p114-p122 census would have read: first match wins."""
    have = {p: t for p, t in rows}
    for p in ONE_TOKEN_ORDER:
        if p in have:
            return have[p]
    return None


def main(claims_p, grants_p, heads_p):
    gset = defaultdict(list)
    for row in open(grants_p, encoding="utf-8"):
        parts = row.rstrip("\n").split("\t")
        if len(parts) == 5 and parts[4] != "NO-FILE":
            gset[parts[0].lower()].append((parts[2], parts[4]))

    branch = {}
    for row in open(heads_p, encoding="utf-8"):
        parts = row.rstrip("\n").split("\t")
        if len(parts) == 3:
            branch[parts[0].lower()] = parts[2]

    # ---- the gold set -----------------------------------------------------
    gold = []
    seen = set()
    for row in open(claims_p, encoding="utf-8"):
        parts = row.rstrip("\n").split("\t", 5)
        if len(parts) != 6:
            continue
        _page, _line, addr, claim, _d, _ctx = parts
        a = addr.lower()
        rows = gset.get(a)
        if not rows:
            continue
        # can the two models even disagree here?
        multi = len(rows) > 1 or any(t.startswith("SPLIT") for _p, t in rows)
        if not multi:
            continue
        if norm(claim) not in grant_tokens(rows):
            continue  # not gold-correct; it is a candidate defect, not a control
        key = (a, norm(claim))
        if key in seen:
            continue
        seen.add(key)
        gold.append((a, claim, rows))

    if not gold:
        print("gold set is EMPTY -- calibration cannot be reported", file=sys.stderr)
        return 1

    # ---- score the narrower models ---------------------------------------
    fp_one, fp_main = [], []
    for a, claim, rows in gold:
        ot = one_token(rows)
        if ot is None or norm(claim) != norm(ot.replace("SPLIT:", "")):
            fp_one.append((a, claim, ot, rows))
        br = branch.get(a, "-")
        if br not in ("main", "master"):
            fp_main.append((a, claim, br, rows))

    n = len(gold)
    print(f"gold-correct rows (models can disagree)\t{n}")
    print(f"ONE-TOKEN false positives\t{len(fp_one)}\t{100.0*len(fp_one)/n:.1f} %")
    print(f"MAIN-ONLY false positives\t{len(fp_main)}\t{100.0*len(fp_main)/n:.1f} %")
    print(f"GRANT-SET false positives\t0\t0.0 %\t(gold label is by construction in the set)")
    print()
    print("# ONE-TOKEN would have flagged these CORRECT rows:")
    for a, claim, ot, rows in fp_one:
        files = " ".join(f"{p}={t}" for p, t in sorted(rows))
        print(f"  {a}\tpage says {claim}\tone-token read {ot}\t[{files}]")
    if fp_main:
        print("# MAIN-ONLY would have read NO-FILE on these CORRECT rows:")
        for a, claim, br, rows in fp_main:
            print(f"  {a}\tpage says {claim}\tdefault branch is {br}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
