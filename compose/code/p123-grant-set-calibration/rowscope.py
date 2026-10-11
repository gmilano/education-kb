#!/usr/bin/env python3
"""ACTION X — re-attribute a candidate claim with ROW scope, not paragraph scope.

WHY A ROW IS NOT A PARAGRAPH. p122's extractor unwraps each paragraph before
attributing a licence token to the nearest address, and for PROSE that is
correct -- this KB hard-wraps near 95 characters, so an address and its token
routinely sit on different lines. But a Markdown TABLE is a sequence of
RECORDS, one per line, and consecutive rows are not one paragraph: a token in
the next row belongs to the next repository. Unwrapping a table therefore
manufactures exactly the neighbour-attribution error p122 documented
(`moodle/moodle` flagged BSD-3-Clause because the token belonged to
`jupyterhub/jupyterhub`, the adjacent row).

So: if the address occurs on a line that is a TABLE ROW, the claim must be on
THAT line to count. Prose keeps paragraph scope.

usage: rowscope.py KB_ROOT CANDIDATES_TSV
"""
import os
import re
import sys

TOK = {
    "MIT": r"\bMIT\b",
    "Apache-2.0": r"Apache[- ]2(\.0)?", "Apache 2.0": r"Apache[- ]2(\.0)?",
    "BSD-3-Clause": r"BSD[- ]3[- ]Clause", "BSD-2-Clause": r"BSD[- ]2[- ]Clause",
    "ISC": r"\bISC\b", "MPL-2.0": r"MPL[- ]2(\.0)?", "Unlicense": r"Unlicense",
}


def main(root, cand):
    rows = [r.rstrip("\n").split("\t") for r in open(cand, encoding="utf-8")]
    pages = {}
    out = {"ROW-CONFIRMED": [], "ROW-REFUTED": [], "PROSE": []}
    for p in rows:
        if len(p) < 7:
            continue
        v, page, _line, addr, claim = p[0], p[1], p[2], p[3], p[4]
        if page not in pages:
            pages[page] = open(os.path.join(root, page), encoding="utf-8").read().splitlines()
        rx = re.compile(TOK.get(claim, re.escape(claim)), re.I)
        arx = re.compile(r"github\.com/" + re.escape(addr) + r"(?![A-Za-z0-9_.-])", re.I)
        hits = [(n, L) for n, L in enumerate(pages[page], 1) if arx.search(L)]
        table_rows = [(n, L) for n, L in hits if L.lstrip().startswith("|")]
        if not table_rows:
            out["PROSE"].append((v, page, addr, claim))
            continue
        # The address is published in table rows. Does ANY of its own rows
        # carry the claimed token?
        if any(rx.search(L) for _n, L in table_rows):
            ln = next(n for n, L in table_rows if rx.search(L))
            out["ROW-CONFIRMED"].append((v, page, addr, claim, ln))
        else:
            out["ROW-REFUTED"].append((v, page, addr, claim, table_rows[0][0]))
    for k in ("ROW-CONFIRMED", "ROW-REFUTED", "PROSE"):
        seen = set()
        print(f"== {k}: {len(out[k])} candidate(s)")
        for t in out[k]:
            key = (t[1], t[2], t[3])
            if key in seen:
                continue
            seen.add(key)
            print("   " + "\t".join(str(x) for x in t))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
