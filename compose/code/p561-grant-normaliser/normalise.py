#!/usr/bin/env python3
# p561 — the four-stage grant normaliser, and the family census it produces.
# Stage 1 raw.  Stage 2 whitespace fold (\s+ -> " ", strip).  Stage 3 punctuation fold
# (curly quotes/dashes -> ASCII, (C)/(c) <- ©, fsf.org scheme).  Stage 4 case fold.
import hashlib, re, sys, urllib.request, json
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"p561"}), timeout=60) as r:
        return r.read()
def d12(b): return hashlib.sha256(b).hexdigest()[:12]
def ws(b):
    t = b.decode("utf-8","replace").replace(" "," ")
    return re.sub(r"\s+"," ",t).strip().encode()
def punct(b):
    t = b.decode()
    for a,c in (("“",'"'),("”",'"'),("‘","'"),("’","'"),
                ("–","-"),("—","-"),("©","(C)"),("®","(R)"),
                ("http://fsf.org/","https://fsf.org/"),
                ("http://www.fsf.org/","https://fsf.org/"),
                ("http://www.gnu.org/","https://www.gnu.org/")):
        t = t.replace(a,c)
    return t.encode()
def cf(b): return b.decode().lower().encode()
FAM = {
 "Apache-2.0": [("publisher apache.org","https://www.apache.org/licenses/LICENSE-2.0.txt"),
   ("spdx Apache-2.0","https://raw.githubusercontent.com/spdx/license-list-data/main/text/Apache-2.0.txt"),
   ("oppia/oppia develop/LICENSE","https://raw.githubusercontent.com/oppia/oppia/develop/LICENSE")],
 "GPL-3.0": [("spdx GPL-3.0-only","https://raw.githubusercontent.com/spdx/license-list-data/main/text/GPL-3.0-only.txt"),
   ("moodle/moodle main/COPYING.txt","https://raw.githubusercontent.com/moodle/moodle/main/COPYING.txt"),
   ("h5p/h5p-php-library master/LICENSE.txt","https://raw.githubusercontent.com/h5p/h5p-php-library/master/LICENSE.txt")],
 "AGPL-3.0": [("spdx AGPL-3.0-only","https://raw.githubusercontent.com/spdx/license-list-data/main/text/AGPL-3.0-only.txt"),
   ("instructure/canvas-lms master/LICENSE","https://raw.githubusercontent.com/instructure/canvas-lms/master/LICENSE"),
   ("openedx/openedx-platform master/LICENSE","https://raw.githubusercontent.com/openedx/openedx-platform/master/LICENSE")],
 "LGPL-3.0": [("spdx LGPL-3.0-only","https://raw.githubusercontent.com/spdx/license-list-data/main/text/LGPL-3.0-only.txt"),
   ("bigbluebutton v4.0.x-develop/LICENSE","https://raw.githubusercontent.com/bigbluebutton/bigbluebutton/v4.0.x-develop/LICENSE")],
 "BSD-3-Clause": [("spdx BSD-3-Clause","https://raw.githubusercontent.com/spdx/license-list-data/main/text/BSD-3-Clause.txt"),
   ("jupyter/nbgrader main/LICENSE","https://raw.githubusercontent.com/jupyter/nbgrader/main/LICENSE"),
   ("jupyterhub/jupyterhub main/LICENSE","https://raw.githubusercontent.com/jupyterhub/jupyterhub/main/LICENSE")],
}
out=[]
hdr=f"{'family':<13} {'source':<40} {'raw_B':>7} {'raw':<13} {'ws_B':>7} {'ws':<13} {'punct':<13} {'case':<13}"
print(hdr); print("-"*len(hdr))
summary={}
for fam,srcs in FAM.items():
    sets={"raw":set(),"ws":set(),"punct":set(),"case":set()}
    for label,url in srcs:
        b=get(url); w=ws(b); p=punct(w); c=cf(p)
        sets["raw"].add(d12(b)); sets["ws"].add(d12(w)); sets["punct"].add(d12(p)); sets["case"].add(d12(c))
        print(f"{fam:<13} {label:<40} {len(b):>7} {d12(b):<13} {len(w):>7} {d12(w):<13} {d12(p):<13} {d12(c):<13}")
        out.append(dict(family=fam,source=label,url=url,raw_B=len(b),raw=d12(b),ws_B=len(w),ws=d12(w),punct=d12(p),case=d12(c)))
    summary[fam]={k:len(v) for k,v in sets.items()}
    n=len(srcs)
    print(f"{fam:<13} {'-- distinct digests / '+str(n)+' sources --':<40} "
          f"{summary[fam]['raw']:>7} {'':<13} {summary[fam]['ws']:>7} {'':<13} "
          f"{summary[fam]['punct']:<13} {summary[fam]['case']:<13}")
    print()
json.dump(out, open("p561-canonical-grant-census.json","w"), indent=1)
print("SUMMARY (distinct digests at each stage):")
for f,s in summary.items(): print(" ", f, s)
