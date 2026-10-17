#!/usr/bin/env python3
"""p272 / backlog item 2: run T32's arithmetic check across EVERY numeric market cell
on these shelves, not just the ones a pass happened to look at.

T32 (p271) found the carried North America cell was impossible by multiplying it.
p271 then recorded, as the cheapest audit available: "no pass has ever run that check
systematically, and it needs zero searches."  This is that run.

Calibration is p271's, not invented here:
    <=25%  normal noise in this literature (rounded baselines, CAGRs labelled to a
           different window, mixed report vintages)
    >25%   FLAG
    >50%   INVESTIGATE
    >=2x   STRUCTURAL
Every row's (base, horizon, cagr, years) is transcribed from the shelf cell named in
`cell`, so a reader can re-derive the verdict from the shelf without trusting this file.
"""
ROWS = [
 # label                                  base      horizon   cagr    yrs  cell
 ("global ResourcERA 2026->2030",         10.4,     32.27,    0.312,  4, "market.md:spread"),
 ("global GVR 2025->2030 (superseded)",    8.30,    32.27,    0.312,  5, "market.md:spread"),
 ("global GVR 2026->2033 (CURRENT)",      11.41,    57.2,     0.259,  7, "p272 NEW"),
 ("global GVR 2025->2033 (CURRENT)",       8.30,    57.2,     0.259,  8, "p272 NEW"),
 ("NA Technotrenz 2026->2030",             3.68,    10.80,    0.311,  4, "market.md:22"),
 ("NA GVR 2026->2033 (CURRENT)",           4.254,   19.3883,  0.242,  7, "p272 NEW"),
 ("EMEA ResourcERA 2026->2030",            2.64,     8.00,    0.319,  4, "market.md:23"),
 ("EMEA GVR 2024->2030",                1520.1,   8003.4,     0.319,  6, "p272 NEW"),
 ("EMEA GVR as LABELLED 2025->2030",    1520.1,   8003.4,     0.319,  5, "p272 NEW"),
 ("EMEA GVR 2022->2030 @35.1%",          721.5,   8003.4,     0.351,  8, "p272 NEW"),
 ("LATAM ResourcERA 2026->2030",           0.67,     2.10,    0.335,  4, "market.md:24"),
 ("LATAM GVR 2024->2030",                259.6,   1505.6,     0.324,  6, "market.md:24"),
 ("LATAM M&M 2024->2029",                105.6,    204.7,     0.117,  5, "p272 NEW"),
 ("MEA GVR 2024->2030",                  280.8,   1645.9,     0.326,  6, "market.md:23"),
 ("MEA GVR as LABELLED 2025->2030",      280.8,   1645.9,     0.326,  5, "market.md:23"),
 ("MEA ResourcERA 2026->2030",             0.56,     1.60,    0.343,  4, "trends.md"),
 ("APAC GVR 2025->2033 (as carried)",   2282.9,  18214.1,     0.281,  8, "market.md:147"),
 ("APAC GVR 2026->2033 (window fix)",   3217.5,  18214.1,     0.281,  7, "p272 NEW"),
 ("APAC p271 derived residual 2026",       2.85,     2.921,   0.281,  0, "market.md:25"),
]
def verdict(m):
    a = abs(m)
    if a >= 100: return "STRUCTURAL"
    if a > 50:   return "INVESTIGATE"
    if a > 25:   return "FLAG"
    return "ok"
print("label\tbase\tpub_horizon\tprojected\tmismatch_pct\timplied_cagr_pct\tlabelled_cagr_pct\tverdict\tcell")
for label, base, hz, cagr, yrs, cell in ROWS:
    if yrs == 0:
        m = (hz - base) / base * 100
        print(f"{label}\t{base}\t{hz}\t{hz}\t{m:+.1f}\t-\t-\t{verdict(m)}\t{cell}")
        continue
    proj = base * (1 + cagr) ** yrs
    m = (hz - proj) / proj * 100
    impl = ((hz / base) ** (1 / yrs) - 1) * 100
    print(f"{label}\t{base}\t{hz}\t{proj:.4g}\t{m:+.1f}\t{impl:.1f}\t{cagr*100:.1f}\t{verdict(m)}\t{cell}")
