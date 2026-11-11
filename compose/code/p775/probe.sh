#!/usr/bin/env bash
# p775 address + grant probe — written from scratch for this pass.
#
# Re-implements rather than executes compose/code/p774/*. Two channels only,
# because they are the two that answer (p775 re-measured all five):
#   ref channel : git ls-remote      -> existence, DEFAULT BRANCH, HEAD sha
#   raw channel : raw.githubusercontent.com -> the grant PAYLOAD bytes
# api.github.com, github.com HTML and codeload.github.com are all 403 under
# this environment's proxy, so no star count, no refs count, no spdx_id.
#
# Usage: p775-probe.sh <addresses-file> <outdir>
set -u
ADDRS="$1"
OUT="$2"
mkdir -p "$OUT/payloads"

# Case-aware grant filenames. A repository that keeps its grant under any of
# these is NOT a NO-GRANT repository; p774 measured 33 names and generalised
# ERPNext that way, so the list is carried in prose and rebuilt here.
NAMES="LICENSE LICENSE.txt LICENSE.md LICENCE LICENCE.txt LICENCE.md license \
license.txt license.md licence licence.txt licence.md License License.txt \
License.md Licence Licence.txt Licence.md COPYING COPYING.txt COPYING.md \
copying LICENSE-MIT LICENSE-APACHE LICENSE.rst licence.rst LICENSE.BSD \
LICENSE-2.0.txt MIT-LICENSE MIT-LICENSE.txt UNLICENSE LICENSE.html \
docs/LICENSE .github/LICENSE"

while IFS= read -r repo; do
  [ -z "$repo" ] && continue
  case "$repo" in \#*) continue ;; esac

  # --- ref channel: existence + default branch + HEAD ---
  sym=$(timeout 45 git ls-remote --symref "https://github.com/$repo" HEAD 2>/dev/null)
  if [ -z "$sym" ]; then
    printf '%s\tABSENT-OR-PRIVATE\t-\t-\t-\t-\t-\n' "$repo"
    continue
  fi
  branch=$(printf '%s\n' "$sym" | awk '/^ref:/{gsub("refs/heads/","",$2); print $2; exit}')
  # DEFECT p775-#3 (caught by control): /HEAD$/ also matches the symref line
  # "ref: refs/heads/main\tHEAD", so it returned the literal "ref:". Require a
  # 40-hex first field.
  head=$(printf '%s\n' "$sym" | awk '$2=="HEAD" && $1 ~ /^[0-9a-f]{40}$/ {print substr($1,1,12); exit}')
  [ -z "$branch" ] && branch="(detached)"

  # --- raw channel: find the grant ---
  slug=$(printf '%s' "$repo" | tr '/' '~')
  found=""; bytes=0
  for n in $NAMES; do
    code=$(timeout 30 curl -sS -o "$OUT/payloads/$slug.txt" \
           -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$branch/$n" 2>/dev/null)
    if [ "$code" = "200" ]; then
      sz=$(wc -c < "$OUT/payloads/$slug.txt")
      # guard: GitHub serves a 14-byte "404: Not Found" body on some paths
      if [ "$sz" -gt 60 ]; then found="$n"; bytes="$sz"; break; fi
    fi
  done
  if [ -z "$found" ]; then
    rm -f "$OUT/payloads/$slug.txt"
    printf '%s\tRESOLVES\t%s\t%s\tNO-GRANT-AT-ROOT(%d names)\t0\t-\n' \
      "$repo" "$branch" "$head" "$(printf '%s' "$NAMES" | wc -w)"
    continue
  fi
  printf '%s\tRESOLVES\t%s\t%s\t%s\t%s\t-\n' "$repo" "$branch" "$head" "$found" "$bytes"
done < "$ADDRS"
