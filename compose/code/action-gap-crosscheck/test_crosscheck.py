#!/usr/bin/env python3
"""Controls for the action<->gap mirror check (pase 59, action 1 of pase 58).

P126's rule is that the negative control goes BEFORE publishing. Pase 58
mandated a specific one: the suite "has to FAIL on the real pair (action 3 <->
trend 392) of pase 57 and PASS on an unrelated pair".

THAT CONTROL CANNOT BE WRITTEN, and the reason is the first finding of the
action: the pair is not real. Pase 57's action block cites gaps 249, 232 and
100 and makes no date claim. So this file does the next honest thing -- it
asserts the ABSENCE as a control (`test_mandated_fixture_is_not_real`), and
replaces the mandated fixture with the real false positive the corpus does
contain: pase 48's `gap 51`, which a gap-number scan flags and which is
precedent, not a request.

    python3 test_crosscheck.py

NOT RUN AT PUBLICATION. The pase-59 environment denied executing code from the
cloned tree (`[Code from External]`, reproducing pase 58), so these assertions
are written but UNVERIFIED. The column that says so is in the README, and the
standing request is narrow: permission to run the OFFLINE suites of this tree.
"""
import os
import sys
import tempfile

import crosscheck as C

CHECKS = []


def ck(label, got, want):
    ok = got == want
    CHECKS.append(ok)
    print("%s %s%s" % ("PASS" if ok else "FAIL", label,
                       "" if ok else "  -> got %r, want %r" % (got, want)))


def with_text(text, fn):
    fd, path = tempfile.mkstemp(suffix=".md")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(text)
    try:
        return fn(path)
    finally:
        os.unlink(path)


# -- the speech-act classifier, which is the whole instrument ---------------
ck("precedent: 'el metodo que cerro el gap 51' is NOT a request",
   C.classify("sobre el metodo que cerro el gap 51 y rindio dos altas"),
   "PRECEDENT")
ck("request: 'cerrar el gap 249' is a request",
   C.classify("Cerrar el gap 249, que es la unica celda sin determinar"),
   "REQUEST")
ck("request: 'medir ... (gap 232)' is a request",
   C.classify("Medir la superficie de Canvas (gap 232) contra la de Moodle"),
   "REQUEST")
ck("precedent: 'cerrado en el pase 29' is not a request",
   C.classify("como quedo cerrado en el pase 29, el gap 51 ya no aplica"),
   "PRECEDENT")

# -- the real false positive: pase 48 <-> gap 51 ---------------------------
FP = (
    "## Las tres acciones que el pase 48 deja escritas para el pase 49\n"
    "3. Barrer por ORGANIZACION, el metodo que cerro el gap 51 y rindio dos\n"
    "   altas en el pase 34, sobre los laboratorios que ya aparecen.\n"
    "## 52. El gap 51, CERRADO en el pase 29 por la lectura de los dos docs\n"
)
rows = with_text(FP, lambda p: list(C.citations(p)))
ck("the corpus' real false positive is seen at all", len(rows), 1)
ck("...and gap 51 is known to be closed", rows[0]["closed_at"], 29)
ck("...and it is classified PRECEDENT", rows[0]["kind"], "PRECEDENT")
ck("...so it is NOT reported stale (the naive scan's error)",
   rows[0]["stale"], False)

# -- the positive control: the same gap, asked for instead of cited --------
TP = (
    "## Las tres acciones que el pase 48 deja escritas para el pase 49\n"
    "3. Resolver el gap 51, que sigue abierto y hay que medirlo.\n"
    "## 52. El gap 51, CERRADO en el pase 29 por la lectura de los dos docs\n"
)
rows = with_text(TP, lambda p: list(C.citations(p)))
ck("a REQUEST for an already-closed gap IS reported stale",
   rows[0]["stale"], True)
ck("...and names the closing pass", rows[0]["closed_at"], 29)

# -- the unrelated pair that must stay quiet (pase 58's "PASS on" half) ----
FWD = (
    "## Las tres acciones que el pase 42 deja escritas para el pase 43\n"
    "2. Cerrar el gap 90, el validador de SEB Server.\n"
    "## 161. Gap 90, CERRADO con codigo en el pase 43\n"
)
rows = with_text(FWD, lambda p: list(C.citations(p)))
ck("a forward reference (asked at 42, closed at 43) is NOT stale",
   rows[0]["stale"], False)

# -- the mandated fixture, asserted ABSENT --------------------------------
P57 = (
    "## Las tres acciones que el pase 57 deja escritas para el pase 58\n"
    "1. Medir la precondicion de plataforma en las otras tres puertas.\n"
    "2. Cerrar el G1? de mcp-moodle-staff (gap 249).\n"
    "3. Permiso de EGRESO DE RED para compose/code/ (gap 232 / P113).\n"
)
rows = with_text(P57, lambda p: list(C.citations(p)))
gaps = sorted(r["gap"] for r in rows)
ck("test_mandated_fixture_is_not_real: pase 57 cites 232 and 249 only",
   gaps, [232, 249])
ck("...and never gap 56, the 'two dates' question",
   56 in gaps, False)

# -- the ledger reader, both forms ---------------------------------------
LED = (
    "## 158. **Gap 50, CERRADO:** el arbol vive en el cuerpo "
    "(agregado en el pase 43 del 2026-10-02)\n"
    "## Estado de gaps al cierre del pase 39 del 2026-10-02\n"
    "| Gap | Estado | Resolucion |\n"
    "|---|---|---|\n"
    "| **56** (calendario del Anexo III) | CERRADO | dos obligaciones |\n"
)
closures = with_text(LED, C.closed_gaps)
ck("ledger form 1: the numbered heading", closures.get(50), 43)
ck("ledger form 2: the row takes its pass from the HEADER", closures.get(56),
   39)

# -- the block reader must not bleed across headers -----------------------
BLEED = (
    "## Las tres acciones que el pase 10 deja escritas para el pase 11\n"
    "1. Medir el gap 7.\n"
    "## 99. Una tendencia cualquiera que menciona el gap 8\n"
    "y sigue hablando del gap 8 aca abajo.\n"
)
rows = with_text(BLEED, lambda p: list(C.citations(p)))
ck("a trend section after the block is not read as an action",
   sorted(r["gap"] for r in rows), [7])

print("\n%d/%d" % (sum(CHECKS), len(CHECKS)))
sys.exit(0 if all(CHECKS) else 1)
