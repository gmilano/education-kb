#!/usr/bin/env python3
"""Offline control for the p445 publisher classifier.

The classifier is the pass's binding error term (`P5`), so it gets a control that encodes
the FALSE POSITIVES hand-labelling actually found, not a set of cases it was built to pass.
"""
import os, sys

# Works under `python3 -I` too, which drops the script's own directory from sys.path.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from publisher_class import classify

CASES = [
    # (owner, expected_class, why)
    # ── Tier B: named institutional orgs ──────────────────────────────────────────────
    ("IFRN",            "INSTITUTIONAL", "Instituto Federal do RN, operates SUAP"),
    ("ifrn-oficial",    "INSTITUTIONAL", "same institution, official org"),
    ("unal",            "INSTITUTIONAL", "Universidad Nacional de Colombia"),
    ("usp",             "INSTITUTIONAL", "Universidade de Sao Paulo"),
    ("inria",           "INSTITUTIONAL", "French national research institute"),
    ("illinois",        "INSTITUTIONAL", "University of Illinois org"),
    # ── Tier A: institution words ─────────────────────────────────────────────────────
    ("universita-di-ferrara",      "INSTITUTIONAL", "spelled-out university"),
    ("Harvard-University-iCommons","INSTITUTIONAL", "university central IT"),
    ("groton-school",              "INSTITUTIONAL", "a school"),
    ("Lawrence-Public-Schools",    "INSTITUTIONAL", "a district"),
    # ── The false positives hand-labelling found. These are the REGRESSION cases. ─────
    # Each one is currently misclassified; the test ASSERTS the known-bad behaviour so a
    # successor who tightens the classifier sees these flip, rather than discovering the
    # contamination again from scratch.
    ("UniversalDependencies", "INSTITUTIONAL", "FALSE POSITIVE: `univ` inside the name"),
    ("EscolaLMS",             "INSTITUTIONAL", "FALSE POSITIVE: an LMS vendor"),
    ("schoolutils",           "INSTITUTIONAL", "FALSE POSITIVE: a dev utility org"),
    ("schoolyardsms",         "INSTITUTIONAL", "FALSE POSITIVE: an SMS product"),
    # ── Plainly non-institutional ─────────────────────────────────────────────────────
    ("macielti",          "NON-INSTITUTIONAL", "an individual"),
    ("fernandobrito",     "NON-INSTITUTIONAL", "an individual"),
    ("ivmelo",            "NON-INSTITUTIONAL", "an individual"),
    ("sebassg",           "NON-INSTITUTIONAL", "an individual"),
    ("moodle",            "NON-INSTITUTIONAL", "the PROJECT, not an institution"),
    ("openedx",           "NON-INSTITUTIONAL", "the PROJECT, not an institution"),
    ("HKUDS",             "NON-INSTITUTIONAL", "a lab acronym NOT on the allowlist -- "
                                               "the recall limit, stated"),
]

FALSE_POSITIVES = {"universaldependencies", "escolalms", "schoolutils", "schoolyardsms"}


def main():
    fails = 0
    for owner, expected, why in CASES:
        got, tier = classify(owner)
        ok = got == expected
        if not ok:
            fails += 1
        flag = "FP" if owner.lower() in FALSE_POSITIVES else "  "
        print(f"{'ok  ' if ok else 'FAIL'} {flag} {owner:30s} -> {got:18s} (tier {tier}) {why}")
    print()
    print(f"{len(CASES)-fails}/{len(CASES)} pass")
    print(f"known false positives asserted: {len(FALSE_POSITIVES)} "
          f"-> hand-measured precision 27/36 = 75.0%")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
