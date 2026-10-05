#!/usr/bin/env python3
"""`P332` — la EXTENSION de un archivo de imagen no es su FORMATO.

Censa el formato REAL (firma de bytes) de los archivos de imagen de un arbol y lo
compara contra lo que su extension promete. Es el instrumento que impide que un
barrido del arbol del titular se filtre «por extension» desde una premisa falsa.

Uso: python3 sniff_format.py RAIZ [--ext .gif]
"""
import os
import sys
from collections import Counter

SIGS = (
    (b"GIF87a", "GIF"),
    (b"GIF89a", "GIF"),
    (b"\x89PNG\r\n\x1a\n", "PNG"),
    (b"\xff\xd8\xff", "JPEG"),
    (b"BM", "BMP"),
    (b"II*\x00", "TIFF"),
    (b"MM\x00*", "TIFF"),
    (b"%PDF", "PDF"),
    (b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1", "OLE/CFB"),
)


def formato(head):
    """Formato por FIRMA. Nunca por extension (`P332`)."""
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return "WEBP"
    if head[:5] == b"<?xml" or head[:4] == b"<svg":
        return "SVG/XML"
    for magic, name in SIGS:
        if head.startswith(magic):
            return name
    return "OTRO:" + head[:8].hex()


def censo(root, exts=None):
    sigs = Counter()
    ejemplo = {}
    total = 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d != ".git"]
        for f in sorted(fn):
            low = f.lower()
            if exts and not any(low.endswith(e) for e in exts):
                continue
            p = os.path.join(dp, f)
            try:
                with open(p, "rb") as fh:
                    head = fh.read(12)
            except OSError:
                continue
            total += 1
            k = formato(head)
            sigs[k] += 1
            ejemplo.setdefault(k, os.path.relpath(p, root))
    return total, sigs, ejemplo


def main(argv):
    if not argv:
        print(__doc__, file=sys.stderr)
        return 2
    root = argv[0]
    exts = None
    if "--ext" in argv:
        exts = [argv[argv.index("--ext") + 1].lower()]
    total, sigs, ej = censo(root, exts)
    if not total:
        print("0 archivos en el filtro: no hay censo que publicar (NO-CLAIM)", file=sys.stderr)
        return 2
    etiqueta = exts[0] if exts else "(todas las extensiones)"
    print(f"arbol      : {root}")
    print(f"filtro     : {etiqueta}")
    print(f"archivos   : {total}")
    for k, v in sigs.most_common():
        print(f"  {k:26s} {v:6d}  {100.0 * v / total:5.1f}%   ej: {ej[k]}")
    if exts:
        promete = {".gif": "GIF", ".png": "PNG", ".jpg": "JPEG", ".jpeg": "JPEG", ".webp": "WEBP"}.get(exts[0])
        if promete:
            cumplen = sigs.get(promete, 0)
            print(f"\nla extension {exts[0]} promete {promete}: lo cumplen {cumplen}/{total}"
                  f" ({100.0 * cumplen / total:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
