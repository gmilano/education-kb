#!/bin/sh
# `Gap 434-B`'s real remedy — a RECENCY channel that IS reproducible from `make`.
#
# `p434` registered that no star count on these shelves can be obtained from inside a
# run, and prescribed either an egress allowlist entry for `api.github.com` or a standing
# rule that stars are advisory colour.  Re-measured on 2026-10-25 (p435): `api.github.com`
# is NOT dead — it answers 200 on `/rate_limit` and on an ATTACHED repository — and the
# 403 on a third-party repository is a per-repository AUTHORIZATION refusal whose body
# says so.  So no allowlist entry can fix it for 1 449 third-party addresses.
#
# What IS reachable for any public address, with no credentials and no API:
#
#   git clone --depth 1 --bare --filter=tree:0   ->  the HEAD COMMIT object alone
#
# measured here: ~0.5 s and ~270 KB per address, against ~20 MB for a plain --depth 1.
# That yields the HEAD committer date, which is a BETTER promotion discriminator than a
# star count for this base's own reasons (`Trend 9` — a permissive licence has a shelf
# life; `Trend 13` — the supply has a currency problem).
#
# ONLINE.  Never in `hooks`.
# RESUMABLE: a slug already in $OUT is skipped.
#
# usage: head_dates.sh <slugs-file> <out-tsv> [parallelism]
set -u
SLUGS="$1"; OUT="$2"; PAR="${3:-16}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT INT TERM
touch "$OUT"
cut -f1 "$OUT" | sort -u > "$TMP/done.txt"
sort -u "$SLUGS" > "$TMP/all.txt"
comm -23 "$TMP/all.txt" "$TMP/done.txt" > "$TMP/todo.txt"
TOTAL=$(wc -l < "$TMP/todo.txt")
echo "head_dates: $TOTAL to probe, parallelism=$PAR" >&2
[ "$TOTAL" -eq 0 ] && exit 0
one() {
  slug="$1"; work="$2"
  d="$work/$(echo "$slug" | tr '/' '_')"
  rm -rf "$d"
  if git clone --quiet --depth 1 --bare --filter=tree:0 \
       "https://github.com/$slug" "$d" >/dev/null 2>&1; then
    line=$(git -C "$d" log -1 --format='%H%x09%cI%x09%aI' 2>/dev/null)
    if [ -n "$line" ]; then
      printf '%s\t%s\n' "$slug" "$line"
    else
      printf '%s\t-\t-\t-\n' "$slug"
    fi
  else
    printf '%s\tCLONE-FAILED\t-\t-\n' "$slug"
  fi
  rm -rf "$d"
}
mkdir -p "$TMP/shards" "$TMP/work"
split -n "l/$PAR" -d -a 3 "$TMP/todo.txt" "$TMP/shards/s"
i=0
for s in "$TMP"/shards/s*; do
  [ -s "$s" ] || continue
  i=$((i+1))
  (
    while IFS= read -r slug; do
      [ -n "$slug" ] && one "$slug" "$TMP/work"
    done < "$s"
  ) >> "$OUT.part.$i" 2>/dev/null &
done
wait
cat "$OUT".part.* >> "$OUT" 2>/dev/null
rm -f "$OUT".part.*
echo "head_dates: $(wc -l < "$OUT") rows in $OUT" >&2
