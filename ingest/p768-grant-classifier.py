#!/usr/bin/env python3
# p768 grant classifier. Closes ACTION p767-D (i) CC 3.0 + by-reference CC, (iii) ISC,
# and keeps p767's rule: classify on OPERATIVE CLAUSE TEXT, never the family's own name.
# Typography-insensitive (p767 T684): normalises curly quotes, (c)/copyright symbols, NBSP.
import sys, re, hashlib

def norm(b):
    try: t = b.decode('utf-8', 'replace')
    except Exception: t = str(b)
    t = t.replace('“','"').replace('”','"').replace('‘',"'").replace('’',"'")
    t = t.replace('©','(c)').replace(' ',' ').replace('–','-').replace('—','-')
    t = re.sub(r'\s+', ' ', t)
    return t

DEP5 = 'format: http://www.debian.org/doc/copyright-format' 
DEP5B = 'format: https://www.debian.org/doc/copyright-format'

def classify_dep5(raw):
    """Debian DEP-5 declares licences BY REFERENCE, per file-glob, with no operative text.
    p768 D2: this is not noise -- it is an upstream-published per-path licence map, which is
    exactly the multi-family/path-scoped structure ACTION p766-D asked for. Returns the
    declared SPDX-ish tokens, marked by-reference so a reader knows no clause text was read."""
    try: t = raw.decode('utf-8', 'replace')
    except Exception: return []
    out = []
    cur_files = '*'
    for line in t.splitlines():
        if line.lower().startswith('files:'):
            cur_files = line.split(':', 1)[1].strip() or '*'
        elif line.lower().startswith('license:'):
            lic = line.split(':', 1)[1].strip()
            if not lic: continue
            tok = 'byref:%s@%s' % (lic, cur_files)
            if tok not in out: out.append(tok)
    return out

def classify(b):
    t = norm(b); tl = t.lower(); hits = []
    if DEP5 in tl or DEP5B in tl:
        d = classify_dep5(b)
        if d: return d
    # --- operative clause discriminators (not family names) ---
    if 'permission is hereby granted, free of charge' in tl and 'without restriction' in tl \
       and 'sublicense' in tl:
        hits.append('MIT')
    if 'permission to use, copy, modify, and/or distribute this software for any purpose' in tl \
       and 'fee is hereby granted' in tl:
        hits.append('ISC')                                     # p767-D (iii)
    if 'licensed under the apache license, version 2.0' in tl or \
       ('apache license' in tl and 'version 2.0' in tl and 'appendix' in tl) or \
       'http://www.apache.org/licenses/license-2.0' in tl:
        hits.append('Apache-2.0')
    if 'redistribution and use in source and binary forms' in tl:
        # BSD text never contains the word "BSD" (p766 D3)
        if 'neither the name' in tl: hits.append('BSD-3-Clause')
        elif 'endorse or promote' in tl: hits.append('BSD-3-Clause')
        else: hits.append('BSD-2-Clause')
    # GNU family: the TITLE decides, not any mention. GPL-2.0's own preamble recommends
    # the LGPL ("use the GNU Lesser General Public License instead of this License"), so an
    # elif chain misreads every GPL-2.0 payload as LGPL. p768 D1, caught by the openSIS control.
    gnu = {'AGPL': tl.find('gnu affero general public license'),
           'LGPL': tl.find('gnu lesser general public license'),
           'LGPL_OLD': tl.find('gnu library general public license'),
           'GPL': tl.find('gnu general public license')}
    gnu = {k: v for k, v in gnu.items() if v >= 0}
    if gnu:
        fam = min(gnu, key=gnu.get)          # earliest offset == the title line
        off = gnu[fam]
        head = tl[off:off + 400]             # version belongs to the TITLE, not the document
        ver3 = 'version 3' in head
        ver2 = 'version 2' in head
        if fam == 'AGPL':
            hits.append('AGPL-3.0' if ver3 else 'AGPL-unversioned')
        elif fam in ('LGPL', 'LGPL_OLD'):
            if ver3: hits.append('LGPL-3.0')
            elif '2.1' in head: hits.append('LGPL-2.1')
            elif ver2: hits.append('LGPL-2.0')
            else: hits.append('LGPL-unversioned')
        else:
            if ver3: hits.append('GPL-3.0')
            elif ver2: hits.append('GPL-2.0')
            else: hits.append('GPL-unversioned')
    if 'mozilla public license' in tl: hits.append('MPL-2.0' if '2.0' in tl else 'MPL')
    # --- Creative Commons, incl. 3.0 and by-reference (p767-D (i)) ---
    cc_ver = None
    for v in ('4.0','3.0','2.5','2.0'):
        if f'creativecommons.org/licenses/' in tl and f'/{v}' in tl: cc_ver = v; break
        if f'version {v}' in tl and 'creative commons' in tl: cc_ver = v; break
    if 'creative commons' in tl or 'creativecommons.org' in tl:
        m = re.search(r'creativecommons\.org/licenses/([a-z\-]+)/(\d\.\d)', tl)
        if m:
            hits.append('CC-' + m.group(1).upper() + '-' + m.group(2))
        else:
            parts = []
            if 'attribution' in tl: parts.append('BY')
            if 'noncommercial' in tl or 'non-commercial' in tl: parts.append('NC')
            if 'sharealike' in tl or 'share alike' in tl: parts.append('SA')
            if 'noderiv' in tl or 'no derivative' in tl: parts.append('ND')
            if 'cc0' in tl or 'public domain dedication' in tl: hits.append('CC0-1.0')
            elif parts: hits.append('CC-' + '-'.join(parts) + ('-' + cc_ver if cc_ver else '-UNVERSIONED'))
    if 'unlicense' in tl and 'public domain' in tl: hits.append('Unlicense')
    # Source-available families. NOT open source; a client deliverable cannot be built on them.
    # p768 D3: the register's most-starred agentic repo carries PolyForm Noncommercial and the
    # index shows NOASSERTION -- the same value it shows for genuine Apache-2.0 and MIT.
    if 'polyform' in tl:
        if 'noncommercial' in tl: hits.append('PolyForm-Noncommercial-1.0.0')
        elif 'shield' in tl: hits.append('PolyForm-Shield-1.0.0')
        else: hits.append('PolyForm-OTHER')
    if 'business source license' in tl or 'busl' in tl: hits.append('BUSL-1.1')
    if 'server side public license' in tl: hits.append('SSPL')
    if 'elastic license' in tl: hits.append('Elastic-2.0')
    if 'commons clause' in tl: hits.append('Commons-Clause')
    if 'sustainable use license' in tl: hits.append('Sustainable-Use')
    # --- proprietary / all-rights-reserved refusals ---
    if 'all rights reserved' in tl and not hits: hits.append('PROPRIETARY/ARR')
    for p in ('no commercial use','not be used for commercial','prior written permission of the author',
              'no production use','may not be copied'):
        if p in tl and 'PROPRIETARY/ARR' not in hits: hits.append('PROPRIETARY/RESTRICTED')
    out = []
    for h in hits:
        if h not in out: out.append(h)
    return out or ['UNRECOGNISED']

if __name__ == '__main__':
    b = open(sys.argv[1],'rb').read()
    print('%d\t%s\t%s' % (len(b), hashlib.sha256(b).hexdigest()[:12], '+'.join(classify(b))))
