#!/usr/bin/env python3
"""ACTION AM, answered by a stricter question: are p125's marks reproducible?

AM asks whether a WRITE-TIME check can reproduce the 81 rows ACTION AF marked.
Before asking that, this module asks whether the SWEEP can -- whether p125's
own committed recognisers, run over p124's pages, propose the marks that
p125's commit contains.

For every row that is unmarked in p124 and marked in p125 (matched on
marker-stripped text, so a row that merely moved still matches), the p124 line
number is recovered and compared against what `mark_forms` -- p125's OWN
writer -- proposes on that same p124 page. A row in the commit but not in the
proposal set was marked by a path this repository does not contain.

Offline. usage: reproduce_marks.py OLDTREE NEWTREE PAGE...
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p125-retraction-cue"))
import correction_form as cf                               # noqa: E402
import mark_forms                                          # noqa: E402

MARKER = cf.MARKER


def strip(line):
    return line.replace(MARKER, "")


def main(argv):
    old_tree, new_tree, pages = argv[0], argv[1], argv[2:]
    tot_swept = tot_prop = tot_hit = 0
    per_page = []
    unreachable = []
    for page in pages:
        o, n = os.path.join(old_tree, page), os.path.join(new_tree, page)
        if not (os.path.exists(o) and os.path.exists(n)):
            continue
        with open(o, encoding="utf-8") as fh:
            old_lines = fh.readlines()
        with open(n, encoding="utf-8") as fh:
            new_lines = fh.readlines()

        was_marked = {strip(l).strip() for l in old_lines if MARKER in l}
        # marker-stripped text -> p124 line number (first occurrence)
        index = {}
        for ln, l in enumerate(old_lines, 1):
            if MARKER not in l:
                index.setdefault(l.strip(), ln)

        swept = {}
        for l in new_lines:
            if MARKER not in l:
                continue
            key = strip(l).strip()
            if key in was_marked or key not in index:
                continue
            swept[index[key]] = key

        # p125's ACTUAL writer is `mark_forms`, not `correction_form`: it
        # carries the APPARATUS guard and the cue model. Measuring against
        # `correction_form` overstates the proposal set by ~50 rows and was
        # the first thing this module got wrong.
        with open(o, encoding="utf-8") as fh:
            olines = fh.readlines()
        proposed = {ln for ln, l in enumerate(olines, 1)
                    if MARKER not in l and mark_forms.cue_hits(l)}
        proposed |= {h[0] for h in mark_forms.table_hits(o)}
        hit = set(swept) & proposed
        tot_swept += len(swept)
        tot_prop += len(proposed)
        tot_hit += len(hit)
        per_page.append((page, len(swept), len(proposed), len(hit)))
        for ln in sorted(set(swept) - proposed):
            unreachable.append((page, ln, swept[ln][:110]))

    print("# %-26s %6s %9s %8s" % ("page", "swept", "proposed", "matched"))
    for page, s, p, h in per_page:
        print("# %-26s %6d %9d %8d" % (page, s, p, h))
    print("# %-26s %6d %9d %8d" % ("TOTAL", tot_swept, tot_prop, tot_hit))
    n = tot_swept or 1
    print("#")
    print("# p125's committed recognisers reproduce %d of %d of its own "
          "marks = %.1f %%" % (tot_hit, tot_swept, 100.0 * tot_hit / n))
    print("# rows marked by a path not in this repository = %d"
          % (tot_swept - tot_hit))
    print("# clause (AM): refuted below 90 %%  ->  %s"
          % ("NOT REFUTED" if 100.0 * tot_hit / n >= 90 else "REFUTED"))
    print("#")
    for page, ln, txt in unreachable[:20]:
        print("UNREACHABLE\t%s:%d\t%s" % (page, ln, txt))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
