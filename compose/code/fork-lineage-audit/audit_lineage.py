#!/usr/bin/env python3
"""
fork-lineage-audit — pase 62.

Dado el HTML de la pagina de un repo de GitHub (guardado como evidencia), reporta:
  - lineage: el "forked from OWNER/REPO", o None si el repo es original
  - surface: la cifra de *tools* que declara el README/descripcion, o None

Por que existe (P160): el campo `description` se hereda ENTERO en un fork, mientras la
superficie real (las *tools*) diverge. Un barrido que lee descripciones sub-cuenta la
superficie; uno que cuenta repos sobre-cuenta el codigo. Este instrumento separa los dos
ejes para que ninguno se infiera del otro.

No hace red: recibe texto ya capturado. La captura y la medicion se mantienen separadas a
proposito, para que el test pueda correr sin salir a internet.
"""
import re

FORK_RE = re.compile(
    r'forked\s+from\s*'                      # el rotulo
    r'(?:<[^>]+>\s*)*'                       # markup intermedio, si lo hay
    r'\[?\s*([A-Za-z0-9._-]+/[A-Za-z0-9._-]+)',
    re.IGNORECASE,
)

# "up to 139 tools", "139 tools", "up to 102 tools and 8 agent skills"
TOOLS_RE = re.compile(r'(?:up\s+to\s+)?(\d{1,4})\s*\+?\s*tools\b', re.IGNORECASE)


def lineage(page_text):
    """Devuelve 'owner/repo' si la pagina declara un fork, si no None."""
    if not page_text:
        return None
    m = FORK_RE.search(page_text)
    return m.group(1) if m else None


def surface(page_text):
    """Devuelve la MAYOR cifra de *tools* declarada, o None.

    Se toma la mayor a proposito: los README de esta familia dicen 'up to N' en el
    encabezado y desglosan cifras menores por perfil mas abajo. La cifra que un
    integrador compara es el techo declarado.
    """
    if not page_text:
        return None
    vals = [int(x) for x in TOOLS_RE.findall(page_text)]
    return max(vals) if vals else None


def audit(name, page_text):
    return {'repo': name, 'fork_of': lineage(page_text), 'tools': surface(page_text)}


def divergence(parent_audit, fork_audit):
    """Diferencia de superficie entre madre y fork. None si falta alguna cifra."""
    a, b = parent_audit.get('tools'), fork_audit.get('tools')
    if a is None or b is None:
        return None
    return b - a


if __name__ == '__main__':
    import sys, json, io
    out = []
    for path in sys.argv[1:]:
        with io.open(path, encoding='utf-8') as f:
            out.append(audit(path, f.read()))
    print(json.dumps(out, indent=2, ensure_ascii=False))
