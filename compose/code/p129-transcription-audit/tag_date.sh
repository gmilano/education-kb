#!/usr/bin/env bash
# p129 instrument: read a tag's commit date over the git lane only (no GitHub API)
addr="$1"; tag="$2"; d=$(mktemp -d)
git init -q "$d" && cd "$d" || exit 1
if timeout 120 git fetch -q --depth 1 "https://github.com/$addr" "refs/tags/$tag:refs/tags/$tag" 2>/dev/null; then
  echo -e "$addr\t$tag\t$(git log -1 --format=%cI "refs/tags/$tag" 2>/dev/null)\t$(git cat-file -t "refs/tags/$tag")"
else
  echo -e "$addr\t$tag\tFETCH-FAIL\t-"
fi
rm -rf "$d"
