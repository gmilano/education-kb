#!/bin/sh
# p120 ACTION J - for each of the 22 UNREAD + permissive-claim addresses, name
# the grant the repository ACTUALLY carries, and say through which channel.
#
# The resolution order matters and is the point of the instrument:
#   1. a licence FILE at a conventional root path, classified by classify3.sh
#   2. a licence FILE at the NON-conventional path the repo's own README names
#   3. the language manifest the repo's own ecosystem treats as authoritative
#      (DESCRIPTION for R, readme.txt for a WordPress plugin)
#   4. a README prose statement, which is a CLAIM BY THE AUTHOR, not a grant
#   5. nothing - which is NO-GRANT, a finding and not a failed measurement
#
# Tiers 4 and 5 are reported as such and never folded into tiers 1-3. A badge
# or a README sentence pointing at a LICENSE file that returns 404 is recorded
# as DANGLING, because that is what it is.
set -u
E=${1:-evidence}; E2=${2:-evidence2}
: > verdict.2026-10-11.tsv
cls() { ./classify3.sh "$1" 2>/dev/null; }
emit() { printf '%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" >> verdict.2026-10-11.tsv; }
f() { echo "$E/$(echo "$1" | tr '/' '_')__$2"; }
f2() { echo "$E2/$(echo "$1" | tr '/' '_')__$(echo "$2" | tr '/' '_')"; }

while IFS="$(printf '\t')" read -r slug branch _s _f _a; do
  [ -n "$slug" ] || continue
  tier=''; grant=''; chan=''
  # tier 1 - conventional root licence file, longest first so a stub loses
  for p in LICENSE.md LICENSE LICENCE.md LICENCE LICENSE.txt COPYING; do
    fp=$(f "$slug" "$p"); [ -s "$fp" ] || continue
    c=$(cls "$fp")
    case "$c" in GRANT-IN-MANIFEST|UNKNOWN|EMPTY) continue ;; esac
    tier=1; grant="$c"; chan="file:$p"; break
  done
  # tier 1b - a SPLIT GRANT. The root file is a prose index and the real grants
  # sit in siblings it names (LICENSE-CODIGO/DADOS for the Brazilian pair,
  # LICENSE-CODE/DATA in English). A split grant has no single answer, so the
  # parts are reported together - never collapsed to the permissive half, which
  # is exactly the error `P119-PAT-0` found inside a recommendation.
  if [ -z "$tier" ]; then
    parts=''
    for p in LICENSE-CODIGO.md LICENSE-DADOS.md LICENSE-CODE.md LICENSE-DATA.md; do
      fp=$(f "$slug" "$p"); [ -s "$fp" ] || continue
      c=$(cls "$fp"); case "$c" in UNKNOWN|EMPTY) c="UNKNOWN($p)" ;; esac
      parts="${parts:+$parts + }$p=$c"
    done
    [ -n "$parts" ] && { tier=1b; grant="SPLIT-GRANT:$parts"; chan="sibling-files"; }
  fi
  # tier 1c - a PROSE INDEX that names its grants inline rather than by sibling
  # file. The index is read for the licence names it asserts, and every name it
  # asserts is reported, including the NonCommercial ones. A prose index that
  # mentions a NonCommercial or gated tier is flagged, because the permissive
  # half is the half a reader remembers.
  if [ -z "$tier" ]; then
    for p in LICENSE.md LICENSE; do
      fp=$(f "$slug" "$p"); [ -s "$fp" ] || continue
      names=$(grep -oiE 'CC BY-NC-SA 4\.0|CC BY-NC|CC BY 4\.0|CC0|\bMIT\b|Apache-2\.0|Apache License|AGPL-3\.0|GPL-3\.0|BSD' "$fp" \
              | tr 'a-z' 'A-Z' | sed 's/APACHE LICENSE/APACHE-2.0/' | sort -u | paste -sd'+' -)
      [ -n "$names" ] || continue
      tier=1c; chan="prose-index:$p"
      if printf '%s' "$names" | grep -q 'NC'; then
        grant="PROSE-INDEX-NONCOMMERCIAL-TIER:$names"
      else
        grant="PROSE-INDEX:$names"
      fi
      break
    done
  fi
  # tier 2 - the non-conventional path the README names
  if [ -z "$tier" ]; then
    for p in docs/License.txt; do
      fp=$(f2 "$slug" "$p"); [ -s "$fp" ] || continue
      c=$(cls "$fp"); case "$c" in UNKNOWN|EMPTY) continue ;; esac
      tier=2; grant="$c"; chan="readme-named-file:$p"; break
    done
  fi
  # tier 3 - the ecosystem's authoritative manifest
  if [ -z "$tier" ]; then
    d=$(f "$slug" DESCRIPTION)
    if [ -s "$d" ]; then
      l=$(grep -i '^License:' "$d" | head -1 | sed -e 's/^[Ll]icense:[[:space:]]*//' -e 's/\r$//' -e 's/[[:space:]]*$//')
      [ -n "$l" ] && { tier=3; grant="MANIFEST:$l"; chan="DESCRIPTION"; }
    fi
    r=$(f2 "$slug" readme.txt)
    if [ -z "$tier" ] && [ -s "$r" ]; then
      l=$(grep -i '^License:' "$r" | head -1 | sed -e 's/^[Ll]icense:[[:space:]]*//' -e 's/\r$//' -e 's/[[:space:]]*$//')
      [ -n "$l" ] && { tier=3; grant="MANIFEST:$l"; chan="wp-readme.txt"; }
    fi
  fi
  # tier 4/5 - author claim in README, or nothing at all
  if [ -z "$tier" ]; then
    rm=$(f "$slug" README.md)
    sect=''
    [ -s "$rm" ] && sect=$(awk '/^#+[[:space:]]*[Ll]icen[cs]/{f=1;next} f&&/^#+[[:space:]]/{exit} f{print}' "$rm")
    if [ -s "$rm" ] && { printf '%s' "$sect" | grep -qiE 'MIT|Apache|BSD|GPL|CC BY' \
         || grep -qiE 'licen[cs]ed under|under the [A-Za-z0-9.-]+ licen[cs]e|^License:|badge/[Ll]icense' "$rm"; }; then
      tier=4; chan="README-prose"
      grant="AUTHOR-CLAIM-NO-FILE"
      grep -qiE 'See the LICENSE file|\]\(LICENSE\)|\(#.*licen' "$rm" && grant="AUTHOR-CLAIM-DANGLING-POINTER"
    else
      tier=5; grant="NO-GRANT-FOUND"; chan="none"
    fi
  fi
  emit "$slug" "$branch" "$grant" "tier$tier:$chan"
done < meta.tsv
