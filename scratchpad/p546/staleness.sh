#!/bin/bash
# p546 — Gap 544-C: a staleness field for every shelf address.
#
# p545 touched all 162 addresses and still could not date one, because
# `ls-remote` serves a sha and not a date. A BLOBLESS BARE clone fetches the
# commit object without any file contents, so the date is one cheap network op
# per repo and the disk cost is a few KB rather than a working tree.
#
# Usage: staleness.sh <slugs-file> <outdir>
set -u
SLUGS="$1"; OUT="$2"
mkdir -p "$OUT"
TSV="$OUT/staleness.tsv"
printf 'slug\tbranch\thead_sha\tcommitted_iso\tage_days\tstatus\n' > "$TSV"
NOW=$(date +%s)

while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  d="$OUT/bare/$(echo "$slug" | tr / _).git"
  rm -rf "$d"
  if ! git clone --bare --depth 1 --filter=blob:none --quiet \
        "https://github.com/$slug" "$d" 2>/dev/null; then
    printf '%s\t-\t-\t-\t-\tCLONE-FAILED\n' "$slug" >> "$TSV"
    continue
  fi
  br=$(git --git-dir="$d" symbolic-ref --short HEAD 2>/dev/null || echo '-')
  sha=$(git --git-dir="$d" rev-parse HEAD 2>/dev/null || echo '-')
  iso=$(git --git-dir="$d" log -1 --format=%cI 2>/dev/null || echo '-')
  if [ "$iso" = "-" ] || [ -z "$iso" ]; then
    printf '%s\t%s\t%s\t-\t-\tNO-DATE\n' "$slug" "$br" "${sha:0:12}" >> "$TSV"
  else
    ts=$(date -d "$iso" +%s 2>/dev/null || echo 0)
    age=$(( (NOW - ts) / 86400 ))
    printf '%s\t%s\t%s\t%s\t%s\tOK\n' "$slug" "$br" "${sha:0:12}" "$iso" "$age" >> "$TSV"
  fi
  rm -rf "$d"          # the date is extracted; keep no repository on disk
done < "$SLUGS"

echo "dated: $(awk -F'\t' '$6=="OK"' "$TSV" | wc -l) / $(( $(wc -l < "$TSV") - 1 ))"
echo "failed: $(awk -F'\t' '$6!="OK" && NR>1' "$TSV" | wc -l)"
