"""`pass260-ecosystem-manifest-tier` — the ecosystem tier `ACTION ZA` asked for, built,
run over 153 repositories, and REFUTED on its own falsifier.

`ACTION ZA` (p259, highest priority) asked to *"add the ECOSYSTEM-NATIVE MANIFEST tier
and probe every grantless and NOASSERTION row on it, keyed by the row's
language/platform: `appinfo/info.xml` (Nextcloud), `*.info.yml` (Drupal), the plugin
header comment (WordPress), `*.cabal`, `*.gemspec`, `*.csproj`"*, with the falsifier
*"fewer than 3 rows across all ecosystems resolve — in which case Nextcloud is a
special case and the ladder stays as it is"*.

p260 ran it.  Every repository's ecosystem was detected from its OWN tree (one
`ls-remote` plus one blobless clone each, 153 trees), and every candidate manifest was
then fetched from `raw.githubusercontent.com` on the resolved ref and read with that
ecosystem's own reader.  Measured, over the six ecosystems `ZA` NAMED:

    NEXTCLOUD   2 repositories    2 declarations   <- both already resolved at p259
    DRUPAL      0 repositories    0
    WORDPRESS   0 repositories    0
    HASKELL     0 repositories    0
    RUBYGEM     1 repository      0 valid  (3 files, every one VENDORED)
    DOTNET      2 repositories    0        (5 files, no licence element in any)

🔴 **Zero rows that p259 had not already resolved.  `ACTION ZA` is REFUTED, and its own
falsifier says what that means: Nextcloud is a special case and the ladder stays as it
is.**

🟢 And the sweep that refuted it resolved **36 slugs** anyway — because it ran the
ecosystems that were ALREADY on the ladder, on a population they had never been run
against:

    package.json     19 declarations      pom.xml           2
    pyproject.toml    9                   version.php       2   (p259's own new tier)
    composer.json     3                   DESCRIPTION       2
    REUSE.toml / LICENSES/  6 declarations over the 2 Nextcloud rows — and they are
                            the only ecosystem channel that carries the BOUND

🔴 **So the cause distribution inverted.**  p259 classified its 11 resolutions and found
`TIER-NOT-RUN` in 1 of them (9 %) against `CHANNEL-ABSENT` in 3.  p260, on a population
14× larger, measures `TIER-NOT-RUN` in **34 of 36 (94.4 %)** and `CHANNEL-ABSENT` in
**0**.  Three passes have now asked for a WIDER ladder — `p257`/`p258` widened path
names for 0 rows, `p259` found the tier already present but mis-contracted, `p260` finds
the tier present, correctly contracted, and simply never executed on these rows.

🔵 **The lesson this module exists to make executable: a ladder's REACH and a ladder's
RUN are different quantities, and this base has only ever measured the first.**
`tier_coverage()` is the predicate that keeps them apart — it answers `NOT-RUN` for a
path that is on the ladder and was never fetched for a row, which is a different
verdict from `ABSENT`, and only one of the two is fixed by adding paths.

Four payload-shaped traps were met while reading the 106 manifests, and each is a
guard here rather than a note on a shelf:

  FOREIGN      `sonic-pi`'s only `.gemspec` files are `app/server/ruby/vendor/
               concurrent-ruby-1.3.5/*.gemspec` — a third party's grant.  They say
               `MIT`, sonic-pi IS `MIT`, so `ZA`'s named channel would have been
               ACCIDENTALLY RIGHT, which is worse than wrong: the method is unsound and
               the next repository will not be so kind.  Guarded BEFORE the read.
  GENERATED    `mn-mde-edfi`'s `.csproj` is OpenAPI-generator output with
               `<RepositoryUrl>https://github.com/GIT_USER_ID/GIT_REPO_ID.git</…>`
               unsubstituted and `<Copyright>No Copyright</Copyright>`.  Those fields
               are a GENERATOR'S DEFAULTS, not the publisher's assertion.
  NAME-CORRUPT `OpenOLAT`'s `pom.xml` line 24 reads `<name>Apache 2.0 Open Source
               L6icense</name>` while its `<url>` is the canonical Apache-2.0 URL.  A
               manifest declaration is a `(name, url)` PAIR and the name alone can be
               noise — p259's `(path, payload)` key, one layer further in.
  NOT-SPDX     `pipwerks`'s `package.json` carries `"license": "MIT-style license:
               http://pipwerks.mit-license.org/"`.  "MIT-style" is not MIT, and a
               field whose SCHEMA says SPDX can still hold prose.

And one guard that exists to stop a FALSE retraction rather than a false grant:
`Open-TutorAi/open-tutor-ai-CE`'s `LICENSE` opens *"Copyright (c) 2023-2025 … All
rights reserved."* — which is the conventional BSD header, not a reservation.  A reader
that stops at line 2 retracts a correct `BSD-3-Clause` cell.  `reservation_verdict()`
refuses to call it proprietary when the three BSD conditions follow.
"""

import json
import os
import re

# ── Location/strength, extending p259's classes rather than replacing them. ────────
# `pass259-grant-location-class` keyed on (path, payload).  This module keys on
# (ecosystem, path, payload), because the SAME path name means different things in
# different ecosystems and the reader is chosen by the ecosystem, not the suffix.
STRENGTH = {
    # the REUSE/SPDX channel is the only one that is machine-readable BY SPECIFICATION
    # rather than by convention, and it is the only ecosystem channel that carries terms
    "REUSE-SPDX": ("family", "bound", "terms"),
    "NEXTCLOUD": ("family",),          # `<licence>agpl</licence>` — no version at all
    "COMPOSER": ("family", "bound"),
    "NPM": ("family", "bound"),
    "PYPROJECT": ("family", "bound"),
    "SETUPPY": ("family", "bound"),
    "MAVEN": ("family", "bound"),
    "MOODLE": ("family", "bound"),
    "R-CRAN": ("family", "bound"),
    "RUBYGEM": ("family", "bound"),
    "DOTNET": ("family", "bound"),
    "DRUPAL": ("family",),
    "WORDPRESS": ("family",),
}

# 🔴 The six ecosystems `ACTION ZA` named, and what each returned over 153 repositories.
# Kept as a constant so the next pass cannot re-register `ZA` without reading it.
ZA_NAMED_RESULT = {
    "NEXTCLOUD": (2, 2, "both already resolved at p259 by this very channel"),
    "DRUPAL": (0, 0, "no Drupal repository in the corpus"),
    "WORDPRESS": (0, 0, "no WordPress plugin or theme in the corpus"),
    "HASKELL": (0, 0, "no .cabal in the corpus"),
    "RUBYGEM": (1, 0, "3 .gemspec files, every one vendored third-party"),
    "DOTNET": (2, 0, "5 .csproj files, no licence element in any; all generator output"),
}

# 🔴 The measured cause distribution.  p259: TIER-NOT-RUN 1 of 11.  p260: 35 of 37.
# `CAUSES_A_LONGER_PATH_LIST_FIXES` is p259's constant; this is the one that says how
# rarely that cause is the live one.
CAUSES_MEASURED_P260 = {
    # the path is on the ladder and was simply never fetched for the row
    "TIER-NOT-RUN": 34,
    # resolved at p259 already; p260's contribution is the BOUND, not the row
    "CHANNEL-ALREADY-RESOLVED": 2,
    # 🔴 the ONLY cause a longer path list fixes, and it is the one that measured zero
    "CHANNEL-ABSENT": 0,
}
CAUSES_A_LONGER_PATH_LIST_FIXES = ("CHANNEL-ABSENT",)

# ── Guards, each run BEFORE the declaration is believed. ───────────────────────────

# A path whose grant belongs to someone else.  p137's foreign-holder lesson, moved
# from "notice it afterwards" to "refuse it beforehand".
FOREIGN_DIR = re.compile(
    r"(^|/)(vendor|vendors|third_party|thirdparty|node_modules|external|externals|"
    r"deps|\.venv|site-packages|bundle|Pods|Godeps)/", re.I)

# Tokens a code generator leaves behind when nobody substituted them.
GENERATOR_TOKENS = ("GIT_USER_ID", "GIT_REPO_ID", "YOUR_PROJECT_NAME", "{{", "<%=",
                    "YOUR_NAME_HERE", "com.example", "org.example")

CANONICAL_URL = {
    "Apache-2.0": ("apache.org/licenses/LICENSE-2.0",),
    "MIT": ("opensource.org/licenses/MIT",),
    "GPL-3.0": ("gnu.org/licenses/gpl-3.0",),
    "AGPL-3.0": ("gnu.org/licenses/agpl-3.0",),
    "ECL-2.0": ("opensource.org/licenses/ECL-2.0",),
    "BSD-3-Clause": ("opensource.org/licenses/BSD-3-Clause",),
}

# Source-available, not OSI.  Shipping a closed derivative or a managed service is the
# thing a studio actually wants to do, and these forbid one or both.
NOT_OSI = ("elastic-2.0", "elastic license", "polyform", "busl", "sspl",
           "commons clause", "fair source", "source available")

CONTENT_LICENCE = re.compile(r"^CC[-_ ]?(BY|0)", re.I)


def is_foreign(path):
    """True when the manifest is a third party's, so its grant is not this row's."""
    return bool(FOREIGN_DIR.search(path or ""))


def is_generated(body):
    """True when the manifest is generator output whose fields were never substituted."""
    return any(t in (body or "") for t in GENERATOR_TOKENS)


def reservation_verdict(body):
    """`All rights reserved` at the top of a BSD/MIT text is BOILERPLATE, not a
    reservation.  Returns `BOILERPLATE`, `RESERVED` or `NO-RESERVATION`.

    This guard exists to stop a correct cell being retracted, which is the failure mode
    a grant reader almost never tests for."""
    b = body or ""
    if not re.search(r"all rights reserved", b, re.I):
        return "NO-RESERVATION"
    permissive = (
        re.search(r"[Rr]edistribution and use in source and binary forms", b)
        or re.search(r"Permission is hereby granted, free of charge", b))
    return "BOILERPLATE" if permissive else "RESERVED"


# ── Ecosystem detection, from the repository's OWN tree. ───────────────────────────

def _any(tree, pattern):
    rx = re.compile(pattern)
    return [p for p in tree if rx.search(p)]


def detect_ecosystems(tree):
    """tree -> [(ecosystem, [candidate paths])].  Detection is by the files the
    repository actually has, never by a guess from its name or description."""
    tree = list(tree)
    roots = {p for p in tree if "/" not in p}
    out = []

    reuse = []
    if "REUSE.toml" in roots:
        reuse.append("REUSE.toml")
    if ".reuse/dep5" in tree:
        reuse.append(".reuse/dep5")
    reuse += sorted(p for p in tree if p.startswith("LICENSES/"))[:6]
    if reuse:
        out.append(("REUSE-SPDX", reuse))

    if "appinfo/info.xml" in tree:
        out.append(("NEXTCLOUD", ["appinfo/info.xml"]))

    for eco, pat in (("DRUPAL", r"(^|/)[^/]+\.info\.yml$"),
                     ("RUBYGEM", r"(^|/)[^/]+\.gemspec$"),
                     ("DOTNET", r"(^|/)[^/]+\.csproj$"),
                     ("HASKELL", r"(^|/)[^/]+\.cabal$"),
                     ("R-CRAN", r"(^|/)DESCRIPTION$")):
        hit = _any(tree, pat)
        if hit:
            out.append((eco, hit[:4]))

    wp = [p for p in ("style.css", "readme.txt") if p in roots]
    if wp and any(p.endswith(".php") for p in tree):
        out.append(("WORDPRESS", wp + sorted(p for p in roots if p.endswith(".php"))[:2]))

    for eco, fn in (("COMPOSER", "composer.json"), ("NPM", "package.json"),
                    ("PYPROJECT", "pyproject.toml"), ("SETUPPY", "setup.py"),
                    ("MAVEN", "pom.xml"), ("MOODLE", "version.php")):
        if fn in roots:
            out.append((eco, [fn]))
    return out


# ── The readers.  Each is the one that ecosystem's own tooling uses. ───────────────

def read_declaration(ecosystem, path, body):
    """(token, read_by) or (None, why-not).  Never a generic grep for 'license'."""
    body = body or ""
    try:
        if ecosystem in ("NPM", "COMPOSER"):
            d = json.loads(body)
            lic = d.get("license") or d.get("licenses")
            if isinstance(lic, list):
                lic = ",".join(x.get("type", str(x)) if isinstance(x, dict) else str(x)
                               for x in lic)
            if isinstance(lic, dict):
                lic = lic.get("type")
            return (str(lic), "json:license") if lic else (None, "KEY-ABSENT")
        if ecosystem == "PYPROJECT":
            m = re.search(r'^\s*license\s*=\s*(?:\{[^}]*?text\s*=\s*)?["\']([^"\']+)["\']',
                          body, re.M)
            if m:
                return m.group(1), "toml:project.license"
            m = re.search(r'^\s*license\s*=\s*\{\s*file\s*=\s*["\']([^"\']+)["\']',
                          body, re.M)
            if m:
                return "FILE-POINTER:" + m.group(1), "toml:license.file"
            cl = re.findall(r'["\']License :: ([^"\']+)["\']', body)
            return (cl[0], "toml:classifier") if cl else (None, "KEY-ABSENT")
        if ecosystem == "SETUPPY":
            m = re.search(r'license\s*=\s*["\']([^"\']+)["\']', body)
            return (m.group(1), "setup.py:license") if m else (None, "KEY-ABSENT")
        if ecosystem == "MAVEN":
            m = re.search(r"<licenses?>.*?<name>\s*([^<]+?)\s*</name>", body, re.S | re.I)
            return (m.group(1), "pom:licenses.name") if m else (None, "KEY-ABSENT")
        if ecosystem == "NEXTCLOUD":
            # 🔵 BOTH spellings.  `<licence>` is the British one Nextcloud actually uses
            # and a reader that knows only `<license>` publishes a spelling as a gap.
            m = re.search(r"<licen[cs]e>\s*([^<]+?)\s*</licen[cs]e>", body, re.I)
            return (m.group(1), "info.xml:<licence>") if m else (None, "KEY-ABSENT")
        if ecosystem == "REUSE-SPDX":
            if (path or "").startswith("LICENSES/"):
                return os.path.basename(path).rsplit(".", 1)[0], "LICENSES/<spdx-id>.txt"
            m = re.search(r"^#?\s*SPDX-License-Identifier:\s*(.+?)\s*$", body, re.M)
            if m:
                return m.group(1), "REUSE.toml:SPDX-License-Identifier"
            m = re.search(r'SPDX-License-Identifier\s*=\s*["\']([^"\']+)["\']', body)
            return (m.group(1), "REUSE.toml:annotation") if m else (None, "KEY-ABSENT")
        if ecosystem == "DOTNET":
            m = re.search(r"<PackageLicenseExpression>\s*([^<]+?)\s*</PackageLicenseExpression>",
                          body, re.I)
            if m:
                return m.group(1), "csproj:PackageLicenseExpression"
            m = re.search(r"<PackageLicenseFile>\s*([^<]+?)\s*</PackageLicenseFile>",
                          body, re.I)
            return ("FILE-POINTER:" + m.group(1), "csproj:PackageLicenseFile") if m \
                else (None, "KEY-ABSENT")
        if ecosystem == "RUBYGEM":
            m = re.search(r"\.licen[cs]es?\s*=\s*\[?\s*[\"']([^\"']+)[\"']", body)
            return (m.group(1), "gemspec:licenses") if m else (None, "KEY-ABSENT")
        if ecosystem == "R-CRAN":
            m = re.search(r"^License:\s*(.+?)\s*$", body, re.M)
            return (m.group(1), "DESCRIPTION:License") if m else (None, "KEY-ABSENT")
        if ecosystem == "DRUPAL":
            m = re.search(r"^\s*license\s*:\s*(.+?)\s*$", body, re.M)
            return (m.group(1), "info.yml:license") if m else (None, "KEY-ABSENT")
        if ecosystem == "WORDPRESS":
            m = re.search(r"^\s*\*?\s*Licen[cs]e:\s*(.+?)\s*$", body, re.M | re.I)
            return (m.group(1), "plugin-header:License") if m else (None, "KEY-ABSENT")
    except Exception as exc:
        # a manifest that does not parse is a MEASUREMENT, not a crash
        return None, "UNPARSEABLE:" + type(exc).__name__
    return None, "NO-READER"


# ── What the token is, once read. ──────────────────────────────────────────────────

SPDX_EXACT = re.compile(
    r"^(MIT|ISC|Apache-2\.0|BSD-2-Clause|BSD-3-Clause|MPL-2\.0|"
    r"(?:L|A)?GPL-[23](?:\.0)?(?:-only|-or-later)?|CC0-1\.0|CC-BY(?:-SA|-NC|-ND)*-4\.0|"
    r"Unlicense|ECL-2\.0|EPL-2\.0|Elastic-2\.0)$")


def token_verdict(token):
    """What KIND of thing the manifest's licence field actually holds."""
    if token is None:
        return "NO-TOKEN"
    t = token.strip()
    if t.startswith("FILE-POINTER:"):
        return "FILE-POINTER"
    if SPDX_EXACT.match(t):
        if CONTENT_LICENCE.match(t):
            return "CONTENT-LICENCE-ON-CODE"
        if t.lower() in (n for n in ("elastic-2.0",)):
            return "NOT-OSI"
        return "SPDX-EXACT"
    low = t.lower()
    if any(n in low for n in NOT_OSI):
        return "NOT-OSI"
    if CONTENT_LICENCE.match(t):
        return "CONTENT-LICENCE-ON-CODE"
    # 🔵 A space is NOT evidence of prose.  `ECL 2.0` and `AGPL 3` are loose spellings
    # of real identifiers and a blunt "contains a space" rule buries both — measured,
    # because the first version of this predicate did exactly that on two live rows.
    # Prose is a URL, real length, or a sentence's worth of words.
    if "://" in t or len(t) > 40 or len(t.split()) >= 4:
        return "NOT-SPDX-PROSE"
    return "SPDX-LOOSE"


def manifest_verdict(name, url=None):
    """A manifest declaration is a `(name, url)` PAIR.  p259 keyed a grant on
    `(path, payload)`; inside the payload the same argument applies again, and
    `OpenOLAT` is the row that proves it: `Apache 2.0 Open Source L6icense` against the
    canonical Apache URL.  Returns (verdict, resolved-identifier-or-None)."""
    v = token_verdict(name)
    if v != "NOT-SPDX-PROSE" or not url:
        return v, (name if v in ("SPDX-EXACT", "SPDX-LOOSE") else None)
    for spdx, urls in CANONICAL_URL.items():
        if any(u in url for u in urls):
            return "NAME-CORRUPT:url-operative", spdx
    return v, None


# ── Reach is not run. ──────────────────────────────────────────────────────────────

def tier_coverage(path_on_ladder, path_was_fetched_for_row):
    """🔴 The predicate this pass exists for.

    A ladder has a REACH (the paths it knows) and a RUN (the paths it actually fetched
    for a given row).  Every pass from p257 to p259 measured reach and reported it as
    coverage, and `ACTION ZA` asked to extend reach again.  p260 measured run: 35 of 37
    resolutions came from a path that was ALWAYS on the ladder and had never been
    fetched for that row.

    `NOT-RUN` and `ABSENT` are different verdicts and only `ABSENT` is fixed by adding
    paths."""
    if path_on_ladder and path_was_fetched_for_row:
        return "RUN"
    if path_on_ladder and not path_was_fetched_for_row:
        return "NOT-RUN"
    return "ABSENT"


def usable_in_closed_derivative(token):
    """What a studio actually asks.  A deliberately conservative predicate: anything
    this module cannot positively identify as permissive answers False."""
    v = token_verdict(token)
    if v != "SPDX-EXACT":
        return False
    return token.strip() in ("MIT", "ISC", "Apache-2.0", "BSD-2-Clause",
                             "BSD-3-Clause", "CC0-1.0", "Unlicense")


# ── Two declarations, one repository. ─────────────────────────────────────────────

def reconcile(filed_token, manifest_token):
    """A filed licence TEXT and an ecosystem manifest can name different licences in
    the same commit.  Measured on [`Zenglian990/AI_Tutor_Release`]: `LICENSE` is a
    canonical `MIT` text (`1 067` B) and `package.json` says `"license": "ISC"` — which
    is what `npm init` writes when nobody chooses.

    🔵 The rule follows from `STRENGTH` and needs no new judgement: a filed payload
    carries family, bound AND terms; a manifest carries a declaration.  **The filed
    text is operative and the manifest is evidence about it.**  Returns
    (operative-token, verdict).
    """
    if filed_token and manifest_token and filed_token.strip() != manifest_token.strip():
        return filed_token, "CONTRADICTED-BY-MANIFEST"
    if filed_token:
        return filed_token, "FILED"
    if manifest_token:
        # 🔴 The grant exists only as a field.  For `MIT`, `ISC`, `BSD` and `Apache-2.0`
        # this is a real duty gap: each of those licences requires a distributor to
        # reproduce the licence TEXT, and the repository never published one.
        return manifest_token, "MANIFEST-ONLY"
    return None, "NO-GRANT"


# Licences whose own terms require a distributor to reproduce the licence text.  A
# `MANIFEST-ONLY` grant in one of these families leaves the distributor owing a
# document the upstream never shipped.
TEXT_REPRODUCTION_REQUIRED = ("MIT", "ISC", "BSD-2-Clause", "BSD-3-Clause",
                              "Apache-2.0")


def manifest_only_duty_gap(token, grant_state):
    """True when the row's only grant is a manifest field AND the named licence
    obliges the distributor to ship a text that does not exist upstream."""
    return grant_state == "MANIFEST-ONLY" and \
        (token or "").strip() in TEXT_REPRODUCTION_REQUIRED
