#!/bin/bash
# `ACTION KU` - p178. Measure a licence file through BOTH of this KB's byte-count
# channels at once, on the same bytes, in the same second.
#
# Channel A (FULL)     : curl | wc -c          - a pipe. Nothing is stripped.
# Channel B (STRIPPING): body=$(curl ...); printf '%s' "$body" | wc -c
#                        - command substitution deletes ALL trailing newlines
#                        before `printf` ever runs, so a file ending in one
#                        line feed is reported one byte short. This is the
#                        mechanism `ACTION KS` proved from its outputs; here it
#                        is exercised from its inputs.
#
# `md5` is read from the pipe channel, because `ACTION KS` made the digest this
# KB's licence identity and the byte count a weak corroborator.
#
# Usage: bash two_channels.sh <owner/repo> [<path>] [<branch>]
set -u
REPO="${1:?owner/repo}"
PATH_IN="${2:-}"
BRANCH="${3:-}"
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt COPYING"
[ -n "$PATH_IN" ] && PATHS="$PATH_IN"

if [ -z "$BRANCH" ]; then
  for b in main master; do
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 25 \
      "https://raw.githubusercontent.com/$REPO/$b/README.md")
    [ "$code" = "200" ] && { BRANCH="$b"; break; }
  done
  [ -z "$BRANCH" ] && BRANCH=main
fi

for p in $PATHS; do
  url="https://raw.githubusercontent.com/$REPO/$BRANCH/$p"
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 25 "$url")
  [ "$code" = "200" ] || continue
  tmp=$(mktemp); curl -s --max-time 25 "$url" >"$tmp"
  full=$(wc -c <"$tmp" | tr -d ' ')                 # channel A
  body="$(cat "$tmp")"                              # command substitution
  strip=$(printf '%s' "$body" | wc -c | tr -d ' ')  # channel B
  md5=$(md5sum <"$tmp" | cut -d' ' -f1)
  lastlf=NO; [ "$(tail -c1 "$tmp" | od -An -tx1 | tr -d ' \n')" = "0a" ] && lastlf=YES
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$REPO" "$BRANCH" "$p" "$code" "$full" "$strip" "$((full - strip))" "$md5:$lastlf"
  rm -f "$tmp"
  exit 0
done
printf '%s\t%s\t-\t404\t-\t-\t-\t-\n' "$REPO" "$BRANCH"
