#!/usr/bin/env bash
# p771 probe instrument — written from scratch this pass. Two channels only:
#   ref  : git ls-remote --symref   -> default branch + HEAD sha  (API is 403)
#   raw  : raw.githubusercontent.com -> grant payload bytes + sha256_12
set -u
OUT_REF="$1"; OUT_GRANT="$2"; ADDRS="$3"
printf 'addr\tref_status\tdefault_branch\thead_sha12\n' > "$OUT_REF"
printf 'addr\tpath\thttp\tbytes\tsha256_12\ttitle_line\n' > "$OUT_GRANT"
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE.rst LICENSE-MIT license.txt"
while IFS= read -r a; do
  [ -z "$a" ] && continue
  r=$(timeout 45 git ls-remote --symref "https://github.com/$a" HEAD 2>/dev/null)
  if [ -n "$r" ]; then
    br=$(printf '%s\n' "$r" | awk '/^ref:/{print $2}' | sed 's#refs/heads/##')
    sha=$(printf '%s\n' "$r" | awk '!/^ref:/{print $1; exit}' | cut -c1-12)
    printf '%s\tRESOLVES\t%s\t%s\n' "$a" "${br:-?}" "${sha:-?}" >> "$OUT_REF"
  else
    printf '%s\tABSENT-OR-PRIVATE\t-\t-\n' "$a" >> "$OUT_REF"
    continue
  fi
  for p in $PATHS; do
    f=$(mktemp)
    code=$(curl -sS -L --max-time 45 -o "$f" -w '%{http_code}' \
      "https://raw.githubusercontent.com/$a/HEAD/$p" 2>/dev/null)
    if [ "$code" = "200" ]; then
      b=$(wc -c < "$f" | tr -d ' ')
      h=$(sha256sum "$f" | cut -c1-12)
      t=$(tr -d '\r' < "$f" | grep -m1 -v '^[[:space:]]*$' | cut -c1-90)
      printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$a" "$p" "$code" "$b" "$h" "$t" >> "$OUT_GRANT"
    fi
    rm -f "$f"
  done
done < "$ADDRS"
