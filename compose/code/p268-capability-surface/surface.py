#!/usr/bin/env python3
"""P268 — un conteo de capacidades tiene SUPERFICIE, y dos superficies del MISMO repo se contradicen.

Esta base cita conteos de herramientas desde el pase 10 (`227` vs `165` de Canvas quedo como
accion abierta). `description-drift-audit/` ya medía la deriva entre la DESCRIPCION de un fork
y la del upstream. Lo que ningun instrumento medía: **la descripcion y el README del MISMO
repo no dicen lo mismo**, y entonces «102 herramientas» no es un dato hasta que se nombra de
donde se leyo.

Medido el 2026-10-04 sobre el cohorte `canvas-mcp`:

  - `vishalsachdev/canvas-mcp` (UPSTREAM, MIT, 274 ★, v1.13.0): la descripcion dice
    **102** herramientas, el cuerpo del README dice **103**. Mismo repo, misma lectura,
    mismo dia.
  - `harrywang/canvas-mcp` (FORK, MIT, 0 ★, v1.12.0): la descripcion dice **80+ / 5 skills**,
    o sea el claim del upstream CONGELADO en una version anterior.
  - `jsrodr/canvas-mcp` (FORK, MIT, 0 ★, v1.10.0): descripcion **80+ / 5**, README **99** —
    la contradiccion interna se HEREDA y se agranda.

🔴 `EastArctica/canvas-mcp`, que el canal de busqueda devolvio como repo vivo, da **404**.
No se escribe como fila: un 404 no es un hallazgo.

La regla que sale: **un conteo de capacidades se cita con su superficie o no se cita.** Y la
comparacion que esta base tenia pendiente (`227` vs `165`) no era comparable ni en principio,
porque los dos numeros podian venir de superficies distintas.

Uso:
    python3 surface.py            # la tabla por repo, con el delta entre superficies
    python3 surface.py --tsv
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SURFACES = ("DESCRIPTION", "README-HEADER", "README-BODY")
ROLES = ("UPSTREAM", "FORK")
NO_CLAIM = "NO-CLAIM"


def load(path=None):
    """Las filas medidas. Los comentarios y la linea de cabecera se descartan."""
    rows = []
    with open(path or os.path.join(HERE, "rows.tsv"), encoding="utf-8") as fh:
        for ln in fh:
            if ln.startswith("#") or not ln.strip():
                continue
            f = ln.rstrip("\n").split("\t")
            if len(f) != 8:
                raise ValueError(f"fila con {len(f)} campos, se esperan 8: {ln!r}")
            rows.append(dict(zip(
                ("slug", "rol", "superficie", "herramientas", "skills",
                 "release", "licencia", "estrellas"), f)))
    return rows


def vocab_ok(rows):
    """Vocabulario cerrado de `superficie` y de `rol`. Sin strip: P248."""
    return all(r["superficie"] in SURFACES and r["rol"] in ROLES for r in rows)


def as_int(value):
    """`NO-CLAIM` no es cero. Un conteo ausente no se cuenta como conteo bajo."""
    return None if value == NO_CLAIM else int(value)


def intra_repo_conflict(rows, slug, field="herramientas"):
    """(hay_conflicto, {superficie: valor}) para UN repo.

    Conflicto = dos superficies del mismo repo publican valores DISTINTOS y los dos son
    claims (ninguno es `NO-CLAIM`). Dos superficies que coinciden no son conflicto, y una
    sola superficie medida tampoco: es cota de instrumento, no acuerdo.
    """
    mine = {r["superficie"]: as_int(r[field]) for r in rows if r["slug"] == slug}
    claims = {s: v for s, v in mine.items() if v is not None}
    return (len(set(claims.values())) > 1, mine)


#: Veredictos de citabilidad. TRES, no dos.
CITABLE, NO_CITABLE, UNDER = "CITABLE", "NO-CITABLE", "COTA-DE-INSTRUMENTO"


def citable(rows, slug, field="herramientas"):
    """¿Se puede citar un conteo de este repo SIN nombrar la superficie? TRES respuestas.

    🔴 `UNDER` es la que la primera version de este instrumento no tenia, y es la que
    importa: un repo con UNA sola superficie medida salia `CITABLE`, como si sus superficies
    estuvieran de acuerdo. No lo estan — **no se midieron**. Publicar acuerdo donde hay una
    sola lectura es exactamente la conclusion demasiado amplia que P119 dejo registrada.
    """
    conflict, mine = intra_repo_conflict(rows, slug, field)
    if conflict:
        return NO_CITABLE
    if len({s for s, v in mine.items() if v is not None}) < 2:
        return UNDER
    return CITABLE


def frozen_claim(rows, slug, upstream="vishalsachdev/canvas-mcp"):
    """¿La DESCRIPCION de este fork repite un claim que el upstream ya no publica?"""
    mine = next((r for r in rows if r["slug"] == slug
                 and r["superficie"] == "DESCRIPTION"), None)
    up = [as_int(r["herramientas"]) for r in rows if r["slug"] == upstream]
    if mine is None or not up:
        return (False, "sin medicion")
    v = as_int(mine["herramientas"])
    if v is None:
        return (False, NO_CLAIM)
    if v in [u for u in up if u is not None]:
        return (False, "coincide con alguna superficie del upstream")
    return (True, f"el fork dice {v}, el upstream publica {sorted(u for u in up if u)}")


def main(argv):
    rows = load()
    if not vocab_ok(rows):
        print("VOCABULARIO FUERA DE RANGO", file=sys.stderr)
        return 2
    slugs = sorted({r["slug"] for r in rows})
    tsv = "--tsv" in argv
    if tsv:
        print("slug\trol\tsuperficies\tconflicto_intra_repo\tcitable_sin_superficie\tclaim_congelado")
    n_conf = n_frozen = 0
    for slug in slugs:
        rol = next(r["rol"] for r in rows if r["slug"] == slug)
        conflict, mine = intra_repo_conflict(rows, slug)
        frozen, why = frozen_claim(rows, slug)
        n_conf += conflict
        n_frozen += frozen
        surf = ", ".join(f"{s}={v if v is not None else NO_CLAIM}"
                         for s, v in sorted(mine.items()))
        if tsv:
            print(f"{slug}\t{rol}\t{surf}\t{conflict}\t{citable(rows, slug)}\t{frozen}")
        else:
            print(f"{slug}  [{rol}]")
            print(f"    herramientas por superficie: {surf}")
            print(f"    conflicto intra-repo: {'SI' if conflict else 'no'}"
                  f"   citable sin nombrar superficie: {citable(rows, slug)}")
            if rol == "FORK":
                print(f"    claim congelado: {'SI' if frozen else 'no'} — {why}")
    print()
    print(f"{len(rows)} mediciones de superficie sobre {len(slugs)} repos")
    print(f"{n_conf} repos donde DOS superficies del MISMO repo se contradicen")
    print(f"{n_frozen} forks cuya DESCRIPCION repite un claim que el upstream ya no publica")
    for verdict in (NO_CITABLE, UNDER, CITABLE):
        k = len([s for s in slugs if citable(rows, s) == verdict])
        print(f"{k} repos con veredicto {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
