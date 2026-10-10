#!/usr/bin/env bash
# grant-ladder-v4 (pass 92, 2026-10-10)
#
# Resolves a GitHub slug to (existence, default branch, HEAD SHA, licence read from the payload, bytes).
#
# WHY v4 EXISTS.  v3 did two things right -- it pinned SHAs and it made its FILENAME reach printable
# (`--count`, P953).  It did one thing wrong, and it is the thing this base has a registered rule for:
#
#   P237: A LICENCE CLASSIFIER MUST NOT BE FORKED TO BE FIXED.
#
# v3 inlined a fresh 30-line Python classifier instead of sourcing `../lib/license_family.sh`, the
# hardened shared classifier that has been in this repository since pass 77 and that carries the
# corrections of P171, P255, P299, P304, P308, P312, P453, P561, P854 and Gap 256.  The fork
# reproduced defects the shared file had already closed, and the cost was MEASURED, not feared:
#
#   * `oat-sa/tao-core`   -> v3 said LGPL-3.0.  The payload's title block says GNU GENERAL PUBLIC
#                            LICENSE, Version 2.  It is GPL-2.0.
#   * `portabilis/i-educar` -> v3 said LGPL-3.0.  Also GPL-2.0.
#
# The mechanism is P171 verbatim on a pair P171 never covered: the canonical GPL-2.0 PREAMBLE says
# "(Some other Free Software Foundation software is covered by the GNU Lesser General Public License
# instead.)" at byte 847 -- inside v3's 4.000 B window -- and v3 tested "gnu lesser" BEFORE
# "gnu general public".  So the cross-reference stole the payload.  Every canonical GPL-2.0 text
# carries that sentence, so the defect was universal, not incidental.
#
# `../lib/license_family.sh` classifies on the TITLE BLOCK and gets all five GNU rows right.  So v4
# has no classifier of its own.  It sources the shared one.  That is the whole point.
#
# AND v4 CARRIES A FIX BACK INTO THE SHARED FILE (P962), because P237 cuts both ways: reuse obliges
# you to repair, not to fork around.  lib's CC0 branch was UNREACHABLE for canonical CC0 text -- it
# was nested inside a gate requiring "Creative Commons" in the title-block window, and CC0's
# legalcode names Creative Commons exactly once, at offset 6.227, in the clause that DISCLAIMS it.
# Fixed in lib, with the real payload committed as a fixture.  See README.md.
set -u
export GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/true

HERE="$(cd "$(dirname "$0")" && pwd)"
# P237: source the hardened shared classifier.  Do not write a new one.
. "$HERE/../lib/license_family.sh"

# 24 candidate filenames -- the same reach v3 published, kept so the two are comparable.
NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt
COPYING COPYING.txt COPYING.md COPYING.LESSER
license license.txt license.md License License.md LICENSE.rst LICENSE.markdown
LICENSE-MIT LICENSE-APACHE LICENSE-BSD LICENSE-CODE COPYRIGHT COPYRIGHT.txt NOTICE"

# P961: THE BYTE FLOOR IS PART OF THE REACH, SO IT IS PRINTED WITH IT.
# v3 accepted a payload only at `bytes > 200` and published its reach as "24 filenames", so every v3
# negative was really "24 names AND nothing over 200 B" -- a denominator with an undisclosed second
# term.  This base owns a REAL 68-byte GPL title stub (`lib/fixtures-p613`, found via p613), so the
# floor was never hypothetical.  v4 accepts any non-empty payload and lets the classifier decide.
FLOOR=1
NCOUNT=$(echo $NAMES | tr ' ' '\n' | grep -c .)

ALL=0
if [ "${1:-}" = "--all" ]; then ALL=1; shift; fi
case "${1:-}" in
  --names) echo "$NCOUNT names, byte floor ${FLOOR} B"; echo $NAMES | tr ' ' '\n' | grep . ; exit 0 ;;
  --count) echo "$NCOUNT" ; exit 0 ;;
  --reach) echo "names=$NCOUNT byte-floor=${FLOOR}B classifier=lib/license_family.sh"; exit 0 ;;
esac

for slug in "$@"; do
  out=$(timeout 30 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$out" ]; then printf '%s\tABSENT\t-\t-\t-\t-\n' "$slug"; continue; fi
  ref=$(echo "$out" | awk '/^ref:/{print $2}' | sed 's#refs/heads/##')
  sha=$(echo "$out" | awk '!/^ref:/{print $1; exit}')
  found=""; every=""
  for n in $NAMES; do
    r=$(timeout 20 curl -s -o "/tmp/lic4.$$" -w "%{http_code} %{size_download}" \
        "https://raw.githubusercontent.com/$slug/$sha/$n" 2>/dev/null)
    code=${r%% *}; bytes=${r##* }
    if [ "$code" = "200" ] && [ "${bytes:-0}" -ge "$FLOOR" ] 2>/dev/null; then
      k=$(osi_family_of "$(cat "/tmp/lic4.$$")")
      [ -z "$found" ] && found="$n|$k|$bytes"
      every="$every $n=$k:${bytes}B"
      [ "$ALL" = "0" ] && break
    fi
  done
  rm -f "/tmp/lic4.$$"
  if [ -z "$found" ]; then
    printf '%s\tEXISTS\t%s\t%s\tNO-LICENCE-PAYLOAD/%s@%sB\t-\n' "$slug" "$ref" "${sha:0:7}" "$NCOUNT" "$FLOOR"
  elif [ "$ALL" = "1" ]; then
    nk=$(echo $every | tr ' ' '\n' | grep -c .)
    distinct=$(echo $every | tr ' ' '\n' | sed 's/.*=//;s/:.*//' | sort -u | tr '\n' ',' | sed 's/,$//')
    tag="SINGLE"; [ "$(echo "$distinct" | tr -cd ',' | wc -c)" -gt 0 ] && tag="SPLIT-GRANT"
    printf '%s\tEXISTS\t%s\t%s\t%s[%s]\t%s file(s):%s\n' "$slug" "$ref" "${sha:0:7}" "$tag" "$distinct" "$nk" "$every"
  else
    printf '%s\tEXISTS\t%s\t%s\t%s\t%s:%sB\n' "$slug" "$ref" "${sha:0:7}" \
      "$(echo "$found"|cut -d'|' -f2)" "$(echo "$found"|cut -d'|' -f1)" "$(echo "$found"|cut -d'|' -f3)"
  fi
done
