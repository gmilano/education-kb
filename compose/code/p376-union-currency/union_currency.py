#!/usr/bin/env python3
"""`p376-union-currency` — `ACTION p375-A`, the action `p375` ranked FIRST and refused to do
quietly.

🔵 What `p375` left standing, and why it was right to.  `p375` built `census_union` and
measured the figure no census had reported: **3 385** addresses over both channels, against the
**2 657** the standing triple publishes.  It then refused to repoint `gate-census-currency` at
the union, for two stated reasons:

  1. `gate-census-currency` governs *p351's sentence*, and that sentence's three numbers are
     quoted in every prior README section.  Repointing the anchor would have made a gate judge
     today's tree against a number written for an older one — which is the retro-editing this
     base's `dated-by-measurement` convention forbids.
  2. `p367` already imports `p351`, so putting the union *inside* `p351` is an import cycle.

🟢 The discharge is therefore NOT a repoint.  `p352` is left byte-for-byte alone, so every
historical quote of `2 657 / 33 / 2 690` stays true against the tree that produced it, and the
union becomes a SECOND governed sentence with its own gate arm.  Two sentences, two
derivations, one anchor file.  The union figure stops being a thing `p375` published once in a
side table and becomes a number this base cannot let go stale — which is the whole content of
`ACTION p375-A`.

🔵 Why this is a fourth layer rather than an edit to `p375`.  `census_union` imports `p351` and
`p367`; this file imports `census_union` AND `p352`.  Nothing imports this file, so the cycle
`p375` named cannot form here no matter which direction a successor extends.

🔴 The pinning discipline, learned from `p310`'s defect and the audit at `Makefile:2947`.  A
control that pins **3 385** would be a control that the next shelf write turns red for the
right reason and the wrong cause — the union total is DERIVED and is supposed to move.  So this
suite pins the INVARIANTS (the union contains channel U; it cannot exceed U + B) and a BOUND
(both channels are non-empty), never the totals.  `main()` is what compares published against
derived, and that comparison is the gate.
"""
import argparse
import importlib.util
import os
import re
import sys


def _load(relpath, name):
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, os.pardir, relpath)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _p352():
    """p352's own anchor ladder and integer parse, imported rather than reimplemented.

    🔵 Two copies of the anchor ladder is precisely the defect this base calls "a second
    channel disagreeing with itself".  The ladder is `p283`'s CASE-CLOSED contract and it has
    exactly one implementation.
    """
    return _load(os.path.join("p352-census-currency", "census_currency.py"), "p376_p352")


def _p375():
    return _load(os.path.join("p375-census-union", "census_union.py"), "p376_p375")


SHELF_FILES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md", "intel/open-gaps.md",
    "compose/patterns.md",
]

# 🔵 The governed sentence.  Deliberately worded so it CANNOT collide with `p352`'s
# `harvested shapes -> are not addresses -> addresses` triple: a parser that matched both
# would let one sentence satisfy the other's gate.  Separator tolerance is `p352`'s, for the
# same measured reason (a pasted thin space is cosmetic, not a stale denominator).
_SEPS = "    ,"
_NUM = r"(\d[\d" + _SEPS + r"]*\d|\d)"
UNION_RE = re.compile(
    r"\*\*" + _NUM + r"\*\*\s+channel-U\s+addresses"
    r".{0,80}?\*\*" + _NUM + r"\*\*\s+channel-B\s+survivors"
    r".{0,80}?\*\*" + _NUM + r"\s+addresses\s+over\s+both\s+channels\*\*",
    re.DOTALL,
)


def to_int(raw):
    return int(re.sub("[" + _SEPS + r"\s]", "", raw))


def derive(root):
    """(channel_u, channel_b_survivors, union) over SHELF_FILES, via p375's own instrument."""
    union_mod = _p375()
    p351 = union_mod._p351()
    paths = [os.path.join(root, p) for p in SHELF_FILES]
    missing = [p for p in paths if not os.path.exists(p)]
    if missing:
        raise FileNotFoundError("; ".join(missing))
    idx = p351.harvest(paths)
    u_addresses, _u_rejected = p351.partition(idx)
    addresses, _rejected, _harvested, b_survivors = union_mod.union_harvest(paths)
    return len(u_addresses), len(b_survivors), len(addresses)


def published(text):
    """The LIVE union sentence, or None when it is absent.

    🔴 First occurrence wins, exactly as `p352` does it.  History below the live section is
    previous passes' figures, correct against THEIR trees; a gate that demanded the whole file
    agree with today's derivation would force the retro-editing the convention forbids.
    """
    hit = UNION_RE.search(text)
    if not hit:
        return None
    return tuple(to_int(g) for g in hit.groups())


def invariants(u, b, union):
    """Structural truths about a set union.  Violated => the instrument is wrong, not the text.

    These are the controls that are safe to pin, because they hold for every tree this base
    will ever have.  A total is not.
    """
    broken = []
    if union < u:
        broken.append(f"union {union} < channel-U {u}: a union cannot lose a member of U")
    if union > u + b:
        broken.append(f"union {union} > U+B {u + b}: a union cannot exceed the sum of parts")
    if u <= 0 or b <= 0:
        broken.append(f"a channel is empty (U={u}, B={b}): a census over nothing is not a census")
    return broken


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir, os.pardir))
    args = ap.parse_args(argv)
    root = os.path.abspath(args.root)

    p352 = _p352()
    anchor = p352.resolve_anchor(root)
    if anchor is None:
        sys.stderr.write(
            "p376-union-currency: no write-up found at any rung of "
            f"{list(p352.ANCHOR_LADDER)} -- refusing to judge a denominator against "
            "nothing\n")
        return 2

    with open(anchor, encoding="utf-8") as fh:
        pub = published(fh.read())
    u, b, union = derive(root)

    broken = invariants(u, b, union)
    if broken:
        print("cifra\tpublished\tderived\tverdict")
        sys.stderr.write("🔴 p376-union-currency: the UNION ITSELF is impossible — "
                         + "; ".join(broken) + "\n")
        return 1

    print("cifra\tpublished\tderived\tverdict")
    if pub is None:
        for label, d in zip(("channel_u", "channel_b_survivors", "union_addresses"),
                            (u, b, union)):
            print(f"{label}\t--\t{d}\tNO-ANCHOR")
        sys.stderr.write(
            "🔴 p376-union-currency: NO ANCHOR. The live write-up states no "
            "`**N** channel-U addresses ... **M** channel-B survivors ... "
            "**K** addresses over both channels` sentence. `ACTION p375-A` made this figure "
            "STANDING precisely so it could not quietly stop being stated, which is how "
            "p349's denominator went unchecked for two passes.\n")
        return 1

    labels = ("channel_u", "channel_b_survivors", "union_addresses")
    stale = 0
    for label, p, d in zip(labels, pub, (u, b, union)):
        ok = p == d
        stale += 0 if ok else 1
        print(f"{label}\t{p}\t{d}\t{'MATCH' if ok else 'STALE'}")
    if stale:
        sys.stderr.write(
            f"🔴 p376-union-currency: {stale} of 3 union cells STALE. The live write-up's "
            "union census was derived BEFORE this pass wrote to the shelves. Re-derive with "
            "`make union-currency` as the LAST act before the commit and restate the "
            "sentence -- do not edit history to match.\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
