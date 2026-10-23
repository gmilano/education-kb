#!/bin/sh
# forkdir.sh OWNER/REPO OWNER/REPO  -- grade a same-name pair by FULL history.
#
# Needs full clones: --depth 1 cannot answer this, and neither can ls-remote.
# Prints one TSV row: a  b  commits_a  commits_b  shared_commits  shared_trees
#                     a_contains_b_head  b_contains_a_head  verdict  direction
set -eu
A=$1; B=$2
D=$(mktemp -d)
trap 'rm -rf "$D"' EXIT

for s in "$A" "$B"; do
  git clone --quiet "https://github.com/$s" "$D/$(echo "$s" | tr '/' '_')"
done
da=$D/$(echo "$A" | tr '/' '_'); db=$D/$(echo "$B" | tr '/' '_')

git -C "$da" rev-list --all | sort > "$D/a.c"; git -C "$db" rev-list --all | sort > "$D/b.c"
git -C "$da" rev-list --all --format='%T' | grep -v '^commit' | sort -u > "$D/a.t"
git -C "$db" rev-list --all --format='%T' | grep -v '^commit' | sort -u > "$D/b.t"

ca=$(wc -l < "$D/a.c"); cb=$(wc -l < "$D/b.c")
sc=$(comm -12 "$D/a.c" "$D/b.c" | wc -l); st=$(comm -12 "$D/a.t" "$D/b.t" | wc -l)
# ancestry: is the OTHER side's HEAD reachable from this side's HEAD?
if git -C "$da" merge-base --is-ancestor "$(git -C "$db" rev-parse HEAD)" HEAD 2>/dev/null; then ab=True; else ab=False; fi
if git -C "$db" merge-base --is-ancestor "$(git -C "$da" rev-parse HEAD)" HEAD 2>/dev/null; then ba=True; else ba=False; fi

# direction signal for a content copy: whose ROOT commit carries a shared tree?
owner=None
if [ "$sc" -eq 0 ] && [ "$st" -gt 0 ]; then
  for side in a b; do
    [ "$side" = a ] && d=$da || d=$db
    rt=$(git -C "$d" rev-list --max-parents=0 HEAD | while read -r r; do git -C "$d" rev-parse "$r^{tree}"; done)
    for t in $rt; do
      if comm -12 "$D/a.t" "$D/b.t" | grep -qxF "$t"; then owner=\"$side\"; fi
    done
  done
fi

v=$(cd "$(dirname "$0")" && python3 -c "
from verdict import grade
print('\t'.join(str(x) for x in grade($sc, $st, $ab, $ba, root_tree_owner=$owner)))")
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$A" "$B" "$ca" "$cb" "$sc" "$st" "$ab" "$ba" "$v"
