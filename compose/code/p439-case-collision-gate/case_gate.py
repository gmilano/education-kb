#!/usr/bin/env python3
"""p439 — two spellings of one repository compile to two entities.

GitHub resolves `owner/repo` case-insensitively, so
`github.com/LearningEquality/kolibri` and `github.com/learningequality/kolibri`
serve the same repository and both links work in a browser. A compiler keying
entities on the reference string does not: it emits two, with two licences, two
dates and two star counts to keep in sync, and a filter on either one silently
misses the rows written under the other.

Measured on 2026-10-07, before this gate existed: **9 of 496** distinct
case-insensitive slugs in the six non-append-only shelf files were written both
ways -- 18 references for 9 repositories.

Resolving the canonical spelling, in priority order, because "pick the prettier
one" is how the next collision gets introduced:

  1. the **package registry's declared homepage** for a package the repo
     publishes (`pypi.org`/`registry.npmjs.org` -> `learningequality/kolibri`);
  2. the repository's **own self-link** in `README.md` or `package.json`
     (-> `Sunbird-Ed/SunbirdEd-mobile-app`, `OpenEMIS/core`, `AI-EDU-LAB/E-EVAL`);
  3. failing both, the spelling the KB already uses most, recorded as a majority
     decision rather than as evidence (`KualiCo/rice`, `Unicon/tool13demo`).

The append-only files are NOT scanned. History records the spelling that was
published, and editing it would be the error this KB forbids elsewhere.

Exit 1 on any collision, so this runs as a gate.
"""
import collections
import os
import re
import sys

REF = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
# `github.com/search/repositories` is a site path, not a repository, and
# `github.com/owner/repo.git` is the clone URL of `owner/repo`.  Counting either
# as its own slug inflates the denominator and, worse, would let `x` and `x.git`
# be reported as a case collision they are not.
RESERVED = {"search", "topics", "orgs", "features", "about", "sponsors",
            "collections", "settings", "apps", "marketplace", "login", "signup",
            "new", "explore", "pricing", "enterprise", "security"}


def normalise(slug):
    """The repository a reference names, or None if it names no repository."""
    owner, _, repo = slug.partition("/")
    if owner.lower() in RESERVED:
        return None
    if repo.endswith(".git"):
        repo = repo[:-4]
    return f"{owner}/{repo}" if repo else None
LIVE = ["agents/top.md", "repos/foundations.md", "verticals/solutions.md",
        "intel/market.md", "intel/trends.md", "compose/patterns.md"]


def collisions(root):
    seen = collections.defaultdict(lambda: collections.defaultdict(list))
    for rel in LIVE:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                for m in REF.finditer(line):
                    s = normalise(m.group(1))
                    if s is None:
                        continue
                    seen[s.lower()][s].append(f"{rel}:{n}")
    return {k: v for k, v in seen.items() if len(v) > 1}, len(seen)


def main():
    # Three levels up: compose/code/p439-case-collision-gate -> compose/code ->
    # compose -> the repository root.  The first build used two and the gate
    # reported "0 distinct slugs", which reads as a clean run and is not one --
    # the failure mode P355 exists to name.
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
    coll, total = collisions(root)
    print(f"distinct case-insensitive slugs in the live files: {total}")
    # A zero denominator is a path fault, not a clean tree, and must not exit 0.
    if total == 0:
        print(f"ERROR: no references found under {root!r} -- wrong root, not a clean run")
        return 2
    if not coll:
        print("0 findings: every repository is cited under exactly one spelling")
        return 0
    print(f"{len(coll)} FINDINGS -- one repository, more than one spelling:")
    for k, v in sorted(coll.items()):
        print(f"  {k}")
        for spelling, where in sorted(v.items()):
            print(f"      {spelling:60} {', '.join(where[:4])}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
