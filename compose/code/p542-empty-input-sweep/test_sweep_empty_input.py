#!/usr/bin/env python3
"""Suite de P542.  Cada caso nombra el defecto que atrapa.

🔴 REGLA LOCAL RESPETADA (P399, y la leccion del pase 122): esta suite NO congela
cardinalidades del corpus.  No afirma "hay 20 defectos": afirma PROPIEDADES
INVARIANTES de la clasificacion, que siguen siendo verdaderas cuando el arbol
cambia.  Una suite que afirma `len(defectos) == 20` caduca el proximo pase y
entonces se la "arregla" retocando el numero, que es como se pierde el control.
"""
import os
import subprocess
import sys

import sweep_empty_input as m

ok, fail = 0, 0


def t(nombre, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {nombre}")
    else:
        fail += 1
        print(f"FAIL {nombre}")


# ---------------------------------------------------------------- casos buenos
# El caso p383 REAL: el arreglo de P541 del pase 43 sale 2 sin leer nada.
t("rc!=0 es REFUSES, no un defecto (el caso p383 del pase 43)",
  m.clasificar(2, 0, 191, None) == "REFUSES")

# El caso p243 REAL: sale 0 y mide 146 archivos porque se descubre por __file__.
t("rc==0 con lecturas es MEASURES (el caso p243, que un loop ingenuo acusaria)",
  m.clasificar(0, 72, 0, 146) == "MEASURES")

# ------------------------------------------------------------------- defectos
t("rc==0 con CERO lecturas es P541-FALSE-PASS",
  m.clasificar(0, 73, 0, 0) == "P541-FALSE-PASS")

t("rc==0 y silencio total es P541-SILENT-SUCCESS (oraculo B, shell)",
  m.clasificar(0, 0, 0, None) == "P541-SILENT-SUCCESS")

# ----------------------------------------------- controles NEGATIVOS, el nucleo
# 🔴 Sin este control la suite aprobaria un instrumento que acuse por "cero
#    lecturas" a secas -- y entonces p383, que es el ARREGLO, saldria acusado.
t("CONTROL NEGATIVO: cero lecturas con rc!=0 NUNCA es defecto",
  all(not m.ES_DEFECTO(m.clasificar(rc, 0, 0, 0)) for rc in (1, 2, 3, 124, 255)))

# 🔴 Sin este control, el oraculo B (silencio) se aplicaria a shell ruidoso y
#    acusaria a sweep_holder.sh, que emite 13 777 bytes de tabla real.
t("CONTROL NEGATIVO: shell que SALE 0 y emite salida no se acusa",
  m.clasificar(0, 13777, 0, None) == "P542-UNADJUDICATED-OUTPUT")

t("CONTROL NEGATIVO: shell que solo escribe en stderr tampoco se acusa",
  m.clasificar(0, 0, 721, None) == "P542-UNADJUDICATED-OUTPUT")

t("un timeout no afirma nada en ninguna direccion",
  m.clasificar(m.TIMEOUT, 0, 0, None) == "P542-UNADJUDICATED-TIMEOUT"
  and not m.ES_DEFECTO(m.clasificar(m.TIMEOUT, 0, 0, None)))

t("una excepcion del instrumento no es un pase",
  m.clasificar("EXC:KeyError", 0, 0, None) == "REFUSES")

# --------------------------------------------------- PROPIEDAD INVARIANTE (P399)
# No es una cuenta: es una implicacion.  Sobrevive a cualquier cambio del arbol.
t("INVARIANTE: toda clase P541-* implica rc==0",
  all(
      (not m.ES_DEFECTO(m.clasificar(rc, no, ne, le)))
      for rc in (1, 2, 124, m.TIMEOUT, "EXC:X")
      for no in (0, 10)
      for ne in (0, 10)
      for le in (None, 0, 5)
  ))

t("INVARIANTE: con oraculo A disponible, el veredicto NO depende de los bytes",
  all(m.clasificar(0, no, ne, 0) == "P541-FALSE-PASS"
      for no in (0, 1, 9999) for ne in (0, 1, 9999)))

t("INVARIANTE: con lecturas>0 jamas hay defecto, con cualquier rc",
  all(not m.ES_DEFECTO(m.clasificar(rc, 0, 0, le))
      for rc in (0, 1, 2) for le in (1, 146, 10**6)))

# ------------------------------------- eje INVOCABLE (el defecto del pase 44)
# 🔴 Lo encontro la primera corrida real: 24 de 49 acusaciones eran MODULOS.
t("un modulo sin __main__ no es un defecto aunque salga 0 sin leer nada",
  m.clasificar(0, 0, 0, 0, invocable=False) == "P542-NOT-A-GATE")

t("CONTROL NEGATIVO: el eje invocable NO absuelve a un gate real",
  m.clasificar(0, 0, 0, 0, invocable=True) == "P541-FALSE-PASS")

t("INVARIANTE: lo no invocable jamas es defecto, con cualquier rc/bytes/lecturas",
  all(not m.ES_DEFECTO(m.clasificar(rc, no, ne, le, invocable=False))
      for rc in (0, 1, 2, m.TIMEOUT)
      for no in (0, 99) for ne in (0, 99) for le in (None, 0, 7)))

t("es_invocable: .py con bloque __main__ es un gate",
  m.es_invocable('if __name__ == "__main__":\n    sys.exit(main())\n', ".py"))
t("es_invocable: .py sin bloque __main__ es un modulo",
  not m.es_invocable("def clasificar(x):\n    return x\n", ".py"))
t("es_invocable: un .sh es invocable por naturaleza",
  m.es_invocable("echo hola\n", ".sh"))
# el caso real que lo motivo: census.py es importado por su suite
t("es_invocable: el caso real p328/census.py se lee como modulo",
  not m.es_invocable("import csv\n\ndef censo(rows):\n    return len(rows)\n", ".py"))

# ------------------------------- eje FILTRO stdin (2do defecto del pase 44)
t("un filtro de stdin no es un defecto: con EOF no hacer nada es correcto",
  m.clasificar(0, 0, 0, 0, invocable=True, filtro=True) == "P542-STDIN-FILTER")

t("CONTROL NEGATIVO: el eje filtro NO absuelve a un gate que no lee stdin",
  m.clasificar(0, 0, 0, 0, invocable=True, filtro=False) == "P541-FALSE-PASS")

t("INVARIANTE: un filtro jamas es defecto, con cualquier rc/bytes/lecturas",
  all(not m.ES_DEFECTO(m.clasificar(rc, no, ne, le, True, True))
      for rc in (0, 1, 2, m.TIMEOUT)
      for no in (0, 99) for ne in (0, 99) for le in (None, 0, 7)))

t("lee_stdin: el caso real fake_upstream.py (for line in sys.stdin)",
  m.lee_stdin("def main():\n    for line in sys.stdin:\n        pass\n"))
t("lee_stdin: el idioma shell `while read -r`",
  m.lee_stdin('while read -r slug; do echo "$slug"; done\n'))
t("lee_stdin: un gate que solo toma rutas por argumento NO es filtro",
  not m.lee_stdin("def main(argv):\n    for p in argv:\n        open(p)\n"))

# ------------------------------------------------------------- eje estatico
t("eje estatico: sys.argv[1:] cuenta como posicional",
  m.consume_posicionales("def main(a):\n  x=sys.argv[1:]\n", ".py"))
t("eje estatico: un script .py sin argv no cuenta",
  not m.consume_posicionales("import os\nprint(1)\n", ".py"))
t("eje estatico: $1 en shell cuenta",
  m.consume_posicionales('slug="$1"\n', ".sh"))
t("eje estatico: \"$@\" en shell cuenta",
  m.consume_posicionales('for f in "$@"; do :; done\n', ".sh"))
t("eje estatico: shell con lista fija no cuenta",
  not m.consume_posicionales('for s in a b c; do echo $s; done\n', ".sh"))
# 🔴 el defecto que atrapa: `$10` NO es `$1`
t("eje estatico: $0 no se confunde con $1",
  not m.consume_posicionales('echo "$0"\n', ".sh"))

# --------------------------------------- el guardia PROPIO (no tener P541)
t("el barrido REHUSA su propia entrada vacia (no tiene la clase que detecta)",
  m.main([]) == 2)
t("el barrido rehusa una ruta que no es directorio",
  m.main([os.path.join(os.path.dirname(__file__), "sweep_empty_input.py")]) == 2)

AQUI = os.path.dirname(os.path.realpath(__file__))
rc_hijo = subprocess.run([sys.executable, os.path.join(AQUI, "readcount.py")],
                         capture_output=True).returncode
t("el hijo readcount.py tambien rehusa entrada vacia", rc_hijo == 2)

# ------------------------------------------------- DETECCION POR MUTACION
# Cada mutante es un defecto PLAUSIBLE del clasificador.  La suite debe matarlo.
def mut_sin_guardia_rc(rc, no, ne, le, inv=True, fl=False):
    """Mutante: olvida que solo rc==0 puede ser defecto."""
    if not inv:
        return "P542-NOT-A-GATE"
    if rc == m.TIMEOUT:
        return "P542-UNADJUDICATED-TIMEOUT"
    if le is not None:
        return "P541-FALSE-PASS" if le == 0 else "MEASURES"
    return "P541-SILENT-SUCCESS" if (no == 0 and ne == 0) else "P542-UNADJUDICATED-OUTPUT"


def mut_silencio_solo_stdout(rc, no, ne, le, inv=True, fl=False):
    """Mutante: mira stdout y se olvida de stderr."""
    if not inv:
        return "P542-NOT-A-GATE"
    if rc == m.TIMEOUT:
        return "P542-UNADJUDICATED-TIMEOUT"
    if rc != 0:
        return "REFUSES"
    if le is not None:
        return "P541-FALSE-PASS" if le == 0 else "MEASURES"
    return "P541-SILENT-SUCCESS" if no == 0 else "P542-UNADJUDICATED-OUTPUT"


def mut_timeout_es_pase(rc, no, ne, le, inv=True, fl=False):
    """Mutante: trata un timeout como exito silencioso."""
    if not inv:
        return "P542-NOT-A-GATE"
    if rc != 0 and rc != m.TIMEOUT:
        return "REFUSES"
    if le is not None:
        return "P541-FALSE-PASS" if le == 0 else "MEASURES"
    return "P541-SILENT-SUCCESS" if (no == 0 and ne == 0) else "P542-UNADJUDICATED-OUTPUT"


def mut_bytes_sobre_oraculo(rc, no, ne, le, inv=True, fl=False):
    """Mutante: deja que los bytes manden aunque el oraculo A exista."""
    if not inv:
        return "P542-NOT-A-GATE"
    if rc == m.TIMEOUT:
        return "P542-UNADJUDICATED-TIMEOUT"
    if rc != 0:
        return "REFUSES"
    if no == 0 and ne == 0:
        return "P541-SILENT-SUCCESS"
    return "P541-FALSE-PASS" if le == 0 else "MEASURES"


def mut_ignora_invocable(rc, no, ne, le, inv=True, fl=False):
    """🔴 Mutante = DEFECTO REAL 1 DEL PASE 44: acusa modulos como si fueran gates."""
    return m.clasificar(rc, no, ne, le, invocable=True, filtro=fl)


def mut_ignora_filtro(rc, no, ne, le, inv=True, fl=False):
    """🔴 Mutante = DEFECTO REAL 2 DEL PASE 44: acusa filtros de stdin."""
    return m.clasificar(rc, no, ne, le, invocable=inv, filtro=False)


def mut_todo_es_modulo(rc, no, ne, le, inv=True, fl=False):
    """Mutante inverso: absuelve a todos tratandolos como modulos."""
    return "P542-NOT-A-GATE"


def controles(c):
    """Los asertos que CUALQUIER clasificador correcto debe cumplir."""
    es_def = lambda x: x.startswith("P541-")
    return [
        c(2, 0, 191, None) == "REFUSES",
        c(0, 72, 0, 146) == "MEASURES",
        c(0, 73, 0, 0) == "P541-FALSE-PASS",
        c(0, 0, 0, None) == "P541-SILENT-SUCCESS",
        c(0, 13777, 0, None) == "P542-UNADJUDICATED-OUTPUT",
        c(0, 0, 721, None) == "P542-UNADJUDICATED-OUTPUT",
        not es_def(c(m.TIMEOUT, 0, 0, None)),
        all(not es_def(c(rc, 0, 0, 0)) for rc in (1, 2, 124)),
        all(c(0, no, ne, 0) == "P541-FALSE-PASS" for no in (0, 9999) for ne in (0, 9999)),
        # los dos lados del eje invocable
        c(0, 0, 0, 0, False) == "P542-NOT-A-GATE",
        c(0, 0, 0, 0, True) == "P541-FALSE-PASS",
        # los dos lados del eje filtro
        c(0, 0, 0, 0, True, True) == "P542-STDIN-FILTER",
        c(0, 0, 0, 0, True, False) == "P541-FALSE-PASS",
    ]


MUTANTES = [
    ("sin_guardia_rc", mut_sin_guardia_rc),
    ("silencio_solo_stdout", mut_silencio_solo_stdout),
    ("timeout_es_pase", mut_timeout_es_pase),
    ("bytes_sobre_oraculo", mut_bytes_sobre_oraculo),
    ("ignora_invocable (el defecto real del pase 44)", mut_ignora_invocable),
    ("ignora_filtro (el 2do defecto real del pase 44)", mut_ignora_filtro),
    ("todo_es_modulo", mut_todo_es_modulo),
]
t("el original pasa todos sus propios controles", all(controles(m.clasificar)))
for nombre, mut in MUTANTES:
    t(f"MUTACION detectada: {nombre}", not all(controles(mut)))

print(f"\n#\ttotal\t{ok + fail}\tPASS={ok}\tFAIL={fail}")
sys.exit(1 if fail else 0)
