#!/bin/bash
# Mide el LICENSE por PAYLOAD (raw.githubusercontent.com): bytes, sha256, titular.
printf "slug\tbranch\tfile\thttp\tbytes\tsha256_12\tholder\n"
for slug in "$@"; do
  found=0
  for br in main master; do
    for f in LICENSE LICENSE.md LICENSE.txt COPYING LICENCE; do
      url="https://raw.githubusercontent.com/$slug/$br/$f"
      code=$(curl -sS -o body.tmp -w '%{http_code}' --max-time 25 "$url")
      if [ "$code" = "200" ]; then
        b=$(wc -c < body.tmp | tr -d ' ')
        h=$(sha256sum body.tmp | cut -c1-12)
        hold=$(grep -m1 -iE 'copyright' body.tmp | sed 's/^[[:space:]]*//' | cut -c1-70)
        [ -z "$hold" ] && hold="(sin linea copyright)"
        printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$slug" "$br" "$f" "$code" "$b" "$h" "$hold"
        found=1; break
      fi
    done
    [ "$found" = "1" ] && break
  done
  [ "$found" = "0" ] && printf "%s\t-\t-\t404\t-\t-\tNO-LICENSE-FILE-FOUND\n" "$slug"
done
