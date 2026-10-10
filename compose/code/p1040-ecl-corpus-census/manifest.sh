#!/usr/bin/env bash
# p1040 limb A3 -- the rows whose grant is NOT in the LICENSE file.
#
# Usage: bash manifest.sh
#
# Five census rows carry a LICENSE of 45-108 B holding only "YEAR:" and
# "COPYRIGHT HOLDER:". That is not a truncated licence -- it is the R
# convention: DESCRIPTION declares `License: MIT + file LICENSE`, and the
# LICENSE file supplies only the two fields the MIT template needs filled in.
# A root-LICENSE-only census therefore misreads EVERY R package in the corpus,
# and it misreads them as UNRECOGNISED rather than as missing -- the Gap 398
# failure mode arriving through a different door (p283/p289's manifest-named
# licence, now measured for R).
#
# The manifest is read, not assumed. A declared string is the publisher's
# CLAIM; it is reported as such and never merged with a payload reading.
set -u
cd "$(dirname "$0")"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

printf 'slug\tlicense_file_bytes\tmanifest\tdeclared_in_manifest\n'
while IFS= read -r slug; do
  case "$slug" in ''|'#'*) continue ;; esac
  lb=$(curl -sS --max-time 40 -o "$TMP/l" -w '%{http_code}' \
        "https://raw.githubusercontent.com/${slug}/HEAD/LICENSE" 2>/dev/null) || lb=000
  [ "$lb" = "200" ] && lb=$(wc -c < "$TMP/l" | tr -d ' ') || lb="HTTP-$lb"

  found="-"; decl="NO-MANIFEST"
  for m in DESCRIPTION package.json pyproject.toml setup.cfg Cargo.toml composer.json; do
    code=$(curl -sS --max-time 40 -o "$TMP/m" -w '%{http_code}' \
            "https://raw.githubusercontent.com/${slug}/HEAD/${m}" 2>/dev/null) || code=000
    [ "$code" = "200" ] || continue
    found="$m"
    case "$m" in
      DESCRIPTION) decl=$(grep -iE '^License:' "$TMP/m" | head -1 | sed 's/^[Ll]icense:[[:space:]]*//' | cut -c1-60) ;;
      package.json|composer.json) decl=$(python3 -I -c "
import json,sys
try:
    d=json.load(open('$TMP/m')); l=d.get('license') or d.get('licenses') or '-'
    print(l if isinstance(l,str) else str(l)[:60])
except Exception: print('PARSE-ERR')") ;;
      *) decl=$(grep -iE '^[[:space:]]*license' "$TMP/m" | head -1 | cut -c1-60) ;;
    esac
    [ -n "$decl" ] && break
  done
  printf '%s\t%s\t%s\t%s\n' "$slug" "$lb" "$found" "${decl:-EMPTY-FIELD}"
done < lost-addresses.manifest-rows-5.2026-10-10.txt
