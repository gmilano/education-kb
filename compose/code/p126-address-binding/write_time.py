#!/usr/bin/env python3
"""ACTION AM -- mark at WRITE time instead of sweeping afterwards.

p125 pre-registered: "a pass writing a retraction should emit the marker with
it. REFUTED if a write-time check cannot reproduce >= 90 % of the 81 rows
ACTION AF marked this pass."

A write-time check sees the line being written. A sweep sees the finished
page. So the clause is a question about CONTEXT, and p125's own module already
answers it structurally: `prose_hits` SKIPS every line beginning with `|`, so
a table row's correction is recognisable only through `table_hits`, which
needs the header above the row to say which column is the old value. A
line-local check cannot see that header.

Two scopes are measured against the same derived set, using p125's OWN
recognisers so the comparison is of context and not of vocabulary:

  LINE   `PROSE_UNMARKED` on the line alone (and nothing for a table row)
  BLOCK  the line plus the nearest table header above it, through the same
         per-row logic `table_hits` applies

The marked set is derived from git rather than asserted: a row is NEWLY
MARKED when its marker-stripped text carries the marker in p125 and appears
unmarked in p124. That derivation returns 81 SWEPT rows, reproducing p125's
own published count exactly, plus 8 rows written already marked.

Offline (reads two extracted trees, no git, no network). usage:
    write_time.py OLDTREE NEWTREE PAGE...
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p125-retraction-cue"))
import correction_form as cf                               # noqa: E402

MARKER = cf.MARKER
SEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")


def strip(line):
    return line.replace(MARKER, "")


def marked_set(path):
    with open(path, encoding="utf-8") as fh:
        return {strip(l).strip() for l in fh if MARKER in l}


def unmarked_set(path):
    with open(path, encoding="utf-8") as fh:
        return {l.strip() for l in fh if MARKER not in l}


def line_scope(line):
    """p125's PROSE_UNMARKED, on this line and nothing else."""
    if line.lstrip().startswith("|") or cf._is_quote(line):
        return None
    for form, pat in cf.PROSE_UNMARKED:
        for m in pat.finditer(line):
            if form == "3" and cf.REL_PRONOUN.search(
                    line[max(0, m.start() - 24):m.start() + 4]):
                continue
            return form
    return None


def header_above(lines, i):
    if not lines[i].lstrip().startswith("|"):
        return None
    j = i - 1
    while j >= 0 and lines[j].lstrip().startswith("|"):
        if SEP.match(lines[j]) and j >= 1:
            return cf.classify_header(lines[j - 1])
        j -= 1
    return None


def row_scope(line, hdr):
    """table_hits' per-row body, lifted to one row plus its header."""
    if hdr is None:
        return None
    cells = cf.split_row(line)
    olds, j = hdr
    if j >= len(cells):
        return None
    new_cell = cells[j]
    new_toks = {cf.norm_token(t) for t in cf.LICENCE.findall(new_cell)}
    new_absent = bool(cf.NO_GRANT.search(new_cell))
    for i in olds:
        if i >= len(cells):
            continue
        old_toks = cf.LICENCE.findall(cells[i])
        if not old_toks or MARKER in cells[i]:
            continue
        if not [t for t in old_toks if cf.norm_token(t) not in new_toks]:
            continue
        if new_toks:
            return "2"
        if new_absent:
            return "8"
    return None


def main(argv):
    old_tree, new_tree, pages = argv[0], argv[1], argv[2:]
    rows = []
    for page in pages:
        o, n = os.path.join(old_tree, page), os.path.join(new_tree, page)
        if not (os.path.exists(o) and os.path.exists(n)):
            continue
        was_marked, was_unmarked = marked_set(o), unmarked_set(o)
        with open(n, encoding="utf-8") as fh:
            lines = fh.readlines()
        for i, line in enumerate(lines):
            if MARKER not in line:
                continue
            key = strip(line).strip()
            if key in was_marked:
                continue
            rows.append((page, i + 1, strip(line), lines, i,
                         "swept" if key in was_unmarked else "written"))

    swept = [r for r in rows if r[5] == "swept"]
    print("# newly marked rows = %d  (swept=%d  written-new=%d)"
          % (len(rows), len(swept), len(rows) - len(swept)))

    for label, subset in (("all-89", rows), ("swept-81", swept)):
        ln_ok = bl_ok = 0
        tbl = 0
        misses = []
        for page, ln, bare, lines, i, _kind in subset:
            is_tbl = bare.lstrip().startswith("|")
            tbl += is_tbl
            a = line_scope(bare) is not None
            b = a or (row_scope(bare, header_above(lines, i)) is not None)
            ln_ok += a
            bl_ok += b
            if not b:
                misses.append((page, ln, bare.strip()[:110]))
        n = len(subset) or 1
        print("#")
        print("# [%s] table rows = %d of %d (%.0f %%)"
              % (label, tbl, len(subset), 100.0 * tbl / n))
        print("# [%s] LINE  scope reproduces %d of %d = %.1f %%  -> %s"
              % (label, ln_ok, len(subset), 100.0 * ln_ok / n,
                 "NOT REFUTED" if 100.0 * ln_ok / n >= 90 else "REFUTED"))
        print("# [%s] BLOCK scope reproduces %d of %d = %.1f %%  -> %s"
              % (label, bl_ok, len(subset), 100.0 * bl_ok / n,
                 "NOT REFUTED" if 100.0 * bl_ok / n >= 90 else "REFUTED"))
        if label == "swept-81":
            for page, ln, txt in misses[:12]:
                print("MISS\t%s:%d\t%s" % (page, ln, txt))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
