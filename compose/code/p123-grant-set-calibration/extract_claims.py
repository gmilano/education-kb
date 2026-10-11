#!/usr/bin/env python3
"""Extract the KB's LIVE licence claims (p123).

THREE CHANGES ON p122'S EXTRACTOR, each from a measured false-positive class.

1. ROW SCOPE FOR TABLE ROWS. p122 unwrapped every paragraph and attributed a
   token to the nearest address. For PROSE that is right -- this KB hard-wraps
   near 95 characters. But a Markdown table is a sequence of RECORDS, one per
   line, and consecutive rows are not one paragraph. Unwrapping a table
   manufactures the neighbour attribution p122 itself documented
   (`moodle/moodle` flagged BSD-3-Clause for `jupyterhub/jupyterhub`'s token).
   Measured on p123's high-consequence subset: 28 of 72 candidates, 39 %.

2. MARKED CORRECTION SPANS ARE REMOVED BEFORE ATTRIBUTION. A repaired row
   records its OLD value on purpose ("AGPL-3.0 was MIT"). p122's guard tried
   to recognise that by VOCABULARY and p121 recorded it mis-firing. ACTION V
   back-filled an explicit `<!--corrected-->` marker on all 51 such rows, so
   the old token can now be deleted by exact match before anything is
   attributed. Measured: this was the single largest false-positive class --
   every one of the 9 highest-consequence ROW-CONFIRMED candidates p123 read
   by hand was a correction row.

3. REPORTED CLAIMS ARE NOT THIS KB'S CLAIMS. A cell saying "a widely-cited
   comparison lists it as MIT" is a claim ABOUT a third party's claim, and
   this KB writes those deliberately, next to the refutation. Tokens governed
   by a reporting phrase are tagged REPORTED and excluded from the live set.
   This guard is narrow and declared; it is not a substitute for reading.

usage: extract_claims.py KB_ROOT [WINDOW] > claims.tsv
output: page <TAB> line <TAB> address <TAB> token <TAB> distance <TAB> context
"""
import os
import re
import sys

PAGES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md",
    "repos/trending.md", "verticals/solutions.md", "intel/market.md",
    "intel/trends.md", "compose/patterns.md", "README.md",
]
ADDR = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?=[)\s>`\"',;]|$)")
LIC = re.compile(
    r"(?<![\w-])(MIT|Apache-2\.0|Apache 2\.0|AGPL-3\.0|AGPL-3|AGPLv3|GPL-3\.0"
    r"|GPL-2\.0|GPLv3|GPLv2|LGPL-3\.0|LGPLv3|BSD-3-Clause|BSD-2-Clause"
    r"|MPL-2\.0|EPL-2\.0|ECL-2\.0|EUPL-1\.2|EUPL-1\.1|Elastic License|CC BY-NC-SA"
    r"|CC BY-SA|CC BY 4\.0)(?![\w-])"
)
# A marked correction span: the old value, recorded on purpose. ACTION V.
CORRECTED = re.compile(r"⚠️ \*\*was [^*]*\*\*<!--corrected-->")
# A reporting phrase: what someone ELSE claims, written next to its refutation.
REPORTING = re.compile(
    r"(lists? it as|lists? as|roundups?|badge|claims?|asserts?|says?|"
    r"comparison|still list|reported as|advertis)", re.I)
WINDOW = 90
# URL paths that are not repository addresses. p123: 14 of 38 "absent"
# addresses were these, i.e. 37 % of a non-existence count that no previous
# pass filtered.
NOT_A_REPO = re.compile(r"^(topics|trending|search|orgs|repos|sponsors|collections)/", re.I)


def is_row(line):
    return line.lstrip().startswith("|")


def attribute(text, page, lineno, out):
    addrs = [(m.start(), m.group(1).rstrip(".").rstrip(")").removesuffix(".git"))
             for m in ADDR.finditer(text)]
    if not addrs:
        return
    for lm in LIC.finditer(text):
        pos, tok = lm.start(), lm.group(1)
        scored = sorted(((abs(pos - ap), ap, a) for ap, a in addrs))
        nearest = scored[0]
        if nearest[0] > WINDOW:
            continue
        if len(scored) > 1 and scored[1][0] == nearest[0]:
            continue  # a tie is a claim about neither
        addr = nearest[2]
        if NOT_A_REPO.match(addr):
            continue
        # Is this token governed by a reporting phrase in the 80 chars before it?
        before = text[max(0, pos - 80):pos]
        kind = "REPORTED" if REPORTING.search(before) else "LIVE"
        ctx = re.sub(r"\s+", " ", text[max(0, pos - 110):pos + 110])
        out.append((page, lineno, addr, tok, nearest[0], kind, ctx))


def claims(root):
    out = []
    for page in PAGES:
        path = os.path.join(root, page)
        if not os.path.exists(path):
            continue
        buf, start = [], 1
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        for n, raw in enumerate(lines, 1):
            line = CORRECTED.sub(" ", raw)
            if is_row(line):
                # flush any open prose paragraph, then score the row alone
                if buf:
                    attribute(" ".join(buf), page, start, out)
                    buf = []
                attribute(line, page, n, out)
                continue
            if line.strip():
                if not buf:
                    start = n
                buf.append(line)
            elif buf:
                attribute(" ".join(buf), page, start, out)
                buf = []
        if buf:
            attribute(" ".join(buf), page, start, out)
    return out


if __name__ == "__main__":
    root = sys.argv[1]
    for page, line, addr, tok, dist, kind, ctx in claims(root):
        print(f"{page}\t{line}\t{addr}\t{tok}\t{dist}\t{kind}\t{ctx}")
