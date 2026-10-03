#!/usr/bin/env python3
"""El reparto de las 66 filas, afirmado contra `rows.tsv` en vez de compuesto a mano.

Por qué existe: el pase 45 midió bien y escribió *«24 `gen` + 7 `gen-ind` + 1 `gen-cond` = 32
filas, más 1 `pack`»* — o sea **33**. Lo que se rompió fue la PROPAGACIÓN: seis archivos aguas
abajo citaron **«32 de 66 (48 %)»** como respuesta a *«¿pone contenido sintético delante de una
persona?»* y **perdieron la fila `pack`** en cada cita, aunque `rows.tsv` la clasifica como
expuesta (*«es donde el contenido generado se vuelve el curso que el alumno abre»*). Los dos
escáneres de esta capa nunca la perdieron: los dos usan **33** como denominador, y la prosa
*«exactamente la mitad»* era el rastro de la cifra correcta sobreviviendo al lado de la incorrecta.

La lección es de propagación, no de aritmética: **una cifra compuesta a mano se cita mal aguas
abajo**, y por eso esta suite la afirma contra el TSV versionado en vez de repetirla.

    python3 test_exposure.py
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

ok = True
checks = 0
failures = []


def check(label, got, want):
    global ok, checks
    checks += 1
    good = got == want
    ok = ok and good
    if not good:
        failures.append(label)
    print(f"{'PASS' if good else 'FAIL'}  {label}: got={got!r} want={want!r}")


def load(path):
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            out.append(line.rstrip("\n").split("\t"))
    return out


rows = load(os.path.join(HERE, "rows.tsv"))
tally = Counter(r[-1] for r in rows)
EXPOSED = ("gen", "gen-ind", "gen-cond", "pack")
exposed = sum(tally[k] for k in EXPOSED)

check("las filas de agents/top.md clasificadas", len(rows), 66)
check("el reparto, leido del TSV versionado", dict(tally),
      {"gen": 24, "gen-ind": 7, "gen-cond": 1, "pack": 1, "no": 33})

# ---------------------------------------- la correccion del pase 56
print("\nla composicion publicada hasta el pase 55, y por que estaba mal")
check("24 + 7 + 1 (gen + gen-ind + gen-cond) da la cifra publicada 32",
      tally["gen"] + tally["gen-ind"] + tally["gen-cond"], 32)
check("...pero OMITE la fila `pack`, que esta clasificada como expuesta",
      tally["pack"], 1)
check("el conjunto expuesto, con las CUATRO clases que no son `no`", exposed, 33)
check("y 33 es exactamente la mitad de 66, que es lo que la prosa ya decia",
      exposed * 2 == len(rows), True)
check("el complemento cierra: expuestas + no = 66", exposed + tally["no"], 66)
check("el porcentaje correcto es 50, no 48", round(exposed * 100 / len(rows)), 50)

# ------------------------- el control que vuelve la correccion independiente de esta suite
print("\nel control: los dos escaneres de esta capa YA usaban 33 como denominador")
for folder, name in (("aiact-50-2-exposure", "exposure"), ("aiact-50-2-spans", "spans")):
    p = os.path.join(os.path.dirname(HERE), folder, "result.2026-10-02.tsv")
    with open(p, encoding="utf-8") as fh:
        data = [l for i, l in enumerate(fh) if i and l.strip()]
    check(f"{name}: filas de resultado publicadas", len(data), 33)

check("asi que la cifra 32 contradecia a los instrumentos del propio repositorio",
      exposed, 33)

print()
print(f"{checks - len(failures)}/{checks} checks passed")
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
