#!/usr/bin/env bash
# `p444/shard.sh` — run `probe.sh` over a slug list in N parallel shards and merge.
#
# Serial, the 321-slug shelf sweep measured ~20 s/slug (clone-bound, not CPU-bound) = ~1.8 h.
# Sharded 6 ways it is ~18 min, and the shards are independent because each writes its OWN
# output directory: the first attempt at this sweep had TWO probes writing one `probe.tsv`
# and the interleaving is why that evidence was discarded rather than published.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SLUGS="${1:?need a slug file}"
OUT="${2:?need an output dir}"
N="${3:-6}"

mkdir -p "$OUT"
grep -vE '^[[:space:]]*(#|$)' "$SLUGS" > "$OUT/clean.txt"
total=$(wc -l < "$OUT/clean.txt")
split -n "l/$N" -d "$OUT/clean.txt" "$OUT/shard-"

pids=()
for f in "$OUT"/shard-*; do
  [ -f "$f" ] || continue
  bash "$HERE/probe.sh" "$f" "$OUT/$(basename "$f")-out" > "$OUT/$(basename "$f").log" 2>&1 &
  pids+=("$!")
done
fail=0
for p in "${pids[@]}"; do wait "$p" || fail=$((fail+1)); done

# merge: one header, then every shard's rows
head -1 "$(ls -d "$OUT"/shard-*-out/probe.tsv | head -1)" > "$OUT/probe.tsv"
for t in "$OUT"/shard-*-out/probe.tsv; do tail -n +2 "$t" >> "$OUT/probe.tsv"; done
mkdir -p "$OUT/payloads"
for d in "$OUT"/shard-*-out/payloads; do cp -n "$d"/* "$OUT/payloads/" 2>/dev/null; done

got=$(tail -n +2 "$OUT/probe.tsv" | cut -f1 | sort -u | wc -l)
echo "merged $OUT/probe.tsv  (slugs asked: $total, slugs reported: $got, shard failures: $fail)"
[ "$total" -eq "$got" ] || { echo "INCOMPLETE SWEEP: asked $total, reported $got" >&2; exit 3; }
