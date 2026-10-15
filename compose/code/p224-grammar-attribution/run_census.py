"""Run ACTION RU's census over the 8 live shelf files and emit the grammar column.

The grammar map is READ FROM EVIDENCE ON DISK, not hardcoded: p222's `rs-cran-grammar`
TSV says which rows were answered from a CRAN `DESCRIPTION`, and p222's `rp-bound-sweep`
TSV already carries a grammar column for the rows it swept. The one row p222 read from an
Odoo `__manifest__.py` is named in its README and is listed here with that provenance.

Two populations are reported, because ACTION RU's falsifier says "a row whose grant was
READ from" such a file, and that is narrower than "a row in that ecosystem":

  STRICT  the grant was actually read first-hand from a CRAN DESCRIPTION or an Odoo
          __manifest__.py. This is the registered population and decides the limb.
  WIDE    the row sits in one of those ecosystems, so the omission grammar applies to it
          whether or not anyone has read its manifest yet. Reported as context only.
"""

import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grammar_attribution as g

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
EV = os.path.join(ROOT, 'evidence')

SHELVES = [
    'agents/top.md', 'agents/trending.md', 'repos/foundations.md', 'repos/trending.md',
    'verticals/solutions.md', 'intel/market.md', 'intel/trends.md', 'compose/patterns.md',
]


def build_grammar_map():
    """(map, provenance) - every entry traceable to a file on disk or a named p222 read."""
    gram, prov = {}, {}

    cran = os.path.join(EV, 'rs-cran-grammar.2026-10-15-p222.tsv')
    with open(cran, newline='') as fh:
        for row in csv.DictReader(fh, delimiter='\t'):
            if row.get('channel') == 'DESCRIPTION':
                slug = row['slug'].strip().lower()
                gram[slug] = 'cran'
                prov[slug] = 'rs-cran-grammar.2026-10-15-p222.tsv (DESCRIPTION read first-hand)'

    sweep = os.path.join(EV, 'rp-bound-sweep.2026-10-15-p222.tsv')
    with open(sweep, newline='') as fh:
        for row in csv.DictReader(fh, delimiter='\t'):
            slug = (row.get('slug') or '').strip().lower()
            grm = (row.get('grammar') or '').strip().lower()
            if slug and grm and slug not in gram:
                gram[slug] = grm
                prov[slug] = 'rp-bound-sweep.2026-10-15-p222.tsv (grammar column)'

    # p222's README: openeducat_core/__manifest__.py line 25 -> 'license': 'LGPL-3'
    gram['openeducat/openeducat_erp'] = 'odoo'
    prov['openeducat/openeducat_erp'] = 'p222 README: openeducat_core/__manifest__.py l.25'
    return gram, prov


# Rows in an omission-grammar ECOSYSTEM but whose manifest has not been read here.
WIDE_ONLY = {
    'openeducat/openeducat_lti': 'odoo',
    'openeducat-inc/openeducat': 'odoo',
    'odoo/odoo': 'odoo',
    'jayvora-serpentcs/odooeduerp': 'odoo',
}


def main():
    gram, prov = build_grammar_map()
    lines, per_file = [], {}
    for rel in SHELVES:
        with open(os.path.join(ROOT, rel), errors='replace') as fh:
            fl = fh.read().splitlines()
        per_file[rel] = len(fl)
        lines.extend(fl)

    strict = g.attribute(lines, gram)
    wide_map = dict(gram)
    wide_map.update(WIDE_ONLY)
    wide = g.attribute(lines, wide_map)

    v = g.verdict(strict)
    vw = g.verdict(wide)

    print('corpus: {} files, {} lines'.format(len(SHELVES), sum(per_file.values())))
    print('GNU mentions      : {}'.format(strict['gnu_mentions']))
    print('  bare            : {}'.format(strict['bare_mentions']))
    print('  qualified       : {}'.format(strict['qualified_mentions']))
    print('bare attributed   : {}'.format(strict['bare_attributed']))
    print('  ambiguous line  : {}'.format(strict['bare_ambiguous_line']))
    print('  no slug on line : {}'.format(strict['bare_no_slug_on_line']))
    print('by grammar (STRICT): {}'.format(
        dict(sorted(strict['by_grammar'].items(), key=lambda kv: -kv[1]))))
    print('by grammar (WIDE)  : {}'.format(
        dict(sorted(wide['by_grammar'].items(), key=lambda kv: -kv[1]))))
    print('')
    print('ACTION RU STRICT: omission-grammar bare mentions = {} (threshold {}) -> LIMB {}'
          .format(v['omission_grammar_bare_mentions'], v['threshold'], v['limb']))
    print('ACTION RU WIDE  : {} -> LIMB {}'
          .format(vw['omission_grammar_bare_mentions'], vw['limb']))
    print('means: {}'.format(v['means']))
    print('')
    print('--- top rows by bare mentions (grammar) ---')
    for slug, n in sorted(strict['by_row'].items(), key=lambda kv: -kv[1])[:15]:
        print('{:5d}  {:12s}  {}'.format(n, wide_map.get(slug, 'unread'), slug))

    out = os.path.join(EV, 'ru-grammar-census.2026-10-15-p224.tsv')
    with open(out, 'w', newline='') as fh:
        w = csv.writer(fh, delimiter='\t')
        w.writerow(['slug', 'bare_gnu_mentions', 'grammar', 'population', 'bound_reading',
                    'provenance'])
        for slug, n in sorted(strict['by_row'].items(), key=lambda kv: (-kv[1], kv[0])):
            grm = gram.get(slug) or WIDE_ONLY.get(slug) or 'unread'
            pop = 'STRICT' if slug in gram else ('WIDE' if slug in WIDE_ONLY else '-')
            reading = ('POSITIVE only (bound carried by omission)'
                       if grm in ('cran', 'odoo') else
                       'genuine silence' if grm == 'spdx' else 'unknown - channel unread')
            w.writerow([slug, n, grm, pop, reading, prov.get(slug, '')])
        w.writerow(['TOTAL-BARE-MENTIONS', strict['bare_mentions'], '-', '-', '-',
                    '{} files, {} lines'.format(len(SHELVES), sum(per_file.values()))])
        w.writerow(['TOTAL-ATTRIBUTED', strict['bare_attributed'], '-', '-', '-',
                    'single-slug lines only'])
        w.writerow(['AMBIGUOUS-LINE', strict['bare_ambiguous_line'], '-', '-', '-',
                    'line names 2+ rows - deliberately NOT attributed (p222 defect guard)'])
        w.writerow(['NO-SLUG-ON-LINE', strict['bare_no_slug_on_line'], '-', '-', '-',
                    'prose mention, no row on the line'])
        w.writerow(['VERDICT-STRICT', v['omission_grammar_bare_mentions'], '-',
                    'LIMB {}'.format(v['limb']), '-', 'threshold 50'])
        w.writerow(['VERDICT-WIDE', vw['omission_grammar_bare_mentions'], '-',
                    'LIMB {}'.format(vw['limb']), '-', 'ecosystem, not yet read'])
    print('\nwrote {}'.format(out))


if __name__ == '__main__':
    main()
