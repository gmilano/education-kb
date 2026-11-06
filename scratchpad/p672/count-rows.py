#!/usr/bin/env python3
"""Count real data rows in the first markdown table of a shelf file.
A data row: starts with '|', is not the header, not the separator, and its
first cell is not a placeholder like 'Name'/'Nombre'/'Repo'."""
import re, sys
PLACEHOLDER = {"name","nombre","repo","repository","licence","license","platform",
               "project","agent","tool","id","pattern","#","-",""}
for path in sys.argv[1:]:
    lines = open(path, errors="replace").read().split("\n")
    rows, inhdr, seen_sep, total_tables = [], False, False, 0
    for ln in lines:
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells:
            continue
        first = re.sub(r"[*`\s🆕🟢🔴🔵🟡⚠️🔧🔄]", "", cells[0]).lower()
        if set(re.sub(r"[^\-: ]", "", s)) <= {"-", ":", " "} and "-" in s:
            seen_sep = True
            continue
        if first in PLACEHOLDER:
            total_tables += 1
            continue
        rows.append(cells[0][:52])
    print("%-32s data_rows=%d  (tables/headers seen=%d)" % (path.split("/")[-1], len(rows), total_tables))
    if "--list" in sys.argv:
        for r in rows: print("    ", r)
