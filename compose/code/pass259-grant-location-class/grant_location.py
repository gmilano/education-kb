"""`pass259-grant-location-class` — WHERE a grant was read, and what that location
entitles a reader to conclude.

`ACTION YU` (p258) asked for a CODE-HEADER tier on the grant ladder, "starting with
`version.php` for Moodle plugins".  p259 ran it and the tier works — 7 of the 9 known
Moodle rows resolved `GPL-3.0-or-later` from a header, across TWO owners.  But the
pass found something the ACTION did not anticipate, and this module is that finding
made executable:

🔴 **`version.php` was ALREADY on the ladder.**  It is Tier C, position 1, and it has
been since the tier was built.  `p247-path-class` grades it `MANIFEST`, and the
MANIFEST contract says — correctly, and for a reason this base paid for at p246 —
*"una DECLARACION, no un payload: la lee la gramatica de ecosistema, nunca el
clasificador de cuerpo"*.  A Moodle `version.php` declares `$plugin->version`; it
declares no licence at all.  The grant is in the comment ABOVE the declaration.  So
the path was fetched, the manifest grammar found no licence field, and the body — a
complete GPL-3.0-or-later notice — was never graded.  `p222-ecosystem-bound-grammar`
even carries the line `'version.php': 'prose',  # Moodle's mandated GPL header`, which
is this base having WRITTEN DOWN the answer four passes before the ACTION asked for it.

🔵 **So the defect was never a missing path.  It was that one path can carry two
different KINDS of evidence, and the ladder keys its contract on the path.**  That is
the shape this module exists to make unrepresentable: a (path, location-class) pair,
where the class — not the path — decides which reader runs and what may be concluded.

The four non-reproducing-absence causes p259 measured, each on a real row:

  BODY-NOT-GRADED   the path was fetched; its contract forbade reading the body
                    (`version.php` × 7 Moodle rows)
  TIER-NOT-RUN      the path is on the ladder, in a tier the probe did not run
                    (`docs/License.txt` — Tier B — `OS4ED/openSIS-Classic`)
  CHANNEL-ABSENT    the ecosystem's own manifest is on no tier at all
                    (`appinfo/info.xml` — Nextcloud — 2 rows)
  ABSENCE-UNCONFIRMED  a single 404 recorded as an absence, which a second attempt
                    refutes (`frappe/education`, `license.txt`, Tier A position 13,
                    a file present in the repository since 2022-04-27)

🔴 The last one is p258's own lesson, mirrored.  p258: *a 403 from one ENDPOINT was
generalised to a whole channel.*  p259: **a 404 from one ATTEMPT was recorded as a
property of the repository.**  One attempt is not an absence, and this module refuses
to emit `NO-GRANT` from a single observation — `absence_verdict()` demands two.

What each location entitles you to conclude is NOT uniform, and flattening that is how
a bare `GPL-3.0` cell gets written over a notice that actually says "or any later
version".  `reading_strength()` is the predicate that keeps them apart.
"""

import re

# ── Location classes.  The class, never the path, selects the reader. ──────────────
LOC_LICENCE_FILE = "LICENCE-FILE"      # a filed grant: the full text, gradeable
LOC_CODE_HEADER = "CODE-HEADER"        # a grant NOTICE in a source file's comment
LOC_APP_MANIFEST = "APP-MANIFEST"      # an application manifest's own licence element
LOC_ECOSYSTEM_MANIFEST = "ECO-MANIFEST"  # composer/package/pyproject: a declaration
LOC_BARE_TOKEN = "BARE-TOKEN"          # a licence FILE whose whole body is a name
LOC_UNKNOWN = "UNKNOWN"

# ── What a reader of that location may conclude. ───────────────────────────────────
# 🔴 These are deliberately NOT ordered on a single axis.  A code header gives family
# AND bound and no terms; a bare token gives family and NEITHER bound nor terms; a
# filed payload gives all three.  A consumer that collapses them to "has licence:
# yes/no" reproduces the `p258` CC defect at a different layer.
STRENGTH = {
    LOC_LICENCE_FILE:       ("family", "bound", "terms"),
    LOC_CODE_HEADER:        ("family", "bound"),
    LOC_APP_MANIFEST:       ("family",),
    LOC_ECOSYSTEM_MANIFEST: ("family", "bound"),
    LOC_BARE_TOKEN:         ("family",),
    LOC_UNKNOWN:            (),
}

# Application manifests that carry a licence ELEMENT of their own.  Closed set, and
# every member was read first-hand at p259 or is pinned by a control.
#   `appinfo/info.xml`  Nextcloud app manifest -> `<licence>agpl</licence>`
APP_MANIFESTS = ("appinfo/info.xml",)

# Ecosystem manifests: `p222` already owns their grammar.  Listed here only so that
# `location_class` can route to it rather than guess.
ECOSYSTEM_MANIFESTS = (
    "composer.json", "package.json", "pyproject.toml", "DESCRIPTION",
    "__manifest__.py", "setup.py", "setup.cfg", "Cargo.toml", "pubspec.yaml",
)

# 🔴 `version.php` is in NEITHER list, and that is the whole point.  It is a manifest
# by path-class and a code header by content, so it is resolved by CONTENT below.
DUAL_PATHS = ("version.php", "pom.xml")

_SOURCE_EXT = (
    ".php", ".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rb", ".java", ".c", ".h",
    ".cc", ".cpp", ".cs", ".rs", ".kt", ".swift", ".sh", ".pl", ".lua", ".scala",
)

_LICENCE_BASENAMES = (
    "license", "licence", "copying", "notice", "license-code", "mit-license",
    "license-mit", "license-apache", "apache-license-2.0",
)

# The operative words of a GRANT, as opposed to a POINTER to one.  `p254` established
# that a pointer is not a grant; these are the phrases that make a header the thing
# itself.  Every one of them appears in a payload p259 read first-hand.
_GRANT_PHRASES = (
    r"is free software",
    r"you can redistribute it and/or modify",
    r"released under the terms of",
    r"licensed under the",
    r"under the terms of the",
    r"permission is hereby granted",
)

# A pointer, and nothing more.  🔴 `OS4ED/openSIS-Classic`'s header carries BOTH: a
# grant sentence AND "See license.txt." — a pointer whose target does not exist at any
# of the 26 Tier-A paths, in six spellings, or anywhere in the repository.  So the
# presence of a pointer may never downgrade a grant that is present beside it.
_POINTER_PHRASES = (
    r"see\s+the?\s*licen[cs]e(\s+file)?",
    r"see\s+licen[cs]e(\.[a-z]+)?\b",
    r"for\s+(the\s+)?full\s+licen[cs]e",
    r"copy\s+of\s+the\s+licen[cs]e\s+(is\s+)?(at|in)",
)

_SPDX_TAG = re.compile(r"SPDX-License-Identifier:\s*([^\s*/#]+)", re.I)

# A licence file whose entire body is a name.  `p1049-bare-token-grant` owns the class;
# this threshold is the one p259 measured: `frappe/education/license.txt` is 19 bytes
# and reads `License: GNU GPL V3`.
BARE_TOKEN_MAX_BYTES = 120


def _basename(path):
    return (path or "").rsplit("/", 1)[-1]


def _is_licence_name(path):
    base = _basename(path).lower()
    stem = base.split(".")[0]
    return stem in _LICENCE_BASENAMES or base in _LICENCE_BASENAMES


def location_class(path, payload=None):
    """Grade WHERE this payload was found.

    `payload` is optional, and the two arguments are not interchangeable: a path alone
    cannot separate a bare token from a filed grant, and for the dual paths it cannot
    separate a manifest from a code header either.  A caller that has the body should
    pass it; a caller that does not gets the path-only answer and must not treat it as
    the same thing.
    """
    path = (path or "").lstrip("./")
    low = path.lower()

    if low in [m.lower() for m in APP_MANIFESTS]:
        return LOC_APP_MANIFEST

    if _is_licence_name(path) and not low.endswith(_SOURCE_EXT):
        if payload is not None and len(payload.encode("utf-8")) <= BARE_TOKEN_MAX_BYTES:
            return LOC_BARE_TOKEN
        return LOC_LICENCE_FILE

    if low in [m.lower() for m in DUAL_PATHS]:
        # Resolved by CONTENT, because this path is both things at once.
        if payload is not None and has_grant_notice(payload):
            return LOC_CODE_HEADER
        return LOC_ECOSYSTEM_MANIFEST

    if low in [m.lower() for m in ECOSYSTEM_MANIFESTS]:
        return LOC_ECOSYSTEM_MANIFEST

    if low.endswith(_SOURCE_EXT):
        if payload is not None and has_grant_notice(payload):
            return LOC_CODE_HEADER
        return LOC_UNKNOWN

    return LOC_UNKNOWN


def header_block(payload, max_lines=40):
    """The leading comment block of a source file, as text.

    Stops at the first line that is neither a comment nor blank nor a shebang nor a
    PHP open tag — so a grant notice that sits BELOW the first statement is not read,
    which is correct: that is no longer the file's header.
    """
    out = []
    for i, line in enumerate(str(payload or "").splitlines()):
        if i >= max_lines:
            break
        s = line.strip()
        if not s or s in ("<?php", "<?", "?>") or s.startswith("#!"):
            out.append(s)
            continue
        if s.startswith(("//", "#", "/*", "*", "*/", "<!--", "--", ";")):
            out.append(s.lstrip("/*#;-<!").strip())
            continue
        break
    return "\n".join(out)


def has_grant_notice(payload):
    """Does this payload's HEADER carry the operative words of a grant?

    🔴 Deliberately reads the header block only.  A 45 KB PHP application whose body
    happens to contain "licensed under the" in a help string is not thereby licensed,
    and `OS4ED/openSIS-Classic/index.php` — the real payload that motivated this — is
    45 523 bytes of which the grant is the first 18 lines.
    """
    block = header_block(payload).lower()
    return any(re.search(p, block) for p in _GRANT_PHRASES)


def has_pointer(payload):
    block = header_block(payload).lower()
    return any(re.search(p, block) for p in _POINTER_PHRASES)


def spdx_tag(payload):
    m = _SPDX_TAG.search(header_block(payload))
    return m.group(1) if m else None


def reading_strength(loc):
    """What a reader of this location class may conclude.  Never a boolean."""
    return STRENGTH.get(loc, ())


def may_conclude(loc, what):
    return what in reading_strength(loc)


# ── The absence predicate.  `p259`'s half of `p258`'s lesson. ──────────────────────
ABSENCE_CONFIRMED = "ABSENCE-CONFIRMED"
ABSENCE_UNCONFIRMED = "ABSENCE-UNCONFIRMED"
ABSENCE_REFUTED = "ABSENCE-REFUTED"


def absence_verdict(observations):
    """Grade a claim that a repository has no readable grant.

    `observations` is a sequence of HTTP status codes from INDEPENDENT attempts at the
    same (slug, ref, path-set).  One 404 is an attempt, not a property:

      any 200          -> ABSENCE-REFUTED
      >= 2 non-200     -> ABSENCE-CONFIRMED
      exactly 1 non-200 -> ABSENCE-UNCONFIRMED   (and may NOT be published as absence)

    🔴 Measured, not stipulated.  p258 recorded `frappe/education` as
    `NO-PAYLOAD-ON-LADDER` after 26 probes; p259 re-ran Tier A on the same ref and got
    `200` at position 13 on a file committed 2022-04-27.  13 of p258's other 14
    absences reproduced exactly, so the ladder is sound and the SINGLE-OBSERVATION
    RULE is what was missing.
    """
    obs = [int(o) for o in observations]
    if not obs:
        return ABSENCE_UNCONFIRMED
    if any(o == 200 for o in obs):
        return ABSENCE_REFUTED
    if len(obs) >= 2:
        return ABSENCE_CONFIRMED
    return ABSENCE_UNCONFIRMED


def publishable_as_absence(observations):
    return absence_verdict(observations) == ABSENCE_CONFIRMED


# ── Why a grant that EXISTS was not found.  The four causes p259 measured. ─────────
CAUSE_BODY_NOT_GRADED = "BODY-NOT-GRADED"
CAUSE_TIER_NOT_RUN = "TIER-NOT-RUN"
CAUSE_CHANNEL_ABSENT = "CHANNEL-ABSENT"
CAUSE_ABSENCE_UNCONFIRMED = "ABSENCE-UNCONFIRMED"
CAUSE_REALLY_ABSENT = "REALLY-ABSENT"

CAUSES = (
    CAUSE_BODY_NOT_GRADED, CAUSE_TIER_NOT_RUN, CAUSE_CHANNEL_ABSENT,
    CAUSE_ABSENCE_UNCONFIRMED, CAUSE_REALLY_ABSENT,
)

# 🔴 Only ONE of the five is a missing path, and two passes (p257, p258) spent 590
# probes widening the list of path NAMES.  That is the measurement this constant
# exists to keep in front of the next pass.
CAUSES_A_LONGER_PATH_LIST_FIXES = (CAUSE_CHANNEL_ABSENT,)


def miss_cause(path_on_ladder, tier_run, body_graded, reprobe_found):
    """Why did a grant that exists read as absent?

    Arguments are the four facts a probe already has, so this is a classification of
    evidence and not an opinion.
    """
    if reprobe_found and tier_run and path_on_ladder:
        return CAUSE_ABSENCE_UNCONFIRMED
    if not path_on_ladder:
        return CAUSE_CHANNEL_ABSENT
    if not tier_run:
        return CAUSE_TIER_NOT_RUN
    if not body_graded:
        return CAUSE_BODY_NOT_GRADED
    return CAUSE_REALLY_ABSENT


# ── The Nextcloud app-manifest grammar.  One element, a closed vocabulary. ─────────
_NC_LICENCE = re.compile(r"<licence>\s*([^<\s]+)\s*</licence>", re.I)
_NC_LICENSE = re.compile(r"<license>\s*([^<\s]+)\s*</license>", re.I)

# 🔴 Both spellings, because the element is `<licence>` in Nextcloud's own schema and
# a reader that only knows the American spelling silently returns None — which this
# base would then record as "no licence" and publish as a gap.
NC_VOCAB = {
    "agpl": "AGPL", "gpl": "GPL", "mit": "MIT", "apache": "Apache",
    "bsd": "BSD", "mpl": "MPL",
}


def app_manifest_licence(payload):
    """Read the licence element of an application manifest.

    Returns `(family, bound)` or `(None, None)`.  🔴 `bound` is ALWAYS `'unspecified'`
    when a family is found: `<licence>agpl</licence>` names no version, so AGPL-3.0 and
    AGPL-1.0 are indistinguishable here.  Returning `'AGPL-3.0'` from this channel
    would be an inference dressed as a reading.
    """
    text = str(payload or "")
    m = _NC_LICENCE.search(text) or _NC_LICENSE.search(text)
    if not m:
        return (None, None)
    fam = NC_VOCAB.get(m.group(1).strip().lower())
    if fam is None:
        return (None, None)
    return (fam, "unspecified")
