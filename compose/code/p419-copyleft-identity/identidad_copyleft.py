#!/usr/bin/env python3
"""Identidad de una cesion COPYLEFT, leida del ENCABEZADO y no del cuerpo.

🆕 `P419` — pase 124 del 2026-10-05.

EL DEFECTO, MEDIDO 2 DE 2
-------------------------
La compuerta del pase 123 (`p411-cession-identity-gate`) clasifica por palabra clave
sobre el cuerpo del documento. Sobre los dos textos copyleft PRISTINOS que midio el
pase 124 se equivoco en los dos:

    ahmedEid1/lumen                     -> devolvio AGPL-3.0, y es GPL-3.0
    xiaochong0302/course-tencent-cloud  -> devolvio LGPL,      y es GPL-2.0

La causa es la misma en los dos casos y no es un bug de regex: **un texto de licencia
pristino NOMBRA a sus parientes**. GPL-3.0 trae la seccion «Use with the GNU Affero
General Public License» (§13); GPL-2.0 cierra nombrando a la «Lesser General Public
License». Un clasificador que busca `affero` o `lesser` en el cuerpo lee la MENCION como
el NOMBRE.

🔴 Por que pesa mas que un error de etiqueta: GPL-3.0 y AGPL-3.0 se diferencian **solo**
en el uso EN RED. Una fila que dice AGPL sobre software GPL le prohibe a un cliente un
despliegue hospedado que en realidad tiene permitido; al reves, le habilita uno que no.
Es la unica columna que decide la entrega.

LA REGLA
--------
La familia se lee del ENCABEZADO: nombre + `Version N`, en las primeras lineas no vacias.
El cuerpo sirve para confirmar, nunca para nombrar. Y el TAMANO no identifica (`P420`):
tres AGPL-3.0 de este corpus miden 34.523 B exactos con digests distintos.
"""
import hashlib
import re
import sys

# (familia, bytes del texto pristino) — el tamano es DELATOR, no identificador (`P420`)
PRISTINOS = {
    'GPL-3.0': 35149,
    'AGPL-3.0': 34523,
    'GPL-2.0': 18046,
    'LGPL-3.0': 7651,
    'Apache-2.0': 11357,
}


def _encabezado(texto, n=2):
    """Primeras n lineas NO VACIAS, normalizadas.

    🔴 `n=2` y NO MAS, y el numero esta medido, no elegido: el encabezado de una licencia
    es TITULO + `Version N`, dos lineas. La primera version de este instrumento usaba
    `n=6` y su propia suite la refuto — con una ventana de 6 lineas, la seccion §13 de
    GPL-3.0 («Use with the GNU Affero General Public License») entra en la ventana y el
    instrumento vuelve a cometer el error de `P419` que vino a arreglar. Una ventana mas
    ancha que el encabezado admite CUERPO, y el cuerpo nombra parientes.

    El encabezado puede venir centrado con relleno, asi que se colapsa el espacio."""
    lineas = [re.sub(r'\s+', ' ', l).strip() for l in texto.splitlines()]
    return ' / '.join([l for l in lineas if l][:n]).lower()


def familia(texto):
    """Devuelve (familia, evidencia). Lee el ENCABEZADO; el cuerpo no nombra."""
    enc = _encabezado(texto)

    # El orden importa: AFFERO y LESSER son mas especificos que GENERAL PUBLIC LICENSE,
    # y hay que probarlos ANTES, pero solo en el ENCABEZADO.
    if 'affero general public license' in enc:
        ver = '3.0' if 'version 3' in enc else '?'
        return f'AGPL-{ver}', 'encabezado nombra AFFERO'
    if 'lesser general public license' in enc:
        ver = '3.0' if 'version 3' in enc else ('2.1' if 'version 2.1' in enc else '?')
        return f'LGPL-{ver}', 'encabezado nombra LESSER'
    if 'general public license' in enc:
        if 'version 3' in enc:
            return 'GPL-3.0', 'encabezado: GENERAL PUBLIC LICENSE + Version 3'
        if 'version 2' in enc:
            return 'GPL-2.0', 'encabezado: GENERAL PUBLIC LICENSE + Version 2'
        return 'GPL-?', 'encabezado nombra GPL SIN version — no se infiere (`P286`)'
    if 'apache license' in enc:
        return 'Apache-2.0', 'encabezado: APACHE LICENSE'
    if 'mit license' in enc:
        return 'MIT', 'encabezado: MIT LICENSE'
    return 'UNCLASSIFIED', 'el encabezado no nombra una familia — tratar como NO-OSI (`P412`)'


def menciones_cruzadas(texto):
    """Las familias que el CUERPO nombra y el encabezado no. Son parentesco, no identidad:
    es exactamente el dato que hizo fallar a la compuerta del pase 123."""
    enc = _encabezado(texto)
    cuerpo = texto.lower()
    out = []
    for aguja, nombre in (('affero', 'AGPL'), ('lesser general public', 'LGPL')):
        if aguja in cuerpo and aguja not in enc:
            out.append(nombre)
    return out


def analizar(raw_bytes):
    texto = raw_bytes.decode('utf-8', 'replace')
    fam, ev = familia(texto)
    n = len(raw_bytes)
    pristino = PRISTINOS.get(fam)
    return {
        'bytes': n,
        'sha256': hashlib.sha256(raw_bytes).hexdigest()[:12],
        'familia': fam,
        'evidencia': ev,
        'cruzadas': menciones_cruzadas(texto),
        # `P420`: coincidir con el tamano pristino NO confirma identidad, solo es consistente
        'tamano_consistente': (pristino == n) if pristino else None,
        # el uso en red es la columna que decide una entrega hospedada
        'alcanza_uso_en_red': fam.startswith('AGPL'),
    }


if __name__ == '__main__':
    for ruta in sys.argv[1:]:
        with open(ruta, 'rb') as fh:
            r = analizar(fh.read())
        cruz = f" | cuerpo menciona {','.join(r['cruzadas'])}" if r['cruzadas'] else ''
        print(f"{ruta.split('/')[-1]:38s} {r['bytes']:6d}B sha:{r['sha256']} "
              f"{r['familia']:12s} red={'SI' if r['alcanza_uso_en_red'] else 'NO'} "
              f"| {r['evidencia']}{cruz}")
