#!/usr/bin/env python3
"""p239-query-shape — the predicate 238 passes of query evidence never recorded.

p237 moved supply discovery to the GitHub REST search channel. p238 found that the
channel's `license:` filter ADMITS a download-lure farm and built a gate against the
lures. p239 measures the thing both passes left unrecorded: THE SORT KEY.

Measured this pass, six harvests, on-topic rate of page 1 (education vocabulary over
name + description):

    total_count   sort       page   on-topic
           24     updated      24      91.7%      org:Ed-Fi-Alliance-OSS
          253     updated      30      63.3%      OneRoster in:name,description,readme
        2 326     updated      40       2.5%      ClassLink OR state longitudinal data ...
        7 576     stars        50      48.0%      "OneRoster" OR "Ed-Fi" OR "PowerSchool" ...
        8 618     updated      30       0.0%      Ed-Fi in:name,description,readme
       81 905     updated      40       0.0%      agente educativo OR tutor inteligente ...

The discriminator is NOT breadth. It is breadth INTERACTING WITH A RECENCY SORT:
7 576 results sorted by stars returned 48% on-topic, while 8 618 results sorted by
`updated` returned 0%. Comparable breadth, a 48-point swing, attributable to the sort
key alone.

Why: over a large result set `sort:updated` ranks by LAST PUSH, so it selects for push
FREQUENCY. What pushes most often is not what is most relevant — it is bot-refreshed
job boards, trending-trackers, VPN subscription lists and freshly minted lure
repositories. Relevance is not in the ordering at all.

The same mechanism re-attributes p238's headline. Re-run of p238's own query, same
`total_count` (10 815), same day, sort key the only difference:

    sort:stars    -> 0 of 30 names carry a release-channel word
    sort:updated  -> 3 of 30 do, including a brand p238 never saw (`Jclic-Full-Version`)

The `license:mit` filter is present in BOTH runs and admits the farm in both. What put
the farm on page one was the sort. p238's gate is still needed — `sort:updated` is the
natural choice for "what is new this week" — but the cheapest mitigation is one
parameter, not four predicates.

No network. Classifies a query's SHAPE before it is spent.
"""

RECENCY_SORTS = {"updated", "created", None, "", "recent"}
RELEVANCE_SORTS = {"stars", "forks", "help-wanted-issues"}

# A qualifier that binds the result set to a named namespace. Measured: the one
# scoped query this pass ran returned the highest on-topic rate of the six (91.7%).
SCOPING_QUALIFIERS = ("org:", "user:", "repo:", "topic:")

# Thresholds read off the measurement above, stated as the observations that set them
# rather than as round numbers:
#   - 253 @ updated -> 63.3%   (usable, already degrading)
#   - 2 326 @ updated -> 2.5%  (collapsed)
# The boundary is therefore somewhere in (253, 2326]; CAUTION_MAX is set at the last
# count observed to still work and REFUSE_MIN at the first observed to fail.
CAUTION_MAX = 253
REFUSE_MIN = 2326


def has_scope(query):
    """True when the query binds itself to a namespace rather than the whole index."""
    q = (query or "").lower()
    return any(k in q for k in SCOPING_QUALIFIERS)


def classify(total_count, sort=None, query="", page_size=30):
    """Classify a harvest's shape. Returns (verdict, reason).

    SCOPED  — bound to a namespace; page one is a sample of that namespace.
    SAMPLE  — page one can be read as a sample of the query.
    NARROW  — readable, but the on-topic rate is already falling; narrow it.
    SLICE   — page one is a timestamp slice, NOT a sample. Do not harvest from it.
    HEAD    — relevance-sorted and broad: a sample of the ALL-TIME head, which selects
              for accumulated attention (awesome-lists, curricula), not fresh supply.
    """
    if total_count is None or total_count < 0:
        return "SLICE", "total_count not recorded — an unmeasured harvest is not a sample"

    recency = sort in RECENCY_SORTS
    scoped = has_scope(query)

    if scoped:
        return "SCOPED", (
            f"query is namespace-bound; {total_count} results are that namespace, "
            "not the index — page one is a sample of it"
        )

    if not recency:
        if sort not in RELEVANCE_SORTS:
            return "SLICE", f"unrecognised sort key {sort!r} — record it before spending the query"
        if total_count > REFUSE_MIN:
            return "HEAD", (
                f"sort:{sort} over {total_count} results samples the ALL-TIME HEAD: it "
                "defeats recency-promoted lures but selects for accumulated attention, "
                "so it returns lists and curricula rather than new supply"
            )
        return "SAMPLE", f"sort:{sort} over {total_count} results — relevance-ordered and narrow"

    # Recency-sorted from here down.
    if total_count >= REFUSE_MIN:
        return "SLICE", (
            f"recency sort over {total_count} results ranks by LAST PUSH, so page one "
            f"selects for push frequency, not relevance (measured: {total_count} >= "
            f"{REFUSE_MIN} returned 0-2.5% on-topic) — scope it with org:/topic:, or "
            "sort by stars"
        )
    if total_count > CAUTION_MAX:
        return "NARROW", (
            f"recency sort over {total_count} results is between the last count measured "
            f"to work ({CAUTION_MAX}, 63.3% on-topic) and the first measured to fail "
            f"({REFUSE_MIN}, 2.5%) — readable, but narrow it before trusting an absence"
        )
    return "SAMPLE", (
        f"recency sort over {total_count} results — at or below the {CAUTION_MAX} "
        "observed to still return a readable page one"
    )


def is_harvestable(verdict):
    """May this harvest supply PUBLISHED ROWS?

    HEAD qualifies. This pass's own `sort:stars` harvest measured 48% on-topic and
    actually supplied six published rows (`PowerSchool-API`, `PyPowerSchool`,
    `clever-go`, `LMS-Toolkit`, and two withheld as non-permissive). A control anchored
    on that measurement refused an earlier version of this function that excluded HEAD,
    which is the whole point of anchoring controls on harvests rather than constants.
    """
    return verdict in ("SCOPED", "SAMPLE", "NARROW", "HEAD")


def supports_absence(verdict):
    """May this harvest ground a "there is no X" claim?  A much narrower question.

    NARROW cannot: its own reason says to narrow it before trusting an absence.
    HEAD cannot, and this KB has the counter-example in its own history. p238 ran the
    `FERPA OR COPPA` query and recorded "0 North America education agents". Re-run here
    at `sort:stars`, page one is awesome-lists and CS curricula — it would support the
    same absence. p239 then published 16 permissive North America rows found by scoping
    the query instead. The absence was an artifact of the harvest's shape, twice over.
    """
    return verdict in ("SCOPED", "SAMPLE")


def supports_recency(verdict):
    """May this harvest ground a "this is what is new" claim?

    HEAD cannot: a relevance sort over a broad set returns the all-time head, which is
    where `agents/trending.md` and `repos/trending.md` must never be filled from.
    """
    return verdict in ("SCOPED", "SAMPLE", "NARROW")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        print("usage: query_shape.py <total_count> [sort] [query]")
        return 2
    total = int(argv[1])
    sort = argv[2] if len(argv) > 2 and argv[2] not in ("-", "none") else None
    query = argv[3] if len(argv) > 3 else ""
    verdict, reason = classify(total, sort, query)
    print(f"{verdict}\t{reason}")
    return 0 if is_harvestable(verdict) else 1


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv))
