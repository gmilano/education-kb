#!/usr/bin/env python3
"""Controles de P251. Positivos Y negativos, y los negativos son los que importan.

Regla de P126: este archivo publica su total en la forma `N/N`, una sola vez,
y el que vale es el codigo de salida.
Regla de P241 (fixtures): ningun fixture es TRUNCADO — los textos de licencia
de los controles llevan la linea de copyright COMPLETA, que es el dato del eje.
"""
import sys
from lineage import (classify, paternity_claim, match_strength, holder_name, read_tsv)

ok = 0; fail = 0
def chk(label, got, want):
    global ok, fail
    if got == want:
        ok += 1
    else:
        fail += 1
        print(f"  FALLA: {label}\n     esperado: {want!r}\n     obtenido: {got!r}")

def row(slug, holder, sha="deadbeefdeadbeef", code="200"):
    return {"slug": slug, "lic_code": code, "lic_sha16": sha, "holder": holder}

# ---------------------------------------------------------------- 1. el ANO no es el titular
chk("holder_name descarta el ano", holder_name("Copyright (c) 2024 R.Huijts"), "R.Huijts")
chk("holder_name descarta (c) y copyright", holder_name("Copyright (c) 2025 Vishal Sachdev"), "Vishal Sachdev")
chk("holder_name sobre '-' da vacio", holder_name("-"), "")

# ---------------------------------------------------------------- 2. correspondencia titular~dueno
chk("STRONG con punto intercalado", match_strength("Copyright (c) 2024 R.Huijts", "r-huijts"), "STRONG")
chk("STRONG nombre completo", match_strength("Copyright (c) 2025 Vishal Sachdev", "vishalsachdev"), "STRONG")
chk("STRONG con acento (NFKD)", match_strength("Copyright (c) 2025 Charlie Cárdenas Toledo",
                                               "CharlieCardenasToledo"), "STRONG")
chk("WEAK con apellido-nombre invertido", match_strength("Copyright (c) 2026 Christian Bru", "bruchris"), "WEAK")
chk("NONE titular colectivo", match_strength("Copyright (c) 2023 Canvas LMS MCP Server Contributors",
                                             "ahnopologetic"), "NONE")
# el control que impide que el ANO produzca correspondencias
chk("el ano NO produce correspondencia", match_strength("Copyright (c) 2025 Someone Else", "2025"), "NONE")

# ---------------------------------------------------------------- 3. origen vs derivado
coh = [row("vishalsachdev/canvas-mcp", "Copyright (c) 2025 Vishal Sachdev", "5385a26e2face987"),
       row("fdis111/canvas-mcp",       "Copyright (c) 2025 Vishal Sachdev", "5385a26e2face987")]
cl = classify(coh)
chk("el dueno-titular es ORIGEN, no su propio fork",
    cl["vishalsachdev/canvas-mcp"][0], "ORIGIN-CANDIDATE")
chk("titular de un tercero es DERIVADO",
    cl["fdis111/canvas-mcp"], ("DERIVATIVE-OF", "vishalsachdev/canvas-mcp"))

# ---------------------------------------------------------------- 4. LA COTA: mismo hash != linaje
#  dos repos del MISMO autor, byte a byte identicos, y NINGUNO es fork del otro.
same_author = [row("acme/alpha", "Copyright (c) 2025 Acme Corp", "aaaa0000aaaa0000"),
               row("acme/beta",  "Copyright (c) 2025 Acme Corp", "aaaa0000aaaa0000")]
cl2 = classify(same_author)
chk("mismo hash + mismo dueno -> los DOS son origen, ninguno derivado",
    (cl2["acme/alpha"][0], cl2["acme/beta"][0]), ("ORIGIN-CANDIDATE", "ORIGIN-CANDIDATE"))
chk("y por lo tanto ninguno reclama paternidad del otro",
    paternity_claim(same_author, "acme/alpha"), ("NO-CLAIM", 0))

# ---------------------------------------------------------------- 5. ausencia -> UNDETERMINED, nunca INDEPENDENT
no_lic = [row("x/y", "-", "-", code="404")]
chk("sin licencia es UNDETERMINED", classify(no_lic)["x/y"][0], "UNDETERMINED")
chk("sin licencia NO es INDEPENDENT", classify(no_lic)["x/y"][0] != "INDEPENDENT", True)

# ---------------------------------------------------------------- 6. LA COMPUERTA DE P251
#  el control negativo es la afirmacion LITERAL del pase 82: que r-huijts/canvas-mcp
#  es el padre de la capa Canvas-MCP de esta base. Sobre el cohorte MEDIDO debe
#  salir NO-CLAIM, y debe salir NO-CLAIM aunque el candidato tenga 0 menciones.
real = read_tsv("rows.tsv")
chk("la afirmacion del pase 82 sale NO-CLAIM sobre el cohorte medido",
    paternity_claim(real, "r-huijts/canvas-mcp"), ("NO-CLAIM", 0))
chk("el padre MEDIDO del racimo grande es vishalsachdev, con 6 derivados",
    paternity_claim(real, "vishalsachdev/canvas-mcp"), ("PARENT", 6))
chk("el padre MEDIDO del racimo chico es bruchris, con 1 derivado",
    paternity_claim(real, "bruchris/canvas-lms-mcp"), ("PARENT", 1))
# y el control que da nombre al patron: CERO menciones no es paternidad
chk("un candidato con CERO derivados medidos no es padre por ausencia de menciones",
    paternity_claim([row("ghost/none", "Copyright (c) 2024 Ghost", "ffff1111ffff1111")],
                    "ghost/none"), ("NO-CLAIM", 0))

# ---------------------------------------------------------------- 7. el cohorte real, invariantes
chk("el cohorte real tiene 17 slugs", len(real), 17)
chk("17 slugs DISTINTOS (0 duplicados)", len({r["slug"] for r in real}), 17)
clr = classify(real)
chk("7 derivados medidos", sum(1 for v in clr.values() if v[0] == "DERIVATIVE-OF"), 7)
chk("6 candidatos a origen", sum(1 for v in clr.values() if v[0] == "ORIGIN-CANDIDATE"), 6)
chk("4 indeterminados", sum(1 for v in clr.values() if v[0] == "UNDETERMINED"), 4)
chk("el reparto suma el cohorte", 7 + 6 + 4, len(real))
chk("r-huijts es ORIGEN pero SIN derivados en el cohorte",
    (clr["r-huijts/canvas-mcp"][0], paternity_claim(real, "r-huijts/canvas-mcp")[1]),
    ("ORIGIN-CANDIDATE", 0))

print(f"\n{ok}/{ok+fail}")
sys.exit(1 if fail else 0)
