#!/usr/bin/env python3
"""p371 — `Gap 477`'s denominator, derived rather than asserted.

`Gap 477` (p370) reads: "63 of the 2 311-address promotion backlog are now graded from
payload; 2 248 are not."  That figure was published WITHOUT a committed list, so the next
pass has to re-derive the set before it can grade an element of it.  This builds the list
and writes it down, so `Gap 477`'s remainder is auditable instead of restated.

THE BACKLOG, defined:
    cited on a RESEARCH shelf (agents/trending.md, repos/trending.md)
      minus carried on a LIVE shelf (top, foundations, solutions, patterns, market,
                                     trends, open-gaps, README.md)
      minus already graded first-hand by p370's probe

`p351`'s shape rule is reused, not reimplemented: an address that fails `address_shape`
is not an address and never enters the denominator.
"""
import os
import re
import sys
import pathlib

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

# 🟢 The shelf list is IMPORTED from `p235`'s committed index, never restated here.
# 🔵 That is this pass's own lesson applied to itself: `p371` re-derived two disciplines
# `p115` had already committed, because they had been copied rather than reused, and a
# copied table drifts.  `RESEARCH` is the two append-only research shelves; `LIVE` is
# every other shelf `p235` knows about, so adding a shelf there reaches this instrument
# without anyone remembering to edit it.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "p235-carried-index"))
from carried_index import SHELVES  # noqa: E402

RESEARCH = ["agents/trending.md", "repos/trending.md"]
LIVE = [shelf for shelf in SHELVES if shelf not in RESEARCH]

SLUG = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

# p351's classes, restated as a predicate.  A tree path, a .git suffix and a badge host
# are not repository addresses, and p351 measured 33 of them in this corpus.
NOT_A_REPO_NAME = {"blob", "tree", "raw", "releases", "issues", "pull", "pulls", "commit",
                   "commits", "wiki", "actions", "topics", "search", "orgs", "sponsors",
                   "settings", "notifications", "apps", "features", "about", "pricing"}
# 🔵 These are GitHub's own reserved first-path-segments, and GitHub treats them
# case-insensitively, so the membership test folds.  The fold sits HERE, beside the
# vocabulary it protects, because `p283`'s ladder audit is right that a fold somewhere
# else in a 200-line file protects nothing — its own first draft claimed immunity for
# 316 of 580 ladders on exactly that reasoning.
NOT_AN_OWNER = {"topics", "search", "orgs", "sponsors", "settings", "features", "about",
                "pricing", "login", "join", "marketplace", "collections", "trending",
                "readme", "explore", "notifications", "new", "codespaces"}


def _reserved_owner(owner):
    return owner.lower() in NOT_AN_OWNER


def _reserved_repo_name(repo):
    return repo.lower() in NOT_A_REPO_NAME


def fold(slug):
    return slug.rstrip(".,)").lower()


def shape_ok(slug):
    slug = slug.rstrip(".,)")
    if slug.count("/") != 1:
        return False
    owner, repo = slug.split("/")
    if not owner or not repo:
        return False
    if _reserved_owner(owner) or _reserved_repo_name(repo):
        return False
    if repo.lower().endswith(".git"):
        return False
    # 🔴 D1, found by this instrument's own first run: `.../archive` passed every test
    # above.  A GitHub name cannot begin with a dot and cannot contain `..`; the string
    # came from a RELATIVE PATH in prose, not from a URL.
    for part in (owner, repo):
        if part.startswith(".") or ".." in part or part.strip(".") == "":
            return False
    # p348: a folded collision is still one address; casing is handled by fold()
    return True


def harvest(files):
    out = {}
    for shelf in files:
        p = ROOT / shelf
        if not p.exists():
            continue
        for raw in SLUG.findall(p.read_text(encoding="utf-8", errors="replace")):
            raw = raw.rstrip(".,)")
            if not shape_ok(raw):
                continue
            out.setdefault(fold(raw), set()).add(raw)
    return out


def main():
    research = harvest(RESEARCH)
    live = harvest(LIVE)

    graded = set()
    p370 = ROOT / "compose/code/p370-git-tree-payload/slugs.2026-10-21-p370.txt"
    if p370.exists():
        for line in p370.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                graded.add(fold(line))

    backlog = {k: v for k, v in research.items() if k not in live and k not in graded}

    sys.stderr.write(
        f"# research-shelf addresses (folded, shape-valid)\t{len(research)}\n"
        f"# carried on a live shelf\t{len(live)}\n"
        f"# already graded by p370's probe\t{len(graded)}\n"
        f"# BACKLOG (Gap 477 remainder)\t{len(backlog)}\n")

    # One canonical spelling per folded address: the most frequent casing wins, ties
    # broken lexically so the list is reproducible byte-for-byte.
    for k in sorted(backlog):
        print(sorted(backlog[k])[0])


if __name__ == "__main__":
    main()
