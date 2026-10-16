"""p242 / P1055 — what the ADDITION DOES: disclosure, narrowing, or a transition.

Why this exists
---------------
Two instruments on this shelf answered a question they were not asked, in the same
pass, and both answers were wrong in the SAME direction: they read *any* departure
from a canonical payload as a change to the GRANT.

1. `p1054` (pass 187) returns `MIT-BODY-PLUS:unclassified-addition` and
   `is_usable_permissive() == False` for
   `AnonymousOnyx22/brightspace-d2l-mcp` (`1 200` B, `main` · `fa9ca3b0d5d1`).
   Its `50` bytes of excess over `MIT_CANONICAL_HIGH` are, read first-hand:

       Portions of this software are derived from brightspace-mcp-server,
       Copyright (c) 2026 Rohan Muppa, used under the MIT License.

   That is an UPSTREAM ATTRIBUTION. It grants no less than MIT; it discloses where
   the code came from — and the upstream it names, `RohanMuppa/brightspace-mcp-server`,
   was read first-hand in the same pass at `1 068` B and classifies `MIT`. The
   downstream row is MORE informative than a bare MIT file, and `p1054` marks it
   unusable.

2. `ACTION VU` (registered by p241) proposed detecting a relicensing by keying on
   "a `LICENSE` payload that names TWO licences and a DATE". Implemented literally
   and swept over this pass's `46` first-hand payloads, that shape fires on `4`
   and is wrong on all `4`: the standard AGPL-3.0 text NAMES GPL-3.0 (its section
   13 is the cross-reference to it) and carries the FSF's own publication dates,
   `19 November 2007` and `28 March 2007`. It found `0` true positives.
   `purysho/EduBoard`, `fentas/lani`, `TouchRefletz/maia.edu` and `rosshd/openlearn`
   are not relicensings; they are four ordinary copyleft grants.

   That is `P171`'s defect class one level up. `P171` is: do not read GPL's
   section-13 TITLE as evidence of Affero. This is: do not read a licence's own
   standard cross-reference as evidence of a SECOND licence.

The shared root
---------------
Both instruments measure that the payload DIFFERS from a template and infer that the
GRANT differs. Those are not the same question. A payload may differ because it
DISCLOSES more (upstream attribution, a third-party component notice, a longer
copyright holder) or because it GRANTS LESS (a field-of-use clause) or because it
grants DIFFERENT THINGS AT DIFFERENT TIMES (a real relicensing). Only the second
and third change what a studio may do.

So this module does not replace either instrument. It classifies the CHARACTER of
the addition, so that `UNDETERMINED` becomes a state a later pass can resolve
instead of a verdict.

The one rule that is NOT relaxed
--------------------------------
`p241`'s rule holds: the absence of a known restriction vocabulary is NEVER
permission. An addition this module cannot read stays `UNDETERMINED` and is NOT
cleared. Clearing is positive-evidence-only — an addition is cleared when it
MATCHES a disclosure shape, never when it merely fails to match a restriction one.

Reuse, not re-listing (`P237`)
------------------------------
The restriction vocabulary is `p1054`'s. It is imported from there by path, never
copied, because a licence-classifier vocabulary that exists in two files is a
vocabulary that will diverge — this base has already paid for that three times
(`P255`, `P237`, `p241`'s cross-instrument table).

No network. The caller supplies bytes.
"""

from __future__ import annotations

import importlib.util
import os
import re

# ---- P237: import p1054's hardened vocabulary by path, do not restate it -------------
_HERE = os.path.dirname(os.path.abspath(__file__))
_P1054 = os.path.join(_HERE, os.pardir, "p1054-mit-plus-clause", "mit_plus.py")


def _load_p1054():
    """Load p1054 by absolute path.

    Why by path and not `import mit_plus`: `make hooks` runs these suites with
    `python3 -I`, which strips the script's own directory from `sys.path`
    (`p355-cwd-portability`). A sibling instrument is therefore not importable by
    name from anywhere, and the Makefile's `cd`-into-the-folder recipe only fixes
    the suite's OWN directory, never its sibling's.
    """
    spec = importlib.util.spec_from_file_location("p1054_mit_plus", _P1054)
    if spec is None or spec.loader is None:  # pragma: no cover - defensive
        raise ImportError(f"cannot load p1054 from {_P1054}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_p1054 = _load_p1054()
RESTRICTION_TERMS = _p1054.RESTRICTION_TERMS
MIT_BODY_MARKER = _p1054.MIT_BODY_MARKER

# ---- kinds ---------------------------------------------------------------------------
CLEAN = "CLEAN"
DISCLOSURE = "DISCLOSURE"
NARROWING = "NARROWING"
TRANSITION = "TRANSITION"
UNDETERMINED = "UNDETERMINED"
STANDARD = "STANDARD"

# ---- the defect this module found IN ITSELF, on its first full sweep -----------------
# Swept over this pass's 49 first-hand payloads, the first cut of `delta_of` returned
# NARROWING on all 8 GPL-3.0/AGPL-3.0 payloads. The reason: `p1054`'s restriction
# vocabulary contains `noncommercial`, and the STANDARD GPL-3.0 text uses that very
# word in its section 6 (`...if you received it noncommercially...`). So the matcher
# was reading a word that belongs to the licence's OWN TERMS as evidence of an added
# restriction — which is `P171`'s defect class a THIRD time, now committed by the
# instrument written to stop it.
#
# The structural fix, rather than deleting the token: a payload that IS a canonical
# licence text has no DELTA to read. There is nothing added to it. Its usability is
# the FAMILY classifier's answer (`lib/license_family.sh`), never this module's. So
# such a payload is reported `STANDARD` and this module declines to grade it.
#
# A standard-text anchor is a phrase that appears in the licence's published text and
# effectively nowhere else. Matched on the whole payload, because these licences carry
# their title at the top and their terms below.
STANDARD_TEXT_ANCHORS = (
    ("GPL-family", "terms and conditions for copying, distribution and modification"),
    ("GPL-family", "gnu general public license"),
    ("GPL-family", "gnu affero general public license"),
    ("GPL-family", "gnu lesser general public license"),
    ("Apache-2.0", "apache license\n                           version 2.0"),
    ("Apache-2.0", "version 2.0, january 2004"),
    ("MPL-2.0", "mozilla public license version 2.0"),
    ("PolyForm", "polyform"),
    ("EPL", "eclipse public license - v 2.0"),
    ("ECL", "educational community license"),
    ("CC", "creative commons attribution"),
)

# ---- the FSF's own publication dates -------------------------------------------------
# These appear in the STANDARD text of the GNU licences. A date in this set is never
# evidence of a relicensing; it is the licence telling you which licence it is.
#   GPL-3.0  / AGPL-3.0 : 29 June 2007 / 19 November 2007
#   AGPL-3.0 preamble   : 28 March 2007 (the Affero GPL v2 reference)
#   GPL-2.0             : June 1991      LGPL-2.1 : February 1999
FSF_PUBLICATION_DATES = (
    "29 june 2007",
    "19 november 2007",
    "28 march 2007",
    "june 1991",
    "february 1999",
    "february 1989",
)

# A licence that NAMES a sibling licence as part of its own standard terms. Reading
# either as "a second licence" is the defect this module exists to stop.
STANDARD_CROSS_REFERENCES = (
    # AGPL-3.0 section 13 -> GPL-3.0, and GPL-3.0 section 13 -> AGPL-3.0.
    ("gnu affero general public license", "gnu general public license"),
    ("gnu general public license", "gnu affero general public license"),
    # LGPL is defined by reference to the GPL.
    ("gnu lesser general public license", "gnu general public license"),
)

# ---- shapes --------------------------------------------------------------------------
# DISCLOSURE: the addition says where code CAME FROM, under terms it names.
# Positive evidence only. Each entry must bind added text to a provenance claim.
DISCLOSURE_PATTERNS = (
    r"portions?\s+of\s+th(?:is|e)\s+(?:software|work|file|code)\s+(?:are|is)\s+derived\s+from",
    r"\bderived\s+from\b[^.]{0,120}?\bused\s+under\b",
    r"\bused\s+under\s+the\s+[A-Za-z0-9.\-+ ]{2,40}\s+licen[cs]e\b",
    r"this\s+product\s+includes\s+software\s+developed\s+(?:at|by)",
    r"\bthird[-\s]party\s+(?:components?|software|libraries|code|dependencies)\b"
    r"[^.]{0,160}?\b(?:their|its)\s+own\s+licen[cs]es?\b",
    r"\bnotices?\s+are\s+retained\b",
    r"\boriginally\s+(?:written|created|authored)\s+by\b",
    r"\bbased\s+on\s+(?:work\s+)?(?:by|from)\b[^.]{0,80}?\blicen[cs]e",
)

# TRANSITION: the payload narrates a CHANGE of licence, bound to an effective moment.
# A transition is about WHEN the copy was obtained, which no other state here is.
TRANSITION_PATTERNS = (
    r"\bwas\s+(?:published|released|licen[cs]ed|distributed)\s+under\b",
    r"\b(?:previously|formerly)\s+(?:published|released|licen[cs]ed|distributed)\b",
    r"\brelicen[cs]ed\b",
    r"\blicen[cs]e\s+change\b",
    r"\bchanged\s+(?:its\s+)?licen[cs]e\b",
    r"\bfrom\s+\d{4}-\d{2}-\d{2}\s+until\s+\d{4}-\d{2}-\d{2}\b",
    r"\bon\s+or\s+after\s+\d{4}-\d{2}-\d{2}\b",
    r"\beffective\s+\d{4}-\d{2}-\d{2}\b",
    r"\bprior\s+releases?\s+remain\s+under\b",
)

_ISO_DATE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_LONG_DATE = re.compile(
    r"\b(?:\d{1,2}\s+)?(?:january|february|march|april|may|june|july|august|september"
    r"|october|november|december)\s+\d{1,2}?,?\s*\d{4}\b",
    re.I,
)


def _material_dates(low: str) -> list:
    """Dates in the payload that are NOT the FSF's own publication dates."""
    found = []
    for m in _ISO_DATE.finditer(low):
        found.append(m.group(0))
    for m in _LONG_DATE.finditer(low):
        tok = " ".join(m.group(0).replace(",", "").split())
        if tok not in FSF_PUBLICATION_DATES:
            found.append(tok)
    return sorted(set(found))


def _is_standard_cross_reference(low: str) -> bool:
    """True when a second licence NAME is present only as a licence's own term."""
    for owner, referenced in STANDARD_CROSS_REFERENCES:
        if owner in low and referenced in low:
            # The owning licence must be the one in the TITLE BLOCK (P171's rule:
            # classify on the title block, never the body).
            head = "\n".join(low.splitlines()[:40])
            if owner in head:
                return True
    return False


def standard_family_of(text: str) -> str:
    """Name the standard licence text a payload IS, or "" if it is not one.

    MIT is held to a STRICTER test than the others, and the asymmetry is deliberate.
    MIT's canonical text is short, fully enumerated and carries no restriction
    vocabulary at all, so ANY restriction term inside an MIT-body payload is an
    addition — whatever the byte count says. Size alone is not enough: a narrowing
    clause can be shorter than `p1054`'s headroom (`graspful`'s clause 2 is), and a
    payload that slipped through on size would be reported `STANDARD` and never
    graded.

    For the long-form licences the opposite holds: their restriction vocabulary IS
    their own terms, and reading it as an addition is the defect recorded above.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()
    if MIT_BODY_MARKER in low:
        if _p1054.classify(raw)["excess"] > 0:
            return ""
        if any(t in low for t in RESTRICTION_TERMS):
            return ""
        return "MIT"
    for family, anchor in STANDARD_TEXT_ANCHORS:
        if anchor in low:
            return family
    return ""


def delta_of(text: str) -> dict:
    """Classify what a payload's departure from a canonical licence DOES.

    Returns a dict carrying the kind plus the evidence for it, so a caller can
    print why rather than just what.
    """
    raw = text if isinstance(text, str) else text.decode("utf-8", "replace")
    low = raw.lower()
    nbytes = len(raw.encode("utf-8"))

    narrowing = sorted({t for t in RESTRICTION_TERMS if t in low})
    disclosure = [p for p in DISCLOSURE_PATTERNS if re.search(p, low)]
    transition = [p for p in TRANSITION_PATTERNS if re.search(p, low)]
    dates = _material_dates(low)
    xref = _is_standard_cross_reference(low)
    std = standard_family_of(raw)

    # A transition needs BOTH the narrative and a date that is not the FSF's own.
    # This is the half `ACTION VU` left out, and it is the half that decides. It is
    # tested FIRST because a relicensing notice can be bolted onto any payload, and
    # whether the grant changed over time outranks what the payload otherwise is.
    if transition and dates:
        kind = TRANSITION
    elif std:
        # A canonical licence text has no addition to read. Ask the family classifier.
        kind = STANDARD
    elif narrowing:
        kind = NARROWING
    elif disclosure:
        kind = DISCLOSURE
    else:
        kind = CLEAN

    return {
        "kind": kind,
        "bytes": nbytes,
        "standard_family": std,
        "narrowing_hits": narrowing,
        "disclosure_hits": len(disclosure),
        "transition_hits": len(transition),
        "material_dates": dates,
        "standard_cross_reference": xref,
    }


def is_relicensing(text: str) -> bool:
    """ACTION VU, implemented so that it is right rather than literal.

    `ACTION VU` as registered ("two licences and a date") fires on every standard
    AGPL-3.0 payload. This requires a transition NARRATIVE and a date that is not
    one the FSF printed in the licence itself.
    """
    return delta_of(text)["kind"] == TRANSITION


def addition_is_disclosure_only(text: str) -> bool:
    """True when the payload's addition only DISCLOSES provenance.

    This is the predicate `p1054` is missing. It is positive-evidence-only: it says
    yes when a disclosure shape MATCHES, never merely because no restriction matched.
    """
    d = delta_of(text)
    return d["kind"] == DISCLOSURE


def resolve_mit_plus(text: str) -> dict:
    """Resolve `p1054`'s `MIT-BODY-PLUS:unclassified-addition` where possible.

    `p1054` is deliberately conservative: it refuses to clear an MIT body with
    bytes added, because the added clause may be written in a vocabulary it does
    not know. That refusal is correct as a DEFAULT and wrong as a VERDICT, and this
    function is the difference.

    Returns the p1054 verdict, this module's reading of the addition, and a
    `usable_permissive` that is True only on POSITIVE evidence.
    """
    p = _p1054.classify(text)
    d = delta_of(text)

    usable = p["verdict"] == "MIT"  # p1054 cleared it outright
    resolution = "p1054-verdict-stands"

    if p["verdict"] == "MIT-BODY-PLUS:unclassified-addition":
        if d["kind"] == DISCLOSURE:
            usable = True
            resolution = "RESOLVED-disclosure-only"
        elif d["kind"] == TRANSITION:
            usable = False
            resolution = "RESOLVED-transition"
        elif d["kind"] == NARROWING:
            usable = False
            resolution = "RESOLVED-narrowing"
        else:
            usable = False
            resolution = "UNRESOLVED-addition-unreadable"

    return {
        "p1054_verdict": p["verdict"],
        "p1054_excess": p["excess"],
        "delta_kind": d["kind"],
        "resolution": resolution,
        "usable_permissive": usable,
        "bytes": d["bytes"],
    }
