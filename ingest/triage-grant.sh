#!/bin/bash
# p531 / Gap 530-A ask 1: triage archive-only addresses by GRANT, read first-hand
# from the licence file's own title block over raw.githubusercontent.com (the only
# GitHub channel reachable from this session's shell: api.github.com and github.com
# both return 403).  No network writes; read-only GETs.
#
# Channel: https://raw.githubusercontent.com/{owner}/{repo}/HEAD/{name}
# HEAD resolves to the default branch, so no per-repo branch lookup is needed.
addr="$1"
names=(LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE-MIT license LICENSE.rst NOTICE)
for n in "${names[@]}"; do
  body=$(curl -sL --max-time 20 "https://raw.githubusercontent.com/${addr}/HEAD/${n}" 2>/dev/null)
  [ -z "$body" ] && continue
  case "$body" in '404: Not Found'*) continue;; esac
  head_txt=$(printf '%s' "$body" | head -c 1200 | tr '\n' ' ' | tr -s ' ')
  grant=UNKNOWN
  case "$head_txt" in
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*|*"GNU Affero General Public License"*) grant=AGPL ;;
    *"GNU LESSER GENERAL PUBLIC LICENSE"*|*"GNU Lesser General Public License"*) grant=LGPL ;;
    *"GNU GENERAL PUBLIC LICENSE"*|*"GNU General Public License"*) grant=GPL ;;
    *"Apache License"*) grant=Apache-2.0 ;;
    *"MIT License"*|*"MIT Licence"*|*"The MIT License"*) grant=MIT ;;
    *"Mozilla Public License"*) grant=MPL ;;
    *"Educational Community License"*) grant=ECL-2.0 ;;
    *"Creative Commons"*|*"CC BY"*) grant=CC ;;
    *"BSD "*|*"Redistribution and use in source and binary forms"*) grant=BSD ;;
    *"Unlicense"*|*"public domain"*) grant=Unlicense ;;
    *"ISC License"*) grant=ISC ;;
  esac
  if [ "$grant" = UNKNOWN ]; then
    case "$head_txt" in
      *"Permission is hereby granted, free of charge"*) grant=MIT ;;
    esac
  fi
  printf '%s\t%s\t%s\n' "$addr" "$grant" "$n"
  return 0 2>/dev/null || exit 0
done
printf '%s\tUNRESOLVED\t-\n' "$addr"
