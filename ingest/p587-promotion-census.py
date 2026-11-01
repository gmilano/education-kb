#!/usr/bin/env python3
"""p587 — the promotion census, re-scoped.  NOT A NEW INSTRUMENT; see provenance.

PROVENANCE, stated first because this base's recurring defect is claiming novelty
for something it already holds:

  * ingest/promotion-rank.py   (p533) -- established that promotion needs TWO
                                        GATES (grant, liveness) and ONE RANK,
                                        and that a recall count "cannot notice
                                        that an address has died".
  * ingest/history-backlog.py  (p539) -- HISTORY-minus-FILED, ranked.
                                        Measured 4,144 history addresses
                                        against 240 filed (5.8%).
  * ingest/backlog-gate.py     (p539) -- runs the two gates over that backlog
                                        in bulk.
  * repos/trending.md          (p585) -- published 3,094 of 3,415 discovered
                                        addresses never filed (~90%).

WHAT THIS ADDS.  A narrow denominator that can be audited by hand: the two
append-only logs against the seven curated pages ONLY -- no evidence/, no
archive/.  Result at p587: 3,483 log addresses, 679 curated, 2,841 (81.6%)
never filed; 39 re-found 10+ times, 4 re-found 20+ times.  Those figures are
NOT comparable to p539's or p585's and are not offered as corrections to them.

WHAT IT SETTLED.  The head of the ranked backlog, measured first-hand, contains
BOTH classes interleaved, which is why the rank alone is not decision-grade:

  26x  microsoft/ai-agents-for-beginners   MIT      78,542*  -> filed p587
  26x  rohitg00/ai-engineering-from-scratch MIT     76,141*  -> filed p587
  19x  virgiliojr94/book-to-skill           MIT     36,673*  -> filed p587
  18x  littlecookie0722/AI-Teaching-Agent   MIT          0*  -> noise
  17x  foradian/fedena                      --          --   -> DOES NOT EXIST
  14x  mitodl/open-learning-ai-tutor        --          --   -> DOES NOT EXIST
  16x  eth-lre/mathtutorbench               no grant    46*  -> not adoptable
  36x  openedx/edx-platform                 pre-rename      -> correctly unfiled

So: gate on grant, gate on liveness, THEN rank -- exactly p533's rule.  All
three inputs arrive free in the `gh api search/repositories -f q=repo:o/n` row
that confirms the address exists, together with default_branch (see 587-D).

Run:  python3 -I ingest/p587-promotion-census.py .
"""
import re, collections, os
CURATED = ["agents/top.md","repos/foundations.md","verticals/solutions.md",
           "intel/market.md","intel/trends.md","compose/patterns.md","README.md"]
LOGS = ["agents/trending.md","repos/trending.md"]
ADDR = re.compile(r'github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?=[)\s/#,`"\']|$)')
SKIP = {"topics","features","orgs","collections","sponsors","apps","marketplace",
        "settings","trending","about","search","login","signup","readme"}
def addrs(path):
    c = collections.Counter()
    if not os.path.exists(path): return c
    for line in open(path, encoding="utf-8", errors="replace"):
        for m in ADDR.finditer(line):
            o, r = m.group(1), m.group(2).rstrip('.')
            if o.lower() in SKIP or not r or r.endswith('.md'): continue
            c[f"{o}/{r}"] += 1
    return c
cur = collections.Counter()
for p in CURATED: cur.update(addrs(p))
log = collections.Counter()
for p in LOGS: log.update(addrs(p))
unpromoted = {a: n for a, n in log.items() if a not in cur}
print(f"addresses in append-only logs      : {len(log)}")
print(f"addresses on curated pages         : {len(cur)}")
print(f"in logs but on NO curated page     : {len(unpromoted)}")
print(f"  of those, re-found 10+ times     : {sum(1 for n in unpromoted.values() if n >= 10)}")
print(f"  of those, re-found 20+ times     : {sum(1 for n in unpromoted.values() if n >= 20)}")
print("\n=== TOP 30 UNPROMOTED BY RE-FIND COUNT ===")
print("refinds\taddress")
for a, n in sorted(unpromoted.items(), key=lambda kv: -kv[1])[:30]:
    print(f"{n}\t{a}")
