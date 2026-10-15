#!/usr/bin/env python3
"""Adjudicate the hits OUTSIDE p215's gate scope by the section they sit in.

`intel/open-gaps.md` and `README.md` are not pure current-state shelves: both carry pass-by-pass
history ("Registered for p212", "Verdicts on p211's open actions", dated pass sections). A hit
inside a dated section is a RECORD and must not be rewritten — the same rule p215 applied to the
two append-only shelves, where it left 93 dated mentions alone.

So the honest unit is: hits whose nearest preceding heading is NOT dated and NOT a
verdict/registration block. Those are live claims. Everything else is history, and is reported
separately rather than counted as a defect.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KB = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

DATED = re.compile(r"(20\d\d-\d\d-\d\d|Pass \d+|p\d{2,3}\b|Registered for|Verdicts on)", re.I)


def heading_for(lines, idx):
    for j in range(idx - 1, -1, -1):
        if lines[j].startswith("#"):
            return j + 1, lines[j].strip()
    return 0, "(no heading)"


def main(hits_path):
    want = []
    with open(hits_path) as fh:
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 5 and parts[0] in ("intel/open-gaps.md", "README.md") \
                    and parts[4].startswith("WRONG"):
                want.append((parts[0], int(parts[1]), parts[2], parts[3], parts[4]))

    cache = {}
    live, history = [], []
    for rel, no, slug, truth, verdict in want:
        if rel not in cache:
            with open(os.path.join(KB, rel), encoding="utf-8", errors="replace") as fh:
                cache[rel] = fh.read().splitlines()
        hno, head = heading_for(cache[rel], no)
        rec = (rel, no, slug, truth, verdict, hno, head[:120])
        (history if DATED.search(head) else live).append(rec)

    print(f"hits examined: {len(want)}")
    print(f"  in a DATED / registration / verdict section (a RECORD): {len(history)}")
    print(f"  in a LIVE section (a current claim):                    {len(live)}")
    print("\n--- LIVE claims contradicted by p215's own readings ---")
    print("file\tline\tslug\ttruth\tverdict\theading_line\theading")
    for r in live:
        print("\t".join(str(x) for x in r))
    print("\n--- records, left alone ---")
    for r in history:
        print("\t".join(str(x) for x in r))


if __name__ == "__main__":
    main(sys.argv[1])
