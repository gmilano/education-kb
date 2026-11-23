#!/usr/bin/env python3
"""p942 item A, SECOND instrument - the first one had three bugs of its own, all
found by inspecting the lines behind its own defect list before publishing it.

BUG 1 (separator).  Byte counts in this base are written in at least four forms:
`1,074 B` (en), `1.078 B` (es), `34 273 B` (spaced), `34,273 B`.  A character class
of [0-9, ] silently captured `078` out of `1.078` and `357` out of `11.357`,
manufacturing a "published 78 B vs served 1078 B" defect out of a correct cell.

BUG 2 (adjacency).  The unit is often outside the code span: "`34 273` B".  A regex
requiring [\\s]*B after the digits does not match, so the line's NEXT byte count -
which belongs to the prose, not the fixture - was captured instead.

BUG 3 (pairing).  Pairing the i-th hash with the i-th byte count, and falling back
to the FIRST count when the two lists differ in length, crosses cells on any line
that mentions a byte count in prose.  Fixed by pairing each hash with the byte
count NEAREST to it in the line.

Output: TSV  file<TAB>line<TAB>slug<TAB>bytes<TAB>hash12<TAB>distance
"""
import re, sys

SLUG   = re.compile(r"(?:github\.com/|`)([A-Za-z0-9][\w.-]*/[\w.-]+)")
# digits with ,/./nbsp/narrow-nbsp/space separators, then optional `*' decoration, then B
BYTES  = re.compile(r"(?<![\w.])([0-9][0-9,.   ]{0,9}[0-9]|[0-9])[`*\s]{0,3}B\b")
HASH12 = re.compile(r"\b([0-9a-f]{12})\b")
FILES  = ["agents/trending.md", "repos/trending.md"]

def norm(s):
    return int(re.sub(r"[^0-9]", "", s))

def main():
    n = 0
    for rel in FILES:
        for ln, line in enumerate(open(rel, encoding="utf-8"), 1):
            hs = list(HASH12.finditer(line))
            if not hs:
                continue
            slugs = [s for s in SLUG.findall(line) if "/" in s]
            if not slugs:
                continue
            bms = list(BYTES.finditer(line))
            if not bms:
                continue
            for hm in hs:
                # nearest byte count to this hash
                best = min(bms, key=lambda m: abs(m.start() - hm.start()))
                dist = abs(best.start() - hm.start())
                print(f"{rel}\t{ln}\t{slugs[0]}\t{norm(best.group(1))}\t{hm.group(1)}\t{dist}")
                n += 1
    print(f"# extracted {n} fixtures", file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())
