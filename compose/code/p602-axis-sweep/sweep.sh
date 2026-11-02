#!/usr/bin/env bash
# p602 axis sweep. Discovery only: emits candidate addresses + API-claimed grant.
# The API grant is a CLAIM. Nothing here is shippable until byte-read (see verify.sh).
#
# 🔴 The HELD list MUST come from `heldset.sh`, not from a `github.com/`-only grep.
#    p602 learned this mid-pass: a URL-only matcher missed 2 404 of 6 083 held addresses
#    (39.5 %) because this base writes addresses as backticked bare slugs in table cells.
#    Novelty was overstated 55.0 % vs 50.4 % and six already-held rows were nearly shipped
#    as new finds. See evidence/held-set-matcher-correction.2026-11-02-p602.tsv.
set -uo pipefail
AXES="${1:?axes file}"
HELD="${2:?held address list}"
OUT="${3:?output tsv}"
printf 'axis\tfull_name\tstars\tapi_spdx\tpushed_at\tapi_default_branch\theld\n' > "$OUT"
while IFS= read -r axis; do
  [ -z "$axis" ] && continue
  rows=$(gh api -X GET search/repositories -f q="$axis" -f sort=stars -f order=desc -f per_page=25 \
     --jq '.items[] | [.full_name,(.stargazers_count|tostring),(.license.spdx_id//"NONE"),(.pushed_at//"?"),(.default_branch//"?")] | @tsv' 2>/dev/null)
  if [ -z "$rows" ]; then printf '%s\t(NIL)\t\t\t\t\t\n' "$axis" >> "$OUT"; fi
  while IFS=$'\t' read -r fn st lic pa db; do
    [ -z "$fn" ] && continue
    low=$(printf '%s' "$fn" | tr 'A-Z' 'a-z')
    if grep -qxF "$low" "$HELD"; then h=HELD; else h=NEW; fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$axis" "$fn" "$st" "$lic" "$pa" "$db" "$h" >> "$OUT"
  done <<< "$rows"
  sleep 2.5
done < "$AXES"
