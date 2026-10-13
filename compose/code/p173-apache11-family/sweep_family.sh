#!/bin/bash
# ACTION JU (p173) — classify every file in a directory tree of licence BODIES with the
# SHARED hardened classifier, so a change to the classifier can be diffed verdict by verdict.
#
# Why this exists and not p172's classify_bodies.sh: that script sources the lib by the
# ABSOLUTE path /tmp/education-kb/... and this pass's clone is at /home/user/education-kb,
# so it cannot run here at all (T247).  Path is resolved RELATIVE to this script.
# Usage: ./sweep_family.sh <dir>   (recursive; one row per file)
set -u
. "$(dirname "$0")/../lib/license_family.sh"
DIR="$1"
printf 'file\tsha256_12\tbytes\tbody_family\n'
find "$DIR" -type f | LC_ALL=C sort | while read -r f; do
  b=${f#"$DIR"/}
  case "$b" in *.pdf) printf '%s\t%s\t%s\t%s\n' "$b" "$(sha256sum "$f"|cut -c1-12)" "$(stat -c%s "$f")" "BINARY-PDF-NOT-READ"; continue;; esac
  payload=$(cat "$f" 2>/dev/null)
  printf '%s\t%s\t%s\t%s\n' "$b" "$(sha256sum "$f"|cut -c1-12)" "$(stat -c%s "$f")" "$(family_of "$payload")"
done
