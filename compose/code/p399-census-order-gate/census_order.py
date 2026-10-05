#!/usr/bin/env python3
"""P399 — un auto-censo publicado en el MISMO pase que agrega filas mide el corpus PRE-ESCRITURA.

Hallazgo del pase 121. `P394` publico, en el pase 120, el censo de titular del estante:
15 ausentes / 46 presentes / 125 mudas / 186 de universo. Re-correr su propia invocacion
publicada sobre el arbol que ESE pase commiteo da 23 / 46 / 139 / 208. La cifra publicada
es, exactamente, el censo del arbol del pase 119: se midio, DESPUES se escribieron las
filas del pase, y se commiteo con la cifra de antes.

No es un error de aritmetica, es un error de ORDEN. Y lo que lo hace invisible desde
afuera es que la clase `presente` no se mueve (46 -> 46): es la unica columna que un
lector verifica a mano, porque es la que tiene nombres propios.

La compuerta: dado un censo publicado y dos revisiones de git, decide si la cifra
describe el arbol propio (OK), el arbol anterior (DESFASADO) o ninguno (DESCONOCIDO).

Uso:
  python3 census_order.py <rev-anterior> <rev-propia> <ausente> <presente> <mudo> <universo>
  python3 census_order.py 8110153 195fe59 15 46 125 186     # el caso de P394

Sale con 0 si la cifra describe el arbol propio, 3 si esta DESFASADA, 4 si no describe
ninguno de los dos (que es peor: no se sabe que midio).
"""
import re
import subprocess
import sys

FILES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md", "compose/patterns.md",
]

HEX12 = re.compile(r"\b[0-9a-f]{12,64}\b")
ABSENT = re.compile(
    r"NOT-APPLICABLE|NOT_APPLICABLE|HOLDER-ABSENT|sin titular|titular\s+\*{0,2}ausente", re.I
)
HOLDER = re.compile(r"titular|Copyright|holder|copyright\s*\(c\)", re.I)
# Los \b de los acronimos cortos son los de `P394`: sin ellos `MIT` casa dentro de
# "com-MIT" y el universo se infla con toda fila que nombre un commit.
LICENSEY = re.compile(
    r"LICENSE|COPYING|licencia|license|Apache|Unlicense|"
    r"\b(MIT|GPL|LGPL|AGPL|BSD|MPL|CC0|CC BY|EPL|Zlib)\b", re.I
)
SEP_ROW = re.compile(r"^[\s:|-]+$")


def is_row(line):
    s = line.strip()
    if not s.startswith("|") or s.count("|") < 2:
        return False
    return not SEP_ROW.fullmatch(s.strip("|"))


def classify(line):
    """'absent' | 'present' | 'mute' | None — el criterio de `P394`, sin cambiarlo."""
    if not is_row(line) or not HEX12.search(line) or not LICENSEY.search(line):
        return None
    if ABSENT.search(line):
        return "absent"
    if HOLDER.search(line):
        return "present"
    return "mute"


def census_lines(lines):
    counts = {"absent": 0, "present": 0, "mute": 0}
    for line in lines:
        kind = classify(line)
        if kind:
            counts[kind] += 1
    counts["universe"] = counts["absent"] + counts["present"] + counts["mute"]
    return counts


def census_at(rev, files=FILES, cwd=None):
    """Censo del arbol de una revision. Un archivo que no existe en esa revision
    NO es un cero: se omite, y el llamador ve el conteo de archivos leidos."""
    lines, read = [], 0
    for f in files:
        r = subprocess.run(["git", "show", f"{rev}:{f}"],
                           capture_output=True, text=True, cwd=cwd)
        if r.returncode == 0:
            lines.extend(r.stdout.splitlines())
            read += 1
    c = census_lines(lines)
    c["files_read"] = read
    return c


def verdict(published, own, prior):
    """('OK'|'DESFASADO'|'DESCONOCIDO', explicacion)."""
    key = ("absent", "present", "mute", "universe")
    pub = tuple(published[k] for k in key)
    if pub == tuple(own[k] for k in key):
        return "OK", "la cifra describe el arbol propio"
    if pub == tuple(prior[k] for k in key):
        return "DESFASADO", "la cifra describe el arbol ANTERIOR: se midio antes de escribir"
    return "DESCONOCIDO", "la cifra no describe ninguno de los dos arboles"


def blind_spot(own, prior):
    """Las clases que NO se mueven entre los dos arboles: un control que mire solo
    esas columnas no detecta el desfase. Es el motivo por el que `P394` paso."""
    return sorted(k for k in ("absent", "present", "mute", "universe") if own[k] == prior[k])


def main(argv):
    if len(argv) != 6:
        print(__doc__)
        return 2
    prior_rev, own_rev = argv[0], argv[1]
    published = dict(zip(("absent", "present", "mute", "universe"), map(int, argv[2:])))
    prior, own = census_at(prior_rev), census_at(own_rev)

    print("arbol\tausente\tpresente\tmudo\tuniverso\tarchivos")
    for label, c in ((f"{prior_rev} (anterior)", prior), (f"{own_rev} (propio)", own)):
        print(f"{label}\t{c['absent']}\t{c['present']}\t{c['mute']}\t{c['universe']}\t{c['files_read']}")
    p = published
    print(f"publicado\t{p['absent']}\t{p['present']}\t{p['mute']}\t{p['universe']}\t-")

    v, why = verdict(published, own, prior)
    print(f"#\tveredicto\t{v}\t{why}")
    blind = blind_spot(own, prior)
    print(f"#\tclases-que-NO-se-mueven\t{','.join(blind) if blind else '(ninguna)'}"
          f"\t<- un control que mire solo estas columnas NO detecta el desfase")
    return {"OK": 0, "DESFASADO": 3, "DESCONOCIDO": 4}[v]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
