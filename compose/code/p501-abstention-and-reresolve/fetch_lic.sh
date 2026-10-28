#!/bin/bash
# p501: resolve a licence payload at a PINNED SHA via raw.githubusercontent (the gate
# Gap 498-M established as discriminating: 200 real / 404 fake). Never curl -sI github.com.
OUT="$1"; shift
printf 'repo\tsha\tpath\thttp\tbytes\tblob_sha1\ttitle_first_80\n' > "$OUT"
while IFS=$'\t' read -r repo sha; do
  [ -z "$repo" ] && continue
  found=0
  for p in LICENSE LICENSE.md LICENSE.txt COPYING LICENCE license; do
    url="https://raw.githubusercontent.com/$repo/$sha/$p"
    code=$(curl -s -o "$OUT.tmp" -w '%{http_code}' --max-time 25 "$url")
    if [ "$code" = "200" ]; then
      b=$(wc -c < "$OUT.tmp" | tr -d ' ')
      s=$(git hash-object "$OUT.tmp")
      t=$(head -c 200 "$OUT.tmp" | tr '\n' ' ' | tr -s ' ' | cut -c1-80)
      printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$sha" "$p" "$code" "$b" "${s:0:12}" "$t" >> "$OUT"
      cp "$OUT.tmp" "$(dirname "$OUT")/lic/$(echo "$repo" | tr '/' '_').$p"
      found=1; break
    fi
  done
  [ $found -eq 0 ] && printf '%s\t%s\t-\tNONE-OF-6-PATHS\t0\t-\t-\n' "$repo" "$sha" >> "$OUT"
done
rm -f "$OUT.tmp"
