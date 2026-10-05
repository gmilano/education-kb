#!/usr/bin/env python3
"""Compuerta de IDENTIDAD de cesion — pase 123 del 2026-10-05.

Tres defectos distintos, medidos este pase, que un clasificador por palabra clave no ve:

🆕 `P411` — la FRASE DE CONCESION no es la IDENTIDAD. `CaviraOSS/PageLM` abre su
   `LICENSE.md` con la concesion MIT **literal** («Permission is hereby granted, free of
   charge, to any person obtaining a copy…») y sigue con un documento titulado *«PageLM
   Community License»* que PROHIBE el uso comercial y exige reparto de ingresos. Un
   clasificador anclado en la frase devuelve `MIT` para una licencia que prohibe
   exactamente lo que este estante existe para habilitar. El delator es el TAMANO:
   8.562 B contra el piso de ~1.070 B de un MIT real.

🆕 `P412` — el balde `UNCLASSIFIED` no es ausencia: es SENAL. Las dos unicas filas que
   cayeron ahi este pase son licencias *source-available* NO-OSI: `Elastic License 2.0`
   (`canyongbs/advisingapp`) y *«Fair code License»* (`leemonade/leemons`). Las dos
   prohiben ofrecer el software como servicio gestionado, que es la forma en que una
   consultora lo entregaria.

🆕 `P414` — hay TRES sub-clases bajo el piso de tamano, y no una:
   - 0 B      -> el archivo existe y no cede nada (`P404`, `studyAlpha`)
   - ~3 B     -> campo `license` de metadata de paquete, no archivo de cesion (`educhain`)
   - ~19 B    -> el archivo entero dice `License: GNU GPL V3`: es un NOMBRAMIENTO, no una
                 cesion. Nombrar una licencia no es otorgarla (`frappe/education`).

La compuerta decide con TRES senales, en este orden: tamano, TITULO, y la seccion de
limitaciones. Nunca con la frase de concesion sola.
"""
import hashlib, re, sys

PISO_DE_CESION = 200          # debajo de esto no hay texto de licencia posible
PISO_MIT = 900                # un MIT real mide ~1.040-1.150 B

# titulos que declaran una licencia NO-OSI, aunque el cuerpo cite frases permisivas
TITULOS_NO_OSI = (
    'community license', 'elastic license', 'fair code', 'fair-code',
    'business source', 'bsl', 'commons clause', 'proprietary', 'all rights reserved',
    'sustainable use license', 'server side public license',
)
# limitaciones que vuelven el software inservible para una entrega gestionada
LIMITACIONES_FATALES = (
    'non-commercial', 'noncommercial', 'revenue-sharing', 'revenue sharing',
    'may not provide the software to third parties as a hosted or managed service',
    'not be sold, sublicensed', 'prior written consent',
)
PLACEHOLDERS = ('<name of author>', '[name of copyright owner]', '<year>', '[yyyy]')


def clasificar(texto: str) -> dict:
    """Devuelve el veredicto de la compuerta para el PAYLOAD de un archivo de cesion."""
    bytes_ = len(texto.encode('utf-8'))
    sha = hashlib.sha256(texto.encode('utf-8')).hexdigest()[:12]
    bajo = texto.lower()
    v = {'bytes': bytes_, 'sha256': sha, 'familia': None, 'usable': False, 'motivo': ''}

    # 1 — TAMANO (`P404`/`P414`): tres sub-clases distintas, cada una con su nombre
    if bytes_ == 0:
        v.update(familia='SIN-CESION', motivo='P404: archivo existe y mide 0 B')
        return v
    if bytes_ < 10:
        v.update(familia='SIN-CESION', motivo=f'P414: {bytes_} B — campo de metadata, no cesion')
        return v
    if bytes_ < PISO_DE_CESION:
        v.update(familia='NOMBRAMIENTO',
                 motivo=f'P414: {bytes_} B — NOMBRA una licencia, no la otorga')
        return v

    # 2 — TITULO (`P411`/`P412`): manda sobre cualquier frase del cuerpo
    primeras = '\n'.join(texto.splitlines()[:6]).lower()
    for t in TITULOS_NO_OSI:
        if t in primeras:
            v.update(familia=f'NO-OSI ({t})',
                     motivo=f'P411/P412: el titulo declara «{t}» — la frase de concesion no decide')
            return v

    # 3 — LIMITACIONES: una concesion permisiva no las tiene
    fatales = [l for l in LIMITACIONES_FATALES if l in bajo]

    if 'apache license' in bajo:
        v['familia'] = 'Apache-2.0'
    elif 'gnu affero' in bajo:
        v['familia'] = 'AGPL-3.0'
    elif 'gnu lesser' in bajo:
        v['familia'] = 'LGPL'
    elif 'gnu general public' in bajo:
        v['familia'] = 'GPL'
    elif 'mozilla public' in bajo:
        v['familia'] = 'MPL-2.0'
    elif 'redistributions of source code' in bajo:
        v['familia'] = 'BSD'
    elif 'permission is hereby granted, free of charge' in bajo:
        # `P411`: la frase MIT con tamano de MIT es MIT; con tamano de tratado, no lo es
        if bytes_ > PISO_MIT * 3:
            v.update(familia='NO-OSI (frase MIT en documento largo)',
                     motivo=f'P411: {bytes_} B con la frase MIT — el cuerpo agrega terminos')
            return v
        v['familia'] = 'MIT'
    else:
        v.update(familia='UNCLASSIFIED',
                 motivo='P412: sin familia OSI reconocible — tratar como NO-OSI hasta leerla')
        return v

    if fatales:
        v.update(motivo=f'P411: familia {v["familia"]} con limitaciones fatales: {fatales[:2]}')
        return v

    v['usable'] = v['familia'] in ('MIT', 'Apache-2.0', 'BSD')
    titular = next((l.strip() for l in texto.splitlines()
                    if re.search(r'copyright (\(c\)|©|[0-9])', l, re.I)), '')
    if any(p in titular for p in PLACEHOLDERS):
        v['motivo'] = 'P403: el titular leido es el PLACEHOLDER del apendice, no un titular'
    elif titular:
        v['motivo'] = f'titular: {titular[:60]}'
    return v


if __name__ == '__main__':
    texto = sys.stdin.read()
    r = clasificar(texto)
    print(f"familia={r['familia']}  usable={'SI' if r['usable'] else 'NO'}  "
          f"{r['bytes']} B  sha256:{r['sha256']}\n  {r['motivo']}")
