#!/usr/bin/env bash
# run.sh -- the census, N chunks wide. Emits one TSV on stdout, in list order.
#
# P113-N  PARALLELISM IS BY PROCESS, NEVER BY EXPORTED FUNCTION. p1040 lost
#   1 077 rows to a silence because `probe_one` ran inside an `xargs` subshell
#   and one function it called was missing from `export -f`, and then the guard
#   written to catch exactly that missed it too. This wrapper splits the ADDRESS
#   LIST and runs the unmodified single-threaded `bind.sh` once per chunk, so
#   there is no shared shell state to forget to export. Chunks are written to
#   numbered files and concatenated in chunk order, so the output is BYTE
#   IDENTICAL to a serial run and the parallelism cannot reorder a figure.
set -uo pipefail
cd "$(dirname "$0")"
list="${1:-addresses.txt}"
ways="${2:-6}"
out="${P113_OUT:-${TMPDIR:-/tmp}/p113chunks}"
rm -rf "$out"; mkdir -p "$out"

grep -v '^#' "$list" | grep -v '^$' > "$out/all.txt"
total=$(wc -l < "$out/all.txt")
per=$(( (total + ways - 1) / ways ))
split -l "$per" -d -a 2 "$out/all.txt" "$out/chunk."

for c in "$out"/chunk.*; do
  ( P113_WORK="$out/work.$(basename "$c")" ./bind.sh "$c" > "$c.tsv" 2> "$c.err" ) &
done
wait

head -1 "$out/chunk.00.tsv"
for c in "$out"/chunk.*.tsv; do tail -n +2 "$c"; done
cat "$out"/chunk.*.err >&2
