#!/usr/bin/env python3
"""p436 — the generalisation of Gap 435-B from ADDRESSES to FINDING IDS.

Gap 435-B found an address dropped by a full-file rewrite while the claim that
rested on it survived.  `gate-dead-citation` (p372) catches a dead ADDRESS.
Nothing on this tree catches a dead FINDING ID: the gap register cites `P527`
and `P533` and no live shelf defines either, because the same rewrite deleted
the rows that did.

DENOMINATOR, and it was wrong on the first build.  The curated shelves carry
almost no P-notation at all (`agents/top.md` 3, `repos/foundations.md` 0), so
grading the register against THEM reported 462 dead citations -- an artefact of
the wrong denominator, not a finding.  The definition channel is the pair of
APPEND-ONLY trend shelves, which by protocol never lose content (and p436
measured 0 drops from them).  A register citation absent from both of those is a
dead citation: the register pointing at evidence the corpus no longer holds.
"""
import os
import re
import sys

PID = re.compile(r"\bP(\d{1,4})\b")
# The definition channel: append-only, so a missing ID here was never written.
DEFINERS = ["agents/trending.md", "repos/trending.md",
            "agents/top.md", "intel/trends.md"]
CITERS = ["intel/open-gaps.md"]


def ids_in(path):
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8", errors="replace") as fh:
        return {"P" + m for m in PID.findall(fh.read())}


def main(argv):
    if len(argv) != 1:
        sys.stderr.write("usage: finding_citations.py REPO_ROOT\n")
        return 2
    root = argv[0]
    if not os.path.isdir(root):
        sys.stderr.write("finding_citations.py: not a directory: %s\n" % root)
        return 2

    defined = set()
    for rel in DEFINERS:
        defined |= ids_in(os.path.join(root, rel))
    # A denominator this small means the definition channel was not read; that is
    # the error this instrument made on its first build, so it refuses instead.
    if len(defined) < 100:
        sys.stderr.write(
            "finding_citations.py: only %d finding IDs in the definition channel "
            "-- denominator looks wrong, refusing to grade\n" % len(defined))
        return 2

    print("citer\tfinding_id\tstatus")
    dead_total = 0
    for rel in CITERS:
        cited = ids_in(os.path.join(root, rel))
        dead = sorted(cited - defined, key=lambda p: int(p[1:]))
        for p in dead:
            print("%s\t%s\tDEAD-NO-LIVE-DEFINITION" % (rel, p))
        sys.stderr.write("%s: cited=%d dead=%d\n" % (rel, len(cited), len(dead)))
        dead_total += len(dead)
    sys.stderr.write("defined on live shelves=%d  dead citations=%d\n"
                     % (len(defined), dead_total))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
