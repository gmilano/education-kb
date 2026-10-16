#!/usr/bin/env python3
"""p1058 — three defects measured on pass 243, on payloads read first-hand.

Every classifier on these shelves answers "WHICH licence is this?".  All three
defects below are cases where that question has an answer and the answer is
useless, because the payload does not do what its NAME says it does.

  1. EMPTY-PAYLOAD   a 200 at the declared licence path with ZERO bytes.
                     `rine77/meineschule-digital`: the README says
                     "MIT - siehe LICENSE", the file exists, HTTP 200, 0 B.
                     Every ladder on these shelves documents `byte-floor=1B`
                     and records such a response as FOUND.

  2. SELF-REFERENCE  a canonical licence body NAMES another licence, and a
                     token classifier reads the cross-reference as the family.
                     GPL-3.0 section 13 is titled "Use with the GNU Affero
                     General Public License".  `EdupageAPI/edupage-api`
                     (102 stars) classifies AGPL-3.0 on a GPL-3.0 payload.
                     This is `P171`'s class, reproduced for the FOURTH time
                     (p242 recorded three) by an instrument written at p243
                     WITHOUT reading `lib/license_family.sh` first.  It is a
                     property of the method, not of one codebase.

  3. GRANT-QUALIFIER a restriction placed BEFORE the grant verb, inside the
                     clause that qualifies it.  `123xiaojun/student-management-
                     system`: "For **non-commercial purposes**, permission is
                     hereby granted, free of charge, ...".  The MIT sentence is
                     verbatim.  Nothing is ADDED after it, so an instrument that
                     reads additions (p242-grant-delta) or byte excess over a
                     size ceiling (p1054) is not the channel that catches it.

P237's rule is kept: this file DECIDES NOTHING about a family.  It reports
whether the family question may be asked at all, and hands the payload on.
"""
import re
import sys

# --- 1. the empty / unreadable payload ------------------------------------------------
# A grant is a text.  Zero bytes is not a short text, it is the absence of one, and the
# sha256 of the empty string is the same for every repository on earth.
SHA256_EMPTY = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def payload_state(text, http_code=200):
    """EMPTY-PAYLOAD | UNREADABLE | NON-EMPTY.  Never a licence family."""
    if int(http_code) != 200:
        return "UNREADABLE"
    if text is None:
        return "UNREADABLE"
    if len(text) == 0:
        return "EMPTY-PAYLOAD"
    if text.strip() == "":
        # whitespace only: a file that exists, has bytes, and still grants nothing
        return "EMPTY-PAYLOAD"
    return "NON-EMPTY"


def is_usable_grant(text, http_code=200):
    """A refusal to clear is never a permission (p241's rule, kept)."""
    return payload_state(text, http_code) == "NON-EMPTY"


# --- 2. the licence body's own cross-references ---------------------------------------
# The fix is structural, as p242 required: do not delete the token, establish whether the
# payload IS a canonical body first.  A canonical body's own words are not foreign matter.
_CANON_ANCHORS = (
    # (family, anchor phrases that only appear in that licence's own canonical text)
    ("GPL-3.0", ("gnu general public license", "version 3, 29 june 2007")),
    ("GPL-2.0", ("gnu general public license", "version 2, june 1991")),
    ("AGPL-3.0", ("gnu affero general public license", "version 3, 19 november 2007")),
    ("LGPL-3.0", ("gnu lesser general public license", "version 3, 29 june 2007")),
    ("Apache-2.0", ("apache license", "version 2.0, january 2004")),
    ("ECL-2.0", ("educational community license", "version 2.0")),
    ("MPL-2.0", ("mozilla public license", "version 2.0")),
    ("SSPL-1.0", ("server side public license", "version 1")),
    ("PolyForm-Noncommercial-1.0.0", ("polyform noncommercial license 1.0.0",)),
)

# GPL-3.0's section 13 heading, verbatim.  The ONLY place the standard GPL-3.0 text names
# Affero, together with the two sentences under it.
_GPL3_S13 = "use with the gnu affero general public license"


def canonical_body_of(text):
    """The family whose OWN canonical text this payload is, or None.

    Order matters: AGPL-3.0's body also contains the words "general public
    license", and GPL-3.0's body contains "affero".  Both are decided by the
    title line plus the FSF's own publication date, which the other licence
    does not carry.
    """
    T = (text or "").lower()
    for fam, anchors in _CANON_ANCHORS:
        if all(a in T for a in anchors):
            return fam
    return None


def family_token_evidence(text, token):
    """May `token` be read as evidence of a family in THIS payload?

    Returns (verdict, basis):
      ABSENT            the token is not in the payload at all
      SELF-REFERENCE    present, but only inside the payload's own canonical body
                        -> NOT evidence.  P171's defect, blocked structurally.
      EVIDENCE          present outside any canonical body -> the matcher may read it
    """
    T = (text or "").lower()
    tok = token.lower()
    if tok not in T:
        return ("ABSENT", "token not present")
    canon = canonical_body_of(text)
    if canon is None:
        return ("EVIDENCE", "payload is not a canonical licence body")
    if canon == "GPL-3.0" and tok == "affero":
        # every occurrence must sit inside section 13 for this to be self-reference
        if _GPL3_S13 in T:
            return ("SELF-REFERENCE",
                    "GPL-3.0 section 13 names the Affero licence; "
                    "the payload is GPL-3.0's own canonical body")
    if canon.lower().startswith(tok) or tok in canon.lower():
        return ("EVIDENCE", "token names the payload's own family")
    return ("SELF-REFERENCE",
            "payload is the canonical body of %s; the token is its cross-reference" % canon)


# --- 3. the restriction that qualifies the grant verb ---------------------------------
_GRANT_VERBS = (
    "permission is hereby granted",
    "permission to use",
    "hereby grants",
    "permitted provided that",
)
_RESTRICTION = (
    "non-commercial", "noncommercial", "not-for-profit", "non commercial",
    "personal use only", "academic use only", "educational use only",
    "evaluation purposes only", "inspection and educational purposes only",
)
# How far before the grant verb the qualifier may sit.  "For non-commercial purposes,"
# is 30 characters; the window is deliberately short so that a restriction belonging to a
# DIFFERENT clause elsewhere in the document is not attributed to the grant.
_QUALIFIER_WINDOW = 120


def grant_qualifier(text):
    """QUALIFIED-GRANT | UNQUALIFIED-GRANT | NO-GRANT-VERB.

    The canonical-body test comes FIRST, and that order is the structural fix
    p242 asked for.  A verbatim canonical text cannot carry a prefix narrowing
    — there is nowhere to put one — and its restriction vocabulary is its own
    terms (GPL-3.0 section 6 uses "noncommercially", SSPL section 13 too).  So
    a canonical body is settled by its family and the window is never read.
    The grant-verb vocabulary below therefore only has to cover BESPOKE
    payloads, which is the only place a qualifier can hide.
    """
    canon = canonical_body_of(text)
    if canon is not None:
        return ("UNQUALIFIED-GRANT", "canonical %s body; window not read" % canon)
    T = (text or "").lower()
    hits = [(T.find(v), v) for v in _GRANT_VERBS if v in T]
    if not hits:
        return ("NO-GRANT-VERB", "-")
    pos, verb = min(hits)
    window = T[max(0, pos - _QUALIFIER_WINDOW):pos]
    found = [r for r in _RESTRICTION if r in window]
    if found:
        return ("QUALIFIED-GRANT", "'%s' qualifies '%s'" % (found[0], verb))
    return ("UNQUALIFIED-GRANT", "no restriction in the %d chars before '%s'"
            % (_QUALIFIER_WINDOW, verb))


def report(text, http_code=200):
    """The whole gate, in the order a reader needs it."""
    st = payload_state(text, http_code)
    if st != "NON-EMPTY":
        return {"state": st, "usable": False, "canonical": None,
                "grant": ("NOT-ASKED", "payload is %s" % st)}
    return {"state": st, "usable": True,
            "canonical": canonical_body_of(text),
            "grant": grant_qualifier(text)}


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8", errors="replace") as fh:
            body = fh.read()
        r = report(body)
        print("%-46s %-14s canon=%-28s %s (%s)" % (
            path.split("/")[-1], r["state"], r["canonical"], r["grant"][0], r["grant"][1]))
