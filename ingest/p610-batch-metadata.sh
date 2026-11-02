#!/bin/bash
# batched metadata with count reconciliation (606-C): requested vs returned
IN="$1"; OUT="$2"; MISS="$3"
: > "$OUT"; : > "$MISS"
tmpb=$(mktemp); req=0; got=0
split -l 20 "$IN" "${tmpb}-part-"
for p in ${tmpb}-part-*; do
  q=""; n=0
  while read -r s; do [ -n "$s" ] && { q="$q repo:$s"; n=$((n+1)); }; done < "$p"
  [ -z "$q" ] && continue
  res=$(gh api -X GET search/repositories -f q="$q" -f per_page=100 \
        --jq '.items[]|[(.full_name|ascii_downcase),.full_name,.default_branch,(.license.spdx_id//"NULL"),.stargazers_count,.size,.pushed_at]|@tsv' 2>/dev/null)
  echo "$res" | grep -v '^$' >> "$OUT"
  req=$((req+n)); got=$((got+$(echo "$res" | grep -c '[^[:space:]]')))
done
rm -f ${tmpb}-part-* "$tmpb"
# reconcile: which requested slugs came back?
cut -f1 "$OUT" | sort -u > "${OUT}.got"
sort -u "$IN" | tr 'A-Z' 'a-z' > "${OUT}.req"
comm -23 "${OUT}.req" "${OUT}.got" > "$MISS"
echo "requested=$(wc -l < ${OUT}.req) returned=$(wc -l < ${OUT}.got) unreconciled=$(wc -l < $MISS)"
