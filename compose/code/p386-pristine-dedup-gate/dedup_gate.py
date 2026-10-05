#!/usr/bin/env python3
"""P386 — compuerta de procedencia: un fingerprint de licencia PRISTINA no transporta linaje.

El pase 117 (`P379`) propuso deduplicar filas por el par (sha256 de LICENSE, titular).
Este pase midio que ese par FUNDE proyectos ajenos cuando la licencia es boilerplate
prístino: el `LICENSE` de Apache-2.0 son 11.357 B fijos que NO llevan titular adentro,
asi que el par se vuelve (constante, constante).

Regla: si el titular esta AUSENTE, el fingerprint vale 0 bits de procedencia y el
deduplicador se ABSTIENE. Si el titular esta PRESENTE, el par si transporta linaje.
"""
import sys

# Boilerplates prístinos conocidos: (bytes) -> nombre. El titular no vive en el texto.
PRISTINE_SIZES = {
    11357: "Apache-2.0",
    35187: "GPL-3.0",
    18092: "GPL-2.0",
    7651: "MPL-2.0",
}
ABSENT = {"", None, "NOT-APPLICABLE", "NOT_APPLICABLE", "ausente", "HOLDER-ABSENT"}


def holder_absent(holder):
    return holder is None or str(holder).strip() in ABSENT


def is_pristine(size_bytes, holder):
    """Prístino = tamaño de boilerplate conocido Y titular ausente del texto."""
    return size_bytes in PRISTINE_SIZES and holder_absent(holder)


def dedup_key(row):
    """Clave de deduplicacion, o None si hay que ABSTENERSE.

    row = {'repo':..., 'sha256':..., 'bytes':..., 'holder':...}
    """
    if is_pristine(row.get("bytes"), row.get("holder")) or holder_absent(row.get("holder")):
        return None  # 0 bits de procedencia -> abstenerse
    return (row["sha256"], str(row["holder"]).strip())


def group(rows):
    """Agrupa por clave. Devuelve (clusters, abstained).

    clusters: {clave: [repos]} -- linaje real
    abstained: [repos] -- cada uno queda SOLO, nunca fundido
    """
    clusters, abstained = {}, []
    for r in rows:
        k = dedup_key(r)
        if k is None:
            abstained.append(r["repo"])
        else:
            clusters.setdefault(k, []).append(r["repo"])
    return clusters, abstained


def main(argv):
    import json
    rows = json.load(open(argv[0], encoding="utf-8")) if argv else []
    clusters, abstained = group(rows)
    print("clave\trepos")
    for k, v in sorted(clusters.items()):
        print(f"{k[0]}|{k[1]}\t{','.join(sorted(v))}")
    print("#\tabstenidos\t" + ",".join(sorted(abstained)))
    print(f"#\tclusters\t{len(clusters)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
