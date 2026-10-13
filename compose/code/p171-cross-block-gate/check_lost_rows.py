#!/usr/bin/env python3
"""P170-C, implemented at p171 for ACTION JM — the cross-block consistency gate.

T216: OpenOLAT was licence-verified at verticals/solutions.md:784 and absent from the ROUTING TABLE
at line 39 of the same file. Append-only, plus "only the newest block is canonical", means a row a
pass does not RE-STATE leaves the compiled view while staying true in the history below it.

p171's FIRST attempt at this gate was unsound and is recorded rather than hidden. It took the
population to be "every repo appearing on a line that also carries a licence identifier", and
reported 372 lost rows across 3 files. That is P471 — a gate that marks everything controls nothing.
The population was wrong: this KB's files carry large CENSUS tables (190+ MCP servers, LTI
libraries, QTI players) that no pass ever intended as recommendations, and a newest block that does
not re-state a 190-row census has lost nothing.

T216's question is narrower and this gate asks only it: a repository this KB once ROUTED an
engagement to, and no longer does. In this KB a routing table is headed by `need`, `engagement`
or `layer` — the tables that answer "what should a client use". A census is headed by `repo`,
`candidate` or `agent / library`, and is out of scope by construction.
"""
import re
import sys

REPO = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?=[)\s`'\"]|$)")
PASS_HDR = re.compile(r"^##\s+Pass\s+(\d+)\b")
# A routing table's FIRST column. Anything else is a census or a probe table.
ROUTING_FIRST_COL = {"need", "engagement", "layer"}


def strip_cell(c):
    return c.strip().strip("*`").strip("🟢🔴🟡🆕🔵 ").strip("*`").strip().lower()


def is_routing_header(line):
    if not line.startswith("|"):
        return False
    cells = [strip_cell(c) for c in line.strip().strip("|").split("|")]
    if len(cells) < 3:
        return False
    first = cells[0].split("—")[0].split("(")[0].strip()
    return first in ROUTING_FIRST_COL


def routing_rows(lines):
    """Yield (line_no, repo) for every repo inside a routing table."""
    in_table = False
    for n, line in enumerate(lines, 1):
        if is_routing_header(line):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                in_table = False
                continue
            if re.match(r"^\|[\s:|-]+\|?\s*$", line):   # the |---|---| separator
                continue
            for m in REPO.finditer(line):
                # GitHub owner/name are case-insensitive, and this KB writes the same repo both
                # ways: "openolat/OpenOLAT" at solutions.md:267 and "OpenOLAT/OpenOLAT" in p170's
                # restored row. A case-sensitive slug match reports a restored row as still lost.
                yield n, m.group(1).casefold()


def newest_block(lines):
    starts = [i for i, l in enumerate(lines) if PASS_HDR.match(l)]
    if not starts:
        return lines, None
    # Newest-FIRST: every pass PREPENDS, so the FIRST header opens the newest block.
    end = starts[1] if len(starts) > 1 else len(lines)
    pass_no = PASS_HDR.match(lines[starts[0]]).group(1)
    return lines[starts[0]:end], pass_no


def main(paths):
    total = 0
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        newest, pass_no = newest_block(lines)
        hist = {}
        for n, repo in routing_rows(lines):
            hist.setdefault(repo, n)
        current = {r for _, r in routing_rows(newest)}
        lost = {r: n for r, n in hist.items() if r not in current}
        print(f"\n## {path}  (newest block: pass {pass_no})")
        print(f"#  routed-in-history: {len(hist)} | routed in newest block: {len(current)}"
              f" | LOST FROM THE ROUTING TABLE: {len(lost)}")
        for repo, n in sorted(lost.items(), key=lambda kv: kv[1]):
            print(f"   LOST  {repo}\tlast/first routed at line {n}")
        total += len(lost)
    print(f"\n# TOTAL ROUTED-THEN-DROPPED ACROSS {len(paths)} FILES: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
