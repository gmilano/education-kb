#!/bin/bash
# Fetch licence payloads for a corpus. Usage: fetch_licences.sh <targets.tsv> <outdir>
# targets.tsv: owner/repo <TAB> default_branch
TARGETS="$1"; OUT="$2"; mkdir -p "$OUT"
printf "repo\tbranch\tfile\thttp\tbytes\n"
while IFS=$'\t' read -r repo branch; do
  [ -z "$repo" ] && continue
  found=0
  for f in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING LICENSE-MIT license; do
    url="https://raw.githubusercontent.com/$repo/$branch/$f"
    safe=$(echo "$repo" | tr '/' '~')
    code=$(curl -sS -m 25 -o "$OUT/$safe.payload" -w "%{http_code}" "$url" 2>/dev/null)
    if [ "$code" = "200" ]; then
      printf "%s\t%s\t%s\t%s\t%s\n" "$repo" "$branch" "$f" "$code" "$(wc -c < "$OUT/$safe.payload")"
      found=1; break
    fi
  done
  if [ "$found" = "0" ]; then
    rm -f "$OUT/$(echo "$repo" | tr '/' '~').payload"
    printf "%s\t%s\t%s\t404\t0\n" "$repo" "$branch" "NONE-OF-8"
  fi
done < "$TARGETS"
