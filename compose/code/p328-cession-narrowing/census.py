#!/usr/bin/env python3
"""Censo de cesion de OATutor-Content contra la cesion MEDIDA del titular.
Uso: python3 census.py /ruta/a/OATutor-Content"""
import json, os, sys, collections, verdict as V

root = sys.argv[1] if len(sys.argv)>1 else "."
rows = V.load_tsv(os.path.join(os.path.dirname(os.path.abspath(__file__)),"osbooks-cesion.tsv"))
# cesion del titular por slug, por ref. Para un item, la obra citada es el slug.
HOLDER = {}
for r in rows:
    HOLDER[r["slug"]] = r["familia"]

CNT=collections.Counter(); BYWORK=collections.Counter(); LAYER=collections.Counter()
SYNTH=collections.Counter()

def layer_of(p):
    if "/tutoring/" in p: return "tutoring"
    return "problema"

def walk(o, lay):
    if isinstance(o, dict):
        if "license" in o:
            LAYER[lay]+=1
            oer=o.get("oer") or ""
            work=V.work_from_oer(oer)
            if str(oer).strip().lower()=="openai":
                SYNTH[(V.fam_from_item(o.get("license")), o.get("type") or "?")]+=1
            hf = HOLDER.get(work) if work else None
            v = V.verdict(o.get("license"), hf)
            CNT[(lay,v)]+=1
            if work: BYWORK[(work, hf or "NO-MEDIDA", v)]+=1
        for k,val in o.items(): walk(val, lay)
    elif isinstance(o, list):
        for val in o: walk(val, lay)

n=0
for dp,dn,fn in os.walk(os.path.join(root,"content-pool")):
    for f in fn:
        if not f.endswith(".json"): continue
        p=os.path.join(dp,f).replace(os.sep,"/"); n+=1
        with open(p,encoding="utf-8") as fh: walk(json.load(fh), layer_of(p))

tot=sum(LAYER.values())
print(f"JSON leidos: {n}")
print(f"\n=== UNIDADES DE CESION (el denominador, NOMBRADO) ===")
for k,v in LAYER.most_common(): print(f"  {k:9s}: {v:7d}")
print(f"  {'TOTAL':9s}: {tot:7d}")
print(f"\n=== VEREDICTO por capa ===")
for (lay,v),c in sorted(CNT.items(), key=lambda x:(-x[1])):
    print(f"  {c:7d}  ({100*c/tot:5.1f} %)  [{lay:9s}] {v}")
print(f"\n=== VEREDICTO agregado ===")
agg=collections.Counter()
for (lay,v),c in CNT.items(): agg[v]+=c
for v,c in agg.most_common(): print(f"  {c:7d}  ({100*c/tot:5.1f} %)  {v}")
print(f"\n=== por obra citada: titular MEDIDO vs veredicto del item ===")
works=sorted({w for w,_,_ in BYWORK})
for w in works:
    sub={(h,v):c for (ww,h,v),c in BYWORK.items() if ww==w}
    s=sum(sub.values()); h=[hh for (hh,_) in sub][0]
    print(f"\n  {w}   [titular cede: {h}]   total {s}")
    for (hh,v),c in sorted(sub.items(), key=lambda x:-x[1]): print(f"      {c:6d}  {v}")
print(f"\n=== capa SINTETICA (oer=openai): contenido generado, cesion declarada ===")
st=0
for (f,t),c in SYNTH.most_common(): print(f"  {c:7d}  type={t:9s} cesion={f}"); st+=c
print(f"  TOTAL sintetico: {st}")
