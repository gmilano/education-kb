#!/usr/bin/env bash
# `ACTION KY` — p179.  THE SECOND GATE, and the one that points at the DEFECT.
#
# `p178-byte-channel-census/check_channel.sh` flags the COUNT line:
#     bytes=$(printf '%s' "$body" | wc -c)
# `ACTION KY` measured the `12` sites it found and `11` of them cannot be repaired there at all —
# the payload is a shell variable by then and the trailing run died at the CAPTURE.  A gate that
# points at a line nobody can fix teaches the wrong repair, which is how `ACTION KY`'s limb `1`
# ("one mechanical commit closes it") came to be pre-registered at all.
#
# 🔵 `T283`: a gate must flag the line where the INFORMATION is lost, not the line where the loss
# becomes visible.
#
# THE RULE, in two steps, because one step is either blind or deafening:
#   1. find every variable assigned from a `curl` command substitution — the capture;
#   2. keep it ONLY if that variable's payload is later BYTE-COUNTED in the same file.
#
# Step 2 is what keeps this gate honest.  A capture that only ever feeds a CLASSIFIER is correct
# and is not flagged: `family_of`/`holder_of` are newline-insensitive and `payload_measure.sh`
# says so in its own `family_of_file` comment.  A capture that feeds `wc -c` is the defect.
#
# Captures of a STATUS CODE ONLY (`-o /dev/null -w '%{http_code}'`) are never payloads and are
# skipped in step 1.
#
# Exit 0 = no capture-then-size site.  Exit 1 = at least one.
set -u
ROOT="${1:-$(cd "$(dirname "$0")/../../.." && pwd)}"
ALLOW='compose/code/lib/payload_measure.sh|compose/code/p178-byte-channel-census/|compose/code/p179-capture-shape/|compose/code/lib/fetch_payload_to_file.sh'

found=0
while IFS= read -r hit; do
  f="${hit%%:*}"; rest="${hit#*:}"; l="${rest%%:*}"; line="${rest#*:}"
  printf '%s' "$f" | grep -qE "$ALLOW" && continue
  printf '%s' "$line" | sed 's/^[[:space:]]*//' | grep -q '^#' && continue
  # A capture that carries `-o` is not a payload capture AT ALL: the body went to a file and the
  # substitution holds only `%{http_code}`.  That is the CORRECT idiom — the one
  # `lib/fetch_payload_to_file.sh` now names — and the first cut of this gate flagged `46` sites
  # because it missed that.  🔵 `p120-unread-grant-resolution/probe.sh` (pass 120) was among the
  # false positives, which is the finding behind it: the right fetch shape has been in this
  # repository since p120 and `11` sites still do not use it. `T280` again, one layer up.
  printf '%s' "$line" | grep -qE -- '-o ("\$[A-Za-z_]|/dev/null|"?[A-Za-z_$])' && continue

  # Step 1: the captured variable name.
  var=$(printf '%s' "$line" | sed -n 's/^[[:space:]]*\(local[[:space:]]*\)\?\([A-Za-z_][A-Za-z0-9_]*\)=\$(.*/\2/p')
  [ -n "$var" ] || continue

  # Step 2: is any payload in this file byte-counted?  The captured variable is often renamed once
  # (`out` -> `content`, `out` -> `body`) before the count, so the file is the unit, not the name.
  grep -qE "wc -c" "$ROOT/$f" || continue

  printf 'CAPTURE-THEN-SIZE\t%s:%s\t%s\n' "$f" "$l" "$(printf '%s' "$line" | sed 's/^[[:space:]]*//' | cut -c1-96)"
  found=$((found + 1))
done < <(cd "$ROOT" && grep -rnE '^[[:space:]]*(local[[:space:]]+)?[A-Za-z_][A-Za-z0-9_]*=\$\(curl' \
  --include=*.sh compose/code ingest 2>/dev/null)

printf 'capture-then-size sites: %s\n' "$found"
[ "$found" -eq 0 ]
