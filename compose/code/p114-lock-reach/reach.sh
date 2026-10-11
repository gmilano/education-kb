#!/usr/bin/env bash
# reach.sh — LOCK-REACH census over this KB's shelf addresses.
#
# WHY THIS AXIS, AND WHY NOW. Six passes have measured this shelf:
#   p107 tag COUNT              how much ref traffic
#   p108 release IDENTITY       can I pin it
#   p109 commit RECENCY         is it alive
#   p110 author CONCENTRATION   what happens if they stop
#   p111 verification SURFACE   can the tree tell me when I broke it
#   p112 dependency CLOSURE     does it resolve to the same bytes twice
#
# p112 published 107 of 296 rows (36.1 %) at `pinned` and, in the same file,
# declared the error that figure carries:
#
#   P112-E  "An ecosystem counts as locked if ONE lockfile for it exists
#            anywhere in the tree. In a monorepo with forty package.json
#            files and one root package-lock.json that is generous. [...]
#            every figure this script produces is an UPPER BOUND on pinning,
#            said here rather than discovered later."
#
# An upper bound whose gap is unmeasured cannot be handed to a client team.
# p114 measures the gap. It asks the resolver's question instead of the
# inventory's: not DOES A LOCK EXIST, but DOES A LOCK REACH THIS MANIFEST --
# at its own directory or an ancestor of it, which is the only relation npm,
# pnpm, cargo and poetry actually honour.
#
# It is the seventh axis in seven passes and the third read from the TREE. It
# is also the first pass that can only ever move rows DOWNWARD: by
# construction (P114-B) no row reads more pinned here than it did at p112, so
# every row that moves is p112's own stated error being paid.
#
# CHANNEL. Anonymous git lane only, re-probed live at pass 113 — unchanged
# since p107 (P107-A: api.github.com answers 403 under this session's scoping,
# and the git lane is the whole instrument):
#   git ls-remote / git fetch                 rc=0
#   raw.githubusercontent.com/<slug>/HEAD/..  200
#   api.github.com                            403
# Tree from a depth-1 blob-filtered fetch; requirement-file BODIES from a
# batched lazy blob fetch against the same promisor remote (P111-H, reused by
# p112 and reused again here).
#
# STAGE B IS NOT OPTIONAL HERE. p112 could credit a pinned requirements.txt as
# a repository-level fact. p114 needs its DIRECTORY (P114-C), so the body read
# is what decides whether a root `setup.py` beside a pinned `ml/requirements.
# txt` is orphaned or covered. P114_NO_BODY=1 measures that contribution.
#
# MODES
#   (default)          the reach rule (P114-B)
#   P114_FLAT=1        p112's rule restored — the negative control (P114-H)
#   P114_NO_BODY=1     skip stage B — measures the P114-C contribution
#   P114_BASE=<url>    transport swap, so the suite drives this same code
#                      against real git repositories over file:// (never a mock)
#
# Output TSV:
#   slug rc files vendor manifests lockable_man covered orphans deepest_orphan
#   root_orphan reqpin_dirs locks_total ecos locks locks_live orphan_ecos
#   deployable verdict orphan_paths
set -uo pipefail
cd "$(dirname "$0")"

list="${1:-addresses.txt}"
workroot="${P114_WORK:-${TMPDIR:-/tmp}/p114work}"
BASE="${P114_BASE:-https://github.com}"
FLAT="${P114_FLAT:-0}"
NO_BODY="${P114_NO_BODY:-0}"

mkdir -p "$workroot"

printf 'slug\trc\tfiles\tvendor\tmanifests\tlockable_man\tcovered\torphans\tdeepest_orphan\troot_orphan\treqpin_dirs\tlocks_total\tecos\tlocks\tlocks_live\torphan_ecos\tdeployable\tverdict\torphan_paths\n'

while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac

  d="$workroot/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$d" "$d.pos" "$d.body"; mkdir -p "$d"
  git init -q --bare "$d" 2>/dev/null

  case "$slug" in
    *://*) url="$slug" ;;
    *)     url="$BASE/$slug" ;;
  esac

  # Promisor config FIRST so stage B's lazy blob fetch has a remote to resolve
  # against (P111-H, reused).
  git --git-dir="$d" remote add origin "$url" 2>/dev/null
  git --git-dir="$d" config remote.origin.promisor true
  git --git-dir="$d" config remote.origin.partialclonefilter blob:none

  if ! git --git-dir="$d" fetch -q --depth=1 --filter=blob:none origin HEAD 2>/dev/null; then
    if ! git --git-dir="$d" fetch -q --depth=1 origin HEAD 2>/dev/null; then
      # P1040. An unread row is never zero.
      printf '%s\t1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tUNREAD\t\n' "$slug"
      rm -rf "$d"; continue
    fi
  fi

  tree=$(git --git-dir="$d" ls-tree -r FETCH_HEAD 2>/dev/null)
  if [ -z "$tree" ]; then
    printf '%s\t0\t0\t0\t0\t0\t0\t0\t-1\t0\t0\t0\t-\t-\t-\t-\t0\tno-manifest\t-\n' "$slug"
    rm -rf "$d"; continue
  fi

  printf '%s\n' "$tree" | awk -f ../lib/reqname.awk -f positions.awk > "$d.pos"

  # ---- stage B: which requirement FILES are themselves locks, and where ----
  # P114-C. The answer is a set of DIRECTORIES, not a boolean.
  extrapy='-'
  nreq=$(awk -F'\t' '$1=="R"' "$d.pos" | wc -l)
  if [ "$nreq" -gt 0 ] && [ "$NO_BODY" != 1 ]; then
    if awk -F'\t' '$1=="R" && $2!="-" {print $2}' "$d.pos" | sort -u \
         | timeout 180 git --git-dir="$d" cat-file --batch > "$d.body" 2>/dev/null \
       && [ -s "$d.body" ]; then
      # Which shas are fully pinned. P112-H: the batch stream interleaves
      # `<sha> blob <size>` headers that carry no `==` and are not comments,
      # so a naive scan reads every one as an UNPINNED requirement and a
      # perfectly pinned repo reports as floating. Headers are DELIMITERS.
      # P112-J: a file with no real requirement line is not evidence.
      # P112-I: bodies go to a FILE; never a pipe into an early-exiting reader.
      pinned_shas=$(awk '
        /^[0-9a-f]{40} (blob|missing)( [0-9]+)?$/ {
          if (cur != "" && real > 0 && real == pin) print cur
          cur = $1; real = 0; pin = 0; next
        }
        cur == "" { next }
        { sub(/\r$/, ""); line = $0
          sub(/[ \t]*#.*$/, "", line)
          gsub(/^[ \t]+|[ \t]+$/, "", line)
          if (line == "")              next
          if (line ~ /^-/)             next      # -r includes, -e, --flags
          real++
          if (line ~ /==/)             { pin++; next }
          if (line ~ /@/)              { pin++; next }   # PEP 508 direct ref
        }
        END { if (cur != "" && real > 0 && real == pin) print cur }
      ' "$d.body")
      if [ -n "$pinned_shas" ]; then
        # sha -> every directory that file sits in (one blob can appear twice)
        extrapy=$(printf '%s\n' "$pinned_shas" | sort -u | awk -F'\t' '
          NR == FNR { pin[$1] = 1; next }
          $1 == "R" && ($2 in pin) { d = ($3 == "" ? "/" : $3); if (!(d in seen)) { seen[d] = 1; out = (out == "" ? d : out "," d) } }
          END { print (out == "" ? "-" : out) }
        ' - "$d.pos")
        [ -n "$extrapy" ] || extrapy='-'
      fi
    fi
  fi

  eval "$(awk -F'\t' -v flat="$FLAT" -v extrapy="$extrapy" -f cover.awk "$d.pos" \
          | sed 's/^\([a-z_]*\)=\(.*\)$/\1="\2"/')"

  files=$(awk -F'\t' '$1=="C" && $2=="files"  {print $3}' "$d.pos")
  vendor=$(awk -F'\t' '$1=="C" && $2=="vendor" {print $3}' "$d.pos")
  deploy=$(awk -F'\t' '$1=="C" && $2=="deploy" {print $3}' "$d.pos")

  rm -rf "$d" "$d.pos" "$d.body"

  printf '%s\t0\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$files" "$vendor" "$man_total" "$lockable_man" "$covered" \
    "$orphans" "$deepest_orphan" "$root_orphan" "$reqpin_dirs" "$locks_total" \
    "$ecos" "$locks" "$locks_live" "$orphan_ecos" "$deploy" "$verdict" \
    "$orphan_paths"
done < "$list"
