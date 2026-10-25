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

Usage: grant_presence.py [--family FAM] PAYLOAD [PAYLOAD ...]     TSV on stdout.
       `--family` supplies the titled family from its hardened owner, for the payloads
       that carry no title line at all (`p441`: 4 of this base's 11 published BSD rows).
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
    # ---------------------------------------------------------------- p440
    # 🟢 `Gap 439-B`'s first family group, bought to that gap's OWN stopping rule:
    # "profile AGPL and GPL-3.0 first -- they are the families a client actually
    # redistributes in this industry".  Every clause below was CALIBRATED against this
    # base's own corpus BEFORE it was written: 69 GPL-family payloads under
    # `compose/code/**/fixtures/**`, whose clause signatures are UNIFORM inside each
    # (family, version) group and DISJOINT across them.  Nothing here is taken from a
    # licence's reputation or from an SPDX identifier.
    #
    # 🔴 WHY THE KEYS CARRY A VERSION AND THE FAMILY LABEL DOES NOT.  `titled_family()`
    # answers `GPL`, never `GPL-2.0` -- and GPL-2.0 and GPL-3.0 are not the same
    # instrument.  Measured here: the 19 stock GPL-2.0 payloads (15 057 B -> 19 350 B)
    # carry NEITHER `basic permissions` NOR `conveying modified source versions`, so a
    # single "GPL" profile written from the 3.0 text condemns all nineteen as TRUNCATED
    # -- a real grant failed by a version it never claimed.  That is `P171` re-imported
    # in a new place, which is precisely the cost `Gap 439-B` priced and declined to pay
    # on `p439`.  The version is resolved FIRST, and a payload whose version cannot be
    # resolved is UNCALIBRATED, never guessed.
    "GPL-3.0": [
        ("basic-permissions", r"basic\s+permissions"),
        ("corresponding-source", r"corresponding\s+source"),
        ("conveying-modified", r"conveying\s+modified\s+source\s+versions"),
        ("disclaimer-of-warranty", r"disclaimer\s+of\s+warranty"),
        ("limitation-of-liability", r"limitation\s+of\s+liability"),
        ("termination", r"\btermination\b"),
    ],
    # 🔴 THE AGPL PROFILE IS THE GPL-3.0 PROFILE PLUS §13, AND §13 IS THE WHOLE POINT.
    # AGPL-3.0 and GPL-3.0 share their operative text almost entirely; the clause that
    # distinguishes them is the one an education client is actually exposed to, because
    # every platform in this industry's LMS tier is reached over a network.  A payload
    # titled AGPL that does not carry §13 has not granted the only term that made it
    # AGPL -- and `frappe/lms`, Open edX and Kuali are all on these shelves under it.
    #
    # 🔴 AND THIS IS EXACTLY WHERE `P171` FIRES IF THE CLAUSE IS CHOSEN BY NAME.  Stock
    # GPL-3.0 carries the string `GNU Affero General Public License` in its own §13
    # HEADING ("Use with the GNU Affero General Public License") and the words
    # `interaction through a network` in that section's body -- so a detector keyed on
    # either phrase reports all 18 of this base's stock GPL-3.0 payloads as AGPL.  The
    # clause taken here is AGPL's OPERATIVE sentence, which GPL-3.0 does not contain.
    # Measured over the corpus it fires on 🟢 15 of 15 full AGPL-3.0 payloads and on
    # 🟢 0 of 18 stock GPL-3.0 payloads.  `C17` holds that line as a control.
    "AGPL-3.0": [
        ("basic-permissions", r"basic\s+permissions"),
        ("corresponding-source", r"corresponding\s+source"),
        ("conveying-modified", r"conveying\s+modified\s+source\s+versions"),
        ("disclaimer-of-warranty", r"disclaimer\s+of\s+warranty"),
        ("limitation-of-liability", r"limitation\s+of\s+liability"),
        ("termination", r"\btermination\b"),
        ("remote-network-heading", r"remote\s+network\s+interaction"),
        ("remote-network-grant",
         r"interacting\s+with\s+it\s+remotely\s+through\s+a\s+computer\s+network"),
    ],
    # GPL-2.0 defines no `Corresponding Source` term and has no `convey` vocabulary: it
    # says `complete corresponding machine-readable source code` and `distribute`.
    # Calibrated on 19 payloads, uniform.  🔵 Note `corresponding source` DOES appear in
    # GPL-2.0 as part of that longer phrase, which is why it is not a 3.0 discriminator
    # and is not asked for here as one.
    "GPL-2.0": [
        ("copy-and-distribute", r"you\s+may\s+copy\s+and\s+distribute"),
        ("machine-readable-source",
         r"complete\s+corresponding\s+machine-readable\s+source\s+code"),
        ("no-warranty", r"no\s+warranty"),
        ("liability-cap", r"in\s+no\s+event"),
    ],
    # ---------------------------------------------------------------- p441
    # 🟢 `Gap 440-A`'s family, BOUGHT — and its PRESCRIPTION REFUTED in the buying.  The
    # gap asked for BSD "the variant resolved from the clause structure, not from the
    # length".  The length half is right and is kept.  🔴 The structure half is UNSOUND
    # and `C26` keeps the proof reproducible: the ONLY text that separates BSD-2 from
    # BSD-3 is the non-endorsement clause, which is also a clause this instrument GRADES.
    # Resolve the variant from it and a BSD-3 payload TRUNCATED AT THAT CLAUSE resolves
    # as a BSD-2, is graded against BSD-2's profile, and comes back 🔴 `GRANT-PRESENT` —
    # a false pass on exactly the truncation shape the instrument exists to catch.
    #
    # 🟢 WHAT IS SOUND IS THE ASYMMETRY, and it is the whole design here.  PRESENCE of the
    # discriminating clause is proof (no BSD-2 contains it); ABSENCE is ambiguous between
    # "a complete BSD-2" and "a BSD-3 cut short".  So the variant is resolved from the
    # payload's own DECLARATION first — the title line, which is the only signal BSD has
    # that is independent of the clauses being graded, and the analogue of GPL's
    # `version 3` — and the structural arm is allowed to answer ONLY in the direction that
    # cannot be wrong.  Everything else DECLINES (`P250`).
    #
    # Calibrated BEFORE it was written, on 11 BSD licence payloads under
    # `compose/code/**/fixtures/**` (164 B → 1 620 B) and 11 probed live from this base's
    # own shelves the same hour (108 B → 2 819 B).  The clause set below is present in
    # 🟢 10 of the 10 complete payloads of both populations and absent from every excerpt.
    #
    # 🔵 THE DISCLAIMER CLAUSES CARRY NO QUOTE CHARACTER, ON PURPOSE.  `C6` is this file's
    # record of a COMPLETE MIT grant condemned by U+201C, and `_QUOTES` folds the
    # typographic forms — but not BSD's other live spelling, ``AS IS'' with a backtick and
    # two apostrophes, which exists on this tree (`apache1.1-real-sakai-manifest.LICENSE`).
    # `express or implied warranties` + `are disclaimed` carries the same obligation and
    # cannot be broken by punctuation at all.  `C31` holds the line.
    "BSD-2": [
        ("source-binary-grant",
         r"redistribution\s+and\s+use\s+in\s+source\s+and\s+binary\s+forms"),
        ("conditions-met", r"provided\s+that\s+the\s+following\s+conditions\s+are\s+met"),
        ("source-notice", r"redistributions\s+of\s+source\s+code\s+must\s+retain"),
        ("binary-notice", r"redistributions\s+in\s+binary\s+form\s+must\s+reproduce"),
        ("warranties-express-implied", r"express\s+or\s+implied\s+warranties"),
        ("warranties-disclaimed", r"are\s+disclaimed"),
        ("liability-cap", r"in\s+no\s+event\s+shall"),
    ],
    # BSD-3 is BSD-2 plus the non-endorsement clause.  🔵 It is listed LAST so a report
    # reads the discriminator in the place a reader looks for it.
    "BSD-3": [
        ("source-binary-grant",
         r"redistribution\s+and\s+use\s+in\s+source\s+and\s+binary\s+forms"),
        ("conditions-met", r"provided\s+that\s+the\s+following\s+conditions\s+are\s+met"),
        ("source-notice", r"redistributions\s+of\s+source\s+code\s+must\s+retain"),
        ("binary-notice", r"redistributions\s+in\s+binary\s+form\s+must\s+reproduce"),
        ("warranties-express-implied", r"express\s+or\s+implied\s+warranties"),
        ("warranties-disclaimed", r"are\s+disclaimed"),
        ("liability-cap", r"in\s+no\s+event\s+shall"),
        ("no-endorsement", r"may\s+be\s+used\s+to\s+endorse\s+or\s+promote"),
    ],
    # 🔴 BSD-0 AND BSD-4 ARE DECLARED-AND-UNPROFILED ON PURPOSE.  Both are RECOGNISED by
    # `resolve_bsd_variant` and neither has a profile, so a payload declaring either
    # grades UNCALIBRATED rather than against a neighbour's clauses.  The reason is this
    # base's own rule and not caution for its own sake: there are 🔴 ZERO 0BSD and ZERO
    # BSD-4 payloads on this tree, so any profile written for them would be taken from a
    # licence's reputation instead of a measured corpus — the one thing `p440`'s GPL group
    # was careful not to do.  0BSD grants with no retention condition at all and BSD-4
    # adds the advertising clause, so neither is approximated by BSD-2.  `Gap 441-B`.
    # 🔴 LGPL IS DELIBERATELY ABSENT AND THAT IS A FINDING, NOT AN OMISSION.  LGPL-3.0
    # is not a standalone grant: its own text says it "incorporates the terms and
    # conditions of version 3 of the GNU General Public License, supplemented by the
    # additional permissions listed below".  Measured on this base's 7 LGPL payloads
    # (3 000 B -> 8 241 B), NONE carries `basic permissions`, `disclaimer of warranty`
    # or `limitation of liability` -- because those live in the GPL-3.0 text it points
    # at.  🔴 So an LGPL profile built from GPL-3.0's clauses would grade every valid
    # LGPL-3.0 payload BY-REFERENCE, and the verdict would be formally true and
    # commercially useless: incorporation by reference is this licence's DESIGN, not a
    # truncation.  Registered as `Gap 440-B`; it needs a verdict vocabulary this
    # instrument does not yet have, so it declines to judge instead.  `C21` pins it.
}

# 🔵 Families whose operative text CHANGES BY VERSION, so the profile key is
# `FAMILY-VERSION` and the version must be resolved before any clause is asked for.
VERSIONED_FAMILIES = ("GPL", "AGPL", "LGPL")

# 🔵 The order below is NOT load-bearing: a payload matching two version declarations
# REFUSES rather than taking the first (`resolve_version`).  Measured over all 69
# GPL-family payloads on this tree, 🟢 zero are ambiguous and zero are unresolvable, so
# the refusal path is a guard against future supply and not a live population.
_VERSION_PATTERNS = [("3.0", re.compile(r"version\s+3")),
                     ("2.0", re.compile(r"version\s+2")),
                     ("1.0", re.compile(r"version\s+1"))]


def resolve_version(text):
    """The licence version a payload DECLARES, or None.

    🔴 Returns None when two different versions are declared.  `P250`: an instrument
    that cannot tell which of two grants it is holding must decline, because the two
    carry different obligations and picking one silently is the error that costs a
    client.  None propagates to GRANT-UNCALIBRATED.
    """
    flat = _norm(text)
    hits = [v for v, rx in _VERSION_PATTERNS if rx.search(flat)]
    return hits[0] if len(hits) == 1 else None


# 🆕 `p441` — the BSD variant DECLARATIONS.  Two word orders per variant, because the
# second one is on live supply and not a precaution: `OpenOLAT/qtiworks`
# (`LICENSE.txt`, 2 058 B · `a5c692f12090`, re-read 2026-10-25) opens *"distributed under
# the 3-clause BSD license"* — the variant named BEFORE the family — and that is the ONLY
# variant declaration anywhere in its 2 058 B.
#
# 🟡 The claim is narrowed to what mutation testing actually showed, rather than left as
# written.  Deleting the reversed patterns does NOT change that payload's verdict, because
# it is COMPLETE and the structural arm then answers `BSD-3` from the endorsement clause.
# What the reversed order buys is the TRUNCATED case: strip that payload's endorsement
# clause and only the declaration can still say it was a BSD-3 and is short of one clause.
# `C29d` is that control, and it is the one that fails when these four patterns go.
BSD_VARIANT_DECLARATIONS = [
    ("BSD-0", r"bsd\s+zero[\s-]clause"), ("BSD-0", r"zero[\s-]clause\s+bsd"),
    ("BSD-2", r"bsd\s+2[\s-]clause"), ("BSD-2", r"2[\s-]clause\s+bsd"),
    ("BSD-3", r"bsd\s+3[\s-]clause"), ("BSD-3", r"3[\s-]clause\s+bsd"),
    ("BSD-4", r"bsd\s+4[\s-]clause"), ("BSD-4", r"4[\s-]clause\s+bsd"),
]
_BSD_DECLS = [(v, re.compile(rx)) for v, rx in BSD_VARIANT_DECLARATIONS]

# The clause that exists in BSD-3 and in no lesser variant.  Named once and used by both
# the profile and the resolver, so the two can never drift apart.
BSD_DISCRIMINATOR = r"may\s+be\s+used\s+to\s+endorse\s+or\s+promote"
_BSD_DISC = re.compile(BSD_DISCRIMINATOR)


def resolve_bsd_variant(text):
    """The BSD variant a payload can be SOUNDLY held to, or None.

    Three arms, in this order, and the order is the whole argument:

      1. 🟢 ONE declaration -> that variant.  Independent of every clause graded.
      2. 🔴 TWO OR MORE declarations -> None.  `P250` again: `GRANT-PRESENT` under BSD-2
         and under BSD-3 are different claims about what a client may do with a name.
      3. 🟢 NO declaration, discriminator PRESENT -> `BSD-3`.  Sound in this direction
         only: the non-endorsement clause appears in no lesser variant, so its presence
         cannot be explained by truncation.  🔴 Its ABSENCE can — a complete BSD-2 and a
         BSD-3 cut short are the same bytes — so that case returns None and the
         instrument declines.  `C26` is the refutation of the alternative.
    """
    flat = _norm(text)
    decl = sorted({v for v, rx in _BSD_DECLS if rx.search(flat)})
    if len(decl) == 1:
        return decl[0]
    if decl:
        return None
    return "BSD-3" if _BSD_DISC.search(flat) else None


# 🔵 Families whose profile key is a VARIANT resolved from the payload, where the variants
# are not versions of one instrument but separate licences under one family name.  Kept
# apart from `VERSIONED_FAMILIES` because the resolution METHOD differs: GPL declares
# `version 3` in its operative text, BSD declares its variant in a title line or not at
# all.  `C32` asserts the GPL path is untouched by this.
VARIANT_FAMILIES = {"BSD": resolve_bsd_variant}


def profile_key(text, family):
    """The CLAUSE_PROFILE key for this payload, or None when there is no profile.

    🔵 Unversioned families pass straight through, so MIT / Apache-2.0 / ISC behave
    exactly as they did at `p439` -- `C4`, `C3` and `C8` are unchanged and still pass.
    """
    if family in VARIANT_FAMILIES:
        # 🔵 `p441`: the resolver answers a WHOLE key (`BSD-3`), not a suffix, because a
        # variant is not a version of one instrument.
        return VARIANT_FAMILIES[family](text)
    if family in VERSIONED_FAMILIES:
        v = resolve_version(text)
        return None if v is None else "%s-%s" % (family, v)
    return family

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
    or (None, None) when the family has no profile here.

    🔵 `p440`: the profile is looked up by `profile_key()`, so a versioned family is
    graded against ITS OWN version's clauses and an unresolvable version declines."""
    profile = CLAUSE_PROFILE.get(profile_key(text, family))
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
    # 🔵 `p440`: reported so a row says WHICH profile judged it.  A verdict whose
    # version is invisible cannot be audited -- `GPL` TRUNCATED and `GPL-2.0`
    # TRUNCATED are different claims about the world.
    key = profile_key(text, family)
    if present is None:
        return {
            "verdict": "GRANT-UNCALIBRATED", "family": family, "profile": key,
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
        "verdict": verdict, "family": family, "profile": key,
        "missing": missing, "present": present, "refs": refs,
        "bytes": len(text.encode("utf-8", "replace")),
    }


FINDING = {
    "GRANT-BY-REFERENCE": "P439-BY-REFERENCE",
    "GRANT-TRUNCATED": "P439-TRUNCATED",
}


def main(argv):
    # 🆕 `p441` — `--family FAM` lets the CALLER supply the titled family, and it exists
    # because of a measurement on this base's own shelves rather than for convenience.
    # 🔴 Of the 11 BSD rows published here, FOUR carry no title line at all
    # (`Open-TutorAi/open-tutor-ai-CE` 1 531 B, `jupyter/nbgrader` 1 512 B,
    # `jupyterhub/jupyterhub` 1 475 B, `open-webui/open-webui` 2 819 B — all four open on
    # `Copyright (c) …`), so `bespoke_census.titled_family()`, which answers from the
    # TITLE by construction, answers None and this instrument never reaches a clause.
    # 🔴 That includes the exact row `Gap 440-A` named as unscreened: a BSD profile alone
    # could not have screened it, which is a correction to the gap's own diagnosis.
    # 🟢 The remedy is NOT to re-answer the family question here — `P171` gives it a
    # hardened owner (`lib/license_family.sh`), which answered `BSD` for all four the same
    # hour — it is to let that owner's answer be PASSED IN.  Default behaviour is
    # unchanged, so every earlier control still holds.
    family_override = None
    if argv and argv[0] == "--family":
        if len(argv) < 2:
            sys.stderr.write("🔴 p439-grant-presence: --family needs a value\n")
            return 2
        family_override, argv = argv[1], argv[2:]
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

    print("payload\tfamily\tprofile\tbytes\tverdict\tmissing\trefs\tfinding")
    findings = 0
    for p in argv:
        path = pathlib.Path(p)
        if not path.is_file():
            sys.stderr.write("🔴 p439-grant-presence: not a file: %s\n" % p)
            return 2
        raw = path.read_text(errors="replace")
        fam = family_override or bc.titled_family(raw)
        r = classify(raw, fam)
        f = FINDING.get(r["verdict"], "")
        if f:
            findings += 1
        print("%s\t%s\t%s\t%d\t%s\t%s\t%s\t%s" % (
            path.name, r["family"], r["profile"] or "-", r["bytes"], r["verdict"],
            ",".join(r["missing"]) or "-", ",".join(r["refs"]) or "-", f or "-"))
    print("#\tfindings\t%d" % findings)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
