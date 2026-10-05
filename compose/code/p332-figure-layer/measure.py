#!/usr/bin/env python3
"""p331-figure-layer — corre las acciones A y B pre-registradas por el pase 106.

A) La capa de IMAGEN: los `.gif` del redistribuidor, cruzados contra el `oer` y el
   `license` del problema que los posee.
B) Las unidades de `tutoring/` con `oer` VACIO: ¿de que problema cuelgan?

Uso: python3 measure.py /ruta/a/OATutor-Content
Salida: TSV por stdout + resumen por stderr. Codigo 2 si el arbol no esta materializado.
"""
import json
import os
import re
import sys
from collections import Counter

OPENSTAX = re.compile(r"openstax\.org", re.I)


def familia(lic):
    """Familia de cesion por bloque de titulo, NUNCA por sha (P171/P329)."""
    if not lic or not lic.strip():
        return "SIN-DECLARAR"
    s = lic.lower()
    # el orden importa: `by-nc-sa` contiene `by` (P299)
    for needle, fam in (
        ("by-nc-sa", "CC BY-NC-SA 4.0"),
        ("by-nc-nd", "CC BY-NC-ND 4.0"),
        ("by-sa", "CC BY-SA 4.0"),
        ("by-nd", "CC BY-ND 4.0"),
        ("by-nc", "CC BY-NC 4.0"),
    ):
        if needle in s:
            return fam
    if re.search(r"\bby\b|licenses/by/", s):
        return "CC BY 4.0"
    return "NO-RESUELVE"


def leer(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:  # noqa: BLE001
        return {"__error__": str(exc)}


def main(root):
    pool = os.path.join(root, "content-pool")
    if not os.path.isdir(pool):
        print("content-pool no materializado", file=sys.stderr)
        return 2

    problemas = {}       # problemId -> (oer, license)
    gifs = []            # (problemId, ruta)
    tut_vacios = []      # (problemId, stepId, hintId, tipo)
    tut_total = 0
    hint_total = 0
    err = 0

    for pid in sorted(os.listdir(pool)):
        pdir = os.path.join(pool, pid)
        if not os.path.isdir(pdir):
            continue
        pj = os.path.join(pdir, pid + ".json")
        if os.path.isfile(pj):
            d = leer(pj)
            if "__error__" in d:
                err += 1
            problemas[pid] = (d.get("oer", ""), d.get("license", ""))
        fig = os.path.join(pdir, "figures")
        if os.path.isdir(fig):
            for f in sorted(os.listdir(fig)):
                if f.lower().endswith(".gif"):
                    gifs.append((pid, os.path.join("content-pool", pid, "figures", f)))
        steps = os.path.join(pdir, "steps")
        if not os.path.isdir(steps):
            continue
        for sid in sorted(os.listdir(steps)):
            tdir = os.path.join(steps, sid, "tutoring")
            if not os.path.isdir(tdir):
                continue
            for f in sorted(os.listdir(tdir)):
                if not f.endswith(".json"):
                    continue
                tut_total += 1
                data = leer(os.path.join(tdir, f))
                if isinstance(data, dict) and "__error__" in data:
                    err += 1
                    continue
                if not isinstance(data, list):
                    data = [data]
                for h in data:
                    if not isinstance(h, dict):
                        continue
                    hint_total += 1
                    if not (h.get("oer") or "").strip():
                        tut_vacios.append((pid, sid, h.get("id", ""), h.get("type", "")))
                    for sub in h.get("subHints", []) or []:
                        if not isinstance(sub, dict):
                            continue
                        hint_total += 1
                        if not (sub.get("oer") or "").strip():
                            tut_vacios.append((pid, sid, sub.get("id", ""), sub.get("type", "")))

    # ---------- ACCION A ----------
    print("# ACCION A — los .gif y la cesion del problema que los posee")
    print("problema\tgif\toer_del_problema\tfamilia_del_problema")
    fam_gif = Counter()
    oer_gif = Counter()
    for pid, ruta in gifs:
        oer, lic = problemas.get(pid, ("", ""))
        fam = familia(lic)
        clase = "openstax" if OPENSTAX.search(oer or "") else ("vacio" if not (oer or "").strip() else "otro")
        fam_gif[fam] += 1
        oer_gif[clase] += 1
        print(f"{pid}\t{ruta}\t{clase}\t{fam}")

    # ---------- ACCION B ----------
    print()
    print("# ACCION B — unidades de tutoring con oer VACIO, por clase del problema padre")
    print("clase_del_problema_padre\tfamilia_del_problema_padre\tunidades")
    cruce = Counter()
    for pid, _sid, _hid, _tipo in tut_vacios:
        oer, lic = problemas.get(pid, ("", ""))
        clase = "openstax" if OPENSTAX.search(oer or "") else ("vacio" if not (oer or "").strip() else "otro")
        cruce[(clase, familia(lic))] += 1
    for (clase, fam), n in sorted(cruce.items(), key=lambda kv: -kv[1]):
        print(f"{clase}\t{fam}\t{n}")

    # ---------- resumen ----------
    w = sys.stderr.write
    w(f"problemas (depth3 json)        : {len(problemas)}\n")
    w(f"archivos tutoring/ leidos      : {tut_total}\n")
    w(f"unidades de hint contadas      : {hint_total}\n")
    w(f".gif enumerados                : {len(gifs)}\n")
    w(f"errores de parseo              : {err}\n")
    w("--- A: familia del problema que posee el .gif ---\n")
    for k, v in fam_gif.most_common():
        w(f"  {k:20s} {v}\n")
    w("--- A: clase de oer del problema que posee el .gif ---\n")
    for k, v in oer_gif.most_common():
        w(f"  {k:20s} {v}\n")
    w(f"--- B: unidades con oer vacio  : {len(tut_vacios)}\n")
    tot = sum(cruce.values()) or 1
    for (clase, fam), n in sorted(cruce.items(), key=lambda kv: -kv[1]):
        w(f"  {clase:10s} {fam:18s} {n:7d}  {100.0*n/tot:5.1f}%\n")
    os_share = sum(n for (c, _f), n in cruce.items() if c == "openstax")
    w(f"--- B: cuelga de problema que cita OpenStax: {os_share}/{tot} = {100.0*os_share/tot:.1f}%\n")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
