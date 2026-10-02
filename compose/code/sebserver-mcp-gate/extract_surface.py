#!/usr/bin/env python3
"""Pass 44, action 1: extract the WHOLE SEB Server REST surface from the tree.

Reads seb-server @ 7f45689 and emits operations.tsv / endpoints.tsv for the gate.
Corrects four defects of the pass-43 extraction, each documented in the README.
"""
import re, os
from collections import Counter
# usage: python3 extract_surface.py [path-to-seb-server-checkout] [out-dir]
# Reproduce the checkout with:
#   git clone --depth 1 --filter=blob:none --sparse https://github.com/SafeExamBrowser/seb-server seb
#   cd seb && git sparse-checkout set \
#       src/main/java/ch/ethz/seb/sebserver/webservice/weblayer/api \
#       src/main/java/ch/ethz/seb/sebserver/gbl/api src/main/resources
import sys
TREE=sys.argv[1] if len(sys.argv)>1 else os.environ.get("SEB_TREE","./seb")
ROOT=os.path.join(TREE,"src/main")
CDIR=os.path.join(ROOT,"java/ch/ethz/seb/sebserver/webservice/weblayer/api")
OUT=sys.argv[2] if len(sys.argv)>2 else os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT,exist_ok=True)

api=open(os.path.join(ROOT,"java/ch/ethz/seb/sebserver/gbl/api/API.java"),encoding='utf-8',errors='replace').read()
raw={m.group(1):re.sub(r'\s+',' ',m.group(2).strip())
     for m in re.finditer(r'String\s+([A-Z_0-9]+)\s*=\s*(.*?);',api,re.S)}

# Spring property defaults, read from the shipped resources (not guessed).
PROPS={"sebserver.webservice.api.admin.endpoint":"/admin-api/v1",
       "sebserver.webservice.api.exam.endpoint":"/exam-api",
       "sebserver.webservice.api.exam.endpoint.discovery":"/exam-api/discovery",
       "sebserver.webservice.api.exam.endpoint.v1":"/exam-api/v1",
       "sebserver.webservice.lms.api.endpoint":"/lms-api/v1",
       "sebserver.webservice.light.setup":"false"}

def expand(expr, seen=frozenset()):
    """Resolve a Java string-concat expression of API constants / ${properties}."""
    parts=[]
    for tok in re.split(r'\s*\+\s*', expr.strip()):
        tok=tok.strip()
        if re.fullmatch(r'"[^"]*"', tok):
            lit=tok[1:-1]
            for p,v in PROPS.items(): lit=lit.replace("${%s}"%p, v)
            parts.append(lit)
        else:
            name=tok.split('.')[-1]
            if name in raw and name not in seen:
                parts.append(expand(raw[name], seen|{name}))
            else:
                parts.append("{%s}"%name)
    return ''.join(parts)

def strip_gen(s):
    o=[];d=0
    for ch in s:
        if ch=='<':d+=1
        elif ch=='>':d=max(0,d-1)
        elif d==0:o.append(ch)
    return ''.join(o)

BAL=r'(?:[^()]|\((?:[^()]|\([^()]*\))*\))*'
def parse(cls):
    s=open(os.path.join(CDIR,cls+".java"),encoding='utf-8',errors='replace').read()
    m=re.search(r'(?:public\s+)?(abstract\s+)?class\s+'+re.escape(cls)+r'\b(.*?)\{',s,re.S)
    decl=strip_gen(m.group(2)) if m else ''
    ext=re.search(r'extends\s+([A-Za-z0-9_]+)',decl)
    head=s[:m.start()] if m else s
    cm=re.search(r'@RequestMapping\(('+BAL+r')\)\s*(?:@[\w.]+(?:\('+BAL+r'\))?\s*)*(?:public\s+)?(?:abstract\s+)?class',s,re.S)
    cond=re.findall(r'@(ConditionalOn\w+)\(('+BAL+r')\)',head)
    routes=[]
    # Only method declarations: a return type then a name then '('. `.` allowed in
    # qualified return types. The class declaration can never match (no return type).
    for mm in re.finditer(r'@RequestMapping\(('+BAL+r')\)\s*(?:@[\w.]+(?:\('+BAL+r'\))?\s*)*'
                          r'(?:public|protected)\s+[\w.<>,\[\]\? ]+?\s+(\w+)\s*\(',s,re.S):
        b=mm.group(1)
        v=re.search(r'RequestMethod\.([A-Z]+)',b)
        p=re.search(r'(?:path|value)\s*=\s*([^,]+?)(?:,\s*method|,\s*consumes|,\s*produces|$)',b,re.S)
        routes.append(dict(verb=v.group(1) if v else 'GET',
                           seg=re.sub(r'\s+',' ',p.group(1).strip()) if p else '(root)',
                           method=mm.group(2)))
    return dict(rest='@RestController' in s, abstract=bool(m and m.group(1)),
                extends=ext.group(1) if ext else None,
                map_expr=re.sub(r'\s+',' ',cm.group(1).strip()) if cm else None,
                cond=';'.join(a+'('+re.sub(r'\s+','',b)+')' for a,b in cond),
                routes=routes)

classes=[f[:-5] for f in sorted(os.listdir(CDIR)) if f.endswith('.java')]
P={c:parse(c) for c in classes}
BASES={'EntityController','ActivatableEntityController','ReadonlyEntityController'}
RO_DENIED={r['method'] for r in P['ReadonlyEntityController']['routes']}

def chain(cls):
    out=[];c=P[cls]['extends']
    while c and c in P: out.append(c); c=P[c]['extends']
    return out

rows=[]
for cls in classes:
    i=P[cls]
    if not i['rest']: continue
    if i['map_expr'] is None:
        ep, prefix = '', '(absolute: no class-level @RequestMapping)'
    else:
        ep = expand(i['map_expr'])
        pm = re.search(r'\$\{([^}]+)\}', i['map_expr'])
        prefix = pm.group(1) if pm else '(literal)'
    base=i['extends'] or '-'
    ro = 'ReadonlyEntityController' in chain(cls)
    for r in i['routes']:
        seg = expand(r['seg']) if r['seg']!='(root)' else '(root)'
        # No class-level @RequestMapping => the method path IS the absolute path,
        # so it becomes the endpoint (the gate denies by endpoint).
        if i['map_expr'] is None and seg != '(root)':
            rows.append((seg,cls,base,r['verb'],'(root)','own',prefix,i['cond'] or '-'))
        else:
            rows.append((ep or '(root)',cls,base,r['verb'],seg,'own',prefix,i['cond'] or '-'))
    for anc in chain(cls):
        if anc not in BASES: continue
        for r in P[anc]['routes']:
            if anc=='ReadonlyEntityController':      tag='inherited-denied'
            elif ro and r['method'] in RO_DENIED:    continue
            elif ro and r['method']=='forceHardDelete': tag='inherited-guarded'
            else:                                    tag='inherited'
            rows.append((ep or '(root)',cls,anc,r['verb'],
                         expand(r['seg']) if r['seg']!='(root)' else '(root)',
                         tag,prefix,i['cond'] or '-'))

with open(os.path.join(OUT,"operations.tsv"),"w") as fh:
    fh.write("# SEB Server REST surface, extracted from SafeExamBrowser/seb-server @ 7f45689\n")
    fh.write("# endpoint resolved with the SHIPPED property defaults "
             "(admin=/admin-api/v1, exam=/exam-api, lms=/lms-api/v1)\n")
    fh.write("# source: own | inherited | inherited-denied (body throws AccessDeniedException) "
             "| inherited-guarded (route live, stopped by the checkWriteAccess override)\n")
    fh.write("# endpoint\tcontroller\tbase_class\tverb\tpath_segment\tsource\tprefix_property\tcondition\n")
    for r in rows: fh.write("\t".join(r)+"\n")

with open(os.path.join(OUT,"endpoints.tsv"),"w") as fh:
    fh.write("# the 55 *_ENDPOINT constants of gbl/api/API.java @ 7f45689\n")
    fh.write("# kind=composed means the constant is defined as OTHER_ENDPOINT + \"/suffix\";\n")
    fh.write("#   a literals-only extractor sees 41 of 55 and misses every composed one.\n")
    fh.write("# constant\tsuffix\tkind\n")
    for k in sorted(raw):
        if not k.endswith('_ENDPOINT'): continue
        kind='literal' if re.fullmatch(r'"[^"]*"',raw[k]) else 'composed'
        fh.write(f"{k}\t{expand(raw[k])}\t{kind}\n")

ctrls=[c for c in classes if P[c]['rest']]
print("rest controllers      :",len(ctrls))
print("operations            :",len(rows))
print("by source             :",dict(Counter(r[5] for r in rows)))
print("distinct endpoints    :",len({r[0] for r in rows}))
print("endpoint constants    :",sum(1 for k in raw if k.endswith('_ENDPOINT')))
print("unresolved {} left    :",sum(1 for r in rows if '{' in r[0]))
print("writes                :",sum(1 for r in rows if r[3] in {'POST','PUT','DELETE','PATCH'}))
print("conditional rows      :",sum(1 for r in rows if r[7]!='-'))
