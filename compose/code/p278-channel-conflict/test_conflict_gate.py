#!/usr/bin/env python3
"""Controls for p278's conflict gate — the PARSING, which is where it failed first.

The gate's verdict logic is `direction.py`'s and is pinned by `test_direction.py` (66
controls).  What is NOT covered there is everything the gate does BEFORE it classifies:
locating p121's table in an append-only file, reading a family out of a prose cell, and
normalising the published direction.  🔴 All three are fragile, and the third shipped broken:
the first cut stripped the direction cell with `[^a-z, ]`, which eats the HYPHEN, so
"permissive over attribution-share" became "attributionshare" and the gate reported
`UNKNOWN DIRECTION PROSE` on a perfectly well-formed row.

🔵 A gate that mangles its own input accuses the shelf of a defect that lives in the gate.
That is the most expensive false positive this base can publish -- a later pass "fixes" the
shelf to satisfy it -- so the hyphen case is a named regression control below.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conflict_gate import family_in_cell, find_table, PROSE_TO_VERDICT  # noqa: E402

FAILED = []
RAN = 0


def check(label, got, want):
    global RAN
    RAN += 1
    if got != want:
        FAILED.append(f"FAIL {label}:\n     got  {got!r}\n     want {want!r}")


# ------------------------------------------------- the hyphen regression (the shipped bug)
import re  # noqa: E402


def normalise(cell):
    """The gate's own normalisation, re-expressed so the control pins the RULE."""
    return re.sub(r"[^a-z, -]", "", cell.lower()).strip()


check("the hyphen survives normalisation — the bug this suite exists for",
      "permissive over attribution-share" in normalise("🔴 permissive over attribution-share"),
      True)
check("the old stripping class would have eaten it (negative arm)",
      "permissive over attribution-share" in re.sub(r"[^a-z, ]", "", "permissive over attribution-share"),
      False)
for prose in PROSE_TO_VERDICT:
    check(f"published prose {prose!r} still matches after normalisation",
          prose in normalise("🔴 **" + prose + "**"), True)
# 🔴 The phrase p278's own correction introduced.  The gate refused the row until the
# vocabulary declared it, which is the behaviour being pinned: an UNDECLARED direction phrase
# must fail, because a matcher loose enough to accept any "permissive over …" would accept a
# phrase nobody defined and the gate would stop deciding anything.
check("the NC direction phrase is declared",
      "permissive over non-commercial" in PROSE_TO_VERDICT, True)
check("an UNdeclared 'permissive over ...' phrase is NOT silently accepted",
      "permissive over whatever-nobody-defined" in PROSE_TO_VERDICT, False)
check("a comma-bearing direction survives",
      "both permissive, wrong name" in normalise("🟡 both permissive, wrong name"), True)

# ------------------------------------------------- family extraction from a prose cell
check("plain MIT cell", family_in_cell("🟢 **MIT**"), "MIT")
check("AGPL with bytes", family_in_cell("🔴 **AGPL-3.0**, `LICENSE` 34 523 B"), "AGPL-3.0")
check("ISC cell", family_in_cell("🟢 **ISC**"), "ISC")
check("BSD family cell", family_in_cell("🟢 BSD family"), "BSD")
check("Fair Code, however spelled", family_in_cell('🔴 **"Fair Code License" v1.0**'), "FAIRCODE")
check("an absent grant stated in prose",
      family_in_cell("🔴 **no licence file — author claim only**"), "NONE")
# 🔴 THE ORDERING CONTROL.  NC/ND must be tested before the bare CC-BY arm, or a
# non-commercial grant reads as attribution-share -- the exact mis-grade that prompted this
# whole instrument (p121's cccareers row).
check("CC-BY-NC-SA is NOT read as CC-BY", family_in_cell("CC-BY-NC-SA-4.0"), "CC-BY-NC-SA-4.0")
check("CC-BY-NC is NOT read as CC-BY", family_in_cell("🔴 CC-BY-NC-4.0"), "CC-BY-NC-4.0")
check("CC-BY-SA is not collapsed to CC-BY", family_in_cell("CC-BY-SA-4.0"), "CC-BY-SA-4.0")
check("a bare CC-BY cell still reads as CC-BY", family_in_cell("🟡 **CC-BY** 4.0"), "CC-BY-4.0")
check("GPL-3.0 is not read as GPL-2.0", family_in_cell("🔴 **GPL-3.0**"), "GPL-3.0")
check("AGPL is not read as GPL", family_in_cell("**AGPL-3.0**"), "AGPL-3.0")
check("LGPL is not read as GPL", family_in_cell("🟡 **LGPL-3.0**"), "LGPL-3.0")
check("an unrecognised cell returns None, never a guess",
      family_in_cell("🔵 see the note below"), None)

# ------------------------------------------------- locating the table in an append-only file
HEADER = "| address | manifest | manifest says | 🟢 committed file says | direction |"
DOC = "\n".join([
    "# a shelf that grows at the TOP, as this base's trending shelves do",
    "some prose",
    HEADER,
    "|---|---|---|---|---|",
    "| [`a/b`](https://github.com/a/b) | `package.json` | 🟢 **MIT** | 🔴 **AGPL-3.0** | 🔴 permissive over network copyleft |",
    "| [`c/d`](https://github.com/c/d) | `package.json` | 🟢 ISC | 🟢 MIT | 🟡 both permissive, wrong name |",
    "",
    "trailing prose that is not a row",
])
line, rows = find_table(DOC)
check("the table is found by its own header, not a line number", line, 3)
check("exactly the data rows are returned", len(rows), 2)
check("the separator row is skipped", rows[0].startswith("| [`a/b`]"), True)
check("the table stops at the first non-row line", rows[-1].startswith("| [`c/d`]"), True)
# 🔵 A gate that cannot find its subject must FAIL, not pass.  p277's deleted tier boundary
# hid in exactly this shape, so the absent-table arm is asserted.
line2, rows2 = find_table("# a document with no such table\n\nprose only\n")
check("a missing table returns no rows (the gate then fails)", rows2, [])
check("a missing table reports no line", line2, None)
# The header must need BOTH distinctive cells, or any table with a "direction" column matches.
_, rows3 = find_table("| a | direction |\n|---|---|\n| x | y |\n")
check("a 'direction' column alone does not match the header", rows3, [])

FLOOR = 25
if RAN < FLOOR:
    FAILED.append(f"FAIL floor: suite ran {RAN} controls, floor is {FLOOR}")

if FAILED:
    print(f"# {len(FAILED)} FAILING of {RAN}:")
    for f in FAILED:
        print("  " + f)
    sys.exit(1)
print(f"# {RAN}/{RAN} controls pass (parsing, ordering, and the hyphen regression)")
sys.exit(0)
