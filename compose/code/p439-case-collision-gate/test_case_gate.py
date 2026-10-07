#!/usr/bin/env python3
"""Controls for p439. Offline; writes its fixtures to a temp tree."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from case_gate import collisions

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append(label)
        print(f"FAIL {label}: got {got!r}, want {want!r}")
    else:
        print(f"PASS {label}")


def tree(files):
    d = tempfile.mkdtemp(prefix="p439.")
    for rel, body in files.items():
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
    return d


# POSITIVE: the real 2026-10-07 case, across two files, as it was found.
d = tree({
    "agents/top.md": "| [`LearningEquality/kolibri`](https://github.com/learningequality/kolibri) |\n",
    "repos/foundations.md": "see [LearningEquality/kolibri](https://github.com/LearningEquality/kolibri)\n",
})
c, n = collisions(d)
check("positive: one repo, two spellings, two files -> 1 finding", len(c), 1)
check("positive: both spellings are reported",
      sorted(c["learningequality/kolibri"]), ["LearningEquality/kolibri", "learningequality/kolibri"])

# NEGATIVE 1: the same repo cited many times, one spelling -> clean. Without this,
# a gate that flagged every repeated reference would also pass the positive.
d = tree({
    "agents/top.md": "a https://github.com/learningequality/kolibri b "
                     "https://github.com/learningequality/kolibri\n",
    "repos/foundations.md": "https://github.com/learningequality/kolibri\n",
})
c, n = collisions(d)
check("negative: one spelling, three references -> 0 findings", len(c), 0)

# NEGATIVE 2: two genuinely different repos whose names differ only after a prefix.
# `kuali/rice` and `KualiCo/rice` are DIFFERENT OWNERS and different repositories
# (head commits 2017-05-17 and 2020-07-01). A gate that compared loosely would
# merge them and demand one be "corrected" into the other.
d = tree({"agents/top.md": "https://github.com/kuali/rice and https://github.com/KualiCo/rice\n"})
c, n = collisions(d)
check("negative: kuali/rice vs KualiCo/rice are two repositories, not a collision", len(c), 0)

# NEGATIVE 3: the append-only files are OUT OF SCOPE by construction.
d = tree({
    "agents/top.md": "https://github.com/learningequality/kolibri\n",
    "agents/trending.md": "https://github.com/LearningEquality/kolibri\n",
    "repos/trending.md": "https://github.com/LearningEquality/kolibri\n",
})
c, n = collisions(d)
check("negative: a spelling that survives only in append-only history is not a finding", len(c), 0)

# NEGATIVE 4: repo-name case, not just owner case, is still a collision.
d = tree({
    "agents/top.md": "https://github.com/Sunbird-Ed/SunbirdEd-mobile-app\n",
    "intel/trends.md": "https://github.com/sunbird-ed/sunbirded-mobile-app\n",
})
c, n = collisions(d)
check("positive: the REPO name's case counts too", len(c), 1)

# NEGATIVE 5: an empty tree yields a ZERO DENOMINATOR, and the gate must not
# read that as clean.  The first build pointed two directories up instead of
# three, found nothing, and printed "0 findings" over the real repository.
d = tree({"notes.txt": "nothing here\n"})
c, n = collisions(d)
check("negative: an empty denominator is reported as 0 slugs, not as 0 findings", n, 0)

# NEGATIVE 6/7: the denominator must count REPOSITORIES, not reference strings.
d = tree({"agents/top.md":
          "https://github.com/search/repositories?q=lti and "
          "https://github.com/ucfopen/pylti1.3.git and "
          "https://github.com/ucfopen/pylti1.3\n"})
c, n = collisions(d)
check("negative: a site path is not a repository", n, 1)
check("negative: owner/repo.git is the SAME repository as owner/repo", len(c), 0)

TOTAL = 9
if FAIL:
    print(f"\nFAIL ({len(FAIL)} of {TOTAL})")
    sys.exit(1)
print(f"\n{TOTAL}/{TOTAL} assertions pass, no network")
