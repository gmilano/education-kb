#!/usr/bin/env bash
# p117 — THE SECOND CHANNEL for a licence verdict.  Repaired at pass `179` by `ACTION KY`.
#
# WHAT CHANGED AND WHY.  Until p179 this instrument fetched with
#
#     body=$(curl -sS -f "$RAW/$slug/$br/$p")      # <- the trailing newline run dies HERE
#     …  "$(printf '%s' "$body" | wc -c)"          # <- and the count is low by that much
#
# `ACTION KS` (p177) found `8` of `12` published byte counts short, `ACTION KU` (p178) found this
# among `12` count sites, and `ACTION KY` (p179) measured that `11` of those `12` — this one
# included — CANNOT be repaired at the counting line, because by then the payload is a variable
# and the bytes are gone.  So the FETCH changed shape, not the count: the body goes to a file and
# the HTTP code comes back on stdout, which is `lib/fetch_payload_to_file.sh`.
#
# 🔵 The classifier still reads the capture, and that is correct, not a leftover:
# `payload_measure.sh` notes that `family_of`/`holder_of` are newline-insensitive, so every
# `spdx` verdict this instrument ever published stands.  Only the byte column moved.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
. "$HERE/../lib/fetch_payload_to_file.sh"
. "$HERE/../lib/payload_measure.sh"

TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  found=""
  for br in main master develop release; do
    for p in LICENSE LICENSE.txt LICENSE.md LICENCE COPYING LICENSE-MIT; do
      dest="$TMP/payload"
      fetch_raw_to_file "$slug" "$br" "$p" "$dest" >/dev/null || continue
      [ -s "$dest" ] || continue
      body=$(cat "$dest")                 # the CLASSIFIER's copy — never the size's
      spdx="UNKNOWN"
      case "$body" in
        *"Apache License"*"Version 2.0"*) spdx="Apache-2.0" ;;
        *"GNU AFFERO GENERAL PUBLIC LICENSE"*|*"GNU Affero General Public License"*) spdx="AGPL-3.0" ;;
        *"GNU LESSER GENERAL PUBLIC"*|*"GNU Lesser General Public"*) spdx="LGPL" ;;
        *"GNU GENERAL PUBLIC LICENSE"*|*"GNU General Public License"*) spdx="GPL" ;;
        *"Educational Community License"*) spdx="ECL-2.0" ;;
        *"MIT License"*|*"Permission is hereby granted, free of charge"*) spdx="MIT" ;;
        *"BSD"*) spdx="BSD" ;;
        *"Mozilla Public License"*) spdx="MPL-2.0" ;;
        *"CC0"*|*"Creative Commons"*) spdx="CC" ;;
      esac
      # The SIZE comes from the file, through the shared primitive.  `md5` travels with it so a
      # later pass can tell a re-measurement from a re-fetch (`T281`: a byte count is not an
      # identity).
      printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
        "$slug" "$br" "$p" "$spdx" "$(size_of_file "$dest")" "$(md5sum < "$dest" | cut -d' ' -f1)"
      found=1; break
    done
    [ -n "$found" ] && break
  done
  [ -z "$found" ] && printf '%s\t-\t-\tNO-LICENCE-FILE\t0\t-\n' "$slug"
done

# A working instrument must not exit non-zero: the final `[ -z "$found" ]` test made this one
# report failure on a fully successful sweep, which is a trap for whichever pass pipes it.
exit 0
