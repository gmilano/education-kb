#!/usr/bin/env bash
# P116 ACTION A. Second channel for layer R placements: raw.githubusercontent.com,
# reading CODEOWNERS / .github/FUNDING.yml / AUTHORS / CONTRIBUTORS — none of which
# p115's layer R reads (it reads the README only).
# Keeps every byte on disk: the streams ARE the evidence, the TSV is a derivation
# (p115's own rule, learned the hard way when its script was edited mid-census).
set -u
SLUGS="$1"; OUT="$2"; STREAMDIR="$3"
mkdir -p "$STREAMDIR"
PATHS=".github/CODEOWNERS CODEOWNERS docs/CODEOWNERS .github/FUNDING.yml AUTHORS AUTHORS.md AUTHORS.txt CONTRIBUTORS CONTRIBUTORS.md"
: > "$OUT"
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  safe=$(printf '%s' "$slug" | tr '/' '%')
  got=0
  for br in main master; do
    for p in $PATHS; do
      url="https://raw.githubusercontent.com/$slug/$br/$p"
      f="$STREAMDIR/$safe@$br@$(printf '%s' "$p" | tr '/' '%')"
      code=$(curl -sS -o "$f" -w '%{http_code}' --max-time 25 "$url" 2>/dev/null || echo 000)
      if [ "$code" = "200" ]; then
        got=$((got+1))
        printf '%s\t%s\t%s\t200\t%s\n' "$slug" "$br" "$p" "$f" >> "$OUT"
      else
        rm -f "$f"
        printf '%s\t%s\t%s\t%s\t-\n' "$slug" "$br" "$p" "$code" >> "$OUT"
      fi
    done
    [ "$got" -gt 0 ] && break
  done
done < "$SLUGS"
