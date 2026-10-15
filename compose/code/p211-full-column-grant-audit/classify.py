#!/usr/bin/env python3
"""Classify licence blobs into families.

Order matters, and it is the order two earlier passes of this KB paid for:

  1. RIDERS FIRST (p207/T-PP). A rider such as the Commons Clause AMENDS the
     licence below it. A title walk finds the inner licence and misses the
     rider, returning a clean permissive answer on a source-available grant.
  2. TITLE-LINE ANCHORED (p205/Gap 466). GPL-3.0, MPL-2.0 and ECL-2.0 quote
     the AGPL and Apache inside their own body, so a whole-body matcher
     misclassifies them. Only the leading non-empty lines decide the family.
  3. STATED vs BODIED (p210). A one-line "License: GNU GPL V3" names a family
     without shipping its body. That is recorded as a distinct state, not as
     a clean grant.
"""
import os
import re
import sys
import json

RIDERS = [
    (r'commons\s+clause', 'Commons-Clause-RIDER'),
    (r'\bthe\s+software\s+is\s+provided\s+to\s+you\s+by\s+the\s+licensor.{0,200}'
     r'without\s+the\s+right\s+to\s+sell', 'sell-restriction-RIDER'),
    (r'\bnon[- ]?commercial\s+use\s+only\b', 'noncommercial-RIDER'),
]

# (pattern, family). Matched against the TITLE WINDOW only.
TITLE_RULES = [
    (r'GNU\s+AFFERO\s+GENERAL\s+PUBLIC\s+LICENSE', 'AGPL-3.0'),
    (r'GNU\s+LESSER\s+GENERAL\s+PUBLIC\s+LICENSE', 'LGPL'),
    (r'GNU\s+GENERAL\s+PUBLIC\s+LICENSE', 'GPL'),
    (r'\bApache\s+License\b', 'Apache-2.0'),
    (r'Educational\s+Community\s+License', 'ECL-2.0'),
    (r'Mozilla\s+Public\s+License', 'MPL-2.0'),
    (r'Eclipse\s+Public\s+License', 'EPL'),
    (r'\bMIT\s+License\b', 'MIT'),
    (r'Permission\s+is\s+hereby\s+granted,\s+free\s+of\s+charge', 'MIT'),
    (r'BSD\s+3-Clause', 'BSD-3-Clause'),
    (r'BSD\s+2-Clause', 'BSD-2-Clause'),
    (r'Redistribution\s+and\s+use\s+in\s+source\s+and\s+binary\s+forms',
     'BSD-family'),
    # CC: most-restrictive spelling first, and the bare "Attribution N.0
    # International" title form -- the deed/legalcode opens with that line and
    # only names "Creative Commons" further down, so a rule keyed on the words
    # "Creative Commons Attribution" misses the whole family.
    (r'Attribution[- ]Non[Cc]ommercial[- ]Share\s?Alike', 'CC-BY-NC-SA'),
    (r'Attribution[- ]Share\s?Alike', 'CC-BY-SA'),
    (r'Attribution[- ]Non[Cc]ommercial', 'CC-BY-NC'),
    (r'Creative\s+Commons\s+Attribution[- ]ShareAlike', 'CC-BY-SA'),
    (r'Creative\s+Commons\s+Attribution[- ]Non[Cc]ommercial', 'CC-BY-NC'),
    (r'^\s*Attribution\s+\d\.\d\s+International', 'CC-BY'),
    (r'Creative\s+Commons\s+Attribution', 'CC-BY'),
    (r'CC0\s+1\.0|Creative\s+Commons\s+Zero', 'CC0-1.0'),
    (r'\bThe\s+Unlicense\b|This\s+is\s+free\s+and\s+unencumbered\s+software',
     'Unlicense'),
    (r'ISC\s+License', 'ISC'),
    (r'Elastic\s+License', 'Elastic-2.0'),
    (r'Business\s+Source\s+License', 'BSL-1.1'),
    (r'zlib\s+License', 'Zlib'),
    (r'Open\s+Software\s+License', 'OSL-3.0'),
    (r'Academic\s+Free\s+License', 'AFL-3.0'),
]

VERSION_HINTS = [
    (r'Version\s+3', '3.0'), (r'\bv?3\.0\b', '3.0'),
    (r'Version\s+2\.1', '2.1'),
    (r'Version\s+2\.0', '2.0'), (r'\bv?2\.0\b', '2.0'),
    (r'Version\s+2\b', '2.0'),
    (r'\b4\.0\b', '4.0'),
]


def classify(body):
    text = body.replace('\r\n', '\n')
    low = text.lower()

    riders = [name for pat, name in RIDERS if re.search(pat, low, re.I | re.S)]

    lines = [ln.strip() for ln in text.split('\n')]
    nonempty = [ln for ln in lines if ln]

    # STATED-not-BODIED: very short blob that names a family.
    bodied = len(text.strip()) >= 400

    # Title window: first 12 non-empty lines, plus the first 600 chars as a
    # fallback for blobs that open with a copyright block.
    window = '\n'.join(nonempty[:12])
    fam = None
    for pat, name in TITLE_RULES:
        if re.search(pat, window, re.I):
            fam = name
            break
    if fam is None:
        head = text[:600]
        for pat, name in TITLE_RULES:
            if re.search(pat, head, re.I):
                fam = name
                break
    if fam is None:
        for pat, name in TITLE_RULES:
            if re.search(pat, text, re.I):
                fam = name + '-BODYONLY'
                break

    # STATED-not-BODIED (p210): a short blob that NAMES a family without
    # shipping its text. Recorded as its own state -- naming a licence is not
    # granting one, and the diligence consequence differs.
    if fam is None and not bodied:
        m = re.search(r'\b(AGPL|LGPL|GPL|Apache|MIT|BSD|MPL|ECL)\b[^\n]{0,40}',
                      text, re.I)
        if m:
            tok = m.group(1).upper()
            v = '3.0' if re.search(r'\b(v?3|three)\b', m.group(0), re.I) else ''
            base = {'AGPL': 'AGPL', 'LGPL': 'LGPL', 'GPL': 'GPL',
                    'APACHE': 'Apache', 'MIT': 'MIT', 'BSD': 'BSD',
                    'MPL': 'MPL', 'ECL': 'ECL'}[tok]
            fam = (base + ('-' + v if v else '')) + '-STATED'

    ver = ''
    if fam in ('GPL', 'LGPL', 'EPL', 'CC-BY', 'CC-BY-SA', 'CC-BY-NC'):
        for pat, v in VERSION_HINTS:
            if re.search(pat, window, re.I):
                ver = v
                break
        if fam == 'GPL':
            fam = 'GPL-3.0' if ver == '3.0' else ('GPL-2.0' if ver == '2.0' else 'GPL')
        elif fam == 'LGPL':
            fam = 'LGPL-3.0' if ver == '3.0' else ('LGPL-2.1' if ver == '2.1' else 'LGPL')
        elif fam == 'EPL':
            fam = 'EPL-2.0' if ver == '2.0' else 'EPL'
        elif fam.startswith('CC-BY'):
            fam = fam + ('-4.0' if ver == '4.0' else '')

    return {
        'family': fam or 'UNRECOGNISED',
        'riders': riders,
        'bodied': bodied,
        'bytes': len(body.encode('utf-8')),
        'lines': len(lines),
    }


if __name__ == '__main__':
    blobdir, results_tsv = sys.argv[1], sys.argv[2]
    out = {}
    with open(results_tsv, encoding='utf-8') as fh:
        for line in fh:
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 5:
                continue
            repo, form, code = parts[0], parts[1], parts[2]
            if form == 'ABSENT':
                out[repo] = {'family': 'ABSENT', 'riders': [], 'bodied': False,
                             'bytes': 0, 'lines': 0, 'path_form': 'ABSENT'}
                continue
            safe = repo.replace('/', '_')
            p = os.path.join(blobdir, safe + '.blob')
            if not os.path.exists(p):
                out[repo] = {'family': 'NOBLOB', 'riders': [], 'bodied': False,
                             'bytes': 0, 'lines': 0, 'path_form': form}
                continue
            with open(p, encoding='utf-8', errors='replace') as bh:
                rec = classify(bh.read())
            rec['path_form'] = form
            out[repo] = rec
    json.dump(out, sys.stdout, indent=1)
