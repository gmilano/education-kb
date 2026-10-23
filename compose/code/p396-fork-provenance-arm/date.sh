#!/bin/bash
# p396 dating channel: blobless clone, p389's method. Arg = repo list file.
while read -r repo; do
  [ -z "$repo" ] && continue
  d=$(mktemp -d)
  if git clone --filter=blob:none --no-checkout --depth 1 -q "https://github.com/$repo" "$d" 2>/dev/null; then
    sha=$(git -C "$d" rev-parse --short HEAD 2>/dev/null)
    iso=$(git -C "$d" log -1 --format=%cI 2>/dev/null)
    days=$(( ( $(date +%s) - $(git -C "$d" log -1 --format=%ct 2>/dev/null) ) / 86400 ))
    branch=$(git -C "$d" rev-parse --abbrev-ref HEAD 2>/dev/null)
    echo -e "$repo\t$sha\t${iso%T*}\t${days}\t$branch"
  else
    echo -e "$repo\tCLONE-FAIL\t-\t-\t-"
  fi
  rm -rf "$d"
done < "$1"
