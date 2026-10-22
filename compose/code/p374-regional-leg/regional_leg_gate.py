#!/usr/bin/env python3
"""`gate-regional-leg` — the standing half of `p374`.  OFFLINE: it reads a committed table.

Four invariants, each one a figure or a failure this base has already paid for:

  `J1`  **The region vocabulary is closed.**  Five values, compared literally.
  `J2`  **A published regional NIL has TWO limbs** — the leg named a jurisdiction, AND a leg in
        another language was run for that same jurisdiction — **and an unsound nil must be
        marked WITHDRAWN.**  🔴 Replaces `I4` (`p372`), which had one limb, was satisfiable
        without naming a jurisdiction, and over-fired on Brazil.
  `J3`  **"Redundant" needs a fact-class test.**  Two productive legs are not substitutes.
  `J4`  **A verdict agrees with its own fact count.**

🟢 `p305`'s standing demand, obeyed: this rule is run over THIS BASE'S OWN recorded legs before
it is published as standing, and the suite below carries the negative control that matters —
removing Germany's in-language leg must turn `J2` RED for `p373`'s cell 2.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regional_leg import (  # noqa: E402
    REGIONS, names_a_jurisdiction, nil_is_admissible, nil_limbs,
    redundancy_is_admissible, region_is_in_vocabulary, verdict_is_consistent,
)

HERE = os.path.dirname(os.path.abspath(__file__))
LEGS = os.path.join(HERE, "legs.tsv")


def load_legs(path=LEGS):
    legs, header = [], None
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            if raw.startswith("#") or not raw.strip():
                continue
            cells = raw.rstrip("\n").split("\t")
            if header is None:
                header = cells
                continue
            row = dict(zip(header, cells))
            row["fact_count"] = int(row["fact_count"])
            row["placenames"] = [p for p in row["placenames"].split(";") if p]
            legs.append(row)
    return legs


def run(legs):
    """Return (failures, counts).  A failure is a tuple (invariant, leg_id, reason)."""
    failures, counts = [], {"J1": 0, "J2": 0, "J3": 0, "J4": 0}

    for leg in legs:
        counts["J1"] += 1
        if not region_is_in_vocabulary(leg["region"]):
            failures.append(("J1", leg["leg_id"],
                             "region %r is not in the closed vocabulary" % leg["region"]))

        counts["J4"] += 1
        ok, why = verdict_is_consistent(leg)
        if not ok:
            failures.append(("J4", leg["leg_id"], why))

        if leg["verdict"] == "NIL":
            counts["J2"] += 1
            ok, why = nil_is_admissible(leg, legs)
            if not ok:
                failures.append(("J2", leg["leg_id"], why))

    # 🔴 J3 is checked against the redundancy claims this base has actually PUBLISHED.
    # p373 published exactly one: that Portuguese is redundant for Brazil.
    for jurisdiction, language in PUBLISHED_REDUNDANCY_CLAIMS:
        counts["J3"] += 1
        ok, why = redundancy_is_admissible(jurisdiction, language, legs)
        if not ok:
            failures.append(("J3", "%s/%s" % (jurisdiction, language), why))

    return failures, counts


#: 🟢 Every "language X is redundant for jurisdiction Y" this base has published.
#: `p373`: "for Brazil an in-language leg is REDUNDANT".  Both Brazilian legs are productive and
#: both carry `policy-milestones`, so `J3` admits it — the claim was correct for Brazil.
#: 🔴 `p373` also generalised it; `J3` is what stops the generalisation reaching Japan, where the
#: same claim would be refused on fact class.
PUBLISHED_REDUNDANCY_CLAIMS = (("Brazil", "Portuguese"),)


def main():
    legs = load_legs()
    failures, counts = run(legs)
    print("── p374-regional-leg — %d legs, invariants J1-J4" % len(legs))
    for inv in ("J1", "J2", "J3", "J4"):
        print("   %s checked on %d" % (inv, counts[inv]))
    if failures:
        for inv, who, why in failures:
            print("   🔴 %s FAIL  %s  %s" % (inv, who, why))
        print("🔴 FAIL — %d violation(s)." % len(failures))
        return 1
    print("🟢 gate-regional-leg — J1 region vocabulary closed · "
          "J2 every published nil names a jurisdiction AND has an in-language sibling · "
          "J3 the one published redundancy claim survives a fact-class test · "
          "J4 every verdict agrees with its fact count")
    return 0


if __name__ == "__main__":
    sys.exit(main())
