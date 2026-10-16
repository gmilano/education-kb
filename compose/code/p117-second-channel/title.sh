#!/usr/bin/env bash
set -u
for spec in "$@"; do
  slug=${spec%@*}; br=${spec#*@}
  for p in LICENSE LICENSE.txt LICENSE.md COPYING.txt COPYING; do
    # `ACTION XY` (p253): the byte column below was `$(printf '%s' "$body"|wc -c)`, which
    # is `P834` — short by the payload's whole trailing-newline run.  Fetch to a FILE, size
    # the FILE; the capture stays for `title`/`ver`, which are newline-insensitive.
    __p=$(mktemp)
    curl -sS --max-time 20 -f -o "$__p" "https://raw.githubusercontent.com/$slug/$br/$p" 2>/dev/null || { rm -f "$__p"; continue; }
    body=$(cat "$__p")
    [ -z "$body" ] && { rm -f "$__p"; continue; }
    title=$(printf '%s' "$body" | sed -n '1,12p' | tr -s ' \t' ' ' | sed 's/^ //;s/ $//' | grep -viE '^$|^copyright|^\(c\)|fsf\.org|^version|everyone is permitted|^preamble' | head -1)
    ver=$(printf '%s' "$body" | sed -n '1,6p' | grep -oiE 'Version [0-9]+' | head -1)
    printf '%-42s %-14s %-7s %s | %s\n' "$slug" "$br/$p" "$(wc -c < "$__p" | tr -d ' ')" "$title" "$ver"
    rm -f "$__p"
    break
  done
done
