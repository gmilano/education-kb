#!/usr/bin/env python3
"""P344 — detector de AFIRMACIONES de cesion en un README.

Lee el README por el canal de PAYLOAD (`raw.githubusercontent.com`), no por la
pagina renderizada. El defecto que este modulo existe para no repetir: un
detector escrito solo en sintaxis Markdown es CIEGO a los badges en HTML, y
`shields.io` se incrusta de las dos formas. Cuatro ejes, cada uno con su
control negativo en `test_p344.py`:

  badge_md    [![License](...badge/License-MIT...)](LICENSE)
  badge_html  <img src="...badge/License-MIT..." alt="License">
  tree        |-- LICENSE   /   `-- LICENSE   (entrada de arbol dibujado)
  prose       "licensed under the **MIT** License"  (con o sin marcas de enfasis)
"""
import re

# --- badges -----------------------------------------------------------------
# shields.io codifica la licencia en la RUTA del badge: /badge/License-MIT-green.svg
_SHIELD = re.compile(r'shields\.io/[^"\')\s]*badge/[^"\')\s]*[Ll]icen[sc]e[^"\')\s]*', re.I)
# badge markdown enlazado: el texto alt o el destino hablan de licencia
_BADGE_MD = re.compile(r'\[!\[([^\]]*)\]\(([^)]*)\)\]\(([^)]*)\)')
# badge html: <img ... src="..." ... alt="...">  (atributos en cualquier orden)
_IMG_HTML = re.compile(r'<img\b[^>]*>', re.I)
_ATTR = re.compile(r'(\w+)\s*=\s*["\']([^"\']*)["\']', re.I)

# --- arbol dibujado ---------------------------------------------------------
# U+251C BOX DRAWINGS LIGHT VERTICAL AND RIGHT, U+2514 .. UP AND RIGHT, y el ASCII
_TREE = re.compile(r'(?:├|└|│|\|--|`--|\+--)[^\n]*\bLICEN[SC]E\b', re.I)

# --- prosa ------------------------------------------------------------------
# El nombre de la licencia puede venir envuelto en **, __, ` o <strong>.
# Se tolera el envoltorio en vez de excluirlo (el defecto del pase 110).
_PROSE = re.compile(
    r'licen[sc]ed\s+under\s+(?:the\s+)?[*_`<>/a-zA-Z0-9 .\-]{2,40}?licen[sc]e',
    re.I)
_PROSE2 = re.compile(
    r'\b(?:released|distributed|available)\s+under\s+(?:the\s+)?'
    r'[*_`<>/a-zA-Z0-9 .\-]{2,40}?licen[sc]e', re.I)

# nombre de familia, para decir QUE se afirma
_FAMILY = re.compile(
    r'\b(MIT|Apache[- ]?2(?:\.0)?|BSD[- ]?[23]?(?:-Clause)?|GPL[- ]?[23]?(?:\.0)?|'
    r'AGPL[- ]?3(?:\.0)?|LGPL[- ]?[23]?(?:\.1|\.0)?|MPL[- ]?2(?:\.0)?|ECL[- ]?2(?:\.0)?|'
    r'CC0|CC[- ]BY(?:[- ]NC)?(?:[- ]SA)?(?:[- ]ND)?(?:[- ]4\.0)?|Unlicense|0BSD|ISC)\b', re.I)


def _is_path_claim(dest: str) -> bool:
    """Un destino que es RUTA relativa a un archivo de licencia es una afirmacion
    resoluble; uno que apunta a http:// es una afirmacion de OTRA clase (puede
    estar roto, como la plantilla sin editar de `SafeTutors`)."""
    d = (dest or '').strip()
    if not d:
        return False
    return bool(re.search(r'LICEN[SC]E', d, re.I))


def detect(text: str) -> dict:
    """Devuelve las afirmaciones encontradas, por eje. Nada se infiere del nombre
    del repo: todo sale del texto."""
    out = {'badge_md': [], 'badge_html': [], 'tree': [], 'prose': [], 'families': []}

    for m in _BADGE_MD.finditer(text):
        alt, src, dest = m.group(1), m.group(2), m.group(3)
        if _SHIELD.search(src) or re.search(r'licen[sc]e', alt, re.I) or _is_path_claim(dest):
            out['badge_md'].append({'alt': alt, 'src': src, 'dest': dest,
                                    'dest_is_path': _is_path_claim(dest)})

    for m in _IMG_HTML.finditer(text):
        attrs = dict((k.lower(), v) for k, v in _ATTR.findall(m.group(0)))
        src, alt = attrs.get('src', ''), attrs.get('alt', '')
        if _SHIELD.search(src) or re.search(r'licen[sc]e', alt, re.I):
            out['badge_html'].append({'alt': alt, 'src': src})

    out['tree'] = [m.group(0).strip() for m in _TREE.finditer(text)]
    out['prose'] = ([m.group(0) for m in _PROSE.finditer(text)]
                    + [m.group(0) for m in _PROSE2.finditer(text)])

    blob = ' '.join([d['src'] + ' ' + d['alt'] for d in out['badge_md']]
                    + [d['src'] + ' ' + d['alt'] for d in out['badge_html']]
                    + out['tree'] + out['prose'])
    out['families'] = sorted({m.group(0).upper().replace(' ', '-')
                              for m in _FAMILY.finditer(blob)})
    return out


def verdict(claims: dict, license_file_hits: int, readme_reachable: bool) -> str:
    """Tres cubetas, no dos (receta `R-109-CESION-RECUPERABLE`)."""
    if license_file_hits > 0:
        return 'CEDE'
    if not readme_reachable:
        return 'INALCANZABLE'
    if claims['badge_md'] or claims['badge_html'] or claims['tree']:
        return 'P342-AFIRMA-SIN-ARCHIVO'
    if claims['prose']:
        return 'P314-PROSA-SIN-ARCHIVO'
    return 'SILENCIO-CONFIRMADO'


if __name__ == '__main__':
    import json, sys
    t = sys.stdin.read()
    c = detect(t)
    print(json.dumps(c, indent=2, ensure_ascii=False))
