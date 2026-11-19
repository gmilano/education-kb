#!/bin/sh
# `928-G1` — byte-read one grant URL CORRECTLY.
#
# Contract: print "<http_code>\t<bytes>\t<sha256_12>" for the EXACT bytes served.
#
# The body is written STRAIGHT TO A FILE and measured from the file. It is never
# carried through a shell variable, because `$( )` strips every trailing newline
# and `sed '$d'` on a combined body+status capture removes the body's last line.
# Either one changes the byte count and therefore the digest.
#
# Usage: byteread.sh <url> <outfile>
set -eu
url=$1; out=$2
code=$(curl -sS --max-time 25 -o "$out" -w '%{http_code}' "$url")
bytes=$(wc -c < "$out" | tr -d ' ')
sha=$(sha256sum "$out" | cut -c1-12)
printf '%s\t%s\t%s\n' "$code" "$bytes" "$sha"
