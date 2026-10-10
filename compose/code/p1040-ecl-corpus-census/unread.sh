#!/usr/bin/env bash
# p1040 limb A2 -- read the UNREAD payloads BY HAND, as P1036 requires.
#
# Usage: bash unread.sh <census-result.tsv>
#
# P1036: "a licence family can be invisible rather than mislabelled, and
# invisible is worse ... every UNRECOGNISED row must be read by hand before any
# bucket count is published." Gap 398 was exactly this failure, found in one
# family (ECL). This limb asks the question the gap generalises to: how many
# OTHER families is the classifier blind to?
#
# It does not classify. It fetches each unread payload and prints the strongest
# identifying line it carries, so a human reading the output can name the family
# and decide whether it deserves a classifier branch. Naming is a separate,
# reviewable step; guessing from a byte count is what P1024/P1030 forbid.
set -u
cd "$(dirname "$0")"
R="${1:-result.corpus.2026-10-10.tsv}"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

printf 'slug\tfile\tbytes\ttitle_line\n'
awk -F'\t' 'NR>1 && $4=="UNREAD" && $5!="-" {print $1"\t"$5}' "$R" | while IFS=$'\t' read -r slug file; do
  code=$(curl -sS --max-time 40 -o "$TMP/p" -w '%{http_code}' \
          "https://raw.githubusercontent.com/${slug}/HEAD/${file}" 2>/dev/null) || code=000
  if [ "$code" != "200" ]; then
    printf '%s\t%s\tHTTP-%s\t-\n' "$slug" "$file" "$code"; continue
  fi
  bytes=$(wc -c < "$TMP/p" | tr -d ' ')
  # The strongest identifying line: the first non-blank line that is not a bare
  # copyright or a markdown rule. Licence texts put their own name there.
  title=$(tr -d '\r' < "$TMP/p" \
          | grep -vE '^[[:space:]]*$|^[[:space:]]*[-=#*]+[[:space:]]*$' \
          | grep -viE '^[[:space:]]*(copyright|\(c\)|all rights)' \
          | head -1 | cut -c1-110 | tr '\t' ' ')
  printf '%s\t%s\t%s\t%s\n' "$slug" "$file" "$bytes" "$title"
done
