#!/usr/bin/env python3
"""P262 — el NIVEL ADMINISTRATIVO de un mandato curricular es una columna propia.

Tres preguntas que esta base, y la prensa secundaria que la alimenta, venian haciendo como una:

  1. NIVEL    -- ¿quien obliga? (nacion / provincia / ciudad / estado / nadie)
  2. VIGENCIA -- ¿obliga YA, o esta anunciado para un ciclo futuro, o es solo una guia?
  3. ENTREGA  -- ¿asignatura PROPIA, o contenido INTEGRADO en materias que ya existen?

La compuerta: ninguna se contesta por inferencia. Sin AUTORIDAD leida no hay nivel; sin ciclo
de entrada en vigor no hay vigencia; sin el texto del instrumento no hay modo de entrega.
La respuesta en ese caso es NO-CLAIM, nunca el valor optimista.
"""

# --- vocabulario CERRADO de region: ya NO vive aqui -------------------------------------
# 🟢 Pase 89: esto era una copia local, y la copia local es la causa de P263. Ahora la
# pregunta viene de `compose/code/lib/region.py`, que es donde P263 dijo que tenia que vivir.
# `region_ok` de la lib es la version de portador DATO —sin perdon a izquierda ni a derecha—,
# que es exactamente la que esta instrumento necesita: sus filas son celdas TSV.
import os as _os
import sys as _sys

_sys.path.insert(0, _os.path.join(
    _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "lib"))
from region import REGIONS, region_ok as _region_ok  # noqa: E402,F401

# --- vocabulario CERRADO de nivel --------------------------------------------------------
NATIONAL = "NATIONAL"
PROVINCE = "SUBNATIONAL-PROVINCE"
CITY = "SUBNATIONAL-CITY"
STATE = "SUBNATIONAL-STATE"
NO_MANDATE = "NO-MANDATE"
NO_CLAIM = "NO-CLAIM"

LEVELS = (NATIONAL, PROVINCE, CITY, STATE, NO_MANDATE, NO_CLAIM)

# el alcance DECLARADO de la autoridad que firma -> el nivel que puede sostener.
# Es un mapa, no una heuristica de texto: se lee de la autoridad, no del titular de la nota.
SCOPE_TO_LEVEL = {
    "national": NATIONAL,
    "national-board": NATIONAL,   # un consejo escolar de alcance nacional (CBSE) obliga nacional
    "province": PROVINCE,
    "municipality-provincial-rank": PROVINCE,  # Pekin: municipio de rango provincial
    "city": CITY,
    "state": STATE,
    "supranational": NO_MANDATE,  # un bloque puede obligar al DESPLIEGUE, no al curriculo
    "none": NO_MANDATE,
}

# --- vigencia ---------------------------------------------------------------------------
IN_FORCE = "IN-FORCE"
ANNOUNCED = "ANNOUNCED-FUTURE"
GUIDANCE = "GUIDANCE-ONLY"

# --- entrega ----------------------------------------------------------------------------
STANDALONE = "STANDALONE"
INTEGRATED = "INTEGRATED"
BOTH = "BOTH-PERMITTED"

DELIVERY = (STANDALONE, INTEGRATED, BOTH, NO_CLAIM)


def _blank(v):
    return v is None or str(v).strip() in ("", "-", "?")


def level_of(row):
    """Pregunta 1. El nivel sale del ALCANCE de la autoridad, nunca del titular de la nota."""
    if _blank(row.get("authority_scope")):
        return NO_CLAIM
    scope = row["authority_scope"].strip()
    if scope not in SCOPE_TO_LEVEL:
        return NO_CLAIM                      # alcance desconocido: no se conjetura
    if scope == "none":
        # AUSENCIA de mandato. Aqui no hay autoridad que nombrar, asi que exigirla seria el
        # error de P248 (pedir el dato que por construccion no existe). Lo que SI se exige es
        # el instrumento que MIDIO la ausencia: sin el, una busqueda propia que no encontro
        # nada es silencio, y P251 prohibe afirmar ausencia desde el silencio propio.
        return NO_MANDATE if not _blank(row.get("instrument")) else NO_CLAIM
    if _blank(row.get("authority")):
        return NO_CLAIM                      # sin autoridad NOMBRADA no hay mandato
    lvl = SCOPE_TO_LEVEL[scope]
    # una autoridad de alcance nacional que solo emitio GUIA no sostiene un mandato
    if lvl == NATIONAL and row.get("force") == GUIDANCE:
        return NO_MANDATE
    return lvl


def force_of(row):
    """Pregunta 2. Sin ciclo de entrada en vigor no se afirma vigencia."""
    declared = (row.get("force") or "").strip()
    if declared == GUIDANCE:
        return GUIDANCE
    if declared not in (IN_FORCE, ANNOUNCED):
        return NO_CLAIM
    if _blank(row.get("in_force")):
        return NO_CLAIM                      # "obliga" sin ciclo es una promesa, no un hecho
    return declared


def delivery_of(row):
    """Pregunta 3. El modo de entrega se lee del instrumento o no se contesta."""
    d = (row.get("delivery") or "").strip()
    if d not in (STANDALONE, INTEGRATED, BOTH):
        return NO_CLAIM
    if _blank(row.get("instrument")):
        return NO_CLAIM                      # sin texto leido, el modo es inferencia
    return d


def classify(row):
    """Las tres columnas, en orden. Nunca una sola palabra."""
    return (level_of(row), force_of(row), delivery_of(row))


def region_ok(row):
    """La region va en vocabulario cerrado. UAE es EMEA, no APAC: el pais manda, no el titular.

    🟢 Pase 89: el cuerpo de esta funcion ya no esta aqui — delega en `lib.region.region_ok`.
    Lo unico propio que queda es la ADAPTACION: esta instrumento recibe una FILA y la lib
    recibe un VALOR. Es la forma concreta de cumplir **P263**: el instrumento sigue teniendo
    su funcion con su nombre y su firma, pero la REGLA es compartida y se endurece en un
    solo lugar.

    🔴 El defecto que la lib garantiza no volver a elegir: no se hace `strip()` antes de
    preguntar por el vocabulario (**P248**). `"APAC "` es un valor DISTINTO y sale rechazado,
    porque el compilador lo bucketea aparte.
    """
    return _region_ok(row.get("region") or "")


def refutes_national_claim(rows, jurisdiction):
    """¿Se puede sostener que `jurisdiction` tiene mandato curricular NACIONAL?

    Devuelve (sostenible: bool, motivo: str). Esta es la funcion que el control negativo usa.
    """
    mine = [r for r in rows if r["jurisdiction"] == jurisdiction]
    if not mine:
        return (False, "sin filas medidas para esa jurisdiccion")
    levels = {level_of(r) for r in mine}
    if NATIONAL in levels:
        return (True, "al menos una fila sostiene nivel nacional")
    return (False, f"el nivel medido mas alto es {sorted(levels)}, ninguno NATIONAL")


def load(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        head = None
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if head is None:
                head = parts
                continue
            rows.append(dict(zip(head, parts)))
    return rows
