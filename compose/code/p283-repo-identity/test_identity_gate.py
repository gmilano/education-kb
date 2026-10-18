#!/usr/bin/env python3
"""Controls for p283's identity gate.

🔵 Every control below is a shape that either (a) broke a draft of this gate on this
base's real corpus, or (b) is the defect the gate exists to catch.  The file-scope
controls (C4, C5) are the 15 false positives the first draft produced on a green shelf.
"""
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from identity_gate import check_offline, live_rows  # noqa: E402

LEDGER = [("ls1intum/iris", "ls1intum/pyris", "p282")]
FAILED = []


def run(name, shelf_text, expect_findings, ledger=LEDGER, shelf="agents/top.md"):
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / shelf).parent.mkdir(parents=True, exist_ok=True)
        (root / shelf).write_text(shelf_text, encoding="utf-8")
        got = check_offline(root, ledger)
    ok = len(got) == expect_findings
    print(f"{'  ok  ' if ok else '  FAIL'} {name} (expected {expect_findings}, got {len(got)})")
    if not ok:
        FAILED.append(name)
        for g in got:
            print(f"        {g}")


H = "| name | repo | licence |\n|---|---|---|\n"

# C1 — THE DEFECT ITSELF: both halves of a recorded pair, two live rows, one table.
run("C1 alias pair, two live rows in one table", H
    + "| Iris | https://github.com/ls1intum/Iris | MIT |\n"
    + "| Pyris | https://github.com/ls1intum/Pyris | MIT |\n", 1)

# C2 — p282's ACTUAL correction shape.  The withdrawn row is still published, struck
# through, carrying its own evidence.  A gate that fires here cannot ever be green
# without deleting the forensic record.
run("C2 withdrawn-in-place (~~) beside the canonical row", H
    + "| ~~Iris~~ → not a separate repository | https://github.com/ls1intum/Iris | MIT |\n"
    + "| Pyris | https://github.com/ls1intum/Pyris | MIT |\n", 0)

# C3 — the same withdrawal expressed as a word rather than strikethrough.
run("C3 withdrawal marked by the word WITHDRAWN", H
    + "| Iris | https://github.com/ls1intum/Iris | WITHDRAWN as a row (p282) |\n"
    + "| Pyris | https://github.com/ls1intum/Pyris | MIT |\n", 0)

# C4 — FALSE POSITIVE the first draft produced 15 times: the build-on tier and the
# `## Agents by function` index both point at one repository.  That is a cross-reference.
run("C4 cross-table index reference is not a duplicate", H
    + "| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp | MIT |\n"
    + "\n## Agents by function\n\n"
    + "| repo | licence | note |\n|---|---|---|\n"
    + "| https://github.com/vishalsachdev/canvas-mcp | MIT | Canvas |\n", 0)

# C5 — same shape for a ledger PAIR split across two tables: an index may legitimately
# name the alias while the tier recommends the canonical.
run("C5 alias pair split across two tables", H
    + "| Pyris | https://github.com/ls1intum/Pyris | MIT |\n"
    + "\n## Elsewhere\n\n"
    + "| repo | note |\n|---|---|\n"
    + "| https://github.com/ls1intum/Iris | the tutor's user-facing name |\n", 0)

# C6 — the live residue p283 found on its first run: BOTH halves inside ONE cell,
# presented as two distinct MIT subsystems.  repos/foundations.md:66, missed by p282.
run("C6 both halves named inside ONE row (the p283 finding)", H
    + "| Artemis | https://github.com/ls1intum/Artemis | MIT | ships Iris "
      "(https://github.com/ls1intum/Iris, MIT) and Pyris "
      "(https://github.com/ls1intum/Pyris, MIT) |\n", 1)

# C7 — prose and indented ASCII diagrams are NOT rows.  verticals/solutions.md explains
# the alias inside a code-block diagram; explaining the defect is the opposite of it.
run("C7 prose and indented diagram are not rows", H
    + "| Pyris | https://github.com/ls1intum/Pyris | MIT |\n"
    + "\nThe tutor is named Iris; https://github.com/ls1intum/Iris is an ALIAS.\n"
    + "\n       | tutoring: ls1intum/Pyris -> https://github.com/ls1intum/Iris\n", 0)

# C8 — the same address twice in one table, which `recount` cannot see because the
# row count is right.
run("C8 same address as two live rows of one table", H
    + "| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp | MIT |\n"
    + "| Canvas MCP | https://github.com/vishalsachdev/canvas-mcp | MIT |\n", 1)

# C9 — address normalisation: case and a `.git` suffix must not hide a pair.
run("C9 case and .git suffix are normalised", H
    + "| Iris | https://github.com/LS1INTUM/Iris.git | MIT |\n"
    + "| Pyris | https://github.com/ls1intum/pyris | MIT |\n", 1)

# C10 — NEGATIVE CONTROL.  With an empty ledger the pair must NOT be reported, or the
# gate is reporting its own hard-coding rather than a shelved adjudication.
run("C10 negative control: empty ledger reports no pair", H
    + "| Iris | https://github.com/ls1intum/Iris | MIT |\n"
    + "| Pyris | https://github.com/ls1intum/Pyris | MIT |\n", 0, ledger=[])

# C11 — a separator must never be read as a data row.
rows = live_rows(H + "| a | https://github.com/x/y | MIT |\n")
print(f"{'  ok  ' if len(rows) == 1 else '  FAIL'} C11 separator is not a data row "
      f"(expected 1 row, got {len(rows)})")
if len(rows) != 1:
    FAILED.append("C11")

# C12 — a table ends at a blank line: two adjacent tables are two tables.
ids = {t for t, _, _ in live_rows(
    H + "| a | https://github.com/x/y | MIT |\n\n" + H + "| b | https://github.com/x/y | MIT |\n")}
print(f"{'  ok  ' if len(ids) == 2 else '  FAIL'} C12 a blank line ends a table "
      f"(expected 2 tables, got {len(ids)})")
if len(ids) != 2:
    FAILED.append("C12")

# ── p300 ──────────────────────────────────────────────────────────────────────────
# C13 — THE FALSE POSITIVE THAT WAS RED FOR TWO PASSES, pinned in shape from
# repos/foundations.md:951,972.  Row A recommends one repository and CITES a sibling in
# its description; row B recommends that sibling.  Two rows, one table, one
# recommendation each.  Whole-row harvesting called this a duplicate, four times over.
run("C13 a sibling cited in a description cell is not a second recommendation", H
    + "| 1EdTech/lti-1-3-php-library | https://github.com/1EdTech/lti-1-3-php-library | "
      "Apache-2.0 | the sanctioned route, cf. https://github.com/tsugiproject/tsugi |\n"
    + "| tsugiproject/tsugi | https://github.com/tsugiproject/tsugi | Apache-2.0 | "
      "framework for LTI tools |\n", 0)

# C14 — OVERFIT GUARD.  The subject is the first ADDRESS-BEARING cell, NOT cell 1.
# Measured at p300: 153 of 379 live address rows on this corpus carry no address in
# cell 1, so a cell-1 rule would silently stop checking 40 % of the shelf.  Here the
# duplicated subject sits in cell 2 behind a plain-text name and MUST still fire.
run("C14 subject found past a nameless first cell (cell-1 overfit guard)", H
    + "| Canvas MCP | https://github.com/vishalsachdev/canvas-mcp | MIT |\n"
    + "| Canvas (MCP) | https://github.com/vishalsachdev/canvas-mcp | MIT |\n", 1)

# C15 — the ALIAS arm must NOT be narrowed along with the address arm.  Both halves of
# a PROVEN pair in one row, the alias reachable only from a description cell: that is
# C6's defect, and p283 found it live.  A symmetric "fix" would delete this finding.
run("C15 alias arm keeps whole-row scope (C6 preserved at the new boundary)", H
    + "| Artemis | https://github.com/ls1intum/Artemis | MIT | bundles "
      "https://github.com/ls1intum/Iris and https://github.com/ls1intum/Pyris |\n", 1)

# C16 — a repository cited ONLY as a cross-reference, by two different rows, is
# recommended by neither.  The complement of C13, and the shape that proves the new
# scope asks about the SUBJECT rather than counting mentions.
run("C16 cited twice but recommended never", H
    + "| a | https://github.com/x/a | MIT | see https://github.com/third/party |\n"
    + "| b | https://github.com/x/b | MIT | also https://github.com/third/party |\n", 0)

# C17 — subject_only must not change the ROW COUNT, only the addresses per row.
n_all = len(live_rows(H + "| a | https://github.com/x/y | MIT | cf https://github.com/p/q |\n"))
n_sub = len(live_rows(H + "| a | https://github.com/x/y | MIT | cf https://github.com/p/q |\n",
                      subject_only=True))
print(f"{'  ok  ' if n_all == n_sub == 1 else '  FAIL'} C17 subject scope changes "
      f"addresses, not row count (got {n_all} / {n_sub})")
if not (n_all == n_sub == 1):
    FAILED.append("C17")

TOTAL = 17
print(f"\n{TOTAL - len(FAILED)}/{TOTAL} controls pass")
sys.exit(1 if FAILED else 0)
