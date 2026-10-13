#!/usr/bin/env bash
# `ACTION LB` — p181.  Does `dolos`'s `-i` (template exclusion) effect depend on the
# TEMPLATE-TO-SUBMISSION RATIO?
#
# p179 discharged `ACTION KW` and fired limb 2: on a 10-line template over a 304-line mean
# submission (ratio 0.033), template exclusion changed nothing material — median |Δsim| 0.00064
# over 105 pairs.  Pattern 1 was amended to make the `-i` step CONDITIONAL on a scaffolded
# assignment, on the REASONING that a bigger handout would matter.  That reasoning was never
# measured.  `ACTION LB` measures it.
#
#   limb 1 — the effect rises with the ratio and crosses 0.02 → `T284` holds and Pattern 1's
#            condition is right: tell the client to supply the template when the handout is big.
#   limb 2 — flat at every ratio → `-i` is cargo cult at ALL ratios and Pattern 1 must DROP the
#            step, not merely condition it.
#
# The ladder is built from the corpus itself at every rung, never from an invented header, so
# each template is boilerplate the course plausibly handed out.
#
# Usage: bash lb_ratio_sweep.sh <corpus_dir> <out_dir>
set -u
CORPUS="${1:-}"; OUT="${2:-}"
[ -d "$CORPUS" ] || { echo "p181/LB: REFUSED — '$CORPUS' is not a directory" >&2; exit 2; }
[ -n "$OUT" ] || { echo "p181/LB: REFUSED — no output directory" >&2; exit 2; }
mkdir -p "$OUT/templates" "$OUT/runs"

NFILES=$(ls "$CORPUS"/*.py | wc -l | tr -d ' ')
TOTLINES=$(cat "$CORPUS"/*.py | wc -l | tr -d ' ')
MEAN=$((TOTLINES / NFILES))
echo "corpus: $NFILES files, $TOTLINES lines, mean submission $MEAN lines"

# ── the template ladder, each rung built FROM the corpus ──────────────────────────────────────
# rungs 1-3: import/from lines shared by >= N modules (relaxing N grows the template)
for n in 6 3 2; do
  awk '/^(import |from )/ {print}' "$CORPUS"/*.py | sort | uniq -c \
    | awk -v n="$n" '$1 >= n {$1=""; sub(/^ /,""); print}' > "$OUT/templates/imports_ge$n.py"
done
# rung 4: ANY line (not just imports) shared by >= 3 modules — real body boilerplate
awk '{print}' "$CORPUS"/*.py | sed 's/[[:space:]]*$//' | grep -v '^$' | sort | uniq -c \
  | awk '$1 >= 3 {$1=""; sub(/^ /,""); print}' > "$OUT/templates/anyline_ge3.py"
# rung 5: ANY line shared by >= 2 modules
awk '{print}' "$CORPUS"/*.py | sed 's/[[:space:]]*$//' | grep -v '^$' | sort | uniq -c \
  | awk '$1 >= 2 {$1=""; sub(/^ /,""); print}' > "$OUT/templates/anyline_ge2.py"
# rung 6: one whole real module as the handout — the scaffolded-assignment case
cat "$CORPUS/database.py" > "$OUT/templates/handout_1mod.py"
# rung 7: three whole real modules as the handout
cat "$CORPUS/database.py" "$CORPUS/config.py" "$CORPUS/models.py" > "$OUT/templates/handout_3mod.py"

# ── baseline: no exclusion ────────────────────────────────────────────────────────────────────
npx --no-install dolos run -l python -f csv -o "$OUT/runs/base" "$CORPUS"/*.py >/dev/null 2>&1
BASE="$OUT/runs/base/pairs.csv"
[ -f "$BASE" ] || { echo "p181/LB: REFUSED — baseline produced no pairs.csv" >&2; exit 3; }

printf '%s\t%s\t%s\t%s\n' rung template_lines ratio outdir > "$OUT/ladder.tsv"
for t in "$OUT"/templates/*.py; do
  rung=$(basename "$t" .py)
  tl=$(grep -cv '^$' "$t" | tr -d ' ')
  ratio=$(awk -v a="$tl" -v b="$MEAN" 'BEGIN{printf "%.4f", a/b}')
  d="$OUT/runs/$rung"
  npx --no-install dolos run -l python -f csv -o "$d" -i "$t" "$CORPUS"/*.py >/dev/null 2>&1
  if [ -f "$d/pairs.csv" ]; then
    printf '%s\t%s\t%s\t%s\n' "$rung" "$tl" "$ratio" "$d" >> "$OUT/ladder.tsv"
    echo "  ran $rung: $tl template lines, ratio $ratio"
  else
    printf '%s\t%s\t%s\t%s\n' "$rung" "$tl" "$ratio" "FAILED" >> "$OUT/ladder.tsv"
    echo "  FAILED $rung ($tl lines) — dolos produced no pairs.csv"
  fi
done
echo "baseline=$BASE"
