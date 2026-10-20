#!/usr/bin/env bash
# p329-grant-link-resolution -- the capture half. The instrument itself does NO network (P-convention
# of this base); this script produces the two inputs `classify()` needs, and nothing else.
#
# Usage:  ./capture.sh owner/repo  [outdir]
#
# It emits:
#   <outdir>/README.md   -- the README text, from raw.githubusercontent.com
#   <outdir>/tree.txt    -- the FULL enumeration, every branch (P275). Not a probe list.
#
# Why a full clone-and-enumerate rather than a path ladder: P275/P278. "To sustain an absence in a
# tree you must ENUMERATE it", and "a count of ZERO over a path that does not exist in that ref
# measures the PATH, not the content". A 404 on LICENSE proves nothing about LICENSE.md.
#
# Channel note (p329): github.com and api.github.com both answer 403 through this proxy, while
# raw.githubusercontent.com answers 200 and git smart-HTTP is OPEN. That is why this script uses
# `git clone`, not the API.
set -uo pipefail
repo="${1:?usage: capture.sh owner/repo [outdir]}"
out="${2:-./capture/$(echo "$repo" | tr '/' '_')}"
mkdir -p "$out"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# Blobless, no checkout: seconds even on a large repo, and enough for ls-tree.
if ! git clone --filter=blob:none --no-checkout "https://github.com/$repo" "$tmp/r" -q 2>/dev/null; then
  echo "CLONE-FAILED $repo" >&2
  exit 2
fi

# Every branch, not just the default one -- a grant committed only on `develop` is still a grant.
: > "$out/tree.txt"
for br in $(git -C "$tmp/r" for-each-ref --format='%(refname)' refs/remotes/origin 2>/dev/null); do
  git -C "$tmp/r" ls-tree -r --name-only "$br" 2>/dev/null >> "$out/tree.txt"
done
sort -u -o "$out/tree.txt" "$out/tree.txt"

# The activity triple, while we have the history -- p329's other finding. Free at this point.
{
  echo "repo=$repo"
  echo "commits=$(git -C "$tmp/r" rev-list --count HEAD 2>/dev/null)"
  echo "authors=$(git -C "$tmp/r" log --format=%an 2>/dev/null | sort -u | wc -l)"
  echo "first_commit=$(git -C "$tmp/r" log --reverse --format=%ad --date=short 2>/dev/null | head -1)"
  echo "last_commit=$(git -C "$tmp/r" log -1 --format=%ad --date=short 2>/dev/null)"
  echo "tree_files=$(wc -l < "$out/tree.txt")"
} > "$out/activity.txt"

# The README, from the channel that is actually open.
#
# 🔴 P441 again, and the p329 ladder ratchet caught this too: the first draft of this script spelled
# the readme filename by hand across three branches. That is a NAME LADDER, with exactly the defect
# of a licence ladder -- a repository using any other spelling or extension would have come back as
# NO-README, and `classify()` would then have returned UNKNOWN_NO_README over a repository that
# ships a perfectly good readme. 🟢 So it is LOOKED UP in the tree enumerated above rather than
# guessed: `git ls-tree --name-only` at the root of the default branch, matched case-insensitively
# with any extension. No spelling is written down here at all.
default_br="$(git -C "$tmp/r" symbolic-ref --short HEAD 2>/dev/null || echo HEAD)"
readme_path="$(git -C "$tmp/r" ls-tree --name-only "$default_br" 2>/dev/null \
                 | grep -iE '^readme(\.[a-z0-9]+)?$' | head -1)"

if [ -n "$readme_path" ]; then
  if curl -sfS -m 25 -o "$out/README.md" \
       "https://raw.githubusercontent.com/$repo/$default_br/$readme_path" 2>/dev/null; then
    echo "readme_branch=$default_br" >> "$out/activity.txt"
    echo "readme_path=$readme_path"   >> "$out/activity.txt"
  fi
fi
[ -s "$out/README.md" ] || echo "NO-README $repo (classify() will return UNKNOWN_NO_README)" >&2

echo "$out"
