#!/bin/bash
# Pass 66, action 3 of pass 65 — measure the jp-cos graph instead of sampling one record.
#
# Pass 65 built dumps.tsv by reading the file names out of index.html, and transcribed two of
# them WITHOUT their `.gz` suffix.  Those two are the largest files in the set, which is
# exactly why they are gzipped.  The 404 it recorded was real and the conclusion it drew from
# it -- "the complete graph only exists behind the blocked domains" -- was false.
#
# This script asks for every name EXACTLY as index.html spells it, and for the bare .ttl too,
# so the correction is visible rather than assumed.
B=https://raw.githubusercontent.com/jp-cos/jp-cos.github.io/HEAD
names=$(curl -s --max-time 30 "$B/index.html" | grep -oE '[A-Za-z-]+-[0-9]{8}\.ttl(\.gz)?' | sort -u)
printf '# archivo\tcodigo\tbytes\tnota\n'
for n in $names; do
  read -r code size < <(curl -s -o /dev/null -w '%{http_code} %{size_download}' --max-time 120 "$B/$n")
  printf '%s\t%s\t%s\t%s\n' "$n" "$code" "$size" "$(echo "$n" | grep -q '\.gz$' && echo 'gzip' || echo '-')"
  case "$n" in
    *.gz) bare="${n%.gz}"
          read -r c2 s2 < <(curl -s -o /dev/null -w '%{http_code} %{size_download}' --max-time 60 "$B/$bare")
          printf '%s\t%s\t%s\t%s\n' "$bare" "$c2" "$s2" 'el nombre SIN .gz — lo que el pase 65 sondeó' ;;
  esac
done
