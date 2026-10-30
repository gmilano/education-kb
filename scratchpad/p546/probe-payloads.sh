#!/bin/bash
# p546 — fetch the payload each quote is charged against.
#
# Branch is RESOLVED, never guessed: p545's alias sweep found only 94 of 162
# shelf repos default to `main` and eight carry values no fixed list would hold
# (`v4.0.x-develop`, `java11`, `2.12`, `19.0`), so a branch ladder fails on 42 %.
# `ls-remote --symref` answers authoritatively in one op.
#
# Usage: probe-payloads.sh <slugs-file> <outdir>
set -u
SLUGS="$1"; OUT="$2"
mkdir -p "$OUT"
: > "$OUT/branches.tsv"
: > "$OUT/fetch.tsv"

while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  safe="${slug//\//__}"
  # --- resolve default branch ---
  br=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null \
       | awk '/^ref:/ {sub("refs/heads/","",$2); print $2; exit}')
  if [ -z "$br" ]; then
    printf '%s\t-\tUNRESOLVED\n' "$slug" >> "$OUT/branches.tsv"
    printf '%s\t-\t-\t0\tNO-BRANCH\n' "$slug" >> "$OUT/fetch.tsv"
    continue
  fi
  printf '%s\t%s\tOK\n' "$slug" "$br" >> "$OUT/branches.tsv"

  # --- fetch README; try the real spellings this base has already met ---
  got=""
  for name in README.md readme.md README.MD Readme.md README.rst README.txt README; do
    code=$(curl -sL -m 25 -o "$OUT/$safe.payload" \
             -w '%{http_code}' \
             "https://raw.githubusercontent.com/$slug/$br/$name" 2>/dev/null)
    if [ "$code" = "200" ] && [ -s "$OUT/$safe.payload" ]; then
      got="$name"; break
    fi
  done
  if [ -z "$got" ]; then
    rm -f "$OUT/$safe.payload"
    printf '%s\t%s\t-\t0\tNO-README\n' "$slug" "$br" >> "$OUT/fetch.tsv"
  else
    printf '%s\t%s\t%s\t%s\tOK\n' "$slug" "$br" "$got" \
      "$(wc -c < "$OUT/$safe.payload" | tr -d ' ')" >> "$OUT/fetch.tsv"
  fi
done < "$SLUGS"

echo "branches: $(grep -c 'OK$' "$OUT/branches.tsv") resolved, $(grep -c 'UNRESOLVED' "$OUT/branches.tsv") unresolved"
echo "payloads: $(grep -c 'OK$' "$OUT/fetch.tsv") fetched, $(grep -cE 'NO-README|NO-BRANCH' "$OUT/fetch.tsv") missing"
