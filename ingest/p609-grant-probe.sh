#!/usr/bin/env bash
# p609 — existence probe (606-E) + grant byte-read across candidate paths/branches.
# Prints TSV: slug  exists  branch  path  http  bytes  first_grant_line
set -u
probe_exists() {
  curl -s -o /dev/null -w '%{http_code}' --max-time 20 \
    "https://github.com/$1/info/refs?service=git-upload-pack"
}
read_grant() {
  local slug="$1" br="$2" p="$3"
  curl -s --max-time 20 -w '\n@@%{http_code}@@%{size_download}@@' \
    "https://raw.githubusercontent.com/$slug/$br/$p"
}
for slug in "$@"; do
  ex=$(probe_exists "$slug")
  found=0
  for br in main master; do
    for p in LICENSE LICENSE.md LICENSE.txt COPYING LICENCE; do
      out=$(read_grant "$slug" "$br" "$p")
      meta=${out##*@@@@}; code=$(printf '%s' "$out" | tr '@' '\n' | grep -E '^[0-9]{3}$' | head -1)
      code=$(printf '%s' "$out" | sed -n 's/.*@@\([0-9]\{3\}\)@@\([0-9]*\)@@$/\1/p')
      size=$(printf '%s' "$out" | sed -n 's/.*@@\([0-9]\{3\}\)@@\([0-9]*\)@@$/\2/p')
      if [ "$code" = "200" ]; then
        line=$(printf '%s' "$out" | sed 's/@@[0-9]*@@[0-9]*@@$//' | grep -viE '^[[:space:]]*$' | head -1 | cut -c1-120)
        printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$ex" "$br" "$p" "$code" "$size" "$line"
        found=1; break
      fi
    done
    [ "$found" = 1 ] && break
  done
  [ "$found" = 0 ] && printf '%s\t%s\t-\t-\tNO_GRANT_FOUND\t-\t-\n' "$slug" "$ex"
done
