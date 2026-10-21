#!/usr/bin/env python3
"""`p352-census-currency` — a census over the shelves must be RE-DERIVED AFTER the pass writes.

p351 published its own headline denominator as **2 476 harvested -> 33 -> 2 443 addresses**.
Re-derived from the nine `SHELF_FILES` of the tree p351 actually committed, the triple is
**2 478 -> 33 -> 2 445**.  The published figure is, exactly, the one the *p350* tree yields --
and the two missing addresses are nameable: `aclascollege/polymath`, which is p351's OWN new
`repos/foundations.md` row, and `imsglobal/openbadges-validator-core`.

So the defect is not arithmetic and it is not carelessness.  It is an ORDERING defect, and it
is structural: a census whose input is the shelves, published in the pass that then writes to
the shelves, is stale the moment it is written.  Every pass that runs this census before
writing its own section will publish a figure its own commit falsifies, and p350's commit
message says the same thing happened to p349 ("p349's own headline denominator is wrong by
one group and two addresses").  Three passes, one mechanism.

🟢 The fix cannot be "remember to re-run it", because that is what failed.  It is a gate that
compares the PUBLISHED triple against the DERIVED one and goes RED when they disagree, so the
census can only be published correctly: write the pass, derive, then state the figure.

🔵 Why the anchor is in `README.md` and the derivation is over `SHELF_FILES`: the two must not
be the same text, or the gate would be checking a number against itself.  `README.md` is not a
`SHELF_FILE`, so stating the figure cannot change it.

🔴 This gate judges only the LIVE (first) occurrence of the sentence.  History below it is
previous passes' published figures, which were correct against THEIR trees and must not be
rewritten -- that is this base's `dated-by-measurement` convention, and a gate that demanded
the whole file agree with today's tree would force exactly the retro-editing the convention
forbids.
"""
import argparse
import importlib.util
import os
import re
import sys

SHELF_FILES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md", "intel/open-gaps.md",
    "compose/patterns.md",
]
# 🔴 p283's ladder-case audit graded this instrument `SINGLE-SPELLING` on the `readme`
# family the moment it entered `HOOK_GATES`, and it was RIGHT to.  A one-rung path ladder
# cannot prove an absence: if this base's write-up were renamed `Readme.md`, a gate pinned to
# the single spelling `README.md` would report its anchor MISSING and refuse, which is loud
# but still wrong -- the file is there.  🟢 So the ladder is CASE-CLOSED rather than the gate
# being taught an exception: stem case AND extension case both vary, first hit wins, and
# `resolve_anchor` returning None is a real absence rather than a spelling miss.
ANCHOR_LADDER = ("README.md", "README.MD", "Readme.md", "readme.md", "README", "readme")
ANCHOR_FILE = ANCHOR_LADDER[0]  # what this base actually ships; the ladder is the contract

# 🔵 Digit groups on these shelves are separated by a PLAIN SPACE (U+0020), measured, not
# assumed: `2 443` at `README.md:23` is `0x32 0x20 0x34 0x34 0x33`.  The thin and no-break
# spaces are accepted too, because a later pass may paste one in and a cosmetic difference
# must not read as a stale denominator.
_SEPS = "     ,"
_NUM = r"(\d[\d" + _SEPS + r"]*\d|\d)"
TRIPLE_RE = re.compile(
    r"\*\*" + _NUM + r"\*\*\s+harvested\s+shapes"
    r".{0,40}?\*\*" + _NUM + r"\*\*\s+are\s+not\s+addresses"
    r".{0,40}?\*\*" + _NUM + r"\s+addresses\*\*",
    re.DOTALL,
)


def to_int(raw):
    """`2 445` -> 2445.  A grouping separator is presentation, never data."""
    return int(re.sub("[" + _SEPS + r"\s]", "", raw))


def _address_shape():
    """p351's classifier, resolved from THIS file's location -- never from the tree measured.

    🔵 The instrument belongs to the repository; only the data varies.  Loading it from the
    `--root` under test would make the gate's own logic a property of the thing it judges,
    which is the shape of defect `p308`'s shelf gate was built to catch pointed inwards.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "..", "p351-address-shape", "address_shape.py")
    spec = importlib.util.spec_from_file_location("p351_address_shape", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def derive(root):
    """(harvested, rejected, addresses) over SHELF_FILES, via p351's own instrument.

    🟢 p351's classifier is imported rather than reimplemented: two copies of a shape filter
    is the defect this base calls a second channel disagreeing with itself.
    """
    mod = _address_shape()
    paths = [os.path.join(root, p) for p in SHELF_FILES]
    missing = [p for p in paths if not os.path.exists(p)]
    if missing:
        raise FileNotFoundError("; ".join(missing))
    idx = mod.harvest(paths)
    addresses, rejected = mod.partition(idx)
    return len(idx), len(rejected), len(addresses)


def resolve_anchor(root):
    """The write-up's path, walked over a CASE-CLOSED ladder; None is a real absence."""
    for rung in ANCHOR_LADDER:
        candidate = os.path.join(root, rung)
        if os.path.exists(candidate):
            return candidate
    return None


def published(text):
    """The LIVE triple the write-up states, or None when the sentence is absent.

    None is not "no claim": main() reports a missing anchor as a FAILURE, because a headline
    denominator that quietly stops being stated is how p349's went unchecked for two passes.
    """
    hit = TRIPLE_RE.search(text)
    if not hit:
        return None
    return tuple(to_int(g) for g in hit.groups())


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
    args = ap.parse_args(argv)
    root = os.path.abspath(args.root)

    anchor = resolve_anchor(root)
    if anchor is None:
        sys.stderr.write("p352-census-currency: no write-up found at any rung of "
                         f"{list(ANCHOR_LADDER)} -- refusing to judge a denominator "
                         "against nothing\n")
        return 2

    with open(anchor, encoding="utf-8") as fh:
        pub = published(fh.read())
    der = derive(root)

    print("cifra\tpublished\tderived\tverdict")
    if pub is None:
        print("harvested_folded\t--\t%d\tNO-ANCHOR" % der[0])
        print("rejected_non_addresses\t--\t%d\tNO-ANCHOR" % der[1])
        print("addresses_corrected\t--\t%d\tNO-ANCHOR" % der[2])
        sys.stderr.write(
            "🔴 p352-census-currency: NO ANCHOR. The live write-up states no "
            "`**N** harvested shapes -> **M** are not addresses -> **K** addresses` "
            "sentence, so its headline denominator cannot be checked at all.\n")
        return 1

    labels = ("harvested_folded", "rejected_non_addresses", "addresses_corrected")
    stale = 0
    for label, p, d in zip(labels, pub, der):
        ok = p == d
        stale += 0 if ok else 1
        print(f"{label}\t{p}\t{d}\t{'MATCH' if ok else 'STALE'}")
    if stale:
        sys.stderr.write(
            f"🔴 p352-census-currency: {stale} of 3 cells STALE. The live write-up's census "
            "was derived BEFORE this pass wrote to the shelves. Re-run "
            "`make address-shape-census`/`gate-address-shape` as the LAST act before the "
            "commit and restate the triple -- do not edit history to match.\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
