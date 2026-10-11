#!/usr/bin/env python3
"""Extract PROSE licence claims from this KB's pages (ACTION R, p122).

WHY THIS IS NOT A LINE SCAN. The first version of this census scanned each
line for an address and a licence token and paired them. It produced 11
candidates of which verification left 1 — a 91 % false-positive rate, from
three causes this KB's prose style guarantees:

  1. ATTRIBUTION. A token on the same line usually belongs to a NEIGHBOURING
     address: "lrsql (Apache-2.0, 144*), scorm-again (354*)" pairs Apache-2.0
     with scorm-again, which the page never claimed.
  2. WRAPPING. Prose here is hard-wrapped near 95 characters, so an address
     and its token routinely sit on different lines. Both halves of the claim
     are invisible to a line scan.
  3. PRECISION. This KB's prose is written per-repository and is often MORE
     precise than a single token: "MIT code / CC BY-NC-SA data", "MIT badges
     over a 404", "published as Apache-2.0 by". A single-token comparison
     reads each of those as a defect.

So: unwrap each paragraph, then attribute a token to an address only when
that address is the NEAREST one and lies within WINDOW characters. A token
with two addresses equally close is not a claim about either.

usage: extract_claims.py KB_ROOT [WINDOW] > claims.tsv
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
    r"|MPL-2\.0|EPL-2\.0|ECL-2\.0|EUPL-1\.2|Elastic License|CC BY-NC-SA"
    r"|CC BY-SA|CC BY 4\.0)(?![\w-])"
)
WINDOW = 90


def paragraphs(path):
    """Yield (start_line, unwrapped_text) for each paragraph, including code
    blocks: an ASCII architecture diagram carries licence claims too, and
    excluding fenced blocks hid one of this pass's three real defects."""
    buf, start = [], 1
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if line.strip():
                if not buf:
                    start = n
                buf.append(line.rstrip("\n"))
            else:
                if buf:
                    yield start, " ".join(buf)
                buf = []
    if buf:
        yield start, " ".join(buf)


def claims(root, window=WINDOW):
    for page in PAGES:
        path = os.path.join(root, page)
        if not os.path.exists(path):
            continue
        for start, text in paragraphs(path):
            addrs = [(m.start(), m.group(1).rstrip(".").rstrip(")").removesuffix(".git"))
                     for m in ADDR.finditer(text)]
            if not addrs:
                continue
            for lm in LIC.finditer(text):
                pos, tok = lm.start(), lm.group(1)
                scored = sorted(((abs(pos - ap), ap, a) for ap, a in addrs))
                nearest = scored[0]
                if nearest[0] > window:
                    continue
                # A tie between two addresses is not a claim about either.
                if len(scored) > 1 and scored[1][0] == nearest[0]:
                    continue
                yield page, start, nearest[2], tok, nearest[0], text[max(0, pos - 110):pos + 110]


if __name__ == "__main__":
    root = sys.argv[1]
    win = int(sys.argv[2]) if len(sys.argv) > 2 else WINDOW
    for page, line, addr, tok, dist, ctx in claims(root, win):
        print(f"{page}\t{line}\t{addr}\t{tok}\t{dist}\t" + re.sub(r"\s+", " ", ctx))
