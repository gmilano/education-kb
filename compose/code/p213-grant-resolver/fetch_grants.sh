#!/bin/bash
# p213: read licence blob at HEAD from raw.githubusercontent.com, 19 path forms.
FORMS="LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt LICENCE LICENCE.md license.txt license.md LICENSE.rst license LICENSE.TXT COPYING.LESSER LICENSE-MIT LICENSE-APACHE docs/LICENSE LICENSE.code LICENSE-AGPL LICENSE.markdown"
while read -r repo; do
  [ -z "$repo" ] && continue
  safe=$(printf '%s' "$repo" | tr '/' '_')
  found=0
  for f in $FORMS; do
    code=$(curl -sS -L --max-time 20 -o "blobs/$safe.tmp" -w "%{http_code}" \
      "https://raw.githubusercontent.com/${repo}/HEAD/${f}" 2>/dev/null)
    if [ "$code" = "200" ]; then
      bytes=$(wc -c < "blobs/$safe.tmp" | tr -d ' ')
      mv "blobs/$safe.tmp" "blobs/$safe.blob"
      printf '%s\t%s\t200\t%s\t-\n' "$repo" "$f" "$bytes"
      found=1; break
    fi
  done
  rm -f "blobs/$safe.tmp"
  [ "$found" = "0" ] && printf '%s\tABSENT\t404\t0\t-\n' "$repo"
done
