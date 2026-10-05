#!/usr/bin/env python3
"""Accion C del pase 107 — `P329` contra esta base.

Barre los `.md` del arbol buscando toda afirmacion de IDENTIDAD DE LICENCIA que se
apoye en un `sha256` (crudo o normalizado) SIN nombrar la familia al lado.

Regla (falsable, escrita antes de correrla):
  una linea es una AFIRMACION-SHA-SIN-FAMILIA si y solo si
    (a) contiene una huella: el token `sha256`/`sha-256` o >=16 hex seguidos, Y
    (b) contiene un verbo de identidad de licencia, Y
    (c) NO nombra ninguna familia de licencia en la MISMA linea.
El control negativo esta adentro: una linea con huella + verbo + familia es
exactamente la forma CORRECTA y debe salir de la clase (b)+(c).

Uso: python3 sweep_sha_claims.py [raiz]
Codigo 0 siempre; el veredicto lo da el conteo impreso.
"""
import os
import re
import sys

HUELLA = re.compile(r"sha-?256|\b[0-9a-f]{16,}\b", re.I)
IDENT = re.compile(
    r"identic|identidad|misma licencia|mismo texto|igual(?:es)? (?:a|al|que)|"
    r"coincide|byte a byte|colaps|huella",
    re.I,
)
FAMILIA = re.compile(
    r"CC ?BY|CC0|creativecommons|MIT|Apache[- ]?2|BSD|AGPL|LGPL|GPL|MPL|"
    r"EPL|Unlicense|NC-SA|NC-ND|BY-SA|BY-ND|propietar|SustainableUse|"
    r"SIN-DECLARAR|NO-RESUELVE|NO-CLAIM|familia",
    re.I,
)

def main(root="."):
    con_familia = 0
    sin_familia = []
    archivos = 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            archivos += 1
            p = os.path.join(dp, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                for i, line in enumerate(fh, 1):
                    if not HUELLA.search(line) or not IDENT.search(line):
                        continue
                    if FAMILIA.search(line):
                        con_familia += 1
                    else:
                        sin_familia.append((p, i, line.strip()))
    print(f"archivos .md barridos                               : {archivos}")
    print(f"lineas con huella + verbo de identidad + FAMILIA     : {con_familia}   (forma CORRECTA)")
    print(f"lineas con huella + verbo de identidad SIN familia   : {len(sin_familia)}   (la clase de `P329`)")
    for p, i, line in sin_familia:
        print(f"  {p}:{i}  {line[:190]}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
