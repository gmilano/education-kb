#!/bin/bash
# usage: verify.sh slug...
OUT="$1"; shift
printf 'slug\tref\tfile\tbytes\tsha256_12\ttitle\n' > "$OUT"
for slug in "$@"; do
  ref=$(timeout 40 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  [ -z "$ref" ] && { printf '%s\tDEAD\t-\t-\t-\t-\n' "$slug" >> "$OUT"; continue; }
  got=0
  for f in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING LICENSE-MIT; do
    url="https://raw.githubusercontent.com/$slug/$ref/$f"
    code=$(timeout 40 curl -sSL -o "$TMPF" -w '%{http_code}' "$url" 2>/dev/null)
    if [ "$code" = "200" ]; then
      b=$(wc -c < "$TMPF" | tr -d ' ')
      h=$(sha256sum "$TMPF" | cut -c1-12)
      t=$(grep -m1 -v '^[[:space:]]*$' "$TMPF" | cut -c1-90 | tr -d '\r')
      printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$ref" "$f" "$b" "$h" "$t" >> "$OUT"
      got=1; break
    fi
  done
  [ "$got" = 0 ] && printf '%s\t%s\tNO-PAYLOAD-AT-ROOT\t-\t-\t-\n' "$slug" "$ref" >> "$OUT"
done
