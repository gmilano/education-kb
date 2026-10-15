"""p224 - ACTION SA: p223's self-claim date gate, generalised to a TABLE.

`ACTION SA` asked whether p223's gate should become general:

    limb 1: 2+ OTHER refuted claims on these shelves (a licence range, a market figure,
            a ministry date) are re-asserted somewhere in live prose -> the table is the
            right shape and the gate becomes general.
    limb 2: 0-1 -> the AI Act date was a one-off and the gate stays single-purpose.

p223's gate hard-coded one subject. This reads (subject, refuted_pattern, correction)
rows from `evidence/sa-refuted-claims.2026-10-15-p224.tsv`, so adding a subject is a data
change rather than a code change.

Two of p223's rules are kept verbatim because they are what made its gate correct:

  * THE UNIT IS THE MATCHED SPAN, NOT THE LINE. p223's gate exonerated a line because a
    quote mark appeared elsewhere on it. A span is scored on its own characters.
  * QUOTED IS ATTRIBUTED, BARE IS ASSERTED. This KB may REPORT a refuted claim as
    somebody else's (that is what a declared-blank or a conflict cell does); it may not
    STATE one as its own. Only ASSERTED is a defect.
"""

import csv
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
TABLE = os.path.join(ROOT, 'evidence', 'sa-refuted-claims.2026-10-15-p224.tsv')

SHELVES = [
    'agents/top.md', 'agents/trending.md', 'repos/foundations.md', 'repos/trending.md',
    'verticals/solutions.md', 'intel/market.md', 'intel/trends.md', 'compose/patterns.md',
]

# p223's span window and quote detection.
_SPAN = 120
_QUOTED = re.compile(r'["“”‘’«»]')
# A pass heading or an explicit historical marker: this KB records what a PRIOR pass
# found, and that is history, not a live claim.
_HISTORICAL = re.compile(
    r'(?i)(^#{2,4}\s*pass\s*\d+|p\d{2,3}\s*(found|said|reported|carried)|'
    r'prior pass|refuted|corrected|was wrong|no longer)')


def load_table(path=TABLE):
    rows = []
    with open(path, newline='') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            rows.append({
                'subject': r['subject'],
                'subject_re': re.compile(r['subject_pattern']),
                'refuted_re': re.compile(r['refuted_pattern']),
                'correction': r['correction'],
                'refuted_by': r['refuted_by'],
                'exempt_re': re.compile(r['exempt_pattern']) if r.get('exempt_pattern') else None,
            })
    return rows


def classify_span(span, row):
    """None | 'ASSERTED' | 'ATTRIBUTED', scored on the SPAN's own characters."""
    if not row['refuted_re'].search(span):
        return None
    if not row['subject_re'].search(span):
        return None
    if row['exempt_re'] is not None and row['exempt_re'].search(span):
        return None
    if _HISTORICAL.search(span):
        return None
    return 'ATTRIBUTED' if _QUOTED.search(span) else 'ASSERTED'


def scan(files=None, table=None):
    table = table if table is not None else load_table()
    files = files if files is not None else SHELVES
    hits = []
    for rel in files:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        with open(path, errors='replace') as fh:
            for n, line in enumerate(fh, 1):
                for row in table:
                    for m in row['refuted_re'].finditer(line):
                        lo, hi = max(0, m.start() - _SPAN), min(len(line), m.end() + _SPAN)
                        span = line[lo:hi]
                        verdict = classify_span(span, row)
                        if verdict:
                            hits.append({
                                'verdict': verdict, 'subject': row['subject'],
                                'file': rel, 'line': n,
                                'correction': row['correction'],
                                'text': span.strip()[:200],
                            })
    return hits


CONTROLS = [
    # (span, subject index, expected) - 6 of the 9 must NOT fire.
    ('the EU AI Act is fully effective August 2026 for education', 0, 'ASSERTED'),
    ('Reported as "fully effective August 2026", which this KB refutes', 0, None),
    ('Annex III education high-risk applies 2027-12-02, not August 2026', 0, None),
    ('Article 50 transparency has applied since August 2026', 0, None),
    ('## Pass 221 - 94.3% of GNU cells carry no bound', 1, None),
    ('94.3% of these grants are unspecified grants across the shelf', 1, 'ASSERTED'),
    ('94.3% is a bare token count, with a grammar footnote', 1, None),
    ('openeducat ships LGPL-3.0 | bare, a silence on the bound', 2, 'ASSERTED'),
    ('openeducat LGPL-3 is Odoo\'s positive only form', 2, None),
]


def self_test():
    table = load_table()
    bad = 0
    for span, idx, expected in CONTROLS:
        got = classify_span(span, table[idx])
        mark = 'ok  ' if got == expected else 'FAIL'
        if got != expected:
            bad += 1
        print('{} expected={!s:11s} got={!s:11s} {}'.format(mark, expected, got, span[:70]))
    print('\n{} controls, {} failures ({} must NOT fire)'.format(
        len(CONTROLS), bad, sum(1 for c in CONTROLS if c[2] is None)))
    return bad


if __name__ == '__main__':
    rc = self_test()
    print('\n--- live scan ---')
    hits = scan()
    asserted = [h for h in hits if h['verdict'] == 'ASSERTED']
    attributed = [h for h in hits if h['verdict'] == 'ATTRIBUTED']
    print('# {} ASSERTED, {} ATTRIBUTED across {} shelf files'.format(
        len(asserted), len(attributed), len(SHELVES)))
    for h in hits:
        print('{}\t{}\t{}:{}\t{}'.format(h['verdict'], h['subject'], h['file'], h['line'], h['text'][:120]))
    subjects = {h['subject'] for h in asserted}
    other = {s for s in subjects if not s.startswith('EU AI Act')}
    print('\nACTION SA: {} OTHER subject(s) re-asserted -> LIMB {}'.format(
        len(other), 1 if len(other) >= 2 else 2))
    sys.exit(rc)
