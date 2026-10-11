#!/usr/bin/env bash
# P118 evidence store. p115's rule is that the streams ARE the evidence and the
# TSV is a derivation, so the bytes must be committed. But 467 captured licence
# files are mostly byte-identical copies of the same handful of standard texts,
# and committing 6.5 MB of duplicated GPL would nearly double this repo.
#
# So the store is CONTENT-ADDRESSED: one copy per distinct licence text under its
# SHA-256, plus a manifest mapping every address to the SHA it committed. Every
# verdict in this pass stays re-derivable byte-for-byte -- `classify2.sh
# evidence/<sha>` reproduces it -- and the manifest additionally proves WHICH
# addresses commit identical licence files, which 467 separate copies did not.
set -u
mkdir -p evidence
: > evidence-manifest.tsv
for d in streams streams2; do
  [ -d "$d" ] || continue
  for f in "$d"/*; do
    [ -f "$f" ] || continue
    sha=$(sha256sum "$f" | cut -c1-64)
    base=$(basename "$f")
    slug=${base%@*@*}; slug=$(printf '%s' "$slug" | tr '%' '/')
    rest=${base#*@}; br=${rest%@*}; p=${rest##*@}
    [ -f "evidence/$sha" ] || cp "$f" "evidence/$sha"
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$p" "$sha" "$(wc -c < "$f" | tr -d ' ')" "$d"
  done
done | sort -u > evidence-manifest.tsv
printf 'captured files: %s\ndistinct licence texts: %s\n' \
  "$(wc -l < evidence-manifest.tsv)" "$(ls evidence | wc -l)"
