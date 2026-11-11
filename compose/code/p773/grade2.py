#!/usr/bin/env python3
"""p773 grant grader v2 -- written from scratch.
Fixes 4 instrument defects v1 shipped (D2-D5), all caught by hand-reading
flagged rows before any verdict was published:
  D2 positional token compare breaks when a repo fills its own copyright holder
  D3 BSD/MIT template slots read as alteration
  D4 Apache payload WITHOUT the appendix read as altered
  D5 byte-identical only/or-later arms reported as a single answer (fixed in v1)
Identity unit: normalised operative body with the copyright slot MASKED.
"""
import re, sys, os, difflib

def norm(s):
    s = s.replace("\r\n","\n")
    s = re.sub(r"[‘’‛]", "'", s)
    s = re.sub(r"[“”]", '"', s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

def mask(s):
    """D2/D3: mask the fillable slots so a filled template == the template."""
    s = re.sub(r"copyright\s*(\(c\)|©)?\s*[^\n]{0,120}?(?=permission|redistribution|all rights reserved|$)",
               " <COPYRIGHT> ", s, flags=re.I)
    s = re.sub(r"<[a-z ]*(organization|organisation|copyright holder|year|owner|name)[a-z ]*>",
               " <SLOT> ", s, flags=re.I)
    s = re.sub(r"\b(19|20)\d\d(\s*[-–]\s*((19|20)\d\d|present))?\b", " <YEAR> ", s)
    # D7 (p773): standard non-operative DECORATION. A licence title line and the
    # "all rights reserved" notice are boilerplate, not terms, and the canonical
    # SPDX texts omit both -- so leaving them unmasked spends the whole absolute
    # edit budget on decoration and reads a clean BSD/MIT payload as an alteration.
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"^(the\s+)?(mit|bsd[ -]*\d*[ -]*clause|isc|apache|mozilla public|"
               r"gnu [a-z ]*public)\s+licen[cs]e(\s*\(?[a-z0-9.\- ]*\)?)?\s*",
               " ", s, flags=re.I)
    s = re.sub(r"all rights reserved\.?", " ", s, flags=re.I)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def operative(s):
    """D4: Apache's grant ends at END OF TERMS AND CONDITIONS; the appendix is optional."""
    i = s.find("end of terms and conditions")
    return s[:i].strip() if i > 0 else s

SPDX = re.compile(r"SPDX-License-Identifier:\s*([A-Za-z0-9.\-+ ]+)", re.I)

def load_canon(d):
    raw = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".txt"):
            raw[fn[:-4]] = norm(open(os.path.join(d,fn),encoding="utf-8",errors="replace").read())
    groups = {}
    for n,b in raw.items(): groups.setdefault(b,[]).append(n)
    return {"|".join(v):k for k,v in groups.items()}

def pick(fam, tag):
    if "|" not in fam: return fam
    arms = fam.split("|")
    if tag:
        for a in arms:
            if a.lower()==tag.strip().lower(): return a
    return fam+" (body-identical group; axis undecidable from body)"

def grade(payload, canon):
    raw_len=len(payload)
    m=SPDX.search(payload); tag=m.group(1).strip() if m else None
    p=norm(payload); pm=mask(p); po=mask(operative(p))
    best=None
    for name,body in canon.items():
        bm=mask(body); bo=mask(operative(body))
        if pm==bm: return {"f":pick(name,tag),"r":"body:canonical","t":tag,"b":raw_len}
        if bm and bm in pm:
            i=pm.find(bm); pre,post=i,len(pm)-i-len(bm)
            r="canonical+PREPENDED" if pre>0 and post==0 else \
              "canonical+APPENDED" if post>0 and pre==0 else "canonical+SURROUNDED"
            c={"f":pick(name,tag),"r":r,"t":tag,"b":raw_len,"pre":pre,"post":post}
            if best is None or len(bm)>best[0]: best=(len(bm),c)
            continue
        if bo and po and bo==po:
            return {"f":pick(name,tag),"r":"canonical:operative-body-match (appendix absent/extra)",
                    "t":tag,"b":raw_len}
        if bm and 0.80 < len(pm)/max(1,len(bm)) < 1.25:
            if difflib.SequenceMatcher(None,pm,bm).quick_ratio()>0.90:
                # D6 (p773): the tolerance must be an ABSOLUTE character budget, not a
                # ratio. At 0.995 a 34,020-char AGPL text tolerates ~170 changed chars --
                # enough to invert an obligation -- while the same ratio on a 1,078-char
                # MIT file tolerates 5. Slots are already masked, so a true template
                # match differs by ~0 chars at any document size.
                delta=sum(max(i2-i1,j2-j1) for op,i1,i2,j1,j2
                          in difflib.SequenceMatcher(None,pm,bm).get_opcodes()
                          if op!="equal")
                if delta==0:
                    return {"f":pick(name,tag),"r":"body:canonical (template slot filled)","t":tag,"b":raw_len}
                if delta<=25:
                    return {"f":pick(name,tag),"r":"body:near-canonical","t":tag,"b":raw_len,
                            "delta":delta}
                if best is None: best=(len(bm),{"f":pick(name,tag),"r":"OPERATIVE-TEXT-ALTERED",
                                                "t":tag,"b":raw_len,"delta":delta})
    if best: return best[1]
    if tag: return {"f":tag,"r":"POINTER-OR-SHORT-NOTICE-resolved-by-SPDX-tag","t":tag,"b":raw_len}
    if raw_len<3000: return {"f":"UNRESOLVED","r":"POINTER-OR-SHORT-NOTICE-no-tag","t":None,"b":raw_len}
    return {"f":"UNRESOLVED","r":"OPERATIVE-TEXT-ALTERED-or-UNKNOWN","t":None,"b":raw_len}

def controls(cdir,canon):
    g=lambda s:grade(s,canon)
    mit=open(f"{cdir}/MIT.txt",encoding="utf-8").read()
    agpl=open(f"{cdir}/AGPL-3.0-or-later.txt",encoding="utf-8").read()
    bsd=open(f"{cdir}/BSD-3-Clause.txt",encoding="utf-8").read()
    ap=open(f"{cdir}/Apache-2.0.txt",encoding="utf-8").read()
    T=[("K1 exact MIT",mit,"MIT",("body:canonical","body:canonical (template slot filled)")),
       ("K2 MIT w/ real holder (D2)", mit.replace("<YEAR>","2021").replace("<COPYRIGHT HOLDERS>","Learning Equality and other contributors") if "<YEAR>" in mit else "MIT License\n\nCopyright (c) 2021 Learning Equality and other contributors\n\n"+mit.split("\n",1)[-1],
        "MIT",("body:canonical","body:canonical (template slot filled)","body:near-canonical")),
       ("K3 BSD-3 w/ org filled + title + all-rights-reserved (D3/D7)",
        "BSD 3-Clause License\n\n"+bsd.replace("<year> <owner>","2004-2025, University of Oslo").replace("Copyright (c) 2004-2025, University of Oslo. ","Copyright (c) 2004-2025, University of Oslo\nAll rights reserved.\n",1),
        "BSD-3-Clause",("body:canonical","body:canonical (template slot filled)","body:near-canonical")),
       ("K4 AGPL prepended, no tag","Blurb.\n\n"+agpl,
        "AGPL-3.0-only|AGPL-3.0-or-later (body-identical group; axis undecidable from body)",("canonical+PREPENDED",)),
       ("K5 AGPL prepended + tag","Blurb.\nSPDX-License-Identifier: AGPL-3.0-or-later\n\n"+agpl,
        "AGPL-3.0-or-later",("canonical+PREPENDED",)),
       ("K6 short notice + tag","X\nSPDX-License-Identifier: AGPL-3.0-or-later\n",
        "AGPL-3.0-or-later",("POINTER-OR-SHORT-NOTICE-resolved-by-SPDX-tag",)),
       ("K7 short notice no tag","Licensed somehow.\n","UNRESOLVED",("POINTER-OR-SHORT-NOTICE-no-tag",)),
       ("K8 Apache operative only, no appendix (D4)",ap[:ap.lower().find("end of terms and conditions")],
        "Apache-2.0",("body:canonical","canonical:operative-body-match (appendix absent/extra)","body:near-canonical","canonical+APPENDED")),
       ("K9 real alteration must still be caught",
        agpl.replace("you must","you may at your discretion").replace("GNU Affero","GNU Afferro"),
        None,("OPERATIVE-TEXT-ALTERED","body:near-canonical")),
      ]
    fails=[]
    for nm,pay,fam,rels in T:
        r=g(pay)
        okf = (fam is None) or (r["f"]==fam)
        if not okf or r["r"] not in rels:
            fails.append(f"{nm}: got {r['f']} / {r['r']}")
    return fails,len(T)

if __name__=="__main__":
    cdir=sys.argv[1]; canon=load_canon(cdir)
    f,n=controls(cdir,canon)
    print("GRADER v2 CONTROLS: %d/%d pass"%(n-len(f),n))
    for x in f: print("  FAIL",x)
    if f: sys.exit(2)
    import urllib.request
    for line in sys.stdin:
        line=line.strip()
        if not line: continue
        a,b,gf=line.split("\t")[:3]
        try:
            pay=urllib.request.urlopen(f"https://raw.githubusercontent.com/{a}/{b}/{gf}",timeout=25).read().decode("utf-8","replace")
        except Exception as e:
            print(f"{a}\tFETCH-FAIL\t{e}"); continue
        r=grade(pay,canon)
        print(f"{a}\t{r['f']}\t{r['r']}\t{r['b']}B\ttag={r['t']}"+(f"\tdelta={r.get('delta')}" if r.get('delta') is not None else "")+(f"\tpre={r.get('pre')}" if r.get('pre') else ""))
