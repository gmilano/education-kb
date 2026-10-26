import os,re,sys,json
ROOT=sys.argv[1]
WRITE=('create','update','post','submit','delete','remove','upload','publish','enroll','unenroll','grade','set_','set-','add','edit','send','reply','write','put','patch','assign','import','restore','conclude','toggle','bulk_update','bulk-update','copy','revert','apply','attach')
READ=('get','list','read','search','fetch','show','find','view','query','describe','analyz','summar','export','download','check','count','compare','discover','health','my_','explain','audit','resolve','project','next','browse','sync','status','login')
# py: @mcp.tool  with or without (...)  then def NAME
py_dec=re.compile(r'@(?:mcp|server|app)\.tool(?:\([^)]*\))?\s*(?:\r?\n\s*)*(?:async\s+)?def\s+([a-zA-Z_][a-zA-Z0-9_]*)')
py_named=re.compile(r'@(?:mcp|server|app)\.tool\(\s*name\s*=\s*["\']([^"\']+)["\']')
# ts/js/go: a tool object literal's name field, or server.tool("x")
nm=re.compile(r'''\bname:\s*['"]([a-z][a-zA-Z0-9_\-]{2,})['"]''')
srv=re.compile(r'''(?:server|mcp)\.(?:tool|registerTool)\(\s*['"]([a-zA-Z0-9_\-]+)['"]''')
go_nm=re.compile(r'''mcp\.NewTool\(\s*['"]([a-zA-Z0-9_\-]+)['"]|Name:\s*['"]([a-z][a-zA-Z0-9_\-]{2,})['"]''')
SKIPDIR={'node_modules','.git','dist','build','venv','.venv','tests','test','__tests__','examples','docs'}
out={}
for d in sorted(os.listdir(ROOT)):
    p=os.path.join(ROOT,d)
    if not os.path.isdir(p): continue
    names=set(); langs=set()
    for dp,dn,fn in os.walk(p):
        dn[:]=[x for x in dn if x not in SKIPDIR]
        for f in fn:
            ext=os.path.splitext(f)[1]
            if ext not in ('.py','.ts','.js','.mjs','.go'): continue
            if '.test.' in f or '.spec.' in f: continue
            try: t=open(os.path.join(dp,f),encoding='utf-8',errors='ignore').read()
            except Exception: continue
            langs.add(ext)
            if ext=='.py':
                names.update(py_dec.findall(t)); names.update(py_named.findall(t))
            elif ext=='.go':
                for a,b in go_nm.findall(t): names.add(a or b)
            else:
                names.update(nm.findall(t)); names.update(srv.findall(t))
    names={n for n in names if n and not n.endswith('_id') and n not in ('noop','divergent_tool','brand_new_tool')}
    def cls(n):
        s=n.lower().lstrip('_')
        for w in WRITE:
            if s.startswith(w): return 'WRITE'
        for w in READ:
            if s.startswith(w): return 'READ'
        return 'OTHER'
    c={'READ':[],'WRITE':[],'OTHER':[]}
    for n in sorted(names): c[cls(n)].append(n)
    out[d.replace('--','/')]={'cls':c,'langs':sorted(langs)}
tot={'READ':0,'WRITE':0,'OTHER':0}
print(f"{'project':<38} {'lang':<10} {'tools':>6} {'READ':>5} {'WRITE':>6} {'OTH':>4}  write%")
print('-'*86)
for k,v in out.items():
    c=v['cls']; n=sum(len(x) for x in c.values())
    for z in tot: tot[z]+=len(c[z])
    lg=','.join(x.lstrip('.') for x in v['langs']) or '-'
    w=f"{100*len(c['WRITE'])/n:>5.1f}%" if n else "   n/a"
    print(f"{k:<38} {lg:<10} {n:>6} {len(c['READ']):>5} {len(c['WRITE']):>6} {len(c['OTHER']):>4}  {w}")
N=sum(tot.values())
print('-'*86)
print(f"{'TOTAL':<38} {'':<10} {N:>6} {tot['READ']:>5} {tot['WRITE']:>6} {tot['OTHER']:>4}  {100*tot['WRITE']/N:>5.1f}%")
print()
print("AUTHOR-AND-PUBLISH tools (the capability p447 said no community server has):")
KEY=('create_course','create-course','create_module','create-module','create_page','create-page','post-announcement','post_announcement','toggle-module-publish','update-syllabus','publish')
for k,v in out.items():
    hit=[n for n in v['cls']['WRITE']+v['cls']['OTHER'] if any(x in n for x in KEY)]
    if hit: print(f"  🟢 {k}: {', '.join(sorted(hit))}")
json.dump(out,open(ROOT+'/../census2.json','w'))
