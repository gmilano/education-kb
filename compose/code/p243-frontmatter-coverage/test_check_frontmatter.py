#!/usr/bin/env python3
"""Suite de P243. Imprime su propio total (P126 regla 3).

El control que importa es el NEGATIVO: una suite que solo prueba el caso bueno no
habilita el instrumento (P126 regla 2). Aca el caso donde el instrumento puede fallar
es la VARIANTE de vocabulario regional — un valor que se lee perfectamente y no esta en
el vocabulario cerrado — y la de frontmatter CERRADO pero incompleto.
"""
import sys

from check_frontmatter import findings_for, parse_frontmatter, REGIONS

checks = []


def check(name, got, want):
    ok = got == want
    checks.append((name, ok, got, want))
    print("%s %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        print("     esperado: %r" % (want,))
        print("     obtenido: %r" % (got,))


OK = "---\nindustry: education\nregion: Global\nupdated: 2026-10-04\n---\n\n# Titulo\n"

# --- casos buenos -----------------------------------------------------------
check("frontmatter completo no produce hallazgo", findings_for("x.md", OK), [])
for r in REGIONS:
    body = OK.replace("region: Global", "region: %s" % r)
    check("region valida del vocabulario: %s" % r, findings_for("x.md", body), [])

# --- el caso que motivo el instrumento: NO hay frontmatter ------------------
check(
    "archivo que empieza con '# ' se marca NO-FRONTMATTER",
    findings_for("x.md", "# P238 — un titulo cualquiera\n\ntexto\n"),
    [("NO-FRONTMATTER", "")],
)
check(
    "archivo vacio se marca NO-FRONTMATTER",
    findings_for("x.md", ""),
    [("NO-FRONTMATTER", "")],
)
check(
    "frontmatter que nunca cierra NO se lee como valido",
    findings_for("x.md", "---\nindustry: education\nregion: Global\n"),
    [("UNCLOSED-FRONTMATTER", "")],
)

# --- el CONTROL NEGATIVO de P126 regla 2: variantes de vocabulario ---------
# Cada una se lee bien en Markdown y es un balde nuevo que rompe el filtro.
for bad in ("Latam", "LatAm", "Europe", "Asia Pacific", "Brazil", "global", "APAC "):
    body = OK.replace("region: Global", "region: %s" % bad)
    check(
        "variante de vocabulario rechazada: %r" % bad,
        findings_for("x.md", body),
        [("REGION-NOT-IN-VOCABULARY", bad.strip() if bad != "APAC " else "APAC")],
    )

# --- frontmatter cerrado pero incompleto -----------------------------------
check(
    "falta la clave region",
    findings_for("x.md", "---\nindustry: education\nupdated: 2026-10-04\n---\n"),
    [("MISSING-KEY", "region")],
)
check(
    "falta la clave industry",
    findings_for("x.md", "---\nregion: Global\nupdated: 2026-10-04\n---\n"),
    [("MISSING-KEY", "industry")],
)
check(
    "faltan dos claves y se reportan las dos",
    findings_for("x.md", "---\nregion: Global\n---\n"),
    [("MISSING-KEY", "industry"), ("MISSING-KEY", "updated")],
)

# --- el parser, por separado ------------------------------------------------
fields, err = parse_frontmatter(OK)
check("el parser extrae industry", fields.get("industry"), "education")
check("el parser extrae updated", fields.get("updated"), "2026-10-04")
check("el parser no reporta error en el caso bueno", err, None)
check(
    "un comentario dentro del bloque no rompe el parseo",
    parse_frontmatter("---\n# nota\nindustry: education\nregion: Global\nupdated: 2026-10-04\n---\n")[0].get("region"),
    "Global",
)

passed = sum(1 for _, ok, _, _ in checks if ok)
total = len(checks)
print("")
print("%d/%d checks passed" % (passed, total))
sys.exit(0 if passed == total else 1)
