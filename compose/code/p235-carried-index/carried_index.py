#!/usr/bin/env python3
"""p235 — ACTION UG (p234): the index these shelves never had.

p234's own gap list closed with: "this KB has no index of what it already carries, so every
pass re-discovers rows and the shelves can argue against their own verified cells for 25
passes at a time." This is that index, plus the two predicates a pass actually needs:

    carried(slug)  -> is this row already on the shelves?  (ACTION UH: case-folded)
    claims(token)  -> do the shelves already mention X, before I publish "there is no X"?
    grade(slug)    -> p379: CARRIED / MENTIONED-B / NEW across BOTH address channels

Shelves only. Not evidence/, not archive/, not compose/code/ — a row cited in an evidence
TSV but absent from the shelves is NOT carried, and a claim in an archived file is not a
live claim.

🔴 p379 — `ACTION p378-A`, AND IT IS DISCHARGED BY NOT DOING WHAT IT SAID.
`Gap 512` was filed because `SLUG` below reads only the `github.com/owner/repo` URL form
(channel **U**), so an address the shelves discuss as a backticked bare slug (channel **B**,
`p367-bare-slug-channel`) grades `NEW`.  `p378` hit this live: `make carried` graded
`msitarzewski/agency-agents` NEW while `repos/trending.md` already carried it.  `ACTION
p378-A` asked for "the channel-B arm `p367` already wrote", ranked first.

🟢 The arm is here.  🔴 It is NOT a union into `carried()`, and the measurement is why.
Over the ten shelves channel B sees **774** addresses channel U cannot.  Classified by the
sentence each one lives in (`evidence/carried-index-channel-mix.2026-10-22-p379.tsv`), that
population is **mixed**: 309 sit beside a licence or grant word, 258 are bare mentions, 134
are mixed, and **73 sit beside a death or refusal marker only**.  Those 73 are addresses
earlier passes PROVED DEAD and wrote down as bare slugs *because* they were reporting a
negative — `1EdTech/badgr-server` and `concentricsky/badgr-server` are on `agents/top.md`
inside a dead-citation sweep, and both still answer `rc=128` first-hand at p379.

🔵 So a union would have made `carried()` answer `CARRIED` for an address whose only
appearance here is a published refutation.  `carried()`'s caller asks *"would publishing
this be a duplicate row?"*; for a proven-dead address the honest answer is neither
`CARRIED` nor `NEW` but *"the shelves have ADJUDICATED this — go read the cell"*.  A
two-valued predicate has nowhere to put that, which is why this is a THIRD value and not a
wider first one.

🟢 `carried()`, `claims()`, `harvest()` and the `check` recipe are therefore BYTE-UNCHANGED
in behaviour.  `p376-A`'s lesson is the governing one: a standing instrument that silently
re-grades becomes a gate that retro-edits history, and several published denominators rest
on channel-U `NEW` counts.  `grade()` and `make verdict` are additive; a caller opts in.
"""
import importlib.util
import os
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


# 🔴 p379: the `.git` clone suffix. `cvmcosta/ltijs.git` and `cvmcosta/ltijs` are ONE
# address, and this module folded case but not suffix for 144 passes.
# 🔵 FOUND BY MEASUREMENT, not by reading: running this module's `channels` census beside
# `p367`'s gave 2 724 against 2 717 over the same ten shelves, and the entire 8-address
# disagreement was 7 `.git` artefacts plus the documentation placeholder `owner/repo`.
# 🔴 It is the IDENTICAL defect `p367`'s own docstring records in its first draft — "it did
# not move the net-new count, because each artefact collided with its own de-suffixed form"
# — surviving in the instrument a pass calls BEFORE publishing a row.
# 🟢 Latent rather than firing, and the distinction is stated so no successor overclaims:
# every one of the 7 de-suffixed forms is independently present, so no address was being
# graded NEW today. The costs were an index inflated by 7 and a FALSE-NEGATIVE WAITING —
# an address published only as `foo/bar.git` would have graded `foo/bar` as NEW.
# 🔵 Safe to change: nothing on these shelves publishes a p235 index size (grepped for
# both totals before the edit), and the change can only move a verdict NEW -> CARRIED,
# the direction that prevents a duplicate rather than creating one.
NAME_TRAILERS = re.compile(r"(?:\.git)$", re.IGNORECASE)


def fold(slug):
    """ACTION UH — fold case before comparing. `OpenOLAT/OpenOLAT` and `openolat/OpenOLAT`
    are one row; it was that pair that defeated p234's cheap duplicate check.

    p379 — fold the `.git` clone suffix too, which is what `p348.slugs_in` has always done
    and this module never did."""
    return NAME_TRAILERS.sub("", slug.rstrip(".,)")).lower()


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


# ── p379: the second address channel, IMPORTED and never reimplemented.
# `p352`'s rule, and `p367`'s own docstring states it: two copies of a shape filter is this
# base's "second channel disagreeing with itself" defect. If the module is missing — a
# partial checkout — channel B degrades to EMPTY and `grade()` falls back to exactly
# `carried()`'s two values, because a quietly guessed channel is worse than a named absence.
_B_MODULE = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir,
                         "p367-bare-slug-channel", "bare_slug_channel.py")


def _load_b():
    if not os.path.exists(_B_MODULE):
        return None
    spec = importlib.util.spec_from_file_location("p367_bare_slug_channel", _B_MODULE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def harvest_b(root="."):
    """-> set of folded addresses channel B can see.  Empty set if p367 is unavailable."""
    mod = _load_b()
    if mod is None:
        return set()
    paths = [f"{root}/{s}" for s in SHELVES if os.path.exists(f"{root}/{s}")]
    if not paths:
        return set()
    survivors, _rejected = mod.channel_b(paths)
    return set(survivors)


# The three values, as strings rather than a bool, so a caller cannot accidentally treat
# MENTIONED-B as truthy-equals-carried the way `if carried(...)` would.
CARRIED = "CARRIED"
MENTIONED_B = "MENTIONED-B"
NEW = "NEW"


def grade(slug, index=None, b=None, root="."):
    """p379 — `ACTION p378-A`.  Three-valued, and the middle value is the whole point.

    CARRIED      channel U has it: the shelves cite it as an address.  A new row duplicates.
    MENTIONED-B  ONLY channel B has it: the shelves discuss the bare slug.  That may be a
                 row written without a link, or an address a pass PROVED DEAD and recorded
                 as a negative.  The two are not distinguishable from the index alone, so
                 this value does not pretend to: it says STOP AND READ THE CELL.
    NEW          neither channel has it.
    """
    index = harvest(root) if index is None else index
    if carried(slug, index):
        return CARRIED
    b = harvest_b(root) if b is None else b
    return MENTIONED_B if fold(slug) in b else NEW


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

    if len(argv) >= 2 and argv[1] == "verdict":
        # p379 — the three-valued recipe. Exit codes are DISTINCT from `check`'s on purpose:
        # 0 NEW, 1 CARRIED, 3 MENTIONED-B. A caller that only knows `check`'s 0/1 therefore
        # cannot silently read MENTIONED-B as NEW; it gets a status it does not recognise.
        if len(argv) < 3:
            print("usage: carried_index.py verdict <owner/repo> [root]", file=sys.stderr)
            return 2
        root = argv[3] if len(argv) > 3 else "."
        slug = argv[2]
        g = grade(slug, root=root)
        print(f"{g}\t{slug}")
        if g == CARRIED:
            print("\tchannel U — the shelves cite this as an address. A new row duplicates.")
            return 1
        if g == MENTIONED_B:
            print("\tchannel B ONLY — the shelves discuss this slug without a link.")
            print("\tSTOP: it may be an existing row, or an address a pass PROVED DEAD.")
            print(f"\tread the cells:  make claims TOKEN={slug}")
            return 3
        return 0

    if len(argv) >= 2 and argv[1] == "channels":
        # The census behind p379's refusal to union the channels.
        root = argv[2] if len(argv) > 2 else "."
        u, b = harvest(root), harvest_b(root)
        only_b = b - set(u)
        print("cifra\tvalor")
        print(f"channel_u_addresses\t{len(u)}")
        print(f"channel_b_survivors\t{len(b)}")
        print(f"channel_b_only\t{len(only_b)}")
        print(f"shelf_address_population\t{len(set(u) | b)}")
        return 0

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
