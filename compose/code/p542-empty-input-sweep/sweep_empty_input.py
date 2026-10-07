#!/usr/bin/env python3
"""P542 — el barrido que el `Gap 243` pidio: invocar TODO instrumento de
`compose/code/` SIN argumentos y exigir que no finja exito.

El gap lo dejo escrito asi: *"one pass, one loop — invoke every argument-taking
instrument with no arguments and assert a non-zero exit"*.  Este archivo es ese
loop, mas los dos oraculos que el gap no nombro y sin los cuales el loop produce
falsos positivos:

  - `p243-frontmatter-coverage` SALE 0 sin argumentos y esta BIEN: se descubre
    a si mismo desde `__file__` (es la leccion de `p355`) y mide 146 archivos.
    Un loop que solo mire el codigo de salida lo acusa sin razon.
  - `p383-region-heading-gate` SALE 2 sin argumentos y esta BIEN: es el arreglo
    de `P541` del pase 43.

Asi que "salio 0" no alcanza como veredicto.  Hace falta saber si el instrumento
JUZGO ALGO.  Dos oraculos, y cada uno declara su alcance:

  ORACULO A (.py, directo) — `readcount.py` corre el instrumento bajo un audit
    hook y cuenta los archivos no-codigo del repo que abre.  `0` lecturas con
    salida `0` es la clase `P541` PROBADA, no inferida.
  ORACULO B (.sh, indirecto) — para shell no hay audit hook.  Se usa el SILENCIO:
    salida `0` con CERO bytes en stdout Y stderr es un exito que no reporto nada,
    indistinguible de un arbol limpio.  Es mas debil que A y se marca como tal.

Un instrumento .sh que salio 0 imprimiendo 13 KB de tabla NO se acusa: queda
`UNADJUDICATED-OUTPUT`, que es una brecha declarada y no una absolucion.

Clases emitidas:
  REFUSES                      salida != 0 — correcto, no finge exito
  MEASURES                     salida 0 y leyo entradas — correcto
  P541-FALSE-PASS              salida 0 y CERO entradas leidas (oraculo A)
  P541-SILENT-SUCCESS          salida 0 y cero bytes en ambos flujos (oraculo B)
  P542-UNADJUDICATED-OUTPUT    salida 0, sin oraculo A, pero emitio algo
  P542-UNADJUDICATED-TIMEOUT   no termino en el plazo — no se afirma nada

Salida TSV.  Codigo 1 si hay hallazgos `P541-*`.
"""
import os
import re
import subprocess
import sys

TIMEOUT = "TIMEOUT"
PLAZO = 12

# --- eje estatico: el instrumento CONSUME argumentos posicionales? -----------
POS_PY = [
    re.compile(r"sys\.argv\[1:\]"),
    re.compile(r"sys\.argv\[1\]"),
    re.compile(r"add_argument\(\s*['\"][^-]"),
    re.compile(r"def main\(\s*argv"),
]
POS_SH = [
    re.compile(r"\$\{?1\}?[^0-9]"),
    re.compile(r'"\$@"'),
    re.compile(r"\$\*"),
    re.compile(r"\bshift\b"),
]


def es_invocable(texto, sufijo):
    """True si el archivo es un GATE invocable, no un modulo de libreria.

    🔴 Defecto que esta funcion existe para no repetir -- lo encontro la PRIMERA
    corrida de este barrido sobre el arbol vivo.  Sin este eje, el barrido acuso
    49 instrumentos de `P541-FALSE-PASS` y 24 de esos 49 son MODULOS que sus
    suites importan (`census.py`, `emit_template.py`, `policy.py`...): no tienen
    bloque `__main__`, invocarlos directamente no hace nada POR DISENO y salir 0
    es lo correcto.  Acusarlos confunde "modulo" con "compuerta que finge exito",
    que es la misma clase de error que `P502` -- un instrumento que no distingue
    *"no hay licencia"* de *"no hay repositorio"*.
    """
    if sufijo == ".sh":
        return True  # un script de shell es invocable por naturaleza
    return "__main__" in texto


RE_STDIN = re.compile(
    r"sys\.stdin|fileinput|^\s*read -r|while read|/dev/stdin", re.MULTILINE
)


def lee_stdin(texto):
    """True si el instrumento es un FILTRO que lee la entrada estandar.

    🔴 Segundo defecto que encontro la corrida real del pase 44, y lo encontro
    revisando UNA acusacion a mano antes de publicar las 34.
    `mcp-allowlist-gateway/fake_upstream.py` es un stub JSON-RPC que lee `stdin`:
    invocado con `stdin` cerrado ve EOF y termina sin hacer nada, SALIENDO 0.
    Eso no es una compuerta que finge exito -- es el comportamiento correcto de
    un filtro, igual que `cat < /dev/null`.  Acusarlo es el mismo error que
    acusar a un modulo: juzgar una forma por el contrato de otra.
    🔵 Este eje tiene PRECEDENCIA sobre los oraculos A y B a proposito: el
    barrido prefiere acusar DE MENOS a acusar de mas.
    """
    return bool(RE_STDIN.search(texto))


def consume_posicionales(texto, sufijo):
    """True si el fuente consume argumentos posicionales."""
    pats = POS_PY if sufijo == ".py" else POS_SH
    return any(r.search(texto) for r in pats)


# --- el corazon: clasificacion PURA, sin E/S, por eso es testeable ----------
def clasificar(rc, nout, nerr, leidos, invocable=True, filtro=False):
    """rc: int | 'TIMEOUT' | 'EXC:...'   leidos: int | None (None = sin oraculo A).

    INVARIANTES que esta funcion defiende:
      1. Un archivo que no es invocable NUNCA es un defecto -- no es una
         compuerta, asi que no puede fingir que aprobo nada.
      2. Un FILTRO de stdin nunca es un defecto: con EOF no hacer nada es
         correcto, y este barrido no le da entrada estandar a nadie.
      3. Solo `rc == 0` puede ser un defecto.  Salir != 0 es rechazar, y
         rechazar es exactamente lo correcto.
    """
    if not invocable:
        return "P542-NOT-A-GATE"
    if filtro:
        return "P542-STDIN-FILTER"
    if rc == TIMEOUT:
        return "P542-UNADJUDICATED-TIMEOUT"
    if rc != 0:
        return "REFUSES"
    # A partir de aqui el instrumento AFIRMA exito sobre una entrada vacia.
    if leidos is not None:
        return "P541-FALSE-PASS" if leidos == 0 else "MEASURES"
    if nout == 0 and nerr == 0:
        return "P541-SILENT-SUCCESS"
    return "P542-UNADJUDICATED-OUTPUT"


ES_DEFECTO = lambda clase: clase.startswith("P541-")


def entradas(base):
    """Los puntos de entrada de compose/code/: ni lib/, ni suites."""
    out = []
    for d in sorted(os.listdir(base)):
        ruta = os.path.join(base, d)
        if not os.path.isdir(ruta) or d == "lib":
            continue
        for f in sorted(os.listdir(ruta)):
            if f.startswith("test") or not f.endswith((".py", ".sh")):
                continue
            out.append(os.path.join(d, f))
    return out


def correr(base, rel, raiz_repo, propio):
    """Invoca UN instrumento sin argumentos.  Devuelve (rc, nout, nerr, leidos)."""
    d, f = os.path.split(rel)
    cwd = os.path.join(base, d)
    es_py = f.endswith(".py")
    try:
        p = subprocess.run(
            ["python3" if es_py else "bash", f],
            cwd=cwd, capture_output=True, timeout=PLAZO, stdin=subprocess.DEVNULL,
        )
        rc, nout, nerr = p.returncode, len(p.stdout), len(p.stderr)
    except subprocess.TimeoutExpired:
        return TIMEOUT, 0, 0, None
    leidos = None
    if es_py and rc == 0:  # el oraculo A solo hace falta cuando AFIRMA exito
        try:
            q = subprocess.run(
                ["python3", os.path.join(propio, "readcount.py"), f, raiz_repo],
                cwd=cwd, capture_output=True, timeout=PLAZO + 8,
                stdin=subprocess.DEVNULL, text=True,
            )
            campos = q.stdout.strip().split("\t")
            if len(campos) == 2 and campos[1].isdigit():
                leidos = int(campos[1])
        except subprocess.TimeoutExpired:
            leidos = None
    return rc, nout, nerr, leidos


def main(argv):
    # Este instrumento detecta la clase `P541`.  Seria absurdo que la tuviera:
    # sin argumentos REHUSA, y no imprime un total de cero.
    if not argv:
        print(
            "P542-NO-INPUT\tREFUSED: este barrido mide el arbol que recibe por "
            "argumento y no recibio ninguno.  Uso: sweep_empty_input.py "
            "<dir_compose_code> [raiz_repo]",
            file=sys.stderr,
        )
        return 2
    base = os.path.realpath(argv[0])
    raiz_repo = os.path.realpath(argv[1]) if len(argv) > 1 else os.path.dirname(
        os.path.dirname(base)
    )
    propio = os.path.dirname(os.path.realpath(__file__))
    if not os.path.isdir(base):
        print(f"P542-NO-INPUT\tREFUSED: no es un directorio: {base}", file=sys.stderr)
        return 2

    print("instrumento\tlenguaje\tposicional\tinvocable\tfiltro\tsalida\tleidos\tclase")
    cuentas, defectos = {}, 0
    for rel in entradas(base):
        texto = open(os.path.join(base, rel), encoding="utf-8", errors="replace").read()
        suf = os.path.splitext(rel)[1]
        pos = consume_posicionales(texto, suf)
        inv = es_invocable(texto, suf)
        filt = lee_stdin(texto)
        rc, nout, nerr, leidos = correr(base, rel, raiz_repo, propio)
        clase = clasificar(rc, nout, nerr, leidos, inv, filt)
        cuentas[clase] = cuentas.get(clase, 0) + 1
        if ES_DEFECTO(clase):
            defectos += 1
        print(
            f"{rel}\t{suf[1:]}\t{'POS' if pos else '-'}\t"
            f"{'GATE' if inv else 'MOD'}\t{'STDIN' if filt else '-'}\t{rc}\t"
            f"{'-' if leidos is None else leidos}\t{clase}"
        )
    for clase in sorted(cuentas):
        print(f"#\t{clase}\t{cuentas[clase]}")
    print(f"#\ttotal\t{sum(cuentas.values())}")
    print(f"#\tdefectos_P541\t{defectos}")
    return 1 if defectos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
