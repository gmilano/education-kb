#!/usr/bin/env python3
"""`P334` — el titular de una FIGURA se resuelve por BYTES, no por el `oer` del item.

Cruza las figuras del redistribuidor contra el arbol `media/` de UNA coleccion del
titular por `sha256` de contenido, y reporta el acierto POR OBRA CITADA. El acierto
por obra es a la vez el control positivo (la obra que corresponde acierta) y el
negativo (las demas dan 0).

Uso: python3 intersect_media.py RAIZ_REDISTRIBUIDOR DIR_MEDIA_DEL_TITULAR
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter

OBRA = re.compile(r"openstax\.org/(?:details/)?books/([a-z0-9-]+)", re.I)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def obra_de(oer):
    m = OBRA.search(oer or "")
    if m:
        return m.group(1)
    return "(oer VACIO)" if not (oer or "").strip() else "(no-openstax)"


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    root, media = argv
    pool = os.path.join(root, "content-pool")
    if not os.path.isdir(pool) or not os.path.isdir(media):
        print("arbol o media/ no materializado (NO-CLAIM)", file=sys.stderr)
        return 2

    titular = {}
    for f in sorted(os.listdir(media)):
        p = os.path.join(media, f)
        if os.path.isfile(p):
            titular.setdefault(sha(p), []).append(f)

    tot, hit = Counter(), Counter()
    pares = []
    for pid in sorted(os.listdir(pool)):
        d = os.path.join(pool, pid)
        fd = os.path.join(d, "figures")
        if not os.path.isdir(fd):
            continue
        figs = [f for f in sorted(os.listdir(fd)) if os.path.isfile(os.path.join(fd, f))]
        if not figs:
            continue
        pj = os.path.join(d, pid + ".json")
        oer = ""
        if os.path.isfile(pj):
            try:
                oer = json.load(open(pj, encoding="utf-8")).get("oer", "") or ""
            except Exception:  # noqa: BLE001
                oer = ""
        o = obra_de(oer)
        for f in figs:
            tot[o] += 1
            h = sha(os.path.join(fd, f))
            if h in titular:
                hit[o] += 1
                pares.append((pid, f, o, titular[h][0], h[:16]))

    print(f"titular: {media} — {sum(len(v) for v in titular.values())} archivos,"
          f" {len(titular)} imagenes distintas")
    print(f"{'obra citada por el item':32s} {'figuras':>8s} {'byte-identicas':>15s} {'%':>7s}")
    for o, n in tot.most_common():
        print(f"{o:32s} {n:8d} {hit[o]:15d} {100.0 * hit[o] / n:6.2f}%")
    T, H = sum(tot.values()), sum(hit.values())
    print(f"{'TOTAL':32s} {T:8d} {H:15d} {100.0 * H / T if T else 0:6.2f}%")
    print("\npares (item, figura, obra citada, archivo del titular, sha256):")
    for r in pares:
        print("  " + "\t".join(r))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
