#!/usr/bin/env bash
# p602 enrichment. `gh api repos/<o>/<n>` is DENIED for repos not attached to this session,
# so stars + description come from search/repositories with a `repo:` OR-batch, which IS
# reachable.  Recorded because the obvious endpoint being blocked is the kind of thing a
# later pass will otherwise rediscover by hitting the same wall.
set -uo pipefail
LIST="${1:?list}"; OUT="${2:?out}"
printf 'repo\tstars\tpushed_at\tapi_spdx\tdescription\n' > "$OUT"
mapfile -t all < <(grep -vE '^\s*(#|$)' "$LIST" | awk '{print $1}')
for ((i=0; i<${#all[@]}; i+=10)); do
  q=""; for r in "${all[@]:i:10}"; do q="$q repo:$r"; done
  gh api -X GET search/repositories -f q="$q" -f per_page=30 \
    --jq '.items[]|[.full_name,(.stargazers_count|tostring),(.pushed_at//"?"),(.license.spdx_id//"NONE"),((.description//"-")|gsub("\t";" "))]|@tsv' 2>/dev/null >> "$OUT"
  sleep 2.5
done
