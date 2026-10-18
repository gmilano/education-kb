"""`ACTION p288` — the THIRD channel.  `p278` grades a row by reading TWO channels, payload
and manifest, and the README is not one of them.

p288's population made that cost visible, because for FIVE of its six rows the payload
channel is empty and the manifest declares nothing, so `p278/sweep.sh` graded them

    NO-CHANNEL   GREY   "neither channel read — this row carries no grade"

and for TWO of those five a third channel was readable on the resolved ref and said
something DECISIVE, in OPPOSITE directions:

  * `anastasasenov/bbmcps`  `readme.md` line 84 -> "This project is open-source and
    available under the MIT License."  The tree is NINE files and NONE of them is a licence
    payload (`NONE_IN_TREE`, 55 paths x 2 refs).  A grant CLAIMED and not SERVED.
  * `hdronamraju/sped-agent` `README.md` line 53 -> "(c) 2026 hdronamraju. All rights
    reserved. ... please ask before reusing the code."  A grant REFUSED in prose, with no
    payload either.

Those two verdicts must not be the same word, and `GREY/neither-channel-read` is the wrong
word for both.  The first is an ASK (`p287`'s reading of `gurukul-ai`, carried forward); the
second is a REFUSAL and the studio must not build on it at all.

🔵 `T-p283`'s shape for the FOURTH time, and this pass found it the same way: the class
reached one instrument and never reached the one beside it.  `pass262-scoped-reservation-
audit/sweep.py` ALREADY fetches the README over FIVE spellings — `README`, `README.md`,
`README.rst`, `README.txt` and the lowercase `readme.md` — but it runs only over slugs the
shelves ALREADY grade `RESTRICTIVE-GRADE`.  A NEW row cannot reach it.  So the reach exists
in this codebase and the gate that grades new rows does not have it.

🔴 And the lowercase rung is not decoration: `bbmcps` serves `readme.md`, NOT `README.md`.
Probed at the uppercase spelling alone it answers 404 on `main`, `master` and `HEAD`, and
this pass's own first reading of it was the false absence "no README on any ref".  The
claim was recovered only because the TREE was enumerated and showed the real spelling.
`p283`'s ladder audit grades the readme ladder in `p279-absence-claims` `CASE-UNVARIED`;
that one is harmless, because it opens this KB's OWN `README.md` at a known local path.
This one was not harmless.

P237's rule holds here: this module has NO network and NO fetch.  It CLASSIFIES README text
and GRADES a claim against a payload family.  The fetch lives in `probe.sh`.
"""

import re

# The path ladder, lowercase rung included.  T272: PRINTABLE, so the next pass extends it
# instead of copying it.  Superset of `pass262`'s EXTRA_PATHS (which this base already ships)
# plus the mixed-case stem that `bbmcps` made this pass look for.
# 🔴 `p283`'s ratchet rejected the first version of this tuple as `STEM-ONLY`: it varied the
# STEM (`README`/`readme`/`Readme`) and spelled every extension ONE way.  That is the very
# defect this pass is about, one axis over, and the ratchet caught it in the instrument
# written to fix it.  The extension case is varied now, so the ladder is `CASE-CLOSED`.
README_PATHS = (
    "README.md", "README", "README.rst", "README.txt",
    "readme.md", "readme", "readme.txt", "Readme.md", "README.markdown",
    "README.MD", "readme.MD", "README.TXT", "README.RST",
)

# A family name alone is NOT a grant claim.  These are the phrasings that actually ASSERT one.
# Anchored on the assertion verb so that a bare mention cannot reach the verdict.
_CLAIM_VERB = r"(?:licen[sc]ed\s+under|available\s+under|released\s+under|distributed\s+under|" \
              r"is\s+licen[sc]ed|under\s+the|covered\s+by|licen[sc]e\s*[:=]\s*)"

_FAMILIES = (
    ("AGPL-3.0", r"(?:GNU\s+)?A(?:ffero\s+)?GPL(?:[-\s]?v?3(?:\.0)?)?"),
    ("LGPL-3.0", r"(?:GNU\s+)?L(?:esser\s+)?GPL(?:[-\s]?v?3(?:\.0)?)?"),
    ("GPL-3.0", r"(?:GNU\s+)?GPL(?:[-\s]?v?3(?:\.0)?)?|GNU\s+General\s+Public\s+Licen[sc]e"),
    ("GPL-2.0", r"(?:GNU\s+)?GPL(?:[-\s]?v?2(?:\.0)?)"),
    ("Apache-2.0", r"Apache(?:\s+Licen[sc]e)?(?:[,\s]+Version)?[-\s]?2(?:\.0)?"),
    ("BSD", r"BSD(?:[-\s]?[23](?:[-\s]?Clause)?)?"),
    ("MPL-2.0", r"M(?:ozilla\s+)?PL(?:[-\s]?2(?:\.0)?)?"),
    ("ISC", r"ISC"),
    ("Unlicense", r"Unlicen[sc]e"),
    ("CC0", r"CC0(?:[-\s]?1\.0)?"),
    ("MIT", r"MIT"),
)

# 🔴 COLLISION CONTROLS, measured before the anchors were trusted.  Every one of these
# strings contains a family token and NONE of them grants anything:
#   "MIT RAISE"            -- the lab in p288's North America leg.  An INSTITUTION.
#   "MIT Media Lab", "MIT OpenCourseWare" -- same shape, and both are plausible in an
#                             education README specifically, which is why this base needs it.
#   "see LICENSE"          -- a POINTER, not a claim.
#   a vendored third-party grant path -- `p280`'s class.
# The verb anchor above already excludes them; `_INSTITUTION` makes it explicit and testable
# rather than incidental, because an incidental exclusion is one a later edit deletes.
_INSTITUTION = re.compile(
    r"MIT\s+(?:RAISE|Media\s+Lab|OpenCourseWare|OCW|App\s+Inventor|Press|Sloan|CSAIL|"
    r"Technology\s+Review|licen[sc]e\s+plate)",
    re.I,
)

# A reservation is a REFUSAL and outranks any family token in the same README.
_RESERVATION = re.compile(
    r"all\s+rights\s+reserved"
    r"|please\s+ask\s+before\s+(?:reusing|using|re-?using)"
    r"|ask\s+(?:me\s+|us\s+)?before\s+(?:reusing|using)"
    r"|not\s+(?:open[-\s]?source|licen[sc]ed\s+for\s+reuse)"
    r"|no\s+licen[sc]e\s+is\s+granted"
    r"|viewing\s+only",
    re.I,
)


# `[MIT](./LICENSE)` -- p287's `AIProf` wrote its claim as a markdown LINK, so the family
# token is wrapped in brackets and the verb sits outside them.  Reduce a link to its text
# before matching, or the postfix arm below cannot see the family at all.
_MDLINK = re.compile(r"\[([^\]]{1,40})\]\([^)]{1,200}\)")

# 🔴 The POSTFIX form, and a control in this pass's own suite is what found it missing:
# `AIProf`'s README reads "This project is [MIT](./LICENSE) licensed." -- family FIRST, verb
# SECOND.  The prefix anchor `_CLAIM_VERB` cannot reach it, and a claim this base has already
# published a correction about is the last one that should go ungraded.
_POSTFIX = r"[-\s]?licen[sc]ed"


def _strip_institutions(text):
    return _INSTITUTION.sub(" ", _MDLINK.sub(r"\1", text))


def readme_claim(text):
    """Classify a README's own licence statement.

    -> ("RESERVATION", None)      an explicit refusal / all-rights-reserved
    -> ("CLAIM", "<FAMILY>")      an affirmative grant claim
    -> ("NO-CLAIM", None)         README read, no licence statement in it
    """
    if text is None:
        return ("NO-README", None)
    if _RESERVATION.search(text):
        return ("RESERVATION", None)
    probe = _strip_institutions(text)
    for family, pat in _FAMILIES:
        if re.search(_CLAIM_VERB + r"\s*(?:the\s+)?" + pat, probe, re.I):
            return ("CLAIM", family)
    # Second arm, ordered AFTER the first so a body carrying both reads the explicit one.
    for family, pat in _FAMILIES:
        if re.search(r"(?:is|are)\s+(?:the\s+)?(?:" + pat + r")" + _POSTFIX, probe, re.I):
            return ("CLAIM", family)
    return ("NO-CLAIM", None)


def channel_verdict(claim, payload_family):
    """Grade the README channel against the payload channel.

    `payload_family` is the family of a licence PAYLOAD actually read, or None when the
    tree was enumerated and carries no candidate grant.
    """
    kind, family = claim
    served = payload_family not in (None, "", "-", "NONE_IN_TREE")

    if kind == "RESERVATION":
        return "RESERVED-AND-SERVED" if served else "RESERVED-NO-PAYLOAD"
    if kind == "CLAIM":
        if not served:
            return "DANGLING-CLAIM"
        return "AGREE" if family == payload_family else "CLAIM-CONFLICT"
    if kind == "NO-CLAIM":
        return "PAYLOAD-ONLY" if served else "SILENT-NO-PAYLOAD"
    return "PAYLOAD-ONLY" if served else "NO-CHANNEL"


# What the studio may do with the row.  A DANGLING-CLAIM is an ASK; a RESERVATION is a STOP.
_POSTURE = {
    "RESERVED-NO-PAYLOAD": "STOP — rights reserved in prose, no grant served",
    "RESERVED-AND-SERVED": "STOP — prose reserves rights against its own payload; resolve first",
    "DANGLING-CLAIM": "ASK — a grant is claimed but never served; request a licence payload",
    "CLAIM-CONFLICT": "STOP — README names one family, payload is another",
    "AGREE": "BUILD-ON — both channels agree",
    "PAYLOAD-ONLY": "BUILD-ON — payload read; README asserts nothing",
    "SILENT-NO-PAYLOAD": "STOP — no grant in any channel",
    "NO-CHANNEL": "STOP — no channel readable",
}


def posture(verdict):
    return _POSTURE.get(verdict, "STOP — ungraded")
