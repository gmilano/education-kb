#!/usr/bin/env python3
"""p940 - compare every PUBLISHED (bytes, sha256_12) grant fixture in the live
content files against this base's own byte-read payload evidence.

WHY THIS EXISTS.  p925 overwrote a correct, four-times-published byte/hash pair for
chadyi/StudyOnTV (1043 / 67ae8445017e, byte-read in p686, p692 and twice in p866)
with 1,042 / fdc484954b1b.  p937, p938 and p939 each re-asserted "the licence column
holds".  The instrument that should have caught it -
evidence/licence-ledger-structured.2026-11-21-p937.tsv - carries the WRONG value under
method `byte-read-p937`, and its own last column is a scrape of the prose cell: the
verifier is seeded from the page it is meant to check, so it agrees with it by
construction.

WHAT IT DOES.  Offline only.  Reads fixtures out of the prose, reads byte-reads out of
evidence/*.tsv, and prints every slug where they disagree.  No network.
"""
import re, sys, glob, os, collections

ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")
LIVE = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
        "repos/trending.md", "verticals/solutions.md", "intel/market.md",
        "intel/trends.md", "compose/patterns.md", "intel/open-gaps.md",
        "intel/measured-unusable.md"]

SLUG = re.compile(r"(?:github\.com/|`)([A-Za-z0-9][\w.-]*/[\w.-]+)")
# a fixture is a byte count and/or a 12-hex hash near each other
BYTES = re.compile(r"([0-9][0-9,  ]{0,9}[0-9]|[0-9])\s*B\b")
HASH12 = re.compile(r"\b([0-9a-f]{12})\b")

def norm_int(s):
    return int(re.sub(r"[^0-9]", "", s))

def prose_fixtures():
    """(slug, bytes, hash12) triples that appear in the SAME line."""
    out = []
    for rel in LIVE:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        for ln, line in enumerate(open(p, encoding="utf-8"), 1):
            hs = HASH12.findall(line)
            if not hs:
                continue
            slugs = [s for s in SLUG.findall(line) if "/" in s]
            bs = [norm_int(b) for b in BYTES.findall(line)]
            for h in hs:
                out.append((rel, ln, slugs[0] if slugs else None,
                            bs[0] if bs else None, h))
    return out

def evidence_reads():
    """slug -> set of (bytes, hash12) actually byte-read, with the file that says so."""
    reads = collections.defaultdict(set)
    for p in glob.glob(os.path.join(ROOT, "evidence", "*.tsv")):
        base = os.path.basename(p)
        try:
            txt = open(p, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        for line in txt.splitlines():
            if "\t" not in line:
                continue
            f = line.split("\t")
            slug = next((c for c in f[:2] if re.fullmatch(r"[\w.-]+/[\w.-]+", c)), None)
            if not slug:
                continue
            h = None; b = None
            for c in f:
                c = c.strip()
                if re.fullmatch(r"[0-9a-f]{12}", c):
                    h = c
                elif re.fullmatch(r"[0-9]{2,7}", c) and 50 <= int(c) <= 200000:
                    b = int(c)
            if h:
                reads[slug].add((b, h, base))
    return reads

def main():
    fx = prose_fixtures()
    ev = evidence_reads()
    print(f"published fixtures (hash-bearing prose lines): {len(fx)}")
    print(f"slugs with byte-read evidence:                 {len(ev)}")
    conflicts = []
    agreed = 0
    unbacked = 0
    for rel, ln, slug, b, h in fx:
        if not slug or slug not in ev:
            unbacked += 1
            continue
        hashes = {e[1] for e in ev[slug]}
        if h in hashes:
            agreed += 1
            # hash agrees: does the byte count?
            bs = {e[0] for e in ev[slug] if e[1] == h and e[0]}
            if b and bs and b not in bs:
                conflicts.append(("BYTES", rel, ln, slug, b, h, sorted(bs), ""))
        else:
            srcs = sorted({e[2] for e in ev[slug]})
            conflicts.append(("HASH", rel, ln, slug, b, h,
                              sorted(((e[0] if e[0] is not None else -1), e[1]) for e in ev[slug]), ",".join(srcs)))
    print(f"fixtures whose hash matches evidence:          {agreed}")
    print(f"fixtures with no byte-read evidence for slug:  {unbacked}")
    print(f"CONFLICTS:                                     {len(conflicts)}")
    print()
    for c in conflicts:
        kind, rel, ln, slug, b, h, ev_pairs, srcs = c
        print(f"[{kind}] {slug}")
        print(f"   published : {b} B  {h}   ({rel}:{ln})")
        print(f"   byte-read : {ev_pairs}   {srcs}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
