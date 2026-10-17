#!/usr/bin/env python3
"""Controls for `pass259-grant-location-class`.

Every fixture is a payload READ FIRST-HAND at `p259` over `raw.githubusercontent.com`
on an `ls-remote`-resolved ref, or — for `addheader.php` — out of a shallow clone of
the repository that ships it.  No excerpt is hand-typed:

  bycs-lp-quizaccess_ai-version.php      bycs-lp/moodle-quizaccess_ai @ main
  jeanlucio-quickpoll-version.php        jeanlucio/moodle-mod_quickpoll @ main
  jeanlucio-dev-tools-addheader.php      jeanlucio/moodle-dev-tools @ main
  os4ed-opensis-index.php                OS4ED/openSIS-Classic @ master   (45 523 B)
  os4ed-opensis-docs-License.txt         OS4ED/openSIS-Classic @ master   (17 286 B)
  frappe-education-license.txt           frappe/education @ develop       (19 B)
  nextcloud-live_transcription-info.xml  nextcloud/live_transcription @ master
  nextcloud-talk_bot_ai-info.xml         nextcloud/talk_bot_ai @ main
  imsglobal-placeholder-README.md        imsglobal/imsglobal.github.io @ main (85 B)

🔴 Run from this directory.  `python3 -I` strips the script's own directory from
`sys.path` (p229), which is why every Makefile recipe `cd`s into the instrument.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p222-ecosystem-bound-grammar"))

import grant_location as gl  # noqa: E402
from bound_grammar import read_bound  # noqa: E402

FIX = os.path.join(HERE, "fixtures-p259")

FAILURES = []
MISSING = []
CHECKS = 0


def check(label, got, want):
    global CHECKS
    CHECKS += 1
    if got != want:
        FAILURES.append(f"{label}: got {got!r}, want {want!r}")


def payload(name):
    path = os.path.join(FIX, name)
    if not os.path.exists(path):
        MISSING.append(name)
        return None
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


MOODLE = payload("bycs-lp-quizaccess_ai-version.php")
QUICKPOLL = payload("jeanlucio-quickpoll-version.php")
ADDHEADER = payload("jeanlucio-dev-tools-addheader.php")
OPENSIS_CODE = payload("os4ed-opensis-index.php")
OPENSIS_FILED = payload("os4ed-opensis-docs-License.txt")
FRAPPE = payload("frappe-education-license.txt")
NC_LIVE = payload("nextcloud-live_transcription-info.xml")
NC_BOT = payload("nextcloud-talk_bot_ai-info.xml")
PLACEHOLDER = payload("imsglobal-placeholder-README.md")

# ── 1. The dual path.  `version.php` is a MANIFEST by name and a CODE-HEADER by ───
#       content, and the class must follow the CONTENT when there is one.
check("version.php with no body is read as a manifest, as the ladder files it",
      gl.location_class("version.php"), gl.LOC_ECOSYSTEM_MANIFEST)
check("version.php WITH a Moodle grant header is a code header",
      gl.location_class("version.php", MOODLE), gl.LOC_CODE_HEADER)
check("the same path, same class, on the second owner",
      gl.location_class("version.php", QUICKPOLL), gl.LOC_CODE_HEADER)
# 🔴 The regression that matters: a version.php that declares a version and nothing
# else must NOT be promoted to a grant location just because of its name.
check("a version.php with no grant words stays a manifest",
      gl.location_class("version.php", "<?php\n$plugin->version = 2026101700;\n"),
      gl.LOC_ECOSYSTEM_MANIFEST)

# ── 2. The classes of the other eight real payloads ───────────────────────────────
check("docs/License.txt is a filed grant", gl.location_class("docs/License.txt", OPENSIS_FILED),
      gl.LOC_LICENCE_FILE)
check("a 19-byte licence file is a BARE TOKEN, not a filed grant",
      gl.location_class("license.txt", FRAPPE), gl.LOC_BARE_TOKEN)
check("a 17 286-byte licence file is NOT a bare token",
      gl.location_class("docs/License.txt", OPENSIS_FILED), gl.LOC_LICENCE_FILE)
check("appinfo/info.xml is an application manifest",
      gl.location_class("appinfo/info.xml", NC_LIVE), gl.LOC_APP_MANIFEST)
check("index.php carrying a grant notice is a code header",
      gl.location_class("index.php", OPENSIS_CODE), gl.LOC_CODE_HEADER)
check("index.php with no grant notice is UNKNOWN, not a header",
      gl.location_class("index.php", "<?php echo 'hello';"), gl.LOC_UNKNOWN)
check("a README is not a grant location", gl.location_class("README.md", PLACEHOLDER),
      gl.LOC_UNKNOWN)
# `p247-path-class`'s SOURCE-FILE finding, kept: a code file NAMED license.*
check("license.go is source, never a filed grant",
      gl.location_class("src/license.go"), gl.LOC_UNKNOWN)
check("license.h is source, never a filed grant",
      gl.location_class("src/v/security/license.h"), gl.LOC_UNKNOWN)

# ── 3. Grant notice vs pointer, on the payload that carries BOTH ──────────────────
check("the Moodle header is a grant", gl.has_grant_notice(MOODLE), True)
check("the openSIS header is a grant", gl.has_grant_notice(OPENSIS_CODE), True)
check("the openSIS header ALSO carries a pointer", gl.has_pointer(OPENSIS_CODE), True)
# 🔴 The whole point: `See license.txt.` sits in the same comment as the grant, and
# the target does NOT exist — 404 on six spellings at root and absent from the whole
# repository.  A reader that lets the pointer defer the grant reads nothing at all.
check("a payload with both a grant and a pointer is still a grant",
      gl.location_class("index.php", OPENSIS_CODE), gl.LOC_CODE_HEADER)
check("a bare pointer with no grant words is not a grant notice",
      gl.has_grant_notice("<?php\n// See the LICENSE file for details.\n"), False)
check("...and it IS a pointer", gl.has_pointer("<?php\n// See the LICENSE file for details.\n"),
      True)

# ── 4. The header window.  A grant below the first statement is not a header. ─────
check("a grant phrase after the first statement is not in the header block",
      gl.has_grant_notice("<?php\n$x = 1;\n// This file is free software\n"), False)
check("the 45 523-byte openSIS body does not drown its 18-line header",
      len(gl.header_block(OPENSIS_CODE)) < 2000, True)

# ── 5. The bound, read through `p222` rather than re-implemented (P237) ───────────
# 🔴 These SEVEN rows are `ACTION YU`'s answer, and they are read by the instrument
# this base already had.  A bare `GPL-3.0` cell over a notice that says "or (at your
# option) any later version" loses the only thing that distinguishes -only from
# -or-later, and -only is the one that cannot be combined forward.
for label, body in (("quizaccess_ai", MOODLE), ("quickpoll", QUICKPOLL),
                    ("dev-tools addheader", ADDHEADER)):
    r = read_bound(gl.header_block(body), "prose")
    check(f"{label}: family", r["family"], "GPL")
    check(f"{label}: version", r["version"], "3.0")
    check(f"{label}: bound is or-later, not bare", r["bound"], "or-later")

_os = read_bound(gl.header_block(OPENSIS_CODE), "prose")
check("openSIS header: family", _os["family"], "GPL")
check("openSIS header: version 2, not 3", _os["version"], "2.0")
# 🔴 "version 2 of the License." with no "or later".  The FSF convention reads that as
# GPL-2.0-only, but the grammar does not INFER it, and neither does this base: the
# measurement is `unspecified` and the -only reading is published as interpretation.
check("openSIS header: the bound is unspecified, NOT inferred to -only",
      _os["bound"], "unspecified")

# ── 6. The application-manifest channel, both spellings ───────────────────────────
check("nextcloud live_transcription reads AGPL", gl.app_manifest_licence(NC_LIVE),
      ("AGPL", "unspecified"))
check("nextcloud talk_bot_ai reads AGPL", gl.app_manifest_licence(NC_BOT),
      ("AGPL", "unspecified"))
check("the American spelling is read too",
      gl.app_manifest_licence("<info><license>mit</license></info>"), ("MIT", "unspecified"))
check("a value outside the vocabulary is not guessed",
      gl.app_manifest_licence("<info><licence>whatever</licence></info>"), (None, None))
check("no licence element at all", gl.app_manifest_licence("<info><name>x</name></info>"),
      (None, None))

# ── 7. Reading strength.  Never a boolean, and never uniform. ─────────────────────
check("a filed payload supports a terms reading",
      gl.may_conclude(gl.LOC_LICENCE_FILE, "terms"), True)
check("a code header does NOT support a terms reading",
      gl.may_conclude(gl.LOC_CODE_HEADER, "terms"), False)
check("a code header DOES support a bound reading",
      gl.may_conclude(gl.LOC_CODE_HEADER, "bound"), True)
check("an app manifest supports family only",
      gl.reading_strength(gl.LOC_APP_MANIFEST), ("family",))
check("a bare token supports no bound reading",
      gl.may_conclude(gl.LOC_BARE_TOKEN, "bound"), False)
check("UNKNOWN supports nothing", gl.reading_strength(gl.LOC_UNKNOWN), ())
# The set itself is load-bearing: a mutant that adds "terms" to CODE-HEADER must fail.
check("exactly two classes support a terms reading",
      sorted(k for k, v in gl.STRENGTH.items() if "terms" in v), [gl.LOC_LICENCE_FILE])

# ── 8. The absence predicate — p259's half of p258's lesson ───────────────────────
check("one 404 is UNCONFIRMED", gl.absence_verdict([404]), gl.ABSENCE_UNCONFIRMED)
check("one 404 may NOT be published as an absence", gl.publishable_as_absence([404]), False)
check("two independent 404s CONFIRM", gl.absence_verdict([404, 404]),
      gl.ABSENCE_CONFIRMED)
check("...and may be published", gl.publishable_as_absence([404, 404]), True)
check("a 200 on re-probe REFUTES, whatever came before",
      gl.absence_verdict([404, 200]), gl.ABSENCE_REFUTED)
check("a refuted absence is not publishable as an absence",
      gl.publishable_as_absence([404, 200]), False)
check("no observations at all is UNCONFIRMED, not CONFIRMED",
      gl.absence_verdict([]), gl.ABSENCE_UNCONFIRMED)
check("a 429 is not a 404 but is still a non-200 observation",
      gl.absence_verdict([429, 404]), gl.ABSENCE_CONFIRMED)

# ── 9. The four causes, each pinned to the real row that produced it ──────────────
check("frappe/education: on the ladder, tier run, re-probe found it -> UNCONFIRMED",
      gl.miss_cause(path_on_ladder=True, tier_run=True, body_graded=True,
                    reprobe_found=True), gl.CAUSE_ABSENCE_UNCONFIRMED)
check("Moodle version.php: on the ladder, tier run, body never graded",
      gl.miss_cause(path_on_ladder=True, tier_run=True, body_graded=False,
                    reprobe_found=False), gl.CAUSE_BODY_NOT_GRADED)
check("openSIS docs/License.txt: on the ladder, Tier B not run",
      gl.miss_cause(path_on_ladder=True, tier_run=False, body_graded=False,
                    reprobe_found=False), gl.CAUSE_TIER_NOT_RUN)
check("nextcloud appinfo/info.xml: on no tier at all",
      gl.miss_cause(path_on_ladder=False, tier_run=False, body_graded=False,
                    reprobe_found=False), gl.CAUSE_CHANNEL_ABSENT)
check("everything run, everything graded, nothing found -> really absent",
      gl.miss_cause(path_on_ladder=True, tier_run=True, body_graded=True,
                    reprobe_found=False), gl.CAUSE_REALLY_ABSENT)
# 🔴 The number this base should keep in front of itself: of five causes, a longer
# list of path NAMES fixes exactly one.  p257 and p258 spent 590 probes on that list.
check("a longer path list fixes exactly one of the five causes",
      len(gl.CAUSES_A_LONGER_PATH_LIST_FIXES), 1)
check("...and the five causes are all distinct", len(set(gl.CAUSES)), 5)

if MISSING:
    FAILURES.append(f"{len(MISSING)} fixture(s) ABSENT, SKIPPED not passed: "
                    f"{', '.join(MISSING)}")

print(f"pass259-grant-location-class: {CHECKS} controls, {len(FAILURES)} failure(s)")
for failure in FAILURES:
    print(f"  FAIL {failure}")
sys.exit(1 if FAILURES else 0)
