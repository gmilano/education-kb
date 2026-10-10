#!/usr/bin/env bash
# depclosure.sh — DEPENDENCY-CLOSURE census over this KB's shelf addresses.
#
# WHY THIS AXIS, AND WHY NOW. Five passes have measured this shelf:
#   p107 tag COUNT              how much ref traffic
#   p108 release IDENTITY       can I pin it
#   p109 commit RECENCY         is it alive
#   p110 author CONCENTRATION   what happens if they stop
#   p111 verification SURFACE   can the tree tell me when I broke it
#
# p111's answer is what forces this pass's question. It put 115 of 296 rows
# (38.9 %) at `checked`: a suite exists, a live CI system runs it, and it runs
# on a pull request. But `checked` is a claim about a pipeline on GITHUB'S
# INFRASTRUCTURE, and p110 says 200 of 296 rows are one person, so two thirds
# of this shelf has to be vendored at a SHA and owned in a client's own
# estate. The moment the suite moves off GitHub Actions, "CI runs the suite"
# decays into "a suite ran once, against whatever the registries served that
# morning".
#
# So p112 asks the question that decides whether p111's verdict SURVIVES being
# taken off GitHub: can the dependency set be resolved to the same bytes
# twice? It is the second axis read from the TREE (p111 was the first) and the
# first one that is about REPRODUCIBILITY rather than intent.
#
# CHANNEL. Anonymous git lane only, re-probed live at pass 112:
#   git ls-remote / git fetch                 rc=0
#   raw.githubusercontent.com/<slug>/HEAD/..  200
#   api.github.com                            403   (P107-A, session scoping)
# The tree comes from a depth-1 blob-filtered fetch; requirement-file BODIES
# come from a batched lazy blob fetch against the same promisor remote, the
# mechanism p111 established at P111-H.
#
# ---------------------------------------------------------------------------
# DISCIPLINES. P112-A..C and P112-G live in manifests.awk beside the code they
# govern; the rest are properties of this driver.
#
# P112-D  A COMMITTED DEPENDENCY TREE IS THE STRONGEST FORM OF THE PROPERTY,
#   NOT AN ABSENCE OF IT. A repo carrying node_modules/ or a Go vendor/ needs
#   no registry to stand up at all. p111 stripped these directories for
#   arithmetic; p112 strips them too AND records that they were there, so a
#   lockless row with its dependencies committed is never reported as
#   `floating`. Build residue (.venv, site-packages, .tox, *.egg-info) is
#   stripped WITHOUT that credit: it is a machine's leftovers, not a
#   declaration.
#
# P112-E  LOCK REACH IS NOT MEASURED, AND THE ERROR DIRECTION IS STATED.
#   An ecosystem counts as locked if ONE lockfile for it exists anywhere in
#   the tree. In a monorepo with forty package.json files and one root
#   package-lock.json that is generous. Like p111's textual CI read, the error
#   can only make a row look MORE reproducible than it is, never less, so
#   every figure this script produces is an UPPER BOUND on pinning. Said here
#   rather than discovered later.
#
# P112-F  A `requirements.txt` PINNED WITH `==` IS A LOCK, AND NO FILENAME CAN
#   TELL YOU WHICH KIND YOU HAVE. Python is the dominant ecosystem on an
#   education-and-AI shelf. Ruling every requirements.txt `floating` on the
#   strength of its name would be the p111-F error in a new costume --
#   alarmist about repositories that are already doing the right thing. So
#   stage B reads the BODIES: a file is a lock when it carries at least one
#   real requirement line and EVERY one of them is pinned (`==`, or a PEP 508
#   direct reference). Lines that are comments, pip options, `-r` includes or
#   `-e .` self-installs are not requirements and are skipped.
#
# P112-H  THE BATCH STREAM CARRIES HEADERS THAT LOOK LIKE REQUIREMENTS.
#   `git cat-file --batch` interleaves `<sha> blob <size>` lines between
#   bodies. Those lines are not comments, do not start with `-`, and carry no
#   `==`, so a naive line scan reads every one of them as an UNPINNED
#   requirement -- and a repository whose requirements are perfectly pinned
#   reports as floating, with the error growing as the number of requirement
#   files grows. Header lines are dropped on an anchored 40-hex pattern.
#
# P112-I  INHERITED FROM P111-I: `set -o pipefail` + an early-exiting reader
#   INVERTS a signal. Bodies go to a FILE and every probe reads the FILE.
#
# P112-J  A VACUOUS FILE IS NOT A PINNED FILE. A requirements file containing
#   only `-r base.txt` has no unpinned line in it, and counting it as a lock
#   would promote a row on the strength of a file that declares nothing. A
#   file is only evidence when it holds at least one real requirement line.
#
# P1040  AN UNREAD ROW IS NEVER ZERO. rc!=0 emits UNREAD with empty metrics,
#   so a fetch failure is never arithmetically indistinguishable from a repo
#   that genuinely declares no dependencies.
# ---------------------------------------------------------------------------
#
# VERDICT LADDER (one per row, decision-grade, worst to best):
#   UNREAD       fetch failed; no claim made
#   no-manifest  nothing declares dependencies -> not applicable (specs,
#                corpora, awesome-lists, and the p111 `no-code` rows)
#   foreign-build  dependencies ARE declared, in a build system this
#                instrument does not resolve (bazel, odoo, moodle plugin,
#                cmake, conan, vcpkg) -> no reproducibility claim is made in
#                either direction (P112-N)
#   floating     manifests, no lock for any lockable ecosystem, nothing
#                vendored -> two installs are two different programs
#   partial-pin  some lockable ecosystems locked, others not -> the polyglot
#                failure: the Python half pinned, the Node half not
#   self-pinned  only self-pinning manifests (maven) -> direct versions
#                literal, transitives resolved rather than locked
#   vendored     no lock, but the dependency tree is COMMITTED -> stands up
#                with no registry at all (P112-D)
#   pinned       every lockable ecosystem present is locked
#
# Output TSV:
#   slug rc files vendor_stripped manifests ecosystems lockable locked
#   lockfiles deps_in_tree reqs_pinned deployable verdict
set -uo pipefail
cd "$(dirname "$0")"

list="${1:-addresses.txt}"
workroot="${P112_WORK:-${TMPDIR:-/tmp}/p112work}"
# BASE lets the test suite point this same code at real git repositories
# served over file:// -- the script is never handed a mock, only a different
# transport.
BASE="${P112_BASE:-https://github.com}"
# P112_NO_BODY=1 skips stage B. It exists so the P112-F contribution can be
# MEASURED on this shelf rather than asserted, never to report a figure.
NO_BODY="${P112_NO_BODY:-0}"

mkdir -p "$workroot"

printf 'slug\trc\tfiles\tvendor_stripped\tmanifests\tecosystems\tlockable\tlocked\tlockfiles\tdeps_in_tree\treqs_pinned\tdeployable\tverdict\n'

while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac

  d="$workroot/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$d"; mkdir -p "$d"
  git init -q --bare "$d" 2>/dev/null

  case "$slug" in
    *://*) url="$slug" ;;
    *)     url="$BASE/$slug" ;;
  esac

  # Promisor config FIRST, so stage B's lazy blob fetch has a remote to
  # resolve against (P111-H, reused).
  git --git-dir="$d" remote add origin "$url" 2>/dev/null
  git --git-dir="$d" config remote.origin.promisor true
  git --git-dir="$d" config remote.origin.partialclonefilter blob:none

  if ! git --git-dir="$d" fetch -q --depth=1 --filter=blob:none origin HEAD 2>/dev/null; then
    # One retry without the partial-clone filter: a few servers refuse it.
    # Blobs then arrive eagerly, so stage B still works, offline.
    if ! git --git-dir="$d" fetch -q --depth=1 origin HEAD 2>/dev/null; then
      printf '%s\t1\t\t\t\t\t\t\t\t\t\t\tUNREAD\n' "$slug"
      rm -rf "$d"
      continue
    fi
  fi

  tree=$(git --git-dir="$d" ls-tree -r FETCH_HEAD 2>/dev/null)
  if [ -z "$tree" ]; then
    printf '%s\t0\t0\t0\t0\t-\t0\t0\t0\t0\t0\t0\tno-manifest\n' "$slug"
    rm -rf "$d"
    continue
  fi

  reqsha="$d.reqsha"; : > "$reqsha"
  eval "$(printf '%s\n' "$tree" | awk -v reqsha="$reqsha" -f manifests.awk)"

  # ---- stage B: are the Python requirement files themselves locks? --------
  reqpin=0
  if [ "$reqs" -gt 0 ] && [ "$NO_BODY" != 1 ] && [ -s "$reqsha" ]; then
    bodyf="$d.body"
    cut -f1 "$reqsha" | timeout 180 git --git-dir="$d" cat-file --batch \
      > "$bodyf" 2>/dev/null
    if [ -s "$bodyf" ]; then
      # P112-I: read the FILE. P112-H: drop the batch headers. P112-J: a file
      # with no real requirement line is not evidence.
      reqpin=$(awk '
        /^[0-9a-f]{40} (blob|missing)( [0-9]+)?$/ { next }   # P112-H
        { sub(/\r$/, ""); line = $0
          sub(/[ \t]*#.*$/, "", line)                        # trailing comment
          gsub(/^[ \t]+|[ \t]+$/, "", line)
          if (line == "")            next
          if (line ~ /^-/)           next                    # -r, -e, --flags
          if (line ~ /^[0-9a-f]{40}$/) next
          real++
          if (line ~ /==/)           { pinned++; next }
          if (line ~ /@/)            { pinned++; next }      # PEP 508 direct
        }
        END { print (real > 0 && real == pinned) ? 1 : 0 }   # P112-J
      ' "$bodyf")
      [ -n "$reqpin" ] || reqpin=0
    fi
    rm -f "$bodyf"
  fi
  rm -f "$reqsha"; rm -rf "$d"

  # P112-F. A fully pinned requirements set locks the `py` ecosystem exactly
  # as a poetry.lock does. Credit it once, and never above the number of
  # lockable ecosystems present.
  locked_eff=$lockedcnt
  if [ "$reqpin" = 1 ]; then
    case ",$ecos," in
      *,py,*)
        # Credit it only if no real py lockfile already counted it, and never
        # above the number of lockable ecosystems present.
        case ",$lockedlist," in
          *,py,*) ;;
          *) locked_eff=$((lockedcnt + 1)) ;;
        esac
        ;;
    esac
  fi

  # ---- verdict ladder -----------------------------------------------------
  if [ "$man" -eq 0 ] && [ "$foreign" -gt 0 ]; then
    verdict=foreign-build                                # P112-N
  elif [ "$man" -eq 0 ]; then
    verdict=no-manifest
  elif [ "$lockable" -eq 0 ]; then
    verdict=self-pinned                                  # P112-B (maven only)
  elif [ "$locked_eff" -ge "$lockable" ]; then
    verdict=pinned
  elif [ "$locked_eff" -gt 0 ]; then
    verdict=partial-pin
  elif [ "$depstree" -eq 1 ]; then
    verdict=vendored                                     # P112-D
  else
    verdict=floating
  fi

  printf '%s\t0\t%d\t%d\t%d\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%s\n' \
    "$slug" "$files" "$vendor" "$man" "$ecos" "$lockable" "$locked_eff" \
    "$lockf" "$depstree" "$reqpin" "$deploy" "$verdict"
done < "$list"
