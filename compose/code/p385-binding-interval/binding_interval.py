#!/usr/bin/env python3
"""P385 — un binding fingerprint->repo cosechado de PROSA es un INTERVALO, no un numero.

Dos extractores sobre el mismo estante dan dos conteos, y los dos estan sesgados:

  - ANCLADO A URL: solo liga repos escritos `github.com/owner/repo` en la misma linea.
    Sesgo: se pierde los forks escritos como handles pelados (`sirdanielm`, `fdis111`).
    Direccion del error: SUBCUENTA. Su resultado es un PISO.

  - PERMISIVO: liga todo repo nombrado en la misma linea.
    Sesgo: co-ocurrencia de parrafo != binding de licencia.
    Direccion del error: SOBRECUENTA. Su resultado es un TECHO.

La medicion honesta es el par (piso, techo). Un conteo publicado como numero unico
esconde cual de los dos sesgos lo produjo.
"""
import collections
import re
import sys

SHA = re.compile(r"sha256[`:\s]{0,4}([0-9a-f]{12,64})")
URL = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*)")
SLUG = re.compile(r"`([A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*)`")
# Handles pelados: asi es como varias filas de esta base nombran a los forks.
HANDLE = re.compile(r"`([A-Za-z0-9][A-Za-z0-9._-]{2,})`")
# Tokens que parecen handle y no lo son: ids de patron, hex, etiquetas, enteros.
NOT_HANDLE = re.compile(
    r"^(P\d+|p\d+[a-z-]*|[0-9a-f]{8,}|\d+|[A-Z][A-Z0-9_-]{2,}|"
    r"sha256|LICENSE|COPYING|main|master|HEAD|develop|true|false)$"
)
NOISE = re.compile(
    r"^(main|master|HEAD|docs|src|fix|feature|LICENSE|COPYING|dependabot)/"
    r"|\.(md|txt|json|py|toml|cfg|html)$",
    re.I,
)


def norm(s):
    return s[:12]


def extract(lines, permissive):
    """Devuelve {fingerprint: {repos}}."""
    out = collections.defaultdict(set)
    for line in lines:
        if "sha256" not in line:
            continue
        shas = [norm(s) for s in SHA.findall(line)]
        if not shas:
            continue
        repos = {m.rstrip(".,)`") for m in URL.findall(line)}
        if permissive:
            repos |= {m.rstrip(".,)`") for m in SLUG.findall(line)}
            repos |= {
                m for m in HANDLE.findall(line)
                if "/" not in m and not NOT_HANDLE.match(m) and "." not in m
            }
        repos = {r for r in repos if not NOISE.search(r)}
        for s in shas:
            out[s] |= repos
    return out


def clusters(binding):
    return {k: v for k, v in binding.items() if len(v) >= 2}


def interval(lines):
    """Devuelve (piso, techo) de racimos de colision."""
    return (
        len(clusters(extract(lines, permissive=False))),
        len(clusters(extract(lines, permissive=True))),
    )


def main(argv):
    lines = []
    for p in argv:
        lines += open(p, encoding="utf-8").read().split("\n")
    floor, ceil = interval(lines)
    anchored = clusters(extract(lines, False))
    print("extractor\tfingerprints\tracimos")
    print(f"anclado-a-url\t{len(extract(lines, False))}\t{floor}")
    print(f"permisivo\t{len(extract(lines, True))}\t{ceil}")
    print(f"#\tintervalo\t[{floor}, {ceil}]")
    if floor == ceil:
        print("#\tveredicto\tCONVERGEN - el conteo no depende de la convencion")
    else:
        print(f"#\tveredicto\tDIVERGEN por {ceil - floor} - el conteo depende de la CONVENCION de escritura")
    for k, v in sorted(anchored.items()):
        print(f"piso\t{k}\t{','.join(sorted(v))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
