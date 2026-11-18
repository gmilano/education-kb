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
    for path in LICENSE LICENSE.md LICENSE.txt license.txt COPYING COPYING.txt COPYING.TXT LICENCE; do
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
  # SPLIT-FILE DUAL GRANT - added p884 on first-hand evidence.
  #
  # `RWTH-OS/eduOS-rs` (493*, the highest-starred education find of p884's owner
  # sweep) returned 404 on all 16 probes above and was therefore reported
  # NO-GRANT-FILE. It is in fact dual-licensed: `LICENSE-APACHE` (9,722 B) AND
  # `LICENSE-MIT` (1,023 B) - the Rust ecosystem's two-file convention. The ladder
  # above cannot see it, so the ladder MANUFACTURED an absence.
  #
  # Worse, and this is the part that reaches a client: `search/repositories` has a
  # single `license.spdx_id` field, and for this repo it says `Apache-2.0` alone.
  # A studio told "Apache-2.0" silently loses the MIT option it is entitled to.
  # One grant field cannot express two grants.
  for ref in main master; do
    a=""; m=""
    for ap in LICENSE-APACHE LICENSE-APACHE-2.0 LICENSE.APACHE; do
      c=$(curl -sS -o "$out/$key.body" -w '%{http_code}' --max-time 30 \
           "https://raw.githubusercontent.com/$slug/$ref/$ap" 2>/dev/null)
      [ "$c" = "200" ] && { a="$ap"; break; }
    done
    for mp in LICENSE-MIT LICENSE.MIT; do
      c=$(curl -sS -o "$out/$key.body2" -w '%{http_code}' --max-time 30 \
           "https://raw.githubusercontent.com/$slug/$ref/$mp" 2>/dev/null)
      [ "$c" = "200" ] && { m="$mp"; break; }
    done
    if [ -n "$a" ] && [ -n "$m" ]; then
      b1=$(stat -c%s "$out/$key.body"); b2=$(stat -c%s "$out/$key.body2")
      s1=$(sha256sum "$out/$key.body" | cut -c1-12)
      s2=$(sha256sum "$out/$key.body2" | cut -c1-12)
      printf '%s\t%s\t%s+%s\t200\t%s+%s\t%s+%s\n' \
        "$slug" "$ref" "$a" "$m" "$b1" "$b2" "$s1" "$s2"
      return 0
    fi
    rm -f "$out/$key.body2"
  done
  rm -f "$out/$key.body" "$out/$key.body2"
  printf '%s\t-\t-\t404\t-\t-\n' "$slug"
}
if [ -n "$SLUGS" ]; then
  while IFS= read -r slug; do
    [ -n "$slug" ] && fetch_one "$slug" "$OUT"
  done < "$SLUGS"
fi
