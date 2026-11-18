#!/usr/bin/env bash
# `899-G2` — measure the rebuilt ledger via batched `gh api search/repositories`.
# p899 measured the top 40 of a 601-row stale ledger. This measures the top N of the
# REBUILT ledger: existence, stars, SPDX licence, last push. Existence is the point —
# a row that returns nothing is an address this KB has been logging at something that
# is not there.
set -uo pipefail
LEDGER="${1:?ledger tsv}"
N="${2:-300}"
OUT="${3:?out tsv}"
printf 'address\tfiles_logging\texists\tstars\tspdx\tpushed\n' > "$OUT"

mapfile -t ROWS < <(tail -n +2 "$LEDGER" | head -n "$N" | cut -f2,3)

batch=""; count=0; declare -A LOGGED=()
flush() {
  [ -z "$batch" ] && return 0
  gh api -X GET search/repositories -f q="$batch" -f per_page=100 \
     --jq '.items[]|[(.full_name|ascii_downcase),.stargazers_count,(.license.spdx_id//"NONE"),(.pushed_at|split("T")[0])]|@tsv' \
     2>/dev/null >> /tmp/claude-0/hits.tsv
  batch=""; count=0; sleep 2
}
: > /tmp/claude-0/hits.tsv
for r in "${ROWS[@]}"; do
  a="${r%%$'\t'*}"; n="${r##*$'\t'}"; LOGGED["$a"]="$n"
  cand="$batch repo:$a"
  if [ ${#cand} -gt 230 ]; then flush; cand=" repo:$a"; fi
  batch="$cand"; count=$((count+1))
done
flush

declare -A S=() L=() P=()
while IFS=$'\t' read -r fn st sp pu; do S["$fn"]=$st; L["$fn"]=$sp; P["$fn"]=$pu; done < /tmp/claude-0/hits.tsv
for a in "${!LOGGED[@]}"; do
  if [ -n "${S[$a]+x}" ]; then
    printf '%s\t%s\tYES\t%s\t%s\t%s\n' "$a" "${LOGGED[$a]}" "${S[$a]}" "${L[$a]}" "${P[$a]}"
  else
    printf '%s\t%s\tNO\t-\t-\t-\n' "$a" "${LOGGED[$a]}"
  fi
done | sort -t$'\t' -k2,2nr -k4,4nr >> "$OUT"
echo "measured: $(( $(wc -l < "$OUT") - 1 )) rows"
