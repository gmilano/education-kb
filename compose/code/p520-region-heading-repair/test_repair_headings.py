"""Controls for the P383 region-heading REPAIR tool. Runs from the repo root and from here."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from repair_headings import plan, apply_plan, owning_pass

BARE = "## Opportunities by region"


def mk(*rows):
    return list(rows)


CLEAN = mk(
    "## 🆕 `p520` — today",
    "text",
    BARE,
    "### North America",
    "## 🆕 `p519` — yesterday",
    "## Opportunities by region — `p519`",
)

REGRESSED = mk(
    "## 🆕 `p520` — today",
    BARE,
    "### North America",
    "## 🆕 `p519` — yesterday",
    BARE,                      # the regression: p519's heading left bare
    "### EMEA",
    "## 🆕 `p518` — before",
    BARE,                      # and p518's too
)

# 🔴 A later bare heading with NO `pNNN` marker anywhere above it. The first bare heading is
# always kept regardless, so the orphan has to be the SECOND one for the refusal to be tested.
ORPHAN = mk(
    "intro prose, no pass marker",
    BARE,                      # kept (first)
    BARE,                      # orphan: nothing above it names a pass
)

NONE_AT_ALL = mk("## 🆕 `p520`", "no canonical block here")


def main():
    failures, n = [], 0

    # A clean file needs no repair and keeps the first heading.
    keep, repairs, unrep = plan(CLEAN)
    n += 1
    if keep != 2:
        failures.append("CLEAN: kept line %r, expected index 2" % keep)
    n += 1
    if repairs:
        failures.append("CLEAN: proposed %d repairs on a clean file" % len(repairs))
    n += 1
    if unrep:
        failures.append("CLEAN: reported unrepairable on a clean file")

    # The regression: two later bare headings, demoted to their OWNING passes.
    keep, repairs, unrep = plan(REGRESSED)
    n += 1
    if keep != 1:
        failures.append("REGRESSED: kept %r, expected 1 (the newest)" % keep)
    n += 1
    if len(repairs) != 2:
        failures.append("REGRESSED: %d repairs, expected 2" % len(repairs))
    n += 1
    if [p for _, _, p in repairs] != ["p519", "p518"]:
        failures.append("REGRESSED: wrong owners %r" % [p for _, _, p in repairs])
    n += 1
    if unrep:
        failures.append("REGRESSED: nothing should be unrepairable here")

    # Applying the plan must leave EXACTLY one bare heading, and be idempotent.
    fixed = apply_plan(REGRESSED, repairs)
    n += 1
    if sum(1 for l in fixed if l.strip() == BARE) != 1:
        failures.append("REGRESSED: after repair, bare count != 1")
    n += 1
    _, again, _ = plan(fixed)
    if again:
        failures.append("REGRESSED: not idempotent, %d repairs still pending" % len(again))

    # 🔴 The refusal control: a bare heading with no pass marker above it is NOT guessed.
    keep, repairs, unrep = plan(ORPHAN)
    n += 1
    if keep != 1:
        failures.append("ORPHAN: kept %r, expected 1" % keep)
    n += 1
    if len(unrep) != 1:
        failures.append("ORPHAN: %d unrepairable, expected 1" % len(unrep))
    n += 1
    if repairs:
        failures.append("ORPHAN: guessed a pass id for an orphan heading")

    # No canonical block at all is a distinct outcome from a clean one.
    n += 1
    if plan(NONE_AT_ALL)[0] is not None:
        failures.append("NONE_AT_ALL: should report no canonical block")

    # owning_pass reads the NEAREST marker above, not the first in the file.
    n += 1
    if owning_pass(REGRESSED, 4) != "p519":
        failures.append("owning_pass: %r, expected p519" % owning_pass(REGRESSED, 4))
    n += 1
    if owning_pass(REGRESSED, 7) != "p518":
        failures.append("owning_pass: %r, expected p518" % owning_pass(REGRESSED, 7))

    print("controls: %d/%d green" % (n - len(failures), n))
    for f in failures:
        print("  FAIL", f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
