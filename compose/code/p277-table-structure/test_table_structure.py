#!/usr/bin/env python3
"""p277 controls for the table-structure gate.  Every house-style shape that broke a draft
is a control here, so a later pass widening the predicate detonates on them instead of on
the shelves."""
import sys
import table_structure as T

FAILED = []


def check(label, actual, expected):
    if actual != expected:
        FAILED.append(f"{label}: expected {expected!r}, got {actual!r}")


L = str.splitlines

# --- the two real defects this gate was built from -------------------------------------
check("p276's shape: separator BELOW the first data row is caught",
      [k for _, k, _ in T.header_defects(L("| A | B |\n| real row | x |\n|---|---|\n"))],
      ["SEPARATOR ON ROW 3, NOT 2"])
check("p277's shape: a blank line that orphans the lower half IS a defect",
      len(T.split_defects(L("| H | x |\n|---|---|\n| a | 1 |\n\n| Koha | 2 |\n| b | 3 |\n"))),
      1)
check("p277's shape: the orphaned row is NAMED, not just counted",
      T.split_defects(L("| H | x |\n|---|---|\n| a | 1 |\n\n| Koha | 2 |\n| b | 3 |\n"))[0][1],
      "| Koha | 2 |")

# --- house-style shape 1: the EMPTY `| | |` header row ---------------------------------
check("an empty `| | |` header row is a HEADER, not a separator",
      bool(T.SEP.match("| | |")), False)
check("a real separator still matches",
      bool(T.SEP.match("|---|---|")), True)
check("an aligned separator still matches",
      bool(T.SEP.match("|:---|---:|")), True)
check("the empty-header table is clean to the gate",
      T.header_defects(L("| | |\n|---|---|\n| rows worked | 12 |\n")), [])

# --- house-style shape 2: a blank between two DIFFERENT tables -------------------------
check("a blank before a genuine header+separator is NOT a defect",
      T.split_defects(L("| a | 1 |\n\n| Repo | Licence |\n|---|---|\n| x | MIT |\n")), [])

# --- house-style shape 3: indented ASCII pipe-art --------------------------------------
check("indented pipe-art is not a table row",
      bool(T.ROW.match("        |                               |")), False)
check("an unindented row is a table row",
      bool(T.ROW.match("| real | row |")), True)
check("indented art around a blank raises nothing",
      T.split_defects(L("        |   |\n\n        |   |\n        |   |\n")), [])

# --- the trailing pipe is OPTIONAL in GFM, and requiring it was a false positive -------
check("a row without a trailing pipe is still a row",
      bool(T.ROW.match("| wrapped cell | text with no closing pipe")), True)
check("a separator without a trailing pipe still matches",
      bool(T.SEP.match("|---|---")), True)

# --- a clean table raises nothing ------------------------------------------------------
check("a well-formed table is clean",
      T.header_defects(L("| A | B |\n|---|---|\n| 1 | 2 |\n| 3 | 4 |\n")), [])
check("a well-formed table has no split defect",
      T.split_defects(L("| A | B |\n|---|---|\n| 1 | 2 |\n")), [])

if FAILED:
    print(f"# {len(FAILED)} FAILING:")
    for f in FAILED:
        print("  FAIL", f)
    sys.exit(1)
print("# p277 table-structure suite: 15/15 PASS")
