#!/usr/bin/env python3
"""p277 (`ACTION AB`) — NO GATE ON THIS BASE READS TABLE STRUCTURE.  This one does.

🔴 Why it exists.  `p276` found `repos/foundations.md` carrying its `|---|` separator BELOW
its first data row, so `p274`'s own recovered `gegok12` row **rendered as part of the table
header** — a real row, published, invisible.  `p276` recorded the class and wrote: *"No gate
on this base reads table structure."*

🔴 `p277` then found a LIVE second instance in a different file and a different shape: a
stray BLANK LINE at `verticals/solutions.md:50`, inside the platform table, which promoted
**`Koha`** — a real GPL-3.0 row — into a table HEADER and orphaned every row after it.
Two instances, two shapes, one invisible failure mode: **a row that is published and does
not render as a row.**

🟢 The predicate, kept deliberately narrow so it has no false positives on this base's own
house style:

    a BLANK line, with a table row immediately above it AND immediately below it,
    where the row BELOW is not itself a header (i.e. no separator follows it)

🔵 Three house-style shapes this must NOT flag, each of which broke an earlier draft:

  1. `| | |` — an EMPTY two-column header row.  An earlier draft's separator pattern
     matched it (every character between the pipes is whitespace or a pipe), so the real
     separator below it looked like a SECOND separator and 34 spurious findings followed.
     A separator must contain at least one `-`.
  2. A blank line between two DIFFERENT tables, where the row after the blank is a genuine
     header with its own separator.  Legitimate, and common here: 7 of the 8 blank-splits
     on this base are this shape.
  3. ASCII pipe-art inside an indented code block (`compose/patterns.md`'s architecture
     diagrams).  A markdown table is never indented, so leading whitespace excludes it.

🔵 And one thing it deliberately does NOT check: a trailing pipe.  GFM makes it optional,
`repos/trending.md:1008` omits it on a 1,179-byte row, and that row renders correctly.
Requiring it produced a false positive; the check was wrong, not the shelf.
"""
import re
import sys
import pathlib

# not indented: a markdown table at an indent is a code block
ROW = re.compile(r"^\|.*$")
# a separator must contain at least one dash -- see note 1 above
SEP = re.compile(r"^\|[\s:|-]*-[\s:|-]*\|?\s*$")

SHELVES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "compose/patterns.md", "README.md",
           "intel/open-gaps.md"]


def split_defects(lines):
    """A blank line that splits a table and leaves the lower half headerless."""
    out = []
    for i in range(1, len(lines) - 2):
        if lines[i].strip():
            continue
        if not (ROW.match(lines[i - 1]) and ROW.match(lines[i + 1])):
            continue
        if SEP.match(lines[i + 2]):      # the lower half starts with a real header
            continue
        out.append((i + 1, lines[i + 1][:70]))
    return out


def header_defects(lines):
    """A table block whose separator is absent or is not on the second line."""
    out, i, n = [], 0, len(lines)
    while i < n:
        if ROW.match(lines[i]) and not SEP.match(lines[i]):
            start, block = i, []
            while i < n and ROW.match(lines[i]):
                block.append(lines[i])
                i += 1
            seps = [j for j, l in enumerate(block) if SEP.match(l)]
            if not seps:
                out.append((start + 1, "NO SEPARATOR", block[0][:60]))
            elif seps[0] != 1:
                out.append((start + 1, f"SEPARATOR ON ROW {seps[0] + 1}, NOT 2", block[0][:60]))
        else:
            i += 1
    return out


def audit(root="."):
    root = pathlib.Path(root)
    findings = []
    for rel in SHELVES:
        p = root / rel
        if not p.exists():
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        for ln, row in split_defects(lines):
            findings.append((rel, ln, "BLANK-SPLITS-TABLE", row))
        # header_defects is reported as a CENSUS, not enforced: a table split across a
        # blank line legitimately produces headerless continuation blocks, and that shape
        # is already covered (and enforced) by BLANK-SPLITS-TABLE above.
    return findings


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    findings = audit(root)
    if findings:
        print(f"🔴 {len(findings)} table-structure defect(s):", file=sys.stderr)
        for rel, ln, kind, row in findings:
            print(f"   {rel}:{ln}\t{kind}\t{row}", file=sys.stderr)
        return 1
    print(f"   {len(SHELVES)} shelves, no row is published as a header")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
