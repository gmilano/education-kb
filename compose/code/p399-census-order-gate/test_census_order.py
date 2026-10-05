#!/usr/bin/env python3
"""Suite de p399-census-order-gate. Cada caso nombra la distincion que sostiene."""
import sys
sys.path.insert(0, ".")
from census_order import is_row, classify, census_lines, verdict, blind_spot, census_at

ok = fail = 0
def check(name, got, want):
    global ok, fail
    if got == want:
        ok += 1
    else:
        fail += 1
        print(f"FALLA\t{name}\tesperado={want!r}\tobtenido={got!r}")

C = lambda a, p, m: {"absent": a, "present": p, "mute": m, "universe": a + p + m}

# --- 1. el criterio heredado de P394 no se cambio ----------------------------
check("prosa-no-es-fila", is_row("el LICENSE mide 11.357 B, sha256 c71d239df917"), False)
check("separador-no-es-fila", is_row("|---|:--|"), False)
check("fila-si-es-fila", is_row("| `a/b` | MIT `c71d239df917` |"), True)
check("ausente-explicito", classify("| `a/b` | Apache-2.0 `c71d239df917` titular `NOT-APPLICABLE` |"), "absent")
check("presente-por-Copyright", classify("| `a/b` | MIT `c71d239df917` `Copyright (c) 2026 X` |"), "present")
check("mudo-no-dice-nada-del-titular", classify("| `a/b` | MIT **1.068 B** `c71d239df917` |"), "mute")
check("sin-huella-queda-fuera", classify("| `a/b` | MIT |"), None)
check("sin-licencia-queda-fuera", classify("| `a/b` | commit `c71d239df917` |"), None)

# --- 2. el veredicto: las tres salidas, y la que importa es la del medio -----
check("cifra-del-arbol-propio-es-OK",
      verdict(C(23, 46, 139), C(23, 46, 139), C(15, 46, 125))[0], "OK")
check("cifra-del-arbol-anterior-es-DESFASADO",
      verdict(C(15, 46, 125), C(23, 46, 139), C(15, 46, 125))[0], "DESFASADO")
check("cifra-de-ningun-arbol-es-DESCONOCIDO",
      verdict(C(99, 99, 99), C(23, 46, 139), C(15, 46, 125))[0], "DESCONOCIDO")

# --- 3. el caso que destapo P399, con las cifras exactas del pase 120 --------
check("el-caso-P394-sale-DESFASADO",
      verdict(C(15, 46, 125), C(23, 46, 139), C(15, 46, 125))[0], "DESFASADO")
check("y-el-universo-publicado-era-186", C(15, 46, 125)["universe"], 186)
check("y-el-universo-del-commit-era-208", C(23, 46, 139)["universe"], 208)

# --- 4. el punto ciego: por que ningun control agarraba el desfase ----------
# `presente` no se movio entre los dos arboles (46 -> 46), y es la unica columna
# que un lector verifica a mano porque es la que tiene nombres propios.
check("presente-es-el-punto-ciego-del-caso-real",
      blind_spot(C(23, 46, 139), C(15, 46, 125)), ["present"])
check("sin-punto-ciego-cuando-todo-se-mueve",
      blind_spot(C(23, 47, 139), C(15, 46, 125)), [])
check("arboles-identicos-son-todo-punto-ciego",
      blind_spot(C(15, 46, 125), C(15, 46, 125)),
      ["absent", "mute", "present", "universe"])

# --- 5. el control negativo que a la compuerta le faltaria sin esto ---------
# Un DESFASADO solo se puede afirmar si los dos arboles DIFIEREN. Si son iguales,
# la cifra describe los dos y el veredicto correcto es OK, no DESFASADO.
check("arboles-iguales-dan-OK-y-no-DESFASADO",
      verdict(C(15, 46, 125), C(15, 46, 125), C(15, 46, 125))[0], "OK")

# --- 6. un archivo ausente en la revision NO es un cero --------------------
# `census_at` omite el archivo que `git show` no encuentra y publica cuantos leyo,
# para que el llamador no confunda "no estaba" con "no tenia filas" (clase de P160).
c = census_at("HEAD", files=["no-existe-en-ningun-arbol.md"])
check("archivo-inexistente-no-cuenta-como-leido", c["files_read"], 0)
check("archivo-inexistente-no-inventa-filas", c["universe"], 0)

# --- 7. el conteo sobre lineas, directo ------------------------------------
check("censo-de-tres-filas-una-de-cada-clase",
      {k: v for k, v in census_lines([
          "| `a/b` | Apache-2.0 `c71d239df917` titular `NOT-APPLICABLE` |",
          "| `c/d` | MIT `de8107bf9312` `Copyright (c) 2026 X` |",
          "| `e/f` | MIT **1.068 B** `58f77360830f` |",
          "texto de prosa con `c71d239df917` y la palabra licencia",
      ]).items()}, C(1, 1, 1))

print(f"\n{ok}/{ok + fail} OK" + (f" — {fail} FALLAS" if fail else ""))
sys.exit(1 if fail else 0)
