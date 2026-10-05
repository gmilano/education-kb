#!/usr/bin/env python3
"""P328 — veredicto de cesion por ITEM contra la cesion del TITULAR.

Dos ejes que esta base trataba como uno:
  eje 1  la obra citada en `oer`  -> que EDICION se cita
  eje 2  la cesion que el titular OTORGA a ESA edicion (leida de su payload)
El veredicto es la COMPARACION. Un item no puede ampliar lo que su titular cede.

Regla de unidad (P126/P107): el denominador se NOMBRA siempre. `items` y
`unidades de cesion` son poblaciones distintas y dan porcentajes distintos.
"""
import re

NC  = "CC BY-NC-SA 4.0"
BY  = "CC BY 4.0"

def fam_from_url(url):
    """Familia desde la URL de md:license. No adivina desde el nombre del libro."""
    u = (url or "").lower()
    if "by-nc-sa" in u: return NC
    if "by-nc"    in u: return "CC BY-NC"
    if "by-sa"    in u: return "CC BY-SA"
    if "/by/"     in u: return BY
    return None

def fam_from_item(lic):
    """Familia que el ITEM declara. '' y None son AUSENCIA, no permiso."""
    if lic is None: return "(sin declarar)"
    s = str(lic).strip()
    if not s: return "(sin declarar)"
    l = s.lower()
    if "by-nc-sa" in l: return NC
    if "/by/" in l or "cc by 4.0" in l: return BY
    if l.replace(" ", "") in ("cc4.0", "cc-4.0"): return "CC4.0 (sin clausulas)"
    return "otro"

def work_from_oer(oer):
    """Obra citada. Acepta las DOS formas de URL de OpenStax
    (/details/books/X y /books/X) — el extractor del pase 105 perdia una."""
    if not oer: return None
    m = re.search(r"(?:details/)?books/([a-z0-9\-]+)", str(oer))
    return m.group(1) if m else None

RANK = {BY: 3, "CC BY-SA": 2, "CC BY-NC": 1, NC: 1}

def verdict(item_lic, holder_fam):
    """CORRECTO / CONTRADICE / SIN-DECLARAR / NO-CLAIM."""
    if holder_fam is None:
        return "NO-CLAIM"          # sin cesion del titular no hay veredicto
    f = fam_from_item(item_lic)
    if f == "(sin declarar)":
        return "SIN-DECLARAR"
    if f in ("otro", "CC4.0 (sin clausulas)"):
        return "NO-CLAIM"          # no nombra clausulas => no se resuelve
    if f == holder_fam:
        return "CORRECTO"
    if RANK.get(f, 0) > RANK.get(holder_fam, 0):
        return "CONTRADICE"        # el item cede MAS de lo que el titular otorga
    return "CORRECTO"              # ceder MENOS siempre se puede

def narrowed(rows):
    """Colecciones con el MISMO collection-id en dos refs cuya cesion se ESTRECHA.
    La identidad es el collection-id, NO el slug: el slug cambia de nombre
    entre ediciones y por eso esta base no veia el estrechamiento."""
    by_col = {}
    for r in rows:
        by_col.setdefault(r["col"], {})[r["ref"]] = r["familia"]
    out = []
    for col, refs in by_col.items():
        if "1e" in refs and "main" in refs:
            if RANK.get(refs["1e"], 0) > RANK.get(refs["main"], 0):
                out.append((col, refs["1e"], refs["main"]))
    return sorted(out)

def load_tsv(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if not line.strip(): continue
            rows.append(dict(zip(head, line.rstrip("\n").split("\t"))))
    return rows
