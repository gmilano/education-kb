#!/usr/bin/env python3
"""p531: the promotion queue, recomputed against the CURRENT live curated files.

Why it cannot read `filed_on` from the ledger.  `evidence/address-ledger.tsv` is
written by the pass that ran the ledger, so its `filed_on` column is that pass's
OPENING balance -- an address the previous pass filed still reads `-`.  p531 hit
this directly: the ledger listed `Cvmcosta/ltijs` and `dmitry-viskov/pylti1.3`
as unfiled and they really were, but it listed `openedx/edx-platform` the same
way and p530 had filed it.  So the grant and the mention count come from the
ledger and the FILED test is re-run against the live text.

Both address channels, per p530's 40.6% lesson: a `github.com/owner/repo` URL
and a bare backticked `owner/repo` slug each count as filed.

This is `Gap 531-B`'s instrument in its one-off form.  531-B asks for it as a
`make promotion-queue` target whose output is a pass's promotion INPUT, so a
sweep cannot miss the top of its own ranking the way p530 did.

Usage:
    python3 -I ingest/live-debt.py .
"""
import sys
root = sys.argv[1]
CURATED = ["agents/top.md", "repos/foundations.md", "verticals/solutions.md",
           "intel/market.md", "intel/trends.md", "compose/patterns.md"]
blob = ""
for rel in CURATED:
    with open(f"{root}/{rel}", encoding="utf-8", errors="replace") as fh:
        blob += fh.read().lower() + "\n"
PERMISSIVE = ("mit", "apache-2.0", "bsd", "isc", "unlicense", "ecl-2.0")
rows = []
with open(f"{root}/evidence/address-ledger.tsv", encoding="utf-8") as fh:
    next(fh)
    for line in fh:
        f = line.rstrip("\n").split("\t")
        if len(f) < 6:
            continue
        addr, first, verdict, filed, measured, mentions = f[:6]
        grants = [g.strip().lower() for g in verdict.split("|")]
        if not any(g in PERMISSIVE for g in grants):
            continue
        if addr.lower() in blob:
            continue
        rows.append((int(mentions), addr, verdict, first, measured))
rows.sort(reverse=True)
print(f"unfiled permissive against live curated files: {len(rows)}")
for m, addr, v, first, meas in rows[:30]:
    print(f"{m}\t{addr}\t{v}\t{first}\t{meas}")
