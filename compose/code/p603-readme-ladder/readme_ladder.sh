#!/usr/bin/env bash
slug="$1"; br="$2"
[ -z "$br" ] && { printf '%s\t-\tNO-BRANCH\n' "$slug"; exit 0; }
for f in README.md readme.md Readme.md ReadMe.md README.MD README.rst README README.txt README.markdown README.adoc docs/README.md; do
  c=$(curl -sI -o /dev/null -w '%{http_code}' --max-time 12 "https://raw.githubusercontent.com/$slug/$br/$f")
  [ "$c" = "200" ] && { printf '%s\t%s\t%s\n' "$slug" "$br" "$f"; exit 0; }
done
printf '%s\t%s\tNONE\n' "$slug" "$br"
