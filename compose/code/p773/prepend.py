#!/usr/bin/env python3
"""Insert a new pass section directly AFTER the YAML frontmatter, refresh
`updated:`, and leave everything below untouched (append-only discipline)."""
import sys,re
target,section,date=sys.argv[1],sys.argv[2],sys.argv[3]
body=open(target,encoding="utf-8").read()
new=open(section,encoding="utf-8").read().rstrip()+"\n\n"
m=re.match(r"^---\n(.*?)\n---\n",body,re.S)
if not m:
    raise SystemExit(f"{target}: no YAML frontmatter -- refusing to write")
fm=m.group(1)
if re.search(r"^updated:",fm,re.M):
    fm=re.sub(r"^updated:.*$","updated: "+date,fm,flags=re.M)
else:
    fm+="\nupdated: "+date
rest=body[m.end():]
open(target,"w",encoding="utf-8").write("---\n"+fm+"\n---\n\n"+new+rest.lstrip("\n"))
print("prepended ->",target)
