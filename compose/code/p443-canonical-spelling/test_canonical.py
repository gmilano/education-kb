#!/usr/bin/env python3
"""Offline controls for p443. `matching_spelling` and the denominator are pure.

Rule 2 of P126: each positive is paired with the false positive that would make the
output unreadable. Three controls exist because the first build published the row they
forbid.

Run: python3 test_canonical.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p439-case-collision-gate"))
import canonical as c  # noqa: E402

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append("%s: got %r want %r" % (label, got, want))


# --- matching_spelling: find the slug, in the spelling the TEXT uses ----------
check("a plain self-link gives the publisher's spelling",
      c.matching_spelling("See https://github.com/LearningEquality/kolibri for docs.",
                          "learningequality/kolibri"),
      "LearningEquality/kolibri")
check("the search is case-insensitive but the ANSWER keeps the text's case",
      c.matching_spelling("https://github.com/NVIDIA/NeMo", "nvidia/nemo"),
      "NVIDIA/NeMo")
check("a shields.io badge carries the slug in the publisher's spelling too",
      c.matching_spelling(
          "![stars](https://img.shields.io/github/stars/Sunbird-Ed/SunbirdEd-mobile-app)",
          "sunbird-ed/sunbirded-mobile-app"),
      "Sunbird-Ed/SunbirdEd-mobile-app")
check("a codecov badge works the same way",
      c.matching_spelling("https://codecov.io/gh/OpenEMIS/core/branch/main",
                          "openemis/core"), "OpenEMIS/core")
check("a clone URL is the same repository, not a different spelling",
      c.matching_spelling("git+https://github.com/KualiCo/rice.git", "kualico/rice"),
      "KualiCo/rice")

# --- the negatives -----------------------------------------------------------
check("a link to a DIFFERENT repository is not this repository's self-link",
      c.matching_spelling("Forked from https://github.com/kuali/rice",
                          "kualico/rice"), None)
check("an empty document yields no spelling rather than a guess",
      c.matching_spelling("", "owner/repo"), None)
check("a github.com SITE path is not a repository",
      c.matching_spelling("https://github.com/search/repositories?q=lms",
                          "search/repositories"), None)
check("a topic page is not a repository",
      c.matching_spelling("https://github.com/topics/edtech", "topics/edtech"), None)
# The control that stops a prefix match: `owner/repo-two` must not answer for
# `owner/repo`.  Without it a sweep over 495 slugs silently cross-matches siblings.
check("a longer repository name is not this one",
      c.matching_spelling("https://github.com/learningequality/kolibri-design-system",
                          "learningequality/kolibri"), None)
check("and the shorter one is not the longer one either",
      c.matching_spelling("https://github.com/learningequality/kolibri",
                          "learningequality/kolibri-design-system"), None)

# --- the denominator is p439's, imported, not re-derived ---------------------
check("the live file list is the one p439 gates, so the two cannot drift",
      c.LIVE, ["agents/top.md", "repos/foundations.md", "verticals/solutions.md",
               "intel/market.md", "intel/trends.md", "compose/patterns.md"])
check("the append-only histories are deliberately NOT scanned",
      any("trending" in f for f in c.LIVE), False)
check("normalise is p439's too", c.normalise("Unicon/tool13demo.git"),
      "Unicon/tool13demo")

# --- scope: a zero denominator is a path fault, not a clean shelf (P355) ------
r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "canonical.py"),
                    os.path.join(HERE, "no-such-directory")],
                   capture_output=True, cwd=HERE)
check("exits 2 when the shelf root is wrong, rather than printing a clean sweep",
      r.returncode, 2)

TOTAL = 15
if FAIL:
    print("FAIL (%d of %d)" % (len(FAIL), TOTAL))
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("%d/%d assertions pass, no network" % (TOTAL, TOTAL))
