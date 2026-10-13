#!/usr/bin/env bash
# ACTION JK driver. Emits NUL-delimited "path\0blob\0body\0" for every candidate that PASSES
# P170-A step 2's content test, so classify.py's denominator is P170-A's and reproduces its count.
# Works against a --filter=blob:none partial clone: blobs are fetched lazily, candidates only.
set -u
repo="$1"
# P170-A step 2, verbatim. A filename is not a grant (T213).
BODY_RE='Permission is hereby granted|Apache License|GNU (GENERAL|LESSER|AFFERO)|Eclipse Public License|Mozilla Public License|Redistributions of source code|Permission to use, copy, modify, and/or distribute|Educational Community License'
# step 1: CANDIDATES, broad name match, tree-wide, exhaustive. Never root-only.
git -C "$repo" ls-tree -r HEAD | awk '$2=="blob"' | while read -r _mode _type blob path; do
  case "$path" in
    *[Ll][Ii][Cc][Ee][Nn]*|*[Cc][Oo][Pp][Yy][Ii][Nn][Gg]*|*[Nn][Oo][Tt][Ii][Cc][Ee]*) ;;
    *) continue ;;
  esac
  body=$(git -C "$repo" cat-file -p "$blob" 2>/dev/null) || continue
  printf '%s' "$body" | grep -qiE "$BODY_RE" || continue
  printf '%s\0%s\0%s\0' "$path" "${blob:0:12}" "$body"
done
