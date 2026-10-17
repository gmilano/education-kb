#!/usr/bin/env python3
"""Controls for `pass260-ecosystem-manifest-tier`.

Every fixture is a payload READ FIRST-HAND at `p260` over `raw.githubusercontent.com`
on an `ls-remote`-resolved ref.  No excerpt is hand-typed.

  nextcloud-live_transcription-REUSE.toml      nextcloud/live_transcription @ master  521 B
  nextcloud-talk_bot_ai-REUSE.toml             nextcloud/talk_bot_ai @ main           686 B
  nextcloud-live_transcription-info.xml        nextcloud/live_transcription @ master 3837 B
  openolat-pom.xml                             OpenOLAT/OpenOLAT @ master           84963 B
  canyongbs-advisingapp-composer.json          canyongbs/advisingapp @ main         12343 B
  pipwerks-scorm-api-wrapper-package.json      pipwerks/scorm-api-wrapper @ master    606 B
  inginious-pyproject.toml                     INGInious/INGInious @ main            3683 B
  moodle-composer.json                         moodle/moodle @ main                  3735 B
  sakai-xapi-provider-pom.xml                  Apereo-…/SakaiXAPI-Provider @ master  6118 B
  sonicpi-vendored-concurrent-ruby.gemspec     sonic-pi-net/sonic-pi @ dev           1623 B
  opentutorai-LICENSE                          Open-TutorAi/open-tutor-ai-CE @ main  1531 B
  jupyterhub-ltiauthenticator-pyproject.toml   jupyterhub/ltiauthenticator @ main    3109 B
  mde-edfi-OdsApi-Sdk.csproj                   mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK     1423 B
  garethmanning-education-agent-skills-package.json  GarethManning/… @ main           607 B
  frappe-lms-package.json                      frappe/lms @ develop                   825 B

🔴 Run from this directory.  `python3 -I` strips the script's own directory from
`sys.path` (p229/p355), which is why every Makefile recipe `cd`s into the instrument.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import manifest_tier as mt  # noqa: E402

FIX = os.path.join(HERE, "fixtures-p260")
FAILURES = []
MISSING = []
CHECKS = 0


def load(name):
    p = os.path.join(FIX, name)
    if not os.path.exists(p):
        MISSING.append(name)
        return None
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def ck(label, got, want):
    global CHECKS
    CHECKS += 1
    if got != want:
        FAILURES.append(f"{label}: got {got!r}, want {want!r}")


# ══ 1. REUSE/SPDX — the channel that carries the BOUND p259 declared unstated ══════
for slug, fn in (("live_transcription", "nextcloud-live_transcription-REUSE.toml"),
                 ("talk_bot_ai", "nextcloud-talk_bot_ai-REUSE.toml")):
    body = load(fn)
    if body is not None:
        tok, how = mt.read_declaration("REUSE-SPDX", "REUSE.toml", body)
        ck(f"reuse/{slug} token", tok, "AGPL-3.0-or-later")
        ck(f"reuse/{slug} read_by", how, "REUSE.toml:SPDX-License-Identifier")
        ck(f"reuse/{slug} verdict", mt.token_verdict(tok), "SPDX-EXACT")
        ck(f"reuse/{slug} closed-derivative", mt.usable_in_closed_derivative(tok), False)

# the LICENSES/ half of the same channel, read by filename as REUSE specifies
ck("reuse LICENSES/ token",
   mt.read_declaration("REUSE-SPDX", "LICENSES/AGPL-3.0-or-later.txt", "")[0],
   "AGPL-3.0-or-later")
ck("reuse LICENSES/ read_by",
   mt.read_declaration("REUSE-SPDX", "LICENSES/AGPL-3.0-or-later.txt", "")[1],
   "LICENSES/<spdx-id>.txt")

# 🔴 and the comparison that is the whole point: the SAME repository, two channels,
# and p259 added the weaker one.
info = load("nextcloud-live_transcription-info.xml")
if info is not None:
    tok_app, _ = mt.read_declaration("NEXTCLOUD", "appinfo/info.xml", info)
    ck("nextcloud app-manifest token", tok_app, "agpl")
    ck("nextcloud app-manifest has no bound", "bound" in mt.STRENGTH["NEXTCLOUD"], False)
    ck("nextcloud reuse HAS bound", "bound" in mt.STRENGTH["REUSE-SPDX"], True)
    ck("nextcloud app-manifest token is not SPDX",
       mt.token_verdict(tok_app), "SPDX-LOOSE")

# ══ 2. The FOREIGN guard — sonic-pi's only .gemspec files are a third party's ══════
gem = load("sonicpi-vendored-concurrent-ruby.gemspec")
VENDORED_PATH = "app/server/ruby/vendor/concurrent-ruby-1.3.5/concurrent-ruby.gemspec"
ck("gemspec path is foreign", mt.is_foreign(VENDORED_PATH), True)
ck("root gemspec is not foreign", mt.is_foreign("sonic-pi.gemspec"), False)
if gem is not None:
    tok, _ = mt.read_declaration("RUBYGEM", VENDORED_PATH, gem)
    # 🔴 It reads MIT, and sonic-pi IS MIT — accidentally right, which is why the guard
    # has to run BEFORE the read rather than after it.
    ck("vendored gemspec would have read", tok, "MIT")
for p in ("node_modules/x/package.json", "third_party/a/b.gemspec",
          "Pods/Alamofire/Alamofire.podspec", ".venv/lib/site-packages/q/setup.py"):
    ck(f"foreign: {p}", mt.is_foreign(p), True)
for p in ("package.json", "src/vendored_notes.md", "app/vendor.js"):
    ck(f"not foreign: {p}", mt.is_foreign(p), False)

# ══ 3. The GENERATED guard — a .csproj whose fields are a generator's defaults ═════
csproj = load("mde-edfi-OdsApi-Sdk.csproj")
if csproj is not None:
    ck("csproj is generator output", mt.is_generated(csproj), True)
    tok, how = mt.read_declaration(
        "DOTNET", "MDE-EdFiClientSDK/EdFi/OdsApiv62_2026/src/EdFi.OdsApi.Sdk/"
                  "EdFi.OdsApi.Sdk.csproj", csproj)
    ck("csproj has no licence element", tok, None)
    ck("csproj why-not", how, "KEY-ABSENT")
    # the field a careless reader WOULD have taken
    ck("csproj carries a copyright string anyway",
       "<Copyright>No Copyright</Copyright>" in csproj, True)
ck("non-generated manifest", mt.is_generated('{"name":"x","license":"MIT"}'), False)

# 🔴 The mutation run caught this suite being decorative in one direction: the live
# `.csproj` carries TWO generator tokens, so deleting either one on its own left every
# control green.  p258's shape — a redundant positive list masking its own members —
# met inside the instrument written to record it.  The set is now pinned member by
# member, and each member is asserted to fire on its own.
ck("generator token set", set(mt.GENERATOR_TOKENS),
   {"GIT_USER_ID", "GIT_REPO_ID", "YOUR_PROJECT_NAME", "{{", "<%=",
    "YOUR_NAME_HERE", "com.example", "org.example"})
for tok in ("GIT_USER_ID", "GIT_REPO_ID", "YOUR_PROJECT_NAME", "{{", "<%=",
            "YOUR_NAME_HERE", "com.example", "org.example"):
    ck(f"generator token fires alone: {tok}",
       mt.is_generated("harmless text " + tok + " more text"), True)
if csproj is not None:
    ck("live csproj matches exactly these generator tokens",
       sorted(t for t in mt.GENERATOR_TOKENS if t in csproj),
       ["GIT_REPO_ID", "GIT_USER_ID"])

# ══ 4. NAME-CORRUPT — OpenOLAT's pom, where the name is noise and the url decides ══
pom = load("openolat-pom.xml")
if pom is not None:
    name, how = mt.read_declaration("MAVEN", "pom.xml", pom)
    ck("openolat name read verbatim", name, "Apache 2.0 Open Source L6icense")
    ck("openolat read_by", how, "pom:licenses.name")
    ck("openolat name alone is prose", mt.token_verdict(name), "NOT-SPDX-PROSE")
    v, ident = mt.manifest_verdict(name, "http://www.apache.org/licenses/LICENSE-2.0")
    ck("openolat pair verdict", v, "NAME-CORRUPT:url-operative")
    ck("openolat resolved identifier", ident, "Apache-2.0")
    # 🔴 without the url there is nothing to resolve, and the module must say so
    ck("openolat name-only resolves nothing", mt.manifest_verdict(name)[1], None)

# ══ 5. NOT-SPDX prose in a field whose schema says SPDX ═══════════════════════════
pw = load("pipwerks-scorm-api-wrapper-package.json")
if pw is not None:
    tok, _ = mt.read_declaration("NPM", "package.json", pw)
    ck("pipwerks token", tok, "MIT-style license: http://pipwerks.mit-license.org/")
    ck("pipwerks verdict", mt.token_verdict(tok), "NOT-SPDX-PROSE")
    # "MIT-style" is NOT MIT, and the conservative predicate must refuse it
    ck("pipwerks not shippable-closed", mt.usable_in_closed_derivative(tok), False)

# ══ 6. NOT-OSI — source-available licences declared in a code manifest ════════════
adv = load("canyongbs-advisingapp-composer.json")
if adv is not None:
    tok, how = mt.read_declaration("COMPOSER", "composer.json", adv)
    ck("advisingapp token", tok, "Elastic-2.0")
    ck("advisingapp read_by", how, "json:license")
    ck("advisingapp verdict", mt.token_verdict(tok), "NOT-OSI")
    ck("advisingapp not shippable-closed", mt.usable_in_closed_derivative(tok), False)
for t in ("PolyForm-Noncommercial-1.0.0", "BUSL-1.1", "Elastic License 2.0",
          "SSPL-1.0", "Commons Clause"):
    ck(f"not-osi: {t}", mt.token_verdict(t), "NOT-OSI")

# ══ 7. CONTENT-LICENCE-ON-CODE — p258's CC class, now inside a code manifest ══════
gm = load("garethmanning-education-agent-skills-package.json")
if gm is not None:
    tok, _ = mt.read_declaration("NPM", "package.json", gm)
    ck("education-agent-skills token", tok, "CC-BY-SA-4.0")
    ck("education-agent-skills verdict", mt.token_verdict(tok),
       "CONTENT-LICENCE-ON-CODE")
    ck("cc-by-sa not shippable-closed", mt.usable_in_closed_derivative(tok), False)
ck("cc0 on code is still a content licence",
   mt.token_verdict("CC0-1.0"), "CONTENT-LICENCE-ON-CODE")

# ══ 8. FILE-POINTER, and p259's rule that a pointer may point nowhere ═════════════
lti = load("jupyterhub-ltiauthenticator-pyproject.toml")
if lti is not None:
    tok, how = mt.read_declaration("PYPROJECT", "pyproject.toml", lti)
    ck("ltiauthenticator token", tok, "FILE-POINTER:LICENSE")
    ck("ltiauthenticator read_by", how, "toml:license.file")
    ck("ltiauthenticator verdict", mt.token_verdict(tok), "FILE-POINTER")
    ck("a pointer is never shippable on its own",
       mt.usable_in_closed_derivative(tok), False)

# ══ 9. The FALSE-RETRACTION guard ═════════════════════════════════════════════════
# `Open-TutorAi/open-tutor-ai-CE` opens "All rights reserved." and IS BSD-3-Clause.
ot = load("opentutorai-LICENSE")
if ot is not None:
    ck("opentutorai reservation is boilerplate", mt.reservation_verdict(ot),
       "BOILERPLATE")
ck("a real reservation",
   mt.reservation_verdict("Copyright (c) 2026 Acme.\nAll rights reserved.\n"
                          "No permission is granted."), "RESERVED")
ck("no reservation clause at all",
   mt.reservation_verdict("MIT License\n\nPermission is hereby granted, free of "
                          "charge, to any person"), "NO-RESERVATION")

# ══ 10. The ecosystems already on the ladder, which is where the rows came from ═══
moo = load("moodle-composer.json")
if moo is not None:
    tok, how = mt.read_declaration("COMPOSER", "composer.json", moo)
    # 🟢 the BOUND for Moodle core, which the shelves carried as a bare `GPL-3.0`
    ck("moodle core token", tok, "GPL-3.0-or-later")
    ck("moodle core read_by", how, "json:license")
    ck("moodle core verdict", mt.token_verdict(tok), "SPDX-EXACT")

sakai = load("sakai-xapi-provider-pom.xml")
if sakai is not None:
    tok, _ = mt.read_declaration("MAVEN", "pom.xml", sakai)
    ck("sakai xapi token", tok, "ECL 2.0")
    ck("sakai xapi is loose, not exact", mt.token_verdict(tok), "SPDX-LOOSE")

ing = load("inginious-pyproject.toml")
if ing is not None:
    tok, how = mt.read_declaration("PYPROJECT", "pyproject.toml", ing)
    ck("inginious token", tok, "AGPL 3")
    ck("inginious read_by", how, "toml:project.license")
    ck("inginious spelling is loose", mt.token_verdict(tok), "SPDX-LOOSE")

lms = load("frappe-lms-package.json")
if lms is not None:
    tok, _ = mt.read_declaration("NPM", "package.json", lms)
    ck("frappe/lms token", tok, "AGPL-3.0-or-later")
    ck("frappe/lms verdict", mt.token_verdict(tok), "SPDX-EXACT")

# ══ 11. Ecosystem detection, from a tree and nothing else ═════════════════════════
NC_TREE = ["appinfo/info.xml", "REUSE.toml", "LICENSES/AGPL-3.0-or-later.txt",
           "LICENSES/MIT.txt", "lib/Service/X.php", "package.json"]
det = dict(mt.detect_ecosystems(NC_TREE))
ck("detect nextcloud", "NEXTCLOUD" in det, True)
ck("detect reuse", "REUSE-SPDX" in det, True)
ck("detect npm from root only", det.get("NPM"), ["package.json"])
ck("reuse candidates include REUSE.toml", "REUSE.toml" in det["REUSE-SPDX"], True)

ck("a nested package.json is not an NPM root",
   dict(mt.detect_ecosystems(["frontend/package.json"])).get("NPM"), None)
ck("drupal detected by *.info.yml",
   dict(mt.detect_ecosystems(["mymod.info.yml", "mymod.module"])).get("DRUPAL"),
   ["mymod.info.yml"])
ck("wordpress needs php beside style.css",
   "WORDPRESS" in dict(mt.detect_ecosystems(["style.css"])), False)
ck("wordpress detected with php",
   "WORDPRESS" in dict(mt.detect_ecosystems(["style.css", "plugin.php"])), True)
ck("empty tree detects nothing", mt.detect_ecosystems([]), [])

# ══ 12. REACH is not RUN — the predicate this pass exists for ═════════════════════
ck("on ladder and fetched", mt.tier_coverage(True, True), "RUN")
ck("on ladder, never fetched", mt.tier_coverage(True, False), "NOT-RUN")
ck("not on ladder at all", mt.tier_coverage(False, False), "ABSENT")
ck("NOT-RUN is not ABSENT",
   mt.tier_coverage(True, False) == mt.tier_coverage(False, False), False)

# ══ 13. The measured record, pinned so the next pass cannot re-register ZA blind ══
ck("ZA named six ecosystems", len(mt.ZA_NAMED_RESULT), 6)
new_rows = sum(res for _, res, _ in mt.ZA_NAMED_RESULT.values())
ck("ZA's named ecosystems resolved 2 rows in total", new_rows, 2)
ck("…and both are the Nextcloud rows p259 had already resolved",
   mt.ZA_NAMED_RESULT["NEXTCLOUD"][1], 2)
ck("drupal/wordpress/haskell absent from the corpus",
   [mt.ZA_NAMED_RESULT[e][0] for e in ("DRUPAL", "WORDPRESS", "HASKELL")], [0, 0, 0])
ck("TIER-NOT-RUN dominates the causes",
   max(mt.CAUSES_MEASURED_P260, key=mt.CAUSES_MEASURED_P260.get), "TIER-NOT-RUN")
ck("CHANNEL-ABSENT — the only cause a longer path list fixes — measured zero",
   mt.CAUSES_MEASURED_P260["CHANNEL-ABSENT"], 0)
ck("TIER-NOT-RUN count", mt.CAUSES_MEASURED_P260["TIER-NOT-RUN"], 34)
ck("the two off-ladder rows were already resolved at p259",
   mt.CAUSES_MEASURED_P260["CHANNEL-ALREADY-RESOLVED"], 2)
ck("resolutions total 36 slugs", sum(mt.CAUSES_MEASURED_P260.values()), 36)
ck("and it is named as such",
   mt.CAUSES_A_LONGER_PATH_LIST_FIXES, ("CHANNEL-ABSENT",))

# ══ 14. Strength, which must not be flattened (p258's CC lesson) ══════════════════
ck("reuse carries terms", mt.STRENGTH["REUSE-SPDX"], ("family", "bound", "terms"))
ck("nextcloud manifest carries family only", mt.STRENGTH["NEXTCLOUD"], ("family",))
ck("strengths are not all equal",
   len({mt.STRENGTH[e] for e in mt.STRENGTH}) > 1, True)

# ══ 15. Readers refuse what they are not contracted for (p259's ACTION ZB) ════════
ck("npm reader on a toml body", mt.read_declaration("NPM", "package.json",
   'license = "MIT"')[1].startswith("UNPARSEABLE"), True)
ck("no reader for an unknown ecosystem",
   mt.read_declaration("COBOL", "x.cbl", "")[1], "NO-READER")
ck("empty body is KEY-ABSENT, not a crash",
   mt.read_declaration("MAVEN", "pom.xml", "")[1], "KEY-ABSENT")
ck("None body is KEY-ABSENT",
   mt.read_declaration("R-CRAN", "DESCRIPTION", None)[1], "KEY-ABSENT")


# ══ 16. Two declarations, one repository (p260's live contradiction) ══════════════
# `Zenglian990/AI_Tutor_Release`: `LICENSE` is a canonical MIT text (1 067 B,
# 6beebb286c673b46) and `package.json` says `"license": "ISC"` — npm init's default.
ck("filed text wins over the manifest",
   mt.reconcile("MIT", "ISC"), ("MIT", "CONTRADICTED-BY-MANIFEST"))
ck("agreement is not a contradiction", mt.reconcile("MIT", "MIT"), ("MIT", "FILED"))
ck("filed only", mt.reconcile("Apache-2.0", None), ("Apache-2.0", "FILED"))
ck("manifest only", mt.reconcile(None, "MIT"), ("MIT", "MANIFEST-ONLY"))
ck("neither", mt.reconcile(None, None), (None, "NO-GRANT"))

# 🔴 `5` of the `7` connectors resolved this pass have NO filed licence text at all.
# An `MIT` that exists only as a field leaves a distributor owing a document upstream
# never published.
ck("manifest-only MIT is a duty gap",
   mt.manifest_only_duty_gap("MIT", "MANIFEST-ONLY"), True)
ck("manifest-only ISC is a duty gap",
   mt.manifest_only_duty_gap("ISC", "MANIFEST-ONLY"), True)
ck("manifest-only AGPL is not THIS gap",
   mt.manifest_only_duty_gap("AGPL-3.0-or-later", "MANIFEST-ONLY"), False)
ck("a filed MIT is no gap", mt.manifest_only_duty_gap("MIT", "FILED"), False)
ck("the text-reproduction set", set(mt.TEXT_REPRODUCTION_REQUIRED),
   {"MIT", "ISC", "BSD-2-Clause", "BSD-3-Clause", "Apache-2.0"})

# ══ report ════════════════════════════════════════════════════════════════════════
print(f"pass260-ecosystem-manifest-tier: {CHECKS} controls")
if MISSING:
    print("MISSING FIXTURES: " + ", ".join(MISSING))
for f in FAILURES:
    print("FAIL " + f)
if FAILURES or MISSING:
    sys.exit(1)
print("OK")
