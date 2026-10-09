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

-----------------------------------------------------------------------------------------
PASE 47 DEL 2026-10-08 — LA COMPUERTA YA NO CLASIFICA LA FAMILIA. LA DELEGA.

El pase 46 declaro abierto que este archivo «todavia inlinea un clasificador de licencias
y todavia carga `P561`». Medido este pase sobre los 29 payloads REALES del arbol, la
escalera inlineada divergia del clasificador endurecido en **18 de 29**. No era una
discrepancia de estilo: ocho clases de respuesta equivocada, y dos de ellas RECHAZAN
software usable.

  `P571`  GPL-3.0 -> AGPL-3.0.  `P171` VERBATIM, en el sexto instrumento. La seccion 13 de
          GPL-3.0 se titula «Use with the GNU Affero General Public License», asi que
          `'gnu affero' in bajo` (el CUERPO entero) marca todo GPL-3.0 como AGPL-3.0.
          Medido sobre el `COPYING` de **Moodle**: la plataforma insignia de esta KB.
  `P572`  GPL-2.0 -> LGPL.  El parrafo de cierre de GPL-2.0 dice «use the GNU Lesser
          General Public License instead of this License», y la rama `gnu lesser` va antes
          que `gnu general public`. Medido sobre `OpenEMIS/core`.
  `P573`  MPL-2.0 -> AGPL-3.0.  `P454`: la seccion 1.12 de MPL-2.0 DEFINE «Secondary
          License» nombrando GPL-2.0, LGPL-2.1 y AGPL-3.0, asi que todo payload MPL-2.0
          trae las tres marcas GNU. Un copyleft debil se lee como el copyleft de red mas
          fuerte que existe: el error en la direccion mas cara.
  `P574`  EPL-2.0 -> GPL.  La misma trampa de «Secondary Licenses». Medido sobre
          `hcengineering/platform` (Huly, que el canal vertical publica) y `eclipse-ee4j/jersey`.
  `P575`  MPL-1.1 -> MPL-2.0.  `P561` VERBATIM: `'mozilla public' in bajo` ESTAMPABA la
          version. Declarado abierto por el pase 46; aqui queda medido y cerrado.
  `P576`  ECL-2.0 -> NO-OSI.  🔴 **FALSO RECHAZO.** El disparador `'community license'`
          existe por `PageLM`, pero la **Educational Community License** —aprobada por la
          OSI, Apache-2.0 mas clausula de patentes— lo contiene como SUBCADENA. La
          compuerta rechazaba **Sakai** por el nombre de su licencia.
  `P577`  BSD-3 -> NO-OSI.  🔴 **FALSO RECHAZO.** El disparador `'all rights reserved'`
          es, en BSD y MIT, parte del ENCABEZADO DE COPYRIGHT convencional
          («Copyright (c) 2022, Yuan Gong / All rights reserved.»). La compuerta leia la
          convencion de BSD como una declaracion propietaria.
  `P578`  dual MPL-2.0-or-EPL-1.0 -> AGPL-3.0. Los DOS brazos perdidos (`Gap 249` sigue
          abierto: el clasificador compartido reporta el brazo MPL).
  `P579`  Unlicense -> usable=NO.  🔴 **TERCER FALSO RECHAZO, y lo encontro esta suite al
          exigir un corpus real.** `LIMITACIONES_FATALES` contiene la SUBCADENA
          `'non-commercial'`, y el texto del Unlicense —la licencia mas permisiva que
          existe— dice «for any purpose, commercial or non-commercial». La enumeracion
          que CONCEDE se leia como la clausula que PROHIBE. Misma clase que `P576` y
          `P577`: una subcadena no distingue una concesion de una prohibicion.

🔵 **Y la razon de que sobreviviera 1 pase: el corpus de `test_gate.py` no tenia NI UN
payload copyleft, ni uno OSI que no fuera MIT.** Siete casos, todos sinteticos, todos
verdes. Una suite verde porque nunca pregunto.

🟢 **La arquitectura, y es composicion y no reemplazo:** `family_of` contesta QUE TEXTO DE
CONCESION ES ESTE; esta compuerta contesta SI EL DOCUMENTO CEDE DE VERDAD ESOS DERECHOS.
Son dos preguntas distintas con contratos opuestos, como las dos de region en `P265`. La
prueba de que no se puede delegar ciego: el clasificador compartido lee `PageLM` como
**MIT**, que es exactamente el payload que `P411` existe para atrapar. Asi que la familia
se delega y la compuerta de TITULO se conserva — estrechada, porque un disparador NO-OSI
no puede invalidar un texto de concesion que el clasificador endurecido reconoce, salvo
que el documento traiga limitaciones fatales.
"""
import hashlib, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, '..', 'lib', 'license_family.sh')

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

# `P579`: fraseos en los que la limitacion aparece para CONCEDERSE, no para prohibirse.
# Se borran del texto ANTES de buscar limitaciones fatales. El Unlicense es el caso que
# lo destapo: «for any purpose, commercial or non-commercial».
FRASEOS_DE_CONCESION = (
    'commercial or non-commercial', 'commercial or noncommercial',
    'non-commercial or commercial', 'noncommercial or commercial',
    'commercial and non-commercial', 'commercial and noncommercial',
)

# `P576`: nombres OSI cuyo TITULO contiene un disparador NO-OSI como SUBCADENA. Sin esta
# exencion, la Educational Community License de Sakai se rechaza por su propio nombre.
TITULOS_OSI_EXENTOS = ('educational community license',)

# El vocabulario que `lib/license_family.sh::family_of` puede emitir, partido en las dos
# preguntas que esta compuerta necesita. NO se re-clasifica nada aqui: solo se interpreta.
OSI_RECONOCIDAS = frozenset({
    '0BSD', 'AGPL-3.0', 'Apache-2.0', 'BSD', 'ECL-2.0', 'EPL-1.0', 'EPL-2.0',
    # `P613`: `GPL-UNVERSIONED` se agrega aqui porque la rama GNU del clasificador dejo de
    # adivinar GPL-2.0 cuando el payload no nombra version. Es `P562`: la correccion viaja
    # al consumidor, o el gate rechaza por desconocido un string que su propia libreria emite.
    'EPL-UNVERSIONED', 'EUPL', 'EUPL-1.1', 'EUPL-1.2', 'GPL-2.0', 'GPL-3.0',
    'GPL-UNVERSIONED', 'ISC',
    # `Gap 256` cerrado en el pase 53: la rama LGPL del clasificador compartido ya LEE la
    # version, asi que puede emitir `LGPL-2.1`. Se agrega aca por `P562` --la correccion
    # viaja al consumidor-- o esta compuerta rechazaria por desconocido un string que su
    # propia libreria produce. Es el mismo movimiento que `P613` hizo con `GPL-UNVERSIONED`.
    'LGPL', 'LGPL-2.1', 'LGPL-3.0', 'MIT', 'MPL-1.0', 'MPL-1.1', 'MPL-2.0',
    'MPL-UNVERSIONED',
    # `P845` (pase 76): la rama PSF del clasificador compartido se agrego porque el LICENSE
    # de Python es un documento COMPUESTO y la rama 0BSD se lo quedaba (ver
    # `lib/license_family.sh`). Se agrega aca por `P562` --la correccion viaja al
    # consumidor-- igual que `GPL-UNVERSIONED` (`P613`) y `LGPL-2.1` (`Gap 256`).
    # PSF-2.0 ES aprobada por la OSI.
    'PSF-2.0',
    'Unlicense',
})
# Permisivas = las que esta base puede construir encima sin obligacion reciproca.
# ECL-2.0 entra porque ES Apache-2.0 mas una clausula de patentes (`P576`).
#
# `P845`: PSF-2.0 entra porque NO es reciproca --no obliga a publicar el derivado-- pero
# entra CON una condicion que MIT no tiene y que el entregable debe cumplir: la seccion 2
# pide reproducir el aviso de copyright de la PSF Y «a brief summary of the changes made».
# Un closure que la contiene es construible; su archivo de avisos tiene una fila mas.
PERMISIVAS = frozenset({
    'MIT', 'Apache-2.0', 'BSD', '0BSD', 'ISC', 'Unlicense', 'ECL-2.0', 'CC0-1.0',
    'PSF-2.0',
})
# Familias NOMBRADAS que no son OSI: se reportan por su nombre, no como UNCLASSIFIED.
# `P412` se conserva —el balde es senal— pero una senal con nombre vale mas.
NO_OSI_NOMBRADAS = ('Elastic', 'BUSL', 'PolyForm', 'NONCOMMERCIAL-NOT-OSI', 'CC-')

# `P445`: el payload va por STDIN y no por argv — varios de estos pasan los 35 kB y una
# lista de argv tiene limite duro, asi que el texto se truncaria en silencio y el fallo
# parecerIa un desacuerdo de clasificadores y no una falla de plomeria.
_PUENTE = '. "$1"\nT=$(cat)\nprintf "%s" "$(family_of "$T")"\n'


class SinClasificador(RuntimeError):
    """El clasificador compartido no esta disponible.

    `P197`: esto se LEVANTA, no se degrada a una escalera inlineada. Una correccion
    sobrevive solo si el instrumento que re-mide la conoce; un fallback silencioso
    re-importa los ocho defectos que este pase acaba de pagar.
    """


def familia_compartida(texto: str, lib: str = LIB) -> str:
    """La FAMILIA, de `lib/license_family.sh::family_of`. No se clasifica aqui."""
    if not os.path.exists(lib):
        raise SinClasificador(f'no existe {lib}')
    try:
        p = subprocess.run(['sh', '-c', _PUENTE, 'sh', lib], input=texto,
                           capture_output=True, text=True, timeout=60)
    except Exception as e:                                   # noqa: BLE001
        raise SinClasificador(str(e)) from e
    fam = (p.stdout or '').strip()
    if not fam:
        raise SinClasificador(f'respuesta vacia (exit {p.returncode})')
    return fam


def clasificar(texto: str, lib: str = LIB) -> dict:
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

    # 2 — FAMILIA: delegada al clasificador endurecido (`P571`..`P578`). Va ANTES de la
    # compuerta de titulo porque la compuerta necesita su respuesta para no rechazar un
    # texto de concesion real (`P576`/`P577`).
    fam = familia_compartida(texto, lib)
    v['familia_compartida'] = fam
    base = fam.split(' (')[0]
    declaracion = fam.endswith('(declaracion)')
    reconocida = base in OSI_RECONOCIDAS

    # 3 — LIMITACIONES: una concesion permisiva no las tiene. `P579`: se descuentan
    # primero los fraseos en los que la limitacion se CONCEDE en vez de prohibirse.
    prohibitivo = bajo
    for frase in FRASEOS_DE_CONCESION:
        prohibitivo = prohibitivo.replace(frase, ' ')
    fatales = [l for l in LIMITACIONES_FATALES if l in prohibitivo]

    # 4 — TITULO (`P411`/`P412`), ESTRECHADA. Un disparador NO-OSI ya no invalida por si
    # solo un texto que el clasificador reconoce: hace falta que NO sea reconocido o que
    # el documento traiga limitaciones fatales. Sin esto, `P576` rechaza Sakai por el
    # nombre «Educational Community License» y `P577` rechaza BSD por su encabezado.
    primeras = '\n'.join(texto.splitlines()[:6]).lower()
    exento = any(n in primeras for n in TITULOS_OSI_EXENTOS)
    disparador = next((t for t in TITULOS_NO_OSI if t in primeras), None)
    if disparador and not exento and (not reconocida or fatales):
        motivo = f'P411/P412: el titulo declara «{disparador}» — la frase de concesion no decide'
        if reconocida and fatales:
            motivo = (f'P411: el titulo declara «{disparador}» y el cuerpo trae '
                      f'{fatales[:2]} — {base} nombrado, no cedido')
        v.update(familia=f'NO-OSI ({disparador})', motivo=motivo)
        return v

    # 5 — la familia delegada, interpretada
    if not reconocida:
        if any(fam.startswith(n) for n in NO_OSI_NOMBRADAS):
            v.update(familia=f'NO-OSI ({fam})',
                     motivo=f'P412: {fam} es una familia NOMBRADA que no es OSI')
            return v
        v.update(familia='UNCLASSIFIED',
                 motivo='P412: sin familia OSI reconocible — tratar como NO-OSI hasta leerla')
        return v

    v['familia'] = base
    if declaracion:
        v.update(motivo=f'P414: el payload NOMBRA {base}, no lo otorga — nombrar no es ceder')
        return v

    # `P411`: la frase MIT con tamano de MIT es MIT; con tamano de tratado, no lo es.
    if base == 'MIT' and bytes_ > PISO_MIT * 3:
        v.update(familia='NO-OSI (frase MIT en documento largo)',
                 motivo=f'P411: {bytes_} B con la frase MIT — el cuerpo agrega terminos')
        return v

    if fatales:
        v.update(motivo=f'P411: familia {base} con limitaciones fatales: {fatales[:2]}')
        return v

    v['usable'] = base in PERMISIVAS
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
