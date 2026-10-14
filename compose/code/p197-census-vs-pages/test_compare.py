#!/usr/bin/env python3
"""Suite de `compare.py`.  OFFLINE.  Las dos primeras cajas son las dos acusaciones
FALSAS que la v1 de este comparador emitio en esta misma pasada, con el texto real de
las paginas; la tercera es una contradiccion VERDADERA, sintetica, que tiene que seguir
disparando.  Sin la tercera, un comparador que nunca acusa pasaria esta suite.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compare

n = f = 0
def check(name, want, got):
    global n, f
    n += 1
    if want == got:
        print("ok   %-58s %s" % (name, got))
    else:
        print("FAIL %-58s want=%s got=%s" % (name, want, got)); f += 1

def row(slug, byts, fam="MIT"):
    return [slug, "YES", "100", "ROOT", "LICENSE", byts, fam, "READ"]

def verdict(pages, r):
    return compare.classify_rows(pages, [r])[0][5]

# --- C1: el tamanio del README, declarado como tal.  Texto real de agents/top.md -------
P1 = {"agents/top.md":
      "| \U0001f534 [`midudev/libros-programacion-gratis`](https://github.com/midudev/libros-programacion-gratis) "
      "| `6 072` | same | \U0001f534 **all `404`; README (`50 266` B) mentions no licence** |"}
check("C1 README bytes no son una concesion",
      "SLUG-NO-FIGURE", verdict(P1, row("midudev/libros-programacion-gratis", "0", "-")))

# --- C2: dos slugs en la misma celda.  Texto real de intel/trends.md (`T5`) ------------
P2 = {"intel/trends.md":
      "| `T5` | **Copyleft has moved into the CONTENT layer** | "
      "`GarethManning/education-agent-skills` `LICENSE` `1 230` B; "
      "`O0000-code/awesome-academic-skills` `CC0-1.0` |"}
check("C2 una cifra de OTRO slug en la celda no acusa",
      "MULTI-SLUG-LINE", verdict(P2, row("O0000-code/awesome-academic-skills", "7048", "CC0-1.0")))

# --- C3: contradiccion VERDADERA: un solo slug, una cifra de concesion distinta --------
P3 = {"repos/foundations.md":
      "| [`acme/widget`](https://github.com/acme/widget) | `MIT` *(`LICENSE`, `1 071` B)* | ok |"}
check("C3 una contradiccion real SI dispara",
      "DISAGREE", verdict(P3, row("acme/widget", "1234")))

# --- C4: acuerdo, con la grafia de millar que usan estas paginas -----------------------
P4 = {"repos/foundations.md":
      "| [`acme/widget`](https://github.com/acme/widget) | `MIT` *(`LICENSE`, `11 348` B)* |"}
check("C4 acuerdo con separador de millar de espacio",
      "AGREE-PUBLISHED", verdict(P4, row("acme/widget", "11348")))
P5 = {"repos/foundations.md": "| `acme/widget` | `MIT` (`LICENSE`, `11,348` B) |"}
check("C4b acuerdo con separador de coma",
      "AGREE-PUBLISHED", verdict(P5, row("acme/widget", "11348")))
P6 = {"repos/foundations.md": "| `acme/widget` | `MIT` (`LICENSE`, `11 348` B) |"}
check("C4c acuerdo con espacio duro",
      "AGREE-PUBLISHED", verdict(P6, row("acme/widget", "11348")))

# --- C5: el slug que no esta en ninguna pagina ----------------------------------------
check("C5 ausente de las paginas no es desacuerdo",
      "SLUG-ABSENT", verdict({"agents/top.md": "nada que ver"}, row("acme/widget", "1071")))

# --- C6: una fila sin bytes (ABSENCE) no puede ACORDAR con nada -----------------------
P7 = {"agents/top.md": "| `acme/widget` | sin fichero de licencia |"}
check("C6 fila sin bytes: no AGREE, no DISAGREE",
      "SLUG-NO-FIGURE", verdict(P7, row("acme/widget", "0", "-")))

# --- C7: las estrellas no son bytes ---------------------------------------------------
P8 = {"agents/top.md": "| `acme/widget` | `833`★; MIT |"}
check("C7 un conteo de estrellas no es una cifra de concesion",
      "SLUG-NO-FIGURE", verdict(P8, row("acme/widget", "1071")))

# --- C8: el conteo de rutas tampoco --------------------------------------------------
P9 = {"agents/top.md": "| `acme/widget` | `5 345` paths; sin licencia |"}
check("C8 un conteo de rutas no es una cifra de concesion",
      "SLUG-NO-FIGURE", verdict(P9, row("acme/widget", "1071")))

print()
print("%d/%d" % (n - f, n))
sys.exit(1 if f else 0)
