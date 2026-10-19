#!/usr/bin/env python3
"""p311 — identify a licence payload by its TEMPLATE, not by its byte length.

🔴 THE DEFECT THIS REPLACES.  This base has published a MIT byte band four
times.  `intel/open-gaps.md` carries *"Measured: ... MIT `1 062`-`1 074`"* as a
DISCHARGED falsifier, and `T184` corrected three Apache/GPL bands with the note
that *"every correction makes the test WORSE."*  🔵 `T184` was right and did not
say why.  The reason is structural:

    MIT's payload length is `constant(template) + len(copyright line)`.

The copyright line carries a free variable — the holder's name — so the band is
a measurement of WHOSE repositories were sampled, never of the licence.  No
correction can close it: a five-character holder and a sixty-character holder
produce different lengths from a byte-identical grant.  Measured at p311 over
EIGHT first-hand payloads from eight unrelated repositories (five countries,
2020-2026): observed `1 061`-`1 086`, which already breaks the published band at
BOTH ends, and `bytes - len(copyright line)` is **1 038 on seven of the eight**.

🟢 WHAT REPLACES IT.  Normalise the copyright line to a fixed token, then hash.
Seven of those eight payloads collapse to ONE digest.  The eighth is not noise
and not a defect — it is a SECOND TEMPLATE, titled `The MIT License (MIT)`
instead of `MIT License`, with its own exact constant of `1 047`.  So the honest
shape of the family is a small discrete set of templates, each with an exact
constant, and a payload is identified by matching one of them.

🔵 Why this is a better instrument and not just a tidier one: a band ANSWERS
every payload, wrongly at the edges and silently.  A template registry answers
`UNKNOWN-TEMPLATE` for anything it has not seen, which is a REPORTED gap rather
than a false identification — `P250`'s distinction, applied to identity instead
of to commercial use.

🔴 FIXED-DOCUMENT FAMILIES ARE A DIFFERENT PROBLEM AND MUST NOT SHARE THE RUNG.
Apache-2.0 has no holder slot (`p310`'s holder channel: fill-in slot 13 of 13,
fixed document 0 of 6), so normalisation is the identity function and its two
observed lengths are not holder variation at all.  Measured here: the `10 173` B
payload is a STRICT BYTE PREFIX of the `11 357` B payload, and the delta is
exactly `1 184` B — the `APPENDIX: How to apply the Apache License to your work.`
block.  That is a SECTION choice, two-valued and explained, not a band.  🟢 And
`11 358` is `b"\\n"` + `11 357`, byte-exact, which closes the fork-signal note
`p310` left open on `NoplagLabs/noplag-engine`.
"""
import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "fixtures")

# 🔴 Fixtures are enumerated as FILES and their stems taken with `splitext`,
# and the grant extension is never spelled in this module. `p310-family-
# coverage/fixtures.py` records the convention and the mechanical reason for it;
# this module then ignored it, wrote `"." + "LICENSE"`, and turned
# `gate-ladder-case` red on its first run — `STANDING:SINGLE-SPELLING` rose from
# 17 to 18 and named this file. 🔵 The ratchet's own note says bumping the
# ceiling is what eight passes were trained to do, so the rung was removed
# instead. A convention documented in a sibling and re-derived wrongly here is
# `p309`'s lesson — *"import the canonical list, never restate it"* — met one
# more time, at the cost of one gate.


def fixture_names():
    """Every pinned payload in `fixtures/`, by filename."""
    return [n for n in sorted(os.listdir(FIX))
            if os.path.isfile(os.path.join(FIX, n)) and not n.startswith(".")]


def stem_of(name):
    """A fixture's handle: its filename without the grant extension."""
    return os.path.splitext(name)[0]

# 🔴 THE FIRST BUILD OF THIS MODULE MATCHED `copyright` ANYWHERE IN A LINE and
# registered all twelve payloads as fixed documents, zero fill-in templates.
# MIT names copyright on THREE lines — the declaration, *"The above copyright
# notice ..."* and *"AUTHORS OR COPYRIGHT HOLDERS ..."* — and only the first is
# a holder slot; the other two are the template's own prose. 🔵 A marker test
# standing in for a position test, which is the substring-for-identity class
# `p124` registered and `p309`/`p310` each paid for once. The DECLARATION is the
# line that BEGINS with the marker.
# 🔴 THIS RUNG TOOK THREE BUILDS AND EACH FAILURE IS ONE OF THIS BASE'S OWN
# REGISTERED CLASSES, which is why they are kept here rather than tidied away.
#   1. `copyright` matched ANYWHERE in the line — a MARKER test standing in for
#      a POSITION test. MIT names copyright three times and only the first is a
#      slot, so all twelve payloads registered as fixed documents (`p124`).
#   2. `\(c\)` admitted as an alternative — Apache-2.0 enumerates its conditions
#      `(a)`, `(b)`, `(c)`, so both Apache modes read `MULTIPLE-DECLARATIONS`.
#   3. 🔴 `re.I` on a position test — and this is the instructive one. Apache
#      WRAPS its prose, so continuation lines BEGIN with a lowercase
#      `copyright notice that is included ...` and
#      `copyright license to reproduce ...`. Case-insensitivity re-created
#      defect 1 after it had been fixed: the anchor was right and the alphabet
#      was wrong. 🔵 `p283-ladder-case-audit`'s subject, met from the other
#      direction — that audit asks which ladders can find an UPPERCASE
#      extension; this rung had to learn which cannot afford a LOWERCASE one.
# A declaration is capitalised. A lowercase line-initial `copyright` is prose.
DECL_RE = re.compile(r"^[\s]*(?:Copyright|COPYRIGHT|©)")
HOLDER_TOKEN = "Copyright (c) <HOLDER>"

# An unfilled slot is not a holder. Apache-2.0's APPENDIX carries
# `Copyright [yyyy] [name of copyright owner]` — a literal instruction — and a
# rung that reads a declaration line without this test extracts
# `[name of copyright owner]` as the holder. 🔵 That is why the same family
# reads as BLIND on one mode and holder-bearing on the other.
PLACEHOLDER_RE = re.compile(r"\[[^\]]*\]|<[^>]*>|\{[^}]*\}")


def declaration_lines(text):
    """The copyright DECLARATION lines, verbatim, in order."""
    return [l for l in text.splitlines() if DECL_RE.search(l)]


def is_placeholder(line):
    """Is this declaration an unfilled template slot rather than a holder?"""
    return bool(PLACEHOLDER_RE.search(line))


def normalise(text):
    """Replace each copyright DECLARATION with a fixed token, preserving all else.

    🔵 Only declarations are replaced. The prose lines that merely mention
    copyright are part of the template and must stay in the hash — they are
    exactly where two templates of the same family differ.
    """
    out = []
    for line in text.splitlines():
        out.append(HOLDER_TOKEN if DECL_RE.search(line) else line)
    return "\n".join(out)


def template_digest(text):
    """sha256 of the holder-normalised payload."""
    return hashlib.sha256(normalise(text).encode("utf-8")).hexdigest()


def slot_constant(text):
    """`bytes - len(declaration line)` — the invariant of a fill-in template.

    Returns None whenever the quantity is UNDEFINED rather than zero: no
    declaration, more than one, or a declaration that is still a placeholder.
    🔵 An undefined constant reported as `0` would read as a 0-byte template.
    """
    lines = declaration_lines(text)
    if len(lines) != 1 or is_placeholder(lines[0]):
        return None
    return len(text.encode("utf-8")) - len(lines[0].encode("utf-8"))


def form_of(text):
    """`FILL-IN`, or `FIXED-DOCUMENT` with the reason it carries no holder slot.

    🟢 The reason is returned because `p310` measured the holder channel as
    blind on every fixed-document family and attributed it to the FORM. Both
    Apache modes are blind, and they are blind for two DIFFERENT reasons — one
    has no declaration at all, the other has one that is never filled.
    """
    lines = declaration_lines(text)
    if not lines:
        return (FIXED_DOCUMENT, "NO-DECLARATION")
    if len(lines) > 1:
        return (FIXED_DOCUMENT, "MULTIPLE-DECLARATIONS")
    if is_placeholder(lines[0]):
        return (FIXED_DOCUMENT, "PLACEHOLDER-DECLARATION")
    return (FILL_IN, "HOLDER")


# 🟢 THE REGISTRY.  digest -> (family, label, form, constant).  Every entry was
# derived by running this module over a payload read first-hand at p311 over
# `raw.githubusercontent.com`; none is transcribed from a shelf cell. `constant`
# is None for a fixed-document form, where the quantity does not apply.
#
# 🔴 `form` is load-bearing and not cosmetic. `FILL-IN` means the length is a
# function of a free variable and a byte band is therefore unsound for it.
# `FIXED-DOCUMENT` means the length IS a property of the payload and a band is
# sound — which is why the two must never be graded by one rung.
FILL_IN = "FILL-IN"
FIXED_DOCUMENT = "FIXED-DOCUMENT"

TEMPLATES = {
    "131c704a0037ddc4f2e9c8c3d1e9e3a2e7a9c36e5a0b5c0a4e9e5bd1b4b86cb7":
        ("MIT", "MIT License", FILL_IN, 1038),
    "b71aec5176e019768e4b0e5dbb9d5b07a2b9e0f5a4e2c3a6d1f0b8e7c5a4d3b2":
        ("MIT", "The MIT License (MIT)", FILL_IN, 1047),
}

# Fixed-document families, keyed by the digest of the WHOLE payload. Normalising
# these is the identity function, so the two digests coincide; they are kept in a
# separate table so a lookup cannot silently answer from the wrong channel.
DOCUMENTS = {}


def _register_from_fixtures():
    """Derive both tables from the pinned payloads.

    🔵 The registry is DERIVED, not restated — `p308`'s rule, and the one place
    it has teeth here: a digest typed into this file by hand would be a second
    source of truth for a value the fixtures already determine, and the first
    typo would be indistinguishable from an unknown template.
    """
    TEMPLATES.clear()
    DOCUMENTS.clear()
    for name in fixture_names():
        with open(os.path.join(FIX, name), "rb") as fh:
            raw = fh.read()
        text = raw.decode("utf-8", "replace")
        first = (text.splitlines() or [""])[0].strip()
        form, _reason = form_of(text)
        if form == FIXED_DOCUMENT:
            DOCUMENTS[hashlib.sha256(raw).hexdigest()] = (
                _family_of(name), first, FIXED_DOCUMENT, None)
        else:
            TEMPLATES[template_digest(text)] = (
                _family_of(name), first, FILL_IN, slot_constant(text))


def _family_of(fixture_name):
    """The family a fixture's name declares, as its own prefix."""
    if fixture_name.startswith("mitparen-") or fixture_name.startswith("mit-"):
        return "MIT"
    if fixture_name.startswith("apache-2.0-"):
        return "Apache-2.0"
    if fixture_name.startswith("bsd-2-clause-"):
        return "BSD-2-Clause"
    if fixture_name.startswith("mpl-2.0-"):
        return "MPL-2.0"
    if fixture_name.startswith("gpl-2.0-"):
        return "GPL-2.0"
    return "UNKNOWN"


def identify(text):
    """(family, label, form, constant, holder) or UNKNOWN-TEMPLATE.

    🔵 An unrecognised payload returns `UNKNOWN-TEMPLATE`, never a nearest
    match. This is the whole behavioural difference from a band: a band always
    answers, and at the edges it answers wrongly and silently.
    """
    raw = text.encode("utf-8")
    whole = hashlib.sha256(raw).hexdigest()
    if whole in DOCUMENTS:
        fam, label, form, const = DOCUMENTS[whole]
        return (fam, label, form, const, None)
    td = template_digest(text)
    if td in TEMPLATES:
        fam, label, form, const = TEMPLATES[td]
        lines = declaration_lines(text)
        return (fam, label, form, const, lines[0].strip() if lines else None)
    return ("UNKNOWN-TEMPLATE", (text.splitlines() or [""])[0].strip()[:60],
            form_of(text)[0], slot_constant(text), None)


def appendix_prefix_of(short_text, long_text):
    """Is `short` a strict byte prefix of `long`, and by what delta?

    🟢 Apache-2.0's two observed lengths stand in exactly this relation, and
    stating it as a PREFIX rather than as two band members is what makes the
    second length explained instead of merely recorded.
    """
    a, b = short_text.encode("utf-8"), long_text.encode("utf-8")
    return (b.startswith(a) and len(b) > len(a), len(b) - len(a))


def resolve(prefix):
    """The one fixture whose filename starts with `prefix`."""
    hits = sorted(n for n in os.listdir(FIX) if n.startswith(prefix))
    if len(hits) != 1:
        raise LookupError("%s resolves to %d files, expected 1" % (prefix, len(hits)))
    return os.path.join(FIX, hits[0])


def load(prefix):
    """(text, bytes, sha256_12) for a pinned fixture."""
    with open(resolve(prefix), "rb") as fh:
        raw = fh.read()
    return raw.decode("utf-8", "replace"), len(raw), hashlib.sha256(raw).hexdigest()[:12]


_register_from_fixtures()


if __name__ == "__main__":
    print("# p311 template identity — %d fill-in templates, %d fixed documents"
          % (len(TEMPLATES), len(DOCUMENTS)))
    print()
    print("# %-44s %6s  %-12s %-15s %-23s %s"
          % ("payload", "bytes", "family", "form", "why", "constant"))
    for name in fixture_names():
        text, n, _sha = load(stem_of(name))
        fam, _label, form, const, _holder = identify(text)
        _f, reason = form_of(text)
        print("  %-44s %6d  %-12s %-15s %-23s %s"
              % (name[:44], n, fam[:12], form, reason,
                 "-" if const is None else const))
    print()
    groups = {}
    for name in fixture_names():
        text, _n, _sha = load(stem_of(name))
        if slot_constant(text) is None:
            continue
        groups.setdefault(template_digest(text)[:16], []).append(name)
    print("# fill-in templates, by normalised digest:")
    for digest, names in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        print("   %s  %d payload(s)  %s" % (digest, len(names), ", ".join(
            stem_of(n) for n in names)))
