#!/usr/bin/env python3
"""p737 licence gate = p736 gate + GPL/LGPL VERSION RESOLUTION.
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
if __name__=='__main__':
    for p in sys.argv[1:]:
        t=open(p,encoding='utf-8',errors='replace').read()
        print(f"{classify(t):<34} {os.path.getsize(p):>6} B  {os.path.basename(p)}")
