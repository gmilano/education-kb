#!/usr/bin/env python3
"""P170-B — un label de ACTION se DEFINE una sola vez en todo el arbol.

p169 emitio `ACTION JF` dos veces en el mismo pase, desde `agents/top.md`
(los grant files de penecho) y desde `intel/open-gaps.md` (el gate de region
`P383`), para dos tareas sin relacion (`T218`). Las dos se ejecutaron y las dos
se reportaron, asi que no se perdio nada -- pero "ACTION JF fue descargada" ya
es ambiguo en el registro permanente.

POR QUE NO SIRVE CONTAR OCURRENCIAS. Un label aparece legitimamente muchas
veces: cada pase cita las acciones de los pases anteriores al juzgarlas. La
primera version de este gate contaba ocurrencias crudas y marcaba 10 labels con
19-41 "definiciones" cada uno, que son referencias historicas por diseno. Un
gate que marca el arbol entero no es un control (P471).

Un label se DEFINE solo en una FILA DE TABLA dentro de una seccion de registro
(un encabezado que contiene "Registered for p" / "Registrada para p"), porque
ahi es donde la accion aparece junto a su falsificador. La prosa de la misma
seccion es RESUMEN: `README.md` resume el registro del pase y `agents/top.md`
enlaza a el. Todo lo demas es referencia. Se mide solo la fila de tabla.

Hallazgos:
  P170-B-DUPLICATE   un label DEFINIDO en mas de un lugar
Salida TSV. Codigo 1 si hay hallazgos.
"""
import re
import sys

LABEL = re.compile(r"`ACTION ([A-Z]{1,3})`")
REGISTER_HEADING = re.compile(r"^#{2,4} .*(?:Registered for p|Registrada para p)", re.I)
ANY_HEADING = re.compile(r"^#{1,4} ")


def definitions(path, text):
    """[(label, linea)] para los labels que aparecen en una seccion de registro."""
    out = []
    lines = text.split("\n")
    in_register = False
    for i, l in enumerate(lines):
        if ANY_HEADING.match(l):
            in_register = bool(REGISTER_HEADING.match(l))
            continue
        # Una DEFINICION es una FILA de la tabla de registro (lleva su
        # falsificador al lado).  La prosa dentro de la misma seccion es
        # RESUMEN, no definicion: `README.md` resume las acciones del pase y
        # `agents/top.md` enlaza a ellas, y ninguna de las dos las define.
        # La primera version de este gate contaba la prosa y marcaba las
        # propias acciones de p170 como duplicadas.
        if in_register and l.lstrip().startswith("|"):
            for m in LABEL.finditer(l):
                out.append((m.group(1), i + 1))
    return out


def main(argv):
    if not argv:
        print(
            "P541-NO-INPUT\tREFUSED: este gate mide los archivos que recibe por "
            "argumento y no recibio ninguno. Uso: check_action_labels.py FILE [...]",
            file=sys.stderr,
        )
        return 2
    seen = {}
    for p in argv:
        for label, ln in definitions(p, open(p, encoding="utf-8").read()):
            seen.setdefault(label, []).append((p, ln))
    print("label\thallazgo\tdefiniciones\tdonde")
    total = 0
    for label in sorted(seen):
        places = seen[label]
        # Un mismo label puede repetirse dentro de UNA tabla de registro (la fila
        # y una mencion en su propio falsificador).  Lo que importa es si se
        # define en mas de un ARCHIVO.
        files = sorted({p for p, _ in places})
        if len(files) > 1:
            total += 1
            where = "; ".join(f"{p}:{ln}" for p, ln in places)
            print(f"ACTION {label}\tP170-B-DUPLICATE\t{len(files)} archivos\t{where}")
    print(f"#\tduplicados\t{total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
