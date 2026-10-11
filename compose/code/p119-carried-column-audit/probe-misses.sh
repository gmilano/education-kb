#!/bin/sh
# The 10 addresses the search index did not return. "Not indexed" is not "gone":
# git ls-remote FOLLOWS a rename, so git-resolves + search-misses == RENAMED,
# while git-fails == actually GONE. Classify, never infer.
for s in "$@"; do
  head=$(timeout 45 git ls-remote "https://github.com/$s" HEAD 2>/dev/null | awk 'NR==1{print $1}')
  if [ -n "$head" ]; then
    printf '%-46s GIT-OK   %s  -> RENAMED-OR-INDEX-MISS\n' "$s" "$(echo $head | cut -c1-12)"
  else
    printf '%-46s GIT-FAIL (none)         -> GONE-OR-PRIVATE\n' "$s"
  fi
done
