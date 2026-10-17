import re, os, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import queue as Q
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
Q.GRANT_EVIDENCE = re.compile(r"[Ll]icen[cs]e\.(txt|md|rtf)|/[Ll]icen[cs]e\b|\bLICEN[CS]E\b"
    r"|\d[\d  ]*[`*_]*\s*B\b|(?i:manifests? declare)|(?i:read at payload)"
    r"|(?i:payload is|payload-read|reproduced to the byte|verbatim [A-Z])"
    r"|(?i:pom\.xml|package\.json|composer\.json|pyproject\.toml|readme\.txt|<licenses>)"
    r"|(?i:metadata grade|metadata\)|manifest grade)")
SCOPED=re.compile(r"(^|/)(assets?|dataset|datasets|fonts?|icons?|images?|media|javascripts|\.corepack)(/|$)",re.I)
TRANSLATION=re.compile(r"(^|/)licen[cs]e_[a-z]+\.(txt|md)$",re.I)
ABSENT=re.compile(r"no licen[cs]e key|^-+$|^none$",re.I)
def cg(paths):
    out=[]
    for p in paths:
        p=p.strip()
        if not p or p=="NONE_IN_TREE" or not Q.LICENCEY.search(p): continue
        if Q.VENDORED.search(p) or Q.SOURCEY.search(p): continue
        if SCOPED.search(os.path.dirname(p)) or TRANSLATION.search(p): continue
        out.append(p)
    return out
def man():
    m={}
    for path in sorted(glob.glob(os.path.join(ROOT,"evidence","manifest-channel.*.tsv"))):
        for line in open(path,encoding="utf-8"):
            if line.startswith("#") or not line.strip(): continue
            c=line.rstrip("\n").split("\t")
            if len(c)<5 or c[0]=="slug": continue
            k=c[4].strip()
            if k and not ABSENT.search(k): m[c[0].strip()]=k
    return m
def attr(line,names=()):
    marks=[(x.start(),x.group(1).rstrip(".")) for x in Q.SLUG.finditer(line)]
    for slug in names:
        b=slug.split("/")[-1]
        if len(b)<4: continue
        for x in re.finditer(r"(?<![-_/A-Za-z0-9])"+re.escape(b)+r"(?![-_/A-Za-z0-9])(?!'s|’s)",line):
            marks.append((x.start(),slug))
    if not marks: return []
    marks.sort(); own=set()
    for ph in Q.NEGATIVE.finditer(line):
        bf=[s for s in marks if s[0]<ph.start()]
        own.add(bf[-1][1] if bf else marks[0][1])
    return sorted(own)
L,_=Q.load_ledgers(ROOT); M=man()
ref=[];ver=0;que=0
for sh in Q.SHELVES:
    for n,line in enumerate(open(f"{ROOT}/{sh}",encoding="utf-8"),1):
        if not Q.NEGATIVE.search(line): continue
        if Q.RETRACTION.search(line) or Q.states_a_grant(line): continue
        for slug in attr(line,L.keys()):
            if slug not in L: que+=1; continue
            g=cg(L[slug]) or (["(manifest) "+M[slug]] if slug in M else [])
            if g: ref.append((sh,n,slug,g[0]))
            else: ver+=1
print(f"REFUTED={len(ref)}  VERIFIED-ABSENT={ver}  QUEUE-UNENUMERATED={que}")
for r in ref: print("   STILL REFUTED:",r[0]+":"+str(r[1]),r[2],r[3][:70])
print("GATE WOULD:", "PASS" if not ref else "FAIL")
