#!/usr/bin/env python3
import re, sys
PLACEHOLDER = {"name","nombre","repo","repository","licence","license","platform","project",
               "agent","tool","id","pattern","#","","what","layer","row","candidate","address"}
SEP = re.compile(r'^\|[\s:\-\|]+\|?$')
for path in sys.argv[1:]:
    data=[]; hdr=0; sep=0
    for ln in open(path, errors="replace"):
        s=ln.strip()
        if not s.startswith("|"): continue
        if SEP.match(s): sep+=1; continue
        cells=[c.strip() for c in s.strip("|").split("|")]
        first=re.sub(r"[^a-z0-9]","",cells[0].lower())
        if first in PLACEHOLDER: hdr+=1; continue
        data.append(cells[0])
    print("%-20s pipe_data_rows=%-5d header_rows=%-3d separators=%-3d" % (path.split('/')[-1], len(data), hdr, sep))
