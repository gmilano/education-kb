# P107 instrument, pase 54: every market triple (start, end, CAGR) must be internally consistent.
# A triple that fails is a defect IN THE SOURCE, catchable without a second source.
def check(label, v0, v1, years, cagr_claimed):
    implied = (v1/v0)**(1/years) - 1
    implied_end = v0*(1+cagr_claimed/100)**years
    ok = abs(implied*100 - cagr_claimed) < 1.0
    print(f"{label}")
    print(f"  claimed: ${v0}B ({2026}) -> ${v1}B ({2026+years}) @ {cagr_claimed}% CAGR")
    print(f"  CAGR implied by the two endpoints : {implied*100:5.1f}%")
    print(f"  endpoint implied by the CAGR      : ${implied_end:4.2f}B")
    print(f"  VERDICT: {'CONSISTENT' if ok else 'INCONSISTENT — the three numbers cannot all be true'}\n")
    return ok

print("=== Pase 54 — control de consistencia de ternas de mercado (fuente: azumo/alicelabs, EMEA sweep) ===\n")
a=check("Europe, AI in education", 2.64, 8.0, 4, 31.9)
b=check("Middle East & Africa, AI in education", 0.56, 1.6, 4, 34.3)
print(f"RESULT: {int(a)+int(b)} of 2 triples consistent. Same sentence, same source, same format.")
