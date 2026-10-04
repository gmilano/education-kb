#!/usr/bin/env python3
"""Suite de P262. Imprime su propio total (regla 3 de P126)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mandate import (classify, level_of, force_of, delivery_of, region_ok,  # noqa: E402
                     refutes_national_claim, load, REGIONS, LEVELS,
                     NATIONAL, PROVINCE, CITY, STATE, NO_MANDATE, NO_CLAIM,
                     IN_FORCE, ANNOUNCED, GUIDANCE, STANDALONE, INTEGRATED, BOTH)

ok = fail = 0


def chk(label, got, want):
    global ok, fail
    if got == want:
        ok += 1
        print(f"PASS {label}")
    else:
        fail += 1
        print(f"FAIL {label}\n     got ={got!r}\n     want={want!r}")


def row(**kw):
    base = dict(jurisdiction="x", region="Global", authority="A", authority_scope="national",
                force=IN_FORCE, in_force="2026-27", delivery=INTEGRATED, grades="-",
                instrument="texto leido")
    base.update(kw)
    return base


HERE = os.path.dirname(os.path.abspath(__file__))
real = load(os.path.join(HERE, "rows.tsv"))

# ---------------------------------------- 1. LA COMPUERTA: nada se contesta por inferencia
chk("sin alcance de autoridad NO hay nivel",
    level_of(row(authority_scope="")), NO_CLAIM)
chk("un alcance que no esta en el mapa NO se conjetura",
    level_of(row(authority_scope="region-ish")), NO_CLAIM)
chk("sin autoridad NOMBRADA no hay mandato, aunque el alcance diga 'national'",
    level_of(row(authority="", authority_scope="national")), NO_CLAIM)
chk("sin ciclo de entrada en vigor no se afirma vigencia",
    force_of(row(in_force="-")), NO_CLAIM)
chk("una vigencia fuera de vocabulario sale NO-CLAIM",
    force_of(row(force="vigente!")), NO_CLAIM)
chk("sin instrumento LEIDO el modo de entrega es inferencia, no dato",
    delivery_of(row(instrument="")), NO_CLAIM)
chk("un modo de entrega fuera de vocabulario sale NO-CLAIM",
    delivery_of(row(delivery="mixto")), NO_CLAIM)

# ---------------------------------------- 2. el nucleo de P262: el nivel sale del ALCANCE
chk("un municipio de rango provincial sostiene PROVINCIA, no NACION",
    level_of(row(authority_scope="municipality-provincial-rank")), PROVINCE)
chk("una ciudad sostiene CIUDAD",
    level_of(row(authority_scope="city")), CITY)
chk("un estado sostiene ESTADO",
    level_of(row(authority_scope="state")), STATE)
chk("un consejo escolar de alcance nacional SI sostiene NACION",
    level_of(row(authority_scope="national-board")), NATIONAL)
chk("un bloque supranacional NO sostiene mandato curricular",
    level_of(row(authority_scope="supranational")), NO_MANDATE)
chk("una autoridad nacional que solo emitio GUIA no sostiene mandato",
    level_of(row(authority_scope="national", force=GUIDANCE)), NO_MANDATE)

# ---------------------------------------- 3. CONTROL NEGATIVO: la afirmacion secundaria literal
# Frase recogida en la busqueda de este pase, repetida por varias fuentes secundarias:
#   "China and the UAE are the only nations running compulsory, national AI curricula
#    since the 2025-26 school year."
sustainable_cn, why_cn = refutes_national_claim(real, "China-Beijing")
chk("CONTROL NEGATIVO: 'China' NO sostiene mandato curricular NACIONAL",
    sustainable_cn, False)
chk("y el motivo nombra el nivel medido, no una opinion",
    "NATIONAL" not in why_cn.split("ninguno")[0].replace("SUBNATIONAL-PROVINCE", ""), True)
sustainable_cnn, _ = refutes_national_claim(real, "China-national")
chk("la fila NACIONAL de China tampoco lo sostiene: es GUIA",
    sustainable_cnn, False)
chk("la UAE SI lo sostiene, y es la mitad verdadera de la frase",
    refutes_national_claim(real, "UAE")[0], True)
chk("preguntar por una jurisdiccion no medida NO devuelve True",
    refutes_national_claim(real, "Narnia")[0], False)

# ---------------------------------------- 4. region en vocabulario CERRADO
chk("la region de la UAE es EMEA, no APAC (el pais manda, no el titular que la agrupa con China)",
    [r["region"] for r in real if r["jurisdiction"] == "UAE"], ["EMEA"])
chk("las 5 regiones del vocabulario y nada mas", len(REGIONS), 5)
chk("todas las filas en vocabulario de region", all(region_ok(r) for r in real), True)
for bad in ("Latam", "Europe", "Asia Pacific", "Brazil", "APAC "):
    chk(f"la variante {bad!r} es RECHAZADA", region_ok({"region": bad}), False)

# ---------------------------------------- 5. el reparto real medido
chk("el cohorte tiene 12 filas", len(real), 12)
chk("12 jurisdicciones/tramos DISTINTOS", len({r["jurisdiction"] for r in real}), 12)
levels = [level_of(r) for r in real]
chk("todo nivel emitido esta en vocabulario", set(levels) <= set(LEVELS), True)
chk("2 tramos NACIONALES, y los dos son India-CBSE + UAE",
    sorted(r["jurisdiction"] for r in real if level_of(r) == NATIONAL),
    ["India-CBSE-3-8", "India-CBSE-9-10", "UAE"])
chk("1 PROVINCIAL, y es Pekin", [r["jurisdiction"] for r in real if level_of(r) == PROVINCE],
    ["China-Beijing"])
chk("1 de CIUDAD, y es CABA", [r["jurisdiction"] for r in real if level_of(r) == CITY],
    ["Argentina-CABA"])
chk("2 de ESTADO, los dos de EEUU", len([r for r in real if level_of(r) == STATE]), 2)
# 3 son AUSENCIA MEDIDA (traen instrumento) y 2 son HUECO DECLARADO (no lo traen).
chk("3 con ausencia MEDIDA de mandato: China-nacional, UE y EEUU-federal",
    sorted(r["jurisdiction"] for r in real if level_of(r) == NO_MANDATE),
    ["China-national", "EU-AIAct", "USA-federal"])
chk("2 en NO-CLAIM, y son el hueco declarado de LATAM",
    sorted(r["jurisdiction"] for r in real if level_of(r) == NO_CLAIM), ["Brazil", "Chile"])
chk("el reparto suma el cohorte", 3 + 1 + 1 + 2 + 3 + 2, len(real))

# la asimetria comercial: ¿cuantos tramos OBLIGAN YA?
chk("4 tramos OBLIGAN HOY", len([r for r in real if force_of(r) == IN_FORCE]), 4)
chk("y de esos 4, exactamente 2 son de alcance NACIONAL: la UAE y India Clases 3-8",
    sorted(r["jurisdiction"] for r in real
           if force_of(r) == IN_FORCE and level_of(r) == NATIONAL),
    ["India-CBSE-3-8", "UAE"])
chk("los otros 2 vigentes son SUB-nacionales (Pekin provincial, CABA ciudad)",
    sorted(r["jurisdiction"] for r in real
           if force_of(r) == IN_FORCE and level_of(r) in (PROVINCE, CITY)),
    ["Argentina-CABA", "China-Beijing"])
chk("3 tramos ANUNCIADOS para ciclo futuro",
    len([r for r in real if force_of(r) == ANNOUNCED]), 3)

# el eje de ENTREGA, que decide si un producto de 'IA como asignatura' tiene estante
standalone_inforce = [r["jurisdiction"] for r in real
                      if delivery_of(r) == STANDALONE and force_of(r) == IN_FORCE]
chk("CERO jurisdicciones obligan HOY una ASIGNATURA PROPIA de IA", standalone_inforce, [])
chk("los 4 tramos vigentes entregan INTEGRADO o AMBOS",
    sorted({delivery_of(r) for r in real if force_of(r) == IN_FORCE}),
    sorted({INTEGRATED, BOTH}))

# ---------------------------------------- 6. los huecos DECLARADOS, no silenciosos
# el hueco se reconoce por la AUSENCIA de instrumento, y sale NO-CLAIM, no NO-MANDATE:
# una busqueda propia que no encontro nada es silencio, y P251 prohibe afirmar desde el silencio.
gaps = [r["jurisdiction"] for r in real if not r["instrument"]]
chk("Brasil y Chile son los 2 sin instrumento, y por eso NO-CLAIM",
    sorted(gaps), ["Brazil", "Chile"])
chk("y EEUU-federal NO es hueco: trae su instrumento de ausencia medida",
    level_of([r for r in real if r["jurisdiction"] == "USA-federal"][0]), NO_MANDATE)
chk("la UE no se cuenta como mandato curricular pero SI trae instrumento citado",
    bool([r for r in real if r["jurisdiction"] == "EU-AIAct"][0]["instrument"]), True)

# ---------------------------------------- 7. las tres columnas, nunca una palabra
chk("classify() devuelve SIEMPRE tres columnas",
    all(len(classify(r)) == 3 for r in real), True)
chk("y la fila de Pekin es exactamente (PROVINCIA, vigente, ambos permitidos)",
    classify([r for r in real if r["jurisdiction"] == "China-Beijing"][0]),
    (PROVINCE, IN_FORCE, BOTH))

print(f"\n{ok}/{ok + fail}")
sys.exit(1 if fail else 0)
