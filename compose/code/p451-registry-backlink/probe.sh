#!/bin/bash
# p451 two-channel probe, controls in BOTH directions.
# ch1 = raw.githubusercontent HEAD/README.md ; ch2 = git ls-remote
for slug in "$@"; do
  c1=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 25 "https://raw.githubusercontent.com/$slug/HEAD/README.md" 2>/dev/null)
  if git ls-remote "https://github.com/$slug" >/dev/null 2>&1; then c2=OK; else c2=FAIL; fi
  printf "%s\t%s\t%s\n" "$slug" "$c1" "$c2"
done
