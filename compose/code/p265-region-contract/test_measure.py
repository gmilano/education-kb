#!/usr/bin/env python3
"""Suite de P265/P266/P267. Imprime su total propio (punto 3 de la regla de P126).

Los dos casos que HABILITAN los instrumentos de este pase:

1. **El control POSITIVO del barrido de grafias.** `measure_variants.py` publica **0**
   hallazgos accionables sobre el arbol real, y un cero no vale sin una corrida donde el
   instrumento SI dispara. `fixtures/tabla-con-variante.md` es una tabla regional legitima
   con dos grafias fuera de vocabulario, y el barrido tiene que encontrar exactamente esas
   dos — ni las de negrita, ni la exacta.
2. **La discrepancia MEDIDA entre los dos validadores preexistentes.** `p243` acepta
   `" APAC"` y `p262` lo rechaza. La suite lo afirma como HECHO, no como defecto: los dos
   tienen razon porque sus portadores tienen sintaxis distinta (P265).

    python3 test_measure.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "lib"))

import measure                                    # noqa: E402
import measure_variants                           # noqa: E402
from region import actionable_variants, variants_in  # noqa: E402

n = ok = 0


def chk(label, got, want):
    global n, ok
    n += 1
    if got == want:
        ok += 1
        print(f"PASS {label}")
    else:
        print(f"FAIL {label}: got {got!r} want {want!r}")


# ---------------------------------------------------------------------------------
# 1. CONTROL POSITIVO del barrido de grafias
# ---------------------------------------------------------------------------------
rows = measure_variants.sweep(os.path.join(HERE, "fixtures"))
act = [r for r in rows if r[4] != "MARKUP"]
chk("el fixture dispara exactamente DOS hallazgos accionables", len(act), 2)
chk("y son las dos grafias plantadas", {(r[2], r[4]) for r in act},
    {("**latam**", "CASO"), ("**North-America**", "SEPARADOR")})
chk("las grafias de vocabulario con negrita NO son accionables",
    {r[2] for r in rows if r[4] == "MARKUP"}, {"**North America**", "**EMEA**"})
chk("la grafia exacta sin markup no aparece en absoluto",
    [r for r in rows if r[2] == "APAC"], [])

# el mismo fixture, por la funcion primitiva
chk("la primitiva clasifica la capitalizacion como CASO",
    actionable_variants("**latam**"), {("**latam**", "LATAM", "CASO")})
chk("y el guion como SEPARADOR", actionable_variants("**North-America**"),
    {("**North-America**", "North America", "SEPARADOR")})
chk("la negrita sola no es accionable", actionable_variants("**LATAM**"), set())
chk("pero SI se registra, clasificada como MARKUP",
    variants_in("**LATAM**"), {("**LATAM**", "LATAM", "MARKUP")})

# ---------------------------------------------------------------------------------
# 2. La matriz diferencial: lo que cada implementacion responde HOY
# ---------------------------------------------------------------------------------
sw = measure.sweep()
by = {v: (verd, legacy, vdet) for v, _k, verd, legacy, vdet in sw}
chk("la matriz tiene 34 valores", len(sw), 34)

# el hecho medido: los dos validadores preexistentes discrepan, y en UN valor
legacy_hits = [v for v, _k, _vd, legacy, _x in sw if legacy]
chk("los validadores preexistentes discrepan en exactamente un valor", len(legacy_hits), 1)
chk("y es el blanco de la IZQUIERDA", legacy_hits, [" APAC"])
chk("p243 lo ACEPTA (en YAML el blanco izquierdo es sintaxis)", by[" APAC"][0]["p243"], True)
chk("p262 lo RECHAZA (en una celda de dato, es dato)", by[" APAC"][0]["p262"], False)
chk("el validador de dato de lib coincide con p262", by[" APAC"][0]["lib"], False)
chk("y el de frontmatter de lib coincide con p243", by[" APAC"][0]["libf"], True)

# el blanco de la DERECHA no lo perdona NINGUNO: eso sigue siendo P248
for c in ("p243", "p262", "lib", "libf"):
    chk(f"{c} RECHAZA 'APAC ' (P248 cerrado por la derecha)", by["APAC "][0][c], False)

# los cinco exactos pasan en todas las columnas
for r in ("North America", "EMEA", "APAC", "LATAM", "Global"):
    chk(f"todas las columnas ACEPTAN {r!r}", set(by[r][0].values()), {True})

# el contrato: validador y detector dan veredicto OPUESTO, y en cuantos valores
opuestos = [v for v, _k, _vd, _l, vdet in sw if vdet]
chk("validador y detector se oponen en 18 valores", len(opuestos), 18)
chk("'🔴 **LATAM**' es uno de ellos", "🔴 **LATAM**" in opuestos, True)
chk("y ningun EXACTO esta entre ellos",
    [v for v, k, _vd, _l, vdet in sw if vdet and k == "EXACTO"], [])

# P266: el default de las dos funciones de deteccion es el ESTRICTO
chk("el default de p239 descarta la celda de cifras", by["86 % NA / 92 % LATAM"][0]["p239"],
    False)
chk("el default de lib tambien", by["86 % NA / 92 % LATAM"][0]["libd"], False)
chk("y la version lenient, pedida explicitamente, SI la acepta",
    by["86 % NA / 92 % LATAM"][0]["p239l"], True)

print()
print(f"{ok}/{n} checks passed")
sys.exit(0 if ok == n else 1)
