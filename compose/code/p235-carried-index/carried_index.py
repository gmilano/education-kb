#!/usr/bin/env python3
"""p235 — ACTION UG (p234): the index these shelves never had.

p234's own gap list closed with: "this KB has no index of what it already carries, so every
pass re-discovers rows and the shelves can argue against their own verified cells for 25
passes at a time." This is that index, plus the two predicates a pass actually needs:

    carried(slug)  -> is this row already on the shelves?  (ACTION UH: case-folded)
    claims(token)  -> do the shelves already mention X, before I publish "there is no X"?

Shelves only. Not evidence/, not archive/, not compose/code/ — a row cited in an evidence
TSV but absent from the shelves is NOT carried, and a claim in an archived file is not a
live claim.
"""
import re
import sys

SHELVES = [
    "README.md",
    "agents/top.md", "agents/trending.md",
    "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md", "intel/trends.md", "intel/open-gaps.md",
    "compose/patterns.md",
]

# Deliberately NOT lazy: ACTION TB's lazy-quantifier lint runs over this directory.
SLUG = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")


def fold(slug):
    """ACTION UH — fold case before comparing. `OpenOLAT/OpenOLAT` and `openolat/OpenOLAT`
    are one row; it was that pair that defeated p234's cheap duplicate check."""
    return slug.rstrip(".,)").lower()


def harvest(root="."):
    """-> {folded_slug: {raw spellings}}. Missing shelves are skipped, not fatal: this must
    stay runnable from a partial checkout."""
    index = {}
    for shelf in SHELVES:
        try:
            with open(f"{root}/{shelf}", encoding="utf-8", errors="replace") as fh:
                body = fh.read()
        except FileNotFoundError:
            continue
        for raw in SLUG.findall(body):
            index.setdefault(fold(raw), set()).add(raw.rstrip(".,)"))
    return index


def carried(slug, index):
    return fold(slug) in index


def collisions(index):
    """The rows carried under more than one spelling — ACTION UH's measurement."""
    return {k: sorted(v) for k, v in index.items() if len(v) > 1}


def claims(token, root="."):
    """ACTION UG's real purpose: before publishing "there is no X", grep the shelves for X.
    Returns {shelf: count}. A non-empty return means STOP and read those cells first."""
    hits = {}
    needle = token.lower()
    for shelf in SHELVES:
        try:
            with open(f"{root}/{shelf}", encoding="utf-8", errors="replace") as fh:
                n = fh.read().lower().count(needle)
        except FileNotFoundError:
            continue
        if n:
            hits[shelf] = n
    return hits


def main(argv):
    root = "."
    if len(argv) >= 2 and argv[1] == "claims":
        if len(argv) < 3:
            print("usage: carried_index.py claims <token> [root]", file=sys.stderr)
            return 2
        root = argv[3] if len(argv) > 3 else "."
        hits = claims(argv[2], root)
        if not hits:
            print(f'NOT CLAIMED\t{argv[2]}\t(a "there is no X" claim about this is establishable)')
            return 0
        print(f"ALREADY CLAIMED\t{argv[2]}\tSTOP — read these cells before publishing an absence:")
        for shelf, n in sorted(hits.items(), key=lambda kv: -kv[1]):
            print(f"\t{shelf}\t{n}")
        return 1

    if len(argv) >= 2 and argv[1] == "check":
        # p254 (`ACTION YB` + `ACTION XZ`): this returned 0 for CARRIED and for NEW alike, so
        # the base's SUPPLY TEST — the thing that found the one new row in sixteen passes —
        # could not be wired into anything.  `ACTION YB` asked for "a GATE, not a grep"; the
        # obstruction was never the recipe, it was that the recipe had no status to give.
        # Polarity matches `claims`: non-zero means STOP, the shelves already carry this.
        root = argv[3] if len(argv) > 3 else "."
        index = harvest(root)
        slug = argv[2]
        hit = carried(slug, index)
        print(f"{'CARRIED' if hit else 'NEW'}\t{slug}")
        return 1 if hit else 0

    if len(argv) >= 2:
        root = argv[1]
    index = harvest(root)
    coll = collisions(index)
    print(f"# shelves indexed: {len(SHELVES)}")
    print(f"# distinct rows carried (case-folded): {len(index)}")
    print(f"# rows carried under >1 spelling (ACTION UH): {len(coll)}")
    try:
        for slug in sorted(index):
            print(slug)
    except BrokenPipeError:
        # piping into `head` is the normal way to read this; don't traceback for it
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
