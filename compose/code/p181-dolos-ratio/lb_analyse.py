#!/usr/bin/env python3
# `ACTION LB` — p181.  Is `dolos`'s template-exclusion effect a function of the
# template-to-submission ratio?
#
# The limb names ONE statistic, fixed at p180 before any number was seen:
#   limb 1 — the effect RISES with the ratio and CROSSES 0.02 (median |Δsim| over all pairs)
#   limb 2 — flat at every ratio → `-i` is cargo cult and Pattern 1 must DROP the step
#
# Reported alongside it, because a median over 105 pairs can hide the thing a grader relies on:
#   * the known-positive similarity (the transform a student actually performs)
#   * the best honest negative (sibling code, same framework/ORM/author)
#   * the SEPARATION between them, which is what a threshold sits in
#
# Usage: python3 -I lb_analyse.py <ladder.tsv> <baseline_pairs.csv>
import csv, statistics, sys

POSITIVES = {("p_rename.py", "recommendations.py"),
             ("p_rename_reorder.py", "recommendations.py"),
             ("p_rename.py", "p_rename_reorder.py")}


def load(path):
    sims = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            left = r["leftFilePath"].rsplit("/", 1)[-1]
            right = r["rightFilePath"].rsplit("/", 1)[-1]
            sims[tuple(sorted((left, right)))] = float(r["similarity"])
    return sims


def split(sims):
    pos = {k: v for k, v in sims.items() if k in POSITIVES}
    neg = {k: v for k, v in sims.items() if k not in POSITIVES}
    return pos, neg


ladder_path, base_path = sys.argv[1], sys.argv[2]
base = load(base_path)
bpos, bneg = split(base)

rows = []
with open(ladder_path, newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        if r["outdir"] == "FAILED":
            continue
        sims = load(r["outdir"] + "/pairs.csv")
        shared = set(base) & set(sims)
        deltas = [abs(sims[k] - base[k]) for k in shared]
        pos, neg = split(sims)
        rows.append({
            "rung": r["rung"],
            "lines": int(r["template_lines"]),
            "ratio": float(r["ratio"]),
            "pairs": len(sims),
            "lost": len(set(base) - set(sims)),
            "median_abs_delta": statistics.median(deltas) if deltas else float("nan"),
            "max_abs_delta": max(deltas) if deltas else float("nan"),
            "worst_pos": min(pos.values()) if pos else float("nan"),
            "best_neg": max(neg.values()) if neg else float("nan"),
        })

rows.sort(key=lambda x: x["ratio"])

b_worst_pos = min(bpos.values())
b_best_neg = max(bneg.values())
print("BASELINE (no -i): pairs=%d  worst_positive=%.4f  best_honest_negative=%.4f  separation=%+.4f"
      % (len(base), b_worst_pos, b_best_neg, b_worst_pos - b_best_neg))
print()
hdr = ("%-14s %6s %7s %6s %5s %10s %10s %10s %10s %11s"
       % ("rung", "lines", "ratio", "pairs", "lost", "med|Δ|", "max|Δ|", "worstPos", "bestNeg", "separation"))
print(hdr)
print("-" * len(hdr))
for r in rows:
    print("%-14s %6d %7.4f %6d %5d %10.5f %10.5f %10.4f %10.4f %+11.4f"
          % (r["rung"], r["lines"], r["ratio"], r["pairs"], r["lost"],
             r["median_abs_delta"], r["max_abs_delta"], r["worst_pos"], r["best_neg"],
             r["worst_pos"] - r["best_neg"]))

print()
crossed = [r for r in rows if r["median_abs_delta"] >= 0.02]
med_at_max = max(rows, key=lambda x: x["ratio"])
print("LIMB TEST — threshold 0.02 on median |Δsim|, fixed at p180:")
print("  ratios measured: %.4f .. %.4f  (%dx span)"
      % (rows[0]["ratio"], rows[-1]["ratio"], round(rows[-1]["ratio"] / max(rows[0]["ratio"], 1e-9))))
print("  rungs crossing 0.02: %d of %d" % (len(crossed), len(rows)))
if crossed:
    print("  first crossing at ratio %.4f (%s, %d lines, median |Δ| %.5f)"
          % (crossed[0]["ratio"], crossed[0]["rung"], crossed[0]["lines"],
             crossed[0]["median_abs_delta"]))
    print("  VERDICT: LIMB 1 — the effect is ratio-dependent and crosses the threshold.")
else:
    print("  highest median |Δ| anywhere on the ladder: %.5f (at ratio %.4f, %d template lines)"
          % (max(r["median_abs_delta"] for r in rows), med_at_max["ratio"], med_at_max["lines"]))
    print("  VERDICT: LIMB 2 — flat at every ratio, including a template LARGER than the mean")
    print("           submission. `-i` does not move the median at any handout size here.")

# the separation is what a grader's threshold actually sits in
sep_moves = [(r["rung"], (r["worst_pos"] - r["best_neg"]) - (b_worst_pos - b_best_neg)) for r in rows]
worst_move = max(sep_moves, key=lambda x: abs(x[1]))
print()
print("  separation vs baseline: largest move %+.4f (%s)" % (worst_move[1], worst_move[0]))
print("  sign change anywhere: %s"
      % ("YES" if any((r["worst_pos"] - r["best_neg"]) * (b_worst_pos - b_best_neg) < 0 for r in rows)
         else "NO"))
