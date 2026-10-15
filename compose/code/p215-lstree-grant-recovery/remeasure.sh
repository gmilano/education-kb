#!/usr/bin/env bash
# p215: re-measure every recovered grant blob BINARY-SAFE (curl -o file, wc -c),
# and record whether the blob is CRLF -- the mechanism behind this KB's byte conflicts.
set -u
cd "$(dirname "$0")"
OUT=qd_bytes.tsv
printf 'repo\tpath\tbytes_binary\tcr_count\tlines\teol\n' > "$OUT"
tmp=$(mktemp -d)
while IFS=$'\t' read -r repo grant path nb ch; do
  [ "$repo" = "repo" ] && continue
  # only single real paths; skip the combined manifest notations
  case "$path" in *+*) path="${path%%+*}";; esac
  f="$tmp/blob"
  code=$(curl -sS -m 45 -w '%{http_code}' -o "$f" \
         "https://raw.githubusercontent.com/$repo/HEAD/$path")
  if [ "$code" != "200" ]; then
    printf '%s\t%s\tHTTP_%s\t-\t-\t-\n' "$repo" "$path" "$code" >> "$OUT"; continue
  fi
  b=$(wc -c < "$f" | tr -d ' ')
  cr=$(tr -dc '\r' < "$f" | wc -c | tr -d ' ')
  ln=$(grep -c '' "$f" | tr -d ' ')
  if [ "$cr" -gt 0 ]; then eol="CRLF"; else eol="LF"; fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$path" "$b" "$cr" "$ln" "$eol" >> "$OUT"
done < qd_recoveries.tsv
rm -rf "$tmp"
echo "--- CRLF blobs (byte counts a text-mode read would understate) ---"
awk -F'\t' '$6=="CRLF"{printf "  %-46s %-28s %s B  (-%s if CR-stripped)\n",$1,$2,$3,$4}' "$OUT"
echo "--- totals ---"
awk -F'\t' 'NR>1{t++; if($6=="CRLF")c++} END{print "  blobs re-measured: "t"   CRLF: "c+0"   LF: "t-c}' "$OUT"
