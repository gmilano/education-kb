#!/usr/bin/env bash
# census.sh — release-ladder census over this KB's shelf addresses using the
# ANONYMOUS GIT LANE only. No api.github.com (403 for repo endpoints since
# pass 93; see P107-A), no clone, no search.
#
# Output TSV: slug  rc  heads  tags_raw  tags_uniq  head_sha40
#   rc=0        reachable, refs read
#   rc!=0       unreachable — UNREAD, never "zero tags" (P1040)
set -uo pipefail
cd "$(dirname "$0")"
list="${1:-addresses.txt}"
printf 'slug\trc\theads\ttags_raw\ttags_uniq\thead_sha40\n'
while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  out=$(GIT_TERMINAL_PROMPT=0 timeout 60 git ls-remote --tags --heads \
        "https://github.com/$slug" 2>/dev/null); rc=$?
  if [ $rc -eq 0 ]; then
    printf '%s\t0\t%s\n' "$slug" "$(printf '%s\n' "$out" | ./parse_refs.sh)"
  else
    printf '%s\t%s\t-\t-\t-\t-\n' "$slug" "$rc"
  fi
done < "$list"
