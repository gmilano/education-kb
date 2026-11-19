import json,re,sys,csv
rows=json.load(open("compose/code/p929-shelf-depth/rows.json"))
found=json.load(open("compose/code/p929-shelf-depth/found.json"))
def norm(pub):
    if not pub: return None
    p=pub.replace('**','').replace('`','')
    for pat,spdx in [(r'Apache[- ]2\.0','Apache-2.0'),(r'\bMIT\b','MIT'),(r'BSD[- ]3[- ]Clause','BSD-3-Clause'),
      (r'BSD[- ]2[- ]Clause','BSD-2-Clause'),(r'\bISC\b','ISC'),(r'MPL[- ]2\.0','MPL-2.0'),(r'\bUnlicense\b','Unlicense'),
      (r'\b0BSD\b','0BSD'),(r'AGPL[- ]?3','AGPL-3.0'),(r'LGPL[- ]?3','LGPL-3.0'),(r'LGPL[- ]?2','LGPL-2.1'),
      (r'GPL[- ]?3','GPL-3.0'),(r'GPL[- ]?2','GPL-2.0'),(r'CC[ -]BY[ -]SA','CC-BY-SA-4.0'),(r'CC[ -]BY[ -]NC','CC-BY-NC-4.0'),
      (r'CC[ -]BY','CC-BY-4.0'),(r'CC0','CC0-1.0'),(r'\bEPL','EPL-2.0'),(r'ODbL','ODbL-1.0'),(r'EUPL','EUPL-1.2'),
      (r'NOASSERTION','NOASSERTION'),(r'\bNONE\b','NONE')]:
        if re.search(pat,p,re.I): return spdx
    return None
star_drift=[];lic_drift=[];arch=[];stale=[]
for r in rows:
    f=found.get(r["slug"].lower())
    if not f: continue
    if r["pub_stars"] is not None and f["stars"] is not None:
        d=f["stars"]-r["pub_stars"]
        if abs(d)>=1: star_drift.append((r["file"],r["line"],r["slug"],r["pub_stars"],f["stars"],d))
    pn=norm(r["pub_lic"]); an=f["lic"]
    if pn and an and an not in ("NOASSERTION",) and pn!=an:
        lic_drift.append((r["file"],r["line"],r["slug"],r["pub_lic"],an))
    if f["archived"]: arch.append((r["file"],r["line"],r["slug"],f["pushed"]))
    if f["pushed"]<"2026-05-01": stale.append((r["file"],r["line"],r["slug"],f["pushed"],f["stars"]))
print("rows audited:",len(rows),"resolved:",len(found))
print("STAR DRIFT rows:",len(star_drift))
big=sorted(star_drift,key=lambda x:-abs(x[5]))[:18]
for b in big: print("   %-42s pub=%-7s now=%-7s %+d  (%s:%s)"%(b[2],b[3],b[4],b[5],b[0],b[1]))
neg=[s for s in star_drift if s[5]<0]
print("   negative-drift rows:",len(neg))
print("LICENCE DRIFT rows:",len(lic_drift))
for l in lic_drift: print("   %-42s published=%-28s api=%s  (%s:%s)"%(l[2],l[3][:28],l[4],l[0],l[1]))
print("ARCHIVED rows:",len(arch))
for a in arch: print("   ",a)
print("STALE (no push since 2026-05-01):",len(stale))
for s in sorted(stale,key=lambda x:x[3])[:15]: print("   %-42s last_push=%s stars=%s (%s)"%(s[2],s[3],s[4],s[0]))
csv.writer(open("evidence/shelf-depth-audit.2026-11-19-p929.tsv","w"),delimiter="\t").writerows(
  [["file","line","slug","pub_stars","api_stars","delta","pub_lic","api_lic","pushed","archived"]]+
  [[r["file"],r["line"],r["slug"],r["pub_stars"],found[r["slug"].lower()]["stars"],
    (found[r["slug"].lower()]["stars"]-r["pub_stars"]) if r["pub_stars"] is not None else "",
    (r["pub_lic"] or "").replace("\t"," "),found[r["slug"].lower()]["lic"],
    found[r["slug"].lower()]["pushed"],found[r["slug"].lower()]["archived"]]
   for r in rows if r["slug"].lower() in found])
