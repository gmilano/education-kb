#!/usr/bin/env python3
"""Suite de p394-holder-absent-census. Cada caso nombra la distincion que sostiene."""
import sys
sys.path.insert(0, ".")
from holder_census import is_row, classify, census

ok = fail = 0
def check(name, got, want):
    global ok, fail
    if got == want:
        ok += 1
    else:
        fail += 1
        print(f"FALLA\t{name}\tesperado={want!r}\tobtenido={got!r}")

# --- 1. universo: una linea de prosa no es una fila ---------------------------
check("prosa-no-es-fila", is_row("el LICENSE mide 11.357 B, sha256 c71d239df917"), False)
check("separador-no-es-fila", is_row("|---|---|"), False)
check("fila-si-es-fila", is_row("| `a/b` | MIT `c71d239df917` |"), True)
check("prosa-con-huella-queda-FUERA-del-universo",
      classify("prosa con `c71d239df917` y la palabra licencia")[0], None)

# --- 2. las tres clases de titular -------------------------------------------
check("ausente-explicito-NOT-APPLICABLE",
      classify("| `a/b` | Apache-2.0, 11.357 B, `c71d239df917`, titular `NOT-APPLICABLE` |")[0],
      "absent")
check("ausente-explicito-sin-titular",
      classify("| `a/b` | Unlicense, 1.212 B, `b5065838cbac`, **sin titular** |")[0], "absent")
check("presente",
      classify("| `a/b` | MIT 1.071 B `5385a26e2face987` titular `Vishal Sachdev` |")[0], "present")
check("mudo-la-fila-no-dice-nada-del-titular",
      classify("| `a/b` | MIT | 1.071 B | `5385a26e2face987` | 3 estrellas |")[0], "mute")

# --- 3. la distincion que manda: MUDO no es AUSENTE --------------------------
# Regla de la clase de P160: la ausencia de la PALABRA no es la ausencia del TITULAR.
muda = "| `a/b` | MIT | `5385a26e2face987` |"
check("P394-mudo-NO-se-cuenta-como-ausente", classify(muda)[0] != "absent", True)

# --- 4. una fila sin huella no entra, aunque hable de licencia ---------------
check("sin-huella-queda-fuera", classify("| `a/b` | MIT | 1.071 B |")[0], None)
# ...y una con huella pero sin mencion de licencia tampoco
check("sin-mencion-de-licencia-queda-fuera",
      classify("| `a/b` | commit `0123456789abcdef` | 3 |")[0], None)

# --- 5. bytes de boilerplate pristino, como evidencia SEPARADA --------------
check("pristino-por-bytes-apache",
      classify("| `a/b` | Apache-2.0 **11.357 B** `c71d239df917` `NOT-APPLICABLE` |")[1], True)
check("pristino-por-bytes-gpl3",
      classify("| `a/b` | GPL-3.0 **35.187 B** `f7fe4d0abcde` sin titular |")[1], True)
check("no-pristino-mit-1071",
      classify("| `a/b` | MIT **1.071 B** `5385a26e2face987` `NOT-APPLICABLE` |")[1], False)

# --- 6. el censo completo, con su clausula ----------------------------------
rows = [
    ("f", 1, "| `a/b` | Apache-2.0 11.357 B `c71d239df917` `NOT-APPLICABLE` |"),
    ("f", 2, "| `c/d` | Apache-2.0 11.357 B `c71d239df917` sin titular |"),
    ("f", 3, "| `e/f` | MIT 1.071 B `5385a26e2face987` titular `Vishal Sachdev` |"),
    ("f", 4, "| `g/h` | MIT | `5385a26e2face987` |"),
]
counts, pristine, listed = census(rows)
check("censo-cuenta-las-tres-clases",
      (counts["absent"], counts["present"], counts["mute"]), (2, 1, 1))
check("censo-pristinas-entre-las-ausentes", pristine, 2)
check("censo-lista-cada-fila-ausente", len(listed), 2)

# --- 7. control de la clausula pre-registrada (>=5 confirma, <=2 refuta) ----
pocas = [("f", i, "| `x/y` | MIT 1.071 B `5385a26e2face987` `NOT-APPLICABLE` |") for i in range(2)]
check("clausula-con-2-ausentes-seria-REFUTADA", census(pocas)[0]["absent"] <= 2, True)
muchas = [("f", i, "| `x/y` | MIT 1.071 B `5385a26e2face987` `NOT-APPLICABLE` |") for i in range(5)]
check("clausula-con-5-ausentes-seria-CONFIRMADA", census(muchas)[0]["absent"] >= 5, True)

print(f"\n{ok}/{ok+fail}")
sys.exit(1 if fail else 0)
