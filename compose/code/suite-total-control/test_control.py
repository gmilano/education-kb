#!/usr/bin/env python3
"""P126's rule, made executable.

El pase 55 contó a mano las aserciones de dos suites, y el instrumento casero dio un falso
positivo (tendencia 313). El control positivo que lo habilitó sólo ejercitó suites que emiten
`PASS`, así que nunca tocó el caso donde el instrumento falla: una suite con OTRO vocabulario.

Esta suite es ese control, y su afirmación central es NEGATIVA: el contador por vocabulario
acierta en el fixture A y se equivoca en el fixture B, mientras el lector del total propio
acierta en los dos. Correrla sobre A solamente —lo que hizo el pase 55— la deja pasar roto.

    python3 test_control.py              # fixtures solamente (offline, sin red)
    python3 test_control.py --inventory  # + qué invocaciones de este repo exponen total propio
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)

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


# --------------------------------------------------------------- los dos instrumentos
def naive_count(text):
    """El instrumento casero: cuenta líneas que empiezan con PASS.

    Es el que P126 prohíbe escribir sin correr antes el que este repositorio ya versiona.
    """
    return len([l for l in text.splitlines() if l.startswith("PASS")])


TOTAL_PATTERNS = (
    re.compile(r"^(\d+)/(\d+) checks passed$"),      # sebserver, npm, trend, unitime, openedx
    re.compile(r"^(\d+)/(\d+) controles pasados$"),  # registry-license-remeasure (castellano)
    re.compile(r"^(\d+) checks run$"),               # mcp-allowlist-gateway
    re.compile(r"^(\d+) de (\d+)$"),                 # los scan_*.sh
)


def self_total(text):
    """El lector del total PROPIO: el número que la suite publica sobre sí misma.

    No sabe nada del vocabulario de las líneas de aserción, que es justamente el punto.
    """
    for line in reversed(text.splitlines()):
        line = line.strip()
        for pat in TOTAL_PATTERNS:
            m = pat.match(line)
            if m:
                return int(m.group(1))
    return None


def run(script):
    p = subprocess.run(["sh", os.path.join(HERE, "fixtures", script)],
                       capture_output=True, text=True, timeout=60)
    return p.stdout


a = run("emits_pass.sh")
b = run("emits_ok.sh")

# ------------------------------------------------- 1. el control POSITIVO, que es el que engaña
print("1. el control positivo del pase 55: el fixture que emite PASS")
check("naive acierta sobre el vocabulario que SI ejercito", naive_count(a), 3)
check("self_total acierta sobre el mismo fixture", self_total(a), 3)
check("los dos coinciden, asi que el control positivo no distingue",
      naive_count(a) == self_total(a), True)

# ------------------------------------------- 2. el control NEGATIVO, que es el que faltaba
print("\n2. el caso que el control del pase 55 NO ejercito: otro vocabulario")
check("la suite B declara 4 aserciones en su total propio", self_total(b), 4)
check("el instrumento casero cuenta 0 sobre la misma suite", naive_count(b), 0)
check("y por eso se EQUIVOCA, que es el hallazgo de P126",
      naive_count(b) != self_total(b), True)
check("el error no es de redondeo: pierde las 4", self_total(b) - naive_count(b), 4)

# --------------------------------- 3. por que el control positivo no alcanzaba (la regla)
print("\n3. la regla de P126, dicha como aserto")
only_positive_passes = naive_count(a) == self_total(a)
check("un control que corra SOLO el fixture A deja pasar el instrumento roto",
      only_positive_passes, True)
check("hace falta el fixture B para que el control tenga poder",
      naive_count(b) != self_total(b), True)
check("los dos fixtures usan vocabularios DISJUNTOS en sus lineas de asercion",
      bool({l.split()[0] for l in a.splitlines() if l.strip()} &
           {l.split()[0] for l in b.splitlines() if l.strip()} - {"ALL", ""}), False)

# ----------------------------------------------------- 4. inventario real, opcional
if "--inventory" in sys.argv:
    print("\n4. inventario: que invocaciones de compose/code/ publican un total propio")
    INVOCATIONS = [
        ("aiact-50-2-pack", ["python3", "test_pack.py"]),
        ("aiact-50-2-marking", ["python3", "test_marking.py"]),
        ("sebserver-mcp-gate", ["python3", "test_gate.py"]),
        ("unitime-mcp-gate", ["python3", "test_gate.py"]),
        ("openedx-course-generator", ["python3", "test_plan.py"]),
        ("proctoring-reach-audit", ["python3", "test_reach.py"]),
        ("seb-proctoring-validator", ["sh", "run_test.sh"]),
        ("registry-license-remeasure", ["python3", "test_anchor.py"]),
        ("npm-surface-probe", ["python3", "test_probe.py"]),
        ("mcp-allowlist-gateway", ["python3", "test_gateway.py"]),
        ("trend-backlink-audit", ["python3", "test_trends.py"]),
        ("aiact-50-2-spans", ["sh", "scan_spans.sh"]),
        ("aiact-50-2-exposure", ["sh", "scan_marking.sh"]),
    ]
    with_total, without_total = [], []
    for folder, cmd in INVOCATIONS:
        d = os.path.join(CODE, folder)
        try:
            p = subprocess.run(cmd, cwd=d, capture_output=True, text=True, timeout=180)
            t = self_total(p.stdout)
        except Exception as e:  # noqa: BLE001
            t = None
            print(f"      {folder}: no se pudo correr ({type(e).__name__})")
        (with_total if t is not None else without_total).append((folder, t))
    for folder, t in with_total:
        print(f"  total propio  {folder}: {t}")
    for folder, _ in without_total:
        print(f"  SIN total     {folder}")
    check("las dos suites del pase 56 ya publican su total",
          sorted(f for f, _ in with_total if f in
                 {"unitime-mcp-gate", "openedx-course-generator"}),
          ["openedx-course-generator", "unitime-mcp-gate"])
    print(f"\n  {len(with_total)} de {len(INVOCATIONS)} invocaciones publican un total propio")
    print("  ⚠️  las que no, se declaran: " +
          (", ".join(f for f, _ in without_total) or "ninguna"))

print()
print(f"{checks - len(failures)}/{checks} checks passed")
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
