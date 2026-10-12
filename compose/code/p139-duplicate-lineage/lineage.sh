#!/usr/bin/env sh
# p139-duplicate-lineage — `ACTION CN`: which of two identical-looking repositories is the
# original, decided WITHOUT reading either one's manifest?
#
#   ./lineage.sh <owner/repo> <owner/repo>
#
# p138 called `Dymayo/moodler-mcp` byte-identical to `GhaithAlHallak8/moodler-mcp` and named
# the second canonical **on the strength of the first's own manifest**. `ACTION CN` asked for a
# channel that is not the manifest. Git is that channel, and it answers three ways at once:
#
#   1. SHARED COMMIT SHAS. A sha is a hash over content, parents, author and timestamp, so two
#      repositories sharing shas share one history -- a fork or mirror. Zero shared shas with
#      an identical tree means the history was RE-AUTHORED, which is what p136's `ACTION BW`
#      found for the ENEM repositories. The two cases look the same in a file listing and are
#      opposites in provenance.
#   2. ANCESTRY. If every commit of B is in A and A has more, B is behind A: A is the trunk.
#   3. REF COUNT. `ls-remote` needs no API token. The original accumulates release tags and
#      branches; a copy usually carries the default branch and little else.
#
# A fourth signal comes free: GitHub's `users.noreply.github.com` author addresses embed the
# account's numeric id and login, so the committing ACCOUNT is visible in the history itself.
#
# Channel note: api.github.com answers 403 here, so `fork: true` cannot be read. Git
# smart-HTTP over github.com does answer, which is what this script uses.
set -u

A=${1:?owner/repo}
B=${2:?owner/repo}

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

clone() {  # blobless, no checkout: commit and tree objects only
  git clone --filter=blob:none --no-checkout --quiet "https://github.com/$1" "$2" 2>/dev/null
}

da="$work/a"; db="$work/b"
clone "$A" "$da" || { echo "CLONE_FAIL $A"; exit 1; }
clone "$B" "$db" || { echo "CLONE_FAIL $B"; exit 1; }

ca=$(git -C "$da" rev-list --count HEAD)
cb=$(git -C "$db" rev-list --count HEAD)
git -C "$da" rev-list HEAD | sort > "$work/sa"
git -C "$db" rev-list HEAD | sort > "$work/sb"
shared=$(comm -12 "$work/sa" "$work/sb" | wc -l | tr -d ' ')
only_a=$(comm -23 "$work/sa" "$work/sb" | wc -l | tr -d ' ')
only_b=$(comm -13 "$work/sa" "$work/sb" | wc -l | tr -d ' ')

refs_a=$(git ls-remote --heads --tags "https://github.com/$A" 2>/dev/null | wc -l | tr -d ' ')
refs_b=$(git ls-remote --heads --tags "https://github.com/$B" 2>/dev/null | wc -l | tr -d ' ')

root_a=$(git -C "$da" rev-list --max-parents=0 HEAD | tail -1)
root_b=$(git -C "$db" rev-list --max-parents=0 HEAD | tail -1)
tree_a=$(git -C "$da" rev-parse HEAD^{tree})
tree_b=$(git -C "$db" rev-parse HEAD^{tree})

if [ "$shared" = "0" ]; then
  if [ "$tree_a" = "$tree_b" ]; then
    verdict="RE_AUTHORED (identical tree, zero shared commits -- p136 ACTION BW's class)"
  else
    verdict="UNRELATED (no shared commits, different trees)"
  fi
elif [ "$only_b" = "0" ] && [ "$only_a" != "0" ]; then
  verdict="B_IS_BEHIND_A -- $A is the trunk"
elif [ "$only_a" = "0" ] && [ "$only_b" != "0" ]; then
  verdict="A_IS_BEHIND_B -- $B is the trunk"
elif [ "$only_a" = "0" ] && [ "$only_b" = "0" ]; then
  verdict="IDENTICAL_HISTORY -- decide on refs and author accounts"
else
  verdict="DIVERGED -- both carry unique commits"
fi

printf 'field\t%s\t%s\n' "$A" "$B"
printf 'commits\t%s\t%s\n' "$ca" "$cb"
printf 'head\t%s\t%s\n' "$(git -C "$da" rev-parse --short HEAD)" "$(git -C "$db" rev-parse --short HEAD)"
printf 'head_date\t%s\t%s\n' "$(git -C "$da" log -1 --format=%cI)" "$(git -C "$db" log -1 --format=%cI)"
printf 'root_commit\t%s\t%s\n' "$root_a" "$root_b"
printf 'head_tree\t%s\t%s\n' "$tree_a" "$tree_b"
printf 'remote_refs\t%s\t%s\n' "$refs_a" "$refs_b"
printf 'shared_commits\t%s\t%s\n' "$shared" "$shared"
printf 'unique_commits\t%s\t%s\n' "$only_a" "$only_b"
printf 'noreply_accounts\t%s\t%s\n' \
  "$(git -C "$da" log --format='%ae' | grep -o '[0-9]*+[A-Za-z0-9-]*@users.noreply.github.com' | sort -u | paste -sd'|' -)" \
  "$(git -C "$db" log --format='%ae' | grep -o '[0-9]*+[A-Za-z0-9-]*@users.noreply.github.com' | sort -u | paste -sd'|' -)"
printf 'verdict\t%s\t%s\n' "$verdict" "$verdict"
