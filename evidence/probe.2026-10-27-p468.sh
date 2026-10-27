#!/usr/bin/env bash
# p468 grant probe v2 — BYTE-EXACT. v1 used $(curl ...) whose command substitution strips
# trailing newlines, which is exactly the -1-byte defect p465 diagnosed in its own instrument.
# v2 writes the payload to a file and measures the file. Nothing is counted through a variable.
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE-MIT license LICENSE.rst"
mkdir -p payloads
for repo in "$@"; do
  head=$(timeout 60 git ls-remote "https://github.com/$repo" HEAD 2>/dev/null | cut -f1)
  if [ -z "$head" ]; then echo "$repo|UNREACHABLE"; continue; fi
  slug=$(printf '%s' "$repo" | tr '/' '_')
  found=""
  for p in $PATHS; do
    code=$(curl -s --max-time 30 -o "payloads/$slug.txt" -w '%{http_code}' "https://raw.githubusercontent.com/$repo/$head/$p")
    if [ "$code" = "200" ]; then
      bytes=$(wc -c < "payloads/$slug.txt" | tr -d ' ')
      sha=$(sha256sum "payloads/$slug.txt" | cut -c1-12)
      echo "$repo|${head:0:12}|$p|${bytes}B|$sha"
      found=1; break
    fi
  done
  [ -z "$found" ] && { rm -f "payloads/$slug.txt"; echo "$repo|${head:0:12}|NO_GRANT@10paths"; }
done
