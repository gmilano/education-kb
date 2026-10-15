#!/bin/bash
# Fetch one repo's licence blob from raw.githubusercontent at HEAD.
# Emits: repo \t path_form \t http \t bytes \t sha256  (or ABSENT)
# Body is written to $OUTDIR/<owner>__<name>.blob when found.
repo="$1"
OUTDIR="$2"
safe=$(printf '%s' "$repo" | tr '/' '_')

forms="LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt LICENCE LICENCE.md license.txt license.md LICENSE.rst license LICENSE.TXT COPYING.LESSER LICENSE-MIT LICENSE-APACHE docs/LICENSE LICENSE.code LICENSE-AGPL"

for f in $forms; do
  url="https://raw.githubusercontent.com/${repo}/HEAD/${f}"
  code=$(curl -sS -L --max-time 20 -o "$OUTDIR/$safe.tmp" -w "%{http_code}" "$url" 2>/dev/null)
  if [ "$code" = "200" ]; then
    bytes=$(wc -c < "$OUTDIR/$safe.tmp" | tr -d ' ')
    sha=$(sha256sum "$OUTDIR/$safe.tmp" | cut -c1-16)
    mv "$OUTDIR/$safe.tmp" "$OUTDIR/$safe.blob"
    printf '%s\t%s\t200\t%s\t%s\n' "$repo" "$f" "$bytes" "$sha"
    exit 0
  fi
done
rm -f "$OUTDIR/$safe.tmp"
printf '%s\tABSENT\t404\t0\t-\n' "$repo"
