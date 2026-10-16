#!/usr/bin/env python3
"""`p246-payload-integrity` — two questions that must be answered BEFORE a family verdict is
trusted, and that no instrument on these shelves asked until pass 246.

    1. ROLE  — is the licence name this payload matched the licence that GOVERNS the payload,
               or is it a licence named in a PARAMETER, applying later or elsewhere?
    2. STATE — is this payload ONE resolved grant, or an unresolved merge of two?

Why this exists (pass 246 del 2026-10-16)
-----------------------------------------

🔴 **THE ROLE FINDING.** `lib/license_family.sh::family_of` answered `Apache-2.0` on
`IAGA-TEAM/IAGA-Sentinel` (`196` stars, `4 913` B), and `commercial_use_ok` then answered
**ALLOWED**. The payload is **Business Source License 1.1** — source-available, NOT OSI — whose
`Additional Use Grant` forbids offering the work *"to third parties as a hosted or managed
service"*, and which says in its own text that a commercial licence must be bought from the
Licensor. A studio that trusted that cell would have offered a client a managed service it has
no right to sell until the `Change Date`, **2030-05-03**.

🟢 The classifier is not missing a `BUSL` branch. **It has one, at line `646`** — and it is
unreachable. BSL 1.1 carries a mandatory `Change License:` parameter naming the licence the
work converts to, and every OSI anchor sits ABOVE line `646`:

    EUPL 154 · MPL 244 · EPL 253 · GPL/AGPL/LGPL 313-371 · Apache 378 · BSD 459 · MIT 503
    CC 565 · ....................................................... BUSL 646

So the FIRST licence name a BSL payload matches is the one in its own `Change License` field,
and `family_of` returns before reaching the branch that would have been right. Measured both
ways, so the claim is not Apache-specific:

    Change License: Apache License, Version 2.0   -> family_of = Apache-2.0  (commercial ALLOWED)
    Change License: GNU GPL, Version 2.0 or later -> family_of = GPL-2.0     (commercial ALLOWED)

🔵 **The class, stated once:** *a licence name in a PARAMETER position is not this payload's
grant.* `Change License` names the grant this work does **not** carry yet. The anchor reads a
field describing a FUTURE licence as the licence in force today. This is the same family of
defect `p240` (language), `p241` (absence of restriction vocabulary) and `P250`/`P312`
(family-implies-commercial) each found on a different axis: **a matcher that reads a token and
never asks what role the token plays in the document.**

🟢 Blast radius, measured and not assumed: **`0` of the `308` carried `Apache-2.0` payloads
re-read first-hand this pass contain the string `Business Source License`.** No published row
flips. The defect is live, the exposure today is nil, and the gate is here so it stays nil.

🔴 **THE STATE FINDING.** `0xnavarro/IA-PARA-TODOS` ships a root `LICENSE` of `11 471` B whose
APPENDIX is an **unresolved git merge conflict** — `<<<<<<< HEAD`, `=======`,
`>>>>>>> 32db549aa17acfc812d4175d983a95945a02b728` — carrying BOTH

    Copyright 2024 0xnavarro - IA-PARA-TODOS        <- the real holder, HEAD side
    Copyright [yyyy] [name of copyright owner]      <- the untouched ASF template, other side

🔴 `p245-apache-canonical` grades it **CANONICAL** *(title, grant sentence and all three
deviation anchors are intact — the conflict is in the appendix, after the terms)*, and
🔴 `holder_of` answers **NOT-APPLICABLE** on a payload that DOES carry a holder line. That
second one is `p241`'s own fix inverted: `p241` taught `holder_of` to ignore the ASF
template-bracket form, and a conflicted payload contains the template form **and** the real
form at once, so the exclusion eats the real answer.

🔵 Attribution is exactly what `Apache-2.0` §4 obliges a redistributor to preserve, and this
payload does not say who to attribute — it offers two candidates and a conflict marker. It is
not a resolved grant, whatever its family. Base rate measured: **`1` of the `321` payloads read
first-hand this pass** (`308` carried Apache + `13` new rows).

P237's rule is kept: this file has NO family classifier. It answers ROLE and STATE and hands
the family question back to `lib/license_family.sh`.
"""
import re
import sys

# ── STATE ──────────────────────────────────────────────────────────────────────────────────
# Anchored at line start. `=======` alone is not a marker: a licence may legitimately underline
# a heading with `=`. The opening and closing markers are what no licence text contains.
_CONFLICT_OPEN = re.compile(r"^<{7}(?:[ \t]|$)", re.MULTILINE)
_CONFLICT_CLOSE = re.compile(r"^>{7}(?:[ \t]|$)", re.MULTILINE)
_CONFLICT_MID = re.compile(r"^={7}[ \t]*$", re.MULTILINE)

# The ASF template holder line, which `p241` taught `holder_of` to exclude.
_TEMPLATE_HOLDER = re.compile(r"Copyright[ \t]+\[yyyy\][ \t]+\[name of copyright owner\]", re.I)
# A real holder line: `Copyright <year>` followed by something that is not a bracket template.
_REAL_HOLDER = re.compile(r"Copyright(?:[ \t]+\(c\))?[ \t]+[12][0-9]{3}[ \t]*[-,]?[ \t]*[^\[\n]", re.I)


def conflicted(text):
    """True when the payload carries unresolved VCS conflict markers.

    Requires BOTH an opening and a closing marker, so a payload that merely quotes one is not
    reported: the finding is an unresolved merge, not the presence of angle brackets.
    """
    if not text:
        return False
    return bool(_CONFLICT_OPEN.search(text)) and bool(_CONFLICT_CLOSE.search(text))


def conflict_sides(text):
    """How many conflict hunks the payload carries. 0 when it is resolved."""
    if not conflicted(text):
        return 0
    return len(_CONFLICT_OPEN.findall(text))


def holder_ambiguous(text):
    """True when the payload offers a REAL holder line and the ASF TEMPLATE line together.

    This is the state that defeats `p241`'s template-bracket exclusion: the exclusion is
    correct on a pristine ASF appendix and wrong here, because the real holder is also present
    and the payload does not say which one governs.
    """
    if not text:
        return False
    return bool(_TEMPLATE_HOLDER.search(text)) and bool(_REAL_HOLDER.search(text))


# ── ROLE ───────────────────────────────────────────────────────────────────────────────────
# A licence name in a PARAMETER position. The parameter label is the evidence; the licence name
# it points at is the value, and the value is NOT this payload's grant.
#
# `[^\n]{0,120}` is bounded and greedy-free by construction (a negated class, not `.*?`), which
# keeps `p230-prose-path-ladder/lazy_lint.py` quiet and keeps the match on ONE line.
_PARAM_ROLES = (
    # BSL 1.1 / BUSL: the licence the work converts to on the Change Date.
    ("change-license", re.compile(r"^[ \t]*Change[ \t]+License[ \t]*:[ \t]*([^\n]{0,120})", re.MULTILINE | re.I)),
    # BSL 1.1: the date the conversion happens. Carried so the gate can state WHEN.
    ("change-date", re.compile(r"^[ \t]*Change[ \t]+Date[ \t]*:[ \t]*([^\n]{0,120})", re.MULTILINE | re.I)),
    # The "alternative/commercial licensing available" pointer, which names a licence you must BUY.
    ("alternative-licence", re.compile(r"alternative[ \t]+licensing[ \t]+arrangements([^\n]{0,120})", re.I)),
)

# Source-available families whose governing grant must win over any licence they merely NAME.
# Matched on the TITLE, so the verdict does not depend on anchor order anywhere else.
_GOVERNING = (
    ("BUSL", re.compile(r"Business[ \t]+Source[ \t]+License", re.I)),
    ("Elastic", re.compile(r"Elastic[ \t]+License", re.I)),
    ("PolyForm", re.compile(r"PolyForm[ \t]+(?:Noncommercial|Strict|Shield|Perimeter)", re.I)),
    ("SSPL", re.compile(r"Server[ \t]+Side[ \t]+Public[ \t]+License", re.I)),
    ("CAL", re.compile(r"Cryptographic[ \t]+Autonomy[ \t]+License", re.I)),
)


def parameter_roles(text):
    """Every (label, value) where this payload names a licence or date in a PARAMETER slot."""
    if not text:
        return []
    out = []
    for label, rx in _PARAM_ROLES:
        m = rx.search(text)
        if m:
            value = m.group(1).strip()
            out.append((label, value))
    return out


def governing_family(text):
    """The family that GOVERNS the payload, independent of which anchor happens to fire first.

    Returns the source-available family name, or `None` when the payload is not one of them —
    in which case `lib/license_family.sh` is the authority and this instrument defers to it.
    """
    if not text:
        return None
    for name, rx in _GOVERNING:
        if rx.search(text):
            return name
    return None


def names_but_does_not_grant(text):
    """The licence names this payload MENTIONS without granting them.

    The whole point of the role axis: these are the tokens that defeat an ordered matcher.
    """
    roles = parameter_roles(text)
    if governing_family(text) is None:
        return []
    out = []
    for label, value in roles:
        if label in ("change-license",) and value:
            out.append(value)
    return out


def verdict(text):
    """One line, in the order a consumer must apply it.

    CONFLICTED outranks the role axis: a payload that is two payloads has no single grant to
    name, so nothing downstream should be reading its family at all.
    """
    if not text or not text.strip():
        return "EMPTY"
    if conflicted(text):
        bits = ["CONFLICTED:hunks=%d" % conflict_sides(text)]
        if holder_ambiguous(text):
            bits.append("holder-ambiguous")
        return ";".join(bits)
    gov = governing_family(text)
    if gov is not None:
        named = names_but_does_not_grant(text)
        if named:
            return "SOURCE-AVAILABLE:%s;names-but-does-not-grant=%s" % (gov, ",".join(named))
        return "SOURCE-AVAILABLE:%s" % gov
    return "SINGLE-RESOLVED-GRANT"


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("usage: payload_integrity.py <payload-file> [...]\n")
        return 2
    for path in argv[1:]:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        if len(argv) > 2:
            sys.stdout.write("%s\t%s\n" % (path, verdict(text)))
        else:
            sys.stdout.write("%s\n" % verdict(text))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
