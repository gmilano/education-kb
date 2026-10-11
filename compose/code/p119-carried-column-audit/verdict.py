#!/usr/bin/env python3
"""p119 ACTION I - score each CARRIED star claim against the measured count.

Offline: reads claims.tsv and the captured stars TSV. No network.

A star count is a point-in-time reading, so a stale claim is not the same
fault as a wrong one. Three verdicts:
  EXACT  claimed == measured
  DRIFT  |delta| <= max(2, 2% of measured)  - consistent with growth since
  WRONG  outside that band - cannot be explained by drift
"""
import sys, csv

def band(measured):
    return max(2, measured * 0.02)

def main(claims_path, stars_path):
    stars = {}
    with open(stars_path, encoding='utf-8') as fh:
        for row in csv.reader(fh, delimiter='\t'):
            if len(row) < 5: continue
            stars[row[0].lower()] = (int(row[1]), row[2], row[3], row[4])

    out = []
    for row in csv.reader(open(claims_path, encoding='utf-8'), delimiter='\t'):
        if len(row) < 7: continue
        shape, page, ln, slug, raw, claimed, hdr = row
        claimed = int(claimed)
        rec = stars.get(slug.lower())
        if rec is None:
            out.append(('NO-ORACLE', shape, page, ln, slug, claimed, '', '', hdr))
            continue
        measured, dbranch, state, upd = rec
        d = claimed - measured
        if d == 0:        v = 'EXACT'
        elif abs(d) <= band(measured): v = 'DRIFT'
        else:             v = 'WRONG'
        out.append((v, shape, page, ln, slug, claimed, measured, d, hdr))

    for r in out:
        print('\t'.join(str(x) for x in r))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
