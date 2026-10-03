#!/bin/bash
# P235 — does the CAPA axis of P230 generalize, and with which SIGN?
#
# P230 (pass 76) measured the OneRoster layer by CAPA (server / client / bridge) and found:
#   server  -> no permissive piece on the live spec   => EXPOSING is closed
#   client  -> four permissive, one on the live spec  => CONSUMING is open
#   bridge  -> the only two open ones unlicensed
# and concluded "CONSUMING OneRoster can be done today; EXPOSING cannot."
#
# The open question pass 76 left: is that a property of the SECTOR or of the STANDARD?
# This instrument asks the same three-capa question of a DIFFERENT standard in the same
# sector -- xAPI / Caliper telemetry -- so the two tables can be compared cell by cell.
#
# Three fields per piece, each measured in its own channel, never inferred from a row:
#   licencia  payload of the license file via raw.githubusercontent (P172), ref HEAD (P170)
#   vida      last commit on the DEFAULT BRANCH read from ls-remote --symref (pass 38's
#             portable invocation: a fetch by HEAD's SHA returns FETCHFAIL in this environment)
#   rol       the spec version found IN THE CODE, not in the README -- because the README
#             states an ambition and the inventory row inherits it (P234/jupiter)
#
# TSV: slug \t capa \t licencia \t ultimo_commit \t dias \t spec_en_codigo
set -u
. "$(cd "$(dirname "$0")/../lib" && pwd)/license_family.sh"
work=$(mktemp -d)

lic() { # slug -> class, via the SHARED tested classifier (P237).  The first build of this
        # instrument inlined an AGPL-first body grep and misread GPL-3.0 as AGPL-3.0.
  for n in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING COPYING.txt NOTICE; do
    o=$(curl -s --max-time 25 -w $'
%{http_code}' "https://raw.githubusercontent.com/$1/HEAD/$n" 2>/dev/null)
    [ "$(printf '%s' "$o" | tail -1)" = "200" ] || continue
    family_of "$(printf '%s' "$o" | sed '$d')"; return
  done
  echo "SIN-ARCHIVO"
}

for spec in "$@"; do
  slug=${spec%%:*}; capa=${spec#*:}
  l=$(lic "$slug")
  # life: default branch by NAME, read from the symref (pass 38 correction)
  br=$(git ls-remote --symref "https://github.com/$slug.git" HEAD 2>/dev/null \
       | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  d="-"; days="-"
  if [ -n "${br:-}" ]; then
    rm -rf "$work/r"; git init -q "$work/r" 2>/dev/null
    if git -C "$work/r" fetch -q --depth 1 "https://github.com/$slug.git" "$br" 2>/dev/null; then
      d=$(git -C "$work/r" log -1 --format=%cI FETCH_HEAD 2>/dev/null | cut -c1-10)
      [ -n "$d" ] && days=$(( ( $(date +%s) - $(date -d "$d" +%s) ) / 86400 ))
    fi
  fi
  # role: the spec version present in the TREE (file names + schema/constant payloads)
  s="-"
  if [ -d "$work/r/.git" ] && [ "$d" != "-" ]; then
    git -C "$work/r" checkout -q FETCH_HEAD 2>/dev/null
    s=$(cd "$work/r" && { find . -path ./.git -prune -o -type f -print 2>/dev/null \
          | grep -oiE 'xapi[-_]?[0-9]+\.[0-9]+(\.[0-9]+)?' ; \
          grep -rhoiE '"?(x[-_]?api[-_ ]?version)"?[":= ]+[0-9]+\.[0-9]+\.[0-9]+' . 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' ; \
        } | tr '[:upper:]' '[:lower:]' | sed 's/[-_]//g; s/^xapi//' | sort -u | paste -sd, -)
    [ -z "$s" ] && s="(sin version en el arbol)"
    cal=$(cd "$work/r" && grep -ril caliper . 2>/dev/null | grep -v '^./.git' | grep -vi 'readme\|\.md$' | wc -l)
    s="$s | caliper-en-codigo:$cal"
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$capa" "$l" "$d" "$days" "$s"
done
rm -rf "$work"
