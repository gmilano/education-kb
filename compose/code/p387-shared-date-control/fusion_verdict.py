#!/usr/bin/env python3
"""P387 — control negativo de P381: la coincidencia de FECHA no es evidencia de fusion.

`P381` (pase 117) cazo un par falso: el NOMBRE de un instrumento con la FECHA de otro.
El pase 118 encontro el caso espejo y mostro que un detector que dispare por fecha
repetida produce un FALSO POSITIVO:

  Corea del Sur  -- Framework Act en vigor          -- 2026-01-22  (real)
  Singapur/IMDA  -- marco de IA agentica publicado  -- 2026-01-22  (real)

Las dos fechas son reales: los dos instrumentos se cronometraron contra Davos.

Regla: un veredicto de FUSION exige que, para cada instrumento del par, emisor y fecha
hayan sido verificados POR SEPARADO. Sin verificacion por instrumento el veredicto es
UNVERIFIABLE, nunca FUSION.
"""
import sys

FUSION = "FUSION"
DISTINCT = "DISTINCT-INSTRUMENTS"
UNVERIFIABLE = "UNVERIFIABLE"


def verdict(a, b):
    """a, b = {'name','issuer','date','verified': bool}.

    FUSION      -> mismo instrumento con dos mitades cruzadas (mismo emisor, nombre distinto)
    DISTINCT    -> dos instrumentos distintos, aunque compartan fecha
    UNVERIFIABLE -> falta verificacion por instrumento; NO se puede afirmar fusion
    """
    if not (a.get("verified") and b.get("verified")):
        return UNVERIFIABLE
    # Dos emisores distintos => dos instrumentos distintos, comparta o no la fecha.
    if a["issuer"] != b["issuer"]:
        return DISTINCT
    # Mismo emisor y mismo nombre => es el mismo instrumento, no hay par.
    if a["name"] == b["name"]:
        return DISTINCT
    # Mismo emisor, nombres distintos, MISMA fecha => mitades cruzadas.
    return FUSION if a["date"] == b["date"] else DISTINCT


def main(argv):
    import json
    pairs = json.load(open(argv[0], encoding="utf-8")) if argv else []
    print("a\tb\tveredicto")
    for a, b in pairs:
        print(f"{a['name']}\t{b['name']}\t{verdict(a, b)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
