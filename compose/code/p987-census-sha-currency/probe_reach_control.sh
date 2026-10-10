#!/bin/sh
# pass96: does the shelf's pinned 7-char SHA resolve on raw.githubusercontent at all?
slug=$1; sha=$2
hit=""
for n in README.md README.markdown README README.rst readme.md; do
  c=$(curl -sI -o /dev/null -w '%{http_code}' "https://raw.githubusercontent.com/$slug/$sha/$n")
  [ "$c" = "200" ] && { hit=$n; break; }
done
if [ -n "$hit" ]; then printf '%s\t%s\tREACH-OK\t%s\n' "$slug" "$sha" "$hit"
else printf '%s\t%s\tSHORT-SHA-UNRESOLVED\t-\n' "$slug" "$sha"; fi
