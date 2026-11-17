#!/usr/bin/env bash
# p869 -- byte-read the grant. 867-G5 is DISCHARGED and its rule is applied here: resolve
# the DEFAULT REF from the metadata channel FIRST, never assume `main` (p868 measured 24%
# of probes would have 404ed on that assumption).  Throttled at 4s per p869's own
# false-absence measurement.
set -u
LADDER="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING LICENSE-APACHE docs/License.txt"
printf 'address\tdefault_ref\tpath\tbytes\tsha256_12\tspdx_declared\tfirst_line\n'
while IFS= read -r a; do
  [ -z "$a" ] && continue
  sleep 4
  meta=$(gh api -X GET search/repositories -f q="repo:$a" 2>/dev/null)
  ref=$(printf '%s' "$meta" | jq -r '(.items[0].default_branch // "")' 2>/dev/null | tr -d '\n')
  spdx=$(printf '%s' "$meta" | jq -r '(.items[0].license.spdx_id // "NONE")' 2>/dev/null | tr -d '\n')
  if [ -z "$ref" ]; then printf '%s\tUNRESOLVED\t-\t-\t-\t-\t-\n' "$a"; continue; fi
  found=""
  for p in $LADDER; do
    u="https://raw.githubusercontent.com/$a/$ref/$p"
    code=$(curl -s -o "$SP_TMP/body" -w '%{http_code}' --max-time 25 "$u" 2>/dev/null)
    if [ "$code" = "200" ]; then found="$p"; break; fi
  done
  if [ -z "$found" ]; then printf '%s\t%s\tNO-PAYLOAD-ON-LADDER\t-\t-\t%s\t-\n' "$a" "$ref" "$spdx"; continue; fi
  b=$(wc -c < "$SP_TMP/body" | tr -d ' ')
  h=$(sha256sum "$SP_TMP/body" | cut -c1-12)
  fl=$(head -3 "$SP_TMP/body" | grep -m1 . | cut -c1-70 | tr -d '\t')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$a" "$ref" "$found" "$b" "$h" "$spdx" "$fl"
done
