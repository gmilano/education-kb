#!/usr/bin/env python3
"""p202 — the scope reader `ACTION OJ` justified and `ACTION OR` registered.

The question is not "what licence is this repo?" but "what grant covers the PATH
I am about to ship?". In education that distinction is not pedantry: the asset a
studio wants is often CONTENT (curriculum, docs, SKILL.md payloads), and content
is licensed from a different instrument family (Creative Commons) than code.

`ACTION OR`'s falsifier was whether the shared preamble defeats a reader.
Measured: it does not. `pupilfirst` and `leemons` share a TEMPLATE, and the
discriminator is the licence named inside the FALLBACK clause, which differs.

Offline. Licence FAMILY naming stays with lib/license_family.sh -- this module
answers scope, not family (P237).
"""
import re

# The fallback clause: "Content outside of the above mentioned [files or]
# restrictions is available under the "X" license as defined below."
_FALLBACK = re.compile(
    r"content\s+outside\s+of\s+the\s+above\s+mentioned\s+"
    r"(?:files\s+or\s+)?restrictions\s+is\s+available\s+under\s+the\s+"
    r"[\"“']([^\"”']+)[\"”']",
    re.I,
)
_PREAMBLE = re.compile(r"portions\s+of\s+this\s+software\s+are\s+licensed\s+as\s+follows", re.I)

# A scope line names a path or a code-class and a licence for it.
_SCOPE_LINE = re.compile(
    r"^\s*[-*]\s*(?P<body>.+)$", re.M)
_PATH_IN = re.compile(r"[\"`']?(?P<path>[A-Za-z0-9_.\-/]+/)[\"`']?")
_LICENCE_NAME = re.compile(
    r"\b(MIT|Apache[\s\-]?2\.0|BSD[\s\-]?\d?|AGPL[\s\-]?3\.0|GPL[\s\-]?[23]\.0"
    r"|LGPL[\s\-]?3\.0|ECL[\s\-]?2\.0|MPL[\s\-]?2\.0)\b", re.I)
# "either A or B, at your option" / "A OR B" -- a dual grant, not a sequence.
_DUAL = re.compile(r"\beither\b|\bor\b.*\bat\s+your\s+option\b|\bOR\b", re.I)

# Content-licence families. A CC grant on a software path is a finding, not a
# detail: CC licences carry no patent grant and Creative Commons itself advises
# against using them for software.
_CONTENT_FAMILIES = [
    ("CC-BY-SA", r"\bcc[\s\-]?by[\s\-]?sa\b|attribution[\s\-]share\s?alike"),
    ("CC-BY-NC", r"\bcc[\s\-]?by[\s\-]?nc\b|noncommercial|non-commercial"),
    ("CC-BY-ND", r"\bcc[\s\-]?by[\s\-]?nd\b|no\s?derivatives"),
    ("CC-BY", r"\bcc[\s\-]?by\b|creative\s+commons\s+attribution"),
    ("CC0", r"\bcc0\b"),
]
# Grants that are NOT OSI-approved however open they present.
_NON_OSI = [
    ("FAIRCODE", r"fair\s?code\s+licen[cs]e"),
    ("SUSTAINABLE-USE", r"sustainable\s+use\s+licen[cs]e"),
]


def has_split_scope_preamble(text):
    """Does this notice announce per-scope grants at all?"""
    return bool(_PREAMBLE.search(text or ""))


def fallback_grant(text):
    """The grant covering everything the exceptions do not. None if unstated.

    This is the field that distinguishes two notices built from the same
    template, and it is the one a repo-level licence column silently reports.
    """
    m = _FALLBACK.search(text or "")
    return m.group(1).strip() if m else None


def content_family(name):
    """Name the content-licence family of a grant string, or None."""
    n = (name or "").lower()
    for fam, pat in _CONTENT_FAMILIES:
        if re.search(pat, n):
            return fam
    return None


def non_osi_family(name):
    n = (name or "").lower()
    for fam, pat in _NON_OSI:
        if re.search(pat, n):
            return fam
    return None


def scopes(text):
    """Every (scope, grant) the notice states, as written.

    `scope` is a path when the line names one, else the line's subject text.
    No inference: a line that names no licence is returned with grant None, so a
    caller cannot mistake silence for a grant.
    """
    out = []
    for m in _SCOPE_LINE.finditer(text or ""):
        body = m.group("body").strip()
        if _FALLBACK.search(body):
            continue  # the fallback is not a scope; it is the remainder
        pm = _PATH_IN.search(body)
        scope = pm.group("path") if pm else body[:60]
        grant = None
        cf = content_family(body)
        nf = non_osi_family(body)
        if cf:
            grant = cf
        elif nf:
            grant = nf
        else:
            names = [n.upper().replace(" ", "-") for n in _LICENCE_NAME.findall(body)]
            # A dual grant is the whole point of reading scope: "AGPL-3.0 OR MIT,
            # at your option" means the licensee MAY take MIT, so the payload is
            # shippable in a closed deliverable. Collapsing it to the first name
            # loses exactly the fact that decides shippability.
            seen = []
            for n in names:
                if n not in seen:
                    seen.append(n)
            if len(seen) >= 2 and _DUAL.search(body):
                grant = "-OR-".join(seen)
            elif seen:
                grant = seen[0]
            elif re.search(r"original\s+licen[cs]e\s+provided\s+by", body, re.I):
                grant = "UPSTREAM-OWN"
        out.append((scope, grant))
    return out


def classify(text):
    """The row a pass may publish. Every field is read, none inferred."""
    fb = fallback_grant(text)
    sc = scopes(text)
    content_scopes = [(s, g) for s, g in sc if g and content_family(g)]
    return {
        "split_scope": has_split_scope_preamble(text),
        "fallback": fb,
        "fallback_content_licence": content_family(fb) if fb else None,
        "fallback_non_osi": non_osi_family(fb) if fb else None,
        "scopes": sc,
        "content_scopes": content_scopes,
        # The finding a repo-level column hides: code and content on one repo
        # under different instrument families.
        "code_content_split": bool(content_scopes) and bool(fb) and not content_family(fb),
    }
