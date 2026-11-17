#!/usr/bin/env bash
# p869 -- 868-G1 validation arm: test the `language` PROXY against a real TREE listing.
# A blobless shallow clone costs no file contents but yields the full path list, so
# "does this repository contain code" is answered by counting source files, not by
# trusting a single `language` field that GitHub computes by its own rules.
set -u
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
printf 'address\tfiles\tsource_files\ttop_ext\ttree_verdict\n'
while IFS= read -r a; do
  [ -z "$a" ] && continue
  d="$WORK/$(printf '%s' "$a" | tr '/' '_')"
  if ! GIT_TERMINAL_PROMPT=0 timeout 180 git clone --quiet --filter=blob:none --depth 1 \
       "https://github.com/$a" "$d" >/dev/null 2>&1; then
    printf '%s\t-\t-\t-\tCLONE-FAILED\n' "$a"; continue
  fi
  list=$(git -C "$d" ls-tree -r HEAD --name-only 2>/dev/null)
  n=$(printf '%s\n' "$list" | grep -c . )
  src=$(printf '%s\n' "$list" | grep -ciE '\.(py|js|jsx|ts|tsx|php|java|kt|rb|go|rs|c|cc|cpp|h|hpp|cs|swift|scala|sh|bash|vue|svelte|dart|r|m|mm|pl|lua|sql|ipynb|xml|gradle|toml)$')
  top=$(printf '%s\n' "$list" | grep -oE '\.[A-Za-z0-9]+$' | sort | uniq -c | sort -rn | head -1 | awk '{print $2" ("$1")"}')
  if [ "$src" -ge 5 ]; then v="CODE"; elif [ "$src" -ge 1 ]; then v="THIN-CODE"; else v="NO-CODE"; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$a" "$n" "$src" "${top:--}" "$v"
  rm -rf "$d"
done
