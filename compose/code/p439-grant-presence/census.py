#!/usr/bin/env python3
"""p439 — the live corpus measured against `Gap 439-A`.  ALWAYS EXITS 0.

🔵 This is a MEASUREMENT target and the exit code is the point.  `Gap 435-A` found a gate
firing on 59.1 % of its population and called it a classifier rather than a detector;
`Gap 438-B` found a gate that goes red when its population drops to zero, because it
asserts a property of the HARVEST and not of the code.  Both prescribed the same remedy:
a population question belongs in a target that measures and never fails.  So the counts
here can move with every harvest without ever blocking a commit, and the CONTROLS that
can go red live in `test_grant_presence.py` against committed fixtures.

🔴 The blind spot this quantifies: `bespoke_census.is_stock()` asks three questions — the
title names a family, no effective restriction fires, the family is one `p257` grades —
and NONE of the three asks whether the granting words are present.  So a payload that is
a POINTER to its licence grades identically to the licence.

Usage: census.py [--root DIR]
"""
import argparse
import collections
import glob
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "p341-bespoke-instrument-census"))
import bespoke_census as bc  # noqa: E402
import grant_presence as gp  # noqa: E402

# A registry-metadata file states a licence as a FIELD (`"license": "MIT"`) and is not a
# payload, so "the grant is not here" is true of it and not interesting.  Counted apart
# rather than dropped — `p275`'s rule is that a count keeps its population.
META_SUFFIXES = (".json", ".tsv")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    a = ap.parse_args(argv)
    root = pathlib.Path(a.root).resolve()

    rows = []
    for p in glob.glob(str(root / "compose/code/**/fixtures/**"), recursive=True):
        pp = pathlib.Path(p)
        if not pp.is_file():
            continue
        try:
            t = pp.read_text(errors="replace")
        except Exception:
            continue
        if len(t) < 40:
            continue
        g = bc.grade(t)
        fam = g["titled_family"]
        if fam is None:
            continue
        r = gp.classify(t, fam)
        rows.append((pp.name, fam, r["verdict"], g["stock"], g["needs_a_human"],
                     r["bytes"], pp.suffix.lower() in META_SUFFIXES))

    counts = collections.Counter(r[2] for r in rows)
    absent = [r for r in rows if r[2] in ("GRANT-BY-REFERENCE", "GRANT-TRUNCATED")]
    payloads = [r for r in absent if not r[6]]
    meta = [r for r in absent if r[6]]
    blind = [r for r in payloads if r[3] and not r[4]]

    print("cifra\tvalue")
    print("titled_payloads_graded\t%d" % len(rows))
    for k in ("GRANT-PRESENT", "GRANT-TRUNCATED", "GRANT-BY-REFERENCE",
              "GRANT-UNCALIBRATED"):
        print("%s\t%d" % (k.lower().replace("-", "_"), counts.get(k, 0)))
    print("grant_absent_licence_payloads\t%d" % len(payloads))
    print("grant_absent_registry_metadata\t%d" % len(meta))
    print("#\tblind_spot_stock_yes_human_no\t%d" % len(blind))
    print("#\tGap 439-A: the rows above grade stock=True and needs_a_human=False while "
          "carrying no granting words.  A MEASUREMENT, not a gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
