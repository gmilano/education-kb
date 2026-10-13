#!/bin/bash
# `ACTION KU` - p178. THE GATE. This is the deliverable of the action, because
# the diagnosis was not the missing part.
#
# `P834` (pass 74, 2026-10-09) already named this defect, measured it at
# 0/1/3 trailing newlines -> 0/1/3 bytes low, and shipped the correct primitive
# `size_of_file` in `lib/payload_measure.sh`. `ACTION KS` (p177) then spent a
# pass re-deriving the same mechanism from its outputs. The vocabulary existed;
# nothing made its absence VISIBLE. That is what this gate does.
#
# It FAILS when an instrument sizes a payload through a command substitution.
# Two sites are allowlisted because they are deliberate CONTROLS and are named
# as such in their own source:
#   lib/payload_measure.sh  -> size_of_capture_BROKEN(), the preserved defect
#   p178-byte-channel-census/two_channels.sh -> channel B of the two-channel probe
#   p178-byte-channel-census/test_check_channel.sh -> the fixture that MEASURES the
#       mechanism at 0/1/3 trailing newlines. Caught by its own gate on the first run;
#       allowlisted rather than reworded, because the measurement IS the control (`T276`:
#       a gate reports its scope, and this one reported mine).
#
# Exit 0 = no unmarked stripping site. Exit 1 = at least one.
set -u
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
ALLOW='compose/code/lib/payload_measure.sh|compose/code/p178-byte-channel-census/two_channels.sh|compose/code/p178-byte-channel-census/test_check_channel.sh'
found=0
while IFS= read -r hit; do
  f="${hit%%:*}"; rest="${hit#*:}"; l="${rest%%:*}"
  printf '%s' "$f" | grep -qE "$ALLOW" && continue
  line="$(sed -n "${l}p" "$ROOT/$f")"
  printf '%s' "$line" | sed 's/^[[:space:]]*//' | grep -q '^#' && continue
  printf 'STRIPPING\t%s:%s\t%s\n' "$f" "$l" "$(printf '%s' "$line" | sed 's/^[[:space:]]*//')"
  found=$((found + 1))
done < <(cd "$ROOT" && grep -rnE "printf '%s' \"?\\\$[A-Za-z_{][A-Za-z0-9_}]*\"? *\| *wc -c|echo \"\\\$[A-Za-z_][A-Za-z0-9_]*\" *\| *wc -c" \
  --include=*.sh --include=*.py compose/code ingest 2>/dev/null)
printf 'unmarked stripping sites: %s\n' "$found"
[ "$found" -eq 0 ]
