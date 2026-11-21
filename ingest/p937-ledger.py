#!/usr/bin/env python3
"""p937 — slug-keyed licence ledger for the three published shelves.

WHY THIS EXISTS (937-F1): evidence/shelf-depth-audit.2026-11-19-p930.tsv keys each
row on (file, line). Any pass that inserts a row above shifts every line below it,
so that pairing rots silently. That audit reproduces 100% against the p928 shelf
and 41.4% against HEAD -- it was already 56.5% mispaired when it was committed,
because p929 was adding rows concurrently.

A slug is stable under insertion. This script keys on the slug and is therefore
merge-proof. Re-run it after any shelf edit; the output should change only where
a licence cell changed.

937-F6 WARNING: do NOT compute a licence census from the `cell` column. These
cells are argumentative prose -- they state the verdict AND discuss the SPDX
false negative, the stub file, or what an earlier pass got wrong. A classifier
cannot separate the verdict from the caveat beside it and mis-scores in BOTH
directions (validated 10/14 against hand byte-reads). Use the `spdx` column of
evidence/licence-ledger-structured.*.tsv, which is populated only where a pass
actually byte-read the grant, and is empty otherwise.

Usage:  python3 -I ingest/p937-ledger.py [--gaps]
"""
import re, sys, json, csv

FILES = ['agents/top.md', 'repos/foundations.md', 'verticals/solutions.md']
SLUG = re.compile(r'github\.com/([A-Za-z0-9._-]+/[A-Za-z0-9._-]+?)(?=[\s)>`|,]|/|$)')
# A licence-bearing column header. 'grant' is included because several shelf
# tables head the column "Grant read" rather than "Licence" -- missing those was
# one of the four census validation failures recorded in 937-F6.
HDR = re.compile(r'licen[cs]e|licence|\bgrant\b', re.I)


def parse(path):
    """Yield (slug, line_no, licence_cell) for each licence-bearing table row."""
    idxs = None
    for i, raw in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        st = raw.strip()
        if not st.startswith('|'):
            if st == '':
                idxs = None          # a blank line ends a table
            continue
        cells = [c.strip() for c in st.strip('|').split('|')]
        if cells and all(re.fullmatch(r'[-: ]*', c) for c in cells):
            continue                 # the |---|---| separator row
        hits = [j for j, c in enumerate(cells) if HDR.search(c)]
        if hits and not SLUG.search(st):
            idxs = hits              # header row: remember the licence columns
            continue
        if not idxs:
            continue
        m = SLUG.search(st)
        if not m:
            continue
        got = [cells[j] for j in idxs if j < len(cells)]
        got = [c for c in got if re.sub(r'[^A-Za-z0-9]', '', c)]
        if got:
            yield m.group(1).rstrip('.'), i, ' / '.join(got)


def main():
    ledger = {}
    for f in FILES:
        for slug, line, cell in parse(f):
            ledger.setdefault(slug, []).append({'file': f, 'line': line, 'cell': cell})

    rows = sum(len(v) for v in ledger.values())
    print(f'licence-bearing rows : {rows}')
    print(f'unique repositories  : {len(ledger)}')

    # The only mechanical check that is safe over prose: is the cell empty, or a
    # bare SPDX non-answer? Anything else needs a human or a byte-read.
    gaps = [(r['file'], r['line'], s, r['cell'])
            for s, rs in ledger.items() for r in rs
            if re.sub(r'[^A-Za-z0-9]', '', r['cell']).upper()
            in ('', 'NOASSERTION', 'NONE', 'NA', 'UNKNOWN', 'TBD')]
    print(f'blank / bare-token   : {len(gaps)}')
    for f, l, s, c in sorted(gaps):
        print(f'    {f}:{l} {s} -> {c!r}')

    if '--gaps' not in sys.argv:
        with open('evidence/licence-ledger.generated.tsv', 'w', newline='') as fh:
            w = csv.writer(fh, delimiter='\t')
            w.writerow(['slug', 'rows', 'files', 'cell_excerpt'])
            for s in sorted(ledger):
                rs = ledger[s]
                w.writerow([s, len(rs), ','.join(sorted({r['file'] for r in rs})),
                            re.sub(r'\s+', ' ', rs[0]['cell'])[:140]])
        print('wrote evidence/licence-ledger.generated.tsv')
    return 0


if __name__ == '__main__':
    sys.exit(main())
