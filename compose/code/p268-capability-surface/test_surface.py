#!/usr/bin/env python3
"""Suite de P268. Imprime su total propio (punto 3 de la regla de P126).

Los controles que HABILITAN el instrumento, y por que cada uno existe:

1. 🔴 **Control NEGATIVO del conflicto**: dos superficies que dicen LO MISMO no son
   conflicto. Sin este caso, un instrumento que siempre devuelve «conflicto» saca 100 % en
   las filas reales —las dos que hay conflictuan— y pasa la suite. Es la regla de **P126**:
   un control sólo habilita si ejercita el caso donde el instrumento puede fallar.
2. 🔴 **Control del tri-estado**: un repo con UNA sola superficie medida tiene que salir
   `COTA-DE-INSTRUMENTO`, no `CITABLE`. La primera version lo daba por acuerdo.
3. 🔴 **`NO-CLAIM` no es cero**: un conteo ausente no puede entrar a la comparacion como un
   conteo bajo, porque eso inventa un conflicto que no se midio.

    python3 test_surface.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from surface import (CITABLE, NO_CITABLE, UNDER, as_int, citable,  # noqa: E402
                     frozen_claim, intra_repo_conflict, load, vocab_ok)

n = ok = 0


def chk(label, got, want):
    global n, ok
    n += 1
    if got == want:
        ok += 1
        print(f"PASS {label}")
    else:
        print(f"FAIL {label}: got {got!r} want {want!r}")


rows = load()

# --- las filas medidas, tal como se leyeron el 2026-10-04 --------------------------
chk("hay 5 mediciones de superficie", len(rows), 5)
chk("sobre 3 repos", len({r['slug'] for r in rows}), 3)
chk("el vocabulario de superficie y rol esta cerrado", vocab_ok(rows), True)
chk("un solo UPSTREAM", len({r['slug'] for r in rows if r['rol'] == 'UPSTREAM'}), 1)
chk("y dos FORKs", len({r['slug'] for r in rows if r['rol'] == 'FORK'}), 2)
chk("todas las licencias medidas son MIT", {r['licencia'] for r in rows}, {"MIT"})

# --- el hallazgo: el upstream se contradice consigo mismo --------------------------
conflict, mine = intra_repo_conflict(rows, "vishalsachdev/canvas-mcp")
chk("el upstream tiene conflicto intra-repo", conflict, True)
chk("y es 102 en la descripcion contra 103 en el README",
    (mine["DESCRIPTION"], mine["README-BODY"]), (102, 103))
chk("asi que su conteo NO es citable sin superficie",
    citable(rows, "vishalsachdev/canvas-mcp"), NO_CITABLE)

# --- el fork hereda la contradiccion y la agranda ----------------------------------
conflict, mine = intra_repo_conflict(rows, "jsrodr/canvas-mcp")
chk("jsrodr tambien conflictua", conflict, True)
chk("80 en la descripcion contra 99 en el README",
    (mine["DESCRIPTION"], mine["README-BODY"]), (80, 99))

# --- el claim CONGELADO ------------------------------------------------------------
for slug in ("harrywang/canvas-mcp", "jsrodr/canvas-mcp"):
    frozen, _why = frozen_claim(rows, slug)
    chk(f"{slug} repite un claim que el upstream ya no publica", frozen, True)
chk("el upstream no puede tener claim congelado contra si mismo",
    frozen_claim(rows, "vishalsachdev/canvas-mcp")[0], False)

# --- CONTROL 2: tri-estado. Una sola superficie NO es acuerdo ----------------------
chk("harrywang, con UNA superficie medida, sale COTA-DE-INSTRUMENTO",
    citable(rows, "harrywang/canvas-mcp"), UNDER)
chk("y NO sale CITABLE", citable(rows, "harrywang/canvas-mcp") == CITABLE, False)
chk("CERO repos del cohorte son citables sin nombrar superficie",
    [s for s in {r['slug'] for r in rows} if citable(rows, s) == CITABLE], [])

# --- CONTROL 1 (NEGATIVO): dos superficies que COINCIDEN no son conflicto ---------
# Si este caso fallara, un instrumento que grita «conflicto» siempre pasaria la suite.
acuerdo = [
    {"slug": "x/y", "rol": "FORK", "superficie": "DESCRIPTION", "herramientas": "42",
     "skills": "3", "release": "v1", "licencia": "MIT", "estrellas": "0"},
    {"slug": "x/y", "rol": "FORK", "superficie": "README-BODY", "herramientas": "42",
     "skills": "3", "release": "v1", "licencia": "MIT", "estrellas": "0"},
]
chk("CONTROL NEGATIVO: dos superficies iguales NO conflictuan",
    intra_repo_conflict(acuerdo, "x/y")[0], False)
chk("CONTROL NEGATIVO: y con dos superficies de acuerdo el veredicto SI es CITABLE",
    citable(acuerdo, "x/y"), CITABLE)

# --- CONTROL 3: NO-CLAIM no es cero ------------------------------------------------
chk("as_int('NO-CLAIM') es None, no 0", as_int("NO-CLAIM"), None)
chk("as_int('0') si es 0", as_int("0"), 0)
sin_claim = [
    {"slug": "x/z", "rol": "FORK", "superficie": "DESCRIPTION", "herramientas": "42",
     "skills": "3", "release": "v1", "licencia": "MIT", "estrellas": "0"},
    {"slug": "x/z", "rol": "FORK", "superficie": "README-BODY",
     "herramientas": "NO-CLAIM", "skills": "NO-CLAIM", "release": "v1",
     "licencia": "MIT", "estrellas": "0"},
]
chk("un NO-CLAIM no inventa conflicto", intra_repo_conflict(sin_claim, "x/z")[0], False)
chk("pero tampoco cuenta como segunda superficie: queda COTA-DE-INSTRUMENTO",
    citable(sin_claim, "x/z"), UNDER)

# --- un repo que no se midio no se afirma -----------------------------------------
chk("un slug sin filas no rinde conflicto", intra_repo_conflict(rows, "no/existe")[0], False)
chk("y su claim congelado es False con motivo",
    frozen_claim(rows, "no/existe"), (False, "sin medicion"))

print()
print(f"{ok}/{n} checks passed")
sys.exit(0 if ok == n else 1)
