#!/bin/bash
# p689 verifier: existence via git ls-remote --symref (real default ref + HEAD sha),
# licence via grant payload read from raw.githubusercontent.com (bytes + sha256_12).
# curl -sI on github.com is NOT used: p684 showed it returns 403 for live, dead and
# nonexistent repos alike, so it has zero discriminating power in this environment.
for slug in "$@"; do
  out=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$out" ]; then echo -e "$slug\tDEAD/NONEXISTENT\t-\t-\t-"; continue; fi
  ref=$(echo "$out" | awk '/^ref:/{print $2}' | sed 's#refs/heads/##')
  sha=$(echo "$out" | grep -oE '^[0-9a-f]{40}' | head -1 | cut -c1-12)
  lic="none"; bytes="-"; h="-"
  for name in LICENSE LICENSE.md LICENSE.txt COPYING LICENCE; do
    body=$(curl -sfL --max-time 25 "https://raw.githubusercontent.com/$slug/$ref/$name")
    if [ -n "$body" ]; then
      bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
      h=$(printf '%s' "$body" | sha256sum | cut -c1-12)
      head3=$(printf '%s' "$body" | head -5 | tr '\n' ' ')
      case "$head3" in
        *"MIT License"*|*"MIT licence"*) lic="MIT" ;;
        *"Apache License"*) lic="Apache-2.0" ;;
        *"BSD"*) lic="BSD" ;;
        *"GNU AFFERO"*|*"GNU Affero"*) lic="AGPL-3.0" ;;
        *"GNU LESSER"*|*"GNU Lesser"*) lic="LGPL" ;;
        *"GNU GENERAL"*|*"GNU General"*) lic="GPL" ;;
        *) lic="OTHER:$(printf '%s' "$head3" | cut -c1-40)" ;;
      esac
      lic="$lic@$name"; break
    fi
  done
  echo -e "$slug\tALIVE\t$ref\t$sha\t$lic\t${bytes}B\t$h"
done
