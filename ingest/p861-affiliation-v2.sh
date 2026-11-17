#!/bin/bash
# p861 v2 -- the affiliation channel, with the two defects v1 caught ON ITSELF declared and fixed.
#
# D861-A  the `holder` step accepted the LICENCE TEXT'S OWN copyright line.  GPL-3.0 and
#         AGPL-3.0 open `Copyright (C) 2007 Free Software Foundation, Inc.`, so v1 placed three
#         copyleft repositories at the FSF -- a false affiliation produced by the highest-
#         precedence step.  Fix: a boilerplate holder is skipped, never read as the project's.
# D861-B  no axis read a DOMAIN.  An institutional e-mail or URL in the README (`.edu`,
#         `.ac.XX`, `.edu.XX`) is a stated affiliation of exactly the class the gap allowed,
#         and it is the commonest way a university project names itself.
#
# Offline: runs against clones v1 already fetched.  No network.
set -u
W="${W:-/tmp/claude-0/p861/clones}"
BOILER='Free Software Foundation|Apache Software Foundation|Open Source Initiative|<COPYRIGHT HOLDER>|copyright holder'
INST='Universit|Universidad|Universidade|Hochschule|Institute of Technology|Polytechnic|College|Ministry|Ministerio|Foundation|Corporation|Laborator|Institut'
printf 'repo\taxis\tevidence\tregion_claim\n'
while read -r repo; do
  [ -z "$repo" ] && continue
  d="$W/$(echo "$repo" | tr '/' '_')"
  [ -d "$d" ] || { printf '%s\tNO-CLONE\t-\t-\n' "$repo"; continue; }
  axis='-'; ev='-'
  ho=$(cat "$d/.licence" 2>/dev/null | grep -i -m1 'copyright' | sed 's/^ *//' | cut -c1-70)
  if [ -n "$ho" ] && ! echo "$ho" | grep -qiE "$BOILER"; then
    if echo "$ho" | grep -qE "$INST"; then
      axis='holder'; ev=$(echo "$ho" | sed 's/.*[Cc]opyright[^A-Za-z0-9]*//' | cut -c1-55)
    fi
  fi
  if [ "$axis" = '-' ]; then
    cf=$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null | grep -ixE 'CITATION\.cff' | head -1)
    if [ -n "$cf" ]; then
      a=$(git -C "$d" show "HEAD:$cf" | grep -iE '^\s*(affiliation|institution):' | head -1 | sed 's/.*: *//; s/^["'"'"']//; s/["'"'"']$//' | cut -c1-55)
      [ -n "$a" ] && { axis='citation'; ev="$a"; }
    fi
  fi
  rp=$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null | grep -ixE 'README(\.(md|rst|txt))?' | head -1)
  if [ "$axis" = '-' ] && [ -n "$rp" ]; then
    a=$(git -C "$d" show "HEAD:$rp" | head -c 8000 | grep -oiE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(edu|ac\.[a-z]{2}|edu\.[a-z]{2})|https?://[A-Za-z0-9.-]+\.(edu|ac\.[a-z]{2}|edu\.[a-z]{2})[^ )]*' | head -1 | cut -c1-55)
    [ -n "$a" ] && { axis='domain'; ev="$a"; }
  fi
  if [ "$axis" = '-' ] && [ -n "$rp" ]; then
    a=$(git -C "$d" show "HEAD:$rp" | head -c 8000 | grep -oE "[A-Z][A-Za-z.&'-]*( [A-Z][A-Za-z.&'-]*){0,4} ($INST)[a-z]*|($INST)[a-z]* (of|de) [A-Z][A-Za-z.'-]*( [A-Z][A-Za-z.'-]*){0,3}" | head -1 | cut -c1-55)
    [ -n "$a" ] && { axis='readme'; ev="$a"; }
  fi
  printf '%s\t%s\t%s\t-\n' "$repo" "$axis" "$ev"
done
