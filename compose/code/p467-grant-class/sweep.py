#!/usr/bin/env python3
"""p467 -- grade every probed payload and join it to the index star count.

Closes three gaps in one sweep:
  * `Gap 466-A` -- a `grant_class` for every address, read from the payload's
    first non-blank line (`line1=1`) or, where the family needs the title block
    or body, recorded as `line1=0`.
  * `Gap 466-B` -- the (star, grant-present) pair for every PROBED address, not
    only the published ones, so candidate ordering can be set by measurement.
  * `Gap 466-C` -- `bytes` is carried as provenance and NO verdict reads it.

Input : probe.tsv (addr, head12, branch, path|NO-ROOT-GRANT, bytes, sha256_12)
        stars.tsv (addr, index stars)
Output: grant-class.tsv on stdout
"""
import sys, os
from grant_class import grade, sellable

probe, stars_f, payroot = sys.argv[1], sys.argv[2], sys.argv[3]
stars = {}
for line in open(stars_f):
    a, s = line.rstrip("\n").split("\t")
    stars[a] = int(s)

rows = []
print("addr\tstars\thead12\tbranch\tpath\tbytes\tsha256_12\tfamily\tgrant_class\tversion\tline1\tsellable\tbasis")
for line in open(probe):
    f = line.rstrip("\n").split("\t")
    addr, head, br, path, nbytes, digest = (f + [""] * 6)[:6]
    text = None
    p = os.path.join(payroot, addr, "payload")
    if path not in ("NO-ROOT-GRANT", "UNRESOLVED") and os.path.exists(p):
        text = open(p, encoding="utf-8", errors="replace").read()
    g = grade(text)
    st = stars.get(addr, -1)
    rows.append((addr, st, g))
    print("\t".join([addr, str(st), head, br, path, nbytes, digest,
                     g["family"], g["grant_class"], g["version"],
                     str(g["line1"]), "1" if sellable(g["grant_class"]) else "0",
                     g["basis"]]))

# --- Gap 466-B: the correlation the gap asked for, printed to stderr --------
def band(s):
    if s >= 1000: return "A >=1000"
    if s >= 300:  return "B 300-999"
    if s >= 100:  return "C 100-299"
    return "D <100"

agg = {}
for addr, st, g in rows:
    b = band(st)
    d = agg.setdefault(b, [0, 0, 0])
    d[0] += 1
    if g["grant_class"] != "NO_GRANT":
        d[1] += 1
    if sellable(g["grant_class"]):
        d[2] += 1
print(f"\nGap 466-B -- (stars, grant-present) over n={len(rows)}", file=sys.stderr)
print("band\tn\tgranted\tgrant_rate\tsellable\tsell_rate", file=sys.stderr)
for b in sorted(agg):
    n, gr, se = agg[b]
    print(f"{b}\t{n}\t{gr}\t{gr/n:.2f}\t{se}\t{se/n:.2f}", file=sys.stderr)
tn = sum(v[0] for v in agg.values()); tg = sum(v[1] for v in agg.values()); ts = sum(v[2] for v in agg.values())
print(f"ALL\t{tn}\t{tg}\t{tg/tn:.2f}\t{ts}\t{ts/tn:.2f}", file=sys.stderr)

cls = {}
l1 = [0, 0]
for _, _, g in rows:
    cls[g["grant_class"]] = cls.get(g["grant_class"], 0) + 1
    l1[g["line1"]] += 1
print("\ngrant_class distribution", file=sys.stderr)
for k in sorted(cls, key=lambda k: -cls[k]):
    print(f"{k}\t{cls[k]}", file=sys.stderr)
print(f"\nGap 466-A anchor: family read from FIRST NON-BLANK LINE alone: {l1[1]}/{tn}"
      f"  ({l1[0]} needed the title block or body)", file=sys.stderr)
