#!/usr/bin/env python3
"""
P322 — la licencia de un item de contenido es un CAMPO, y un campo se puede llenar MAL.

OATutor-Content declara en su README: «All content in this repository is made available
under the Creative Commons Attribution 4.0 International (CC BY 4.0) license», y acto
seguido: «Attribution is given within each json file».  Son DOS afirmaciones, y la segunda
puede falsificar a la primera, porque el campo por item existe y se puede llenar con
cualquier cosa.

Defectos que este clasificador existe para no cometer (familia P171 — un regex que matchea
UNA serializacion reporta ausencia para las otras; y P314 — un puntero no es una cesion):

  D1 `license` VACIA no es CC BY.  Un string vacio es ausencia de cesion por item, y
     contarlo como «hereda el README» es asumir lo que hay que medir.
  D2 `license` con una URL que NO es de licencia es el caso peor: parece lleno, pasa
     cualquier compuerta que pregunte «hay algo?», y no cede nada.  Especimen medido:
     un PDF de solucionario de examen de un curso.
  D3 `license == oer` delata el mecanismo: el autor copio la URL de PROCEDENCIA al campo
     de CESION.  Es un puntero a la fuente, no un permiso del titular.
  D4 el nombre de archivo no es dato.  `.../a95836f13.1driverslicense.json` contiene la
     subcadena «license» y es un problema sobre una licencia de conducir.  Un barrido que
     grepea rutas lo cuenta como archivo de licencia: este clasificador lee el CAMPO.
"""
import re

CC_BY_4 = re.compile(r'creativecommons\.org/licenses/by/4\.0', re.I)
CC_ANY  = re.compile(r'creativecommons\.org/licenses/([a-z\-]+)/([0-9.]+)', re.I)
URLISH  = re.compile(r'https?://', re.I)
# Nombres de familia OSI/CC escritos como texto, sin URL.
NAMED   = re.compile(r'\b(CC[ \-]?BY(?:[ \-]?(?:NC|SA|ND)){0,2}|MIT|Apache|BSD|GPL|public domain|CC0)\b', re.I)


def classify(item):
    """item: dict del json de problema. Devuelve (clase, detalle)."""
    if not isinstance(item, dict):
        return ('AUSENTE', 'no es un objeto')
    if 'license' not in item:
        return ('AUSENTE', 'sin campo license')
    raw = item.get('license')
    if raw is None:
        return ('AUSENTE', 'license=null')
    s = str(raw).strip()
    if s == '':
        return ('VACIA', '')                                   # D1
    oer = str(item.get('oer') or '').strip()

    m = CC_ANY.search(s)
    if m:
        if CC_BY_4.search(s):
            return ('CC-BY-4.0', s[:80])
        return ('OTRA-CC', f'{m.group(1).lower()}-{m.group(2)}')

    if URLISH.search(s):
        # D2/D3: una URL que no es de licencia.  Si ademas coincide con `oer`, el
        # mecanismo esta a la vista: se copio la procedencia al campo de cesion.
        if oer and s == oer:
            return ('URL-NO-LICENCIA', f'=oer {s[:70]}')        # D3
        return ('URL-NO-LICENCIA', s[:70])                      # D2

    if NAMED.search(s):
        return ('NOMBRADA-SIN-URL', s[:60])

    return ('OTRO', s[:60])
