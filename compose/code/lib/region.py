#!/usr/bin/env python3
"""`lib/region.py` — la pregunta de region, que son DOS preguntas con contratos OPUESTOS.

Pase 89 del 2026-10-04. Existe porque **P263** (pase 88) dejo escrita la regla
—«mientras la pregunta no viva en `compose/code/lib/`, cada instrumento nuevo la
reimplementa y vuelve a elegir el bug»— y este pase la fue a cumplir y encontro que la
regla, tal como estaba escrita, **no se puede cumplir**: no hay UNA pregunta de region.

Hay dos, y necesitan leniencia CONTRARIA:

| Pregunta | Quien la hace | `"APAC "` | `| 🔴 **LATAM** |` |
|---|---|---|---|
| VALIDADOR — «¿este valor esta en vocabulario?» | `p243` (frontmatter), `p262` (filas) | RECHAZA (P248) | RECHAZA |
| DETECTOR — «¿esta celda NOMBRA regiones?»     | `p239` (tablas publicadas)           | acepta        | acepta      |

🔴 **Una sola funcion compartida habria roto una de las dos**: con la leniencia del
detector, `p243` y `p262` vuelven a aceptar `"APAC "` y P248 se reabre; con el rigor del
validador, `p239` deja de reconocer sus propias celdas y vuelve a reclamar como
incompletas tablas que estan completas (los tres falsos positivos que su v1 pago).

🔵 **Asi que el contrato de este modulo es que las dos funciones DISIENTAN** sobre la clase
`DIVERGENCE`, y eso esta afirmado en `test_region.py` como caso obligatorio. La divergencia
no es un defecto a conciliar: es la razon por la que son dos funciones.

Uso:
    import sys, os; sys.path.insert(0, ".../compose/code/lib")
    from region import REGIONS, region_ok, regions_named
"""
import re

#: Vocabulario CERRADO. Cinco valores, exactos. No `Latam`, no `Europe`, no `Brazil`.
REGIONS = ("North America", "EMEA", "APAC", "LATAM", "Global")

NORM_DROP = re.compile(r"[^A-Za-z ]")          # emoji, **, backticks, numeros
PAREN = re.compile(r"\s*\([^)]*\)")            # "APAC (Vietnam)" -> "APAC"
#: Solo MARKUP: `**`, backticks, `_`, `#`, emoji. Deja letras, digitos, espacios y guion,
#: porque el guion de `North-America` NO es markup: es parte de la grafia (P267).
MARKUP_DROP = re.compile(r"[^A-Za-z0-9 \-]")

#: Los valores donde VALIDADOR y DETECTOR tienen que dar veredictos opuestos.
#: `test_region.py` los afirma uno por uno; es el control que habilita este modulo.
DIVERGENCE = (
    "APAC ",
    " APAC",
    "APAC\t",
    "**LATAM**",
    "🔴 **LATAM**",
    "APAC (Vietnam)",
    "`EMEA`",
    "apac",
    "latam",
    "North  America",
)


def region_ok(value):
    """VALIDADOR. `True` solo si `value` es, byte a byte, uno de los cinco.

    🔴 NO se hace `strip()` antes de preguntar: eso es exactamente **P248**. `"APAC "` se
    renderiza identico en Markdown pero el compilador lo bucketea aparte, asi que es un
    valor DISTINTO y tiene que salir rechazado. `None` y `""` tambien salen rechazados: la
    ausencia no es vocabulario (quien quiera distinguir «falta» de «variante» mira la
    clave, como hace `p243`).

    El defecto que esta funcion existe para no volver a elegir se reintrodujo dos veces:
    en `p243` (corregido en el pase 82) y en `p262` (corregido en el pase 88, a seis pases
    de distancia y en un archivo nuevo) -> **P263**.
    """
    return value in REGIONS


def regions_named(cell, strict=True):
    """DETECTOR. El conjunto de regiones que una celda de tabla NOMBRA.

    Es lenient a proposito, porque mide prosa publicada y no un campo: saca el parentesis
    calificativo (`APAC (Vietnam)`), descarta todo lo que no sea letra o espacio (emoji,
    `**`, backticks, numeros) y parte la celda por `/`, `,` y ` y ` porque una celda puede
    nombrar DOS regiones. Compara con `casefold()`.

    `strict=True` ES EL DEFAULT, y ese default es parte del contrato: la celda cuenta como
    celda de REGION solo si no queda residuo. Es el arreglo de la v3 de `p239`, que evita
    leer como regional una celda de CIFRAS (`86 % NA / 92 % LATAM`) o de PERFIL DE CLIENTE.

    🔴 La primera version de ESTE modulo puso `strict=False` por default y P265 lo midio:
    es la misma clase de defecto que `parse_frontmatter(text, raw=False)` en `p243` —el
    comportamiento endurecido detras de un argumento NO default, asi que el proximo
    llamador hereda el flojo sin pedirlo—. Ver **P266**.

    🔵 Esta leniencia es la que un validador no puede tener. Ver `DIVERGENCE`.
    """
    c = PAREN.sub("", cell)
    out, residue = set(), False
    for part in re.split(r"[/,]| y ", c):
        t = NORM_DROP.sub(" ", part)
        t = re.sub(r"\s+", " ", t).strip()
        if not t:
            continue
        hit = next((r for r in REGIONS if t.casefold() == r.casefold()), None)
        if hit:
            out.add(hit)
        else:
            residue = True
    if strict and residue:
        return set()
    return out


def region_ok_frontmatter(raw_value):
    """VALIDADOR para el portador FRONTMATTER, donde el blanco de la IZQUIERDA es sintaxis.

    `p243` y `p262` discrepan hoy sobre `" APAC"` —p243 lo ACEPTA, p262 lo RECHAZA— y P265
    midio que **los dos tienen razon**, porque sus portadores son distintos: en YAML
    `region:   APAC` separa la clave del valor con blanco arbitrario, asi que a la izquierda
    el blanco NO es dato; en una celda TSV como la de `p262`, SI lo es.

    🔵 La consecuencia es que «¿esta en vocabulario?» no tiene UNA respuesta ni siquiera
    entre validadores: **depende de la SINTAXIS del portador.** Por eso son dos funciones y
    no un parametro. A la derecha ninguno de los dos portadores perdona: eso sigue siendo
    P248.
    """
    if raw_value is None:
        return False
    return region_ok(raw_value.lstrip(" \t"))


def variants_in(cell):
    """Las grafias NO de vocabulario que el DETECTOR normalizo hasta hacerlas coincidir.

    El detector tiene que ser lenient para medir prosa publicada, pero esa leniencia tiene
    un costo que esta base no estaba midiendo: `| North-America |` en una celda **se lee
    como region y nunca se reporta**, mientras el mismo string en frontmatter es un hallazgo
    de `p243`. O sea que el vocabulario cerrado se aplica en un portador y no en el otro.

    🔴 Y la primera version de esta funcion metio en la misma bolsa las 172 celdas del arbol,
    de las cuales la enorme mayoria son `**LATAM**`: **negrita no es una variante de grafia,
    es formato.** Confundirlas es el mismo falso positivo que la v1 de `p239` pago tres veces.
    Asi que cada hallazgo sale CLASIFICADO:

    | Clase | Que cambia respecto del vocabulario | Ejemplo | Accionable |
    |---|---|---|---|
    | `MARKUP`     | solo markup: `**`, backtick, emoji | `**LATAM**`      | no, es formato |
    | `CASO`       | la capitalizacion de las letras    | `latam`          | SI             |
    | `SEPARADOR`  | guion, doble espacio, puntuacion   | `North-America`  | SI             |

    Devuelve el conjunto de `(grafia, region, clase)`.
    """
    out = set()
    c = PAREN.sub("", cell)
    for part in re.split(r"[/,]| y ", c):
        t = NORM_DROP.sub(" ", part)
        t = re.sub(r"\s+", " ", t).strip()
        if not t:
            continue
        hit = next((r for r in REGIONS if t.casefold() == r.casefold()), None)
        if not hit or part.strip() == hit:
            continue
        # OJO: NO se colapsa el blanco interno. `North  America` con doble espacio es una
        # variante real —el validador la rechaza— y colapsarla la archivaria como formato.
        bare = MARKUP_DROP.sub("", part).strip()
        if bare == hit:
            klass = "MARKUP"
        elif bare.casefold() == hit.casefold():
            klass = "CASO"
        else:
            klass = "SEPARADOR"
        out.add((part.strip(), hit, klass))
    return out


def actionable_variants(cell):
    """Las de `variants_in()` que NO son solo formato. Es la cifra que vale (P267)."""
    return {v for v in variants_in(cell) if v[2] != "MARKUP"}
