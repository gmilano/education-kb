#!/usr/bin/env python3
"""p662: re-implement the ledger's OWN filed_on derivation out-of-tree and
compare it against the stored column.  Definition copied from
ingest/address-ledger.py: an address is `filed` iff a `github.com/owner/repo`
address occurs in one of the six CURATED files."""
import os, re, sys, collections
root = sys.argv[1]
CURATED = ["agents/top.md","repos/foundations.md","verticals/solutions.md",
           "intel/market.md","intel/trends.md","compose/patterns.md"]
ADDR = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9_.-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)")

tree = collections.defaultdict(set)          # addr_lower -> {file}
for f in CURATED:
    for m in ADDR.finditer(open(os.path.join(root,f),encoding='utf-8').read()):
        repo = m.group(2)
        for suf in (".git",):
            if repo.endswith(suf): repo = repo[:-len(suf)]
        tree[f"{m.group(1)}/{repo}".lower()].add(f)

rows = [l.rstrip("\n").split("\t") for l in
        open(os.path.join(root,"evidence/address-ledger.tsv"),encoding='utf-8')][1:]

stale, unindexed, moved, agree = [], [], [], 0
for r in rows:
    if len(r) < 4: continue
    addr, first, verdict, filed = r[0], r[1], r[2], r[3]
    a = addr.lower()
    actual = tree.get(a, set())
    claims = {x.strip().split(":")[0] for x in filed.split(",") if x.strip() and x.strip() != "-"}
    claims_curated = {c for c in claims if c in CURATED}
    if not claims:
        if actual: unindexed.append((addr, first, verdict, "-", ",".join(sorted(actual))))
        else: agree += 1
    else:
        if claims_curated & actual: agree += 1
        elif actual: moved.append((addr, first, verdict, filed, ",".join(sorted(actual))))
        else: stale.append((addr, first, verdict, filed, "NOWHERE"))

tree_total = len(tree)
print(f"curated_distinct_addresses_in_tree\t{tree_total}")
print(f"ledger_rows\t{len(rows)}")
print(f"ledger_filed_on_claims\t{sum(1 for r in rows if len(r)>3 and r[3] not in ('-',''))}")
print(f"agree\t{agree}")
print(f"STALE_filed_on__ledger_says_filed_tree_says_nowhere\t{len(stale)}")
print(f"MOVED_filed_on__filed_but_on_a_different_page\t{len(moved)}")
print(f"UNINDEXED__tree_has_it_ledger_says_unfiled\t{len(unindexed)}")
print(f"HONEST_FILED_COUNT (distinct ledger addresses present in curated tree)\t"
      f"{sum(1 for r in rows if len(r)>3 and r[0].lower() in tree)}")
print()
for name, lst in (("STALE",stale),("MOVED",moved),("UNINDEXED",unindexed)):
    print(f"### {name}  n={len(lst)}")
    for x in sorted(lst): print("\t".join(x))
    print()
