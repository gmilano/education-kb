#!/usr/bin/env bash
set -u
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  found=""
  for br in main master develop release; do
    for p in LICENSE LICENSE.txt LICENSE.md LICENCE COPYING LICENSE-MIT; do
      body=$(curl -sS --max-time 20 -f "https://raw.githubusercontent.com/$slug/$br/$p" 2>/dev/null) || continue
      [ -z "$body" ] && continue
      spdx="UNKNOWN"
      case "$body" in
        *"Apache License"*"Version 2.0"*) spdx="Apache-2.0" ;;
        *"GNU AFFERO GENERAL PUBLIC LICENSE"*|*"GNU Affero General Public License"*) spdx="AGPL-3.0" ;;
        *"GNU LESSER GENERAL PUBLIC"*|*"GNU Lesser General Public"*) spdx="LGPL" ;;
        *"GNU GENERAL PUBLIC LICENSE"*|*"GNU General Public License"*) spdx="GPL" ;;
        *"Educational Community License"*) spdx="ECL-2.0" ;;
        *"MIT License"*|*"Permission is hereby granted, free of charge"*) spdx="MIT" ;;
        *"BSD"*) spdx="BSD" ;;
        *"Mozilla Public License"*) spdx="MPL-2.0" ;;
        *"CC0"*|*"Creative Commons"*) spdx="CC" ;;
      esac
      printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$p" "$spdx" "$(printf '%s' "$body" | wc -c)"
      found=1; break
    done
    [ -n "$found" ] && break
  done
  [ -z "$found" ] && printf '%s\t-\t-\tNO-LICENCE-FILE\t0\n' "$slug"
done
