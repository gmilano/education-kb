"""`pass262-scoped-reservation-audit` — `ACTION ZI`, and the three things it found.

`ACTION ZI` (`p261`) asked: *"re-run `p260`'s `reservation_verdict()` over every payload
this base has ever graded as `RESERVED` or proprietary, with the SCOPED guard"*, falsified
*"if no published retraction turns out to be third-party — in which case `nextSIS` is one
repository's aggregate and not a class."*

🟢 **It is a class.**  `36` slugs probed, `64` payloads read first-hand, and the second
member was found immediately — but it is **not** an aggregate, and `p261`'s scoped guard
**cannot see it**:

🔴 **`sdv-dev/SDV`.**  The `All Rights Reserved` on line `34` of its `4 818` B `LICENSE` is
**MariaDB Corporation Ab's** — *"License text copyright (c) 2017 MariaDB Corporation Ab,
All Rights Reserved."* — the **steward of the Business Source License form**, reserving
rights in the LICENCE DOCUMENT, not DataCebo reserving rights in SDV.  `aggregate_sections()`
returns `[]` because a BUSL steward notice is not a rule-delimited grant heading, so
`subject_span()` returns the whole file and `reservation_verdict_scoped()` answers `RESERVED`.

🔵 **The conclusion happens to be right** — BUSL-1.1 is not OSI — **and that is the failure
`p260` named and `p261` repeated: an accidentally-correct answer from an unsound method.**
The same notice sits in every BUSL payload ever written, including permissively-licensed
projects that merely *vendor* a BUSL dependency's text.

🔴 **`dssg/student-early-warning`** is the opposite error: a REAL GRANT graded `RESERVED`.
Its `2 069` B `LICENSE` reserves rights on line `3` and then grants, on line `5`,
*"Permission to use, copy, modify, and distribute this software … is hereby granted"* — the
**X11/academic variant**, which omits MIT's *"free of charge"*.  `p261`'s permissive test is
two literal phrases, so a grant with a field-of-use restriction reads as a bare reservation.

🔴 **And the harvester this module replaces would have BROKEN A CORRECTION.**
`intel/trends.md` l.`575` carries `BUSL-1.1, "source-available, not OSI"` for
[`twentyhq/twenty`](https://github.com/twentyhq/twenty) — in a column headed *"what the
secondary source said"*, beside the payload reading that **refutes** it.  `p249` already
corrected that row to `AGPL-3.0`; a sweep that takes any grant-cell token as a verdict
re-asserts the refuted claim and undoes the correction.  🔵 `ZD` taught that a row's state is
what the NEWEST section says.  **`p262`: a row's state is also not what the row QUOTES.**

Everything here is offline.  The online sweep is `sweep.py`.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE_ROOT = os.path.dirname(HERE)

# 🔵 `p229`: *a probe list copied is a probe list forked.*  The CC axes were built at `p258`
# and are not re-implemented here — `leading_family()` asks that module whether a token it
# found is restrictive, because `CC-BY` and `CC-BY-NC-SA` share a prefix and only one of them
# is usable.  A bare `startswith("CC-BY")` reads the second as the first; this pass's own
# first-cut harvester did exactly that and mis-filed `anaistack/cefr-asag-corpus`.
sys.path.insert(0, os.path.join(CODE_ROOT, "pass258-content-licence-family"))
try:
    import content_licence as _cc
except Exception:                                            # pragma: no cover
    _cc = None

CLASSIFIER_UNAVAILABLE = "CLASSIFIER-UNAVAILABLE"


# ─────────────────────────────────────────────────────────────────────────────
# 1.  BYTES ARE NOT CHARACTERS
#
# 🔴 Two shelf figures disagreed with this pass's first sweep —
# `anaistack/cefr-asag-corpus` (`20 863` B on the shelf, `20 859` from the sweep) and
# `alfredang/AI-LMS-TMS` (`57 174` B / `55 028`).  **Both shelf figures are correct.**  The
# sweep reported `len(payload.decode())` — CHARACTERS — and the deltas are exactly the
# multi-byte characters: `4` and `2 146`.
#
# 🔵 `p261`'s lesson was *disbelieve the instrument before disbelieving the shelves*, and it
# applies to the instrument a pass wrote this hour as much as to one it inherited.  No
# correction was published off those two deltas.  Every size this module reports is bytes.
# ─────────────────────────────────────────────────────────────────────────────

def payload_size(raw):
    """Size in BYTES, whatever it is handed.

    Accepts `bytes` (authoritative) or `str` (re-encoded as UTF-8 first).  A caller that
    passes already-decoded text still gets the byte count the shelves record."""
    if isinstance(raw, bytes):
        return len(raw)
    return len((raw or "").encode("utf-8"))


def size_disagreement(raw):
    """`(bytes, chars, delta)` — the quantity that made this pass doubt two correct cells."""
    b = raw if isinstance(raw, bytes) else (raw or "").encode("utf-8")
    return len(b), len(b.decode("utf-8", "replace")), len(b) - len(b.decode("utf-8", "replace"))


# ─────────────────────────────────────────────────────────────────────────────
# 2.  THE STEWARD RESERVATION — the class `p261`'s guard cannot see
#
# A FORM licence (BUSL, and any other licence published as a reusable document) carries its
# steward's copyright in the document itself.  That reservation belongs to the steward, is
# present in every copy of the form, and says nothing whatever about the subject repository.
# It is third-party in exactly `nextSIS`'s sense and structurally invisible to a guard keyed
# on rule-delimited sections, because a steward notice is a SENTENCE, not a SECTION.
# ─────────────────────────────────────────────────────────────────────────────

STEWARD_NOTICE = re.compile(
    r"licen[cs]e text copyright[^.\n]*?all rights reserved", re.I)

# The stewards this base has met first-hand.  Named rather than inferred: a pass that meets a
# tenth form licence adds it here with the payload it read, and the control below fails until
# the fixture exists.
KNOWN_STEWARDS = (
    ("MariaDB Corporation Ab", "Business Source License"),
)


def steward_reservation_spans(body):
    """Line numbers (1-based) of reservations belonging to a LICENCE FORM's steward."""
    out = []
    for i, line in enumerate((body or "").splitlines(), 1):
        if STEWARD_NOTICE.search(line):
            out.append(i)
    return out


def names_known_steward(body):
    """Is the steward one this base has read first-hand?  Unknown stewards are reported."""
    t = body or ""
    return [s for s, _form in KNOWN_STEWARDS if s.lower() in t.lower()]


# ─────────────────────────────────────────────────────────────────────────────
# 3.  THE PERMISSIVE TEST, WIDENED — and why two literal phrases were never enough
#
# `p261`'s `reservation_verdict_scoped()` decides BOILERPLATE-vs-RESERVED by looking for BSD's
# *"Redistribution and use in source and binary forms"* or MIT's *"Permission is hereby
# granted, free of charge"*.  Neither matches the X11/academic form, which grants in the same
# breath and omits *"free of charge"* because the grant is NOT free of charge for everyone —
# the restriction is the field of use, not the price.
#
# 🔴 `dssg/student-early-warning` is that form, and the base published it as a bare refusal.
# ─────────────────────────────────────────────────────────────────────────────

PERMISSIVE_PHRASES = (
    # BSD, both clauses counts
    re.compile(r"redistribution and use in source and binary forms", re.I),
    # MIT / Expat
    re.compile(r"permission is hereby granted,\s*free of charge", re.I),
    # 🆕 X11 / academic: a grant whose consideration is a field of use, not a fee.
    re.compile(r"permission to use,\s*copy,\s*modify,?\s*(and\s+)?(distribute|merge)"
               r"[^.]{0,400}?is hereby granted", re.I | re.S),
    # 🆕 ISC
    re.compile(r"permission to use,\s*copy,\s*modify,?\s*and/or distribute this software"
               r"\s+for any purpose", re.I),
)

# A grant can be real and still be unusable in a client deliverable.  These are the field-of-
# use limits that make a grant CONDITIONAL rather than permissive — reported separately,
# because "there is a grant" and "a studio may ship it" are different questions and this base
# has conflated them before (`p257`: Apache-2.0 vs a non-commercial academic licence).
FIELD_OF_USE = (
    re.compile(r"not[- ]for[- ]profit", re.I),
    re.compile(r"non[- ]?commercial", re.I),
    re.compile(r"academic research", re.I),
    re.compile(r"educational[^.]{0,40}purposes only", re.I),
)


def permissive_grant(span_text):
    """Does this span GRANT?  Returns the matching phrase's index, or `None`."""
    for i, rx in enumerate(PERMISSIVE_PHRASES):
        if rx.search(span_text or ""):
            return i
    return None


def field_of_use_limits(span_text):
    """The named field-of-use restrictions in a span that nonetheless grants."""
    return [rx.pattern for rx in FIELD_OF_USE if rx.search(span_text or "")]


# ─────────────────────────────────────────────────────────────────────────────
# 4.  THE VERDICT
# ─────────────────────────────────────────────────────────────────────────────

V_NONE = "NO-RESERVATION"
V_BOILERPLATE = "BOILERPLATE"
V_RESERVED = "RESERVED"
V_THIRD_PARTY = "THIRD-PARTY-RESERVATION"
V_STEWARD = "STEWARD-RESERVATION"
V_CONDITIONAL = "CONDITIONAL-GRANT"

ALL_VERDICTS = frozenset({V_NONE, V_BOILERPLATE, V_RESERVED, V_THIRD_PARTY,
                          V_STEWARD, V_CONDITIONAL})

RESERVATION = re.compile(r"all rights reserved", re.I)


def reservation_verdict_v2(body, scoped=None):
    """`p261`'s guard plus the two verdicts this pass had to add.

    `scoped` is `pass261.reservation_verdict_scoped` — injected rather than imported so this
    module cannot drift from the guard it extends, and so a caller can run the OLD guard and
    the new one over the same payload and publish the delta, which is what `ACTION ZI`
    actually asked for."""
    lines = (body or "").splitlines()
    hits = [i for i, l in enumerate(lines) if RESERVATION.search(l)]
    if not hits:
        return V_NONE

    # The steward's notice is removed from the population BEFORE the span test, because it is
    # third-party by authorship and no span containing it can be reasoned about.
    steward = set(i - 1 for i in steward_reservation_spans(body))
    remaining = [i for i in hits if i not in steward]
    if steward and not remaining:
        return V_STEWARD

    prior = scoped(body) if scoped else None
    if prior == V_THIRD_PARTY:
        return V_THIRD_PARTY

    # Span: the subject's, when the caller gave us p261's scoped guard to agree with.
    span = "\n".join(lines)
    if permissive_grant(span) is not None:
        return V_CONDITIONAL if field_of_use_limits(span) else V_BOILERPLATE
    return V_RESERVED


def verdict_delta(body, scoped):
    """`(p261_verdict, p262_verdict, changed)` — the ACTION ZI column, per payload."""
    old = scoped(body)
    new = reservation_verdict_v2(body, scoped=scoped)
    return old, new, old != new


# ─────────────────────────────────────────────────────────────────────────────
# 5.  THE HARVESTER — a cell's ROLE, because a row's state is not what the row QUOTES
# ─────────────────────────────────────────────────────────────────────────────

SLUG_RX = re.compile(r"github\.com/([A-Za-z0-9][\w.-]*)/([A-Za-z0-9][\w.-]*)")
TABLE_RULE = re.compile(r"^\s*\|[\s:|-]+\|\s*$")

# A column header that announces its cells are a CLAIM UNDER TEST rather than this base's
# finding.  Every one of these is a header this base actually writes.
CLAIM_COLUMN = re.compile(
    r"what the (secondary source|roundup|README|`README`)"
    r"|README[^|]{0,24}(actually\s+)?says"
    r"|`?README`?\s*,\s*read (today|this pass)"
    r"|(before|prior to)\s+(today|this pass)"
    r"|this shelf'?s cell before"
    r"|what the [^|]{0,30}\bsaid\b"
    r"|roundup'?s word"
    r"|\bclaimed\b"
    r"|what it (used to|previously) (say|read)", re.I)

ROLE_VERDICT = "VERDICT"
ROLE_QUOTED = "QUOTED-CLAIM"

RESTRICTIVE_TOKEN = re.compile(
    r"NOT OPEN SOURCE|NOT OSI|proprietary|source.available|Elastic-[12]\.0|BUSL"
    r"|Commons Clause|PolyForm|Confluent|Functional Source|UNLICENSED|unlicensed"
    r"|non[- ]commercial|all rights reserved|SSPL|Community License", re.I)

# The token a grant cell LEADS with, if any.  A cell that opens with a family and then warns
# about proprietary code downstream is a verdict of that family, not a restrictive grade —
# `nvaccess/nvda`'s *"GPL-2.0 … do not link into proprietary code"* is the shape.
LEADING_TOKEN = re.compile(
    r"^[\W\s]*?\**`?([A-Za-z][\w.+-]*(?:-[\w.+-]+)*)`?\**", re.U)


def table_cells(line):
    s = (line or "").strip()
    if not (s.startswith("|") and s.count("|") >= 3):
        return None
    return [c.strip() for c in s.strip("|").split("|")]


def cell_role(header_cell):
    """`VERDICT` or `QUOTED-CLAIM`, from the column header alone."""
    return ROLE_QUOTED if CLAIM_COLUMN.search(header_cell or "") else ROLE_VERDICT


# 🔴 THE THIRD PREFIX COLLISION THIS PASS, and the worst of them: `Unlicense` is a
# public-domain DEDICATION and `unlicensed` means THERE IS NO GRANT.  They share seven
# characters and they are opposites.  A `startswith` reader files every *"🔴 unlicensed —
# pattern only, do not vendor the code"* cell as a usable family and drops it from the
# population — which is how `barneslardo/sis-demo` and four others went missing from this
# sweep's first run.
#
# 🔵 `p251-prefix-collision` exists for this shape in repository identifiers (the `maia`
# class) and `p261` met it in heading namespaces.  It is here too, in LICENCE NAMES, and the
# remedy is the same: match the WHOLE token, not its opening.
FAMILY_NAMES = (
    "MIT", "Apache", "BSD", "GPL", "AGPL", "LGPL", "MPL", "CC0", "CC",
    "EPL", "Unlicense", "Zlib", "ISC", "Artistic", "OFL", "EUPL",
)
# A family, then OPTIONALLY a separator and a version/axis suffix — never bare adjacency.
# `CC` + `-BY-NC-SA-4.0` is a family with a suffix; `Unlicense` + `d` is not.
FAMILY_TOKEN = re.compile(
    r"^(?:" + "|".join(FAMILY_NAMES) + r")(?:[-._ +]\S*)?$", re.I)


def leading_family(grant_cell):
    """The licence token the cell LEADS with, or `None`.

    The token must be a family NAME, optionally followed by a separator and a version or
    axis suffix.  `unlicensed` is not `Unlicense`; see `FAMILY_TOKEN`."""
    m = LEADING_TOKEN.match(grant_cell or "")
    if not m:
        return None
    tok = m.group(1)
    return tok if FAMILY_TOKEN.match(tok) else None


def leads_with_usable(grant_cell):
    """Does the cell lead with a family a studio may ship?

    Delegates the CC axes to `p258`, so `CC-BY-NC-SA-4.0` is NOT read as `CC-BY`."""
    tok = leading_family(grant_cell)
    if tok is None:
        return False
    if _cc is None:
        return CLASSIFIER_UNAVAILABLE
    verdict = _cc.classify_token(tok)
    return verdict not in _cc.UNUSABLE_VERDICTS


GRADE_RESTRICTIVE = "RESTRICTIVE-GRADE"
GRADE_SCOPE_NOTE = "SCOPE-NOTE"


def restrictive_signal(grant_cell):
    """Is there anything restrictive in this cell at all?

    🔴 Two channels, because the prose vocabulary alone misses a whole family: a cell
    reading `**CC-BY-NC-SA-4.0**` carries no word from `RESTRICTIVE_TOKEN` and is as
    unusable as one that spells out *non-commercial*.  The second channel asks `p258`
    about the family the cell LEADS with, so the axes stay in one place."""
    if RESTRICTIVE_TOKEN.search(grant_cell or ""):
        return True
    usable = leads_with_usable(grant_cell)
    if usable is CLASSIFIER_UNAVAILABLE:
        return CLASSIFIER_UNAVAILABLE
    return leading_family(grant_cell) is not None and usable is False


def grade_class(header_cell, grant_cell):
    """What a restrictive token in a grant cell actually MEANS.

    Three answers, and this pass's first-cut harvester gave all `40` rows the first one:

    - `QUOTED-CLAIM`      — the column holds a claim under test (`twentyhq/twenty`)
    - `SCOPE-NOTE`        — the cell leads with a usable family; the token is advice, a second
                            component, or a downstream warning (`nvaccess/nvda`)
    - `RESTRICTIVE-GRADE` — the token IS this row's grade
    """
    signal = restrictive_signal(grant_cell)
    if signal is CLASSIFIER_UNAVAILABLE:
        return CLASSIFIER_UNAVAILABLE
    if not signal:
        return None
    if cell_role(header_cell) == ROLE_QUOTED:
        return ROLE_QUOTED
    usable = leads_with_usable(grant_cell)
    if usable is CLASSIFIER_UNAVAILABLE:
        return CLASSIFIER_UNAVAILABLE
    return GRADE_SCOPE_NOTE if usable else GRADE_RESTRICTIVE


def harvest(path):
    """`[(slug, shelf, line, grade_class, grant_cell)]` for one shelf."""
    out = []
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    header = None
    for n, line in enumerate(lines, 1):
        if TABLE_RULE.match(line):
            header = table_cells(lines[n - 2]) if n >= 2 else None
            continue
        cells = table_cells(line)
        if cells is None:
            if not line.strip().startswith("|"):
                header = None
            continue
        for i, c in enumerate(cells):
            m = SLUG_RX.search(c)
            if not m:
                continue
            grant = cells[i + 1] if i + 1 < len(cells) else ""
            hdr = header[i + 1] if header and i + 1 < len(header) else ""
            k = grade_class(hdr, grant)
            if k:
                out.append((f"{m.group(1)}/{m.group(2)}".lower(),
                            os.path.basename(path), n, k, grant[:200]))
            break
    return out
