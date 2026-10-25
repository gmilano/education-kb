#!/usr/bin/env python3
"""p442 — NO SELL SHELF MAY PUBLISH A PAYLOAD CELL NOBODY HAS RE-MEASURED.

## What this gate is for

A payload cell on this base reads `<path>` <bytes> B · `<sha256₁₂>`, and it is the only part
of a shelf row a reader can check.  `p442` re-measured all 162 of them against the file AND
against `printf '%s' "$(cat f)"`:

    🟢 143  REPRODUCES        bytes and digest are the file's
    🔴  19  CAPTURE-MEASURED  bytes short by the trailing-newline run, digest of the
                              STRIPPED bytes -- `P834`, in the published cell

🔴 All 19 came from three recent passes — `p432` (5 of its 5 rows), `p433` (2 of 5) and
`p438` (2 of 11) — so the defect was not even consistent WITHIN a pass: the same pass
measured some rows through `lib/payload_measure.sh` and typed others by hand.  A reader
cannot tell those apart by looking, which is exactly why this is a gate and not a remark.

## The ratchet

The gate is OFFLINE: it joins the cells the shelves publish against the recorded sweep in
`evidence/`.  A cell that is not in the record has never been re-measured, and that is a
RED — the same shape as `gate-register-currency`.  To clear it, re-run

    compose/code/p442-shelf-tree-crosscheck/sweep_published.sh <cells.tsv> > <record>

which measures through the library (`sha12_of_file`, `size_of_file`) and types any
non-reproducing cell with the capture control (`sha12_of_capture_BROKEN`).  🔵 A pass that
publishes a new payload row therefore has two ways to stay green and both are correct ones:
build the cell with `lib/measure --cell`, and extend the record.

## Declared scope

Only the three SELL shelves are read -- `agents/top.md`, `repos/foundations.md`,
`verticals/solutions.md`.  `agents/trending.md` and `repos/trending.md` are APPEND-ONLY
history: their cells were true when written and are not re-measurable at today's HEAD, so
charging them here would make the gate permanently red for a reason that is not a defect.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_published_cells import rows as published_cells  # noqa: E402  (one parser, not two)

SHELVES = ("agents/top.md", "repos/foundations.md", "verticals/solutions.md")
RECORD = "evidence/published-cell-reproduction.2026-10-25-p442.tsv"
GREEN = "REPRODUCES"


def load_record(path):
    """(slug, pub_path, bytes, sha12) -> verdict.  The key is the PUBLISHED spelling, so a
    branch-qualified cell (`master/LICENSE`) is keyed as the shelf writes it; the sweep
    carries the resolved path in its own column for the reader."""
    rec = {}
    with open(path, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        need = ("slug", "pub_path", "pub_bytes", "pub_sha12", "verdict")
        missing = [c for c in need if c not in head]
        if missing:
            sys.stderr.write("🔴 p442: record is missing column(s) %s\n" % ",".join(missing))
            return None
        ix = {c: head.index(c) for c in need}
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < len(head):
                continue
            key = (f[ix["slug"]], f[ix["pub_path"]], f[ix["pub_bytes"]], f[ix["pub_sha12"]])
            rec[key] = f[ix["verdict"]]
    return rec


def main():
    root = "."
    argv = sys.argv[1:]
    if argv and argv[0] == "--root":
        root = argv[1] if len(argv) > 1 else "."
        argv = argv[2:]
    record_path = os.path.join(root, RECORD)
    if argv:
        record_path = argv[0]
    if not os.path.exists(record_path):
        sys.stderr.write("🔴 p442: no reproduction record at %s — a published cell with no "
                         "record is CELL-UNMEASURED, and so is all of them (P355)\n"
                         % record_path)
        return 2
    rec = load_record(record_path)
    if rec is None:
        return 2
    cells = []
    for shelf in SHELVES:
        p = os.path.join(root, shelf)
        if not os.path.exists(p):
            sys.stderr.write("🔴 p442: sell shelf absent: %s\n" % shelf)
            return 2
        cells.extend(list(published_cells(p)))
    if not cells:
        sys.stderr.write("🔴 p442: zero published cells parsed — a parse fault, not a clean "
                         "shelf (P355)\n")
        return 2
    if not rec:
        sys.stderr.write("🔴 p442: the record is empty while %d cells are published\n"
                         % len(cells))
        return 2
    red = []
    green = 0
    for shelf, line, slug, path, nbytes, sha, _head in cells:
        verdict = rec.get((slug, path, nbytes, sha))
        if verdict == GREEN:
            green += 1
        elif verdict is None:
            red.append((shelf, line, slug, path, "CELL-UNMEASURED"))
        else:
            red.append((shelf, line, slug, path, verdict))
    print("# p442 cell-reproduction gate — %d published cells, %d green, %d red"
          % (len(cells), green, len(red)))
    for shelf, line, slug, path, why in red:
        print("🔴 %s:%d\t%s\t%s\t%s" % (shelf, line, slug, path, why))
    if red:
        print("🔴 FAIL — a published payload cell must be re-measured through "
              "`lib/payload_measure.sh`; see this gate's docstring for the one command.")
        return 1
    print("🟢 PASS — every published payload cell reproduces from the file it names.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
