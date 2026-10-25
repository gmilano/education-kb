#!/usr/bin/env python3
"""p436 — the over-accusation audit on claims.py's HEADER rule.

P543's lesson: a one-line remedy that over-accuses (49 -> 23) is worse than no
instrument.  claims.py's HEADER notation licenses "the block that follows the
header" as promoted.  The false-positive mechanism is a block that also lists
DECLINED addresses without opening a new markdown header.  This prints every
HEADER claim site with its header text, the slug count it captured, and whether
the captured block carries a decline marker -- so the rule is graded by hand
rather than trusted.
"""
import re
import sys

HEADER = re.compile(r"^#{2,4}\s")
PROMOTED = re.compile(r"\bPromoted\b", re.IGNORECASE)
DECLINE = re.compile(
    r"Declin|Refus|no grant|NO-GRANT|no licence|no license|rejected|not shelved|Deferred",
    re.IGNORECASE)
SLUG = re.compile(r"`([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?/[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)`")


def main(argv):
    if not argv:
        sys.stderr.write("usage: audit_blocks.py FILE [FILE...]\n")
        return 2
    print("file\tline\tslugs_captured\tdecline_marker_in_block\theader")
    flagged = 0
    total = 0
    for path in argv:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
        for i, line in enumerate(lines):
            s = line.strip()
            if not (HEADER.match(s) and PROMOTED.search(s)):
                continue
            if SLUG.findall(s):
                continue  # slug on the header itself; block rule not used
            block = []
            for j in range(i + 1, min(i + 60, len(lines))):
                if HEADER.match(lines[j].strip()):
                    break
                block.append(lines[j])
            btext = "\n".join(block)
            n = len(set(SLUG.findall(btext)))
            marker = "YES" if DECLINE.search(btext) else "no"
            total += 1
            if marker == "YES":
                flagged += 1
            print("\t".join([path, str(i + 1), str(n), marker, s[:120]]))
    sys.stderr.write("HEADER block-rule sites=%d  with decline marker inside block=%d\n"
                     % (total, flagged))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
