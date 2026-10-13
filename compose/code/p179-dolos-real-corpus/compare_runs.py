#!/usr/bin/env python3
# `ACTION KW` — p179.  Does template exclusion (`-i`) change the PAIR RANKING?
#
# limb 1 — it materially changes the ranking → the `-i` step in Pattern `1` is load-bearing.
# limb 2 — it does not → the step is cargo cult and the pattern should drop it.
#
# "Materially" is defined BEFORE the numbers are seen, because a threshold chosen afterwards is
# not a falsifier:
#
#   M1  the TOP-5 set changes (membership, not order), OR
#   M2  any known positive moves by >= 2 rank positions, OR
#   M3  the median absolute similarity delta over all 105 pairs is >= 0.02, OR
#   M4  the ranking gap between the worst known positive and the best known negative changes sign
#       (i.e. exclusion fixes, or breaks, the separation a grader relies on).
#
# If none of the four holds, limb 2 fires.
#
# Usage: python3 -I compare_runs.py <noi_pairs.csv> <i_pairs.csv>
import csv, sys, statistics

POSITIVES = {("recommendations.py", "p_rename.py"),
             ("recommendations.py", "p_rename_reorder.py"),
             ("p_rename.py", "p_rename_reorder.py")}


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            left = r["leftFilePath"].rsplit("/", 1)[-1]
            right = r["rightFilePath"].rsplit("/", 1)[-1]
            key = tuple(sorted((left, right)))
            rows.append({"pair": key, "sim": float(r["similarity"]),
                         "overlap": int(r["totalOverlap"]),
                         "longest": int(r["longestFragment"])})
    rows.sort(key=lambda x: -x["sim"])
    return rows


def is_pos(pair):
    return tuple(sorted(pair)) in {tuple(sorted(p)) for p in POSITIVES}


a, b = load(sys.argv[1]), load(sys.argv[2])
rank_a = {r["pair"]: i + 1 for i, r in enumerate(a)}
rank_b = {r["pair"]: i + 1 for i, r in enumerate(b)}
sim_a = {r["pair"]: r["sim"] for r in a}
sim_b = {r["pair"]: r["sim"] for r in b}

print(f"pairs: A={len(a)} B={len(b)}")
print()
print("== TOP 8, run A (no template exclusion) ==")
for i, r in enumerate(a[:8], 1):
    tag = "POSITIVE" if is_pos(r["pair"]) else "negative"
    print(f"{i:>3}. {r['sim']:.4f}  {tag:8}  {r['pair'][0]} <-> {r['pair'][1]}")
print()
print("== TOP 8, run B (-i template.py) ==")
for i, r in enumerate(b[:8], 1):
    tag = "POSITIVE" if is_pos(r["pair"]) else "negative"
    print(f"{i:>3}. {r['sim']:.4f}  {tag:8}  {r['pair'][0]} <-> {r['pair'][1]}")
print()

print("== the known positives, in both runs ==")
for p in sorted({tuple(sorted(x)) for x in POSITIVES}):
    if p in rank_a:
        print(f"  {p[0]} <-> {p[1]}")
        print(f"      A: rank {rank_a[p]:>3}  sim {sim_a[p]:.4f}        "
              f"B: rank {rank_b[p]:>3}  sim {sim_b[p]:.4f}")
print()

# ── the four pre-registered criteria ──────────────────────────────────────────────────────────
top5_a = {r["pair"] for r in a[:5]}
top5_b = {r["pair"] for r in b[:5]}
m1 = top5_a != top5_b

moves = {p: abs(rank_a[p] - rank_b[p]) for p in rank_a if is_pos(p)}
m2 = any(v >= 2 for v in moves.values())

deltas = [abs(sim_a[p] - sim_b[p]) for p in sim_a if p in sim_b]
med = statistics.median(deltas)
m3 = med >= 0.02

def separation(rank, sim):
    pos = [p for p in rank if is_pos(p)]
    neg = [p for p in rank if not is_pos(p)]
    worst_pos = max(rank[p] for p in pos)
    best_neg = min(rank[p] for p in neg)
    return best_neg - worst_pos

sep_a, sep_b = separation(rank_a, sim_a), separation(rank_b, sim_b)
m4 = (sep_a > 0) != (sep_b > 0)

print("== the four pre-registered criteria ==")
print(f"  M1 top-5 membership changes .................. {m1}   A={sorted(top5_a)!s:.0}" )
print(f"       A top5: {sorted(top5_a)}")
print(f"       B top5: {sorted(top5_b)}")
print(f"  M2 a known positive moves >= 2 ranks ......... {m2}   moves={moves}")
print(f"  M3 median |delta sim| >= 0.02 ................ {m3}   median={med:.5f}  max={max(deltas):.5f}")
print(f"  M4 positive/negative separation changes sign .. {m4}   A={sep_a} B={sep_b}")
print()
material = m1 or m2 or m3 or m4
print("VERDICT: LIMB 1 — template exclusion materially changes the ranking; `-i` is LOAD-BEARING"
      if material else
      "VERDICT: LIMB 2 — template exclusion does NOT change the ranking on this corpus; the `-i`\n"
      "         step is cargo cult HERE, and Pattern 1 must say on what corpus it would matter")
print()
print("== detection, which is the question a client actually asks ==")
for p in sorted({tuple(sorted(x)) for x in POSITIVES}):
    if p in sim_a:
        print(f"  {p[0]} <-> {p[1]}: A sim {sim_a[p]:.4f} (rank {rank_a[p]}), "
              f"B sim {sim_b[p]:.4f} (rank {rank_b[p]})")
neg_top = [r for r in a if not is_pos(r["pair"])][:3]
print("  highest-scoring KNOWN NEGATIVES in run A (the false-positive surface):")
for r in neg_top:
    print(f"    {r['sim']:.4f}  {r['pair'][0]} <-> {r['pair'][1]}  (overlap {r['overlap']}, "
          f"longest fragment {r['longest']})")
sys.exit(0)
