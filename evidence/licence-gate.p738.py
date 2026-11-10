#!/usr/bin/env python3
"""p738 licence gate = p737 gate + CC0 RESOLUTION + a 14-name filename chain.

p738 repairs two defects, both measured (evidence/gate-controls.2026-11-10-p738.tsv):

 1. CC0-1.0 was classified 'CC-BY-family (not a software grant)', 3/3, because the
    generic 'Creative Commons' rule fired first. CC0 is a public-domain dedication:
    it carries NO attribution obligation and is strictly MORE permissive than CC-BY,
    so the old verdict understated the grant and pushed usable material into the
    cannot-use bucket. Fix: match 'CC0 1.0 Universal' ABOVE the generic rule, and
    treat the bare preamble line 'Creative Commons Legal Code' as decoration so it
    cannot terminate the walk (two of the three payloads carry that preamble and
    one does not, so the rule must survive both layouts).

 2. The six-name filename chain produced 'no grant found at probed paths' for two
    repositories that DO carry a grant: iansan5653/open-mcr at lowercase
    'license.txt' and kiwix/kiwix-js at 'LICENSE-GPLv3.txt'. The raw probe is
    case-sensitive (724-I), so lowercase variants are load-bearing. Chain: 6 -> 14.

 3. Not a code change but a procedure change (T331): a licence found ONLY in a
    manifest must be corroborated against the README licence section before it is
    recorded. cast-org/clusive declares "license": "ISC" in package.json -- which
    is npm init's DEFAULT value -- while its README section says BSD-3-Clause.
    T312 said "read the manifest"; p738 adds "and do not trust it alone".

Original p737 docstring follows.
p737 licence gate = p736 gate + GPL/LGPL VERSION RESOLUTION.
p736 returned bare 'GPL' / 'LGPL', discarding the version. GPL-2.0 and GPL-3.0
differ in patent and compatibility terms, so a bare family is not a usable verdict.
p737 resolves the version from the version line that FOLLOWS the family line
(never from the file size, and never from a whole-payload match: GPL-3.0 sec.13
names the AGPL, which is the p736/T311 trap this gate must keep passing).

Original p736 docstring follows.
p736 licence gate: classify by FAMILY-NAME LINE, then operative clause.
Rule: scan lines; skip decoration (pure punctuation, YAML keys, 'Copyright' lines).
The family is decided by the FIRST line that names a licence family. Only if no
line names a family do we fall back to the operative clause. Never substring-match
a family name across the whole payload: GPL-3.0 sec.13 names the AGPL."""
import re,sys,os
FAMILY_LINE=[(r'GNU AFFERO GENERAL PUBLIC LICEN[SC]E','AGPL-3.0'),
 (r'GNU LESSER GENERAL PUBLIC LICEN[SC]E','LGPL'),
 (r'GNU GENERAL PUBLIC LICEN[SC]E','GPL'),
 (r'\bApache Licen[sc]e\b','Apache-2.0'),
 (r'Educational Community Licen[sc]e','ECL-2.0'),
 (r'CERN Open Hardware Licen[sc]e.*Permissive','CERN-OHL-P-2.0'),
 (r'CERN Open Hardware Licen[sc]e','CERN-OHL'),
 (r'Mozilla Public Licen[sc]e','MPL-2.0'),
 (r'MIT Licen[sc]e','MIT'),
 (r'CC0 1\.0 Universal','CC0-1.0'),
 (r'Creative Commons Attribution-NonCommercial','CC-BY-NC (NOT usable)'),
 (r'Creative Commons','CC-BY-family (not a software grant)'),
 (r'\bBSD\b','BSD-unspecified')]
CLAUSE=[(r'Permission is hereby granted, free of charge','MIT'),
 (r'Licensed to .{0,40} under the Apache Licen[sc]e','Apache-2.0'),
 (r'Apereo licenses this file to you under the Apache Licen[sc]e','Apache-2.0'),
 (r'Redistribution and use in source and binary forms','BSD')]
def decoration(l):
    s=l.strip()
    if not s: return True
    if re.fullmatch(r'[\-=_*#~`<>/\\|.,:;\[\]{}()\'"+ ]+',s): return True
    if s.lower().startswith('copyright'): return True
    if re.fullmatch(r'(title|category|order|isWIP|SPDX-License-Identifier)\s*:.*',s,re.I): return True
    if re.fullmatch(r'Creative Commons Legal Code',s,re.I): return True  # p738: preamble, names no family
    return False
def _ver(lines,famline,fam):
    # Resolve the version from the version line that follows the family line.
    i=lines.index(famline)
    for l in lines[i:i+6]:
        m=re.search(r'Version\s+([0-9]+)(?:\.([0-9]+))?',l,re.I)
        if m:
            return m.group(1)+'.'+(m.group(2) or '0')
    return 'unversioned'

def classify(text):
    lines=text.splitlines()
    for l in lines:
        if decoration(l): continue
        for pat,fam in FAMILY_LINE:
            if re.search(pat,l,re.I):
                if fam=='BSD-unspecified' and 'Redistribution and use' not in text: continue
                if fam.startswith('BSD'):
                    return 'BSD-3-Clause' if re.search(r'Neither the name',text,re.I) else 'BSD-2-Clause'
                if fam in ('GPL','LGPL','AGPL-3.0'):
                    return fam if fam.endswith('3.0') else fam+'-'+_ver(lines,l,fam)
                return fam
    for pat,fam in CLAUSE:
        if re.search(pat,text,re.I):
            if fam=='BSD':
                return 'BSD-3-Clause' if re.search(r'Neither the name',text,re.I) else 'BSD-2-Clause'
            return fam
    return 'UNCLASSIFIED'
# p738: the probe chain, in order. The raw channel is case-sensitive, so the
# lowercase variants are not redundant -- each recovered a real grant this pass.
CHAIN=['LICENSE','LICENSE.md','LICENSE.txt','COPYING','LICENCE','License',
 'LICENSE-MIT','LICENSE-APACHE','LICENSE-GPLv3.txt','license','license.txt',
 'licence','LICENSE.rst','COPYING.md']

if __name__=='__main__':
    for p in sys.argv[1:]:
        t=open(p,encoding='utf-8',errors='replace').read()
        print(f"{classify(t):<34} {os.path.getsize(p):>6} B  {os.path.basename(p)}")
