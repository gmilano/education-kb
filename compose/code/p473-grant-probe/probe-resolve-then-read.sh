#!/bin/bash
# p473 batch 2: resolve default branch first-hand, then read the grant payload.
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENSE.rst COPYING COPYING.txt copying license license.txt license.md LICENSE-MIT LICENSE-APACHE"
OUT=grant3.tsv
printf "repo\tHEADsha\tdefault_ref\tpath\tbytes\tsha256_12\tline1\tline2\n" > $OUT
mkdir -p payloads3
while read -r repo; do
  [ -z "$repo" ] && continue
  out=$(git ls-remote --symref "https://github.com/$repo" HEAD 2>/dev/null)
  if [ -z "$out" ]; then printf "%s\tUNRESOLVED\t-\t-\t-\t-\t-\t-\n" "$repo" >> $OUT; continue; fi
  sym=$(echo "$out" | grep '^ref:' | head -1 | awk '{print $2}')
  sha=$(echo "$out" | grep -v '^ref:' | head -1 | awk '{print substr($1,1,12)}')
  ref=${sym#refs/heads/}
  found=0
  for p in $PATHS; do
    f="payloads3/$(echo "$repo" | tr '/' '_').$(echo "$p" | tr '/' '_')"
    code=$(curl -s --max-time 25 -o "$f" -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$ref/$p")
    if [ "$code" = "200" ]; then
      b=$(wc -c < "$f" | tr -d ' ')
      d=$(sha256sum "$f" | cut -c1-12)
      l1=$(grep -v '^[[:space:]]*$' "$f" | sed -n 1p | cut -c1-80 | tr -d '\r\t' | sed 's/^ *//')
      l2=$(grep -v '^[[:space:]]*$' "$f" | sed -n 2p | cut -c1-60 | tr -d '\r\t' | sed 's/^ *//')
      printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$repo" "$sha" "$ref" "$p" "$b" "$d" "$l1" "$l2" >> $OUT
      found=1; break
    else rm -f "$f"; fi
  done
  [ "$found" = "0" ] && printf "%s\t%s\t%s\tNOGRANT/%s_paths\t-\t-\t-\t-\n" "$repo" "$sha" "$ref" "$(echo $PATHS|wc -w)" >> $OUT
done < addrs2.txt
