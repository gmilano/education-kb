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

print(f"\n{12 - len(FAILED)}/12 controls pass")
sys.exit(1 if FAILED else 0)
