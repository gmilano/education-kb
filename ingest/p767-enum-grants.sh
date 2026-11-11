#!/usr/bin/env bash
# p767 grant enumerator. Replaces the path-GUESS matrix with a path ENUMERATION.
# Closes T665 (non-root blind spot) and serves ACTION p766-D(ii) (path-scoped families).
# usage: enum-grants.sh owner/repo outdir
set -u
ADDR="$1"; OUT="$2"; D="$OUT/$(echo "$ADDR" | tr '/' '~')"
rm -rf "$D"; mkdir -p "$D"
HEADREF=$(timeout 90 git ls-remote --symref "https://github.com/$ADDR" HEAD 2>/dev/null \
          | awk '/^ref:/{print $2}' | head -1)
if [ -z "$HEADREF" ]; then echo -e "$ADDR\tNO_LSREMOTE\t-\t-\t-\t-"; exit 0; fi
BR="${HEADREF#refs/heads/}"
if ! timeout 300 git clone --quiet --depth 1 --filter=blob:none --no-checkout \
      "https://github.com/$ADDR" "$D/r" 2>/dev/null; then
  echo -e "$ADDR\tCLONE_FAIL\t$BR\t-\t-\t-"; exit 0; fi
timeout 90 git -C "$D/r" ls-tree -r --name-only HEAD > "$D/tree.txt" 2>/dev/null
NFILES=$(wc -l < "$D/tree.txt")
# every grant-bearing path at ANY depth, ANY capitalisation, ANY extension
grep -iE '(^|/)(licen[sc]e|copying|copyright|notice|eula|terms|unlicense)([._-][a-z0-9.]*)?$|(^|/)licen[sc]es?/' \
  "$D/tree.txt" 2>/dev/null \
  | grep -ivE '\.(png|jpe?g|gif|svg|ico|pdf|ttf|woff2?|eot|zip|gz|tgz|mp4|webp|otf|rtf|docx?)$' \
  > "$D/grantpaths.txt"
NP=$(wc -l < "$D/grantpaths.txt")
mkdir -p "$D/blobs"
i=0
while IFS= read -r p; do
  [ -z "$p" ] && continue
  i=$((i+1)); safe=$(echo "$p" | tr '/' '~')
  timeout 60 git -C "$D/r" cat-file blob "HEAD:$p" > "$D/blobs/$safe" 2>/dev/null || rm -f "$D/blobs/$safe"
done < "$D/grantpaths.txt"
echo -e "$ADDR\tOK\t$BR\t$NFILES\t$NP\t$(ls "$D/blobs" 2>/dev/null | wc -l)"
