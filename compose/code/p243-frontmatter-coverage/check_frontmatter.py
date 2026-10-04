#!/usr/bin/env python3
"""P243 — cobertura de frontmatter YAML sobre TODOS los .md del arbol, no solo los 8 de contenido.

El eje que ningun instrumento de esta KB medía: P239/P240 declaran su alcance en los 8
archivos de contenido, asi que los README de `compose/code/` quedaban fuera de toda
medicion de frontmatter. Un .md sin frontmatter se compila sin `industry` ni `region`.

Region es VOCABULARIO CERRADO. Una variante (`Latam`, `Europe`, `Asia Pacific`) no es un
error de lectura: es un balde nuevo que rompe el filtro sin romper el render — el defecto
que el pase 78 encontro en `repos/trending.md`.

Uso:
    python3 check_frontmatter.py [raiz]      # raiz por omision: el arbol del repo
    python3 check_frontmatter.py --tsv       # salida TSV para diffear entre pases
"""
import os
import sys

REGIONS = ("North America", "EMEA", "APAC", "LATAM", "Global")
REQUIRED = ("industry", "region", "updated")


def repo_root(start=None):
    d = os.path.abspath(start or os.path.dirname(__file__))
    while d != "/":
        if os.path.isdir(os.path.join(d, ".git")):
            return d
        d = os.path.dirname(d)
    return os.path.abspath(start or ".")


def markdown_files(root):
    out = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.join(base, f))
    return sorted(out)


def parse_frontmatter(text, raw=False):
    """Devuelve (dict, error). error None si el bloque esta bien formado.

    Con `raw=True` los valores se devuelven SIN normalizar por la derecha.
    P248: un normalizador no puede borrar el defecto que el instrumento debe
    detectar. `region: APAC ` se lee identico en Markdown, y si el compilador
    de abajo NO limpia, es un balde nuevo que rompe el filtro -- asi que la
    pregunta de vocabulario se hace contra el byte, no contra el valor ya
    limpiado. El espacio que SEPARA la clave del valor si es sintaxis, y por
    eso se saca siempre por la izquierda.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, "NO-FRONTMATTER"
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            body = lines[1:i]
            break
    else:
        return None, "UNCLOSED-FRONTMATTER"
    fields = {}
    for ln in body:
        if not ln.strip() or ln.lstrip().startswith("#"):
            continue
        if ":" not in ln:
            return None, "MALFORMED-LINE"
        k, v = ln.split(":", 1)
        fields[k.strip()] = (v.lstrip(" \t") if raw else v.strip())
    return fields, None


def findings_for(path, text):
    """Lista de (codigo, detalle) para un archivo."""
    found = []
    fields, err = parse_frontmatter(text, raw=True)
    if err:
        return [(err, "")]
    for key in REQUIRED:
        if key not in fields:
            found.append(("MISSING-KEY", key))
    region = fields.get("region")
    if region is not None and region not in REGIONS:
        # el caso que importa: variante de vocabulario, no ausencia.
        # El detalle se publica normalizado para que `Latam` y `Latam ` no
        # abran dos hallazgos distintos; el CODIGO ya dice que no esta en
        # vocabulario, y el byte crudo es lo que decidio el rechazo (P248).
        found.append(("REGION-NOT-IN-VOCABULARY", region.strip()))
    return found


def scan(root):
    rows = []
    for path in markdown_files(root):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        rel = os.path.relpath(path, root)
        for code, detail in findings_for(path, text):
            rows.append((rel, code, detail))
    return rows


def main(argv):
    tsv = "--tsv" in argv
    args = [a for a in argv[1:] if not a.startswith("--")]
    root = repo_root(args[0] if args else None)
    total = len(markdown_files(root))
    rows = scan(root)
    if tsv:
        print("file\tcode\tdetail")
        for r in rows:
            print("\t".join(r))
    else:
        for rel, code, detail in rows:
            print("%s: %s%s" % (rel, code, (" (%s)" % detail) if detail else ""))
    clean = total - len({r[0] for r in rows})
    # total propio, en una de las formas que el lector anclado ya reconoce (P126 regla 3)
    print("%d de %d archivos .md con frontmatter completo y region en vocabulario" % (clean, total))
    return 1 if rows else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
