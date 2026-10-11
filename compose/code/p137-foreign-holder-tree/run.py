#!/usr/bin/env python3
"""p137-foreign-holder-tree, step 2: read the payloads probe.sh found, publish the verdicts.

    python3 -I run.py trees.tsv result.tsv

Payloads come from `raw.githubusercontent.com/<slug>/HEAD/<path>` -- the one
GitHub channel that answers in this environment (`api.github.com` is 403 and
`curl -I` on github.com HTML is 403 even for repositories that clone fine).
"""
import csv
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from foreign_holder import holder_of, family_of, licence_paths, repo_verdict  # noqa: E402

# The repository's own identities, for the foreign-holder test. Owner slug alone
# is not enough: `sakaiproject` ships Apereo notices, `OpenOLAT` ships frentix's.
OWN = {
    'openedx': ['openedx', 'open edx', 'edx', 'axim'],
    'instructure': ['instructure', 'canvas'],
    'bigbluebutton': ['bigbluebutton', 'blindside'],
    'sakaiproject': ['sakai', 'apereo'],
    'learningequality': ['learning equality', 'learningequality'],
    'overhangio': ['overhang'],
    'openeducat': ['openeducat', 'tech receptives'],
    'adaptlearning': ['adapt'],
    'ILIAS-eLearning': ['ilias'],
    'OpenOLAT': ['openolat', 'frentix', 'olat', 'zurich'],
    'academico-sis': ['academico'],
    'Crosstalk-Solutions': ['crosstalk'],
}


def fetch(slug, path):
    url = f'https://raw.githubusercontent.com/{slug}/HEAD/{path}'
    p = subprocess.run(['curl', '-sSL', '--max-time', '25', '-w', '\n%{http_code}', url],
                       capture_output=True)
    text = p.stdout.decode('utf-8', 'replace')
    body, _, code = text.rpartition('\n')
    return body, code.strip()


def main(trees_tsv, out_tsv):
    rows = list(csv.reader(open(trees_tsv), delimiter='\t'))[1:]
    with open(out_tsv, 'w', newline='') as fh:
        w = csv.writer(fh, delimiter='\t')
        w.writerow(['slug', 'tree_paths', 'root_licence', 'nonroot_licence_shaped',
                    'nonroot_grants', 'foreign_holders', 'verdict', 'foreign_sample'])
        n_probed = n_foreign = 0
        for row in rows:
            if len(row) < 3 or row[1] == 'CLONE_FAIL':
                continue
            slug, npaths, lic = row[0], row[1], row[2]
            paths = [p for p in lic.split(';') if p]
            own = OWN.get(slug.split('/')[0], [slug.split('/')[0]])
            _root, non_root = licence_paths(paths)
            payloads = [(p, '') for p in paths if p not in non_root]
            for p in non_root:
                body, code = fetch(slug, p)
                payloads.append((p, body if code == '200' else ''))
            v = repo_verdict(slug, payloads, own)
            n_probed += 1
            if v['foreign']:
                n_foreign += 1
            sample = ' | '.join(f'{p}=>{h} [{f}]' for p, h, f in v['foreign'][:3])
            w.writerow([slug, npaths, v['root_licence'], v['nonroot_licence_shaped'],
                        v['nonroot_grants'], len(v['foreign']), v['verdict'], sample])
        w.writerow([f'# probed={n_probed} with_foreign_holder={n_foreign} '
                    f'share={n_foreign / n_probed:.2%}' if n_probed else '# probed=0'])
        print(f'probed={n_probed} with_foreign_holder={n_foreign} '
              f'({n_foreign / n_probed:.0%})' if n_probed else 'probed=0')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
