#!/usr/bin/env python3
"""p942 item A - adjudicate every published fixture in the two APPEND-ONLY trending
files against the repository's OWN SERVED BYTES.

Classes:
  EXACT     published hash reproduces the payload as served (bytes agree too)
  EXACT-B   published hash reproduces as served, but the published byte count does not
  STRIPPED  published hash reproduces ONLY after trailing newlines are removed
            -> the p940/p941 defect: unreproducible by any reader who fetches the file
  UNMATCHED published hash matches no payload this slug serves on the root ladder
  NOPAYLOAD slug served no grant at all on the root ladder (grant outside root,
            non-standard branch, or the address is gone)
"""
import sys, collections

SP = sys.argv[1]
fx = [l.rstrip("\n").split("\t") for l in open(f"{SP}/fx2.tsv") if "\t" in l and not l.startswith("#")]
raw = collections.defaultdict(set)      # slug -> {(bytes, sha)}
strip = collections.defaultdict(set)
for l in open(f"{SP}/measured.tsv"):
    p = l.rstrip("\n").split("\t")
    if len(p) != 7:
        continue
    slug, br, path, rb, rs, sb, ss = p
    raw[slug].add((int(rb), rs))
    strip[slug].add((int(sb), ss))

counts = collections.Counter()
stripped_rows, unmatched_rows, exactb_rows = [], [], []
for rel, ln, slug, b, h in fx:
    b = int(b)
    if slug not in raw:
        counts["NOPAYLOAD"] += 1
        continue
    rh = {s for (_, s) in raw[slug]}
    sh = {s for (_, s) in strip[slug]}
    if h in rh:
        if (b, h) in raw[slug]:
            counts["EXACT"] += 1
        else:
            counts["EXACT-B"] += 1
            exactb_rows.append((rel, ln, slug, b, h, sorted(x for x, s in raw[slug] if s == h)))
    elif h in sh:
        counts["STRIPPED"] += 1
        served = sorted(raw[slug])
        stripped_rows.append((rel, ln, slug, b, h, served))
    else:
        counts["UNMATCHED"] += 1
        unmatched_rows.append((rel, ln, slug, b, h))

tot = sum(counts.values())
print(f"published fixtures adjudicated : {tot}")
for k in ("EXACT", "EXACT-B", "STRIPPED", "UNMATCHED", "NOPAYLOAD"):
    print(f"  {k:10s} {counts[k]:5d}   {100.0*counts[k]/tot:5.1f}%")
adjud = counts["EXACT"] + counts["EXACT-B"] + counts["STRIPPED"]
if adjud:
    print(f"\nstripped rate among fixtures whose slug served a matching payload: "
          f"{counts['STRIPPED']}/{adjud} = {100.0*counts['STRIPPED']/adjud:.1f}%")
print(f"\ndistinct slugs carrying >=1 STRIPPED fixture: {len({r[2] for r in stripped_rows})}")
print(f"distinct slugs carrying >=1 UNMATCHED fixture: {len({r[4-1] for r in unmatched_rows})}")

print("\n--- STRIPPED, first 25 ---")
for r in stripped_rows[:25]:
    print(f"{r[0]}:{r[1]}  {r[2]}  published {r[3]} B {r[4]}  served {r[5]}")
print(f"\n--- EXACT-B (hash right, bytes wrong), all {len(exactb_rows)} ---")
for r in exactb_rows[:20]:
    print(f"{r[0]}:{r[1]}  {r[2]}  published {r[3]} B {r[4]}  served bytes {r[5]}")
