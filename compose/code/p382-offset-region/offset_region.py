"""`Gap 541` — a timezone-offset CENSUS placed into a region, or refused with the reason.

p381 ranked this third and specified two rules: `-0500` alone -> `AMBIGUOUS-NA-LATAM`, and
`{-0400, -0500}` -> North America. 🔵 Both are implemented. This module ALSO implements the
DST-SPAN test, which goes BEYOND the registration, because this base's own shelves already
contain the reasoning and `ACTION ZI-b` already demands it:

    "a `-0500`-only placement must state whether any commit falls outside Mar-Nov"
                                                     -- ACTION ZI-b, agents/trending.md

🟢 WHY THE SPAN TEST IS STRICTLY MORE INFORMATIVE. US Eastern is -0500 in winter and -0400 in
summer; US Central is -0600 in winter and -0500 in summer; Colombia, Peru, Ecuador and most of
Mexico are -0500 ALL YEAR. So the MONTHS a -0500 commit falls in rule candidates OUT:

  * -0500 observed in a DST month (mid-Mar..early-Nov) CANNOT be US Eastern.
  * -0500 observed in a non-DST month CANNOT be US Central.
  * -0500 observed in BOTH windows cannot be any US zone at all -> year-round -0500 -> LATAM.

🔴 Declared limit, and it is the same one p381 named in `Gap 540`: an offset census records the
AUTHOR's clock, not the institution's. `trending.md` already carries the counter-example
("The institution is where it deploys; the author is wherever they are"). This module places
an OFFSET SET; it does not claim to place an organisation.

🟢 Self-contained: stdlib only, so it runs under `python3 -I` from any directory
(`p355-cwd-portability`).
"""

NORTH_AMERICA = "North America"
LATAM = "LATAM"
AMBIGUOUS = "AMBIGUOUS-NA-LATAM"
NOT_RESOLVED = "NOT-RESOLVED"

# US DST runs from the second Sunday in March to the first Sunday in November. Month
# granularity is all a `%ad`-month census carries, so March and November are treated as
# STRADDLING and excluded from both windows rather than guessed at.
_DST_MONTHS = frozenset({4, 5, 6, 7, 8, 9, 10})
_STD_MONTHS = frozenset({12, 1, 2})
_STRADDLE = frozenset({3, 11})


def place_offsets(offsets, months=()):
    """(verdict, reason) for an offset census, optionally with the commit MONTHS.

    `offsets` is any iterable of strings like `-0500`, `+0800`. `months` is an iterable of
    ints 1..12. Returns the verdict and the sentence `ACTION ZI-b` requires.
    """
    offs = {o.strip() for o in offsets if o and o.strip()}
    mset = {int(m) for m in months}

    if not offs:
        return NOT_RESOLVED, "no offset in the census"

    # p381's rule 2, verbatim: one location crossing a DST boundary is a US location.
    if {"-0400", "-0500"} <= offs:
        return NORTH_AMERICA, ("both -0400 and -0500 present: one location crossing a US "
                               "DST boundary, which a year-round -0500 zone cannot produce")
    if {"-0500", "-0600"} <= offs:
        return NORTH_AMERICA, ("both -0500 and -0600 present: US Central crossing a DST "
                               "boundary")

    if offs == {"-0500"}:
        in_dst = mset & _DST_MONTHS
        in_std = mset & _STD_MONTHS
        if in_dst and in_std:
            return LATAM, ("-0500 in both a DST month (%s) and a standard month (%s): no US "
                           "zone holds one offset across both, so this is a year-round -0500 "
                           "zone -- Colombia, Peru, Ecuador or most of Mexico"
                           % (sorted(in_dst), sorted(in_std)))
        if in_dst:
            return AMBIGUOUS, ("-0500 only, and every dated commit falls in a DST month (%s). "
                               "US Eastern is RULED OUT (it reads -0400 then); US Central "
                               "(DST) and year-round LATAM both remain"
                               % sorted(in_dst))
        if in_std:
            return AMBIGUOUS, ("-0500 only, and every dated commit falls in a standard month "
                               "(%s). US Central is RULED OUT (it reads -0600 then); US "
                               "Eastern and year-round LATAM both remain" % sorted(in_std))
        if mset & _STRADDLE:
            return AMBIGUOUS, ("-0500 only, and every dated commit falls in March or November, "
                               "which straddle the DST transition: no candidate is ruled out")
        return AMBIGUOUS, ("-0500 only, with no commit months supplied: US Eastern in winter "
                           "and Colombia/Peru/Ecuador/most of Mexico year-round are "
                           "indistinguishable (p381's rule 1)")

    # Everything else is outside this instrument's remit: it owns the NA/LATAM collision only.
    return NOT_RESOLVED, ("offset set %s is not the -0400/-0500/-0600 collision this "
                          "instrument adjudicates" % sorted(offs))
