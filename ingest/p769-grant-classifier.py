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

POINTER_MAX = 400   # a pointer is small; a grant payload is not

def classify_pointer(raw, t):
    """p769 D4: a grant PATH may hold a POINTER rather than a payload. Three forms beyond
    p768's DEP-5: the CRAN field stub (eplusr LICENSE, 64 B: YEAR/COPYRIGHT HOLDER only, with
    the text named in DESCRIPTION), the Sphinx include (SEED docs/source/license.rst, 69 B),
    and the bare path reference. A pointer carries NO grant and must never be graded."""
    tl = t.lower()
    if len(raw) > POINTER_MAX:
        return None
    if re.search(r'^\s*year\s*:', tl, re.M) and 'copyright holder' in tl \
       and 'permission' not in tl:
        return ['byref:CRAN-field-stub']
    if '.. include::' in tl:
        return ['byref:sphinx-include']
    if re.search(r'see\s+(the\s+)?(file\s+)?licen[sc]e', tl) and 'permission' not in tl:
        return ['byref:path-reference']
    return None

def classify(b):
    t = norm(b); tl = t.lower(); hits = []
    ptr = classify_pointer(b, t)
    if ptr: return ptr
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
    # p769 D1: a GNU title only counts as the GRANT if it sits in the payload's opening
    # region. MPL-2.0's own Exhibit B names the GNU GPL ("Secondary License"), so an
    # offset-anywhere find() grades a clean 16,725 B MPL payload as GPL-3.0. Generalises
    # p768's D1 from GPL-vs-LGPL to "a non-GNU licence that merely mentions the GPL".
    GNU_TITLE_WINDOW = 600
    def _gnu_at(needle):
        i = tl.find(needle)
        return i if 0 <= i < GNU_TITLE_WINDOW else -1
    gnu = {'AGPL': _gnu_at('gnu affero general public license'),
           'LGPL': _gnu_at('gnu lesser general public license'),
           'LGPL_OLD': _gnu_at('gnu library general public license'),
           'GPL': _gnu_at('gnu general public license')}
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
    # p769 D2: Mulan Permissive Software License v2 -- OSI-approved, permissive, with a
    # patent grant and patent-retaliation clause. Bilingual payload (Chinese + English).
    if ('mulan permissive software license' in tl or '木兰宽松许可证' in t):
        hits.append('MulanPSL-2.0' if ('version 2' in tl or '第2版' in t) else 'MulanPSL')
    # p769 D3: ZT PUBLIC LICENSE -- a VENDOR-AUTHORED licence, not an OSI family. Permits
    # commercial sale of derivatives (6.2.4) yet forbids removing or obscuring the vendor's
    # logo, copyright and brand strings FROM THE RUNNING UI (2.4, 6.2.2). A detector that
    # answers permissive/copyleft/noncommercial gets this wrong toward PERMISSION.
    if 'zt public license' in tl or 'ZT PUBLIC LICENSE' in t:
        hits.append('ZTPL-1.0/BRAND-LOCK')
    # p769 D7: Zlib/libpng. Clean, permissive, no name in the text at all -- so a
    # family-name matcher cannot see it. glfw ships it inside EnergyPlus's third_party tree.
    if "provided 'as-is', without any express or implied warranty" in tl \
       and 'altered source versions must be plainly marked' in tl:
        hits.append('Zlib')
    # p769 D8: an UNFILLED TEMPLATE is not a grant. OpenStudio carries three LICENSE.md files
    # whose entire content is the instruction "Insert your license here" (24 B, 0d980364ebe9).
    # A probe that asks "does a LICENSE path exist?" counts these as licensed. Stronger cousin
    # of p768-B: there the canonical text carried no OWNERSHIP; here it carries no GRANT.
    if tl.strip() in ('insert your license here', 'insert your licence here') \
       or tl.strip().startswith('insert your licen'):
        return ['template:UNFILLED']
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
    if 'all rights reserved' in tl and not hits:
        # p769 D5: distinguish a copyright NOTICE from a proprietary GRANT. A notice asserts
        # ownership and grants nothing; it is not a refusal. LBNL-ETA/EnergyPlus-MCP ships
        # Copyright.txt (903 B, "All rights reserved" + a US Government licence-back) beside
        # License.txt (2,474 B, modified BSD-3). Grading the notice refuses a usable agent.
        grantish = any(k in tl for k in (
            'permission is hereby granted', 'redistribution and use', 'you may not use',
            'licensed under', 'is hereby granted', 'subject to the terms'))
        if grantish:
            hits.append('PROPRIETARY/ARR')
        else:
            hits.append('notice:COPYRIGHT-ONLY')
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
