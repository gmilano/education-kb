#!/usr/bin/env bash
# agree.sh -- LOCK-AGREEMENT census: does the lock that REACHES the root
#              manifest actually AGREE with it?
#
# WHY THIS AXIS, AND WHY NOW. Eight passes have measured this shelf:
#   p107 tag COUNT              how much ref traffic
#   p108 release IDENTITY       can I pin it
#   p109 commit RECENCY         is it alive
#   p110 author CONCENTRATION   what happens if they stop
#   p111 verification SURFACE   can the tree tell me when I broke it
#   p112 dependency CLOSURE     does a lock exist
#   p113 provider BINDING       (parallel axis, independent)
#   p114 lock REACH             does that lock reach the manifest
#
# p114 ended by naming what its own figure still hides, in the trend table it
# published in intel/trends.md:
#
#   reach | p114 | 34.5 % full-reach; 76.1 % of manifests reached
#         |      | WHAT THE FIGURE HIDES: whether the pinned versions are
#         |      | any good
#
# "Any good" has two decidable halves and one undecidable one. Whether a
# pinned version is current needs a registry (out of the git lane, P116-D).
# Whether it is SECURE needs an advisory feed (likewise). But whether the lock
# and the manifest even describe the same dependency SET is decidable from
# committed bytes alone -- and it is the half with a hard failure mode:
#
#   `npm ci` does not install a stale lock. It exits 1 and installs nothing.
#
# So p114's 208 rows whose root manifest is reached are not yet 208 rows that
# build. p116 measures how many of them a resolver would actually accept.
#
# It is the ninth axis in nine passes, the fifth read from the TREE, and -- like
# p114 -- it can only ever move rows DOWNWARD: by construction (P116-B) this
# census reads no row as more reproducible than p114 did.
#
# DENOMINATOR (P116-A). p114's result TSV, rows with lockable_man > 0 AND
# root_orphan == 0: the 134 addresses p114 says have a lockable root manifest
# that a lock DOES reach. Rows p114 already failed are not re-failed here; this
# axis is a tightening of p114's positive class, not a new census of the shelf.
#
# WHY ROOT-ONLY IS NOT A SHORTCUT (P116-B). The root manifest has no ancestor,
# so the only lock that can reach it is a lock AT the root. Root-only reading
# is therefore exactly p114's root_orphan == 0 condition re-read, not a
# narrower sample of it. The unit is identical and the two figures compose.
#
# CHANNEL. Anonymous git lane only, re-probed live at pass 116 -- unchanged
# since p107 (P107-A):
#   git ls-remote / git fetch                 rc=0
#   raw.githubusercontent.com/<slug>/HEAD/..  200
#   api.github.com                            403
# Tree from a depth-1 blob-filtered fetch; manifest and lock BODIES from a
# batched lazy blob fetch against the same promisor remote (P111-H, reused by
# p112, p114 and reused again here). agree.py is invoked with `python3 -I` and
# given ABSOLUTE PATHS, never run from inside a fetched tree, so no blob on
# this shelf can be imported as code by the instrument that measures it.
#
# MODES
#   (default)          the agreement rule (P116-B)
#   P116_PEER=1        count peerDependencies too -- the POSITIVE control that
#                      shows how much drift the P116-E exclusion suppresses
#   P116_NO_DEV=1      runtime deps only -- measures the devDependencies
#                      contribution to drift
#   P116_BASE=<url>    transport swap, so the suite drives this same code
#                      against real git repositories over file:// (never a mock)
#
# Output TSV:
#   slug rc root_ecos measured declared present missing verdict detail
# where `declared` is already net of the three by-design exclusions:
#   P116-E peerDependencies    P116-F composer platform pkgs
#   P116-J non-registry specs  P116-L workspace-local packages
set -uo pipefail
cd "$(dirname "$0")"
HERE="$(pwd)"

list="${1:-addresses.txt}"
workroot="${P116_WORK:-${TMPDIR:-/tmp}/p116work}"
BASE="${P116_BASE:-https://github.com}"
PEER="${P116_PEER:-0}"
NO_DEV="${P116_NO_DEV:-0}"
mkdir -p "$workroot"

export P116_PEER="$PEER" P116_NO_DEV="$NO_DEV"

printf 'slug\trc\troot_ecos\tmeasured\tdeclared\tpresent\tmissing\tverdict\tdetail\n'

while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac

  d="$workroot/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$d"; mkdir -p "$d"
  git init -q --bare "$d" 2>/dev/null
  case "$slug" in
    *://*) url="$slug" ;;
    *) url="$BASE/$slug" ;;
  esac
  git -C "$d" remote add origin "$url" 2>/dev/null

  if ! git -C "$d" fetch -q --depth 1 --filter=blob:none origin HEAD 2>/dev/null; then
    ok=0
    for b in main master; do
      git -C "$d" fetch -q --depth 1 --filter=blob:none origin "$b" 2>/dev/null && { ok=1; break; }
    done
    [ "$ok" = 1 ] || { printf '%s\t1\t-\t-\t-\t-\t-\tUNREAD\tfetch-failed\n' "$slug"; continue; }
  fi

  # root-level entries only (P116-B)
  root="$(git -C "$d" ls-tree --name-only FETCH_HEAD 2>/dev/null)"
  [ -n "$root" ] || { printf '%s\t1\t-\t-\t-\t-\t-\tUNREAD\tempty-tree\n' "$slug"; continue; }

  # Workspace-local names are resolved LAZILY, only for a row that actually
  # shows drift (P116-O). Doing it for every row means fetching every
  # sub-manifest in every tree -- canvas-lms has 596 -- and the first draft of
  # this census managed 3 rows in four minutes before it was restructured.
  wsf="$d.ws"; : > "$wsf"; wsdone=0

  resolve_ws() {
    [ "$wsdone" = 0 ] || return 0
    wsdone=1
    subman="$(git -C "$d" ls-tree -r --name-only FETCH_HEAD 2>/dev/null \
              | grep -E '/package\.json$' || :)"
    [ -n "$subman" ] || return 0
    wshas=""
    while IFS= read -r sp; do
      [ -n "$sp" ] || continue
      ss=$(git -C "$d" rev-parse "FETCH_HEAD:$sp" 2>/dev/null) || continue
      wshas="${wshas}${ss}
"
    done <<WSEOF
$subman
WSEOF
    # one batched lazy fetch for every sub-manifest blob (P111-H), then one
    # single reader process for the whole stream
    printf '%s' "$wshas" | git -C "$d" cat-file --batch 2>/dev/null \
      | python3 -I "$HERE/wsnames.py" > "$wsf" 2>/dev/null || : > "$wsf"
  }

  has() { printf '%s\n' "$root" | grep -qxF "$1"; }

  ecos=""; pairs=""
  if has package.json; then
    ecos="${ecos}npm,"
    # P116-I. All three npm lock flavours count. Preference order is the one
    # npm/yarn/pnpm themselves apply when more than one is committed.
    for cand in package-lock.json npm-shrinkwrap.json yarn.lock pnpm-lock.yaml; do
      if has "$cand"; then pairs="${pairs}npm:package.json:$cand "; break; fi
    done
  fi
  if has composer.json; then
    ecos="${ecos}composer,"
    has composer.lock && pairs="${pairs}composer:composer.json:composer.lock "
  fi
  if has Cargo.toml; then
    ecos="${ecos}cargo,"
    has Cargo.lock && pairs="${pairs}cargo:Cargo.toml:Cargo.lock "
  fi
  ecos="${ecos%,}"; [ -n "$ecos" ] || ecos="-"

  if [ -z "$pairs" ]; then
    # root manifest exists in an ecosystem this axis has no lock grammar for
    printf '%s\t0\t%s\t0\t-\t-\t-\tno-lock-grammar\troot manifest is not npm/composer/cargo\n' "$slug" "$ecos"
    continue
  fi

  # ---- batched lazy blob fetch: every needed blob in ONE request (P111-H) ----
  shas=""; declare -A BLOB=()
  for p in $pairs; do
    IFS=: read -r eco man lock <<<"$p"
    for f in "$man" "$lock"; do
      s=$(git -C "$d" rev-parse "FETCH_HEAD:$f" 2>/dev/null) || continue
      BLOB["$f"]="$s"; shas="${shas}${s}
"
    done
  done
  bodies="$d.body"; mkdir -p "$bodies"
  printf '%s' "$shas" | git -C "$d" cat-file --batch >/dev/null 2>&1 || true
  for f in "${!BLOB[@]}"; do
    git -C "$d" cat-file blob "${BLOB[$f]}" > "$bodies/$(printf '%s' "$f" | tr '/' '_')" 2>/dev/null || :
  done

  tot_d=0; tot_p=0; tot_m=0; measured=0; worst="agree"; detail=""
  for p in $pairs; do
    IFS=: read -r eco man lock <<<"$p"
    mf="$bodies/$(printf '%s' "$man" | tr '/' '_')"
    lf="$bodies/$(printf '%s' "$lock" | tr '/' '_')"
    row=$(python3 -I "$HERE/agree.py" "$eco" "$mf" "$lf" "$slug" 2>/dev/null) || row=""
    [ -n "$row" ] || { detail="${detail}${eco}=probe-failed;"; worst="UNREAD"; continue; }
    IFS=$'\t' read -r _ _ dcl prs mis vrd names <<<"$row"
    # Only a drifting row is worth the cost of reading the whole tree's
    # sub-manifests, and only npm has workspaces in this axis's grammar.
    if [ "$vrd" = drift ] && [ "$eco" = npm ]; then
      resolve_ws
      if [ -s "$wsf" ]; then
        row2=$(python3 -I "$HERE/agree.py" "$eco" "$mf" "$lf" "$slug" "$wsf" 2>/dev/null) || row2=""
        if [ -n "$row2" ]; then
          IFS=$'\t' read -r _ _ dcl prs mis vrd names <<<"$row2"
        fi
      fi
    fi
    measured=$((measured+1))
    case "$dcl" in ''|-|*[!0-9]*) ;; *) tot_d=$((tot_d+dcl)) ;; esac
    case "$prs" in ''|-|*[!0-9]*) ;; *) tot_p=$((tot_p+prs)) ;; esac
    case "$mis" in ''|-|*[!0-9]*) ;; *) tot_m=$((tot_m+mis)) ;; esac
    detail="${detail}${eco}=${vrd}(${prs}/${dcl})"
    [ -n "$names" ] && detail="${detail}[${names}]"
    detail="${detail};"
    case "$vrd" in
      drift) [ "$worst" = UNREAD ] || worst="drift" ;;
      agree|empty-manifest) : ;;
      *) [ "$worst" = drift ] || [ "$worst" = UNREAD ] || worst="$vrd" ;;
    esac
  done

  [ "$measured" = 0 ] && worst="no-lock-grammar"
  printf '%s\t0\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$ecos" "$measured" "$tot_d" "$tot_p" "$tot_m" "$worst" "${detail%;}"
done < "$list"
