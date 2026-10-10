#!/usr/bin/env bash
# p1040 limb A calibration -- does the HEAD-ref path agree with p1029's
# ls-remote path, address for address?
#
# Usage: bash calibrate.sh <p1029-result.tsv> <p1040-result.tsv>
#
# The HEAD-ref change is the only reason a 1 395-address census is affordable,
# so it has to be shown not to change any ANSWER before its results are
# published. Dropping ls-remote could plausibly have changed three things:
#   - the ref resolved (HEAD vs the named default branch)
#   - which licence file was found first
#   - whether a row reads ABSENT
# Agreement is checked on the licence family, the payload bytes and the sha256.
#
# ONE class of disagreement is EXPECTED and is the point of the pass: a row
# p1029 read as UNRECOGNISED that p1040 now names ECL-*. Those are reported
# separately as RECOVERED, never folded into the agreement count.

set -u
cd "$(dirname "$0")"
OLD="${1:-../p1029-lost-address-recovery/result.2026-10-10.tsv}"
NEW="${2:-result.calibration.2026-10-10.tsv}"

python3 -I - "$OLD" "$NEW" <<'PY'
import sys, csv

def rows(path):
    with open(path, newline='') as fh:
        r = csv.DictReader(fh, delimiter='\t')
        return {x['slug']: x for x in r}

old, new = rows(sys.argv[1]), rows(sys.argv[2])
shared = sorted(set(old) & set(new))

agree = []; recovered = []; disagree = []
for s in shared:
    o, n = old[s], new[s]
    o_lic, n_lic = o['licence'], n['licence']
    same_payload = (o['bytes'] == n['bytes']) and (o['sha256'] == n['sha256'])
    if o_lic == n_lic and same_payload:
        agree.append(s)
    elif o_lic == 'UNRECOGNISED' and n_lic.startswith('ECL') and same_payload:
        recovered.append((s, o_lic, n_lic, n['bytes']))
    else:
        disagree.append((s, o_lic, n_lic, o['bytes'], n['bytes'], o['sha256'], n['sha256']))

print(f"compared={len(shared)} agree={len(agree)} recovered_by_ecl={len(recovered)} disagree={len(disagree)}")
print(f"old_only={sorted(set(old)-set(new))} new_only={sorted(set(new)-set(old))}")

if recovered:
    print("\nRECOVERED -- permissive rows p1029 could not see:")
    for s, o, n, b in recovered:
        print(f"  {s}\t{o} -> {n}\t{b} B")
if disagree:
    print("\nDISAGREE -- the HEAD-ref path changed an ANSWER (investigate before publishing):")
    for s, ol, nl, ob, nb, os_, ns in disagree:
        print(f"  {s}\tlic {ol} -> {nl}\tbytes {ob} -> {nb}\tsha {os_} -> {ns}")
PY
