"""p143-edunext-jurisdiction -- `ACTION DJ`, and the test the pre-registration did not ask for.

`ACTION DJ` registered: establish eduNEXT's jurisdiction from commit offsets across its
own repositories. 🔴 **Falsifier: refuted if the offsets are not predominantly `-0500`**,
which would mean the `.co` reading is wrong and the row must stay unplaced.

`-0500` IS predominant -- in 5 of 5 repositories. 🔵 **And that is not enough, for a
reason visible in the same data.**

`-0500` is Colombia (COT) and it is also US Eastern Standard Time. 🟢 **The two are
distinguishable, because Colombia does not observe daylight saving and the United States
does.** A Colombian committer is `-0500` in January and `-0500` in July. A US Eastern
committer is `-0500` in January and `-0400` in July.

So the question is not "is `-0500` dominant" but 🔴 **"does the `-0400` population sit in
the DST window?"**

  * If `-0400` commits cluster in Mar-Nov and `-0500` in Nov-Mar, the author population
    is DST-OBSERVING and `-0500` is US Eastern, not Bogota.
  * If `-0400` and `-0500` are mixed through every month, there are two populations and
    the `-0500` one may well be Colombian.

🔵 **This is `T32`'s rule applied before publishing rather than after**: ask the
instrument what shape its answer has, not only which bucket is biggest.

US DST, 2007-present: second Sunday in March to first Sunday in November. This probe
uses whole months (Apr-Oct strictly inside, Jan-Feb + Dec strictly outside) and reports
the boundary months Mar and Nov separately rather than forcing them.

Run: python3 -I dstsplit.py name=path [name=path ...]
"""

import os
import subprocess
import sys

DST_IN = {4, 5, 6, 7, 8, 9, 10}      # strictly inside US DST
DST_OUT = {1, 2, 12}                  # strictly outside US DST
BOUNDARY = {3, 11}                    # transition months, reported, never forced


def commits(repo):
    out = subprocess.run(
        ["git", "-C", repo, "log", "--format=%ad", "--date=format:%m %z"],
        capture_output=True, text=True, timeout=300).stdout
    for line in out.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit():
            yield int(parts[0]), parts[1]


COLS = ["subject", "total", "n_0500", "n_0400", "0400_in_dst", "0400_out_dst",
        "0500_in_dst", "0500_out_dst", "verdict"]


def main(argv):
    print("\t".join(COLS))
    agg = {"total": 0, "n5": 0, "n4": 0, "f4i": 0, "f4o": 0, "f5i": 0, "f5o": 0,
           "b4": 0, "b5": 0}
    for spec in argv:
        name, path = spec.split("=", 1)
        if not os.path.isdir(path):
            continue
        n5 = n4 = f4i = f4o = f5i = f5o = b4 = b5 = total = 0
        for mon, off in commits(path):
            total += 1
            if off == "-0500":
                n5 += 1
                if mon in DST_IN:
                    f5i += 1
                elif mon in DST_OUT:
                    f5o += 1
                else:
                    b5 += 1
            elif off == "-0400":
                n4 += 1
                if mon in DST_IN:
                    f4i += 1
                elif mon in DST_OUT:
                    f4o += 1
                else:
                    b4 += 1
        # A DST-observing population puts ~all -0400 inside the window and
        # ~all -0500 outside it.
        if n4 and f4o == 0 and f5i == 0:
            v = "DST_OBSERVING_CLEAN"
        elif n4 and f4o <= max(1, n4 // 20) and f5i <= max(1, n5 // 20):
            v = "DST_OBSERVING"
        elif n4 == 0:
            v = "NO_DST_SIGNAL (no -0400 at all)"
        else:
            v = "MIXED — both offsets in both windows"
        print("\t".join(str(x) for x in
                        [name, total, n5, n4, f4i, f4o, f5i, f5o, v]))
        agg["total"] += total
        agg["n5"] += n5
        agg["n4"] += n4
        agg["f4i"] += f4i
        agg["f4o"] += f4o
        agg["f5i"] += f5i
        agg["f5o"] += f5o
        agg["b4"] += b4
        agg["b5"] += b5

    print("\n# POOLED across all subjects", file=sys.stderr)
    print("# commits total              : %d" % agg["total"], file=sys.stderr)
    print("# -0500                      : %d" % agg["n5"], file=sys.stderr)
    print("# -0400                      : %d" % agg["n4"], file=sys.stderr)
    print("#", file=sys.stderr)
    print("# -0400 inside DST (Apr-Oct) : %d" % agg["f4i"], file=sys.stderr)
    print("# -0400 outside  (Jan,Feb,Dec): %d" % agg["f4o"], file=sys.stderr)
    print("# -0400 boundary (Mar,Nov)   : %d" % agg["b4"], file=sys.stderr)
    print("# -0500 inside DST (Apr-Oct) : %d" % agg["f5i"], file=sys.stderr)
    print("# -0500 outside  (Jan,Feb,Dec): %d" % agg["f5o"], file=sys.stderr)
    print("# -0500 boundary (Mar,Nov)   : %d" % agg["b5"], file=sys.stderr)
    print("#", file=sys.stderr)
    if agg["n4"]:
        pct_in = 100.0 * agg["f4i"] / max(1, agg["f4i"] + agg["f4o"])
        print("# -0400 that falls INSIDE the DST window: %.1f%%" % pct_in,
              file=sys.stderr)
        print("# 🔴 A Colombian population cannot produce -0400 at all; Colombia has "
              "observed no DST since 1993.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
