#!/usr/bin/env bash
# `ACTION KY` — p179.  THE CLASS-`C` PROOF, and the reason this pass does not simply "add the
# trailing run back" to the published figures.
#
# `ACTION KS` (p177) and `ACTION KU` (p178) both treated the defect as LOSS: the count comes back
# low by the trailing run, so add the run back.  That remedy is implementable on class `A` (the
# file is still there to re-measure) and on class `B` (re-fetch to a file).  🔴 ON CLASS `C` IT IS
# NOT IMPLEMENTABLE AT ALL, because the channel is not lossy, it is AMBIGUOUS: two payloads whose
# sizes differ come back as the SAME BYTES, so there is no run to add back.
#
# The class-`C` idiom, verbatim from `p250`, `p170`, `p206`, `p211`, `p122` and `p324`:
#
#     out=$(curl -s -w "\n%{http_code}" URL)      # capture 1
#     code=$(printf '%s' "$out" | tail -1)
#     content=$(printf '%s' "$out" | sed '$d')    # capture 2  <- the run dies HERE
#     bytes=$(printf '%s' "$content" | wc -c)     # <- the line the p178 gate flags
#
# This instrument runs that exact pipeline with the network replaced by a local fixture, so the
# result is reproducible offline and in any order (`P355`).  No `curl`, no host, no allowlist.
#
# Usage: bash ambiguity_proof.sh
set -u
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT

# Three payloads that differ ONLY in their trailing newline run: 0, 1 and 3.
printf 'MIT License\n\nCopyright (c) 2026 Nobody' > "$tmp/run0"
printf 'MIT License\n\nCopyright (c) 2026 Nobody\n' > "$tmp/run1"
printf 'MIT License\n\nCopyright (c) 2026 Nobody\n\n\n' > "$tmp/run3"

printf 'fixture\ttrue_size\tclassC_recovered_size\tclassC_md5_of_recovery\tfull_channel_size\n'
for r in run0 run1 run3; do
  f="$tmp/$r"
  true_size=$(wc -c < "$f" | tr -d ' ')

  # ── the class-C channel, byte for byte, with the fixture standing in for the response body ──
  out=$(printf '%s200' "$(cat "$f")
")                                            # capture 1: body + "\n" + http_code
  content=$(printf '%s' "$out" | sed '$d')    # capture 2: strip the status line back off
  c_size=$(printf '%s' "$content" | wc -c | tr -d ' ')
  c_md5=$(printf '%s' "$content" | md5sum | cut -d' ' -f1)

  # ── the FULL channel, for contrast: the primitive from lib/payload_measure.sh ──
  full=$(wc -c < "$f" | tr -d ' ')

  printf '%s\t%s\t%s\t%s\t%s\n' "$r" "$true_size" "$c_size" "$c_md5" "$full"
done

# The verdict, computed rather than asserted in prose.
s0=$(printf '%s' "$(printf '%s200' "$(cat "$tmp/run0")
")" | sed '$d' | md5sum | cut -d' ' -f1)
s1=$(printf '%s' "$(printf '%s200' "$(cat "$tmp/run1")
")" | sed '$d' | md5sum | cut -d' ' -f1)
s3=$(printf '%s' "$(printf '%s200' "$(cat "$tmp/run3")
")" | sed '$d' | md5sum | cut -d' ' -f1)

echo
if [ "$s0" = "$s1" ] && [ "$s1" = "$s3" ]; then
  echo "p179 VERDICT: AMBIGUOUS — payloads of 3 different sizes recover to ONE identical byte"
  echo "              string. The trailing run is not recoverable from the capture, so no"
  echo "              arithmetic correction to a class-C figure can be right for all three."
  echo "              A class-C figure can only be repaired by RE-FETCHING to a file."
  exit 0
else
  echo "p179 VERDICT: DISTINGUISHABLE — the class-C channel preserves the run after all, and this"
  echo "              pass's reading of the 6 class-C sites is WRONG. Investigate before publishing."
  exit 1
fi
