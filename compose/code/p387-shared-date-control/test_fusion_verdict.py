#!/usr/bin/env python3
"""Suite de P387. El caso 1 es el control negativo REAL del pase 118."""
import fusion_verdict as f

ok = fail = 0


def t(name, cond):
    global ok, fail
    if cond:
        ok += 1; print(f"PASS {name}")
    else:
        fail += 1; print(f"FAIL {name}")


KOREA = {"name": "Framework Act", "issuer": "KR", "date": "2026-01-22", "verified": True}
SG = {"name": "Model AI Governance Framework for Agentic AI", "issuer": "IMDA-SG",
      "date": "2026-01-22", "verified": True}

t("CONTROL NEGATIVO: Corea y Singapur comparten fecha y NO son fusion",
  f.verdict(KOREA, SG) == f.DISTINCT)

# El caso que P381 si debe cazar: mismo emisor, nombres cruzados, misma fecha.
A = {"name": "instrumento A", "issuer": "X", "date": "2024-08-29", "verified": True}
B = {"name": "instrumento B", "issuer": "X", "date": "2024-08-29", "verified": True}
t("mismo emisor + nombres distintos + misma fecha => FUSION", f.verdict(A, B) == f.FUSION)

# Mismo emisor, fechas distintas: dos instrumentos reales.
B2 = dict(B, date="2024-06-03")
t("mismo emisor con fechas distintas => instrumentos distintos", f.verdict(A, B2) == f.DISTINCT)

# Sin verificacion por instrumento no se puede afirmar fusion.
t("sin verificar no se afirma fusion", f.verdict(dict(A, verified=False), B) == f.UNVERIFIABLE)
t("sin verificar NINGUNO tampoco", f.verdict(dict(A, verified=False), dict(B, verified=False)) == f.UNVERIFIABLE)

# El mismo instrumento citado dos veces no es un par.
t("el mismo instrumento dos veces no es fusion", f.verdict(A, dict(A)) == f.DISTINCT)

# La fecha compartida nunca basta por si sola: emisores distintos ganan.
t("emisores distintos ganan sobre la fecha compartida",
  f.verdict(dict(A, issuer="Y"), B) == f.DISTINCT)

print(f"\n{ok}/{ok+fail} checks passed")
raise SystemExit(1 if fail else 0)
