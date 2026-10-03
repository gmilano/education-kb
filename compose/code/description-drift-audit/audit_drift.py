#!/usr/bin/env python3
"""
description-drift-audit -- pase 63.

Mide UNA sola cosa que el pase 62 no habia separado: dentro de UN MISMO repo, la cifra de
*tools* que anuncia el campo `description` de GitHub contra la que declara el README.

Por que existe (P165). El pase 62 encontro la divergencia en una familia de FORKS y la
explico como herencia: la `description` se hereda entera y la superficie no (P160). Medido
sobre repos ORIGINALES, la divergencia aparece igual. El fork no es la causa: es una de las
maneras en que la `description` se queda vieja. La otra es que el autor la escribio una vez
y no la volvio a tocar.

Diferencia con `fork-lineage-audit` (pase 62), y es la razon de que este instrumento exista
aparte: ahi `surface()` toma el MAXIMO sobre todo el texto capturado, asi que mezcla los dos
ejes en una sola cifra -- exactamente lo que hay que separar para medir la deriva.

El control que manda (P126/P151): cuando falta una de las dos cifras, la deriva es None y
NO es 0. Un 0 se lee como «coinciden»; es el error de P151 -- una salida implausible que
entra a un diff sin que nadie la mire.

No hace red: recibe texto ya capturado, igual que el instrumento del pase 62.
"""
import re

TOOLS_RE = re.compile(r'(?:up\s+to\s+)?(\d{1,4})\s*\+?\s*tools\b', re.IGNORECASE)


def _tools(text):
    """La MAYOR cifra de *tools* declarada en un trozo de texto, o None."""
    if not text:
        return None
    vals = [int(x) for x in TOOLS_RE.findall(text)]
    return max(vals) if vals else None


def split_capture(page_text):
    """Separa la captura en (description, readme).

    Convencion de captura de esta KB (heredada del pase 62): linea 1 = `owner/repo`,
    linea 2 = `forked from ...` si lo hay, la PRIMERA linea no vacia siguiente = la
    `description` de GitHub, y el resto = README. Se devuelve (None, ...) cuando el repo
    no tiene descripcion, que es un caso real y no un error de captura.
    """
    if not page_text:
        return None, None
    lines = [ln.strip() for ln in page_text.splitlines()]
    body, desc = [], None
    for ln in lines[1:]:
        if not ln or ln.lower().startswith('forked from'):
            continue
        if desc is None:
            if ln.upper().startswith('NO DESCRIPTION'):
                desc = ''          # explicitamente sin descripcion
            else:
                desc = ln
            continue
        body.append(ln)
    return desc, '\n'.join(body)


def audit(name, page_text):
    desc, readme = split_capture(page_text)
    d_tools, r_tools = _tools(desc), _tools(readme)
    return {
        'repo': name,
        'description_tools': d_tools,
        'readme_tools': r_tools,
        'drift': drift(d_tools, r_tools),
        'searchable': bool(desc),   # sin descripcion, un barrido por busqueda no lo ve
    }


def drift(description_tools, readme_tools):
    """README menos description. None si falta cualquiera de las dos: NO 0."""
    if description_tools is None or readme_tools is None:
        return None
    return readme_tools - description_tools


if __name__ == '__main__':
    import sys, json, io
    out = []
    for path in sys.argv[1:]:
        with io.open(path, encoding='utf-8') as f:
            out.append(audit(path, f.read()))
    print(json.dumps(out, indent=2, ensure_ascii=False))
