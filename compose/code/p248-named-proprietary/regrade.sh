#!/bin/bash
# Re-grade the 183 FIRST-HAND repository payloads cached by p118 against both classifiers.
cd /tmp/education-kb || exit 1
lib="$1"; out="$2"
# shellcheck disable=SC1090
. "$lib"
: > "$out"
find compose/code/p118-licence-column-sweep/evidence -type f -regextype posix-extended \
     -regex '.*/[0-9a-f]{64}' | sort | while read -r f; do
  p=$(cat "$f")
  fam=$(osi_family_of "$p")
  if commercial_use_ok "$p"; then c=ALLOWED; else c=DENIED; fi
  printf '%s\t%s\t%s\n' "$(basename "$f")" "$fam" "$c" >> "$out"
done
wc -l < "$out"
