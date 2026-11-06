#!/usr/bin/env python3
"""Count rows of the FIRST (main sell) table only: the contiguous block of pipe
lines that follows the first header+separator pair."""
import re, sys
SEP = re.compile(r'^\|[\s:\-\|]+\|?$')
for path in sys.argv[1:]:
    lines=[l.rstrip("\n") for l in open(path, errors="replace")]
    i=0; n=len(lines); start=None
    while i < n-1:
        if lines[i].strip().startswith("|") and SEP.match(lines[i+1].strip()):
            start=i+2; break
        i+=1
    if start is None:
        print(path, "NO TABLE"); continue
    rows=[]
    j=start
    while j < n and lines[j].strip().startswith("|"):
        s=lines[j].strip()
        if not SEP.match(s):
            rows.append([c.strip() for c in s.strip("|").split("|")])
        j+=1
    print("=== %s : main table = %d rows (starts line %d, ends line %d)" % (path.split('/')[-1], len(rows), start+1, j))
    # region column distribution if present
    hdr=[c.strip().lower() for c in lines[start-2].strip().strip("|").split("|")]
    if "region" in hdr:
        ri=hdr.index("region")
        from collections import Counter
        c=Counter(re.sub(r"[^A-Za-z ().]","",r[ri]).strip() if len(r)>ri else "MISSING" for r in rows)
        print("    Region column:", dict(c))
    print("    header:", hdr)
