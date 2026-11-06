#!/usr/bin/env python3
"""p672 — a WORKING gate for the defect the curation brief names first:
"NEVER leave a header or example row as data."

WHY THE OBVIOUS GATE DOES NOT WORK (672-E)
  The natural implementation is "flag any row whose first cell is a field name
  (Name/Nombre/Repo/Licencia) and that is not followed by a separator". Run over
  this KB it reports 80 hits across three pages and EVERY ONE IS A FALSE
  POSITIVE, because these pages make heavy use of TRANSPOSED key-value tables:

      | Licence payload | MIT, 1,073 B |
      | Description     | identical string |
      | Stars / forks   | 905 / 787 |

  In a transposed table the field name belongs in column 1 on every row. That is
  data, correctly formatted. A gate that cannot tell it from a stray header will
  be switched off after its first run, which is worse than no gate.

THE DISCRIMINATOR
  A real header row has field names in (nearly) ALL of its cells. A transposed
  data row has a field name in the FIRST cell and a VALUE in the rest. So score
  the whole row, not the first cell, and require a majority of cells to be
  field-name-shaped before flagging. A genuine stray header also has no
  markdown link, no digits and no units in its value cells.

  Exit 1 if any real orphan header/example row is found, so it can run as a
  pre-commit gate. Controls are built in and run on every invocation.
"""
import re, sys

SEP = re.compile(r'^\|[\s:\-\|]+\|?$')
FIELD = {"name","nombre","repo","repository","licence","licencia","license","platform",
         "project","agent","tool","stars","estrellas","region","description","descripcion",
         "stack","branch","use case","why it is a foundation","default branch","id",
         "pattern","verdict","note","candidate","address","grant","layer","what"}
# NB: licence identifiers (MIT, Apache-2.0) are deliberately NOT placeholders.
# A row that compares two independent licence readings legitimately carries the
# same identifier in several cells -- the gate flagged exactly such a row
# (repos/trending.md: `tokenaii/...` | MIT | MIT | AGREE) before this fix. A
# VALUE vocabulary must never be enrolled as placeholder text (672-E, 2nd sign).
EXAMPLE = {"foo","bar","baz","example","ejemplo","tbd","todo","xxx","...","lorem ipsum",
           "owner/repo","user/repo","github.com/...","your-org/your-repo"}

def norm(c):
    return re.sub(r"[`*_\s]+"," ", c.strip().lower()).strip()

def scan(path):
    lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    hits = []
    for k, ln in enumerate(lines):
        s = ln.strip()
        if not s.startswith("|") or SEP.match(s):
            continue
        # a header followed by a separator is a legitimate table header
        if k + 1 < len(lines) and SEP.match(lines[k+1].strip()):
            continue
        cells = [norm(c) for c in s.strip("|").split("|")]
        cells = [c for c in cells if c != ""]
        if len(cells) < 2:
            continue
        fieldish = sum(1 for c in cells if c in FIELD)
        examplish = sum(1 for c in cells if c in EXAMPLE)
        # a VALUE cell carries a link, a digit, or prose; field names carry none
        valueish = sum(1 for c in cells[1:]
                       if ("](" in c or re.search(r"\d", c) or len(c.split()) > 3))
        if valueish:                      # transposed data row -> not a defect
            continue
        if fieldish >= max(2, (len(cells) + 1) // 2):
            hits.append((k + 1, "ORPHAN-HEADER", s[:90]))
        elif examplish >= max(2, (len(cells) + 1) // 2):
            hits.append((k + 1, "EXAMPLE-ROW", s[:90]))
    return hits

def controls():
    """Both signs, every run (667-C). A gate with only one control is untrusted."""
    import tempfile, os
    pos = "| Name | Repo | Licence |\n| Nombre | Repo | Licencia |\n"          # real defect
    neg = ("| Name | Repo |\n|---|---|\n| **X** | [a/b](https://github.com/a/b) |\n"
           "| Licence payload | MIT, 1,073 B |\n| Description | identical string |\n")
    out = []
    for label, body, want in (("positive", pos, True), ("negative", neg, False)):
        fd, p = tempfile.mkstemp(suffix=".md"); os.write(fd, body.encode()); os.close(fd)
        got = bool(scan(p)); os.unlink(p)
        out.append((label, got, want, got == want))
    return out

if __name__ == "__main__":
    ok = True
    print("controls:")
    for label, got, want, passed in controls():
        print("  %-9s fired=%-5s expected=%-5s %s" % (label, got, want, "OK" if passed else "FAILED"))
        ok &= passed
    if not ok:
        print("GATE UNTRUSTWORTHY — controls failed"); sys.exit(2)
    total = 0
    for path in sys.argv[1:]:
        hits = scan(path)
        total += len(hits)
        print("%-24s %s" % (path, "clean" if not hits else "%d DEFECT(S)" % len(hits)))
        for line, kind, txt in hits:
            print("    L%-6d %-14s %s" % (line, kind, txt))
    print("TOTAL REAL DEFECTS: %d" % total)
    sys.exit(1 if total else 0)
