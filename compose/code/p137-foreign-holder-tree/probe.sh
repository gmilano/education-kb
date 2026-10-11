#!/bin/bash
# p137-foreign-holder-tree, step 1: enumerate the TREE, not a filename list.
#
#   ./probe.sh out.tsv owner/repo [owner/repo ...]
#
# A blobless, no-checkout, depth-1 clone fetches commit+tree objects and no file
# contents, so a 67 589-path repository (moodle) costs seconds and almost no disk.
# `git ls-tree -r HEAD --name-only` then yields every path at HEAD.
#
# This script only COLLECTS paths. Classification lives in `foreign_holder.py`
# so that it is testable offline -- and because the first version of this probe
# counted an empty list as one item and published seven wrong rows.
set -u
OUT=$1; shift
WORK=$(mktemp -d)
printf 'slug\tpaths\tlicence_shaped_paths\n' > "$OUT"
for slug in "$@"; do
  d="$WORK/$(echo "$slug" | tr '/' '_')"
  if ! git clone --filter=blob:none --no-checkout --depth 1 --quiet \
        "https://github.com/$slug" "$d" 2>/dev/null; then
    printf '%s\tCLONE_FAIL\t\n' "$slug" >> "$OUT"; continue
  fi
  all=$(git -C "$d" ls-tree -r HEAD --name-only)
  n=$(printf '%s' "$all" | grep -c '' || true)
  lic=$(printf '%s' "$all" | grep -iE '(^|/)(licen[cs]e|copying|notice|copyright)([._-][a-z0-9.+-]*)?$|\.licen[cs]e$' || true)
  printf '%s\t%s\t%s\n' "$slug" "$n" "$(printf '%s' "$lic" | tr '\n' ';')" >> "$OUT"
  rm -rf "$d"
done
rm -rf "$WORK"
