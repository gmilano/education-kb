#!/usr/bin/env bash
# Verification ladder for KB repo rows.
# Step 1: existence + HEAD SHA + default branch via `git ls-remote --symref` (authoritative; proxy-safe).
# Step 2: licence payload read from raw.githubusercontent.com PINNED TO THE RESOLVED SHA.
# NOTE: curl on github.com HTML and api.github.com both return 403 for real AND invented slugs
#       under this session's egress proxy -> they cannot discriminate and are NOT used.
set -u
export GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/true
NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE-MIT LICENSE-APACHE license LICENSE.rst NOTICE"

for slug in "$@"; do
  out=$(timeout 30 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$out" ]; then echo -e "$slug\tABSENT\t-\t-\t-\t-"; continue; fi
  ref=$(echo "$out"  | awk '/^ref:/{print $2}' | sed 's#refs/heads/##')
  sha=$(echo "$out"  | awk '!/^ref:/{print $1; exit}')
  short=${sha:0:7}
  found=""
  for n in $NAMES; do
    r=$(timeout 20 curl -s -o /tmp/lic.$$ -w "%{http_code} %{size_download}" \
        "https://raw.githubusercontent.com/$slug/$sha/$n" 2>/dev/null)
    code=${r%% *}; bytes=${r##* }
    if [ "$code" = "200" ] && [ "$bytes" -gt 200 ] 2>/dev/null; then
      # classify from the payload text, not from a badge
      kind=$(head -c 3000 /tmp/lic.$$ | tr 'A-Z' 'a-z' | python3 -c '
import sys
t=sys.stdin.read()
if "apache license" in t and "version 2.0" in t: print("Apache-2.0")
elif "gnu affero" in t: print("AGPL-3.0")
elif "gnu lesser" in t: print("LGPL-3.0")
elif "gnu general public" in t: print("GPL-3.0" if "version 3" in t else "GPL")
elif "mozilla public" in t: print("MPL-2.0")
elif "permission is hereby granted, free of charge" in t: print("MIT")
elif "redistribution and use in source and binary" in t: print("BSD")
elif "unlicense" in t or "public domain" in t: print("Unlicense/PD")
elif "creative commons" in t: print("CC")
else: print("OTHER/unclassified")
')
      found="$n|$kind|$bytes"; break
    fi
  done
  rm -f /tmp/lic.$$
  if [ -z "$found" ]; then echo -e "$slug\tEXISTS\t$ref\t$short\tNO-LICENCE-PAYLOAD\t-"
  else echo -e "$slug\tEXISTS\t$ref\t$short\t$(echo $found|cut -d'|' -f2)\t$(echo $found|cut -d'|' -f1):$(echo $found|cut -d'|' -f3)B"; fi
done
