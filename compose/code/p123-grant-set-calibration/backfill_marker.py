#!/usr/bin/env python3
"""ACTION V — back-fill a machine-readable marker on every REPAIRED row.

THE PROBLEM THIS RETIRES. p121's correction guard recognised a repaired row
by its VOCABULARY: it matched phrases like "was", "corrected", "previously".
A guard built from vocabulary has to be taught every new phrase a human
writes, and p121 recorded it mis-firing on ordinary prose and on this KB's
own table headers. A marker the writer emits is read by exact match and
needs no vocabulary at all.

WHAT COUNTS AS A ROW, AND WHY IT MATTERS. p122 measured "57 rows need the
marker; 1 exists". Both figures are wrong, and p123 measured them again
rather than inheriting them:

  * 57 counted every line containing the inline `was` marker, including SIX
    lines of PROSE DISCUSSING the marker ("Its correction tables on two pages
    read ..."). Prose about a repaired row is not a repaired row. The real
    population is 51 TABLE rows.
  * "1 exists" counted a `<!--corrected-->` occurrence that is part of the
    ACTION V CLAUSE TEXT, not a marker on a row. Zero rows carry it.

So a row is a line that STARTS with `|` and carries the inline marker. The
marker is inserted INSIDE the cell, directly after the `was ...` span it
documents, because a row can in principle carry more than one correction and
because trailing content after a row's final `|` becomes a phantom cell.

Idempotent: a span already followed by the marker is left alone.

usage: backfill_marker.py [--apply] FILE...
       default is a dry run; --apply rewrites in place.
"""
import re
import sys

# The inline marker as this KB writes it: ⚠️ **was <token>**
SPAN = re.compile(r"(⚠️ \*\*was [^*]*\*\*)(?!<!--corrected-->)")
MARKER = "<!--corrected-->"


def fix_line(line):
    if not line.startswith("|") or "⚠️ **was" not in line:
        return line, 0
    new, n = SPAN.subn(r"\1" + MARKER, line)
    return new, n


def main(argv):
    apply_ = "--apply" in argv
    files = [a for a in argv if a != "--apply"]
    total, touched = 0, 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        out, n_file = [], 0
        for line in lines:
            new, n = fix_line(line)
            out.append(new)
            n_file += n
        if n_file:
            touched += 1
            total += n_file
            print(f"{path}\t{n_file}")
            if apply_:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.writelines(out)
    print(f"# rows marked={total} files={touched} applied={apply_}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
