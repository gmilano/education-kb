#!/usr/bin/env python3
"""p274 — T32 v3: apply p272's OWN second duty to p272's OWN ledger.

p272 wrote the amendment ("a 10% mismatch is not automatically noise -- test the
window before writing it off") in the same pass whose 19-cell ledger marked three
mismatches of +7.7%, +7.8% and +11.5% `ok`, and -12.2% `ok`, without running the
window test on any of them.

This script runs the test the amendment describes, on every market cell this base
publishes, and classifies each one:

  PASS        |mismatch| <= 1.0%  as the publisher labels the window
  WINDOW_FIX  closes to <= 1.0% when the span is read one year LONGER or SHORTER
              -> one of the two year labels on the row is wrong
  SPLICE      closes at neither -> the endpoints are two report vintages, not one
              growth curve, and must never be published as a series

No network. No searches. Arithmetic only.
"""
import sys

# label, base, base_year, horizon, horizon_year, cagr_pct, where, p272_verdict
CELLS = [
    # --- global ---
    ("global ResourcERA 2026->2030", 10.4, 2026, 32.27, 2030, 31.2, "market.md:spread", "ok"),
    ("global GVR superseded 2025->2030", 8.3, 2025, 32.27, 2030, 31.2, "market.md:spread", "ok"),
    ("global GVR CURRENT 2026->2033", 11.4, 2026, 57.2, 2033, 25.9, "market.md:headline", "ok"),
    ("global GVR CURRENT 2025->2033", 8.3, 2025, 57.2, 2033, 25.9, "market.md:headline", "ok"),
    ("global GVR CURRENT 2025->2026 (both printed figures)", 8.3, 2025, 11.4, 2026, 25.9, "market.md:headline", "NOT SWEPT"),
    ("global TBRC 2026->2030", 10.6, 2026, 42.48, 2030, 41.5, "market.md:spread", "PASS p273"),
    ("global TBRC 2025->2026 (own 40.9%)", 7.52, 2025, 10.6, 2026, 40.9, "market.md:spread", "derived p273"),
    ("global Precedence 2026->2035", 9.58, 2026, 136.79, 2035, 34.52, "market.md:spread", "PASS p273"),
    ("global MarkWide 2026->2035", 8.7, 2026, 100.21, 2035, 31.20, "market.md:spread", "PASS p273"),
    # --- North America ---
    ("NA Technotrenz 2026->2030", 3.68, 2026, 10.8, 2030, 31.1, "market.md:headline", "ok"),
    ("NA GVR CURRENT 2026->2033", 4.254, 2026, 19.3883, 2033, 24.2, "market.md:headline", "ok"),
    ("NA GVR as printed 2025->2033", 3.1138, 2025, 19.3883, 2033, 24.2, "market.md:p271-table", "NOT SWEPT"),
    ("NA M&M 2024->2029", 0.951, 2024, 2.3, 2029, 15.9, "market.md:p271-table", "NOT SWEPT"),
    # --- EMEA / Europe ---
    ("EMEA ResourcERA 2026->2030", 2.64, 2026, 8.0, 2030, 31.9, "market.md:headline", "ok"),
    ("EMEA GVR 2024->2030", 1.5201, 2024, 8.0034, 2030, 31.9, "market.md:p272", "ok"),
    ("EMEA GVR as LABELLED 2025->2030", 1.5201, 2025, 8.0034, 2030, 31.9, "market.md:p272", "FLAG"),
    ("EMEA MarketDataForecast 2025->2034", 1.59, 2025, 20.0, 2034, 32.47, "market.md:p270-table", "NOT SWEPT"),
    ("EMEA MarketDataForecast 2025->2026", 1.59, 2025, 2.11, 2026, 32.47, "market.md:p270-table", "NOT SWEPT"),
    # --- MEA ---
    ("MEA GVR 2024->2030", 0.2808, 2024, 1.6459, 2030, 32.6, "market.md:headline", "ok"),
    ("MEA GVR as LABELLED 2025->2030", 0.2808, 2025, 1.6459, 2030, 32.6, "market.md:headline", "FLAG"),
    ("MEA ResourcERA 2026->2030", 0.56, 2026, 1.6, 2030, 34.3, "trends.md", "ok"),
    ("MEA GVR AI-tutors 2025->2033", 0.1885, 2025, 1.7368, 2033, 32.0, "market.md:p271-table", "NOT SWEPT"),
    ("MEA Transpire AI-tutors 2025->2033", 0.1864, 2025, 1.73002, 2033, 32.13, "market.md:p271-table", "NOT SWEPT"),
    # --- LATAM ---
    ("LATAM ResourcERA 2026->2030", 0.67, 2026, 2.1, 2030, 33.5, "market.md:headline", "ok"),
    ("LATAM GVR 2024->2030", 0.2596, 2024, 1.5056, 2030, 32.4, "market.md:headline", "ok"),
    ("LATAM M&M 2024->2029", 0.1056, 2024, 0.2047, 2029, 11.7, "market.md:headline", "ok"),
    # --- APAC ---
    ("APAC GVR as carried 2025->2033", 2.2829, 2025, 18.2141, 2033, 28.1, "market.md:p272", "ok"),
    ("APAC GVR window fix 2026->2033", 3.2175, 2026, 18.2141, 2033, 28.1, "market.md:headline", "ok"),
]

TOL = 1.0          # closes
ROUND_TOL = 2.0    # publishers print baselines to 2-3 significant figures


def project(base, cagr_pct, years):
    return base * (1.0 + cagr_pct / 100.0) ** years


def mismatch_pct(projected, horizon):
    return (projected - horizon) / horizon * 100.0


def classify(base, base_year, horizon, horizon_year, cagr):
    """PASS / ROUNDING / WINDOW_FIX / SPLICE for one cell."""
    span = horizon_year - base_year
    as_labelled = mismatch_pct(project(base, cagr, span), horizon)
    if abs(as_labelled) <= TOL:
        return "PASS", as_labelled, span, None
    for alt in (span + 1, span - 1):
        if alt < 1:
            continue
        m = mismatch_pct(project(base, cagr, alt), horizon)
        if abs(m) <= TOL:
            return "WINDOW_FIX", as_labelled, alt, m
    if abs(as_labelled) <= ROUND_TOL:
        return "ROUNDING", as_labelled, span, None
    return "SPLICE", as_labelled, span, None


def derived_2026(base, base_year, horizon, horizon_year, cagr):
    """The 2026 point read FORWARD from the printed base vs BACKWARD from the
    horizon.  p272's standing instruction says to prefer the second.  Where the
    two disagree, a published '2026' figure is not one number."""
    fwd = project(base, cagr, 2026 - base_year)
    bwd = horizon / (1.0 + cagr / 100.0) ** (horizon_year - 2026)
    return fwd, bwd, (fwd - bwd) / bwd * 100.0


def implied_cagr(base, horizon, span):
    if span <= 0 or base <= 0:
        return float("nan")
    return ((horizon / base) ** (1.0 / span) - 1.0) * 100.0


def rows():
    for label, base, by, hor, hy, cagr, where, prior in CELLS:
        verdict, as_lab, span, fixed = classify(base, by, hor, hy, cagr)
        fwd, bwd, split = derived_2026(base, by, hor, hy, cagr)
        yield {
            "p2026_from_base": round(fwd, 4),
            "p2026_from_horizon": round(bwd, 4),
            "p2026_split_pct": round(split, 2),
            "cell": label,
            "base": base,
            "horizon": hor,
            "labelled_span_y": hy - by,
            "labelled_cagr_pct": cagr,
            "implied_cagr_pct": round(implied_cagr(base, hor, hy - by), 2),
            "mismatch_as_labelled_pct": round(as_lab, 2),
            "closing_span_y": span if verdict == "WINDOW_FIX" else (hy - by),
            "mismatch_after_fix_pct": ("" if fixed is None else round(fixed, 2)),
            "verdict": verdict,
            "p272_or_p273_verdict": prior,
            "where": where,
        }


FIELDS = ["cell", "base", "horizon", "labelled_span_y", "labelled_cagr_pct",
          "implied_cagr_pct", "mismatch_as_labelled_pct", "closing_span_y",
          "mismatch_after_fix_pct", "p2026_from_base", "p2026_from_horizon",
          "p2026_split_pct", "verdict", "p272_or_p273_verdict", "where"]


def main():
    out = sys.stdout
    out.write("# p274 — T32 v3 window sweep. PASS <=1.0% as labelled · "
              "ROUNDING <=2.0% · WINDOW_FIX closes at span+/-1y · SPLICE closes at neither.\n")
    out.write("# SIGN CONVENTION: mismatch = projected/published_horizon - 1.  p272's ledger "
              "used published/projected - 1, so the SAME cell reads -10.3 here and +11.5 there. "
              "Two conventions is one reason a '10% threshold' was never comparable across cells.\n")
    out.write("# p2026_* : the 2026 point read forward from the printed base vs backward from "
              "the horizon.  A non-zero split means a published '2026 market size' is not one number.\n")
    out.write("\t".join(FIELDS) + "\n")
    tally = {}
    for r in rows():
        out.write("\t".join(str(r[f]) for f in FIELDS) + "\n")
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    out.write("# tally: " + " · ".join(f"{k}={v}" for k, v in sorted(tally.items())) + "\n")


if __name__ == "__main__":
    main()
