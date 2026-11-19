#!/usr/bin/env bash
set -uo pipefail
for s in "$@"; do
  gh api -X GET search/repositories -f q="repo:$s" -f per_page=1 \
    --jq '.items[] | [.full_name,(.stargazers_count|tostring),(.license.spdx_id // "NULL"),(.pushed_at|split("T")[0]),((.description//"")|gsub("[\t\n]";" ")|.[0:90])] | @tsv' 2>/dev/null
  sleep 1
done
