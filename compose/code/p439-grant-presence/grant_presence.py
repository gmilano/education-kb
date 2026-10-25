#!/usr/bin/env python3
"""p439 — `Gap 439-A`: the escalation column sees a MODIFIED grant and not an ABSENT one.

`Gap 438-A` measured one half of this: `bespoke_census.needs_a_human()` detects an
addition (`p1054` writes `MIT-BODY-PLUS:unclassified-addition`) and routes the row
`no` anyway, because the predicate never reads the column its own grader wrote.

🔴 THIS GAP IS THE OTHER HALF: a payload can be SHORTER than the grant it names, and
the CODE-LICENCE path does not ask.  Measured 2026-10-25 on
`spragginsdesigns/ai-tutor-webapp` (`LICENSE` **552 B** · `sha256₁₂ 5809eb2eab28`,
HEAD read 2026-10-25): `titled_family = Apache-2.0`, `scan_verdict = PERMISSIVE`,
🔴 `stock = True`, 🔴 `needs_a_human = False` — and the payload is the Apache-2.0
**APPENDIX notice**, whose own words are *"You may obtain a copy of the License at
<url>"*.  The licence text is NOT IN THE REPOSITORY.  Two consequences a client pays
for, neither visible in that row:

  1. 🔴 The holder named in the grant is **Vercel, Inc.** — the Next.js template's
     notice, carried unchanged.  Nothing in the repository grants anything over the
     code the repository's own author wrote.
  2. 🔴 Apache-2.0 §4(a) obliges a redistributor to GIVE recipients a copy of the
     License.  A repository shipping only the pointer has not done it, so the
     obligation lands on whoever vendors it next — the client.

🔴 AND THE PRINCIPLE WAS ALREADY SETTLED ON THIS BASE -- IT JUST NEVER TRAVELLED.
`P1065` (pass 254) states that A POINTER TO A LICENCE IS NOT A GRANT, and
`pass258-content-licence-family/content_licence.py::is_grant()` IMPLEMENTS it, by exactly
the method used here: look for the words that perform the grant (`licensed rights`,
`copyright and related rights`) rather than the name of the licence.  🔴 It is scoped to
CREATIVE COMMONS content licences and was never carried into the code-licence path, so
`is_stock()` and `needs_a_human()` -- the predicates that grade MIT, Apache-2.0 and BSD --
have never asked the question for a single code payload.  🔵 THAT IS THIS BASE'S SIGNATURE
FAILURE MODE, not a new class: `lib/README.md` records pass 77 re-importing `P171` because
a correction lived in five instruments and a sixth inherited nothing, and `Gap 394-B`
records a standing gate whose rule was never enforced where the verdicts are written.
This file is `P1065` carried one directory across, to the family of licences a client
actually redistributes.

🟢 AND THE CLASS WAS ALREADY FIXTURED HERE TOO.  `grade()` over this base's own committed
fixtures, same hour: `md-incorporation-by-reference.md` (226 B), `licence-apache2-
appendix.txt` (311 B), `grant-apache20.txt` (742 B), `apache.txt` (157 B),
`xblock.LICENSE.TXT.head` (159 B), `apache-2.0.txt` (3 000 B),
`webuntis-ha.LICENSE.mit-truncated` (797 B), `aprende-brasil.LICENSE.mit-truncated`
(814 B), `pupilfirst.LICENSE.head` (601 B), `md-dangling-file-reference.md` (90 B) —
🔴 **10 of 10 grade `stock = True, needs_a_human = False`.**  The fixtures exist to
test other instruments; the escalation column never learned from any of them.

WHY THIS CLASSIFIES BY CLAUSE AND NOT BY BYTE COUNT
---------------------------------------------------
A byte floor is the obvious instrument and this file deliberately does not make it the
decider.  `P171` is this base's standing lesson that a licence question answered by
substring presence imports a defect (GPL-3.0 §13 is titled with AGPL's name, so every
GPL-3.0 payload read as AGPL-3.0), and the generalisation `lib/README.md` draws is that
the question must be asked of STRUCTURE.  Measured on this base's own corpus the floor
is also not safe: `BSD` stock payloads run **221 B → 1 514 B** (n=8) because BSD-0,
BSD-2 and BSD-3 are three different lengths under one family name, so any single BSD
floor either misses BSD-3 truncation or condemns every valid BSD-0.

So the primary signal is OPERATIVE-CLAUSE PRESENCE: does the payload contain the words
that DO the granting for the family it names?  The byte count is carried in the row as
a corroborator, reported and never decisive.

VERDICTS
  GRANT-PRESENT        the family's operative clauses are all present
  GRANT-BY-REFERENCE   an incorporation marker is present and the operative clauses
                       are not: the grant names a document it does not contain
  GRANT-TRUNCATED      no incorporation marker, but operative clauses are missing:
                       the payload is an excerpt of its own grant
  GRANT-UNCALIBRATED   the titled family has no clause profile here.  🔵 NOT a defect
                       and NOT a pass: it is this instrument declining to judge, which
                       `P250` requires over guessing.

Findings (exit 1 if any, exit 2 on refusal):
  P439-BY-REFERENCE    GRANT-BY-REFERENCE
  P439-TRUNCATED       GRANT-TRUNCATED
  P439-NO-INPUT        called with no payload (`P541`: measuring nothing is not a
                       clean tree)

Usage: grant_presence.py PAYLOAD [PAYLOAD ...]     TSV on stdout.
"""
import pathlib
import re
import sys

# The operative clauses, per family.  Each entry is (label, regex).  ALL must match for
# GRANT-PRESENT.  These are the words that perform the grant or carry the obligation --
# not the title, which `titled_family` already answered, and not boilerplate that an
# excerpt would keep.
CLAUSE_PROFILE = {
    "MIT": [
        ("permission-grant", r"permission\s+is\s+hereby\s+granted"),
        ("without-restriction", r"without\s+restriction"),
        ("notice-obligation", r"above\s+copyright\s+notice"),
        ("warranty-disclaimer", r'provided\s+"as\s+is"'),
        # 🔴 THE FIFTH CLAUSE IS THIS BASE'S OWN FIXTURES CORRECTING THIS FILE.  The
        # first profile written here had four clauses and graded BOTH
        # `webuntis-ha.LICENSE.mit-truncated` (797 B) and
        # `aprende-brasil.LICENSE.mit-truncated` (814 B) as GRANT-PRESENT -- fixtures
        # whose own NAMES say otherwise.  Reading them showed why, and it is the
        # truncation that matters most to a consultancy: both keep the warranty
        # disclaimer and drop MIT's FINAL paragraph, the liability cap.  "AS IS" and
        # "IN NO EVENT SHALL ... BE LIABLE" are two different protections, and a
        # payload can keep the first while withholding the second.
        ("liability-cap", r"in\s+no\s+event\s+shall"),
    ],
    "Apache-2.0": [
        # The numbered operative sections.  The APPENDIX notice carries NONE of them.
        ("copyright-grant", r"grant\s+of\s+copyright\s+license"),
        ("patent-grant", r"grant\s+of\s+patent\s+license"),
        ("redistribution", r"\bredistribution\b"),
        ("definitions", r"\bdefinitions\b"),
    ],
    "ISC": [
        ("permission-grant", r"permission\s+to\s+use,\s+copy,\s+modify"),
        ("warranty-disclaimer", r'provided\s+"as\s+is"'),
    ],
}

# Markers that say "the grant lives somewhere else".  Presence of any one of these, with
# the operative clauses absent, is the BY-REFERENCE shape rather than a bare excerpt.
REFERENCE_MARKERS = [
    ("apache-appendix", r"you\s+may\s+obtain\s+a\s+copy\s+of\s+the\s+license\s+at"),
    ("compliance-notice", r"you\s+may\s+not\s+use\s+this\s+file\s+except\s+in\s+compliance"),
    ("licence-url", r"https?://\S*licen[sc]e"),
    # 🔴 THE FIRST DRAFT WROTE THE TWO MARKERS BELOW WITH UPPERCASE `LICEN[SC]E` /
    # `COPYING` LITERALS AND MATCHED THEM AGAINST TEXT `_norm()` HAD ALREADY LOWERCASED,
    # so two of five markers COULD NEVER FIRE -- dead code that still read as coverage.
    # That is this base's `P237` shape: a rule you have to remember is not a control.
    # `C15` now asserts every marker fires on its own specimen.
    #
    # 🟢 And the fold is applied HERE, at the match site, with `re.I` -- not left to the
    # caller.  Two reasons: these patterns name FILENAME STEMS (`licence`, `copying`),
    # which real repositories spell in at least four casings, and a marker that only
    # works because some earlier line happened to lowercase its input is the same latent
    # defect in a different place.  `p283`'s ladder audit grades a single-spelling
    # filename stem with no visible fold, and it is right to.
    ("see-file", r"see\s+(?:the\s+)?(?:`|\[|\*)?(?:licen[sc]e|copying)"),
    ("md-link", r"\[[^\]]{1,60}\]\(\s*\.{0,2}/?[^)\s]*licen[sc]e[^)\s]*\s*\)"),
]

# Compiled once, with `re.I` (`p283`: the fold is visible on the path to the spelling).
_MARKERS = [(lbl, re.compile(rx, re.I)) for lbl, rx in REFERENCE_MARKERS]


# 🔴 THE QUOTE FOLD IS A FALSE POSITIVE THIS BASE'S CORPUS CAUGHT BEFORE THIS GATE WAS
# WIRED.  The first profile here matched MIT's warranty disclaimer as `provided "as is"`
# with ASCII quotes, and graded `mit-openhands-1096.LICENSE` (1 096 B, a COMPLETE MIT
# licence belonging to a load-bearing dependency) as GRANT-TRUNCATED on the strength of
# one missing clause -- because that payload writes “AS IS” with U+201C/U+201D
# typographic quotes.  A real grant would have been condemned by a punctuation
# character.  Every quote form is folded to ASCII before any clause is asked for.
_QUOTES = {
    0x201C: '"', 0x201D: '"', 0x201E: '"', 0x201F: '"', 0x00AB: '"', 0x00BB: '"',
    0x2018: "'", 0x2019: "'", 0x201A: "'", 0x201B: "'", 0x2039: "'", 0x203A: "'",
    0x2033: '"', 0x2032: "'",
}


def _norm(text):
    """Lowercased, quote-folded, with whitespace runs folded, so a clause broken across
    lines or typeset with curly quotes still matches.  `P834`'s lesson is about BYTES and
    is why the byte count is taken from the untouched payload, never from this."""
    return re.sub(r"\s+", " ", text.translate(_QUOTES).lower())


def clause_report(text, family):
    """Which of the family's operative clauses are present.  Returns (present, missing)
    or (None, None) when the family has no profile here."""
    profile = CLAUSE_PROFILE.get(family)
    if profile is None:
        return None, None
    flat = _norm(text)
    present = [lbl for lbl, rx in profile if re.search(rx, flat)]
    missing = [lbl for lbl, rx in profile if not re.search(rx, flat)]
    return present, missing


def references_found(text):
    """Which "the grant lives elsewhere" markers appear.  Case-folded at the match site
    via `re.I`, so this answers the same on a raw payload and a normalised one."""
    flat = _norm(text)
    return [lbl for lbl, rx in _MARKERS if rx.search(flat)]


def classify(text, family):
    """One payload, one verdict.  `family` is the TITLED family -- this instrument does
    not re-answer the family question (`P171`: it has a hardened owner)."""
    present, missing = clause_report(text, family)
    refs = references_found(text)
    if present is None:
        return {
            "verdict": "GRANT-UNCALIBRATED", "family": family,
            "missing": [], "present": [], "refs": refs,
            "bytes": len(text.encode("utf-8", "replace")),
        }
    if not missing:
        verdict = "GRANT-PRESENT"
    elif refs:
        verdict = "GRANT-BY-REFERENCE"
    else:
        verdict = "GRANT-TRUNCATED"
    return {
        "verdict": verdict, "family": family,
        "missing": missing, "present": present, "refs": refs,
        "bytes": len(text.encode("utf-8", "replace")),
    }


FINDING = {
    "GRANT-BY-REFERENCE": "P439-BY-REFERENCE",
    "GRANT-TRUNCATED": "P439-TRUNCATED",
}


def main(argv):
    if not argv:
        sys.stderr.write(
            "🔴 p439-grant-presence: P439-NO-INPUT — called with no payload. "
            "P541: measuring nothing is not a clean tree.\n")
        return 2
    # Imported, not re-implemented: the family question belongs to `license_family.sh`'s
    # Python peer in the census, per `lib/README.md`.
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]
                           / "p341-bespoke-instrument-census"))
    import bespoke_census as bc

    print("payload\tfamily\tbytes\tverdict\tmissing\trefs\tfinding")
    findings = 0
    for p in argv:
        path = pathlib.Path(p)
        if not path.is_file():
            sys.stderr.write("🔴 p439-grant-presence: not a file: %s\n" % p)
            return 2
        raw = path.read_text(errors="replace")
        fam = bc.titled_family(raw)
        r = classify(raw, fam)
        f = FINDING.get(r["verdict"], "")
        if f:
            findings += 1
        print("%s\t%s\t%d\t%s\t%s\t%s\t%s" % (
            path.name, r["family"], r["bytes"], r["verdict"],
            ",".join(r["missing"]) or "-", ",".join(r["refs"]) or "-", f or "-"))
    print("#\tfindings\t%d" % findings)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
