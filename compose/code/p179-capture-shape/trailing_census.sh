#!/usr/bin/env bash
# `ACTION KY` — p179.  TRAILING-RUN CENSUS over a corpus that is already on disk.
#
# Why this exists as an instrument and not as a one-liner: `ACTION KS` (p177) stated the error as
# "+1 byte", and `lib/payload_measure.sh` corrected that to "the ENTIRE trailing run" from
# fixtures it built itself (0/1/3).  Neither had measured a REAL corpus, so this KB had no
# evidence that a run longer than 1 occurs in the wild.  It does.
#
# Columns: payload, FULL channel (`wc -c < file`), STRIPPING channel (capture then count), and
# the delta — which IS the trailing-newline run, by `trailing_newlines()`'s definition.
#
# Usage: bash trailing_census.sh <dir>
set -u
dir="${1:-}"
[ -d "$dir" ] || { echo "p179: REFUSED — '$dir' is not a directory; a census over nothing is not a census" >&2; exit 2; }

printf 'payload\tfull\tstripping\ttrailing_run\n'
n=0; nonzero=0; gt1=0
for f in "$dir"/*; do
  [ -f "$f" ] || continue
  full=$(wc -c < "$f" | tr -d ' ')
  cap=$(cat "$f"); strip=$(printf '%s' "$cap" | wc -c | tr -d ' ')   # the P834 channel, on purpose
  d=$((full - strip))
  printf '%s\t%s\t%s\t%s\n' "$(basename "$f")" "$full" "$strip" "$d"
  n=$((n + 1))
  [ "$d" -gt 0 ] && nonzero=$((nonzero + 1))
  [ "$d" -gt 1 ] && gt1=$((gt1 + 1))
done
printf '# p179: %s payloads, %s with a trailing run, %s with a run LONGER THAN 1\n' "$n" "$nonzero" "$gt1"
