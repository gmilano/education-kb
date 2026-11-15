#!/bin/bash
# p773 -- D9 fix: the grant filename list must be CASE-AWARE and wide.
# A missing lowercase license.txt produced a false NO-GRANT-AT-ROOT on ERPNext.
#
# p831 -- P834 REPAIR.  This script measured the payload through a captured body:
#   b=$(curl …);  printf '%s' "$b" | wc -c ;  printf '%s' "$b" | sha256sum
# `$( … )` strips the entire run of TRAILING NEWLINES, so every byte count this
# emitted was short by that run and every sha256 was of truncated content — a hash
# that can never be reproduced from the file it names, on a base whose shelves pin
# SHAs.  `agents/top.md` (p830) graded this site `CAPTURED-LIVE`, refused to pin the
# verdict down, and left the repair as the move that takes the gate green.  This is
# that repair: the payload is written to a FILE and the FILE is measured, so the
# trailing-newline run is counted.  No shell variable ever holds the body.
s="$1"; br="$2"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
for f in LICENSE LICENSE.md LICENSE.txt LICENSE.rst LICENCE LICENCE.md LICENCE.txt \
         license license.md license.txt licence licence.txt License License.md License.txt \
         COPYING COPYING.txt COPYING.md copying copying.txt COPYRIGHT NOTICE \
         LICENSE-MIT LICENSE-APACHE LICENSE-APACHE-2.0 LICENSE.APACHE2 \
         MIT-LICENSE MIT-LICENSE.txt LICENSE.BSD docs/LICENSE .github/LICENSE; do
  code=$(timeout 15 curl -sS -o /dev/null -w '%{http_code}' --max-time 15 \
         "https://raw.githubusercontent.com/$s/$br/$f" 2>/dev/null)
  if [ "$code" = "200" ]; then
    timeout 20 curl -sSL --max-time 20 -o "$tmp/payload" \
      "https://raw.githubusercontent.com/$s/$br/$f" 2>/dev/null
    printf '%s\t%s\t%s\t%s\n' "$s" "$f" \
           "$(wc -c < "$tmp/payload" | tr -d ' ')" \
           "$(sha256sum "$tmp/payload" | cut -c1-12)"
    exit 0
  fi
done
printf '%s\tNO-GRANT-AT-ROOT\t-\t-\n' "$s"
