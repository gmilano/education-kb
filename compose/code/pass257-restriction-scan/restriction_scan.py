"""`pass257-restriction-scan` — run the restriction vocabulary on EVERY payload,
not only on the ones shaped like MIT.

🔴 The defect this closes, measured at `p257` against three real payloads read
first-hand in the same hour:

    payload                                   bytes   p1054 verdict    p1054 hits
    opentutor/opentutor-classifier (USC)       1 812   NOT-MIT-BODY     []
    yetanalytics/project-persephone (Apache)  11 356   NOT-MIT-BODY     []
    moodlehq/moodle-plugin-ci (GPL-3.0)       35 146   NOT-MIT-BODY     []

A permissive grant, a copyleft grant and a NON-COMMERCIAL ACADEMIC licence are
byte-for-byte distinguishable and `p1054` reports them identically.  `classify()`
returns early when `MIT_BODY_MARKER` is absent and hardcodes `"hits": []`, so the
restriction vocabulary is only ever applied INSIDE the MIT-body branch.

🟢 `is_usable_permissive` is NOT wrong — `USABLE_VERDICTS` is a closed set holding
only `MIT`, so nothing restricted was ever published as permissive through it.
The defect is in the EVIDENCE, and the cost is a reader's: `NOT-MIT-BODY` with no
hits reads as *"not MIT, probably fine, check later"* when the correct reading of
the USC payload is *"non-profit use only; commercial use requires a written
agreement with the USC Stevens Center for Innovation."*  `p255` caught PageLM only
because PageLM RECITES the MIT grant before diverging at the eleventh word; a
bespoke academic licence never recites it and so never reaches the vocabulary.

🔵 This is `ACTION YM`/`ACTION YH`'s hole met in the wild for the first time with a
real payload, and it is wider than either registered: the gap is not a missing
title anchor, it is the SCOPE of the scan.

🔴 And the trap that makes a naive fix wrong, also measured rather than read:
verbatim `GPL-3.0` contains the token `noncommercial` in its own anti-circumvention
text.  A scanner that simply reports any vocabulary hit as a restriction flags
every GPL payload.  Each family therefore carries its MEASURED benign hit set, and
the verdict is computed on hits MINUS that set.

───────────────────────────────────────────────────────────────────────────────────
🔴 `p287` — `T-p286b`: THE VOCABULARY WAS ENGLISH-ONLY, AND ITS MISS READ AS
   "NO RESTRICTION" RATHER THAN "CANNOT READ".

Measured at `p286` and reproduced here as a fixture, not described:

    payload                                    bytes   p257 verdict (before)
    sira313/rapkumer   LICENSE (Indonesian)    3 140   UNCLASSIFIED:no-family-no-restriction, 0 hits
    heronerar/OpenGaokao LICENSE (92.9% CJK)  15 992   UNCLASSIFIED:no-family-no-restriction, 0 hits

`rapkumer`'s §3 is titled `LARANGAN PENGGUNAAN KOMERSIAL` — PROHIBITION OF COMMERCIAL
USE — and prohibits commercial use in any form.  `OpenGaokao`'s first clause says
`禁止商业使用` and its body says it is **not** an OSI-approved licence.  Both were
published by this instrument as carrying **no restriction at all**.

🔵 Two things make this `T-p283`'s shape rather than a missing token.  First, the
LOGIC was never wrong — an English control fires `RESTRICTED:added-restriction`
correctly, so the vocabulary's LANGUAGE is the whole defect.  Second, this base
ALREADY KNEW: `lib/license_family.sh::commercial_use_ok` carries zh/ja/ko/es/pt/fr/
de/it restriction phrases, added at `P240`/`P241` for this exact failure.  🔴 **The
class was established in one instrument and never reached the one beside it**, and
the Python channel had no arm for ANY language including the ones the shell fixed.

🟢 So the vocabulary is now keyed BY LANGUAGE (`RESTRICTION_TERMS_BY_LANGUAGE`),
which is what makes a per-language negative control expressible at all; `p287` adds
the **`id`** (Indonesian/Malay) arm the shell lib also lacks, and the shell lib gains
it in the same change.  A phrase is matched, never a bare word: `comercial` appears
in permissive Spanish and 商业 appears in any notice that mentions commercial use in
order to ALLOW it — the same conservatism the shell arm already used.

🔴 And the second half, which is the half that matters more:

    A SCANNER WHOSE VOCABULARY DOES NOT COVER A BODY'S LANGUAGE CANNOT
    DISTINGUISH "NOTHING FOUND" FROM "NOTHING LOOKED FOR".

Adding arms shrinks that set; it cannot empty it.  So `UNREADABLE-BODY` is a verdict
rather than a silence: a substantial body with no family, no hits and **no language
arm** now says *cannot read* instead of *no restriction*.  🔵 Note the one property
that makes the language test cheap enough to trust — the verdict asks only
COVERED-vs-NOT, so a confusion BETWEEN two covered languages cannot change it.  Only
two error directions exist, and the costly one (an uncovered language mistaken for a
covered one) is guarded by requiring positive evidence of a covered language rather
than by assuming it, which is `P241`'s rule: never read the absence of one's own
vocabulary as permission.
"""

# The vocabulary `p1054` carries, lifted verbatim so the two cannot drift apart
# silently — `test_restriction_scan.py` asserts this set is a superset of it.
P1054_TERMS = (
    "commercial use",
    "compete",
    "competing",
    "competitor",
    "field of use",
    "hosted, managed",
    "may not use the software to",
    "non-commercial",
    "noncommercial",
    "saas",
    "software as a service",
    "software-as-a-service",
)

# 🟢 New at `p257`, every one of them PRESENT in the USC payload and absent from
# `p1054`'s vocabulary.  An academic licence restricts with a different register
# than a commercial source-available one: it says "non-profit", not "non-commercial".
ACADEMIC_TERMS = (
    "non-profit",
    "nonprofit",
    "all rights reserved",
    "without a written agreement",
    "research purposes",
    "educational, research",
    "personal, educational",
    "academic use",
    "internal use only",
    "evaluation purposes",
)

# 🟢 `p287` (`T-p286b`).  THE VOCABULARY, KEYED BY LANGUAGE.
#
# The English arm is exactly what `p257` carried, moved rather than rewritten, so
# no English verdict in this base's history changes.  The non-English arms are
# ported PHRASE FOR PHRASE from `lib/license_family.sh::commercial_use_ok`
# (`P240`, `P241`) — two implementations of one predicate are measured against each
# other, never trusted to agree (`p637`), and `test_restriction_scan.py` asserts the
# port both ways.
#
# 🔴 A PHRASE, never a bare word.  `comercial` occurs in permissive Spanish, 商业
# occurs in any notice that mentions commercial use in order to PERMIT it, and
# `komersial` occurs in `rapkumer`'s own §6 MIT carve-out for Feather Icons.
RESTRICTION_TERMS_BY_LANGUAGE = {
    "en": tuple(sorted(set(P1054_TERMS + ACADEMIC_TERMS))),
    # 🟢 NEW at `p287`, and the arm with the live specimen behind it.  `rapkumer`'s
    # §3 is `LARANGAN PENGGUNAAN KOMERSIAL`; `dilarang` is the Indonesian/Malay
    # prohibitive and carries the restriction on its own only in these compounds.
    "id": (
        "larangan penggunaan komersial",
        "penggunaan komersial dilarang",
        "dilarang menggunakan secara komersial",
        "dilarang untuk tujuan komersial",
        "tidak untuk tujuan komersial",
        "tujuan non-komersial",
        "non-komersial",
        "nonkomersial",
        "bukan untuk komersial",
        "tanpa izin tertulis",
    ),
    "es": (
        "uso no comercial",
        "usos no comerciales",
        "fines no comerciales",
        "prohibido el uso comercial",
        "sin autorizacion por escrito",
        "sin autorización por escrito",
    ),
    "pt": (
        "uso nao comercial",
        "uso não comercial",
        "fins nao comerciais",
        "fins não comerciais",
        "proibido o uso comercial",
        "sem autorizacao por escrito",
        "sem autorização por escrito",
    ),
    "fr": (
        "usage non commercial",
        "fins non commerciales",
        "a des fins non commerciales",
        "à des fins non commerciales",
        "sans autorisation ecrite",
        "sans autorisation écrite",
    ),
    "de": (
        "nicht-kommerziell",
        "nicht kommerzielle nutzung",
        "keine kommerzielle nutzung",
        "ohne schriftliche genehmigung",
    ),
    "it": (
        "uso non commerciale",
        "fini non commerciali",
        "senza autorizzazione scritta",
    ),
    "zh": (
        "禁止商业使用",
        "禁止商用",
        "非商业使用",
        "非商业性使用",
        "仅限个人非商业",
        "商业使用必须",
        "商业用途需",
        "商业用途请",
        "不得用于商业",
    ),
    "ja": (
        "商用利用禁止",
        "商用利用は禁止",
        "非営利",
    ),
    "ko": (
        "비상업적",
    ),
    "vi": (
        "phi thương mại",
        "không nhằm mục đích thương mại",
        "cấm sử dụng cho mục đích thương mại",
    ),
}

# The flattened union.  `p257`'s name and contract are preserved exactly — the
# suite's "superset of `p1054`'s vocabulary" control reads THIS, and it must keep
# holding across the re-keying.
RESTRICTION_TERMS = tuple(sorted(
    t for arm in RESTRICTION_TERMS_BY_LANGUAGE.values() for t in arm
))

# The set of languages in which "nothing found" is a MEASUREMENT.  Outside it,
# "nothing found" is an ARTEFACT, and `UNREADABLE-BODY` says so.
COVERED_LANGUAGES = frozenset(RESTRICTION_TERMS_BY_LANGUAGE)

# 🔴 Anchored on the TITLE LINE, and that is a correction this instrument's own
# controls forced at `p257`.  The first draft matched these anchors anywhere in the
# body, with `agpl` ordered before `gpl` so an AGPL payload could not grade as GPL.
# It graded `moodlehq/moodle-plugin-ci`'s verbatim GPL-3.0 (35 146 B, read
# first-hand) as `AGPL` — because **GPL-3.0 section 13, at line 552 of its own
# text, is titled "Use with the GNU Affero General Public License"**.  Every
# GPL-3.0 payload in existence carries that string.  A body-wide anchor for a
# family whose name another family's own text QUOTES can only ever be wrong.
#
# 🟢 So: the family is named by the payload's own title line, which is where a
# licence states what it is.  Ordering within this tuple becomes a tiebreaker
# rather than load-bearing, and that is the point — the fix removes the dependence
# on order instead of getting the order right.
TITLE_ANCHORS = (
    ("apache license", "Apache-2.0"),
    ("gnu affero general public license", "AGPL"),
    ("gnu lesser general public license", "LGPL"),
    ("gnu general public license", "GPL"),
    ("eclipse public license", "EPL"),
    ("mozilla public license", "MPL"),
    ("isc license", "ISC"),
    ("mit license", "MIT"),
    ("bsd", "BSD"),
)

# Stage two, consulted ONLY when the title line names nothing: a BSD or ISC grant
# is routinely shipped with a bare copyright line first, so its operative clause is
# the only anchor available.  Both phrases are ones no other family's text quotes.
BODY_ANCHORS = (
    ("redistribution and use in source and binary forms", "BSD"),
    ("permission to use, copy, modify, and/or distribute this software", "ISC"),
    # 🟢 `p287`, and found the same way the `LICENCE` spelling was — by a real
    # payload, not by reasoning.  `Priyamakeshwari/TeachGPT` ships `LICENSE.md`
    # (1 057 B, `main`): a VERBATIM MIT body whose TITLE LINE IS SIMPLY ABSENT.  It
    # opens on the bare copyright line and goes straight to the operative clause, so
    # the title stage sees no family and stage two had an anchor for BSD and for ISC
    # — the two families that routinely open on a copyright line — AND NOT FOR THE
    # ONE FAMILY THIS BASE PUBLISHES MOST.
    #
    # 🔵 That is `T-p283`'s shape for the third time in one pass and the second time
    # in this one function: `p1054` has carried `MIT_BODY_MARKER` since it was
    # written, so the base already knew an MIT body is identifiable without its
    # title.  The class reached `p1054` and never reached the instrument beside it.
    #
    # 🟡 The direction of this one is the CONSERVATIVE one — `UNCLASSIFIED` is never
    # published as permissive — so it cost no wrong licence claim.  It cost the other
    # thing: a real, usable MIT grant read as unclassifiable, which is a dependency
    # the studio declines for no reason.  Both directions are defects.
    #
    # 🔴 Collision measured before adding, on all 7 fixtures (the rule `P171` exists
    # for — a family name or clause appearing inside ANOTHER family's body):
    #     payload                     carries "permission is hereby granted, free of charge"
    #     mit-1091                    1   <- the only one
    #     apache-2.0-11356            0
    #     gpl-3.0-35146               0
    #     usc-academic-1812           0
    #     rapkumer-id-3140            0   <- and it HAS an MIT carve-out in its §6
    #     opengaokao-zh-15992         0
    #     notfound-14                 0
    # The `rapkumer` row is the one worth naming: a bespoke NON-COMMERCIAL licence
    # that sub-licences a vendored icon set under MIT does NOT recite MIT's grant,
    # so this anchor cannot turn that payload permissive.  Asserted in the suite.
    ("permission is hereby granted, free of charge", "MIT"),
)

# How many leading lines count as the title.  A licence names itself in its first
# line or two; `4` carries headroom for a leading blank line or a rule.
TITLE_LINES = 4

PERMISSIVE_FAMILIES = frozenset({"Apache-2.0", "BSD", "ISC", "MIT"})
COPYLEFT_FAMILIES = frozenset({"AGPL", "GPL", "LGPL", "EPL", "MPL"})

# 🔴 Measured, not assumed.  `moodlehq/moodle-plugin-ci`'s verbatim GPL-3.0 body
# (35 146 B, read first-hand at `p257`) hits `noncommercial`; verbatim Apache-2.0
# (11 356 B) hits nothing.  A family's benign set is the price of not crying wolf.
BENIGN_FAMILY_HITS = {
    "GPL": frozenset({"noncommercial"}),
    "AGPL": frozenset({"noncommercial"}),
    "LGPL": frozenset({"noncommercial"}),
}

VERDICT_RESTRICTED = "RESTRICTED:added-restriction"
VERDICT_FAMILY_PLUS = "FAMILY-PLUS-RESTRICTION:needs-a-human"
VERDICT_PERMISSIVE = "PERMISSIVE"
VERDICT_COPYLEFT = "COPYLEFT"
VERDICT_UNCLASSIFIED = "UNCLASSIFIED:no-family-no-restriction"
# 🟢 NEW at `p287`.  Distinguishes "the vocabulary ran and found nothing" from
# "the vocabulary has no arm for this body's language, so it never looked".
# 🔴 The name carries the reading: the two verdicts above it are MEASUREMENTS and
# this one is an ADMISSION, and a reader who cannot tell them apart ships the
# `rapkumer` payload as unrestricted.
VERDICT_UNREADABLE = "UNREADABLE-BODY:no-vocabulary-for-this-language"

ALL_VERDICTS = (
    VERDICT_RESTRICTED,
    VERDICT_FAMILY_PLUS,
    VERDICT_PERMISSIVE,
    VERDICT_COPYLEFT,
    VERDICT_UNCLASSIFIED,
    VERDICT_UNREADABLE,
)

# 🔴 The consuming arm as a CLOSED allow-list, for `p248`'s reason: a verdict added
# later must not fall through into the usable branch.
USABLE_VERDICTS = frozenset({VERDICT_PERMISSIVE})


# ── The language test ──────────────────────────────────────────────────────────────
#
# 🔵 Why a cheap test is sound HERE and would not be in general: `scan` consults it
# only to ask COVERED-vs-NOT, so confusing two covered languages for each other —
# which is the overwhelmingly likely error, since `es`/`pt`/`it` share function words
# — cannot change a verdict.  Of the two errors that CAN:
#
#   * an uncovered language read as covered   -> a false "no restriction".  COSTLY.
#   * a covered language read as uncovered    -> a false `UNREADABLE-BODY`.  Cheap:
#                                                it asks a human to read a payload.
#
# So the test demands POSITIVE evidence of a covered language and defaults to
# uncovered, which is `P241`'s rule applied to the language axis instead of the
# restriction axis: never read the absence of one's own vocabulary as permission.
#
# 🔴 And the reason script detection alone will not do, which this base measured
# before: `p240-grant-language` returns `LATIN-SCRIPT` for the Indonesian payload and
# thereby certifies that the English token-match APPLIES — on the very body that
# defeats it.  Script is necessary for the CJK arms and insufficient for the rest.

# Non-Latin scripts are identified by codepoint range, because a script IS the
# evidence there.  Ordered so that the Han check cannot swallow Japanese: a body
# with kana is Japanese even though it also carries Han characters.
_SCRIPT_RANGES = (
    ("ja", ((0x3040, 0x309F), (0x30A0, 0x30FF))),          # hiragana, katakana
    ("ko", ((0xAC00, 0xD7AF), (0x1100, 0x11FF))),          # hangul
    ("zh", ((0x4E00, 0x9FFF), (0x3400, 0x4DBF))),          # CJK unified ideographs
)

# A body is called non-Latin-script when this share of its NON-SPACE characters sits
# in one script's ranges.  🔵 `0.10` and not a majority: `OpenGaokao`'s payload is
# 92.9% CJK, but a bespoke grant that states its restriction in Chinese inside an
# otherwise-English document is the harder and more dangerous shape, and it is still
# caught at this floor.
_SCRIPT_SHARE = 0.10

# Latin-script languages are identified by FUNCTION WORDS — closed-class words a
# legal text cannot avoid — never by the content words a licence shares across
# languages (`licence`, `software`, `copyright` travel almost unchanged).
_LATIN_MARKERS = {
    "en": (" the ", " and ", " of ", " to ", " this ", " that ", " is ", " for ",
           " any ", " with ", " shall ", " or ", " not ", " be "),
    "id": (" dan ", " yang ", " untuk ", " dengan ", " tidak ", " ini ", " dalam ",
           " atau ", " adalah ", " pada ", " dari ", " akan "),
    "es": (" el ", " la ", " los ", " las ", " de ", " que ", " para ", " con ",
           " no ", " es ", " y ", " del ", " por ", " se "),
    "pt": (" o ", " a ", " de ", " que ", " para ", " com ", " nao ", " não ",
           " e ", " do ", " da ", " os ", " as ", " por "),
    "fr": (" le ", " la ", " les ", " de ", " que ", " pour ", " avec ", " ne ",
           " est ", " et ", " des ", " du ", " par ", " une "),
    "de": (" der ", " die ", " das ", " und ", " nicht ", " ist ", " fur ", " für ",
           " mit ", " von ", " den ", " dem ", " eine ", " auf "),
    "it": (" il ", " lo ", " la ", " di ", " che ", " per ", " con ", " non ",
           " e ", " del ", " della ", " un ", " una ", " gli "),
    "vi": (" va ", " và ", " cua ", " của ", " khong ", " không ", " duoc ",
           " được ", " cho ", " la ", " cac ", " các "),
}

# How many DISTINCT function words must fire before a language is claimed.  Set by
# measurement against this instrument's own fixtures rather than chosen: at `3` the
# 14-byte `404` body still claims nothing, and every verbatim grant in
# `fixtures-p257` claims English.
_MIN_MARKERS = 3

# Below this many bytes a body has too little text for the marker test to mean
# anything, so `UNREADABLE-BODY` is NOT claimed and the verdict stays
# `UNCLASSIFIED`.  🔵 That is deliberately the quieter direction for short bodies:
# a 14-byte `404` and a 209-byte reference-only pointer are already their own
# classes elsewhere in this base (`p262`), and shouting "cannot read" at them would
# bury the case this verdict exists for.
UNREADABLE_MIN_BYTES = 400


def _script_of(text):
    """The non-Latin script a body is written in, or None."""
    chars = [c for c in text if not c.isspace()]
    if not chars:
        return None
    for lang, ranges in _SCRIPT_RANGES:
        n = sum(1 for c in chars
                if any(lo <= ord(c) <= hi for lo, hi in ranges))
        if n / len(chars) >= _SCRIPT_SHARE:
            return lang
    return None


def language_of(text):
    """The body's language when there is POSITIVE evidence for one, else None.

    Returns a key of `RESTRICTION_TERMS_BY_LANGUAGE` whenever it returns anything,
    so `language_of(body) in COVERED_LANGUAGES` is the only question asked of it.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    script = _script_of(raw)
    if script is not None:
        return script

    # Pad so a marker at the very start or end of a line still has its boundaries.
    low = " " + " ".join(raw.lower().split()) + " "
    scores = {
        lang: sum(1 for m in markers if m in low)
        for lang, markers in _LATIN_MARKERS.items()
    }
    best = max(scores, key=lambda k: scores[k])
    if scores[best] < _MIN_MARKERS:
        return None
    return best


def family_of(text):
    """The licence family the payload NAMES ITSELF, or None.

    Two stages, and the order between them is the whole correctness argument:
    the title line first, because that is where a licence states its identity;
    the operative-clause anchors only when the title named nothing, because a
    BSD or ISC grant often opens with a bare copyright line.

    A body-wide search is deliberately NOT a third stage.  GPL-3.0 quotes the
    Affero GPL by name in its own section 13, so any family whose name appears
    inside another family's text is unresolvable body-wide.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()

    head = "\n".join(
        [ln for ln in low.splitlines() if ln.strip()][:TITLE_LINES]
    )
    for anchor, fam in TITLE_ANCHORS:
        if anchor in head:
            return fam

    for anchor, fam in BODY_ANCHORS:
        if anchor in low:
            return fam
    return None


def scan(text):
    """Scan ANY licence payload.  `hits` is populated unconditionally.

    The contract that distinguishes this from `p1054.classify`: there is no shape
    gate in front of the vocabulary.  A payload that mentions a restriction gets a
    non-empty `hits` whatever it looks like.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()
    nbytes = len(raw.encode("utf-8"))

    fam = family_of(raw)
    hits = tuple(t for t in RESTRICTION_TERMS if t in low)
    benign = BENIGN_FAMILY_HITS.get(fam, frozenset())
    effective = tuple(t for t in hits if t not in benign)
    lang = language_of(raw)

    if effective:
        verdict = VERDICT_RESTRICTED if fam is None else VERDICT_FAMILY_PLUS
    elif fam in PERMISSIVE_FAMILIES:
        verdict = VERDICT_PERMISSIVE
    elif fam in COPYLEFT_FAMILIES:
        verdict = VERDICT_COPYLEFT
    elif lang not in COVERED_LANGUAGES and nbytes >= UNREADABLE_MIN_BYTES:
        # 🔴 `p287`.  No family, no hits — and no arm that could have produced a
        # hit.  Saying `UNCLASSIFIED` here is the claim that nothing was found;
        # the truth is that nothing was looked for.
        verdict = VERDICT_UNREADABLE
    else:
        verdict = VERDICT_UNCLASSIFIED

    return {
        "verdict": verdict,
        "family": fam,
        "bytes": nbytes,
        "hits": hits,
        "benign_hits": tuple(sorted(t for t in hits if t in benign)),
        "effective_hits": effective,
        # 🟢 Published so a reader can tell WHICH arm produced a hit, and so an
        # `UNREADABLE-BODY` row names what it could not read.
        "language": lang,
        "vocabulary_covers_language": lang in COVERED_LANGUAGES,
    }


def is_usable_permissive(text):
    """True only for a payload whose family is permissive AND carries no restriction.

    A row this returns False for must not be published as permissive on any page
    of this KB.  It is deliberately independent of `p1054`: the two instruments
    agree on MIT by construction and this one also grades Apache, BSD and ISC.
    """
    return scan(text)["verdict"] in USABLE_VERDICTS
