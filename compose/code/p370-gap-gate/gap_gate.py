#!/usr/bin/env python3
"""`p370-gap-gate/gap_gate.py` — la compuerta que `p311` no cubre: un hueco DECLARADO.

Pase 115 del 2026-10-05.

`p311-duplicate-alta-gate/` existe desde el pase 100 porque un ALTA estaba por publicarse
sobre piezas que la base YA TENIA. Ese gate contesta «¿esto ya esta aca?» para lo que ENTRA.

🔴 **Nada contestaba la pregunta simetrica para lo que se declara AUSENTE.** Un hueco
(«LATAM: CERO repositorios») es una afirmacion sobre el CONTENIDO PROPIO, igual que un
alta, y por lo tanto es falsable contra el indice propio — pero se publicaba sin control.

El pase 115 encontro dos instancias en el arbol, en archivos y ejes distintos:

1. `intel/market.md` declara **«CERO repositorios de origen LATAM»** por 4o pase
   consecutivo, mientras `agents/top.md:7125` publica `LabSirius/TutorIA` — **MIT**,
   **LATAM (Pereira, Colombia)**, Grupo Sirius de la Universidad Tecnologica de Pereira,
   financiado por el **SNCTI** colombiano, y marcado **ACTIVO** por esta misma base.
2. El pase 114 nombro la capa de evaluacion pedagogica como **`pedagogy-benchmark`
   (12 estrellas)**, mientras `repos/foundations.md:4262` trae `eth-lre/mathtutorbench`
   (**43 estrellas**, CC BY 4.0, ETH Zurich + CU Boulder, EMNLP 2025 oral) desde el pase 4.

🔵 **Y la discriminacion que hace honesto al instrumento (si no, marca todo hueco legitimo):**
un hueco de CANAL («este canal no encuentra codigo de LATAM») NO es contradecible por filas
del indice; un hueco de INDICE («la capa de CODIGO de LATAM sigue abierta») SI lo es.

El pase 113 escribio el suyo con el alcance puesto —«*no se publica como "LATAM no produce
codigo" — se publica como lo que es: este canal no encuentra codigo de LATAM*»— y hasta
nombro una pieza LATAM propia en la misma oracion. El 114 conservo el numero y solto el
alcance. 🔴 **Por eso el caso obligatorio de la suite es que las DOS oraciones reales del
arbol salgan con veredicto OPUESTO**: si el gate marcara las dos, seria un contador de la
palabra «CERO» y no una compuerta.

Uso:
    python3 gap_gate.py --self-test
    python3 gap_gate.py --sweep RAIZ      # barre los huecos declarados del arbol
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lib"))
from region import REGIONS, regions_named  # noqa: E402  (P237: no se reimplementa)

# Marcadores de ALCANCE. El de canal gana cuando aparecen los dos: el alcance mas
# ESTRECHO es el que quedo evidenciado, y creerle el ancho seria el error de P371.
CHANNEL_MARKERS = (
    r"este canal",
    r"esta consulta",
    r"lo buscado este pase",
    r"no devuelve c[oó]digo",
    r"el barrido devolvi[oó]",
    r"no encuentra c[oó]digo",
    r"hay que cambiar de canal",
    r"un informado hueco",
)
INDEX_MARKERS = (
    r"la capa de c[oó]digo de \w+ sigue abierta",
    r"cero repositorios de origen",
    r"esta base no tiene",
    r"esta kb no tiene",
    r"no hay ninguna pieza",
    r"la capa de \w+ es `?[\w.-]+`?,? \(?\d+ estrellas",
)

SCOPE_CHANNEL = "CANAL"
SCOPE_INDEX = "INDICE"
SCOPE_UNDETERMINED = "SIN-ALCANCE"

V_CONTRADICHO = "CONTRADICHO"
V_SOSTENIDO = "SOSTENIDO"
V_NO_CLAIM = "NO-CLAIM"


def scope_of(claim):
    """Clasifica el ALCANCE de un hueco declarado.

    El marcador de CANAL gana sobre el de INDICE a proposito: una oracion que dice las
    dos cosas quedo evidenciada solo en la estrecha.
    """
    low = claim.lower()
    has_channel = any(re.search(m, low) for m in CHANNEL_MARKERS)
    has_index = any(re.search(m, low) for m in INDEX_MARKERS)
    if has_channel:
        return SCOPE_CHANNEL
    if has_index:
        return SCOPE_INDEX
    return SCOPE_UNDETERMINED


# 🔴 La region de una PROSA es una TERCERA pregunta, y no se puede contestar con las dos
# de `lib/region.py`. Aquel modulo documenta dos contratos opuestos —VALIDADOR de campo y
# DETECTOR de CELDA— y los dos presuponen un portador DELIMITADO: `regions_named` parte por
# `/`, `,` y ` y `, y exige que cada parte sea IGUAL a un nombre de region. Sobre la oracion
# «La capa de CODIGO de LATAM sigue abierta» devuelve `set()` con los dos valores de
# `strict`, porque la oracion no es una celda. Pasarle `strict=False` NO la convierte en un
# lector de prosa: solo apaga el control de residuo, que es el arreglo que P265/P266 pagaron.
# 🔵 Asi que aca se nombra la tercera pregunta en vez de estirar una de las dos (`P263`).
def region_in_prose(text):
    """TERCERA pregunta: que regiones del vocabulario CERRADO nombra una prosa.

    Limite de palabra, no subcadena, y nada fuera de las cinco: `Brasil` no es una region
    de este vocabulario y tiene que salir vacio (el error que `P135`/`P368` ya costaron).
    """
    out = set()
    for r in REGIONS:
        if re.search(r"(?<![\w])" + re.escape(r) + r"(?![\w])", text, re.IGNORECASE):
            out.add(r)
    return out


def region_claimed(claim):
    """La region sobre la que el hueco afirma. `None` si no nombra exactamente una."""
    named = region_in_prose(claim)
    return next(iter(named)) if len(named) == 1 else None


def repo_rows(text):
    """Filas de tabla publicadas que nombran un repo de GitHub, con su celda de region."""
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.startswith("|") or "github.com/" not in line:
            continue
        m = re.search(r"github\.com/([\w.-]+/[\w.-]+)", line)
        if not m:
            continue
        # 🔴 Aca NO sirve el detector de celda, y el motivo esta medido en `test_`: las
        # celdas de region de ESTA base mezclan region con atribucion —`**LATAM (Pereira,
        # Colombia)** - Grupo Sirius, Universidad Tecnologica de Pereira`—, y `strict=True`
        # (su default, que es parte de su contrato) las rechaza por RESIDUO y devuelve
        # `set()`. Usarlo aca haria que el gate SOSTENGA el hueco falso por falso negativo,
        # o sea que coincidiria con el pase 114 por el motivo contrario.
        # 🔵 La pregunta correcta sobre una fila de repo es la de PROSA, y es segura aqui
        # porque la linea ya quedo restringida a filas con URL de GitHub: el riesgo que
        # `strict` existe para cubrir —leer como regional una celda de CIFRAS tipo
        # `86 % NA / 92 % LATAM`— vive en filas SIN repo, que este filtro ya descarto.
        rows.append((n, m.group(1).rstrip("."), region_in_prose(line)))
    return rows


# Una fila puede NOMBRAR una region de tres formas distintas, y solo una es una
# UBICACION: `| ... | 🟢 **LATAM** (Brasil) |` la coloca; `fuerte en LATAM y EMEA` habla de
# su MERCADO (`P368`: la region del proveedor no es la region de su mercado); y
# `el primer alta LATAM de esta KB` es prosa del pase. El piso se mide con la primera.
PLACEMENT = re.compile(r"^(?:[^\w(]|\*\*)*(" + "|".join(REGIONS) + r")\b", re.IGNORECASE)


def placement_cells(line):
    """Celdas de la fila donde la region ENCABEZA la celda, que es como esta base ubica."""
    out = []
    for cell in line.split("|"):
        c = cell.strip()
        if not c or len(c) > 140:
            continue
        m = PLACEMENT.match(c)
        if m:
            out.append((m.group(1).upper() if m.group(1).upper() in ("EMEA", "APAC", "LATAM")
                        else m.group(1), c))
    return out


def placed_in(line, region):
    """True si la fila UBICA el repo en `region` (y no solo la menciona)."""
    return any(r.upper() == region.upper() for r, _ in placement_cells(line))


def contradicting_rows(claim, tree_files):
    """Filas del indice propio que contradicen un hueco de INDICE sobre una region."""
    reg = region_claimed(claim)
    if reg is None:
        return []
    out = []
    for path, text in tree_files:
        lines = text.splitlines()
        for n, slug, regs in repo_rows(text):
            if reg in regs:
                out.append((path, n, slug, reg, placed_in(lines[n - 1], reg)))
    return out


def verdict(claim, tree_files):
    """(veredicto, alcance, region, filas_que_contradicen)."""
    scope = scope_of(claim)
    reg = region_claimed(claim)
    if scope != SCOPE_INDEX:
        # Un hueco de canal es una afirmacion sobre la CONSULTA, no sobre el arbol:
        # ninguna fila del indice lo puede refutar.
        return V_NO_CLAIM if scope == SCOPE_UNDETERMINED else V_SOSTENIDO, scope, reg, []
    rows = contradicting_rows(claim, tree_files)
    return (V_CONTRADICHO if rows else V_SOSTENIDO), scope, reg, rows


def read_tree(root, names=("agents", "repos", "verticals", "intel", "compose")):
    out = []
    for d in names:
        p = os.path.join(root, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if f.endswith(".md"):
                fp = os.path.join(p, f)
                with open(fp, encoding="utf-8") as fh:
                    out.append((os.path.join(d, f), fh.read()))
    return out


GAP_SENTENCE = re.compile(
    r"[^.\n]*(?:hueco|cero repositorios|sigue abierta)[^.\n]*\.", re.IGNORECASE)


def sweep(root):
    tree = read_tree(root)
    seen, rows = set(), []
    for path, text in tree:
        for s in GAP_SENTENCE.findall(text):
            s = " ".join(s.split())
            if len(s) < 40 or s in seen:
                continue
            seen.add(s)
            v, scope, reg, hits = verdict(s, tree)
            if reg is None:
                continue
            rows.append((path, v, scope, reg, len(hits), s[:110]))
    return rows


def main(argv):
    if "--self-test" in argv:
        import test_gap_gate
        return test_gap_gate.run()
    if "--sweep" in argv:
        root = argv[argv.index("--sweep") + 1]
        rows = sweep(root)
        by_v = {}
        for path, v, scope, reg, nhits, s in rows:
            by_v[v] = by_v.get(v, 0) + 1
            print(f"{v:<12} {scope:<12} {reg:<14} filas={nhits:<3} {path}  {s}")
        print(f"\n# huecos con region: {len(rows)}  " +
              "  ".join(f"{k}={v}" for k, v in sorted(by_v.items())))
        return 0 if rows else 1
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
