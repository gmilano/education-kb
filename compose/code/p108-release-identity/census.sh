#!/usr/bin/env bash
# census.sh — release-IDENTITY census over this KB's shelf addresses.
# ANONYMOUS GIT LANE ONLY: no api.github.com (403 by session scoping, P107-A),
# no clone, no search.
#
# Address list: ./addresses.txt — p107's list with case-duplicates removed
# (P108-F). GitHub owner/repo is case-insensitive, so the three pairs p107
# carried were one repo counted twice; the honest denominator is 296.
#
# Output TSV: slug rc tags_uniq stable_n prerel_n latest_stable latest_stable_sha40
#             prefix_n latest_prefix latest_prefix_sha40 class
#   rc!=0 -> UNREAD. An unread row is never "no releases" (P1040).
set -uo pipefail
cd "$(dirname "$0")"
list="${1:-addresses.txt}"
printf 'slug\trc\ttags_uniq\tstable_n\tprerel_n\tlatest_stable\tlatest_stable_sha40\tprefix_n\tlatest_prefix\tlatest_prefix_sha40\tclass\n'
while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  out=$(GIT_TERMINAL_PROMPT=0 timeout 60 git ls-remote --tags \
        "https://github.com/$slug" 2>/dev/null); rc=$?
  if [ $rc -eq 0 ]; then
    printf '%s\t0\t%s\n' "$slug" "$(printf '%s\n' "$out" | ./pick_latest.sh)"
  else
    printf '%s\t%s\t-\t-\t-\t-\t-\t-\t-\t-\tUNREAD\n' "$slug" "$rc"
  fi
done < "$list"
