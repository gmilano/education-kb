import sys,os,re,urllib.request,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from norm import ws,punct,sha12
def fold(t):
    return re.sub(r'Copyright\s*(?:\(c\)|\(C\))?\s*[0-9]{4}(?:\s*[-,]\s*(?:[0-9]{4}|present))?\s*[^.]{0,120}?(?=\s+Permission is hereby granted)',
                  'Copyright (c) <YEAR> <HOLDER>',t,flags=re.I)
def get(s,p="LICENSE"):
    o=subprocess.run(["git","ls-remote","--symref",f"https://github.com/{s}","HEAD"],capture_output=True,text=True,timeout=90).stdout
    b=re.search(r"ref:\s+refs/heads/(\S+)\s+HEAD",o).group(1)
    for pp in (p,"LICENSE.md","LICENSE.txt","license.txt"):
        try:
            r=urllib.request.urlopen(f"https://raw.githubusercontent.com/{s}/{b}/{pp}",timeout=60)
            if r.status==200: return r.read()
        except Exception: pass
t=punct(ws(get("EduThemes/paper-lms"))).decode()
base=fold(t); bl=len(base.encode())
print("=== 561-D decisive test: EQUAL-LENGTH operative substitution ===")
print(f"  stock folded: {bl} B  {sha12(base)}")
tests=[("permit->forbid (6->6, INVERTS the grant)", t.replace("to permit persons","to forbid persons",1)),
       ("Software->Hardware (8->8)",                 t.replace("of the Software, and to permit","of the Hardware, and to permit",1)),
       ("free of charge->free of charge (control)",  t)]
for name,v in tests:
    f=fold(v); L=len(f.encode())
    same_len = (L==bl); same_dig = (sha12(f)==sha12(base))
    print(f"  {name:44s} fold_B={L:5d} {'==' if same_len else '!='}stock  sha={sha12(f)}")
    if not same_dig and same_len:
        print(f"      -> LENGTH GATE FALSE-MATCHES; digest gate catches it")
    elif same_dig:
        print(f"      -> identical (control)")
    else:
        print(f"      -> both gates catch it")
print("\n=== why 2 of 9 do not collapse: the copyright span the fold must match ===")
for s in ("frappe/frappe","ucfopen/canvasapi","EduThemes/paper-lms"):
    b=get(s); tt=punct(ws(b)).decode()
    m=re.search(r'(.{0,10}Copyright.{0,130}?)(?=Permission is hereby granted)',tt,re.I)
    fired = fold(tt)!=tt
    print(f"  {s:26s} fold fired={str(fired):5s} span={m.group(1)[:118]!r}" if m else f"  {s:26s} NO COPYRIGHT SPAN FOUND before grant clause")
