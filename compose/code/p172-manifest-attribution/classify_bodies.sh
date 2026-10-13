#!/bin/bash
# ACTION JO — classify every blob in Sakai's licences/ manifest by the licence FAMILY its
# BODY carries, keyed by the component named in its FILENAME.
# Classifier is the shared hardened one (compose/code/lib/license_family.sh), per P237.
set -u
# P174-KC: the shared classifier is a SIBLING of this instrument. Resolve it from
# this script's own location, never from the clone path the pass happened to use.
. "$(cd "$(dirname "$0")/.." && pwd)/lib/license_family.sh"
DIR="$1"
printf 'file\tsha256_12\tbytes\tbody_family\n'
for f in "$DIR"/*; do
  b=$(basename "$f")
  case "$b" in *.pdf) printf '%s\t%s\t%s\t%s\n' "$b" "$(sha256sum "$f"|cut -c1-12)" "$(stat -c%s "$f")" "BINARY-PDF-NOT-READ"; continue;; esac
  payload=$(cat "$f" 2>/dev/null)
  printf '%s\t%s\t%s\t%s\n' "$b" "$(sha256sum "$f"|cut -c1-12)" "$(stat -c%s "$f")" "$(family_of "$payload")"
done
