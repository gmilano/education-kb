import os,sys,hashlib,csv
sys.path.insert(0,"/home/user/education-kb/compose/code/p474-scope-and-language")
import family_lang as fl
from family_lang import grade, _norm, TITLES

# the pre-p474 reader: English title strings only
EN_ONLY = {"AGPL":["GNU AFFERO GENERAL PUBLIC LICENSE"],"LGPL":["GNU LESSER GENERAL PUBLIC LICENSE"],
 "GPL":["GNU GENERAL PUBLIC LICENSE"],"ECL":["EDUCATIONAL COMMUNITY LICENSE"],
 "APACHE":["APACHE LICENSE"],"MIT":["MIT LICENSE"],"CC":["CREATIVE COMMONS"]}
def en_only(payload):
    head=_norm("\n".join([l for l in payload.splitlines() if l.strip()][:6]))
    for fam,needles in EN_ONLY.items():
        if any(n in head for n in needles): return fam
    return "UNSTATED"

rows=[]
for fn in sorted(os.listdir("payloads")):
    p=os.path.join("payloads",fn)
    if not os.path.isfile(p): continue
    b=open(p,'rb').read()
    body=b.decode('utf-8','replace')
    g=grade(body)
    rows.append(dict(payload=fn,bytes=len(b),digest=hashlib.sha256(b).hexdigest()[:12],
        en_only=en_only(body), family=g["family"] or "UNSTATED", version=g["version"] or "-",
        or_later=g["or_later"], scope=g["scope"], nc_part=g["noncommercial_part"],
        reserved=g["reserved_part"], single_cell_sound=g["single_cell_sound"]))

cols=["payload","bytes","digest","en_only","family","version","or_later","scope","nc_part","reserved","single_cell_sound"]
with open("grant-lang-scope.2026-10-27-p474.tsv","w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=cols,delimiter="\t"); w.writeheader(); w.writerows(rows)

print("\n=== Gap 473-C: rows where the English-only reader DISAGREES with the language-aware reader ===")
n=0
for r in rows:
    if r["en_only"]!=r["family"]:
        n+=1
        print(f"  {r['payload'][:58]:58} en_only={r['en_only']:9} -> p474={r['family']}-{r['version']} or_later={r['or_later']}")
print(f"  {n} disagreement(s) of {len(rows)} payloads")
print("\n=== p474 scope axis: payloads where a single SPDX-style cell is NOT sound ===")
for r in rows:
    if not r["single_cell_sound"]:
        print(f"  {r['payload'][:58]:58} scope={r['scope']:12} nc_part={r['nc_part']} reserved={r['reserved']}")
print(f"\ntotal payloads graded: {len(rows)}")
