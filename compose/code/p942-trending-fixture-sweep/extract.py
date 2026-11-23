#!/usr/bin/env python3
"""p942 item A - extract every PUBLISHED (slug, bytes, sha256_12) fixture from the
two APPEND-ONLY trending files, so each can be adjudicated against the repository's
own served bytes (p941's method) rather than against this base's evidence TSVs
(p940's method, which p941 showed reads the wrong artefact).

Output: TSV  file<TAB>line<TAB>slug<TAB>bytes<TAB>hash12
"""
import re, sys

SLUG  = re.compile(r"(?:github\.com/|`)([A-Za-z0-9][\w.-]*/[\w.-]+)")
BYTES = re.compile(r"([0-9][0-9,  ]{0,9}[0-9]|[0-9])\s*B\b")
HASH12= re.compile(r"\b([0-9a-f]{12})\b")
FILES = ["agents/trending.md", "repos/trending.md"]

def main():
    n = 0
    for rel in FILES:
        for ln, line in enumerate(open(rel, encoding="utf-8"), 1):
            hs = HASH12.findall(line)
            if not hs:
                continue
            slugs = [s for s in SLUG.findall(line) if "/" in s]
            bs = [int(re.sub(r"[^0-9]", "", b)) for b in BYTES.findall(line)]
            if not slugs or not bs:
                continue
            # one fixture per hash; pair positionally with byte counts when the
            # counts line up, else fall back to the line's first byte count.
            for i, h in enumerate(hs):
                b = bs[i] if len(bs) == len(hs) else bs[0]
                print(f"{rel}\t{ln}\t{slugs[0]}\t{b}\t{h}")
                n += 1
    print(f"# extracted {n} fixtures", file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())
