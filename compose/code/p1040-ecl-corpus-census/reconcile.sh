#!/usr/bin/env bash
# p1040 limb A4 -- reconcile the hand-read rows back into the census.
#
# Usage: bash reconcile.sh
#
# P1036 forbids publishing a bucket count while UNRECOGNISED rows are unread.
# unread.sh read all 54. This script applies ONE rule per class, on the title
# line that was actually measured, and reconciles to the last row -- the
# arithmetic discipline pass 105 used for the 38->40 correction.
#
# Each rule is keyed on a string a human read in the output, never on a byte
# count (P1024/P1030) and never on a filename (P1029).
set -u
cd "$(dirname "$0")"
python3 -I - <<'PY'
import csv, collections, re

rows = list(csv.DictReader(open('result.unread.2026-10-10.tsv'), delimiter='\t'))
rows = [r for r in rows if r.get('title_line') is not None]

# (bucket, family, regex on the measured title line)
RULES = [
    # --- permissive grants the classifier could not see --------------------
    ('PERMISSIVE', '0BSD',           r'BSD Zero Clause'),
    ('PERMISSIVE', 'ISC',            r'^ISC License'),
    ('PERMISSIVE', 'MIT-BY-REF',     r'licensed under \[MIT\]'),
    # --- copyleft grants the classifier could not see ----------------------
    ('COPYLEFT',   'EUPL',           r'EUPL'),
    ('COPYLEFT',   'AGPL-3.0',       r'GNU Affero General Public License|AFFERO GNU'),
    ('COPYLEFT',   'GPL-3.0',        r'^GNU General Public License'),
    ('COPYLEFT',   'MPL-2.0',        r'Mozilla Public License, version 2\.0'),
    ('COPYLEFT',   'OSL-3.0',        r'Open Software License'),
    ('COPYLEFT',   'GPL-2.0',        r'The Linux Kernel is provided under'),
    # --- public-domain dedication ------------------------------------------
    ('CC',         'CC0-1.0',        r'CC0 1\.0 Universal'),
    # --- NOT grants Globant can build on. Naming these is as load-bearing as
    #     recovering the permissive ones: an UNREAD row promoted by mistake is
    #     a legal problem, not a missed opportunity.
    ('NON-GRANT',  'Elastic-2.0',    r'Elastic License 2\.0'),
    ('NON-GRANT',  'BUSL-1.1',       r'Business Source License'),
    ('NON-GRANT',  'PolyForm',       r'PolyForm'),
    ('NON-GRANT',  'PROPRIETARY',    r'[Pp]roprietary|may not be used, copied'),
    ('NON-GRANT',  'BESPOKE-TOU',    r'BY DOWNLOADING|Community License|Evaluation Dataset License'),
    ('NON-GRANT',  'ALL-RIGHTS-RES', r'版权所有'),
]

# The manifest limb MEASURED these five; they are not title-line matches.
MANIFEST = {
    'rstudio/ggcheck':       ('PERMISSIVE', 'MIT-MANIFEST'),
    'rstudio/tblcheck':      ('PERMISSIVE', 'MIT-MANIFEST'),
    'sidneybissoli/educabr': ('PERMISSIVE', 'MIT-MANIFEST'),
    'sonsoleslp/tna':        ('PERMISSIVE', 'MIT-MANIFEST'),
    'ucbds-infra/ottr':      ('PERMISSIVE', 'BSD-3-MANIFEST'),
}

out, left = [], []
for r in rows:
    slug, title = r['slug'], (r['title_line'] or '')
    if slug in MANIFEST:
        b, f = MANIFEST[slug]; out.append((slug, b, f, 'manifest')); continue
    for bucket, fam, rx in RULES:
        if re.search(rx, title):
            out.append((slug, bucket, fam, 'title')); break
    else:
        left.append((slug, title[:70]))

moved = collections.Counter(b for _, b, _, _ in out)
print(f"hand-read rows: {len(rows)}   classified: {len(out)}   still unread: {len(left)}")
print("\nreclassified out of UNREAD:")
for b, n in moved.most_common(): print(f"  -> {b}: {n}")
print("\nby family:")
for (f, n) in collections.Counter(f for _, _, f, _ in out).most_common():
    print(f"  {f}: {n}")

# Census totals as limb A published them, then corrected.
CEN = {'PERMISSIVE': 802, 'COPYLEFT': 177, 'CC': 50, 'UNREAD': 54}
print(f"\n{'bucket':<12}{'census':>8}{'corrected':>11}   difference")
tot_c = 0
for b in ('PERMISSIVE', 'COPYLEFT', 'CC'):
    corr = CEN[b] + moved[b]; tot_c += corr
    print(f"{b:<12}{CEN[b]:>8}{corr:>11}   +{moved[b]}")
ng = moved['NON-GRANT']; tot_c += ng
print(f"{'NON-GRANT':<12}{0:>8}{ng:>11}   +{ng}  <- named, never promotable")
rem = len(left); tot_c += rem
print(f"{'UNREAD':<12}{CEN['UNREAD']:>8}{rem:>11}   -{CEN['UNREAD']-rem}")
print(f"{'TOTAL':<12}{sum(CEN.values()):>8}{tot_c:>11}   {'RECONCILES' if tot_c==sum(CEN.values()) else 'DOES NOT RECONCILE'}")

print(f"\nstill unread after this pass ({len(left)}) -- next pass's worklist:")
for s, t in left: print(f"  {s}\t{t}")
PY
