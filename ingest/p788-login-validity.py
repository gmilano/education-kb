#!/usr/bin/env python3
"""p788-A — the login-validity clause, run on the BASE-WIDE extraction.
Carried p785-B -> p786-B -> p787-A. An owner that is not a legal GitHub login
cannot be a repository address, so it is an extraction artefact, not a finding.
"""
import re,sys,os,collections
ADDR=re.compile(r'github\.com/([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+)')
LOGIN=re.compile(r'^[A-Za-z0-9]([A-Za-z0-9-]{0,37}[A-Za-z0-9])?$')
PATHWORDS={'archive','blob','releases','tree','raw','commit','commits','compare',
           'pull','issues','wiki','tags','branches','search','topics','orgs','apps',
           'sponsors','settings','login','about','features','pricing','security'}
ARCHEXT=('.tar','.gz','.zip','.tgz','.bz2','.xz','.7z','.rar')
rows=[]
for dirpath,dirnames,files in os.walk('.'):
    dirnames[:]=[d for d in dirnames if d not in ('.git',)]
    for fn in files:
        if not fn.endswith(('.md','.markdown')): continue
        p=os.path.join(dirpath,fn)
        try: txt=open(p,encoding='utf-8',errors='replace').read()
        except Exception: continue
        for i,line in enumerate(txt.splitlines(),1):
            for owner,repo in ADDR.findall(line):
                rows.append((owner,repo,p,i))
seen=set(); uniq=[]
for o,r,p,i in rows:
    k=(o,r)
    if k in seen: continue
    seen.add(k); uniq.append((o,r,p,i))
rej=collections.defaultdict(list)
for o,r,p,i in uniq:
    why=None
    if len(o)>39: why='owner>39chars'
    elif not LOGIN.match(o): why='owner-not-a-legal-login'
    elif o.lower() in PATHWORDS: why='owner-is-a-github-path-word'
    elif r.lower().endswith(ARCHEXT): why='repo-is-an-archive-artefact'
    elif r.lower() in PATHWORDS: why='repo-is-a-github-path-word'
    if why: rej[why].append((o,r,p,i))
print("base-wide extraction: %d address occurrences, %d distinct owner/repo pairs"%(len(rows),len(uniq)))
tot=sum(len(v) for v in rej.values())
print("REJECTED by the login-validity clause: %d of %d distinct (%.2f%%)"%(tot,len(uniq),100.0*tot/max(1,len(uniq))))
for why,items in sorted(rej.items(),key=lambda kv:-len(kv[1])):
    print("\n## %s — %d"%(why,len(items)))
    for o,r,p,i in items[:40]: print("   %s/%s    <- %s:%d"%(o,r,p,i))
    if len(items)>40: print("   ... %d more"%(len(items)-40))
