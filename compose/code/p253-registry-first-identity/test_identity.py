#!/usr/bin/env python3
"""Suite de P253. Imprime su propio total (regla 3 de P126)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from identity import (package_identity, collision, resolution_is_decidable, load,  # noqa: E402
                      PROBE_GUESSED)

ok = fail = 0


def chk(label, got, want):
    global ok, fail
    if got == want:
        ok += 1
        print(f"PASS {label}")
    else:
        fail += 1
        print(f"FAIL {label}\n     got ={got!r}\n     want={want!r}")


def row(**kw):
    base = dict(slug="", tree_name="-", tree_repo="-", tree_name_http="-", pub_name="-",
                pub_version="-", pub_maintainer="-", pub_repo="-", pub_dir="-", probe_kind="")
    base.update(kw)
    return base


HERE = os.path.dirname(os.path.abspath(__file__))
real = load(os.path.join(HERE, "result.2026-10-04.tsv"))
coll = load(os.path.join(HERE, "collision.2026-10-04.tsv"))

# ------------------------------------------------- 1. LA COMPUERTA: el arbol no puede negar solo
chk("una lectura de arbol sin manifiesto NO produce 'sin paquete'",
    package_identity(row(slug="a/b", tree_name="-", probe_kind="tree"))[0], "UNDETERMINED")
chk("sin ninguna sonda no se contesta",
    package_identity(row(slug="a/b", probe_kind=""))[0], "UNDETERMINED")

# ------------------------------------------------- 2. LA COMPUERTA: un 404 conjeturado no niega
chk("un 404 sobre un nombre CONJETURADO sale UNDETERMINED, no 'no publicado'",
    package_identity(row(slug="a/b", tree_name="-", probe_kind=PROBE_GUESSED))[0], "UNDETERMINED")
# el caso que lo prueba en el mundo: el scope NO es el dueno de GitHub
chk("scope != dueno: @owen-x-tech publica por owentaylor, asi que conjeturar el scope es invalido",
    package_identity(row(slug="owentaylor/canvas-mcp", tree_name="-",
                         pub_name="@owen-x-tech/canvas-mcp", pub_maintainer="owen-x-tech",
                         pub_repo="owentaylor/canvas-mcp", probe_kind="registry"))[0],
    "PUBLISHED-NOT-IN-TREE")

# ------------------------------------------------- 3. CONTROL NEGATIVO: la afirmacion del pase 83
# "los 7 del racimo PUBLICAN el mismo name canvas-mcp-code-api" -> el nombre da 404: DECLARAN.
chk("el nombre que el pase 83 llamo 'publicado' sale DECLARED-NOT-PUBLISHED",
    package_identity(row(slug="AmirF194/canvas-mcp", tree_name="canvas-mcp-code-api",
                         tree_repo="ABSENT", tree_name_http="404",
                         probe_kind="declared+guessed"))[0],
    "DECLARED-NOT-PUBLISHED")
# "la resolucion por capa de paquete en esta familia es INDECIDIBLE" -> es decidible.
decidable, landed = resolution_is_decidable(real)
chk("la resolucion por capa de paquete del cohorte NO es indecidible", decidable, True)
chk("10 de las 17 filas aterrizan en un repo concreto", landed, 10)

# ------------------------------------------------- 4. presente != publicado (el discriminador)
chk("un manifiesto de subdirectorio SIN mantenedor atribuido no es una publicacion",
    package_identity(row(slug="fdis111/canvas-mcp", tree_name="canvas-mcp-code-api",
                         tree_repo="ABSENT", tree_name_http="404", pub_name="canvas-mcp",
                         pub_dir="cli", pub_maintainer="-",
                         probe_kind="declared+tree-subdir"))[0],
    "SUBDIR-MANIFEST-PRESENT")
chk("el mismo manifiesto CON mantenedor y puntero si es publicacion a profundidad N",
    package_identity(row(slug="vishalsachdev/canvas-mcp", tree_name="canvas-mcp-code-api",
                         tree_repo="ABSENT", tree_name_http="404", pub_name="canvas-mcp",
                         pub_dir="cli", pub_maintainer="vishalsachdev",
                         pub_repo="vishalsachdev/canvas-mcp",
                         probe_kind="declared+registry"))[0],
    "PUBLISHED-AT-SUBDIR")

# ------------------------------------------------- 5. aterriza en OTRO dueno
chk("un nombre publicado que apunta a otro repo sale PUBLISHED-BY-OTHER",
    package_identity(row(slug="algorithm0r/canvas-lms-mcp", tree_name="canvas-lms-mcp",
                         tree_repo="bruchris/canvas-lms-mcp", tree_name_http="200",
                         pub_name="canvas-lms-mcp", pub_repo="bruchris/canvas-lms-mcp",
                         pub_maintainer="bruchris", probe_kind="declared"))[0],
    "PUBLISHED-BY-OTHER")
chk("y el caso sano aterriza en si mismo",
    package_identity(row(slug="bruchris/canvas-lms-mcp", tree_name="canvas-lms-mcp",
                         tree_repo="bruchris/canvas-lms-mcp", tree_name_http="200",
                         pub_name="canvas-lms-mcp", pub_repo="bruchris/canvas-lms-mcp",
                         pub_maintainer="bruchris", probe_kind="declared"))[0],
    "PUBLISHED-AT-ROOT")

# ------------------------------------------------- 6. la colision de nombre entre capas
chk("mcp-canvas-lms es una colision: mismo nombre, otro actor, sin puntero",
    collision(coll[0])[0], "NAME-COLLISION")
chk("una fila con puntero propio NO es colision",
    collision(dict(npm_name="canvas-lms-mcp", npm_maintainer="bruchris",
                   npm_repo_pointer="git+https://github.com/bruchris/canvas-lms-mcp.git",
                   repo_of_same_name="bruchris/canvas-lms-mcp",
                   repo_publishes_instead="canvas-lms-mcp"))[0],
    "NO-CLAIM")

# ------------------------------------------------- 7. invariantes del cohorte real
chk("el cohorte real tiene 17 filas", len(real), 17)
chk("17 slugs DISTINTOS", len({r["slug"] for r in real}), 17)
verdicts = [package_identity(r)[0] for r in real]
chk("la columna veredicto del TSV coincide con el modulo",
    verdicts, [r["verdict"] for r in real])
chk("5 publicados en la raiz", verdicts.count("PUBLISHED-AT-ROOT"), 5)
chk("1 publicado a profundidad N", verdicts.count("PUBLISHED-AT-SUBDIR"), 1)
chk("5 DECLARAN un nombre que no existe", verdicts.count("DECLARED-NOT-PUBLISHED"), 5)
chk("3 publicados que la lectura de arbol NO vio",
    verdicts.count("PUBLISHED-NOT-IN-TREE"), 3)
chk("1 manifiesto presente sin publicacion", verdicts.count("SUBDIR-MANIFEST-PRESENT"), 1)
chk("1 publicado por otro", verdicts.count("PUBLISHED-BY-OTHER"), 1)
chk("1 indeterminado, y es el unico", verdicts.count("UNDETERMINED"), 1)
chk("el reparto suma el cohorte", 5 + 1 + 5 + 3 + 1 + 1 + 1, len(real))

# el hecho que vuelve a P183: 7 arboles declaran el MISMO nombre inexistente
declaring = [r for r in real if r["tree_name"] == "canvas-mcp-code-api"]
chk("7 arboles declaran canvas-mcp-code-api", len(declaring), 7)
chk("y los 7 tienen repository ABSENT",
    all(r["tree_repo"] == "ABSENT" for r in declaring), True)
chk("de esos 7, exactamente 1 tiene publicacion propia atribuida",
    sum(1 for r in declaring if r["pub_maintainer"] not in ("-", "")), 1)

print(f"\n{ok}/{ok + fail}")
sys.exit(1 if fail else 0)
