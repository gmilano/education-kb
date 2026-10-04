#!/usr/bin/env python3
"""`measure.py` — la SATURACION de un barrido regional se mide; declararla es otra cosa.

Pase 95 del 2026-10-04. Los pases 91/92/93/94 vienen registrando que las cuatro busquedas
regionales obligatorias devuelven lo mismo, y el encargo pide que si una region no rinde se
ESCRIBA. 🔴 **Pero «saturacion» dicha en prosa no tiene denominador**, y el pase 93 dejo la
regla: *un conteo solo es un conteo si ENUMERA*.

Este instrumento la aplica al barrido regional: se enumeran los hechos que las busquedas de HOY
devolvieron, uno por fila, con el patron que los identifica; se mide cuantos YA estan en el
corpus publicado; y el resultado es una fraccion con su lista, no un adjetivo.

Uso (desde la raiz de la KB):
  python3 compose/code/p287-regional-saturation/measure.py \
      compose/code/p287-regional-saturation/facts.2026-10-04.tsv \
      intel/market.md intel/trends.md agents/top.md agents/trending.md \
      verticals/solutions.md repos/foundations.md repos/trending.md compose/patterns.md
"""
import re
import sys


def load_facts(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh):
            line = line.rstrip("\n")
            if not line.strip() or (i == 0 and line.startswith("region\t")):
                continue
            parts = line.split("\t")
            if len(parts) >= 3:
                rows.append((parts[0], parts[1], parts[2]))
    return rows


def measure(facts, corpus):
    """-> (total, ya, [(region, fact) nuevos])"""
    new = []
    for region, fact, pat in facts:
        if not re.search(pat, corpus, re.I):
            new.append((region, fact))
    return len(facts), len(facts) - len(new), new


def main(argv):
    facts = load_facts(argv[1])
    corpus = ""
    for f in argv[2:]:
        with open(f, encoding="utf-8", errors="replace") as fh:
            corpus += fh.read()
    total, already, new = measure(facts, corpus)
    by = {}
    for region, fact, pat in facts:
        by.setdefault(region, [0, 0])
        by[region][0] += 1
    for region, fact in new:
        by[region][1] += 1
    print("region\thechos\tnuevos")
    for region in sorted(by):
        print("%s\t%d\t%d" % (region, by[region][0], by[region][1]))
    print("TOTAL\t%d\t%d" % (total, len(new)))
    print("ya_en_la_base\t%d" % already)
    for region, fact in new:
        print("NUEVO\t%s\t%s" % (region, fact))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
