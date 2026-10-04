#!/usr/bin/env python3
"""P253 — la identidad de paquete de un repositorio NO es un hecho a una sola profundidad.

Profundidad 0 (`package.json` de la raiz) es una DECLARACION.
El registro es la PUBLICACION.
En un monorepo el manifiesto publicado puede vivir a profundidad N y DECIRLO
(`repository.directory`).

Un instrumento que lee profundidad 0 y le pregunta al registro por ESE nombre no mide
ninguna de las dos cosas: mide la interseccion de sus propias dos conjeturas.

La COMPUERTA de este modulo: ninguna lectura de arbol puede, por si sola, producir
"no tiene paquete", y ningun 404 sobre un nombre CONJETURADO puede producir
"no publicado". Las dos salen `UNDETERMINED`.
"""

# Las unicas procedencias de sonda que este modulo reconoce.
#   declared  : el nombre salio del `package.json` del arbol -> su 404 SI es informativo
#   registry  : la fila se encontro preguntandole al registro -> publicacion directa
#   guessed   : el nombre lo CONSTRUYO el barrido (p. ej. "@" + dueno + "/" + repo)
PROBE_DECLARED = "declared"
PROBE_REGISTRY = "registry"
PROBE_GUESSED = "guessed"


def _probes(row):
    return {p for p in str(row.get("probe_kind", "")).split("+") if p}


def _empty(v):
    return v in (None, "", "-", "ABSENT")


def package_identity(row):
    """Devuelve (veredicto, detalle). Nunca afirma ausencia desde el arbol ni desde una conjetura."""
    probes = _probes(row)
    slug = row.get("slug", "")
    tree_name = row.get("tree_name")
    pub_name = row.get("pub_name")
    pub_repo = row.get("pub_repo")
    pub_dir = row.get("pub_dir")
    http = str(row.get("tree_name_http", "-"))

    # ---- COMPUERTA 1: sin ninguna sonda de registro no se contesta nada.
    if not probes or probes == {PROBE_GUESSED}:
        return ("UNDETERMINED", "solo nombres conjeturados: un 404 es un hecho sobre la conjetura")

    # ---- COMPUERTA 2: el arbol no vio manifiesto. Eso es del arbol, no del mundo.
    if _empty(tree_name) and PROBE_REGISTRY not in probes:
        return ("UNDETERMINED", "el arbol no vio manifiesto y no se le pregunto al registro")

    # Publicado y encontrado POR el registro, sin que el arbol lo declarara.
    if _empty(tree_name) and PROBE_REGISTRY in probes and not _empty(pub_name):
        return ("PUBLISHED-NOT-IN-TREE", f"{pub_name} existe aunque la lectura de arbol dio '-'")

    # ---- El arbol declaro un nombre. Ahora el registro decide.
    if not _empty(tree_name):
        if http == "404":
            # El nombre DECLARADO no existe. Pero quizas el repo publica OTRA cosa.
            # ⚠️ El discriminador es el MANTENEDOR: un manifiesto de subdirectorio PRESENTE en el
            # arbol no es una publicacion. Sin mantenedor atribuido no se afirma que publique.
            if not _empty(pub_dir) and _empty(row.get("pub_maintainer")):
                return ("SUBDIR-MANIFEST-PRESENT",
                        f"./{pub_dir} lleva el manifiesto de {pub_name}, sin publicacion propia atribuida")
            if not _empty(pub_name) and not _empty(pub_dir):
                return ("PUBLISHED-AT-SUBDIR",
                        f"raiz declara {tree_name} (no publicado); se publica {pub_name} desde ./{pub_dir}")
            if not _empty(pub_name):
                return ("PUBLISHED-OTHER-NAME",
                        f"raiz declara {tree_name} (no publicado); se publica {pub_name}")
            if PROBE_GUESSED in probes:
                return ("DECLARED-NOT-PUBLISHED",
                        f"{tree_name} da 404 y no se hallo publicacion (conjeturas agotadas, NO exhaustivo)")
            return ("DECLARED-NOT-PUBLISHED", f"{tree_name} da 404")
        if http == "200":
            # Publicado. ¿Aterriza en ESTE repo o en otro?
            if not _empty(pub_repo) and _norm(pub_repo) != _norm(slug):
                return ("PUBLISHED-BY-OTHER",
                        f"{tree_name} existe pero apunta a {pub_repo}, no a {slug}")
            if not _empty(pub_dir):
                return ("PUBLISHED-AT-SUBDIR", f"{pub_name} publicado desde ./{pub_dir}")
            return ("PUBLISHED-AT-ROOT", f"{pub_name} publicado y apunta a {slug}")

    # Manifiesto de subdirectorio visto en el arbol, sin publicacion propia atribuida.
    if not _empty(pub_dir) and _empty(row.get("pub_maintainer")):
        return ("SUBDIR-MANIFEST-PRESENT",
                f"./{pub_dir} lleva el manifiesto de {pub_name}, sin publicacion propia atribuida")

    return ("UNDETERMINED", "las sondas corridas no alcanzan para un veredicto")


def _norm(s):
    return str(s or "").strip().lower().rstrip("/")


def collision(row):
    """Un nombre de npm igual al nombre del repo que aterriza en OTRO actor."""
    same = _norm(row.get("npm_name")) == _norm(str(row.get("repo_of_same_name", "")).split("/")[-1])
    pointer_elsewhere = _empty(row.get("npm_repo_pointer"))
    if same and pointer_elsewhere:
        return ("NAME-COLLISION",
                f"{row.get('npm_name')} lo mantiene {row.get('npm_maintainer')} sin puntero; "
                f"{row.get('repo_of_same_name')} publica {row.get('repo_publishes_instead')}")
    return ("NO-CLAIM", "no se sostiene una colision con estas sondas")


def resolution_is_decidable(rows):
    """¿La capa de paquete resuelve el cohorte? Cuenta filas que aterrizan en UN repo concreto."""
    landed = [r for r in rows
              if package_identity(r)[0] in
              ("PUBLISHED-AT-ROOT", "PUBLISHED-AT-SUBDIR", "PUBLISHED-NOT-IN-TREE",
               "PUBLISHED-BY-OTHER", "PUBLISHED-OTHER-NAME")]
    return (len(landed) > 0, len(landed))


def load(path):
    rows, head = [], None
    with open(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            cells = line.split("\t")
            if head is None:
                head = cells
                continue
            rows.append(dict(zip(head, cells)))
    return rows
