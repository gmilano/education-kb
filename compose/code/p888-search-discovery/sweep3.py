#!/usr/bin/env python3
"""p888 sweep3: REGIONAL discovery legs in-language. Owner /users is 403, so
region cannot come from owner location; an in-language query + a named national
curriculum is the strongest region evidence this session can obtain."""
import json,subprocess,sys,time,os
OUT=os.path.dirname(os.path.abspath(__file__))
LEGS=[
 ("LATAM-es-tutor","tutor educativo inteligencia artificial in:name,description,readme","LATAM"),
 ("LATAM-pt-tutor","tutor educacional inteligencia artificial in:name,description,readme","LATAM"),
 ("LATAM-es-docente","docente profesor aula plan de clase in:name,description,readme","LATAM"),
 ("LATAM-pt-escola","escola professor aluno plano de aula in:name,description,readme","LATAM"),
 ("LATAM-es-eval","evaluacion automatica examen rubrica in:name,description,readme","LATAM"),
 ("LATAM-enem","ENEM OR vestibular OR SAEB questoes in:name,description,readme","LATAM"),
 ("EMEA-africa","Nigeria OR Kenya OR Ghana OR 'South Africa' curriculum school in:name,description,readme","EMEA"),
 ("EMEA-fr","enseignant eleve cours scolaire IA in:name,description,readme","EMEA"),
 ("EMEA-de","Lehrer Schule Unterricht KI in:name,description,readme","EMEA"),
 ("EMEA-ar","Arabic curriculum school exam in:name,description,readme","EMEA"),
 ("APAC-india","NCERT OR CBSE OR 'Indian curriculum' school in:name,description,readme","APAC"),
 ("APAC-sea","Indonesia OR Vietnam OR Thailand OR Philippines curriculum school in:name,description,readme","APAC"),
 ("NA-us-standards","'Common Core' OR NGSS OR 'state standards' lesson in:name,description,readme","North America"),
 ("NA-canada","Ontario OR Alberta OR 'British Columbia' curriculum in:name,description,readme","North America"),
]
def gh(q,sort="updated"):
    r=subprocess.run(["gh","api","-X","GET","search/repositories","-f",f"q={q}","-f","per_page=50","-f",f"sort={sort}"],capture_output=True,text=True,timeout=90)
    if r.returncode!=0: return None,r.stderr.strip()[:160]
    try: return json.loads(r.stdout),None
    except Exception as e: return None,str(e)[:160]
rows=[];meta=[]
for name,q,region in LEGS:
    d,err=gh(q)
    if d is None:
        meta.append((name,region,q,"ERROR",0,err));print(f"[{name}] ERROR {err}",file=sys.stderr);continue
    tc=d.get("total_count",0);items=d.get("items",[])
    meta.append((name,region,q,"OK",tc,f"{len(items)} returned"))
    print(f"[{name}] ({region}) tc={tc} n={len(items)}",file=sys.stderr)
    for it in items:
        lic=it.get("license") or {}
        rows.append({"leg":name,"leg_region":region,"slug":it["full_name"],
          "stars":it.get("stargazers_count"),"forks":it.get("forks_count"),
          "spdx":lic.get("spdx_id") or "NONE","pushed":(it.get("pushed_at") or "")[:10],
          "archived":it.get("archived"),"is_fork":it.get("fork"),"branch":it.get("default_branch"),
          "lang":it.get("language") or "-","desc":(it.get("description") or "").replace("\t"," ")[:300]})
    time.sleep(2.2)
json.dump(rows,open(f"{OUT}/raw3.json","w"),indent=1)
with open(f"{OUT}/legs3.tsv","w") as f:
    f.write("leg\tregion\tquery\tstatus\ttotal_count\tnote\n")
    for m in meta: f.write("\t".join(str(x) for x in m)+"\n")
print(f"TOTAL {len(rows)}",file=sys.stderr)
