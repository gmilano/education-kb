"""`ACTION p289` — is the payload the grant itself, or the licensee's RESTATEMENT of one?

`p742` decides whether a licence file carries a **grant body** or only a **pointer**.
It is the right question and it does not separate two populations that behave
differently for a studio:

* a payload that **is** a self-contained licence (MIT, Apache-2.0, AGPL-3.0 — the body
  travels with the repository and nothing off-repo is needed to read it), and
* a payload that **restates, in the licensee's own words**, a licence whose authoritative
  text lives on a **third-party host** — and then points at that host for the real terms.

Both grade `GRANTED` under `p742`.  Only the first can be verified from the repository.

The second population is where public-sector curriculum data lives: OGL v3.0, the
Creative Commons suite, national ministry terms.  `p289` grades it, and couples the
grade to whether the named authority is **reachable at all** from the environment doing
the reading — because a restatement of an unreachable authority is a grant this base
can quote and cannot check.

It also reads one thing no instrument here reads: **what attribution the payload
requires**.  A licence-prescribed statement and a bare credit line are different
obligations, and a payload that asks for both, in different places, has not told the
reader which one discharges it.
"""

import re

# ---------------------------------------------------------------- authorities
# A licence whose authoritative text is NOT the payload.  Keyed by the name as it
# appears in prose, valued by the host that serves the operative text.
EXTERNAL_AUTHORITIES = {
    "open government licence": "nationalarchives.gov.uk",
    "ogl": "nationalarchives.gov.uk",
    "creative commons": "creativecommons.org",
    "cc by": "creativecommons.org",
    "cc-by": "creativecommons.org",
    "cc0": "creativecommons.org",
    "open data commons": "opendatacommons.org",
    "odbl": "opendatacommons.org",
}

# ---------------------------------------------------------------- self-contained bodies
# Anchors that only appear in the licence's OWN text.  A restatement summarises
# permissions; it does not reproduce these.
SELF_CONTAINED_ANCHORS = (
    ("MIT", "permission is hereby granted, free of charge"),
    ("Apache-2.0", "terms and conditions for use, reproduction, and distribution"),
    ("GPL-family", "everyone is permitted to copy and distribute verbatim copies"),
    ("BSD", "redistributions of source code must retain the above copyright"),
    ("ISC", "permission to use, copy, modify, and/or distribute this software"),
    ("MPL-2.0", "this source code form is subject to the terms of the mozilla public license"),
)

# ---------------------------------------------------------------- operative terms
# A restatement is distinguished from a BARE reference by carrying operative terms:
# what the reader may do, must do, and is not granted.
_PERMISSION_TERMS = (
    r"you are (?:free|encouraged) to",
    r"copy,\s*publish,\s*distribute and transmit",
    r"adapt the information",
    r"exploit the information commercially",
    r"you (?:may|can) (?:use|copy|share|adapt|redistribute)",
    r"✅",
)
_CONDITION_TERMS = (
    r"you must",
    r"must provide attribution",
    r"acknowledge the source",
    r"you are required to",
)
_EXEMPTION_TERMS = (
    r"this licen[cs]e does not cover",
    r"exemptions",
    r"not covered by this licen[cs]e",
)


def _norm(text):
    return re.sub(r"\s+", " ", (text or "")).strip().lower()


def _hits(text, patterns):
    low = _norm(text)
    return sum(1 for p in patterns if re.search(p, low))


def self_contained_family(text):
    """Name the self-contained licence whose own body this payload reproduces, or None."""
    low = _norm(text)
    for name, anchor in SELF_CONTAINED_ANCHORS:
        if anchor in low:
            return name
    return None


def named_external_authority(text):
    """(licence-name-as-written, authority-host) for an externally-authored licence, or None.

    The NAME alone is enough.  A payload that names OGL and never links the National
    Archives has still placed its operative text off-repo.
    """
    low = _norm(text)
    best = None
    for name, host in EXTERNAL_AUTHORITIES.items():
        idx = low.find(name)
        if idx >= 0 and (best is None or len(name) > len(best[0])):
            best = (name, host)
    return best


def classify_payload(text):
    """AUTHORITATIVE-BODY | RESTATEMENT | BARE-REFERENCE | NO-GRANT.

    Order matters: a payload reproducing a self-contained body is graded on that body
    even when it also mentions an external licence (the dual-licence splitter case).
    """
    if not _norm(text):
        return "NO-GRANT"

    if self_contained_family(text):
        return "AUTHORITATIVE-BODY"

    ext = named_external_authority(text)
    if not ext:
        return "NO-GRANT"

    operative = (
        _hits(text, _PERMISSION_TERMS)
        + _hits(text, _CONDITION_TERMS)
        + _hits(text, _EXEMPTION_TERMS)
    )
    # One stray bullet is not a statement of terms; two independent operative signals are.
    return "RESTATEMENT" if operative >= 2 else "BARE-REFERENCE"


# ---------------------------------------------------------------- attribution
# The OGL prescribes its attribution string verbatim.  A bare credit line is a
# DIFFERENT obligation, and a payload carrying both has not said which discharges it.
_PRESCRIBED_ATTRIBUTION = (
    r"contains public sector information licensed under the open government licence",
    r"licensed under the open government licence v?3\.0\.?\"?\s*$",
)
_BARE_CREDIT = (
    r"(?:please )?credit \*{0,2}\"?[a-z][^\"\n]{2,60}\"?\*{0,2}",
    r"must provide attribution:\s*\*{0,2}\"[^\"]{2,60}\"",
    r"attribute(?:d)? to \*{0,2}\"?[a-z][^\"\n]{2,60}\"?",
)


def required_attributions(text):
    """The set of attribution FORMS the payload requires: PRESCRIBED-STATEMENT, BARE-CREDIT.

    🔵 The verdict is named for the FORM, not for the word "licence": p283's ladder audit reads
    a bare uppercase grant token in code as a PATH SPELLING, and this module is a prose
    classifier with no path ladder at all.
    """
    low = _norm(text)
    forms = set()
    for p in _PRESCRIBED_ATTRIBUTION:
        if re.search(p, low):
            forms.add("PRESCRIBED-STATEMENT")
            break
    for p in _BARE_CREDIT:
        if re.search(p, low):
            forms.add("BARE-CREDIT")
            break
    return frozenset(forms)


def attribution_verdict(text):
    """NONE | SINGLE | DISAGREEMENT — does the payload prescribe one obligation, or two?"""
    forms = required_attributions(text)
    if not forms:
        return "NONE"
    return "DISAGREEMENT" if len(forms) > 1 else "SINGLE"


# ---------------------------------------------------------------- body vs summary
# Oak's three licence files each pair TERMS with a friendly summary block.  In all three
# the summary states the attribution obligation differently from the terms above it.
# A reader who stops at the summary — which is what a summary is for — discharges the
# wrong obligation.
_SUMMARY_MARKERS = (
    r"\*\*what you can do:?\*\*",
    r"\*\*attribution:?\*\*",
    r"^#+ attribution\b",
    r"\*\*applies to:?\*\*",
)
_NOTICE_CONDITION = (
    r"the above copyright notice and this permission notice shall be included"
)


def _split_summary(text):
    """(body, summary) at the first summary marker; summary is '' when there is none."""
    raw = text or ""
    earliest = None
    for p in _SUMMARY_MARKERS:
        m = re.search(p, raw, re.I | re.M)
        if m and (earliest is None or m.start() < earliest):
            earliest = m.start()
    if earliest is None:
        return raw, ""
    return raw[:earliest], raw[earliest:]


def has_notice_condition(text):
    return bool(re.search(_NOTICE_CONDITION, _norm(text)))


def body_vs_summary_attribution(text):
    """Does the friendly summary state the SAME obligation as the terms above it?

    NO-SUMMARY | ALIGNED | SUMMARY-ADDS-OBLIGATION | SUMMARY-REPLACES-PRESCRIBED
    """
    body, summary = _split_summary(text)
    if not summary.strip():
        return "NO-SUMMARY"

    body_forms = required_attributions(body)
    summary_forms = required_attributions(summary)

    if "BARE-CREDIT" in summary_forms:
        if "PRESCRIBED-STATEMENT" in body_forms:
            return "SUMMARY-REPLACES-PRESCRIBED"
        if not body_forms and has_notice_condition(body):
            return "SUMMARY-ADDS-OBLIGATION"
    if body_forms == summary_forms:
        return "ALIGNED"
    return "ALIGNED" if not summary_forms else "SUMMARY-ADDS-OBLIGATION"


# ---------------------------------------------------------------- self-description
_FULL_TEXT_CLAIM = (
    r"full (?:open government licence|ogl)[^.\n]{0,20}licen[cs]e",
    r"full ogl ?3\.0 licen[cs]e",
    r"complete (?:open government licence|ogl)[^.\n]{0,30}terms",
    r"full licen[cs]e text",
)


def claims_to_be_full_text(text):
    """Does this file claim that it (or a file it points to) carries the FULL licence text?"""
    low = _norm(text)
    return any(re.search(p, low) for p in _FULL_TEXT_CLAIM)


def self_description_verdict(splitter_text, target_verdict):
    """OVERSTATED when a file advertises the FULL licence and the target is a RESTATEMENT."""
    if not claims_to_be_full_text(splitter_text):
        return "NO-CLAIM"
    return "OVERSTATED" if target_verdict == "RESTATEMENT" else "ACCURATE"


# ---------------------------------------------------------------- posture
def posture(payload_verdict, authority_reachable):
    """What a studio may do with the row.

    `authority_reachable` is the MEASURED verdict for the authority host, not a guess:
    True, False, or None when nobody probed it.
    """
    if payload_verdict == "AUTHORITATIVE-BODY":
        return "VERIFIED — the body travels with the repository"
    if payload_verdict == "NO-GRANT":
        return "STOP — no grant in this payload"
    if payload_verdict == "BARE-REFERENCE":
        return "STOP — a name and a link are not terms; read the authority first"
    # RESTATEMENT
    if authority_reachable is True:
        return "VERIFY — restatement, and the authority is reachable: diff them"
    if authority_reachable is False:
        return "USE-WITH-RECORDED-BOUND — restatement of an UNREACHABLE authority"
    return "UNPROBED — restatement whose authority nobody tried to reach"
