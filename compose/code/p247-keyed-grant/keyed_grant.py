#!/usr/bin/env python3
"""p247-keyed-grant — the ENFORCEMENT axis, and the WINDOWLESS name channel.

`ACTION XA` (p246) asked for the anchor ORDER in `lib/license_family.sh` to be fixed so the
`BUSL` branch stops being dead code.  p247 did that (P1062, limb 1, blast radius measured
over 368 fixture payloads: 3 flip, all 3 BSL payloads that were being misread -- two as
**MIT**, one as Apache-2.0).  THIS FILE IS THE HALF THE ORDER CANNOT REACH, and the pass
only found it because it read three real source-available payloads instead of one:

    payload                                     bytes   family_of     commercial_use_ok
    IAGA-TEAM/IAGA-Sentinel        (BSL 1.1)    4 913   BUSL  (fixed) DENIED  (fixed)
    cockroachdb/cockroach          (CSL 2024)   8 766   UNCLASSIFIED  ALLOWED  <-- here
    redpanda-data/common-go  (Redpanda CL)     27 204   UNCLASSIFIED  ALLOWED  <-- here

THREE payloads, THREE DIFFERENT CAUSES, and the first draft of this file got the second one
wrong until the offsets were measured -- which is why they are printed as a column and not
asserted in prose:

  1. ORDER      `IAGA-Sentinel`: name at offset 0, inside the window, stolen by the anchor
                for its own `Change License`.  The HOIST (P1062) fixes it, and only it.
  2. VOCABULARY `cockroachdb/cockroach`: its name sits at offset **0** -- fully inside the
                window -- and no anchor in this base knows the string `CockroachDB Software
                License`.  Position cannot matter for a name nobody looks for.  Same for
                `Redpanda Community License` at offset 2.
  3. WINDOW     `redpanda-data/common-go` ALSO carries a real `Business Source License v.1.1`
                reference, at offset **4 969** of 24 661 -- BEYOND the 4 000-character
                window `osi_family_of` truncates at (P308).  So even after the hoist, the one
                anchor that WOULD have fired cannot see it.  `name_anywhere()` below is
                therefore explicitly WINDOWLESS: it answers a question the shared classifier
                cannot, and it is a SIGNAL, never a family stamp (the family stays the
                classifier's to decide).

And the vocabulary gap goes deeper than the names.  The `CockroachDB Software License`
contains the word "commercial"
     **ZERO** times.  It does not restrict commercial use in words at all: it conditions the
     grant on an ARTEFACT -- "You will not operate the Software or a Modified Version
     without a License Key", "without sharing Telemetry", "License Key: A valid unique code
     or token ... provisioned for You by Licensor" -- and then forbids circumventing the
     "Protective Measures" that enforce it.  Every matcher that enumerates ways of saying
     "restricted" returns ALLOWED on it by construction, which is the CLASS `p241` named:

         > Every one of these matchers enumerates ways of saying "restricted" and treats
         > the absence of its own vocabulary as permission.

     `p241-blanket-denial` does not catch it either, and correctly so: the CSL DOES grant
     something (`GRANT-PRESENT`, grants=1 denials=0).  The grant axis and the restriction
     axis are both blind to a grant that is real but KEYED.

So this instrument asks a POSITIVE question, in the shape p241 prescribed -- not "does this
payload say a restriction word?" but:

         IS THE LICENSEE'S PERMISSION TIED TO AN ARTEFACT THE LICENSOR ISSUES OR MONITORS?

and a payload that answers yes is `KEYED-GRANT`: never permissive, whatever its family reads.

WHY THE NEGATIVE VERDICT IS NAMED `NO-KEYED-CONDITION` AND NOT `OPEN`.  p241's lesson again:
the absence of this signal is not a permission.  A reader who wants a permission verdict must
go and get one; this file refuses to be that reader's default-permit exit.

THE ADVERSARIAL CONTROL THAT SHAPES THE MATCHER, measured and not assumed: `GPL-3.0`'s own
text contains "authorization key" once, "Installation Information" four times and
"technological measures" twice -- so the broad artefact vocabulary MUST be shielded or the
instrument would call the GPL a keyed grant.  The two GNU contexts are the exact inverse of
a keyed grant: section 6 FORCES the distributor to HAND OVER the keys, and section 3 WAIVES
the licensor's anti-circumvention power.  Both are grant-WIDENING.  The shield is therefore
gated on those sentences' own words, and `gpl-3.0.txt` / `agpl-3.0.txt` are in the suite as
first-hand payloads, not as paraphrases.

usage:  python3 -I keyed_grant.py <payload-file> [...]      # one TSV line per file
        python3 -I keyed_grant.py --vocabulary               # print the probe lists (T272)
"""

import re
import sys

# The P308 window, reproduced here only so `in_window` can be REPORTED.  Nothing in this
# file reads it: every scan below is windowless by design.
SHARED_CLASSIFIER_WINDOW = 4000

# ---------------------------------------------------------------------------------------
# The artefact vocabulary.  Deliberately BROAD (it includes the GNU spelling "authorization
# key"), because a narrow vocabulary is a vocabulary that a payload defeats by rewording --
# the defect `p241` found in seven matchers.  Breadth is paid for with the shield below, not
# with omission.
# ---------------------------------------------------------------------------------------
ARTEFACT = {
    "LICENCE-KEY": re.compile(
        r"licen[cs]e key|activation (?:key|code)|product key|authorization key"
        r"|unique code or token|licen[cs]e file(?: that| which)? (?:unlock|enabl)",
        re.I,
    ),
    "TELEMETRY": re.compile(
        r"telemetry|phone(?:s|d)? home"
        r"|usage data (?:is|are|will be|must be) (?:sent|shared|communicated|reported)",
        re.I,
    ),
    "COUNTERMEASURE": re.compile(
        r"technical countermeasures|protective measures|technological (?:protection )?measures"
        r"|designed to enforce the terms|licen[cs]e (?:enforcement|validation) (?:mechanism|service)",
        re.I,
    ),
    # The gap in the subscription anchor is deliberate.  The narrow contiguous form
    # ("subscription is active") misses "a subscription that must be active" and "Your
    # subscription remains in good standing" -- the brittleness p241 named, in miniature.
    # The gap is bounded at 24 characters so the anchor cannot reach across a clause.
    "ENTITLEMENT": re.compile(
        r"entitlement|seats? (?:purchased|licensed)"
        r"|subscription[^.;]{0,24}?(?:active|current|valid|in good standing)"
        r"|active subscription|paid (?:plan|tier|subscription) (?:is )?required",
        re.I,
    ),
}

# The CONDITIONING relation.  The artefact has to sit in a sentence that ties it to the
# licensee's own permission; a definitions-only mention is not a condition.
CONDITIONING = re.compile(
    r"will not|shall not|may not|must not|without|requires?|required|subject to"
    r"|conditioned upon|only (?:if|while|when)|unless|permitted by|provisioned"
    r"|issued (?:to )?you|obtain|terminates?|revoke",
    re.I,
)

# The GNU SHIELD.  A sentence that carries one of these is the INVERSE of a keyed grant:
# GPL-3.0 section 6 compels the distributor to SURRENDER the keys ("Installation
# Information"), and section 3 WAIVES the licensor's power to forbid circumvention.  The
# shield discards the single HIT, never the payload: a hypothetical licence that both waives
# anti-circumvention AND keys its grant elsewhere still fires on the other sentence.
GNU_SHIELD = re.compile(
    r"installation information|forbid circumvention|waive[sd]? any legal power"
    r"|no additional restrictions|anti-circumvention|WIPO copyright treaty"
    r"|covered work.{0,80}effective technological measures"
    # CC-BY-4.0 section 2(a)(4)-(5), found as a FALSE POSITIVE of this very instrument on a
    # real payload in the same pass: `microsoft/autogen`'s root `LICENSE` is CC-BY-4.0 and
    # its sentence "You may not offer or impose any additional or different terms ... or
    # apply any Effective Technological Measures to the Licensed Material" fired
    # COUNTERMEASURE.  It is the INVERSE of a keyed grant -- a prohibition on the LICENSEE
    # imposing enforcement downstream -- and the same waiver shape as GPL-3.0 section 3.
    # The lesson is the one p241 wrote: the shield has to be gated on the sentence's own
    # words, and a new vocabulary earns a new shield clause, not an exception list.
    r"|may not offer or impose|apply any effective technological measures"
    r"|waives (?:and/or agrees not to assert )?any right to prohibit",
    re.I,
)

# A PARAMETER FILE is not a grant, and this is the third state this file answers for.
# Measured in the `ACTION XB` sweep: 5 of the 6 `UNCLASSIFIED` payloads in the 821-payload
# MIT tier are 45-61 BYTE files containing ONLY `YEAR:` and `COPYRIGHT HOLDER:` -- the CRAN
# convention, where `DESCRIPTION` says `License: MIT + file LICENSE` and the `LICENSE` file
# supplies the two PARAMETERS the MIT template needs.  Verified first-hand on
# `rstudio/ggcheck` (45 B payload; `DESCRIPTION` -> `License: MIT + file LICENSE`).
#
# WHY IT MATTERS, and the direction is p308's and not p312's: the shelves' `MIT` cells for
# those five rows are CORRECT, and a first-hand gate that grades the payload alone would
# "correct" five correct cells to `UNCLASSIFIED` -- and `UNCLASSIFIED` is the branch that
# falls to `commercial_use_ok`'s token match.  So the shape has to be a NAMED state, not an
# absence: "this payload is the parameters, the grant is in the manifest".
_CRAN_LINE = re.compile(r"^\s*(?:year|copyright holder|person|organization)\s*:", re.I)


def parameter_file(text):
    """Is this payload a PARAMETER file (CRAN `MIT + file LICENSE`) rather than a grant?

    True only when EVERY non-blank line is a `KEY: value` parameter line from the CRAN
    vocabulary AND there is at least one.  A payload with a grant sentence in it is never a
    parameter file, however short.
    """
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return False
    return all(_CRAN_LINE.match(ln) for ln in lines)

# The WINDOWLESS name channel.  A CLOSED list of source-available / proprietary licence
# NAMES, each anchored on the full multi-word name -- never on a bare acronym, which is the
# P312 criterion this base already pays for ("BSL" alone matches a Brazilian statute, a bank
# and a bootloader).
SOURCE_AVAILABLE_NAMES = (
    ("BUSL", re.compile(r"business source licen[cs]e", re.I)),
    ("Elastic", re.compile(r"elastic licen[cs]e", re.I)),
    ("PolyForm", re.compile(r"polyform (?:noncommercial|shield|strict|small business|perimeter)", re.I)),
    ("SSPL", re.compile(r"server side public licen[cs]e", re.I)),
    ("CAL", re.compile(r"cryptographic autonomy licen[cs]e", re.I)),
    ("FSL", re.compile(r"functional source licen[cs]e", re.I)),
    ("SUL", re.compile(r"sustainable use licen[cs]e", re.I)),
    ("FAIRCODE", re.compile(r"fair[ -]?code", re.I)),
    ("CommonsClause", re.compile(r"commons clause", re.I)),
    ("ConfluentCommunity", re.compile(r"confluent community licen[cs]e", re.I)),
    ("RedpandaCommunity", re.compile(r"redpanda community licen[cs]e", re.I)),
    ("CockroachDB-CSL", re.compile(r"cockroachdb (?:software )?licen[cs]e", re.I)),
    ("TimescaleLicense", re.compile(r"timescale licen[cs]e", re.I)),
    ("MariaDB-BSL", re.compile(r"mariadb business source", re.I)),
)

# The NOTICE shield.  An artefact word can land inside a copyright line -- a holder named
# "Keystone Telemetry Ltd." is not a keyed grant -- and a copyright notice carries no
# condition on anyone's use.  Measured: the MIT fixture with that holder substituted does NOT
# fire even without this shield, because the sentence split already separates the notice from
# the grant; the shield is here so the verdict does not depend on where a `.` happens to fall.
# It is deliberately NARROW: it only discards a notice sentence that states no operating
# condition of its own, so a sentence that both names a holder AND keys the grant still fires.
NOTICE = re.compile(r"copyright\s*(?:\(c\)|©|\bc\b)?\s*\d{4}|all rights reserved", re.I)
OPERATING_CONDITION = re.compile(
    r"without a|without sharing|will not|shall not|may not|must not|requires? a"
    r"|subject to|unless|only (?:if|while|when)|conditioned upon|provisioned|issued (?:to )?you",
    re.I,
)

_WS = re.compile(r"\s+")
# Sentence split.  Legal prose uses `.` inside section numbers ("4.1") and abbreviations, so
# the split keeps a digit-dot-digit together; an over-split would HIDE a conditioning cue
# from its own artefact, which is the direction that loses a finding.
_SENT = re.compile(r"(?<![0-9])[.;:](?![0-9])")


def normalise(text):
    """Whitespace-squeeze only.  No truncation: that is the whole point of this file."""
    return _WS.sub(" ", text).strip()


def sentences(text):
    return [s.strip() for s in _SENT.split(normalise(text)) if s.strip()]


def keyed_grant(text):
    """Return (fires, kinds, hits).

    `hits` carries one (kind, sentence) pair per surviving match so a caller can PRINT the
    sentence that decided -- T272's rule: a verdict you cannot show is a verdict that gets
    copied without its evidence.
    """
    hits = []
    for sent in sentences(text):
        if not CONDITIONING.search(sent):
            continue
        if GNU_SHIELD.search(sent):
            continue
        if NOTICE.search(sent) and not OPERATING_CONDITION.search(sent):
            continue
        for kind, rx in ARTEFACT.items():
            if rx.search(sent):
                hits.append((kind, sent))
    kinds = sorted({k for k, _ in hits})
    return (bool(hits), kinds, hits)


def name_anywhere(text):
    """WINDOWLESS scan for source-available licence names.

    Returns a list of (name, offset) pairs, sorted by offset.  THE OFFSET IS THE POINT: it is
    measured in the SAME whitespace-squeezed coordinates `osi_family_of` truncates at 4 000,
    so `offset >= 4000` says, as a number, that no anchor at any POSITION could have fired on
    that name.  A per-name offset is reported rather than a single minimum because one payload
    can carry both -- `redpanda-data/common-go` has its own name at `2` and a real BSL
    reference at `4 969`, and a single `min()` would have hidden exactly the finding.
    """
    n = normalise(text)
    found = []
    for name, rx in SOURCE_AVAILABLE_NAMES:
        m = rx.search(n)
        if m:
            found.append((name, m.start()))
    return sorted(found, key=lambda p: (p[1], p[0]))


def verdict(text):
    """One line per payload: the TSV row this instrument publishes.

    verdict  kinds  names(name@offset,...)  beyond_window  reach
    """
    fires, kinds, _hits = keyed_grant(text)
    named = name_anywhere(text)
    beyond = [nm for nm, off in named if off >= SHARED_CLASSIFIER_WINDOW]
    if parameter_file(text):
        # Answered FIRST, because it is a statement about what the payload IS: nothing else
        # said about a parameter file is a statement about a grant.
        v = "PARAMETER-FILE"
    elif fires:
        v = "KEYED-GRANT"
    elif named:
        v = "NAMED-SOURCE-AVAILABLE"
    else:
        # NOT "open".  The absence of a keyed condition is not a permission -- p241.
        v = "NO-KEYED-CONDITION"
    return (
        v,
        ",".join(kinds) if kinds else "-",
        ",".join("%s@%d" % (nm, off) for nm, off in named) if named else "-",
        ",".join(beyond) if beyond else "-",
        # The reach statement, in the terms the SHARED classifier works in.
        (
            "unreachable-by-order" if beyond and len(beyond) == len(named)
            else "partly-beyond-window" if beyond
            else "in-window" if named
            else "-"
        ),
    )


def main(argv):
    if len(argv) >= 2 and argv[1] == "--vocabulary":
        print("window-reported-only=%d  (this file never truncates)" % SHARED_CLASSIFIER_WINDOW)
        print("--- ARTEFACT kinds")
        for k in ARTEFACT:
            print("   " + k)
        print("--- SOURCE_AVAILABLE_NAMES (closed list, full names only)")
        for name, _ in SOURCE_AVAILABLE_NAMES:
            print("   " + name)
        return 0
    if len(argv) < 2:
        sys.stderr.write(__doc__.rsplit("usage:", 1)[-1])
        return 2
    print("file\tverdict\tkinds\tnames\tbeyond_window\treach")
    for path in argv[1:]:
        with open(path, encoding="utf-8", errors="replace") as fh:
            row = verdict(fh.read())
        print(path + "\t" + "\t".join(row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
