#!/usr/bin/env bash
# Action B (pass 109): P340 re-sweep. Does cession live in a SPELLING the sweep didn't ask for?
# Channel: raw.githubusercontent.com only (api/web github = 403). Negative control included.
OUT="$1"; TARGETS="$2"
: > "$OUT"
NAMES="LICENSE LICENCE COPYING README.md LICENSE.md LICENCE.md LICENSE.txt LICENSE.TXT COPYING.txt LICENCE.txt"
BRANCHES="main master"
while read -r repo; do
  [ -z "$repo" ] && continue
  for br in $BRANCHES; do
    for nm in $NAMES; do
      url="https://raw.githubusercontent.com/$repo/$br/$nm"
      code=$(curl -sS -o /tmp/p340.body -w '%{http_code}' --max-time 20 "$url" 2>/dev/null || echo 000)
      bytes=0; sha="-"; fam="-"
      if [ "$code" = "200" ]; then
        bytes=$(wc -c < /tmp/p340.body)
        sha=$(sha256sum < /tmp/p340.body | cut -d' ' -f1 | cut -c1-12)
        head -c 4000 /tmp/p340.body > /tmp/p340.head
        if   grep -qi 'MIT License' /tmp/p340.head; then fam="MIT"
        elif grep -qi 'Apache License' /tmp/p340.head; then fam="Apache-2.0"
        elif grep -qi 'GNU AFFERO' /tmp/p340.head; then fam="AGPL-3.0"
        elif grep -qi 'GNU LESSER' /tmp/p340.head; then fam="LGPL"
        elif grep -qi 'GNU GENERAL PUBLIC' /tmp/p340.head; then fam="GPL"
        elif grep -qi 'Redistribution and use in source and binary' /tmp/p340.head; then fam="BSD"
        elif grep -qi 'Mozilla Public License' /tmp/p340.head; then fam="MPL-2.0"
        elif grep -qi 'Creative Commons\|CC BY' /tmp/p340.head; then fam="CC"
        elif grep -qi 'Educational Community License' /tmp/p340.head; then fam="ECL-2.0"
        else fam="OTRO-200"
        fi
      fi
      printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$br" "$nm" "$code" "$bytes" "$sha" "$fam" >> "$OUT"
    done
  done
done < "$TARGETS"
