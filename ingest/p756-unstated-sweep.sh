#!/bin/bash
# p756 — ACTION p755-A.  The unstated-ledger sweep, with three instrument changes on p755's script.
#
#  1. ref = HEAD, not main+master.  HEAD resolves the TRUE default branch, so `develop`/`dev`/
#     `trunk` repos stop scoring as false NONE.  Proof: oat-sa/qti-sdk main=404, HEAD=200.
#     It also HALVES the request count (p755 did main+master x 5 names = 10; this does 5).
#  2. two legs.  Leg A = p755's 5 canonical names (comparable).  Leg B = 14 further names,
#     run only on leg-A misses, so the extra cost falls only where it can pay.
#  3. leg E, an EXISTENCE probe.  p755 emitted one "NONE" for both "repo has no licence file"
#     and "address is not readable", which are different defects with different fixes.
#
# KNOWN LIMIT, measured: raw.githubusercontent.com does NOT follow repository renames or org
# moves.  apereo/opencast -> 404 while opencast/opencast -> 200.  So UNREADABLE means
# "not readable AT THIS ADDRESS", never "does not exist".  git ls-remote would disambiguate
# and is credential-denied in this session (p755, p293).
#
# Classify from the TITLE BLOCK ONLY (P171) — but see T510: a title block is insufficient for
# notice-form GPL, untitled LGPL, and any BSD text (whose own words include "All rights
# reserved."), so every unresolved payload must get a FULL read before a verdict is published.
#
# usage: xargs -P 14 -I{} ./p756-unstated-sweep.sh {} < addresses.txt > results.tsv
a="$1"
work=$(mktemp -d); trap 'rm -rf "$work"' EXIT
emit(){ printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$a" "$1" "$2" "$3" "$4" "$5"; }
legA="LICENSE LICENSE.md LICENSE.txt LICENCE COPYING"
legB="LICENSE.rst LICENCE.md LICENCE.txt license LICENSE-MIT MIT-LICENSE MIT-LICENSE.txt COPYING.txt COPYING.md LICENSE-APACHE UNLICENSE LICENSE.html docs/LICENSE LICENSE/LICENSE"
for leg in A B; do
  [ "$leg" = A ] && names="$legA" || names="$legB"
  for n in $names; do
    code=$(curl -sS --max-time 10 -o "$work/p" -w "%{http_code}" "https://raw.githubusercontent.com/$a/HEAD/$n" 2>/dev/null)
    if [ "$code" = "200" ]; then
      sz=$(stat -c %s "$work/p")
      [ "$sz" -lt 40 ] && continue     # a <40 B payload is a POINTER, not a grant (T511)
      sha=$(sha256sum "$work/p" | cut -c1-12)
      t=$(head -c 4000 "$work/p" | tr -s ' \t\r\n' ' ' | cut -c1-90)
      emit "GRANT-$leg" "HEAD/$n" "$sz" "$sha" "$t"; exit 0
    fi
  done
done
for n in README.md readme.md README.rst README package.json .gitignore setup.py index.html; do
  code=$(curl -sS --max-time 10 -o /dev/null -w "%{http_code}" "https://raw.githubusercontent.com/$a/HEAD/$n" 2>/dev/null)
  if [ "$code" = "200" ]; then emit "NOGRANT" "exists:$n" "-" "-" "readable, no licence file at 19 probed paths"; exit 0; fi
done
emit "UNREADABLE" "-" "-" "-" "no 200 on 19 licence paths + 8 existence paths"
