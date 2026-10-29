#!/usr/bin/env python3
"""p533: the promotion queue with a MATERIALITY column -- `Gap 532-B`'s instrument.

p532 shipped the queue ranked by `distinct_passes`: how many passes of this base
have described an address and never filed it.  That is a RECALL measure, and
p532 said so itself -- its top ten spanned 78,100 stars down to 1.  This pass
measured the queue head and the ranking turns out to be worse than merely noisy:

  * recall rank 1  -- DMontgomery40/mcp-canvas-lms, 16 distinct passes, 104 stars
                      -- has NO LICENCE FILE at 15 probed paths.  The top of the
                      queue is not promotable at all.
  * recall rank 18 -- freeCodeCamp/freeCodeCamp -- is BSD-3-Clause and 458,181
                      stars, 32x the next-largest unfiled address.
  * 4 of 35 queue-head addresses are archived or have not been pushed in over a
    year.  A recall count cannot notice that an address has died.

So promotion priority needs three inputs, not one: does the grant let us build
(gate), is the address alive (gate), and how much does it matter (rank).

Usage:
    python3 -I ingest/promotion-rank.py . evidence/materiality-measurements.2026-10-29-p533.tsv
"""
import sys

root, measurements = sys.argv[1], sys.argv[2]

CURATED = ["agents/top.md", "repos/foundations.md", "verticals/solutions.md",
           "intel/market.md", "intel/trends.md", "compose/patterns.md"]
PERMISSIVE = ("mit", "apache-2.0", "bsd", "bsd-3-clause", "bsd-2-clause",
              "isc", "unlicense", "ecl-2.0")
STALE_BEFORE = "2025-10-29"   # one year before this pass

# Both address channels, per p530's 40.6% lesson: a github.com URL and a bare
# backticked owner/repo slug each count as filed.
blob = ""
for rel in CURATED:
    with open(f"{root}/{rel}", encoding="utf-8", errors="replace") as fh:
        blob += fh.read().lower() + "\n"

# Measured materiality, keyed by address.
meas = {}
with open(measurements, encoding="utf-8") as fh:
    next(fh)
    for line in fh:
        f = line.rstrip("\n").split("\t")
        if len(f) >= 7:
            meas[f[0].lower()] = dict(stars=f[1], grant=f[2], channel=f[3],
                                      pushed=f[4], archived=f[5], note=f[6])


def band(stars):
    """Materiality band.  Stars are a weak proxy for how much an address matters,
    but they are three orders of magnitude better than a mention count."""
    if not stars.isdigit():
        return "?"
    n = int(stars)
    return "A" if n >= 10000 else "B" if n >= 1000 else "C" if n >= 100 \
        else "D" if n >= 10 else "E"


rows = []
with open(f"{root}/evidence/address-ledger.tsv", encoding="utf-8") as fh:
    next(fh)
    for line in fh:
        f = line.rstrip("\n").split("\t")
        if len(f) < 7:
            continue
        addr, first, verdict, filed, measured, mentions, dpasses = f[:7]
        if addr.lower() in blob:          # already filed -- re-run live, not from the ledger
            continue
        m = meas.get(addr.lower())
        # Prefer a grant measured from the licence file's own title block over the
        # ledger's carried verdict (shelf rules 8-9: the API grades licences badly).
        grant = m["grant"] if m else verdict
        grants = [g.strip().lower() for g in grant.replace("+", "|").split("|")]
        permissive = any(g in PERMISSIVE for g in grants)
        if not m and not permissive:
            continue
        archived = (m or {}).get("archived", "unknown") == "YES"
        pushed = (m or {}).get("pushed", "unmeasured")
        stale = pushed != "unmeasured" and pushed < STALE_BEFORE
        stars = (m or {}).get("stars", "unmeasured")
        # Report every gate that fires, and distinguish a grant that is known
        # absent from one that was merely never read.  Per shelf rule 8 an API
        # `NOASSERTION` means "the title block has not been read", not "no
        # grant exists" -- and `projectfedena/fedena` is the case where it
        # could not be read, because the API indexes the repo and `raw` serves
        # nothing for it.  Calling that "ungranted" claims more than was shown.
        unreadable = grant.strip().upper() in ("UNRESOLVED", "NOASSERTION", "")
        reasons = []
        if not permissive:
            reasons.append("grant-unresolved" if unreadable else "ungranted")
        if archived:
            reasons.append("archived")
        if stale:
            reasons.append("stale")
        blocked = "+".join(reasons)
        rows.append(dict(addr=addr, dpasses=int(dpasses), mentions=int(mentions),
                         stars=stars, band=band(stars), grant=grant,
                         channel=(m or {}).get("channel", "ledger-carried"),
                         pushed=pushed, blocked=blocked, first=first,
                         promotable="no" if blocked else "yes"))

# Promotable first, then by measured materiality, then by recall.
rows.sort(key=lambda r: (r["promotable"] != "yes",
                         -(int(r["stars"]) if r["stars"].isdigit() else -1),
                         -r["dpasses"]))

cols = ["rank", "promotable", "blocked", "stars", "band", "grant", "channel",
        "pushed", "distinct_passes", "mentions", "address", "first_seen_pass"]
print("\t".join(cols))
for i, r in enumerate(rows, 1):
    print("\t".join([str(i), r["promotable"], r["blocked"] or "-", r["stars"],
                     r["band"], r["grant"], r["channel"], r["pushed"],
                     str(r["dpasses"]), str(r["mentions"]), r["addr"], r["first"]]))
