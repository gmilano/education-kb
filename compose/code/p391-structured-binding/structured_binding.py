#!/usr/bin/env python3
"""P391 — el binding fingerprint->repo leido de la CELDA de tabla, no de la LINEA.

Accion B pre-registrada por el pase 118. `P385` midio que un binding cosechado de
PROSA es un intervalo [3, 22] porque los dos extractores disponibles estan sesgados
en direcciones opuestas:

  - ANCLADO A URL: solo ve `github.com/owner/repo`. Se pierde la familia de 8 forks
    que las filas nombran con handles pelados. SUBCUENTA -> PISO = 3.
  - PERMISIVO: liga todo repo nombrado en la misma LINEA, incluido el que solo
    co-ocurre en el parrafo resumen. SOBRECUENTA -> TECHO = 22.

Este extractor corrige las dos puntas con UNA decision estructural: el binding solo
existe dentro de una FILA DE TABLA, y el repo solo se lee de una CELDA DE IDENTIDAD.

  1. Solo filas de tabla markdown (`| ... | ... |`). Mata la co-ocurrencia de prosa,
     que es de donde salia `de8107bf9312 -> {VedShh/Tutor-AI, pupilfirst/pupilfirst}`.
  2. Dentro de la fila, una celda es de IDENTIDAD si su texto, limpio de markdown,
     es *nada mas que* referencias a repos/handles (y separadores). Una celda de
     prosa larga ("Que es, y por que entra") NO liga, aunque nombre un repo.
  3. Los handles pelados de una celda de identidad SI ligan, que es justo lo que el
     extractor anclado a URL no veia.

Separacion de responsabilidades respecto de `P386`: este modulo mide el BINDING
(que repos comparten un fingerprint). Decidir si ese fingerprint transporta LINAJE
es de la compuerta de `p386-pristine-dedup-gate/`, que se abstiene con titular
ausente. Un racimo contado aqui NO es una afirmacion de linaje.
"""
import collections
import re
import sys

SHA = re.compile(r"sha256[`:\s]{0,4}([0-9a-f]{12,64})")
URL = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*)")
SLUG = re.compile(r"`([A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*)`")
HANDLE = re.compile(r"`([A-Za-z0-9][A-Za-z0-9._-]{2,})`")
ANCHOR = re.compile(r"(?:DERIVATIVE-OF|fork de|forks de|upstream)\s+`?([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*)`?", re.I)

NOT_HANDLE = re.compile(
    r"^(P\d+|p\d+[a-z-]*|[0-9a-f]{8,}|\d+|[A-Z][A-Z0-9_-]{2,}|"
    r"sha256|LICENSE|COPYING|main|master|HEAD|develop|true|false)$"
)
NOISE = re.compile(
    r"^(main|master|HEAD|docs|src|fix|feature|LICENSE|COPYING|dependabot)/"
    r"|\.(md|txt|json|py|toml|cfg|html|rst)$",
    re.I,
)
# Lo que puede aparecer en una celda de IDENTIDAD sin convertirla en prosa:
# separadores, enfasis, enlaces, notas de canonicidad, emojis de veredicto.
IDENTITY_FILLER = re.compile(
    r"(\*+|_+|~+|·|\||,|;|/|\(|\)|\[|\]|&|→|⇒|…|\.|:|-|–|—|\s|"
    r"canonica|canónica|canonical|registrada|upstream|fork|forks|nuevo|nueva|"
    r"idem|ídem|DERIVATIVE-OF|de|y|and|the|[0-9]|★|🆕|🟢|🔴|🔵|⚠️|🔬|✅|📌|x|×)+",
    re.I,
)
MAX_IDENTITY_WORDS = 14


def norm(s):
    return s[:12]


def cells(line):
    """Celdas de una fila de tabla markdown, o None si no es fila de tabla."""
    s = line.strip()
    if not s.startswith("|") or s.count("|") < 2:
        return None
    body = s.strip("|")
    if re.fullmatch(r"[\s:|-]+", body):   # fila separadora ---|---
        return None
    return [c.strip() for c in body.split("|")]


def repos_in(cell):
    """Repos nombrados en una celda, por cualquiera de las tres convenciones."""
    out = {m.rstrip(".,)`") for m in URL.findall(cell)}
    out |= {m.rstrip(".,)`") for m in SLUG.findall(cell)}
    out |= {
        m for m in HANDLE.findall(cell)
        if "/" not in m and not NOT_HANDLE.match(m) and "." not in m
    }
    return {r for r in out if not NOISE.search(r)}


def is_identity_cell(cell, found):
    """Una celda es de IDENTIDAD si, sacadas las referencias a repos, no queda prosa.

    Es el criterio que distingue la celda `| vishalsachdev/canvas-mcp |` de la celda
    `| Backend del chatbot de MIT Open Learning que ayuda al alumno a ... |`, que
    tambien puede nombrar un repo pero solo lo MENCIONA.
    """
    if not found:
        return False
    rest = cell
    for r in sorted(found, key=len, reverse=True):
        rest = rest.replace(r, " ")
        if "/" in r:
            rest = rest.replace(r.split("/", 1)[1], " ")
    rest = re.sub(r"https?://\S*", " ", rest)
    rest = IDENTITY_FILLER.sub(" ", rest)
    leftover = [w for w in rest.split() if len(w) > 1]
    return len(leftover) == 0 and len(cell.split()) <= MAX_IDENTITY_WORDS


def extract(lines):
    """Devuelve ({fingerprint: {repos}}, filas_de_tabla_vistas)."""
    out = collections.defaultdict(set)
    rows = 0
    for line in lines:
        if "sha256" not in line:
            continue
        cs = cells(line)
        if cs is None:
            continue
        rows += 1
        shas = [norm(s) for s in SHA.findall(line)]
        if not shas:
            continue
        anchor = ANCHOR.search(line)
        anchor_repo = anchor.group(2) if anchor else None
        bound = set()
        for c in cs:
            found = repos_in(c)
            if not is_identity_cell(c, found):
                continue
            for r in found:
                # Un handle pelado se califica con el repo ancla de la fila, si lo hay,
                # para que dos familias distintas no colapsen en el mismo handle.
                bound.add(r if "/" in r else (f"{r}/{anchor_repo}" if anchor_repo else r))
        for s in shas:
            out[s] |= bound
    return out, rows



# --- Lectura por COLUMNA TIPADA ------------------------------------------------
# El extractor de arriba sigue exigiendo el token literal `sha256` pegado al digest.
# Varias tablas de esta base NO lo escriben asi: lo ponen en el ENCABEZADO de la
# columna y dejan el hex pelado en las celdas. Para esas filas, un extractor
# anclado al token cuenta CERO. Leer la columna por su encabezado es la unica
# lectura verdaderamente estructurada.
HEX12 = re.compile(r"\b([0-9a-f]{12,64})\b")
SHA_HEADER = re.compile(r"sha256|huella|fingerprint|digest", re.I)
REPO_HEADER = re.compile(r"repo|slug|pieza|proyecto|miembro|fork", re.I)
SEP_ROW = re.compile(r"^[\s:|-]+$")


def _is_sep(line):
    s = line.strip()
    return s.startswith("|") and bool(SEP_ROW.fullmatch(s))


def extract_typed(lines):
    """Binding leido de columnas tipadas por su ENCABEZADO.

    Devuelve ({fingerprint: {repos}}, filas_leidas).
    """
    out = collections.defaultdict(set)
    header, sha_cols, repo_cols, rows = None, [], [], 0
    prev = None
    for line in lines:
        cs = cells(line)
        if cs is None:
            if _is_sep(line) and prev is not None:
                header = prev
                sha_cols = [i for i, h in enumerate(header) if SHA_HEADER.search(h)]
                repo_cols = [i for i, h in enumerate(header) if REPO_HEADER.search(h)]
            else:
                header, sha_cols, repo_cols = None, [], []
            prev = cells(line) if cells(line) else None
            continue
        prev = cs
        if header is None or not sha_cols:
            continue
        shas = set()
        for i in sha_cols:
            if i < len(cs):
                shas |= {norm(h) for h in HEX12.findall(cs[i])}
        if not shas:
            continue
        rows += 1
        anchor = ANCHOR.search(line)
        anchor_repo = anchor.group(2) if anchor else None
        bound = set()
        # Columnas declaradas de repo primero; si el encabezado no las declara,
        # se cae al criterio de celda de identidad.
        cand = [cs[i] for i in repo_cols if i < len(cs)] or cs
        for c in cand:
            found = repos_in(c)
            if c in cs and not repo_cols and not is_identity_cell(c, found):
                continue
            for r in found:
                bound.add(r if "/" in r else (f"{r}/{anchor_repo}" if anchor_repo else r))
        for s in shas:
            out[s] |= bound
    return out, rows


def merge(a, b):
    out = collections.defaultdict(set)
    for d in (a, b):
        for k, v in d.items():
            out[k] |= v
    return out


def clusters(binding):
    return {k: v for k, v in binding.items() if len(v) >= 2}


def main(argv):
    lines = []
    for p in argv:
        lines += open(p, encoding="utf-8").read().split("\n")
    anchored, rows_a = extract(lines)
    typed, rows_t = extract_typed(lines)
    both = merge(anchored, typed)
    ca, ct, cb = clusters(anchored), clusters(typed), clusters(both)
    print("extractor\tfilas\tfingerprints\tracimos")
    print(f"celda-anclada-al-token\t{rows_a}\t{len(anchored)}\t{len(ca)}")
    print(f"columna-tipada-por-encabezado\t{rows_t}\t{len(typed)}\t{len(ct)}")
    print(f"union-estructurada\t{rows_a + rows_t}\t{len(both)}\t{len(cb)}")
    for k, v in sorted(cb.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        origen = "ambos" if k in ca and k in ct else ("token" if k in ca else "encabezado")
        print(f"racimo\t{k}\t{len(v)}\t{origen}\t{','.join(sorted(v))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
