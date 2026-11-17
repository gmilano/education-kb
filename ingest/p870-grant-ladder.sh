#!/usr/bin/env bash
# p870 -- the LADDER GAP, and the re-measurement it forces.
#
# p869's byte-read ladder is a fixed list of 8 FILENAMES:
#   LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING LICENSE-APACHE docs/License.txt
# `raw.githubusercontent.com` is CASE-SENSITIVE, and the whole Frappe estate ships its grant as
# all-lowercase `license.txt`.  p870 measured that `frappe/education` and `frappe/lms` return
# NO-PAYLOAD-ON-LADDER while carrying a readable grant at `license.txt` (19 B "License: GNU GPL
# V3", and 33,893 B "GNU AFFERO GENERAL PUBLIC LICENSE").
#
# So this instrument does NOT guess filenames.  It LISTS the tree and matches case-insensitively,
# which turns "is there a grant" from a lookup into an observation.
set -u
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT
printf 'address\tgrant_files_found\tfirst_path\tbytes\tsha256_12\tfirst_line\tverdict\n'
while IFS= read -r a; do
  [ -z "$a" ] && continue
  d="$W/$(printf '%s' "$a" | tr '/' '_')"
  if ! GIT_TERMINAL_PROMPT=0 timeout 180 git clone --quiet --filter=blob:none --depth 1 \
       "https://github.com/$a" "$d" >/dev/null 2>&1; then
    printf '%s\t-\t-\t-\t-\t-\tCLONE-FAILED\n' "$a"; continue
  fi
  hits=$(git -C "$d" ls-tree -r HEAD --name-only 2>/dev/null \
         | grep -iE '(^|/)(licen[cs]e|copying|notice)([.-][A-Za-z0-9.]+)?$' || true)
  n=$(printf '%s\n' "$hits" | grep -c . || true)
  if [ "$n" -eq 0 ]; then
    printf '%s\t0\t-\t-\t-\t-\tNO-GRANT-FILE-IN-TREE\n' "$a"; rm -rf "$d"; continue
  fi
  p=$(printf '%s\n' "$hits" | head -1)
  # fetch just that blob's bytes; the clone is blobless so ask the raw channel for the exact path
  ref=$(git -C "$d" rev-parse --abbrev-ref HEAD 2>/dev/null)
  curl -s -o "$W/body" --max-time 25 "https://raw.githubusercontent.com/$a/$ref/$p" 2>/dev/null
  b=$(wc -c < "$W/body" | tr -d ' ')
  h=$(sha256sum "$W/body" | cut -c1-12)
  fl=$(head -3 "$W/body" | grep -m1 . | cut -c1-54 | tr -d '\t')
  printf '%s\t%s\t%s\t%s\t%s\t%s\tGRANT-FILE-PRESENT\n' "$a" "$n" "$p" "$b" "$h" "$fl"
  rm -rf "$d"
done
