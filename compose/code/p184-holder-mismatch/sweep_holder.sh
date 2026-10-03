#!/bin/bash
# P184 — read the HOLDER of every license file this KB has already measured as present.
#
# Input: ../p170-headref-license-sweep/result.2026-10-03.tsv, which names the slug AND the
# exact filename the license was read at.  No filename guessing is needed here: P170 already
# paid for that, and re-guessing would be the P126 rule-1 error (writing an instrument when
# the repository already versions one).
#
# TSV: slug · verdict · holder · license_family · bytes
IN="${1:-../p170-headref-license-sweep/result.2026-10-03.tsv}"
one() {
  slug=$1; file=$2; fam=$3; bytes=$4
  body=$(curl -s --max-time 25 "https://raw.githubusercontent.com/${slug}/HEAD/${file}" 2>/dev/null)
  if [ -z "$body" ]; then printf '%s\tFETCH-FAILED\t-\t%s\t%s\n' "$slug" "$fam" "$bytes"; return; fi
  out=$(printf "%s" "$body" | python3 extract_holder.py "$slug" "$fam")
  printf '%s\t%s\t%s\n' "$out" "$fam" "$bytes"
}
awk -F'\t' '$2=="LICENSED"{print $1"\t"$3"\t"$5"\t"$4}' "$IN" | while IFS=$'\t' read -r s f fam b; do
  one "$s" "$f" "$fam" "$b" &
  while [ "$(jobs -rp | wc -l)" -ge 6 ]; do wait -n 2>/dev/null || sleep 0.2; done
done
wait
