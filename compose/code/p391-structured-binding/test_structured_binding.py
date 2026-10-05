#!/usr/bin/env python3
"""Suite de p391-structured-binding. Cada caso nombra el sesgo que demuestra."""
import sys
sys.path.insert(0, ".")
from structured_binding import (cells, repos_in, is_identity_cell, extract,
                                extract_typed, merge, clusters)

ok = fail = 0
def check(name, got, want):
    global ok, fail
    if got == want:
        ok += 1
    else:
        fail += 1
        print(f"FALLA\t{name}\tesperado={want!r}\tobtenido={got!r}")

# --- 1. cells(): distinguir fila de tabla de prosa -----------------------------
check("prosa-no-es-fila", cells("texto con sha256:abcdef123456 suelto"), None)
check("separador-no-es-fila", cells("|---|---|"), None)
check("fila-se-parte-en-celdas",
      cells("| `a/b` | MIT | `sha256:0123456789ab` |"),
      ["`a/b`", "MIT", "`sha256:0123456789ab`"])

# --- 2. el sesgo de co-ocurrencia: una celda de PROSA no liga -----------------
prosa = "Backend del chatbot de MIT que usa `VedShh/Tutor-AI` para resolver problemas del curso"
check("celda-de-prosa-NO-es-identidad", is_identity_cell(prosa, repos_in(prosa)), False)
check("celda-de-slug-SI-es-identidad",
      is_identity_cell("`vishalsachdev/canvas-mcp`", repos_in("`vishalsachdev/canvas-mcp`")), True)
check("celda-de-handles-pelados-SI-es-identidad",
      is_identity_cell("`sirdanielm` · `fdis111`", repos_in("`sirdanielm` · `fdis111`")), True)

# --- 3. el sesgo que el extractor anclado a URL tenia: handles pelados --------
handles = ["| 🟢 **`DERIVATIVE-OF vishalsachdev/canvas-mcp`** | **2** | `sirdanielm` · `fdis111` | "
           "`LICENSE` **1.071 B**, `sha256:5385a26e2face987` |"]
b, _ = extract(handles)
check("handles-pelados-ligados-y-calificados-por-el-ancla",
      b["5385a26e2fac"],
      {"sirdanielm/canvas-mcp", "fdis111/canvas-mcp"})
# PUNTO CIEGO PROPIO, declarado en la misma suite que lo produce: el repo canonico
# vive en una celda COMPUESTA (`DERIVATIVE-OF vishalsachdev/canvas-mcp`), que no es
# un slug entre backticks, asi que el lector lo usa como ANCLA para calificar los
# handles pero NO lo liga como miembro. El racimo que publica es por eso un PISO en
# su MEMBRESIA, aunque el conteo de racimos (lo que pedia la accion B) no se afecta.
check("punto-ciego-el-canonico-de-celda-compuesta-NO-se-liga",
      "vishalsachdev/canvas-mcp" in b["5385a26e2fac"], False)

# --- 4. control de co-ocurrencia: prosa en la MISMA fila no entra -------------
mixto = ["| `krishna16-origin/ai-tutor` | MIT, `sha256:de8107bf9312862c` | "
         "Tutor desplegado; nada que ver con `pupilfirst/pupilfirst` ni con el resto del parrafo |"]
b2, _ = extract(mixto)
check("co-ocurrencia-en-celda-de-prosa-NO-liga", b2["de8107bf9312"], {"krishna16-origin/ai-tutor"})

# --- 5. el punto ciego del extractor anclado al TOKEN -------------------------
# Tabla cuyo encabezado dice sha256 y cuyas celdas traen el hex pelado.
tabla = [
    "| repo | bytes | sha256 |",
    "|---|---|---|",
    "| `bibo242/blackboard-mcp` | 1.084 | `d65abf96e389134e` |",
    "| `felipedias-ie/blackboard-mcp` | 1.084 | `d65abf96e389134e` |",
]
ba, _ = extract(tabla)
check("anclado-al-token-NO-ve-la-columna-tipada", clusters(ba), {})
bt, _ = extract_typed(tabla)
check("columna-tipada-SI-la-ve",
      bt["d65abf96e389"],
      {"bibo242/blackboard-mcp", "felipedias-ie/blackboard-mcp"})

# --- 6. P392: dos columnas de huella en la misma tabla dan DOS racimos --------
dos_col = [
    "| repo | sha256 README | sha256 LICENSE |",
    "|---|---|---|",
    "| `a/opentutor` | `274d94acdd565ff4` | `5352b49679829689` |",
    "| `b/opentutor` | `274d94acdd565ff4` | `5352b49679829689` |",
]
bd, _ = extract_typed(dos_col)
check("P392-dos-columnas-de-huella-dan-dos-racimos", len(clusters(bd)), 2)
check("P392-y-los-dos-racimos-tienen-el-MISMO-conjunto-de-repos",
      len({frozenset(v) for v in clusters(bd).values()}), 1)

# --- 7. merge y control de convergencia --------------------------------------
check("merge-une-sin-perder", clusters(merge(ba, bt)).keys() == {"d65abf96e389"}, True)
uniforme = [
    "| `x/one` | MIT, `sha256:aaaaaaaaaaaa` |",
    "| `y/two` | MIT, `sha256:aaaaaaaaaaaa` |",
]
bu, _ = extract(uniforme)
check("control-convergencia-convencion-uniforme", len(clusters(bu)), 1)

# --- 8. ruido: una ruta de archivo no es un repo ------------------------------
check("ruta-no-es-repo", repos_in("`main/LICENSE`"), set())
check("id-de-patron-no-es-handle", repos_in("`P386`"), set())

print(f"\n{ok}/{ok+fail}")
sys.exit(1 if fail else 0)
