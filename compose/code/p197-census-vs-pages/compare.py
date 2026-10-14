#!/usr/bin/env python3
"""p197-census-vs-pages -- ¿«nunca sondeada» significa «no medida», o sólo
«ausente del TSV del censo»?

p196 pre-registró: «sondear las 26 filas del padrón que ningún censo alcanzó».  Esta
pasada las sondeó (30 con la comparación plegada por caso) y la pregunta que surgió
es anterior: ¿están medidas EN LAS PÁGINAS?  Porque una fila publicada con su cifra
de bytes está medida, esté o no en el artefacto del censo.

Instrumento: para cada fila sondeada esta pasada, busca su slug en las ocho páginas y
busca la cifra de bytes DE ESTA PASADA cerca del slug, en cualquiera de las grafías que
esta base usa para un número (7651, "7 651", "7,651", espacios finos y duros).

Veredictos:
  AGREE-PUBLISHED   la página trae la MISMA cifra -> la fila estaba medida y el canal
                    de árbol la reproduce: acuerdo entre canales independientes
  DISAGREE          la página trae OTRA cifra junto al slug -> contradicción real
  SLUG-NO-FIGURE    el slug está publicado pero sin cifra de bytes
  SLUG-ABSENT       el slug no aparece en ninguna página
Sale no-cero si hay cualquier DISAGREE.
"""
import re, sys, os, unicodedata

PAGES = ["agents/top.md","agents/trending.md","repos/foundations.md","repos/trending.md",
         "verticals/solutions.md","compose/patterns.md","intel/market.md","intel/trends.md"]
SEPS = ["", " ", ",", " ", " ", " ", "."]

SLUG_RX = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9._-]+")
FIG_RX  = re.compile(r"`?([0-9][0-9    ,.]{2,})`?\s*(?:B\b|bytes)")
# Una cifra NO es una cifra de concesion si la linea la declara de otra cosa.  La ventana
# es el propio parentesis o celda: 24 caracteres antes de la cifra.
NOT_PAYLOAD = re.compile(r"(README|readme|Readme|paths|rutas|★|stars|estrellas|LOC|commits)")


def variants(n):
    s = str(n)
    out = {s}
    if len(s) > 3:
        for sep in SEPS:
            out.add(s[:-3] + sep + s[-3:])
    return out


def load(root):
    txt = {}
    for p in PAGES:
        fp = os.path.join(root, p)
        if os.path.exists(fp):
            txt[p] = open(fp, encoding="utf-8").read()
    return txt


def other_slugs(line, slug):
    """Otros slugs nombrados en la misma linea -- la causa de Gap 441."""
    out = set()
    for m in SLUG_RX.finditer(line):
        cand = m.group(0)
        if cand.lower() == slug.lower():
            continue
        if cand.count("/") != 1:
            continue
        if cand.lower() in ("https/", "http/"):
            continue
        # un fragmento de URL o de ruta no es un slug publicado
        if m.start() >= 2 and line[m.start()-2:m.start()] in ("//", ".c", ".o"):
            continue
        out.add(cand)
    return out


def figures_in(line):
    """Las cifras en bytes de una linea, menos las que la linea declara de otra cosa."""
    out = set()
    for m in FIG_RX.finditer(line):
        pre = line[max(0, m.start() - 24):m.start()]
        if NOT_PAYLOAD.search(pre):
            continue
        cand = re.sub(r"[^0-9]", "", m.group(1))
        if cand:
            out.add(cand)
    return out


def classify_rows(pages, rows):
    res = []
    for r in rows:
        slug, exists, _np, _scope, _path, byts, fam, verdict = r[:8]
        want = variants(byts) if byts.isdigit() and byts != "0" else set()
        hit_pages, fig_pages, other, shared = [], [], set(), set()
        for p, t in pages.items():
            lines = [ln for ln in t.splitlines() if slug in ln]
            if not lines:
                continue
            hit_pages.append(p)
            matched = False
            for ln in lines:
                if want and any(v in ln for v in want):
                    matched = True
                    continue
                figs = figures_in(ln) - {byts}
                if not figs:
                    continue
                co = other_slugs(ln, slug)
                if co:
                    shared |= co
                else:
                    other |= figs
            if matched:
                fig_pages.append(p)
        if not hit_pages:
            v = "SLUG-ABSENT"
        elif fig_pages:
            v = "AGREE-PUBLISHED"
        elif other:
            v = "DISAGREE"
        elif shared:
            v = "MULTI-SLUG-LINE"
        else:
            v = "SLUG-NO-FIGURE"
        res.append((slug, exists, byts, fam, verdict, v,
                    ",".join(sorted(fig_pages)) or "-",
                    ",".join(sorted(other | shared)) or "-"))
    return res


def main(root, tsv, out):
    pages = load(root)
    rows = [l.rstrip("\n").split("\t") for l in open(tsv, encoding="utf-8")][1:]
    res = classify_rows(pages, rows)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("slug\texists\tbytes_p197\tfamily_p197\tread_verdict\tpage_verdict\t"
                 "pages_with_figure\tother_figures_or_slugs\n")
        for row in res:
            fh.write("\t".join(row) + "\n")
    tally = {}
    for row in res:
        tally[row[5]] = tally.get(row[5], 0) + 1
    for k in sorted(tally):
        print("%-18s %s" % (k, tally[k]))
    for row in res:
        extra = row[7] if row[7] != "-" else ""
        print("%-48s %7s %-22s %-16s %s" % (row[0], row[2], row[3], row[5], extra))
    return 1 if tally.get("DISAGREE") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
