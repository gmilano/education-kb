#!/bin/bash
# Read licence bytes at the default ref via raw.githubusercontent.com (the only gate with
# discriminating power through this proxy; api.github.com=403, curl -sI github.com=403 for all).
TSV="$1"
OUT="$2"
printf "repo\tref\tlicence_path\thttp\tbytes\tsha256_12\tspdx_guess\tapi_declared\tstars\n" > "$OUT"
awk -F'\t' 'NR>1 && $8=="no" && ($3=="MIT"||$3=="Apache-2.0"||$3 ~ /BSD/) {print $1"\t"$7"\t"$3"\t"$2}' "$TSV" | \
while IFS=$'\t' read -r repo ref api stars; do
  found=0
  for p in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING LICENSE-MIT license; do
    url="https://raw.githubusercontent.com/$repo/$ref/$p"
    code=$(curl -s -o /tmp/lic.$$ -w "%{http_code}" "$url")
    if [ "$code" = "200" ]; then
      bytes=$(wc -c < /tmp/lic.$$)
      sha=$(sha256sum /tmp/lic.$$ | cut -c1-12)
      # classify from operative text
      if   grep -qi "Apache License" /tmp/lic.$$ && grep -qi "Version 2.0" /tmp/lic.$$; then g="Apache-2.0"
      elif grep -qi "Permission is hereby granted, free of charge" /tmp/lic.$$; then g="MIT"
      elif grep -qi "Redistributions of source code must retain" /tmp/lic.$$; then
           if grep -qi "Neither the name" /tmp/lic.$$; then g="BSD-3-Clause"; else g="BSD-2-Clause"; fi
      elif grep -qi "GNU AFFERO" /tmp/lic.$$; then g="AGPL-3.0"
      elif grep -qi "GNU LESSER" /tmp/lic.$$; then g="LGPL"
      elif grep -qi "GNU GENERAL PUBLIC" /tmp/lic.$$; then g="GPL"
      else g="UNKNOWN-abstain"; fi
      printf "%s\t%s\t%s\t200\t%s\t%s\t%s\t%s\t%s\n" "$repo" "$ref" "$p" "$bytes" "$sha" "$g" "$api" "$stars" >> "$OUT"
      found=1; break
    fi
  done
  [ $found -eq 0 ] && printf "%s\t%s\t-\tNOT_FOUND\t-\t-\tNO-ROOT-GRANT\t%s\t%s\n" "$repo" "$ref" "$api" "$stars" >> "$OUT"
  rm -f /tmp/lic.$$
done
