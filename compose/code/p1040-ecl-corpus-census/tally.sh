#!/usr/bin/env bash
# p1040 limb A tally -- the bucket counts, named by property (P1037).
set -u
cd "$(dirname "$0")"
R="${1:-result.corpus.2026-10-10.tsv}"
python3 -I - "$R" <<'PY'
import sys, csv, collections
rows=list(csv.DictReader(open(sys.argv[1]), delimiter='\t'))
print(f"rows={len(rows)}")
st=collections.Counter(r['status'] for r in rows)
for k,v in st.most_common(): print(f"  status {k}: {v}")
gr=[r for r in rows if r['licence'] not in ('ABSENT',)]
print(f"\nwith_grant_payload={len(gr)}")
bk=collections.Counter(r['bucket'] for r in gr)
print("buckets (named by PROPERTY, not by member list):")
for k,v in bk.most_common(): print(f"  {k}: {v}")
print("\nfamilies:")
for k,v in collections.Counter(r['licence'] for r in gr).most_common(): print(f"  {k}: {v}")
dv=collections.Counter(r['divergence'] for r in gr if r['divergence'] not in ('-',''))
print("\ndivergence (the Gap 398 mechanism, per row):")
for k,v in dv.most_common(): print(f"  {k}: {v}")
print("\nROWS RECOVERED BY THE ECL WIRING -- permissive rows the old classifier could not see:")
for r in rows:
    if r['divergence']=='RECOVERED-BY-ECL':
        print(f"  {r['slug']}\t{r['licence']}\t{r['bytes']} B\t{r['sha256']}")
unread=[r for r in gr if r['bucket']=='UNREAD']
print(f"\nUNREAD payloads that must be read by hand before any count is published (P1036): {len(unread)}")
for r in unread[:40]:
    print(f"  {r['slug']}\t{r['licence']}\t{r['file']}\t{r['bytes']} B")
if len(unread)>40: print(f"  ... and {len(unread)-40} more")
thr=[r for r in rows if r['status']=='THROTTLED']
print(f"\nTHROTTLED (unmeasured, NOT counted as absent): {len(thr)}")
PY
