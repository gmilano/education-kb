#!/usr/bin/env python3
"""Suite de `lib/region.py`. Imprime su total propio (punto 3 de la regla de P126).

El caso OBLIGATORIO de esta suite es el ultimo bloque: **las dos funciones tienen que
DISENTIR** sobre `DIVERGENCE`. Una suite que solo afirmara «el validador rechaza las
variantes» pasaria igual con una sola funcion lenient compartida, que es el error que
este modulo existe para no cometer -> es un control que no ejercita el caso donde el
instrumento puede fallar, y eso es exactamente lo que la regla de **P126** prohibe.

    python3 test_region.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from region import (DIVERGENCE, REGIONS, region_ok, region_ok_frontmatter,  # noqa: E402
                    regions_named, variants_in, actionable_variants)

n = ok = 0


def chk(label, got, want):
    global n, ok
    n += 1
    if got == want:
        ok += 1
        print(f"PASS {label}")
    else:
        print(f"FAIL {label}: got {got!r} want {want!r}")


# --- el vocabulario cerrado, tal como es -------------------------------------------
chk("el vocabulario tiene exactamente cinco valores", len(REGIONS), 5)
chk("y son los cinco de la especificacion", set(REGIONS),
    {"North America", "EMEA", "APAC", "LATAM", "Global"})
for r in REGIONS:
    chk(f"el validador ACEPTA {r!r}", region_ok(r), True)

# --- control NEGATIVO del validador: P248 y las variantes de balde -----------------
for bad in ("APAC ", " APAC", "APAC\t", "Latam", "latam", "LATAM ", "Europe",
            "Asia Pacific", "Asia-Pacific", "Brazil", "Brasil", "North-America",
            "NA", "North  America", "global", "GLOBAL", "", "Global "):
    chk(f"el validador RECHAZA {bad!r}", region_ok(bad), False)
chk("el validador RECHAZA None (la ausencia no es vocabulario)", region_ok(None), False)

# --- el detector, sobre las celdas que p239 publica de verdad ----------------------
chk("detecta la celda con emoji y negrita", regions_named("🔴 **LATAM**"), {"LATAM"})
chk("detecta el calificativo entre parentesis", regions_named(" APAC (Vietnam) "), {"APAC"})
chk("una celda puede nombrar DOS regiones", regions_named("**APAC / LATAM**"),
    {"APAC", "LATAM"})
chk("y TRES, separadas por coma", regions_named("EMEA, APAC, LATAM"),
    {"EMEA", "APAC", "LATAM"})
chk("el separador ' y ' tambien parte", regions_named("EMEA y LATAM"), {"EMEA", "LATAM"})
chk("backticks fuera", regions_named("`EMEA`"), {"EMEA"})
chk("el doble espacio se colapsa", regions_named("North  America"), {"North America"})
chk("una celda sin region ninguna da vacio", regions_named(" Licencia "), set())

# --- strict: el arreglo de la v3 de p239 ------------------------------------------
# El default es strict=True y eso es contrato: P266. La celda de cifras NO es regional
# sin que nadie tenga que pedirlo.
chk("el DEFAULT descarta la celda de cifras (P266)",
    regions_named("86 % NA / 92 % LATAM"), set())
chk("y strict=True explicito da lo mismo",
    regions_named("86 % NA / 92 % LATAM", strict=True), set())
chk("la leniencia hay que PEDIRLA, y entonces si rinde LATAM",
    regions_named("86 % NA / 92 % LATAM", strict=False), {"LATAM"})
chk("strict DESCARTA la celda de perfil de cliente",
    regions_named("Ministerio, APAC / LATAM / Africa", strict=True), set())
chk("strict ACEPTA la celda que es solo regiones",
    regions_named("**APAC / LATAM**", strict=True), {"APAC", "LATAM"})

# --- el portador FRONTMATTER: a la izquierda el blanco es SINTAXIS (P265) ----------
chk("frontmatter ACEPTA el separador de un espacio", region_ok_frontmatter(" APAC"), True)
chk("frontmatter ACEPTA el separador de tres espacios",
    region_ok_frontmatter("   APAC"), True)
chk("frontmatter ACEPTA tabulador como separador", region_ok_frontmatter("\tAPAC"), True)
chk("frontmatter RECHAZA el blanco de la DERECHA (eso sigue siendo P248)",
    region_ok_frontmatter("APAC "), False)
chk("frontmatter RECHAZA la variante de balde", region_ok_frontmatter(" Latam"), False)
chk("frontmatter RECHAZA None", region_ok_frontmatter(None), False)
chk("y el validador de DATO rechaza lo que el de frontmatter acepta: son portadores distintos",
    (region_ok(" APAC"), region_ok_frontmatter(" APAC")), (False, True))

# --- la leniencia del detector, ahora REPORTADA (P267) -----------------------------
chk("reporta el guion, clasificado SEPARADOR", variants_in("North-America"),
    {("North-America", "North America", "SEPARADOR")})
chk("reporta el doble espacio, clasificado SEPARADOR", variants_in("North  America"),
    {("North  America", "North America", "SEPARADOR")})
chk("reporta la capitalizacion, clasificada CASO", variants_in("latam"),
    {("latam", "LATAM", "CASO")})
chk("no reporta nada cuando la grafia ES la del vocabulario", variants_in("LATAM"), set())
chk("no reporta nada cuando no hay region", variants_in("Licencia"), set())
chk("reporta las DOS de una celda con dos", variants_in("North-America / latam"),
    {("North-America", "North America", "SEPARADOR"), ("latam", "LATAM", "CASO")})
# 🔴 El caso que separa FORMATO de VARIANTE: la negrita se registra pero NO es accionable.
# Sin esta distincion el barrido sobre el arbol real devuelve 172 hallazgos de los cuales
# 164 son `**LATAM**`, y la cifra deja de significar algo. Ver P267.
chk("la negrita se registra como MARKUP", variants_in("**LATAM**"),
    {("**LATAM**", "LATAM", "MARKUP")})
chk("el emoji tambien es MARKUP", variants_in("🔴 **LATAM**"),
    {("🔴 **LATAM**", "LATAM", "MARKUP")})
chk("y el backtick", variants_in("`EMEA`"), {("`EMEA`", "EMEA", "MARKUP")})
chk("MARKUP NO es accionable", actionable_variants("**LATAM**"), set())
chk("CASO SI es accionable", actionable_variants("**latam**"),
    {("**latam**", "LATAM", "CASO")})
chk("SEPARADOR SI es accionable", actionable_variants("**North-America**"),
    {("**North-America**", "North America", "SEPARADOR")})

# --- EL CASO OBLIGATORIO: las dos funciones tienen que DISENTIR --------------------
# Si alguna vez una sola funcion sirviera a las dos preguntas, este bloque falla.
for v in DIVERGENCE:
    chk(f"DIVERGENCIA {v!r}: el validador rechaza", region_ok(v), False)
    chk(f"DIVERGENCIA {v!r}: y el detector SI la nombra",
        bool(regions_named(v, strict=False)), True)
chk("la clase de divergencia no esta vacia (si lo estuviera, el control no controla)",
    len(DIVERGENCE) > 0, True)

print()
print(f"{ok}/{n} checks passed")
sys.exit(0 if ok == n else 1)
