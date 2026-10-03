#!/bin/bash
# Authoritative license sweep, HEAD-ref based.
# raw.githubusercontent.com resolves the ref "HEAD" to the repo's DEFAULT branch,
# whatever it is named -> the branch dimension disappears (main/master/develop/trunk all covered).
# Three-way outcome: LICENSED / UNLICENSED (repo reachable, no license file) / UNREACHABLE.
# TSV: slug \t status \t hit_path \t bytes \t license_id
slug="$1"
classify() {
  local c="$1" head12 body
  head12=$(printf '%s' "$c" | head -12)
  if   printf '%s' "$head12" | grep -qi "GNU AFFERO GENERAL PUBLIC LICENSE"; then echo "AGPL-3.0"; return
  elif printf '%s' "$head12" | grep -qi "GNU LESSER GENERAL PUBLIC LICENSE"; then echo "LGPL"; return
  elif printf '%s' "$head12" | grep -qi "GNU GENERAL PUBLIC LICENSE"; then echo "GPL"; return
  elif printf '%s' "$head12" | grep -qi "Apache License"; then echo "Apache-2.0"; return
  elif printf '%s' "$head12" | grep -qi "Mozilla Public License"; then echo "MPL-2.0"; return
  elif printf '%s' "$head12" | grep -qi "CC0 1.0\|Creative Commons Zero"; then echo "CC0-1.0"; return
  elif printf '%s' "$head12" | grep -qi "Creative Commons Attribution"; then echo "CC-BY"; return
  elif printf '%s' "$head12" | grep -qi "Business Source License"; then echo "BUSL"; return
  elif printf '%s' "$head12" | grep -qi "Elastic License"; then echo "Elastic"; return
  elif printf '%s' "$head12" | grep -qi "PolyForm"; then echo "PolyForm"; return
  elif printf '%s' "$head12" | grep -qi "ISC License"; then echo "ISC"; return
  elif printf '%s' "$head12" | grep -qi "MIT License\|MIT No Attribution"; then echo "MIT"; return
  fi
  body="$c"
  if   printf '%s' "$body" | grep -qi "Permission is hereby granted, free of charge"; then echo "MIT"
  elif printf '%s' "$body" | grep -qi "Redistribution and use in source and binary"; then echo "BSD"
  elif printf '%s' "$body" | grep -qi "free and unencumbered software"; then echo "Unlicense"
  else echo "UNKNOWN"; fi
}
for fn in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt license license.md license.txt \
          LICENCE LICENCE.md LICENSE-MIT LICENSE-APACHE LICENSE.rst LICENSE-MIT.txt; do
  out=$(curl -s --max-time 25 -w $'\n%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/${fn}" 2>/dev/null)
  code=$(printf '%s' "$out" | tail -1)
  if [ "$code" = "200" ]; then
    content=$(printf '%s' "$out" | sed '$d')
    bytes=$(printf '%s' "$content" | wc -c | tr -d ' ')
    printf '%s\tLICENSED\t%s\t%s\t%s\n' "$slug" "$fn" "$bytes" "$(classify "$content")"
    exit 0
  fi
done
# Existence control: separates "reachable but unlicensed" from "cannot reach the repo at all".
for rm in README.md README.rst readme.md README README.markdown docs/README.md package.json setup.py; do
  code=$(curl -s -o /dev/null --max-time 25 -w '%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/${rm}" 2>/dev/null)
  if [ "$code" = "200" ]; then
    printf '%s\tUNLICENSED\t-\t0\t(reachable via %s)\n' "$slug" "$rm"
    exit 0
  fi
done
printf '%s\tUNREACHABLE\t-\t0\t-\n' "$slug"
