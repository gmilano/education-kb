#!/usr/bin/env bash
# p525 control harness.  Fetches each control payload at its PINNED SHA and compares
# the title-anchored classifier against the expected family AND the expected
# confidence band.  Also prints what ingest/probe-grant.sh's body scan would say, so
# the delta is visible rather than asserted.
set -uo pipefail
cd "$(dirname "$0")"
PASS=0; FAIL=0
printf 'slug\tpath\tsha\tbytes\tsha256_16\texpected\tgot\tconf\tverdict\n'
tail -n +2 controls.tsv | while IFS=$'\t' read -r slug path sha exp expconf why; do
  [ -z "${slug:-}" ] && continue
  tmp=$(mktemp)
  code=$(curl -s -w '%{http_code}' -o "$tmp" "https://raw.githubusercontent.com/${slug}/${sha}/${path}")
  if [ "$code" != "200" ]; then
    printf '%s\t%s\t%s\t-\t-\t%s\tHTTP-%s\t-\tFETCH-FAIL\n' "$slug" "$path" "$sha" "$exp" "$code"
    rm -f "$tmp"; continue
  fi
  bytes=$(wc -c < "$tmp" | tr -d ' ')
  dig=$(sha256sum "$tmp" | cut -c1-16)
  out=$(python3 -I title_grant.py "$tmp")
  got=$(printf '%s' "$out" | cut -f2)
  conf=$(printf '%s' "$out" | cut -f3)
  if [ "$got" = "$exp" ] && [ "$conf" = "$expconf" ]; then v=PASS; else v=FAIL; fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$path" "$sha" "$bytes" "$dig" "$exp" "$got" "$conf" "$v"
  rm -f "$tmp"
done
