#!/usr/bin/env python3
"""Offline controls for `p853-slug-presence`.

Every case below is a MEASURED one from this base, not a hypothetical:
the two failures `852-G3` recorded, plus the boundary cases that a naive
repair of either failure would then get wrong in the other direction.
"""
import os
import sys

# `python3 -I` strips the script's own directory from `sys.path`, which is the
# exact defect `p355-cwd-portability` recorded as the reason a working gate
# stayed a one-off: it could not be invoked from where a hook runs.  This suite
# is therefore runnable BOTH ways — `python3 test_presence.py` and
# `python3 -I compose/code/p853-slug-presence/test_presence.py`.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from presence import classify, patterns, _slug_parts, tier_of, verdict

FAIL = []


def check(name, got, want):
    if got != want:
        FAIL.append(f"🔴 {name}: got {got!r}, want {want!r}")
    else:
        print(f"🟢 {name}")


# ── (i) the UNDER-REPORTING failure: a bare slug with no URL ────────────────
# p852: a URL-keyed index called `weizhenFrank/AutoGrader` NEW while
# `agents/trending.md` already held it as a bare slug.
check("bare slug, no URL, is PRESENT",
      classify("weizhenFrank/AutoGrader", "| weizhenFrank/AutoGrader | no grant file |"), "bare")
# 🔵 The two arms are NOT redundant and NOT nested: the bare arm's look-behind
# rejects a preceding `/`, so it deliberately does not fire inside a URL path.
# A URL-only line therefore classifies `url`, and that is the whole reason the
# URL arm has to exist — the repair for p852's under-reporting cannot be "just
# use the bare pattern".
check("URL form alone classifies `url`, not `both`",
      classify("weizhenFrank/AutoGrader",
               "see https://github.com/weizhenFrank/AutoGrader for the probe"), "url")
check("raw.githubusercontent evidence line is PRESENT",
      classify("Halleck45/OpenPronounce",
               "byte-read https://raw.githubusercontent.com/Halleck45/OpenPronounce/main/LICENSE"), "url")

# ── (ii) the OVER-REPORTING failure: a longer name must not satisfy a shorter ─
# p852: `UOC/java-lti-1.3` is live and MIT; `UOC/java-lti-1.3-provider` is dead
# (`772-K31`).  A substring check transfers the dead sibling's 404 to the live row.
check("longer repo name does NOT satisfy shorter (the 772-K31 collapse)",
      classify("UOC/java-lti-1.3",
               "| UOC/java-lti-1.3-provider | 404 on both branches | dead |"), "absent")
check("the live sibling itself IS found",
      classify("UOC/java-lti-1.3-provider",
               "| UOC/java-lti-1.3-provider | 404 on both branches |"), "bare")
check("longer OWNER name does not satisfy shorter",
      classify("UOC/java-lti-1.3", "xUOC/java-lti-1.3 is a different account"), "absent")
check("same repo name under a different owner is NOT present",
      classify("johnswyou/autograder", "webtech-network/autograder is the sandboxed one"), "absent")

# ── boundary cases a naive repair of either direction then gets wrong ───────
check(".git suffix IS the same repository",
      classify("Mu-Y/mpl-mdd", "git clone https://github.com/Mu-Y/mpl-mdd.git"), "url")
check("a path UNDER the repo is still that repository",
      classify("Mu-Y/mpl-mdd", "https://github.com/Mu-Y/mpl-mdd/blob/main/LICENSE"), "url")
check("a sibling with a name-char suffix is NOT that repository",
      classify("Mu-Y/mpl-mdd", "https://github.com/Mu-Y/mpl-mdd-v2"), "absent")
check("case variance is the SAME repository (GitHub resolves case-insensitively)",
      classify("yuangongnd/GOPT", "https://github.com/YuanGongND/gopt"), "url")
check("case variance in the BARE form too",
      classify("yuangongnd/GOPT", "| yuangongnd/gopt | BSD-3-Clause |"), "bare")
check("a deeper path that merely CONTAINS the slug is not a bare hit",
      classify("owner/repo", "vendor/owner/repo/file.py"), "absent")
check("trailing punctuation does not hide a hit",
      classify("ai-zahran/E2E-R", "(https://github.com/ai-zahran/E2E-R), MIT"), "url")
check("markdown link text + target counts once as both forms",
      classify("Secondtonumb/IF-MDD",
               "[`Secondtonumb/IF-MDD`](https://github.com/Secondtonumb/IF-MDD)"), "both")
check("absent is absent",
      classify("nobody/nothing", "| webtech-network/autograder | Apache-2.0 |"), "absent")

# ── the parser accepts the forms this base actually writes addresses in ─────
check("parse bare", _slug_parts("a/b"), ("a", "b"))
check("parse url", _slug_parts("https://github.com/a/b"), ("a", "b"))
check("parse url with path", _slug_parts("https://github.com/a/b/tree/main"), ("a", "b"))
check("parse .git", _slug_parts("https://github.com/a/b.git"), ("a", "b"))

try:
    _slug_parts("notaslug")
except ValueError:
    print("🟢 a non-slug is refused rather than silently scanned")
else:
    FAIL.append("🔴 a non-slug was accepted")

# ── the FORM is retained, because collapsing it is what hid p852's failure ──
url, bare = patterns("a/b")
check("url pattern does not fire on a bare slug", bool(url.search("a/b")), False)
check("bare pattern does NOT fire inside a URL path — the arms are complementary, "
      "not nested, which is why removing either one re-opens 852-G3",
      bool(bare.search("https://github.com/a/b")), False)
check("bare pattern fires on a slug in a table cell",
      bool(bare.search("| a/b | MIT |")), True)

# ── the TIER arm: p852's taxonomy, made mechanical, plus the self-pollution
# this instrument created the first time it was run over the live corpus ─────
check("a shelf file is the GRADED tier", tier_of("agents/top.md"), "shelf")
check("foundations is a shelf", tier_of("repos/foundations.md"), "shelf")
check("verticals is a shelf", tier_of("verticals/solutions.md"), "shelf")
check("trending history is NOT a shelf", tier_of("agents/trending.md"), "history")
check("the gap ledger is history, not a shelf", tier_of("intel/open-gaps.md"), "history")
check("an instrument fixture is its OWN tier, never corpus presence",
      tier_of("compose/code/p853-slug-presence/test_presence.py"), "instrument")
check("shelf hit ⇒ SHELVED", verdict({"shelf", "history"}), "SHELVED")
check("history only ⇒ UNGRADED (p852 measured 13 of 17 in this state)",
      verdict({"history"}), "UNGRADED")
check("fixture only ⇒ FIXTURE-ONLY, NOT shelved and NOT new",
      verdict({"instrument"}), "FIXTURE-ONLY")
check("nothing ⇒ NEW", verdict(set()), "NEW")

print()
if FAIL:
    print("\n".join(FAIL))
    print(f"🔴 {len(FAIL)} control(s) FAILED")
    sys.exit(1)
print("🟢 p853-slug-presence: all controls pass, OFFLINE")
