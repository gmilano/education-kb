#!/usr/bin/env python3
"""Auditoria de una AFIRMACION DE CESION de segunda mano contra la lectura de primera mano.

🆕 `P429` — pase 125 del 2026-10-05 (lectura `22:50Z`).

EL DEFECTO, MEDIDO 4 DE 4 CONTRA UNA SOLA FUENTE
------------------------------------------------
El canal de plataformas de este estante (`open source platform education ...`) devuelve
listicles del tipo «Best Open Source LMS 2026». Esos articulos traen una COLUMNA DE
LICENCIA, y esa columna es exactamente el dato que una propuesta copia. El pase 125 la
midio entera contra el sidebar de GitHub, 4 afirmaciones de un mismo articulo:

    Sakai      -> afirmo ECL-2.0            y es ECL-2.0     🟢 acierto
    Chamilo    -> afirmo GPL v3             y es GPL-3.0     🟢 acierto
    Forma LMS  -> afirmo «Apache 2.0, la    y NO TIENE       🔴 refutada
                  mas permisiva de esta        campo de
                  comparacion»                 licencia
    Open edX   -> «free, open-source»,      y es AGPL-3.0    🔴 omitida
                  sin nombrar la cesion

2 de 4. Pero el reparto NO es aleatorio, y eso es el hallazgo:

🔴 **Las 2 que el articulo acierta son las 2 donde la licencia no cambia la entrega.**
🔴 **Las 2 que falla son las 2 donde SI la cambia** — `Forma LMS` presentado como «la mas
permisiva» cuando no cede NADA (sin archivo de licencia = todos los derechos
reservados), y `Open edX` recomendado para escala empresarial sin decir que es AGPL-3.0,
que es la clausula de USO EN RED.

Es el hermano de `P419` por el otro lado: `P419` dice que la identidad de un copyleft no
se lee de las licencias que CITA; `P429` dice que no se lee de quien lo RECOMIENDA. En los
dos casos el eje corrompido es el mismo — el uso en red — y es el unico que decide si un
despliegue hospedado es legal.

LA REGLA
--------
Una afirmacion de cesion de segunda mano no se publica como dato. Se publica como
CANDIDATA, y se clasifica por el RIESGO DE ENTREGA de su discrepancia, que no es el
tamano del error sino QUE DECISION cambia:

    BLOQUEANTE   la discrepancia cambia si se puede usar la pieza (sin cesion, o no-OSI)
    HOSPEDAJE    la discrepancia cambia si el despliegue HOSPEDADO es legal (AGPL <-> otra)
    COSMETICA    la discrepancia no cambia ninguna de las dos
"""
import sys

# Familias que obligan a abrir el codigo cuando el software se ofrece POR RED.
# Es la unica distincion que mueve un despliegue SaaS, y la que `P419` aisla.
RED = {'AGPL-3.0', 'AGPL-1.0', 'SSPL', 'OSL-3.0'}

# Copyleft de distribucion: obliga al distribuir binario/fuente, no por red.
COPYLEFT = {'GPL-2.0', 'GPL-3.0', 'LGPL-2.1', 'LGPL-3.0', 'MPL-2.0', 'EPL-2.0'}

PERMISIVA = {'MIT', 'Apache-2.0', 'BSD-2-Clause', 'BSD-3-Clause', 'ECL-2.0', 'ISC'}

# `SIN_CESION` no es «desconocida»: un repo sin archivo de licencia NO cede nada.
SIN_CESION = {'NINGUNA', 'SIN-LICENCIA', None, ''}


def _clase(fam):
    if fam in SIN_CESION:
        return 'SIN_CESION'
    if fam in RED:
        return 'RED'
    if fam in COPYLEFT:
        return 'COPYLEFT'
    if fam in PERMISIVA:
        return 'PERMISIVA'
    return 'NO_CLASIFICADA'


def riesgo(afirmada, primera_mano):
    """Clasifica el RIESGO DE ENTREGA de la discrepancia entre lo afirmado y lo medido.

    Devuelve (veredicto, riesgo, motivo). `afirmada=None` modela la OMISION, que es un
    modo de falla propio y no un acierto: `Open edX` no dijo nada falso sobre su licencia,
    y una propuesta que lo lea igual se lleva un AGPL sin saberlo.
    """
    ca, cp = _clase(afirmada), _clase(primera_mano)

    if afirmada is None:
        # No afirmo nada. Solo es inocuo si lo medido tampoco mueve la entrega.
        if cp in ('RED', 'SIN_CESION'):
            return ('OMITIDA', 'HOSPEDAJE' if cp == 'RED' else 'BLOQUEANTE',
                    f'no nombro la cesion y lo medido es {primera_mano} ({cp})')
        return ('OMITIDA', 'COSMETICA', 'no nombro la cesion y lo medido no mueve la entrega')

    if afirmada == primera_mano:
        return ('ACIERTO', 'COSMETICA', 'la afirmacion coincide con el payload')

    # Hay discrepancia. El riesgo se lee del PAR, no del error.
    #
    # 🔴 La comparacion de uso-en-red es CLASE contra CLASE (`ca`/`cp`), no clase contra
    # el conjunto de FAMILIAS. La v1 de este instrumento escribio `cp in RED` con `cp` ya
    # convertida a clase: `'RED' in {'AGPL-3.0', ...}` es siempre False, asi que la rama
    # NO disparaba nunca por el lado medido. Su suite paso 12/12 igual, porque una rama
    # posterior devolvia el veredicto correcto por el motivo equivocado ⇒ `P430`.
    if cp == 'SIN_CESION':
        return ('REFUTADA', 'BLOQUEANTE',
                f'se afirmo {afirmada} y el repo no declara cesion: no se puede usar')
    if ca == 'SIN_CESION':
        return ('REFUTADA', 'COSMETICA',
                f'se afirmo sin cesion y el repo cede {primera_mano}: el error favorece al cliente')
    if (cp == 'RED') != (ca == 'RED'):
        return ('REFUTADA', 'HOSPEDAJE',
                f'{afirmada} vs {primera_mano}: cambia la clausula de USO EN RED')
    if ca != cp:
        return ('REFUTADA', 'HOSPEDAJE' if cp == 'RED' else 'BLOQUEANTE',
                f'{afirmada} ({ca}) vs {primera_mano} ({cp}): cambia el regimen')
    return ('REFUTADA', 'COSMETICA',
            f'{afirmada} vs {primera_mano}: misma clase, no cambia la entrega')


def main(argv):
    if len(argv) == 3:
        af = None if argv[1] in ('-', 'NADA') else argv[1]
        v, r, m = riesgo(af, argv[2])
        print(f'{v}\t{r}\t{m}')
        return 0
    print('uso: audit_claim.py <afirmada|-> <primera_mano>', file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
