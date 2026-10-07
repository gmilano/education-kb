#!/usr/bin/env python3
"""Controls for p448.  Offline: the corpus is a fixture, no fetch, no clone."""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from crossref import CORPUS_PATHS, citations_of  # noqa: E402

ok = 0
bad = []


def check(label, got, want):
    global ok
    if got == want:
        ok += 1
    else:
        bad.append("%s: got %r want %r" % (label, got, want))


# A fixture corpus: slug -> text of its manifests and README.
CORPUS = {
    "a/one": "deps: github.com/target/repo and https://github.com/Other/Thing",
    "b/two": "see [target/repo](https://github.com/target/repo) for details",
    "target/repo": "this is target/repo itself, the self-citation",
    "c/three": "we vendor TARGET/REPO under a different case",
    "d/four": "nothing relevant here at all",
    "e/five": "do not match target/repository or xtarget/repo or target/repo-extra",
}

# ---------------------------------------------------------------------------
# 1. the core match, and the boundary cases that a naive substring gets wrong
# ---------------------------------------------------------------------------
hits = citations_of("target/repo", CORPUS, "target/repo")
citers = {s for v in hits.values() for s in v}
check("finds both plain citers", {"a/one", "b/two"} <= citers, True)
check("finds the case variant too", "c/three" in citers, True)
check("SELF is excluded", "target/repo" not in citers, True)
check("no citation from the unrelated repo", "d/four" not in citers, True)

# `e/five` is the whole reason the regex has look-arounds: `target/repository`,
# `xtarget/repo` and `target/repo-extra` all CONTAIN `target/repo` as a substring and
# none of them is a citation of it.  A plain `in` test would count this repo.
check("rejects longer-repo, longer-owner and suffixed forms", "e/five" not in citers,
      True)

# and the spellings are reported SEPARATELY, which is what makes a disagreement visible
check("both spellings are recorded", set(hits), {"target/repo", "TARGET/REPO"})

# ---------------------------------------------------------------------------
# 2. calibration: the channel must discriminate before a negative is a claim (P249)
# ---------------------------------------------------------------------------
planted = citations_of("globant-kb-p448/this-slug-does-not-exist", CORPUS,
                       "globant-kb-p448/this-slug-does-not-exist")
check("planted slug has no citers", planted, {})
# the positive half of the same control: a slug that IS there must be found, otherwise
# "0 citers" below would be indistinguishable from a broken matcher
check("a present slug IS found", bool(citations_of("Other/Thing", CORPUS,
                                                   "Other/Thing")), True)

# ---------------------------------------------------------------------------
# 3. the self-exclusion must actually CHANGE a case, or it is decoration
# ---------------------------------------------------------------------------
with_self = citations_of("target/repo", CORPUS, "nobody/nothing")
check("without self-exclusion the self-citation IS counted",
      "target/repo" in {s for v in with_self.values() for s in v}, True)
check("...and excluding it removes exactly that one",
      len({s for v in with_self.values() for s in v})
      - len({s for v in hits.values() for s in v}), 1)

# ---------------------------------------------------------------------------
# 4. the independence premise this pass had to retract
# ---------------------------------------------------------------------------
# The action framed 495 neighbours as "independent spellings by third parties".  Five of
# the 13 real citations came from the SAME OWNER one repository over, which is not a
# third party.  The owner test is the measurement that showed it, so it is asserted.
def same_owner(a, b):
    return a.split("/")[0].lower() == b.split("/")[0].lower()


check("same-owner pair detected", same_owner("ink-waffle/moodle-mcp",
                                             "ink-waffle/sisu-mcp"), True)
check("different-owner pair detected", same_owner("KualiCo/rice", "kuali/rice"), False)
# NEGATIVE: the owner test must not be fooled by case, or the 5 would have been 3
check("owner test is case-insensitive", same_owner("CAHLR/OATutor-Content",
                                                   "cahlr/OATutor"), True)

# ---------------------------------------------------------------------------
# 5. the corpus definition is part of the measurement (P107)
# ---------------------------------------------------------------------------
check("corpus path list is non-empty and published", len(CORPUS_PATHS) >= 16, True)
for p in ("README.md", "package.json", "pyproject.toml", "pom.xml", "composer.json"):
    check("corpus covers %s" % p, p in CORPUS_PATHS, True)
# a citation in a file NOT on the list is invisible, and that is a declared limit:
# asserting it keeps the limit honest rather than letting it be forgotten
check("a path not on the list is not consulted", "CITATION.cff" in CORPUS_PATHS, False)

print("p448 controls: %d/%d" % (ok, ok + len(bad)))
for b in bad:
    print("  FAIL", b)
sys.exit(1 if bad else 0)
