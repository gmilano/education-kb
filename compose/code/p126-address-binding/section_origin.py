#!/usr/bin/env python3
"""P126-B: where do the violations that p125 did not report come from?

p125 committed 36 residual violations. Recomputed on the committed pages the
same assertion returns 49. The 13-record difference is not drift: a pass
measures the pages, then PREPENDS its own section to them, and that section
is prose about licences and addresses -- so it can itself violate the
assertion the pass has just discharged.

This script attributes every fresh violation to the pass section it falls in,
using each page's own `**Pass NNN,` datelines as the section boundaries.

Offline. usage: section_origin.py PAGE...
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "p125-retraction-cue"))
import repair_search                                       # noqa: E402

DATELINE = re.compile(r"^\*\*Pass (\d+),")


def sections(path):
    """-> [(first_line, last_line, 'pNNN')], newest first; [] if unheaded."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    marks = [(ln, m.group(1)) for ln, line in enumerate(lines, 1)
             for m in [DATELINE.match(line)] if m]
    out = []
    for i, (ln, tag) in enumerate(marks):
        end = marks[i + 1][0] - 1 if i + 1 < len(marks) else len(lines)
        out.append((ln, end, "p" + tag))
    return out


def attribute(path, ln):
    for first, last, tag in sections(path):
        if first <= ln <= last:
            return tag
    return "(unsectioned)"


def main(pages):
    pairs = repair_search.repaired_pairs(pages)
    vs = repair_search.violations(pages, pairs)
    tally = {}
    for path, ln, addr, tok, _ in vs:
        tag = attribute(path, ln)
        tally[tag] = tally.get(tag, 0) + 1
        print("%s\t%s:%d\t%s\t%s" % (tag, path, ln, addr, tok))
    print("#")
    for tag in sorted(tally, key=lambda t: -tally[t]):
        print("# %-14s %d" % (tag, tally[tag]))
    print("# total %d" % len(vs))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
