#!/usr/bin/env bash
# p881 — the two-channel probe for the channel state p881 MEASURED:
#   api.github.com/repos/*  -> 403 "not enabled for this session"  (metadata channel DOWN)
#   github.com HTML, codeload -> 403                                (DOWN)
#   git ls-remote            -> 200                                 (REFS channel UP)
#   raw.githubusercontent    -> resolves                            (BYTES channel UP)
# So this pass can byte-read a grant and prove liveness of a ref, and CANNOT read
# spdx_id, stars, forks or pushed_at.  A pass that cannot measure stars must not
# publish stars.  Usage: probe.sh <slug> [...]
set -u
PATHS="LICENSE LICENSE.txt LICENSE.md license.txt license LICENCE COPYING LICENSE-MIT LICENSE.Apache-2.0 docs/License.txt"
printf 'slug\trefs_channel\thead_ref\tgrant_path\tbytes\tsha256_12\tfirst_line\n'
for slug in "$@"; do
  sym=$(timeout 40 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null | awk '/^ref:/{print $2}' | head -1)
  if [ -z "$sym" ]; then printf '%s\tREFS-REFUSED\t-\t-\t-\t-\t-\n' "$slug"; continue; fi
  br=${sym#refs/heads/}
  found=0
  for p in $PATHS; do
    body=$(curl -s --max-time 25 -w '\n%{http_code}' "https://raw.githubusercontent.com/$slug/$br/$p")
    code=$(printf '%s' "$body" | tail -1); payload=$(printf '%s' "$body" | sed '$d')
    if [ "$code" = "200" ]; then
      n=$(printf '%s' "$payload" | wc -c)
      h=$(printf '%s' "$payload" | sha256sum | cut -c1-12)
      fl=$(printf '%s' "$payload" | grep -m1 -v '^[[:space:]]*$' | cut -c1-70)
      printf '%s\tUP\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$p" "$n" "$h" "$fl"
      found=1; break
    fi
  done
  [ "$found" = 0 ] && printf '%s\tUP\t%s\tNO-PAYLOAD-ON-LADDER\t-\t-\t-\n' "$slug" "$br"
done

true
