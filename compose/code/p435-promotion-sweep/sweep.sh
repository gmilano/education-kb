#!/bin/sh
# `Gap 434-A` — grade the UNPROMOTED population, so `gate-promotion`'s grade table is no
# longer 7 rows against a 2 457-address denominator.
#
# This is a RUNNER, not a new classifier.  It reuses, unchanged:
#   * the address population  — `p434-promotion-gate`'s own census functions
#   * the grant ladder        — `p228-shelf-gate/fetch_grants.sh` (main|master x 8 paths)
#   * the family classifier   — `p228-shelf-gate/classify_grant.py`
# per T108: run this base's instruments, do not re-improvise them.
#
# ONLINE.  Never in `hooks` — `raw.githubusercontent.com` is the only reachable grant
# channel here (`Gap 433-C`), and api.github.com is 403, so NO STAR COLUMN IS EMITTED
# (`Gap 434-B`: a star count is advisory colour, never a gate predicate).
#
# RESUMABLE: a slug already present in $RESULTS is skipped, so a killed run resumes.
#
# usage: sweep.sh <slugs-file> <work-dir> [parallelism]
set -u
SLUGS="$1"; WORK="$2"; PAR="${3:-12}"
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
LADDER="$HERE/../p228-shelf-gate/fetch_grants.sh"
RESULTS="$WORK/raw-results.tsv"
BODIES="$WORK/bodies"
mkdir -p "$WORK" "$BODIES"
: > "$WORK/todo.txt"
touch "$RESULTS"
# resume: only slugs with no row yet
cut -f1 "$RESULTS" | sort -u > "$WORK/done.txt"
sort -u "$SLUGS" > "$WORK/all.txt"
comm -23 "$WORK/all.txt" "$WORK/done.txt" > "$WORK/todo.txt"
TOTAL=$(wc -l < "$WORK/todo.txt")
echo "sweep: $TOTAL to probe ($(wc -l < "$WORK/done.txt") already done), parallelism=$PAR" >&2
[ "$TOTAL" -eq 0 ] && exit 0
rm -rf "$WORK/shards"; mkdir -p "$WORK/shards"
split -n "l/$PAR" -d -a 3 "$WORK/todo.txt" "$WORK/shards/s"
for s in "$WORK"/shards/s*; do
  [ -s "$s" ] || continue
  sh "$LADDER" "$s" "$BODIES" >> "$RESULTS.$$.$(basename "$s")" 2>/dev/null &
done
wait
cat "$RESULTS".$$.* >> "$RESULTS" 2>/dev/null
rm -f "$RESULTS".$$.*
echo "sweep: $(wc -l < "$RESULTS") rows in $RESULTS" >&2
