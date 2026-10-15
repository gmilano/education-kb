#!/usr/bin/env bash
# p230 — ACTION TC. Re-probe EXISTENCE for every slug these shelves carry.
# A trending table that never re-probes accumulates ghosts; and p229's own ABSENT
# class turned out to be partly the harvester's (ACTION TD), so the sweep must run
# on the FIXED harvest, never on p228's truncated one.
#
#   usage: exists.sh <slugs-file> <out.tsv>
# Columns: slug  state  ref  head_sha
set -uo pipefail
SLUGS="$1"; OUT="$2"; : > "$OUT"
one() {
  local slug="$1" line ref head
  line=$(GIT_TERMINAL_PROMPT=0 git ls-remote --symref "https://github.com/${slug}" HEAD 2>/dev/null)
  if [[ -z "$line" ]]; then
    printf '%s\tABSENT\t-\t-\n' "$slug"; return
  fi
  ref=$(sed -n 's#^ref: refs/heads/\([^\t]*\)\tHEAD$#\1#p' <<<"$line" | head -1)
  head=$(awk '/\tHEAD$/{print $1; exit}' <<<"$line")
  printf '%s\tLIVE\t%s\t%s\n' "$slug" "${ref:-HEAD}" "${head:--}"
}
export -f one
cut -f1 "$SLUGS" | grep -v '^$' | xargs -P 6 -I{} bash -c 'one "$@"' _ {} >> "$OUT"
sort -o "$OUT" "$OUT"
