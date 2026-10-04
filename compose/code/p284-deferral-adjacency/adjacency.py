#!/usr/bin/env python3
"""`adjacency.py` — una correccion verificada que vive en PROSA no es un control: no viaja.

Pase 95 del 2026-10-04. Existe por un defecto MEDIDO en esta base, no por hipotesis.

El pase 58 (2026-10-03) verifico por TRES canales concordantes que el *Digital Omnibus* corrio
el **Anexo III autonomo** del AI Act de **2026-08-02 a 2027-12-02** (Consejo 2026-06-29, DOUE
2026-07-24, Reglamento (UE) 2026/1744), **y que el articulo 50 NO fue tocado**. La correccion
quedo escrita en `agents/top.md`. 🔴 **Pero no viajo: 13 afirmaciones publicadas siguen atando
el deber de ALTO RIESGO a agosto de 2026**, y una de ellas es la tendencia **#75**, cuya tesis
—«la demanda de conformidad en EMEA esta VENCIDA, no anticipada»— se INVIERTE con el diferimiento.

P284: *cuando una fecha regulatoria se corrige, la correccion hay que MEDIRLA en todas las
afirmaciones que dependen de ella, no escribirla una vez. El control es de ADYACENCIA: toda
afirmacion que ate un deber a la fecha VIEJA tiene que llevar la nueva a la vista.*

Lo que este modulo NO hace: decidir si la frase es correcta. Decide si la afirmacion esta
ACOMPAÑADA. Es un detector de huerfanas, y por eso su contrato es el de `p239`/`region.py`
(detector laxo), no el del validador.
"""
import re

# La fecha VIEJA, en las formas en que esta base la escribe (es y en).
OLD_DATE = re.compile(r'agosto de 2026|2026-08-02|2 de agosto de 2026|August 2,? ?2026', re.I)
# El DEBER que el Omnibus corrio. Sin esto, la fecha sola es correcta: la aplicacion GENERAL
# del Reglamento y el articulo 50 SI rigen desde 2026-08-02.
DUTY = re.compile(r'alto riesgo|high-risk|Anexo III|Annex III', re.I)
# La correccion que tiene que estar a la vista.
DEFERRAL = re.compile(r'2027-12-02|2 de diciembre de 2027|December 2,? ?2027|'
                      r'Omnibus|2026/1744', re.I)
# Eximente: la frase habla EXPLICITAMENTE del articulo 50, que el Omnibus no toco. Ahi la
# fecha vieja es la fecha CORRECTA y exigir el diferimiento seria el error simetrico.
ART50 = re.compile(r'art[ií]culo\s*50|article\s*50|50\(2\)|aiact-50-2|transparencia', re.I)

WINDOW = 6


def scan(lines, window=WINDOW):
    """-> (total, acompañadas, [huerfanas]) sobre una lista de lineas.

    Una afirmacion es la coincidencia, en UNA linea, de la fecha vieja con el deber corrido.
    Esta acompañada si el diferimiento aparece a +-`window` lineas, o si la propia linea se
    declara del articulo 50.
    """
    total = 0
    orphans = []
    for i, line in enumerate(lines):
        if not (OLD_DATE.search(line) and DUTY.search(line)):
            continue
        total += 1
        if ART50.search(line):
            continue
        ctx = "\n".join(lines[max(0, i - window):i + window + 1])
        if not DEFERRAL.search(ctx):
            orphans.append((i + 1, line.strip()))
    return total, total - len(orphans), orphans


def scan_file(path, window=WINDOW):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return scan(fh.read().splitlines(), window)


if __name__ == "__main__":
    import sys
    files = sys.argv[1:]
    T = C = 0
    bad = []
    for f in files:
        t, c, o = scan_file(f)
        T += t
        C += c
        for n, l in o:
            bad.append((f, n, l))
    print("afirmaciones\t%d" % T)
    print("acompanadas\t%d" % C)
    print("huerfanas\t%d" % len(bad))
    for f, n, l in bad:
        print("HUERFANA\t%s:%d\t%s" % (f, n, l[:150]))
    sys.exit(1 if bad else 0)
