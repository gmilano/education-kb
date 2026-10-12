"""p150-grant-ladder-order — ACTION FE: run both ladder arms over the test set.

Usage:
    python3 run_ladder_order.py <corpus_dir> <npmtrees_dir> > result.tsv

Prints one row per subject: the grant under p147's inverted ladder (control) and under
the corrected FILE > PKG_ONLY > README_ONLY ladder, and whether the class moves.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ladder_order as L  # noqa: E402

COLS = ["subject", "tier", "p147_grant", "p147_licence", "fixed_grant", "fixed_licence",
        "evidence", "moved"]


def rows(root, tier):
    if not os.path.isdir(root):
        return
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if not os.path.isdir(path):
            continue
        ctl = L.census_p147_order(path, name, L.EXTENDED_README, allow_informal=True)
        fix = L.census(path, name, L.EXTENDED_README, allow_informal=True)
        moved = "MOVED" if ctl["grant"] != fix["grant"] else "-"
        yield dict(subject=name, tier=tier,
                   p147_grant=ctl["grant"], p147_licence=ctl["licence"],
                   fixed_grant=fix["grant"], fixed_licence=fix["licence"],
                   evidence="%s|%s" % (ctl["evidence"], fix["evidence"]), moved=moved)


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    out = []
    out += list(rows(argv[1], "clone"))
    out += list(rows(argv[2], "npm"))
    print("\t".join(COLS))
    for r in out:
        print("\t".join(str(r[c]) for c in COLS))
    moved = [r for r in out if r["moved"] == "MOVED"]
    sys.stderr.write("subjects=%d moved=%d\n" % (len(out), len(moved)))
    for r in moved:
        sys.stderr.write("  MOVED %-45s %s/%s -> %s/%s\n" % (
            r["subject"], r["p147_grant"], r["p147_licence"],
            r["fixed_grant"], r["fixed_licence"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
