#!/usr/bin/env bash
set -u
for spec in "$@"; do
  slug=${spec%@*}; br=${spec#*@}
  for p in LICENSE LICENSE.txt LICENSE.md COPYING.txt COPYING; do
    body=$(curl -sS --max-time 20 -f "https://raw.githubusercontent.com/$slug/$br/$p" 2>/dev/null) || continue
    [ -z "$body" ] && continue
    title=$(printf '%s' "$body" | sed -n '1,12p' | tr -s ' \t' ' ' | sed 's/^ //;s/ $//' | grep -viE '^$|^copyright|^\(c\)|fsf\.org|^version|everyone is permitted|^preamble' | head -1)
    ver=$(printf '%s' "$body" | sed -n '1,6p' | grep -oiE 'Version [0-9]+' | head -1)
    printf '%-42s %-14s %-7s %s | %s\n' "$slug" "$br/$p" "$(printf '%s' "$body"|wc -c)" "$title" "$ver"
    break
  done
done
