"""Grade a SERVED licence payload into a commercial verdict. Pure functions, no I/O.

🔵 Why this exists. `Gap 520-B` recorded that `NOASSERTION` was the largest blocker on these
shelves and that no channel in `p519`'s session could read a served byte. A channel CAN be read
in this one (`curl` -> `raw.githubusercontent.com`, the same channel `p504` used), so the blocked
rows are gradeable again. This module turns payload bytes into a verdict a studio can act on.

🔴 The instrument finding that shaped the design, and it CORRECTS `p455`. `p455` anchored its
reader on the title block, on the stated ground that it is "the only region of a payload a
preamble cannot reach". `claroline/Claroline` is the counterexample: line 1 reads
`Claroline Connect License` -- a name no SPDX id matches -- while four lines down, INSIDE the same
title window, sits a verbatim `GNU AFFERO GENERAL PUBLIC LICENSE`. So a title *window* cannot tell
a wrapper from a clean grant; it sees a standard name either way. The HEADLINE -- line 1 alone --
can.

🟢 The rule is therefore two-stage and ordered: a recognised STANDARD BODY outranks an
unrecognised HEADLINE. A bespoke headline over a standard body is a WRAPPER and the grant is the
body's. A bespoke headline over a body that matches nothing stays BESPOKE. Nothing is guessed in
either direction: an unmatched payload grades `UNSTATED`, never "probably fine".

Verdicts:
  PERMISSIVE                  -- MIT / Apache-2.0 / BSD: buildable commercially, with attribution
  COPYLEFT                    -- GPL / AGPL / LGPL: buildable, obligations propagate
  SHAREALIKE_CONTENT          -- CC BY-SA: commercial use allowed, ShareAlike binds derivatives
  NON_COMMERCIAL_REFUSED      -- CC BY-NC or a bespoke non-commercial grant: NOT for paid work
  SOURCE_AVAILABLE_RESTRICTED -- Elastic / BSL-shaped: source open, hosting or field restricted
  UNSTATED                    -- matched nothing. A refusal, not a grade.
"""

TITLE_LINES = 12

# 🔴 A TIGHTER window, for GNU family discrimination only. 12 lines is wide enough to swallow a
# cross-reference: a GPL payload whose section 13 sits near the top would still be misread. A real
# GNU licence names itself in its first two non-blank lines ("GNU ... PUBLIC LICENSE" / "Version
# N, date"), and the widest legitimate case on these shelves is `claroline/Claroline`, whose
# wrapper pushes the AGPL title down to line 4. Six lines covers that and excludes the body.
GNU_TITLE_LINES = 6

STANDARD_NAMES = (
    "mit license",
    "apache license",
    "gnu general public",
    "gnu affero",
    "gnu lesser",
    "bsd",
    "elastic license",
    "attribution-noncommercial",
    "attribution-sharealike",
    "creative commons",
    "mozilla public",
)

# 🔴 The GNU family MUST be read from the title region, never from the body, and a control pins
# why: canonical GPL-3.0 cross-references the AGPL in its own section 13 ("Remote Network
# Interaction; Use with the GNU Affero General Public License"), and LGPL incorporates the GPL by
# reference. So a body-order match grades verbatim GPL-3.0 as AGPL-3.0 -- which is what this
# grader did until `chamilo/chamilo-lms`, a positive control with an independently known answer,
# DISAGREED. Each GNU text names its siblings; only the title says which one you were handed.
GNU_TITLE_SIGNATURES = (
    ("gnu affero general public license", "AGPL", "COPYLEFT"),
    ("gnu lesser general public license", "LGPL", "COPYLEFT"),
    ("gnu general public license", "GPL", "COPYLEFT"),
)

# (needle in body, spdx, verdict). Non-GNU families only. Ordered: NonCommercial before
# ShareAlike, since a CC BY-NC-SA payload names both.
BODY_SIGNATURES = (
    ("attribution-noncommercial", "CC-BY-NC-4.0", "NON_COMMERCIAL_REFUSED"),
    ("attribution-sharealike", "CC-BY-SA-4.0", "SHAREALIKE_CONTENT"),
    ("elastic license 2.0", "Elastic-2.0", "SOURCE_AVAILABLE_RESTRICTED"),
    ("apache license", "Apache-2.0", "PERMISSIVE"),
    ("permission is hereby granted, free of charge", "MIT", "PERMISSIVE"),
    ("redistribution and use in source and binary forms", "BSD", "PERMISSIVE"),
)

NON_COMMERCIAL_MARKERS = ("non-commercial", "noncommercial")


def _norm(text):
    return " ".join(text.lower().split())


def title_block(text):
    """The first TITLE_LINES non-blank lines, lowercased. A preamble cannot reach here."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return " \n".join(lines[:TITLE_LINES]).lower()


def gnu_title_region(text):
    """The first GNU_TITLE_LINES non-blank lines, normalised. Where a GNU licence names itself."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return _norm(" ".join(lines[:GNU_TITLE_LINES]))


def headline(text):
    """The FIRST non-blank line alone, lowercased. See the wrapper note in the module docstring."""
    for line in text.splitlines():
        if line.strip():
            return line.strip().lower()
    return ""


def names_standard(region):
    """True if this region of the payload names a licence an SPDX id matches."""
    return any(k in region for k in STANDARD_NAMES)


def gnu_version(text):
    """GPL/AGPL/LGPL version, read from the title region. `p455`'s version axis."""
    region = _norm(title_block(text))
    for version, needle in (("3.0", "version 3"), ("2.1", "version 2.1"), ("2.0", "version 2")):
        if needle in region:
            return version
    return "UNSTATED"


def gnu_or_later(text):
    """`GPL-2.0-only` cannot combine forward; `-or-later` can. `p455` read this axis; so do we."""
    body = _norm(text)
    if "any later version" in body:
        return "or-later"
    return "UNSTATED"


def grade(text):
    """payload text -> dict(spdx, verdict, basis). Never guesses."""
    title = title_block(text)
    body = _norm(text)

    # A bespoke non-commercial grant: no standard name in the title window AND the body restricts
    # commercial use in its own words. Graded FIRST, because such licences commonly borrow MIT's
    # "permission is hereby granted" opening and a body-order match would call them permissive.
    if not names_standard(title) and any(m in body for m in NON_COMMERCIAL_MARKERS):
        return {
            "spdx": "BESPOKE-NC",
            "verdict": "NON_COMMERCIAL_REFUSED",
            "basis": "no standard licence named in the title window; body restricts commercial use",
        }

    matched = None
    # GNU first, anchored on the title region -- see GNU_TITLE_SIGNATURES.
    gnu_region = gnu_title_region(text)
    for needle, family, verdict in GNU_TITLE_SIGNATURES:
        if needle in gnu_region:
            matched = (family, verdict)
            break
    if matched is None:
        for needle, spdx, verdict in BODY_SIGNATURES:
            if needle in body:
                matched = (spdx, verdict)
                break

    if matched is None:
        return {
            "spdx": "UNSTATED",
            "verdict": "UNSTATED",
            "basis": "payload matched no known licence body",
        }

    spdx, verdict = matched
    if spdx in ("GPL", "AGPL", "LGPL"):
        spdx = "%s-%s" % (spdx, gnu_version(text))

    if spdx.startswith(("GPL-", "AGPL-", "LGPL-")):
        basis = "standard GNU body; version from title region; election=%s" % gnu_or_later(text)
    else:
        basis = "standard %s body matched" % spdx

    if not names_standard(headline(text)):
        basis = "WRAPPER: bespoke headline over a verbatim %s body; the body is the grant" % spdx

    return {"spdx": spdx, "verdict": verdict, "basis": basis}


def permissive(verdict):
    return verdict == "PERMISSIVE"


def buildable_for_paid_client_work(verdict):
    """The question a studio actually asks. NON_COMMERCIAL is the one hard NO."""
    return verdict in ("PERMISSIVE", "COPYLEFT", "SHAREALIKE_CONTENT")
