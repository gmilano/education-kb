#!/bin/sh
# Step 2 of `ACTION ST` — read each slug's grant FIRST-HAND off raw.githubusercontent.com.
#
# raw is one of the four channels these shelves have measured as reachable for 22
# consecutive passes (api.github.com and github.com HTML are not). One slug costs
# one request when it hits `main/LICENSE`; the ladder below only runs on a 404, so
# the cost is ~1 request per slug and not 12.
#
# usage: fetch_grants.sh <slugs-file> <out-dir>
SLUGS="$1"; OUT="$2"; mkdir -p "$OUT"
fetch_one() {
  slug="$1"; out="$2"
  o=${slug%%/*}; r=${slug##*/}
  key="${o}__${r}"
  for ref in main master; do
    for path in LICENSE LICENSE.md LICENSE.txt license.txt COPYING LICENCE; do
      f="$out/$key.body"
      code=$(curl -sS -o "$f" -w '%{http_code}' --max-time 30 \
              "https://raw.githubusercontent.com/$slug/$ref/$path" 2>/dev/null)
      if [ "$code" = "200" ]; then
        bytes=$(stat -c%s "$f")
        sha=$(sha256sum "$f" | cut -c1-12)
        printf '%s\t%s\t%s\t200\t%s\t%s\n' "$slug" "$ref" "$path" "$bytes" "$sha"
        return 0
      fi
    done
  done
  rm -f "$out/$key.body"
  printf '%s\t-\t-\t404\t-\t-\n' "$slug"
}
if [ -n "$SLUGS" ]; then
  while IFS= read -r slug; do
    [ -n "$slug" ] && fetch_one "$slug" "$OUT"
  done < "$SLUGS"
fi
