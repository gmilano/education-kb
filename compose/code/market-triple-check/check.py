# P107 instrument, pase 54: every market triple (start, end, CAGR) must be internally consistent.
# A triple that fails is a defect IN THE SOURCE, catchable without a second source.
# Pase 56: the base year is now an argument. It used to be hardcoded to 2026, which printed the
# wrong years for any triple not based in 2026 -- the per-geography triples below are 2024-based.
def check(label, v0, v1, years, cagr_claimed, y0=2026):
    implied = (v1 / v0) ** (1 / years) - 1
    implied_end = v0 * (1 + cagr_claimed / 100) ** years
    ok = abs(implied * 100 - cagr_claimed) < 1.0
    print(f"{label}")
    print(f"  claimed: ${v0}B ({y0}) -> ${v1}B ({y0 + years}) @ {cagr_claimed}% CAGR")
    print(f"  CAGR implied by the two endpoints : {implied * 100:5.1f}%")
    print(f"  endpoint implied by the CAGR      : ${implied_end:4.2f}B")
    print(f"  VERDICT: {'CONSISTENT' if ok else 'INCONSISTENT — the three numbers cannot all be true'}\n")
    return ok


print("=== Pase 54 — control de consistencia de ternas de mercado (fuente: azumo/alicelabs, EMEA sweep) ===\n")
a = check("Europe, AI in education", 2.64, 8.0, 4, 31.9)
b = check("Middle East & Africa, AI in education", 0.56, 1.6, 4, 34.3)
print(f"RESULT: {int(a) + int(b)} of 2 triples consistent. Same sentence, same source, same format.\n")

print("=== Pase 56 — las ternas POR GEOGRAFÍA del mismo proveedor, y la global del barrido ===\n")
# Both per-geography triples come from the same vendor's geography pages (marketsandmarkets).
na = check("North America, AI in education (reconfirmada del pase 55)", 0.951, 2.3032, 5, 15.9, y0=2024)
ap = check("Asia Pacific, AI in education (NUEVA en este pase)", 0.5916, 1.8481, 5, 20.9, y0=2024)
gl = check("Global, AI in education (barrido global de este pase)", 7.52, 10.6, 1, 40.9, y0=2025)

print(f"RESULT: {int(na) + int(ap) + int(gl)} of 3 triples consistent.")
print("  Las DOS ternas por geografía del mismo proveedor fallan, y fallan en el MISMO sentido:")
print("  el CAGR declarado es MENOR que el que exigen sus propios extremos.")
print("  La terna GLOBAL del barrido, de otra fuente, cierra.")
