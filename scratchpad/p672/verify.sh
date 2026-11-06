#!/bin/bash
# p672 verifier. Per 671-R: HASH, do not count -- a byte count is defeated by two
# mutations of opposite sign cancelling in length. Per p509/p516: resolve the real
# default branch, never assume main/master.
set -u
printf 'slug\tlive\tdefault_ref\tgrant_file\tbytes\tsha256_12\tfirst_line\tspdx_api\tstars\tpushed\n'
for slug in "$@"; do
  sym=$(timeout 30 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null | awk '/^ref:/{print $2}' | head -1)
  if [ -z "$sym" ]; then printf '%s\tNO\t-\t-\t-\t-\t-\t-\t-\t-\n' "$slug"; continue; fi
  ref="${sym#refs/heads/}"
  gf="-"; bytes="-"; sha="-"; fl="-"
  for cand in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING LICENSE-MIT LICENSE.MIT license LICENSE.rst; do
    url="https://raw.githubusercontent.com/$slug/$ref/$cand"
    code=$(curl -so /tmp/p672pay -w '%{http_code}' "$url" 2>/dev/null)
    if [ "$code" = "200" ] && [ -s /tmp/p672pay ]; then
      gf="$cand"
      bytes=$(wc -c < /tmp/p672pay | tr -d ' ')
      sha=$(sha256sum /tmp/p672pay | cut -c1-12)
      fl=$(head -3 /tmp/p672pay | tr '\n' ' ' | sed 's/\t/ /g' | cut -c1-72)
      break
    fi
  done
  meta=$(gh api -X GET search/repositories -f q="repo:$slug" --jq '.items[0] | [(.license.spdx_id // "none"), (.stargazers_count|tostring), (.pushed_at|tostring)] | @tsv' 2>/dev/null)
  [ -z "$meta" ] && meta=$'-\t-\t-'
  printf '%s\tYES\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$ref" "$gf" "$bytes" "$sha" "$fl" "$meta"
  sleep 1
done
