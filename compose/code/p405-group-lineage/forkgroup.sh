#!/bin/sh
# forkgroup.sh GROUP OWNER/REPO...  -- grade a WHOLE name-collision group's lineage.
#
# O(N) clones for C(N,2) verdicts.  p404's forkdir.sh clones two repositories per pair,
# so canvas-mcp's 20 addresses would cost 190 pairs x 2 clones.  Every fact a pair
# verdict needs is a property of one repository, so each address is cloned ONCE and
# cached; the pairs are then set operations.
#
# Needs FULL clones.  `--depth 1` and `ls-remote` both discard the objects the verdict
# rests on, which is p404's finding and is not re-litigated here.
#
# Writes a per-address facts cache under $WORK, then emits two TSVs on stdout via run.py.
set -eu
[ $# -ge 3 ] || { echo "usage: forkgroup.sh GROUP OWNER/REPO OWNER/REPO [OWNER/REPO...]" >&2; exit 2; }
GROUP=$1; shift
HERE=$(cd "$(dirname "$0")" && pwd)
WORK=${WORK:-$(mktemp -d)}
mkdir -p "$WORK/facts"

for s in "$@"; do
  key=$(echo "$s" | tr '/' '_')
  f=$WORK/facts/$key
  [ -s "$f" ] && continue
  d=$WORK/clones/$key
  rm -rf "$d"
  # An address that does not resolve is recorded as UNRESOLVED and does not abort the
  # group: p402 met one (eastarctica/canvas-mcp) and a group of 20 must not be lost to it.
  if ! git clone --quiet "https://github.com/$s" "$d" 2>"$WORK/err.$key"; then
    printf 'slug\t%s\nstatus\tUNRESOLVED\n' "$s" > "$f"
    continue
  fi
  # A repository that exists with no commits clones fine and has no HEAD.  p401 met this
  # class (EXISTS_EMPTY_TREE); graded as its own status so it cannot read as UNRESOLVED.
  if ! git -C "$d" rev-parse HEAD >/dev/null 2>&1; then
    printf 'slug\t%s\nstatus\tEMPTY\n' "$s" > "$f"
    rm -rf "$d"; continue
  fi
  {
    printf 'slug\t%s\nstatus\tOK\n' "$s"
    printf 'head\t%s\n'        "$(git -C "$d" rev-parse HEAD)"
    printf 'branch\t%s\n'      "$(git -C "$d" rev-parse --abbrev-ref HEAD)"
    printf 'head_date\t%s\n'   "$(git -C "$d" log -1 --format=%ad --date=short)"
    printf 'tags\t%s\n'        "$(git -C "$d" tag | wc -l | tr -d ' ')"
    printf 'refs\t%s\n'        "$(git -C "$d" show-ref | wc -l | tr -d ' ')"
    # Root commit, its date and its author: the provenance half of a CONTENT-COPY.
    for r in $(git -C "$d" rev-list --max-parents=0 --all); do
      printf 'root\t%s\n' "$r"
      printf 'root_tree\t%s\n' "$(git -C "$d" rev-parse "$r^{tree}")"
      printf 'root_date\t%s\n' "$(git -C "$d" log -1 --format=%ad --date=short "$r")"
      printf 'root_author\t%s\n' "$(git -C "$d" log -1 --format='%an <%ae>' "$r")"
    done
    git -C "$d" rev-list --all            | sed 's/^/commit\t/'
    git -C "$d" rev-list --all --format='%T' | grep -v '^commit' | sort -u | sed 's/^/tree\t/'
    git -C "$d" rev-list HEAD             | sed 's/^/ancestor\t/'
    # The grant, read from the payload at HEAD -- free, because the tree is already here.
    #
    # 🔴 p283's ladder rule, and p401's `readme.md` specimen: a FIXED LIST OF SPELLINGS is the
    # defect, not a shortcut.  `git cat-file -e HEAD:LICENSE` is case-sensitive exactly as
    # `raw.githubusercontent.com` is, so a probe list grades a repository carrying `license`
    # or `License.md` as HAVING NO GRANT -- and p401 measured that error's direction: an
    # ungranted repository reads as UNENCUMBERED, which is the opposite of the truth.
    #
    # 🟢 A full clone makes the list unnecessary.  ENUMERATE the root tree and fold the case,
    # so every spelling is found including ones no list would have guessed.
    lp=$(git -C "$d" ls-tree --name-only HEAD \
         | grep -iE '^(licen[cs]e|copying|notice)(\.(md|txt|rst))?$' | head -1)
    if [ -n "$lp" ]; then
      printf 'licence_path\t%s\n' "$lp"
      printf 'licence_bytes\t%s\n' "$(git -C "$d" cat-file -s "HEAD:$lp")"
      printf 'licence_title\t%s\n' "$(git -C "$d" show "HEAD:$lp" | grep -m1 -iE '[a-z]' | tr -d '\r' | cut -c1-80)"
    fi
  } > "$f"
  rm -rf "$d"
done

python3 "$HERE/run.py" "$GROUP" "$WORK/facts" "$@"
