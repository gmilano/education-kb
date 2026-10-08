#!/usr/bin/env python3
"""`p598-register-freshness-gate/freshness_gate.py` — `Gap 252`, remedio 2.

Pase 49 del 2026-10-08.

`Gap 252` nombro tres remedios y dejo dos abiertos. El que declaro **«the honest next
instrument»** es este: *«no row may carry "cheapest/next win" unless re-asserted by the
latest pass that touched it»* — una CONVENCION mas un CONTROL. Aca esta el control.

🔴 **Y este pase es la prueba viva de que no era opcional.** El pase 49 leyo el registro
de arriba hacia abajo, encontro la fila de `Gap 246` diciendo que las licencias de los
artefactos `pt_core_news_*` **«are unmeasured»**, y gasto presupuesto volviendolas a
medir. Ya estaban medidas: `verticals/solutions.md:258` las publica como
**CC-BY-SA-4.0** y hasta dice *«was published as "unmeasured", now measured»*.
🔵 **`P582` (pase 48) encontro el mismo defecto por INSPECCION sobre `Gap 39`; el pase 49
lo encontro PAGANDOLO.** Dos instancias, dos filas distintas, dos descubrimientos
independientes: el defecto no esta confinado a `Gap 39`.

## La discriminacion que lo hace una compuerta y no un contador de palabras

🔴 El error facil es marcar toda fila que diga «unmeasured». La mayoria tienen razon:
`Gap 244` dice que 31 instrumentos de shell estan sin juzgar y **siguen sin juzgarse**.
Marcarla seria el error de `P371` — creerle al alcance ancho — y dejaria el instrumento
inservible por ruido.

🔵 Una fila esta RANCIA solo si el arbol VIVO la contradice:

1. la fila hace una **afirmacion de frescura** — de MEDICION (`unmeasured`, `untested`)
   o de PRIORIDAD (`cheapest remaining win`, `smallest gap`); y
2. el arbol vivo (los ocho archivos de trabajo, **nunca el registro mismo**) trae una
   linea que nombra el **mismo sujeto** de la fila **y** carga un **marcador de
   medicion** (un veredicto de licencia, un conteo de bytes de payload, un SHA, o la
   frase «now measured» / «read first-hand»).

🔴 **Sin la condicion 2 no hay hallazgo.** Una fila que dice «unmeasured» cuyo sujeto
aparece en el arbol solo en PROSA queda **SOSTENIDA**, no rancia.

🔴 **El caso obligatorio de la suite es que dos filas REALES de este arbol salgan con
veredicto OPUESTO** — `Gap 246` RANCIA (medida en `verticals/`) y `Gap 244` SOSTENIDA
(sus 31 filas de shell siguen sin oraculo). Si marcara las dos, seria un `grep`.

## El sujeto, y por que no se puede usar cualquier token

🔴 Las filas estan llenas de tokens entrecomillados que NO son sujetos: `Gap 246`, `P544`,
`P504`, nombres de archivo (`agents/top.md`) y palabras sueltas. Un sujeto es un
**identificador de artefacto** — `pt_core_news_*`, `es_core_news_sm`, `EqUMP`, `qti3` —
y se reconoce por forma, con los no-sujetos excluidos por lista explicita.

Uso:
    python3 freshness_gate.py --self-test
    python3 freshness_gate.py --sweep RAIZ
"""
import os
import re
import sys

# --- Afirmaciones de frescura -------------------------------------------------
# Dos clases, a proposito: `Gap 252` nombra la de PRIORIDAD como «la que engania mas
# fuerte», porque una recomendacion se ACTUA sin re-derivarse.
MEASUREMENT_CLAIM = (
    r"\bare unmeasured\b", r"\bis unmeasured\b", r"\bunmeasured\b",
    r"\bstill untested\b", r"\buntested\b",
    r"\bnot known to\b", r"\bsin medir\b", r"\bno probado\b",
    r"\bunjudged\b", r"\bunadjudicated\b", r"\bno measurement\b",
)
PRIORITY_CLAIM = (
    r"cheapest remaining win", r"cheapest gap", r"smallest gap",
    r"cheapest\b[^.|]{0,40}\bon this KB", r"\bnext win\b",
)

CLASS_MEASUREMENT = "MEDICION"
CLASS_PRIORITY = "PRIORIDAD"

V_RANCIA = "RANCIA"
V_SOSTENIDA = "SOSTENIDA"
V_NO_CLAIM = "NO-CLAIM"
V_CITA = "CITA"

# 🔴 Marcadores de CORRECCION. Una fila que CITA una afirmacion superada y trae su
# correccion al lado NO esta rancia: es el acto de corregir. El barrido v1 marco tres
# filas asi —las tablas «The rows pass N changed»— y marcarlas invierte el sentido del
# instrumento: castigaria exactamente la practica que `Gap 252` pide.
CORRECTION_MARKERS = (
    r"SUPERSEDED", r"DO NOT ACT ON THIS ROW", r"forward pointer",
    r"\bTESTED, and it splits\b", r"\bCERRADO\b", r"\bCLOSED\b",
    r"Pass \d+ said", r"Pase \d+ dijo", r"\bPass \d+ says\b",
    r"was overturned", r"re-adjudicat",
)

# --- Marcadores de medicion en el arbol vivo ----------------------------------
# Lo que cuenta como «alguien ya midio esto». Cada uno es un ARTEFACTO de lectura
# directa, no una opinion: un veredicto de licencia, bytes de payload, un SHA, o la
# declaracion explicita de primera mano.
MEASURE_MARKER = (
    r"\b(?:MIT|Apache-2\.0|Apache 2\.0|BSD-[23]|CC-BY-SA-4\.0|CC BY-SA 4\.0|"
    r"GPL-3\.0|GNU GPL 3\.0|AGPL|EPL-2\.0|LGPL-[\d.]+)\b",
    r"\b\d{1,3}(?:[,\s]\d{3})*\s*B\b",          # conteo de bytes de payload
    r"\b[0-9a-f]{8}\b",                          # SHA corto
    r"now measured", r"read first-hand", r"medido", r"leido de payload",
    r"HTTP\s*200",
)

# --- Sujetos ------------------------------------------------------------------
# 🔴 Excluidos por lista explicita: son REFERENCIAS, no sujetos de medicion.
NOT_SUBJECT = re.compile(
    r"^(?:Gap|gap)\s*\d+$|^P\d+(?:-[\w*-]+)?$|^[A-Za-z]+/[a-z-]+\.md$|^\d+$|"
    r"^(?:main|master|argv|__main__|LICENSE(?:\.md|\.txt)?|README(?:\.md)?)$|"
    # 🔴 Etiquetas en MAYUSCULAS: son CLASES de veredicto y variables de entorno, no
    # artefactos. El barrido v1 extrajo `REFUSES`, `MEASURES` (clases del TSV de `p542`)
    # y `PATH` (la variable del shim que `Gap 244` propone) y produjo CUATRO acusaciones
    # falsas con ellas: `PATH` colisiona con la palabra «path» en todo el arbol.
    r"^[A-Z][A-Z0-9_*-]{2,}$",
)
# Un identificador de artefacto: tiene `_`, `-`, `/`, `.` o CamelCase, o es un nombre
# de paquete reconocible. Las palabras comunes en minuscula sueltas no califican.
SUBJECT_SHAPE = re.compile(r"^(?=.{3,60}$)(?:[\w.-]+/[\w.*-]+|[\w*-]*[_*][\w.*-]*|[A-Za-z]+[A-Z]\w*)$")


def subjects_of(row):
    """Identificadores de artefacto que la fila nombra, en orden de aparicion."""
    out = []
    for tok in re.findall(r"`([^`]{2,70})`", row):
        tok = tok.strip()
        if NOT_SUBJECT.match(tok) or not SUBJECT_SHAPE.match(tok):
            continue
        if tok not in out:
            out.append(tok)
    return out


def claim_classes(row):
    """Las clases de afirmacion de frescura que la fila carga."""
    out = []
    if any(re.search(p, row, re.IGNORECASE) for p in MEASUREMENT_CLAIM):
        out.append(CLASS_MEASUREMENT)
    if any(re.search(p, row, re.IGNORECASE) for p in PRIORITY_CLAIM):
        out.append(CLASS_PRIORITY)
    return out


def subject_regex(subject):
    """`pt_core_news_*` tiene que coincidir con `pt_core_news_sm`: el `*` es un glob."""
    parts = [re.escape(p) for p in subject.split("*")]
    return re.compile(r"(?<![\w])" + r"[\w.-]*".join(parts) + r"(?![\w])", re.IGNORECASE)


def contradicting_lines(subjects, tree_files):
    """Lineas del arbol vivo que nombran un sujeto Y cargan un marcador de medicion."""
    out = []
    for subject in subjects:
        rx = subject_regex(subject)
        for path, text in tree_files:
            for n, line in enumerate(text.splitlines(), 1):
                if not rx.search(line):
                    continue
                if any(re.search(m, line, re.IGNORECASE) for m in MEASURE_MARKER):
                    out.append((subject, path, n, " ".join(line.split())[:120]))
    return out


def is_quotation(row):
    """True si la fila trae su propia correccion: la afirmacion es una CITA."""
    return any(re.search(m, row, re.IGNORECASE) for m in CORRECTION_MARKERS)


def closure_lines(gap, register_text, row_line):
    """Lineas POSTERIORES del registro que declaran CERRADO ese numero de gap.

    🔴 La evidencia que refuta una afirmacion de PRIORIDAD no es una medicion: es un
    CIERRE. El barrido v1 marco `Gap 238` por la licencia MIT de `qti3`, que no tiene
    nada que ver con si el gap sigue abierto — veredicto correcto, evidencia equivocada.
    🔵 Y el cierre vive en el registro, que es el unico caso donde el registro ES la
    evidencia: por eso se busca aca y no en el arbol.
    """
    out = []
    for n, line in enumerate(register_text.splitlines(), 1):
        if n <= row_line:
            continue
        # 🔴 El cierre pertenece al gap que la fila DECLARA, no a ninguno que CITE.
        # El barrido v2 marco `Gap 240` con la fila de `Gap 245`, que dice
        # «PARTIALLY CLOSED» de SI MISMA y menciona «cheaper than `Gap 240`»: dos
        # numeros en una linea, y el veredicto se le atribuyo al equivocado.
        # 🔵 Por eso se exige el numero DECLARADO en negrita, con `GAP_ROW`, que es el
        # mismo lector que arma el barrido — no una segunda definicion de «fila».
        if declared_gap(line) != gap:
            continue
        if re.search(r"\bCERRADO\b|\bCLOSED\b|\bcerrado\b", line):
            out.append((f"Gap {gap}", REGISTER, n, " ".join(line.split())[:120]))
    return out


def verdict(row, tree_files, gap=None, register_text="", row_line=0):
    """(veredicto, clases, sujetos, evidencia_que_contradice).

    La evidencia se elige por CLASE de afirmacion:
      · MEDICION  -> una medicion del sujeto en el arbol vivo
      · PRIORIDAD -> un CIERRE posterior de ese gap en el registro
    """
    classes = claim_classes(row)
    if not classes:
        return V_NO_CLAIM, classes, [], []
    if is_quotation(row):
        return V_CITA, classes, subjects_of(row), []
    subs = subjects_of(row)
    hits = []
    if CLASS_MEASUREMENT in classes and subs:
        hits += contradicting_lines(subs, tree_files)
    if CLASS_PRIORITY in classes and gap is not None:
        hits += closure_lines(gap, register_text, row_line)
    return (V_RANCIA if hits else V_SOSTENIDA), classes, subs, hits


# --- Lectura del arbol --------------------------------------------------------
REGISTER = os.path.join("intel", "open-gaps.md")


def read_tree(root, names=("agents", "repos", "verticals", "intel", "compose")):
    """Los ocho archivos de trabajo. 🔴 El registro mismo queda EXCLUIDO a proposito:
    si se incluyera, cada fila se contradeciria consigo misma y el gate marcaria todo."""
    out = []
    for d in names:
        p = os.path.join(root, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if not f.endswith(".md"):
                continue
            rel = os.path.join(d, f)
            if rel == REGISTER:
                continue
            with open(os.path.join(root, rel), encoding="utf-8") as fh:
                out.append((rel, fh.read()))
    return out


GAP_ROW = re.compile(r"^\|.*?\*\*(\d{1,3})\*\*.*\|")


def declared_gap(line):
    """El numero que la fila DECLARA en negrita, o `None`.

    🔵 Es un helper con nombre y no una expresion en linea a proposito: `closure_lines`
    y `register_rows` tienen que coincidir en que cuenta como «la fila de este gap», y
    dos lecturas distintas de «fila» es el error que `P480` ya costo una vez.
    """
    m = GAP_ROW.match(line)
    return int(m.group(1)) if m else None


def register_rows(path):
    """Filas del registro que declaran un numero de gap en negrita."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh.read().splitlines(), 1):
            m = GAP_ROW.match(line)
            if m:
                rows.append((n, int(m.group(1)), line))
    return rows


def sweep(root):
    tree = read_tree(root)
    reg_path = os.path.join(root, REGISTER)
    with open(reg_path, encoding="utf-8") as fh:
        reg_text = fh.read()
    rows = []
    for n, gap, line in register_rows(reg_path):
        v, classes, subs, hits = verdict(line, tree, gap, reg_text, n)
        if v == V_NO_CLAIM:
            continue
        rows.append((n, gap, v, classes, subs, hits))
    return rows


def main(argv):
    # P541 / `Gap 245`: una compuerta que sale 0 sin juzgar nada es indistinguible de
    # un arbol limpio. El pase 49 documenta ese defecto en 23 instrumentos; habria sido
    # absurdo reproducirlo en el instrumento que lo documenta.
    if not argv:
        print(
            "P598-NO-INPUT\tREFUSED: este gate barre el registro de un arbol y no "
            "recibio ninguno.  Uso: freshness_gate.py --sweep RAIZ  |  --self-test",
            file=sys.stderr,
        )
        return 2
    if "--self-test" in argv:
        import test_freshness_gate
        return test_freshness_gate.run()
    if "--sweep" in argv:
        i = argv.index("--sweep")
        if i + 1 >= len(argv):
            print("P598-NO-INPUT\tREFUSED: --sweep necesita una RAIZ.", file=sys.stderr)
            return 2
        rows = sweep(argv[i + 1])
        print("linea\tgap\tveredicto\tclases\tsujetos\tcontradicciones")
        n_rancia = 0
        for n, gap, v, classes, subs, hits in rows:
            n_rancia += v == V_RANCIA
            print(f"{n}\t{gap}\t{v}\t{'+'.join(classes)}\t{','.join(subs[:3]) or '-'}\t{len(hits)}")
            for subject, path, ln, txt in hits[:2]:
                print(f"\t\t↪ {subject} medido en {path}:{ln}\t{txt}")
        print(f"#\tfilas_con_afirmacion\t{len(rows)}")
        print(f"#\tP598-RANCIA\t{n_rancia}")
        return 1 if n_rancia else 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
