#!/usr/bin/env bash
# grant_ladder.sh — resolve existence, pin SHA, read licence payload, name family.
# Method: existence by `git ls-remote --symref` (P880: curl -sI and api.github.com
# both return 403 for real AND invented slugs, so neither can discriminate).
# Payload pinned to the resolved SHA, never to a branch name (P793).
# Bytes by `curl -w '%{size_download}'` (P929: method stated with the figure).
# Family named from the payload, with MIT/ISC separated by body signature (P943:
# an MIT payload can contain no family name at all).
set -uo pipefail

NAMES=(LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt
       COPYING.LESSER LICENSE-MIT LICENSE-APACHE license.txt License.txt
       LICENSE.rst MIT-LICENSE MIT-LICENSE.txt LICENSE.MIT)

family() {  # $1 = payload file
  local p="$1" head body
  head=$(head -c 400 "$p" | tr '\n' ' ' | tr -s ' ')
  body=$(cat "$p")
  case "$head" in
    *"Apache License"*)             echo "Apache-2.0"; return;;
    *"Educational Community License"*) echo "ECL-2.0"; return;;
    *"GNU AFFERO"*|*"GNU Affero"*)  echo "AGPL-3.0"; return;;
    *"GNU LESSER"*|*"GNU Lesser"*)  echo "LGPL"; return;;
    *"GNU GENERAL PUBLIC"*|*"GNU General Public"*) echo "GPL"; return;;
    *"Mozilla Public License"*)     echo "MPL-2.0"; return;;
    *"MIT License"*|*"MIT license"*) echo "MIT"; return;;
    *"BSD"*)                        echo "BSD"; return;;
    *"Unlicense"*|*"UNLICENSE"*)    echo "Unlicense"; return;;
    *"Creative Commons"*|*"CC0"*)   echo "CC"; return;;
  esac
  # P943: no family name in the title block. Decide on body signature.
  if grep -qi "sublicense" <<<"$body" && grep -qi "above copyright notice" <<<"$body"; then
    echo "MIT-by-signature"
  elif grep -qi "above copyright notice" <<<"$body"; then
    echo "ISC-or-BSD-by-signature"
  else
    echo "NO-FAMILY-NAMED"
  fi
}

printf 'slug\tbranch\tsha\tlicence_file\tbytes\tfamily\n'
for slug in "$@"; do
  info=$(timeout 30 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$info" ]; then
    printf '%s\tNOT-RESOLVED\t-\t-\t-\tEXISTENCE-DENIED\n' "$slug"; continue
  fi
  branch=$(awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}' <<<"$info")
  sha=$(awk '!/^ref:/{print substr($1,1,7); exit}' <<<"$info")
  found=""
  for n in "${NAMES[@]}"; do
    url="https://raw.githubusercontent.com/$slug/$sha/$n"
    out=$(timeout 25 curl -s -o "/tmp/pl.$$" -w '%{http_code} %{size_download}' "$url" 2>/dev/null)
    code=${out%% *}; size=${out##* }
    if [ "$code" = "200" ] && [ "${size:-0}" -gt 100 ]; then
      printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "${branch:-?}" "$sha" "$n" "$size" "$(family /tmp/pl.$$)"
      found=1; break
    fi
  done
  [ -z "$found" ] && printf '%s\t%s\t%s\t-\t-\tNO-PAYLOAD-IN-%d-NAMES\n' "$slug" "${branch:-?}" "$sha" "${#NAMES[@]}"
  rm -f "/tmp/pl.$$"
done
