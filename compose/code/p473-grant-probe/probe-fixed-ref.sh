#!/bin/bash
# p473 grant probe. Payload channel: raw.githubusercontent.com (Gap 472-A).
# Path set includes lowercase license.txt / license.md / license (Gap 472-B).
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENSE.rst COPYING COPYING.txt license license.txt license.md LICENSE-MIT"
OUT=grant.tsv
printf "repo\tref\tpath\thttp\tbytes\tsha256_12\tline1\n" > $OUT
mkdir -p payloads
while IFS=$'\t' read -r repo ref; do
  [ -z "$repo" ] && continue
  found=0
  for p in $PATHS; do
    f="payloads/$(echo "$repo" | tr '/' '_').$(echo "$p" | tr '/' '_')"
    code=$(curl -s --max-time 25 -o "$f" -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$ref/$p")
    if [ "$code" = "200" ]; then
      b=$(wc -c < "$f" | tr -d ' ')
      d=$(sha256sum "$f" | cut -c1-12)
      l1=$(grep -m1 -v '^[[:space:]]*$' "$f" | cut -c1-90 | tr -d '\r\t')
      printf "%s\t%s\t%s\t200\t%s\t%s\t%s\n" "$repo" "$ref" "$p" "$b" "$d" "$l1" >> $OUT
      found=1
      break
    else
      rm -f "$f"
    fi
  done
  if [ "$found" = "0" ]; then
    printf "%s\t%s\t-\tNOGRANT_AT_%s_PATHS\t-\t-\t-\n" "$repo" "$ref" "$(echo $PATHS | wc -w)" >> $OUT
  fi
done < addrs.tsv
cat $OUT
