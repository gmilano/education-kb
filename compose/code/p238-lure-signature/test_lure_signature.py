#!/usr/bin/env python3
"""Controls for `P238-1`.

Runnable BOTH ways, which is `p355-cwd-portability`'s rule and the reason p229's
gate stayed a one-off: `python3 -I` strips the script's directory from sys.path, so
the directory is re-added explicitly here instead of being assumed.

The positive fixtures are reductions of READMEs p238 read first-hand off
raw.githubusercontent.com (`rockstar49summer/Moodle-Full-Version-Unlocked`, 11 604 B;
`mallyrix943/Google-Classroom-Full-Version`, 10 722 B).  The negative fixtures are
real rows p238 PUBLISHED, including 0-star ones, because a gate that fails those is
worse than no gate.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lure_signature import (  # noqa: E402
    badge_hit, classify, coldness_hit, funnel_hit, is_self_host, name_hit,
)

FAILS = []


def check(label, got, want):
    if got != want:
        FAILS.append("%s\n    got:  %r\n    want: %r" % (label, got, want))


# ---------------------------------------------------------------- fixtures

LURE_MOODLE = """# Moodle - Windows Edition | Latest Stable Release 2026

*Reviewed by the senior review board - Senior Software Analyst - Verified against the official source*

<img src="https://softyne.com/wp-content/uploads/moodle-9567-0.webp" width="80">

### DOWNLOAD LATEST STABLE RELEASE

[![DOWNLOAD LATEST STABLE RELEASE](https://softyne.com/wp-content/uploads/downloadlatestversion.svg)](https://softyne.com/moodle)

[![Version](https://www.softyne.com/wp-content/uploads/version.svg)]()
[![Platform](https://www.softyne.com/wp-content/uploads/platform.svg)]()
[![License](https://www.softyne.com/wp-content/uploads/license.svg)]()
[![Updated](https://www.softyne.com/wp-content/uploads/updated.svg)]()

See the [guide](https://softyne.com/moodle/#video-guide), [about us](https://softyne.com/about-us/)
and the [privacy policy](https://softyne.com/privacy-policy-2/).
"""

# A real project: badges on shields.io, links spread over its own registries and docs.
CLEAN_AIRBLACKBOX = """# AIR Blackbox

[![PyPI](https://img.shields.io/pypi/v/air-blackbox)](https://pypi.org/project/air-blackbox/)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Status](https://img.shields.io/badge/status-production-brightgreen)](https://github.com/airblackbox/airblackbox)

Open-source infrastructure for AI agents. See the [console](https://airblackbox.ai/console/scan),
the [MCP server](https://github.com/airblackbox/air-blackbox-mcp), the
[changelog](CHANGELOG.md) and [eval/competitors](eval/competitors/README.md).
Licence text at [apache.org](https://www.apache.org/licenses/LICENSE-2.0).
"""

# A genuine p238 row, 0 stars, 0 forks, pushed the same day.  MUST be CLEAR.
CLEAN_KOBA = """# koba

Agente para professores da SEDUC-SP: corrige as atividades de registro da
Educacao Profissional. Construido com Python.

Licenca: MIT - ver [LICENSE](LICENSE).
"""

# ---------------------------------------------------------------- predicate 1

check("name_hit flags Full-Version-Unlocked",
      name_hit("Moodle-Full-Version-Unlocked"), ["full-version", "unlocked"])
check("name_hit flags Google-Classroom-Full-Version",
      name_hit("Google-Classroom-Full-Version"), ["full-version"])
check("name_hit is case-insensitive",
      name_hit("CMAPTOOLS-UNLOCKED"), ["unlocked"])
check("name_hit clears a real repository", name_hit("airblackbox"), [])
check("name_hit clears a real education repo", name_hit("Cleison-Morais/koba"), [])
# A name may legitimately contain 'download' as a verb; only the compound fires.
check("name_hit does not fire on 'downloader'", name_hit("video-downloader"), [])

# ---------------------------------------------------------------- predicate 2

host, share, total = funnel_hit(LURE_MOODLE)
check("funnel_hit names the lure host", host, "softyne.com")
check("funnel_hit scores the lure at 100%", round(share, 2), 1.0)

host, share, total = funnel_hit(CLEAN_AIRBLACKBOX)
check("funnel_hit clears a real project", host, None)

# Short READMEs cannot be judged on link concentration; below min_links it abstains.
host, share, total = funnel_hit(CLEAN_KOBA)
check("funnel_hit abstains on a short README", host, None)
check("funnel_hit reports 0 countable links for koba", total, 0)

# www. and bare host are ONE host, not two - else a funnel splits and hides.
host, share, total = funnel_hit(
    "a https://x.com/1 b https://www.x.com/2 c https://x.com/3 "
    "d https://www.x.com/4 e https://x.com/5")
check("funnel_hit folds www. into the bare host", host, "x.com")
check("funnel_hit counts the folded links once", total, 5)

# ------------------------------------------- predicate 2b: the self-host exemption
# p238 measured this as the gate's ONLY false-positive mode: six real projects
# scored 60-93% concentration on their OWN documentation domains.  Controls are the
# six real hosts observed, plus the lure pair that must NOT be exempted.

check("self-host: docs.snath.ai belongs to snath-ai/lar",
      is_self_host("docs.snath.ai", "snath-ai/lar"), True)
check("self-host: ai-sdlc.io belongs to ai-sdlc-framework/ai-sdlc",
      is_self_host("ai-sdlc.io", "ai-sdlc-framework/ai-sdlc"), True)
check("self-host: attestix.io belongs to VibeTensor/attestix",
      is_self_host("attestix.io", "VibeTensor/attestix"), True)
check("self-host: arkforge.tech belongs to ark-forge/mcp-eu-ai-act",
      is_self_host("arkforge.tech", "ark-forge/mcp-eu-ai-act"), True)
check("self-host: owner github.io page is self",
      is_self_host("sattyamjjain.github.io", "sattyamjjain/agent-audit-kit"), True)
check("self-host: mixed-case owner github.io page is self",
      is_self_host("alexandrugirlea.github.io", "AlexandruGirlea/precommiteu"), True)

check("self-host: softyne.com is NOT the lure's own host",
      is_self_host("softyne.com", "rockstar49summer/Moodle-Full-Version-Unlocked"), False)
check("self-host: softyne.com is NOT the classroom lure's own host",
      is_self_host("softyne.com", "mallyrix943/Google-Classroom-Full-Version"), False)
check("self-host: a bare 'github' label never counts as self",
      is_self_host("github.io", "github-user/github-thing"), False)
check("self-host: abstains with no slug", is_self_host("x.com", None), False)
check("self-host: short names cannot match (no 3-letter collisions)",
      is_self_host("abc.com", "ab/abc"), False)

# The exemption must survive end-to-end: concentration on the project's own host
# produces CLEAR, while the same concentration on an unrelated host convicts.
OWN_DOCS = ("see " + " ".join("[d%d](https://docs.snath.ai/p%d)" % (i, i) for i in range(8)))
host, share, total = funnel_hit(OWN_DOCS, "snath-ai/lar")
check("funnel_hit exempts the project's own docs host", host, None)
host, share, total = funnel_hit(OWN_DOCS, "unrelated-owner/unrelated-repo")
check("funnel_hit still convicts the same links for a stranger", host, "docs.snath.ai")

# A forged badge on the project's own host is not a forgery.
check("badge_hit exempts a licence badge on the project's own host",
      badge_hit("![License](https://attestix.io/license.svg)", "VibeTensor/attestix"), [])
check("badge_hit still catches it for an unrelated owner",
      badge_hit("![License](https://attestix.io/license.svg)", "someone/else"),
      ["https://attestix.io/license.svg"])

# ---------------------------------------------------------------- predicate 3

badges = badge_hit(LURE_MOODLE)
check("badge_hit catches the forged licence badge",
      badges, ["https://www.softyne.com/wp-content/uploads/license.svg"])
check("badge_hit clears shields.io licence badges", badge_hit(CLEAN_AIRBLACKBOX), [])
check("badge_hit ignores non-licence remote images",
      badge_hit("![logo](https://example.com/logo.png)"), [])

# ---------------------------------------------------------------- predicate 4

check("coldness fires on 0/0/today", coldness_hit(0, 0, 0), True)
check("coldness fires at the 7-day edge", coldness_hit(0, 0, 7), True)
check("coldness stops after 7 days", coldness_hit(0, 0, 8), False)
check("coldness clears a starred repo", coldness_hit(24, 3, 0), False)
check("coldness clears a forked repo", coldness_hit(0, 2, 0), False)
check("coldness abstains without a push age", coldness_hit(0, 0, None), False)
check("coldness abstains on junk input", coldness_hit("x", "y", "z"), False)

# ---------------------------------------------------------------- verdicts

verdict, reasons = classify("Moodle-Full-Version-Unlocked", LURE_MOODLE, 0, 0, 0)
check("the Moodle lure is LURE", verdict, "LURE")
check("the Moodle lure reports all four reasons", len(reasons), 4)

verdict, _ = classify("airblackbox", CLEAN_AIRBLACKBOX, 24, 3, 1)
check("a real production repo is CLEAR", verdict, "CLEAR")

# THE control that matters most: a genuine 0-star row p238 published.
verdict, reasons = classify("koba", CLEAN_KOBA, 0, 0, 0)
check("a genuine 0-star LATAM row is CLEAR", verdict, "CLEAR")
check("coldness alone never produces a non-CLEAR verdict",
      [r for r in reasons if r.startswith("COLDNESS")] != [] and verdict == "CLEAR", True)

# One substantive predicate is SUSPECT, not LURE - a name alone is not a conviction.
verdict, _ = classify("some-tool-unlocked", CLEAN_KOBA, 50, 10, 30)
check("a name hit alone is SUSPECT", verdict, "SUSPECT")

# Two substantive predicates convict even with stars, so a bought-star lure still trips.
verdict, _ = classify("Pronote-Full-Version", LURE_MOODLE, 500, 90, 400)
check("name + funnel convicts despite stars and age", verdict, "LURE")

# Empty and None READMEs must not raise.
for bad in ("", None):
    verdict, _ = classify("whatever", bad, None, None, None)
    check("empty README (%r) is CLEAR, not a crash" % bad, verdict, "CLEAR")

# ---------------------------------------------------------------- report

TOTAL = 45
if FAILS:
    print("FAIL %d/%d" % (len(FAILS), TOTAL))
    for f in FAILS:
        print("  " + f)
    sys.exit(1)
print("PASS %d/%d controls - p238-lure-signature" % (TOTAL, TOTAL))
