"""`P637` (pase 53, 2026-10-08) — la COMPUERTA DE ACUERDO ENTRE INSTRUMENTOS.

Por que existe.  `Gap 256` sobrevivio TRES pases declarado como «la rama LGPL sub-lee la
version».  Lo que realmente pasaba era otra cosa, y mas barata de detectar: esta KB tiene
TRES implementaciones de la pregunta «que familia de licencia es este payload», y sobre el
payload de `openeducat/openeducat_erp` daban DOS respuestas distintas.  Cada instrumento
pasaba SUS PROPIAS fixtures, asi que ninguna suite lo veia.

    lib/license_family.sh::osi_family_of            -> LGPL      (el compartido: lo consumen las compuertas)
    p419-copyleft-identity::familia                 -> LGPL-3.0  (correcto, desde el pase 123)
    licence-grant-gate/grant_gate.py::family_of     -> LGPL      (grueso POR CONTRATO)

Y el estante (`verticals/solutions.md`) decia `LGPL-3.0`, o sea que LA MAYORIA ESTABA MAL.
Por eso este instrumento NO vota: reporta el desacuerdo y deja que lo adjudique la lectura
de primera mano.  Un voto por mayoria habria cementado el defecto.

`P255` ya habia encontrado esta forma sobre la pregunta del TITULAR (tres instrumentos, tres
respuestas).  Esto la generaliza a una compuerta corrible.

Un desacuerdo es de UNA de dos clases, y nombrar cual es el punto:

  * `DEFECTO`   — dos instrumentos que PRETENDEN la misma granularidad y difieren.
  * `CONTRATO`  — un instrumento deliberadamente mas grueso (`grant_gate` contesta la
                  pregunta concesion-vs-mencion, donde la version no es portante).

`agreement.py` no sale a la red: los payloads son texto, y la unica dependencia externa es
`bash` para la libreria compartida.
"""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(AQUI, '..', 'lib', 'license_family.sh')
P419 = os.path.join(AQUI, '..', 'p419-copyleft-identity')
GRANT = os.path.join(AQUI, '..', 'licence-grant-gate')

# `P445`: el payload va por STDIN y no por argv — varios pasan los 35 kB y argv tiene limite
# duro, asi que el texto se truncaria en silencio y el fallo pareceria un desacuerdo.
_PUENTE = '. "$1"\nT=$(cat)\nprintf "%s" "$(osi_family_of "$T")"\n'

# Instrumentos cuya granularidad es deliberadamente distinta.  No son defectos.
CONTRATO_GRUESO = frozenset({'grant_gate'})


def _compartido(texto):
    r = subprocess.run(['bash', '-c', _PUENTE, '_', LIB],
                       input=texto, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError('la libreria compartida no cargo: %s' % r.stderr.strip())
    return r.stdout.strip()


def _p419(texto):
    if P419 not in sys.path:
        sys.path.insert(0, P419)
    import identidad_copyleft
    return identidad_copyleft.familia(texto)[0]


def _grant(texto):
    if GRANT not in sys.path:
        sys.path.insert(0, GRANT)
    import grant_gate
    return grant_gate.family_of(texto)


LECTORES = (('compartido', _compartido), ('p419', _p419), ('grant_gate', _grant))


def leer_todos(texto):
    """{nombre: respuesta}.  Un lector que EXPLOTA se registra como tal y no se silencia:
    `P614` — una suite que no puede cargar su dependencia debe NEGARSE, no pasar."""
    out = {}
    for nombre, fn in LECTORES:
        try:
            out[nombre] = fn(texto)
        except Exception as e:                      # noqa: BLE001 - se reporta, no se traga
            out[nombre] = 'ERROR: %s' % type(e).__name__
    return out


def _base(fam):
    """La familia sin version: `LGPL-3.0` -> `LGPL`.  Es como se distingue una diferencia de
    GRANULARIDAD (un instrumento leyo menos) de una CONTRADICCION (leyeron familias distintas)."""
    fam = fam.split(' (')[0]
    for sep in ('-',):
        if sep in fam:
            cabeza = fam.split(sep)[0]
            # `CC-BY-4.0` y `CC-BY-SA-4.0` comparten cabeza `CC`; alcanza para esta pregunta.
            if cabeza:
                return cabeza
    return fam


def adjudicar(texto, respuesta_del_estante=None):
    """-> dict con las respuestas, la clase del desacuerdo y el veredicto.

    `respuesta_del_estante` es la lectura de PRIMERA MANO.  Cuando se pasa, es el
    desempate — nunca la mayoria (`P637`: sobre openeducat la mayoria estaba mal)."""
    r = leer_todos(texto)
    vivos = {k: v for k, v in r.items() if not v.startswith('ERROR:')}
    distintas = set(vivos.values())
    bases = {_base(v) for v in vivos.values()}

    if len(distintas) <= 1:
        clase, veredicto = 'ACUERDO', sorted(distintas)[0] if distintas else 'SIN-LECTORES'
    elif len(bases) > 1:
        # Familias distintas, no granularidades distintas.  Es lo mas grave que puede salir.
        clase, veredicto = 'CONTRADICCION', 'INDECIDIBLE'
    else:
        # Misma familia, versiones distintas: alguien leyo menos.
        discrepantes = {k for k, v in vivos.items() if v != max(distintas, key=len)}
        clase = 'CONTRATO' if discrepantes <= CONTRATO_GRUESO else 'DEFECTO'
        veredicto = max(distintas, key=len)

    if respuesta_del_estante is not None and clase in ('DEFECTO', 'CONTRADICCION'):
        veredicto = respuesta_del_estante           # el desempate es la lectura, no el conteo
    return {'respuestas': r, 'clase': clase, 'veredicto': veredicto,
            'estante': respuesta_del_estante}
