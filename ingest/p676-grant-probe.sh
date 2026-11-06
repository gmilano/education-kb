#!/usr/bin/env bash
# p676 — liveness + REAL default ref + grant payload bytes/sha256.
# Uses the git channel for the default ref (p673: main/master/develop/dev all occur),
# then byte-reads the grant AT THAT REF. Never assumes `main`.
# TSV: slug  live  default_ref  grant_path  http  bytes  sha256_12  title_line
set -u
mkdir -p evidence/p676-payloads
for slug in "$@"; do
  sym=$(timeout 45 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$sym" ]; then printf '%s\tDEAD\t-\t-\t-\t-\t-\t-\n' "$slug"; continue; fi
  ref=$(printf '%s' "$sym" | sed -n 's#^ref:[[:space:]]*refs/heads/\([^[:space:]]*\).*#\1#p' | head -1)
  [ -z "$ref" ] && ref=HEAD
  found=0
  for p in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING LICENSE-MIT LICENSE.rst; do
    out=$(mktemp)
    code=$(curl -s -o "$out" -w '%{http_code}' --max-time 30 "https://raw.githubusercontent.com/$slug/$ref/$p")
    if [ "$code" = "200" ]; then
      b=$(wc -c < "$out" | tr -d ' ')
      h=$(sha256sum "$out" | cut -c1-12)
      t=$(grep -m1 -vE '^[[:space:]]*$' "$out" | tr -d '\r' | cut -c1-70)
      cp "$out" "evidence/p676-payloads/$(printf '%s' "$slug" | tr '/' '~').grant"
      printf '%s\tLIVE\t%s\t%s\t200\t%s\t%s\t%s\n' "$slug" "$ref" "$p" "$b" "$h" "$t"
      found=1; rm -f "$out"; break
    fi
    rm -f "$out"
  done
  [ "$found" = 0 ] && printf '%s\tLIVE\t%s\t-\tNO_GRANT\t-\t-\t-\n' "$slug" "$ref"
done
