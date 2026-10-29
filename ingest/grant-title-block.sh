#!/usr/bin/env bash
# p536 — Gap 535-C's remedy, wired: read a grant's TITLE BLOCK and record WHICH
# REF answered.  A reader keyed to `main` alone produces false "no licence"
# results; `open-learning-exchange/planet` is 404 on `main` and 200 on `master`.
# Branch order is main, then master.  Path order covers the five spellings this
# base has actually met.
# Usage: ingest/grant-title-block.sh owner/repo [owner/repo ...]
set -uo pipefail
printf 'address\tref\tpath\tbytes\ttitle_block\n'
for slug in "$@"; do
  found=0
  for ref in main master; do
    for p in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING; do
      url="https://raw.githubusercontent.com/${slug}/${ref}/${p}"
      body=$(curl -sfL --max-time 25 "$url" 2>/dev/null) || continue
      [ -z "$body" ] && continue
      bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
      # title block = first three non-blank lines, joined
      title=$(printf '%s' "$body" | grep -v '^[[:space:]]*$' | head -3 \
              | tr '\n' ' ' | sed 's/  */ /g; s/^ //; s/ $//' | cut -c1-150)
      printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$ref" "$p" "$bytes" "$title"
      found=1
      break 2
    done
  done
  [ "$found" -eq 0 ] && printf '%s\t-\t-\t0\tNO-GRANT-AT-10-PROBED-PATHS\n' "$slug"
done
