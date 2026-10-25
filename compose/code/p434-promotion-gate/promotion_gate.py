#!/usr/bin/env python3
"""`p434-promotion-gate` — `Gap 433-A`: a curated shelf may not be MISSING what the
trending shelf already holds.

🔴 WHAT `Gap 433-A` SAID, AND WHY ITS PRESCRIBED REMEDY IS NOT WHAT THIS BUILDS.
`p433` declared the trending shelves write-only — append-only by contract, with **no
promotion path**, so an address enters at 20 ★, grows, and no instrument ever looks at it
again.  That diagnosis is 🟢 **confirmed and quantified** by this module.  Its prescribed
remedy was:

    a gate that takes every address in the trending shelves, reads its current star
    count, and fails when an address above a threshold (say 150 ★) carries a permissive
    grade and appears in NO curated shelf.

🔴 **That remedy is unbuildable here, for two independently measured reasons, and this
module implements the CORRECTED predicate instead.**

**Reason 1 — the star channel does not exist from inside a run.**  A star count is served
by `api.github.com` and by `github.com` HTML, and `p434` re-measured both at **HTTP 403**
through this environment's proxy (`codeload.github.com` likewise).  What answers is
`raw.githubusercontent.com` (200) and the git smart-HTTP transport (`ls-remote`).  This is
not new: `p228-shelf-gate/fetch_grants.sh` has carried the comment *"api.github.com and
github.com HTML are not"* for over two hundred passes.  🔵 **So `Gap 433-A` prescribed a
gate keyed on the one quantity no reachable channel serves**, and a `make` target cannot
obtain it at any worker count.

**Reason 2 — the threshold only ever suppresses true positives.**  `p434` graded the seven
trending-shelf addresses that are absent from every curated shelf and carry the most
traction.  Measured, payloads read first-hand:

| address | ★ | family | permissive? |
|---|---|---|---|
| `brycewang-stanford/Auto-Empirical-Research-Skills` | 4 771 | CC-BY-SA-4.0 | 🔴 no |
| `sitor-ai/frametell` | 400 | AGPL-3.0 | 🔴 no |
| `minicoohei/ai-agent-camp` | 346 | **NO-GRANT** | 🔴 no |
| `helixnow/deep-student` | 290 | AGPL-3.0 | 🔴 no |
| `ystemsrx/sql-to-ER` | 192 | AGPL-3.0 | 🔴 no |
| `wenflow-org/wenflow` | 59 | **MIT** | 🟢 yes |
| `zhangl1001/civil-ai` | 41 | **MIT** | 🟢 yes |

🔴 **Every address above `Gap 433-A`'s own 150 ★ threshold is non-permissive, and both
permissive ones are below it.**  So the prescribed predicate fires **0** times on the
population it was written for, while the star-free predicate fires **2**.  Traction and
permissiveness are *anti-correlated* in this domain's new supply, which is why a threshold
is the wrong instrument: it is a filter against exactly the rows a build-on shelf wants.

🟢 **THE CORRECTED PREDICATE, and the whole reason this gate can be blocking:**
*an address is a finding when its pinned grade is PERMISSIVE and it appears in no curated
shelf* — no star count, therefore fully offline, therefore admissible in `make hooks`.
`--predicate p433` keeps the refuted form runnable so the refutation stays reproducible
rather than becoming a claim in prose.

    make gate-promotion                  # offline controls + the live shelves, in `make hooks`
    promotion_gate.py census  <files>    # the unpromoted population, offline
    promotion_gate.py findings <files>   # the blocking arm alone

🟡 WHAT THIS DOES NOT CLAIM.  The gate judges the addresses that carry a **pinned grade**
in `grades.*.tsv`; every other unpromoted address is reported as `UNGRADED`, which is a
**REACH bound, not a defect count** (`p228`'s vocabulary, and its distinction).  Grading
the remainder is an ONLINE sweep and a later pass's work.  🔵 A finding is also not an
instruction to shelve: `UNPROMOTED-PERMISSIVE` says a permissive address this base already
recorded is absent from every build-on shelf, and whether it belongs there is a pass's
judgement — `p400-candidate-membership`'s question, not this gate's.

🔵 Addresses are compared CASE-FOLDED, because `p439-case-collision-gate` measured that
this corpus cites repositories under more than one spelling, and a promotion check that
folds one side and not the other reports a false finding.  Non-addresses are removed by
`p351-address-shape` rather than re-filtered here (`T108`: run this base's instruments).
"""
import collections
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "p351-address-shape"))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "p444-root-vs-tree-family"))
from address_shape import harvest, partition          # noqa: E402
from root_vs_tree import PERMISSIVE                   # noqa: E402

# The shelves a reader consults for something to BUILD ON.  An address absent from every
# one of these is absent from the recommendation surface, whatever the trend record says.
CURATED = ("agents/top.md", "repos/foundations.md", "verticals/solutions.md",
           "compose/patterns.md", "intel/market.md", "intel/trends.md")
TRENDING = ("agents/trending.md", "repos/trending.md")

# `Gap 433-A`'s own figure, kept so `--predicate p433` is the prescription and not a
# strawman of it.
P433_THRESHOLD = 150


def shelf_addresses(paths):
    """Shelf files -> set of folded addresses, non-addresses removed by `p351`."""
    addresses, _rejected = partition(harvest(paths))
    return addresses


def read_grades(path):
    """`grades.*.tsv` -> folded slug -> {family, stars, head, bytes, sha12, channel}."""
    grades = {}
    with open(path, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if not line.strip():
                continue
            row = dict(zip(header, line.rstrip("\n").split("\t")))
            grades[row["slug"].lower()] = row
    return grades


def unpromoted(trending, curated):
    """Folded addresses present in a trending shelf and in NO curated shelf."""
    return trending - curated


def findings(trending, curated, grades, predicate="p434"):
    """-> (findings, ungraded) where a finding is (slug, family, stars, class).

    `p434`  : PERMISSIVE and absent from every curated shelf.  No star count.
    `p433`  : `Gap 433-A` as prescribed — PERMISSIVE and stars >= 150.  Kept runnable.
    """
    out, ungraded = [], []
    for slug in sorted(unpromoted(trending, curated)):
        row = grades.get(slug)
        if row is None:
            ungraded.append(slug)
            continue
        fam = row.get("family", "")
        stars = int(row["stars"]) if row.get("stars", "").isdigit() else None
        if fam not in PERMISSIVE:
            continue
        if predicate == "p433":
            # The prescribed form.  A row whose star count is unknown cannot be judged
            # by it at all — which is the refutation, not a limitation of this code.
            if stars is None or stars < P433_THRESHOLD:
                continue
        out.append((slug, fam, stars, "UNPROMOTED-PERMISSIVE"))
    return out, ungraded


def main(argv):
    mode = "findings"
    if argv and argv[0] in ("census", "findings"):
        mode, argv = argv[0], argv[1:]
    grades_path = os.path.join(_HERE, "grades.2026-10-25.tsv")
    predicate = "p434"
    rest = []
    i = 0
    while i < len(argv):
        if argv[i] == "--predicate":
            predicate = argv[i + 1]
            i += 2
        elif argv[i] == "--grades":
            grades_path = argv[i + 1]
            i += 2
        else:
            rest.append(argv[i])
            i += 1
    # `P541` / `Gap 243` — an instrument that measures over the files it is GIVEN must
    # refuse an empty argument list rather than report success over nothing.
    if not rest:
        sys.stderr.write(
            "p434-promotion-gate: no repository root given — refusing to judge a "
            "promotion surface over nothing\n"
            "usage: promotion_gate.py [census|findings] <repo-root> "
            "[--predicate p434|p433] [--grades FILE]\n")
        return 2
    root = rest[0]
    curated = shelf_addresses([os.path.join(root, p) for p in CURATED
                               if os.path.exists(os.path.join(root, p))])
    trending = shelf_addresses([os.path.join(root, p) for p in TRENDING
                                if os.path.exists(os.path.join(root, p))])
    grades = read_grades(grades_path)
    found, ungraded = findings(trending, curated, grades, predicate)

    if mode == "census":
        print("cifra\tvalor")
        print(f"curated_addresses\t{len(curated)}")
        print(f"trending_addresses\t{len(trending)}")
        print(f"unpromoted\t{len(unpromoted(trending, curated))}")
        print(f"graded\t{len(grades)}")
        print(f"ungraded_reach_bound\t{len(ungraded)}")
        fams = collections.Counter(
            grades[s]["family"] for s in unpromoted(trending, curated) if s in grades)
        for fam, n in sorted(fams.items()):
            print(f"family:{fam}\t{n}")
        return 0

    print("slug\tfamily\tstars\tclass")
    for slug, fam, stars, cls in found:
        print(f"{slug}\t{fam}\t{'-' if stars is None else stars}\t{cls}")
    print(f"#\tfindings\t{len(found)}\tpredicate={predicate}")
    print(f"#\tungraded\t{len(ungraded)}\tREACH-BOUND-not-a-defect-count")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
