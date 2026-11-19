#!/usr/bin/env bash
# p920 — one search/repositories leg -> TSV (slug, stars, search-channel licence, pushed_at, desc)
set -uo pipefail
Q="$1"
gh api -X GET search/repositories -f q="$Q" -f per_page=30 -f sort=stars \
  --jq '.items[] | [.full_name, (.stargazers_count|tostring), (.license.spdx_id // "NULL"), (.pushed_at|split("T")[0]), ((.description // "") | gsub("[\t\n]";" ") | .[0:110])] | @tsv' 2>&1
