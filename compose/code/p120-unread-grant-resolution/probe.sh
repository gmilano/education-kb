#!/bin/sh
# p120 ACTION J - resolve the 22 UNREAD + permissive-claim addresses p118's
# 957-claim sweep could not read.
#
# Channel: raw.githubusercontent.com (the only OPEN GitHub channel this pass;
# api.github.com and github.com HTML both return http=403). The default branch
# for each address is the one MEASURED in p118's default-branch.2026-10-11.tsv
# and re-confirmed this pass through the search channel - NOT assumed to be main.
#
# Unlike p119's ACTION F, this does not assume the root grant is a prose index.
# It probes the whole conventional licence surface, so an address that measures
# NO-FILE here has been shown to carry no licence file at any conventional path
# on its default branch - which is a finding, not a measurement failure.
set -u
OUT=${1:-evidence}
mkdir -p "$OUT"
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md license LICENSE-CODIGO.md
LICENSE-DADOS.md LICENSE-CODE.md LICENSE-DATA.md COPYING COPYING.txt COPYRIGHT
NOTICE LICENSE.rst LICENSE-MIT LICENSE-APACHE DESCRIPTION package.json
composer.json README.md"
: > "$OUT/manifest.tsv"
while IFS="$(printf '\t')" read -r slug branch _stars _fork _arch; do
  [ -n "$slug" ] || continue
  for p in $PATHS; do
    f="$OUT/$(echo "$slug" | tr '/' '_')__$(echo "$p" | tr '/' '_')"
    code=$(curl -s -o "$f" -w '%{http_code}' --max-time 30 \
      "https://raw.githubusercontent.com/$slug/$branch/$p")
    if [ "$code" = "200" ]; then
      size=$(wc -c < "$f")
      printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$branch" "$p" "$code" "$size" >> "$OUT/manifest.tsv"
    else
      rm -f "$f"
      printf '%s\t%s\t%s\t%s\t0\n' "$slug" "$branch" "$p" "$code" >> "$OUT/manifest.tsv"
    fi
  done
done < meta.tsv
