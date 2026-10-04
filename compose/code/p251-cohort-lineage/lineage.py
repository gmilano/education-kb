#!/usr/bin/env python3
"""
P251 — clasificador de TOPOLOGIA de un cohorte.

Regla central, y es la correccion que este modulo existe para hacer cumplir:
la paternidad NO se infiere de la ausencia de menciones en el indice propio.
Se mide, y el discriminador es el TITULAR del archivo de licencia contra el
DUENO del repositorio (el eje de P184, usado aca como instrumento de linaje):

  holder ~ owner                     -> ORIGIN-CANDIDATE
  holder ~ owner de OTRO del cohorte -> DERIVATIVE-OF <ese>
  holder sin correspondencia         -> UNDETERMINED   (nunca INDEPENDENT)
  sin archivo de licencia            -> UNDETERMINED   (nunca INDEPENDENT)

COTA DECLARADA, y es la que impide leer de mas este instrumento:
un `LICENSE` byte a byte identico prueba MISMO TITULAR, no linaje. Dos repos
del mismo autor coinciden sin que ninguno sea fork del otro. Por eso la salida
distingue ORIGIN-CANDIDATE de DERIVATIVE-OF por el dueno, y no por el hash.
"""
import re, sys, unicodedata
from collections import defaultdict

def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s.lower())

def tokens(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return [t for t in re.split(r"[^A-Za-z0-9]+", s.lower()) if len(t) >= 3]

def holder_name(holder):
    """Extrae el nombre del titular de una linea de copyright."""
    if not holder or holder == "-":
        return ""
    h = re.sub(r"(?i)copyright", " ", holder)
    h = re.sub(r"\(c\)|\(C\)|©", " ", h)
    h = re.sub(r"\b(19|20)\d{2}\b", " ", h)          # el ANO no es el titular
    h = re.sub(r"[,\-–]+", " ", h)
    return h.strip()

def match_strength(holder, owner):
    """STRONG | WEAK | NONE — con la cota: es una heuristica de NOMBRE."""
    hn, on = norm(holder_name(holder)), norm(owner)
    if not hn or not on:
        return "NONE"
    if hn == on or hn in on or on in hn:
        return "STRONG"
    ht = tokens(holder_name(holder))
    if ht:
        hits = sum(1 for t in ht if t in on)
        if hits and hits * 2 >= len(ht):
            return "WEAK"
    return "NONE"

def classify(rows):
    """rows: lista de dicts con slug, lic_code, lic_sha16, holder.
    Devuelve dict slug -> (verdict, detail)."""
    owners = {r["slug"].split("/")[0]: r["slug"] for r in rows}
    out = {}
    for r in rows:
        slug = r["slug"]
        owner = slug.split("/")[0]
        if r.get("lic_code") != "200" or r.get("lic_sha16") in (None, "-", ""):
            out[slug] = ("UNDETERMINED", "sin archivo de licencia por canal calibrado")
            continue
        holder = r.get("holder", "-")
        if match_strength(holder, owner) != "NONE":
            out[slug] = ("ORIGIN-CANDIDATE", f"titular ~ dueno ({holder_name(holder)})")
            continue
        best = None
        for other_owner, other_slug in owners.items():
            if other_owner == owner:
                continue
            st = match_strength(holder, other_owner)
            if st != "NONE" and (best is None or st == "STRONG"):
                best = (other_slug, st)
                if st == "STRONG":
                    break
        if best:
            out[slug] = ("DERIVATIVE-OF", best[0])
        else:
            out[slug] = ("UNDETERMINED", f"titular sin correspondencia en el cohorte: {holder_name(holder)!r}")
    return out

def paternity_claim(rows, candidate):
    """La compuerta de P251. Devuelve (veredicto, n_derivados).
    NO-CLAIM si el candidato no tiene UN derivado MEDIDO en el cohorte.
    Nunca devuelve PARENT por ausencia de menciones."""
    cl = classify(rows)
    kids = [s for s, (v, d) in cl.items() if v == "DERIVATIVE-OF" and d == candidate]
    if not kids:
        return ("NO-CLAIM", 0)
    return ("PARENT", len(kids))

def read_tsv(path):
    rows, hdr = [], None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if hdr is None:
                hdr = parts
                continue
            rows.append(dict(zip(hdr, parts)))
    return rows

if __name__ == "__main__":
    rows = read_tsv(sys.argv[1] if len(sys.argv) > 1 else "rows.tsv")
    cl = classify(rows)
    clusters = defaultdict(list)
    for r in rows:
        clusters[r.get("lic_sha16", "-")].append(r["slug"])
    print(f"cohorte: {len(rows)} slugs\n")
    for slug, (v, d) in sorted(cl.items(), key=lambda kv: (kv[1][0], kv[0])):
        print(f"  {v:<17} {slug:<42} {d}")
    print("\nracimos por sha256 del LICENSE (= MISMO TITULAR, no linaje):")
    for sha, members in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        if sha == "-":
            print(f"  {'(sin licencia)':<18} n={len(members)}  {', '.join(sorted(members))}")
        else:
            print(f"  {sha:<18} n={len(members)}  {', '.join(sorted(members))}")
    print("\ncompuerta de paternidad (P251):")
    for cand in sorted({r["slug"] for r in rows}):
        v, n = paternity_claim(rows, cand)
        if v == "PARENT":
            print(f"  PARENT   {cand} -> {n} derivado(s) MEDIDO(s)")
    for cand in sorted({r["slug"] for r in rows}):
        v, n = paternity_claim(rows, cand)
        if v == "NO-CLAIM":
            print(f"  NO-CLAIM {cand}")
