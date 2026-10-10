#!/usr/bin/env bash
# vsurface.sh — VERIFICATION-SURFACE census over this KB's shelf addresses.
#
# WHY THIS AXIS, AND WHY NOW. Four passes have measured this shelf's
# maintenance and all four read the HISTORY:
#   p107 tag COUNT       how much ref traffic
#   p108 release IDENTITY  can I pin it
#   p109 commit RECENCY    is it alive
#   p110 author CONCENTRATION  what happens if they stop
# p110's result forces this pass's question. 200 of 296 rows (67.6 %) are
# `solo`, so for two thirds of this shelf the engagement decision is NOT
# "depend on it", it is "vendor it at a SHA and own it". Owning a tree is only
# tractable if the tree can tell you when you have broken it.
#
# So p111 is the first axis on this shelf read from the TREE rather than from
# the history: does HEAD ship a test suite, does it ship a CI configuration,
# and does that configuration actually run the suite on a change that arrives
# as a pull request.
#
# CHANNEL. Anonymous git lane only, re-probed live at pass 111:
#   git ls-remote / git fetch                 rc=0
#   raw.githubusercontent.com/<slug>/HEAD/..  200
#   api.github.com                            403   (P107-A, session scoping)
# So /contents and /actions cannot be read. The tree comes from a depth-1
# blob-filtered fetch; CI file BODIES come from a batched lazy blob fetch
# against the same promisor remote (P111-H).
#
# ---------------------------------------------------------------------------
# DISCIPLINES, each of which an earlier draft of this script got wrong.
#
# P111-A  A PATH COMPONENT, NEVER A SUBSTRING.
#   `grep -i test` over a tree matches docs/testimonials.rst, src/latest.py,
#   contest/, protest.js and greatest.h. All five shapes are on this shelf;
#   tutor alone contributes docs/testimonials.rst. Directory matches are
#   component-exact and filename matches are separator-anchored (`test_`,
#   `test-`, `_test.`, `.test.`), never a bare `test*` prefix.
#
# P111-B  DEPTH 1 IS ENOUGH, AND DEEPER WOULD BE WRONG.
#   This INVERTS p110-D deliberately. p110 measured a property of history, so
#   its window was load-bearing and — because --depth is a GENERATION limit —
#   its windows were NOT comparable across rows. A tree property needs exactly
#   one commit, every row is read at exactly the same depth, so p111's rows
#   ARE comparable to each other in a way p110's never were.
#
# P111-C  A VENDORED SUITE IS NOT THIS REPO'S SUITE.
#   node_modules/, vendor/, third_party/, site-packages/, Pods/, .tox/ carry
#   thousands of UPSTREAM test files. Left in, the one repo on the shelf with
#   a committed dependency tree reads as the best-tested row on it. Vendor
#   paths are dropped before any arithmetic and COUNTED, so the drop is
#   auditable rather than silent.
#
# P111-D  A CI CONFIG FOR A SERVICE THAT NO LONGER RUNS IS NOT CI.
#   Travis CI ended its free open-source tier; a .travis.yml is a fossil, not
#   a check. Counting "has CI" over all systems therefore overstates the
#   shelf. ci_systems is emitted per row so a travis-only row is visible, and
#   the verdict ladder refuses to call such a row checked.
#
# P111-E  RUNNER CONFIG IS NOT A TEST, AND A BUILD MANIFEST IS NOT RUNNER
#   CONFIG. tox.ini / phpunit.xml / jest.config.js are evidence a suite is
#   MEANT to be run, so they get their own column instead of inflating the
#   test count. pyproject.toml, package.json and setup.cfg are NOT counted:
#   they merely CAN carry a [tool.pytest] table, and counting them makes
#   nearly every Python and Node row on the shelf read as having a suite.
#
# P111-F  "NO TESTS" IS NOT A DEFECT IN A REPO WITH NO CODE.
#   This shelf holds specifications, awesome-lists, curriculum datasets and
#   corpora. A spec with no test suite is correctly bare and is NOT a risk,
#   so src_files gates the verdict: a row with no source files is `no-code`,
#   not `bare`. Without this gate the headline figure is both wrong and
#   alarmist — the failure mode prior passes of this KB have flagged most.
#
# P111-G  A CHECK THAT DOES NOT RUN ON A PULL REQUEST DOES NOT CHECK A FORK.
#   This is the whole point of the axis. p110 says two thirds of the shelf
#   must be forked. A workflow triggered only by `push` to the UPSTREAM's own
#   branches never runs on a contributor's topic branch or on the PR that
#   carries it back. Such a row has CI and a suite and still cannot tell a
#   forker whether their change is sound.
#
# P111-H  THE CI BODY IS READ, NOT INFERRED FROM ITS FILENAME.
#   `.github/workflows/test.yml` is a filename, not a guarantee; `ci.yml` and
#   `main.yml` routinely hold the only test job. Bodies are read through a
#   single BATCHED `git cat-file --batch` per repo against the promisor
#   remote: 8 blobs in 2.6 s measured, versus one round trip each.
#   The read is a TEXTUAL one and this script claims nothing more: it reports
#   that a config NAMES a test runner and MENTIONS a pull_request trigger. It
#   does not execute the graph, so a runner named inside a job that is gated
#   off still counts. The direction of that error is known and stated: it can
#   only make a row look MORE checked than it is, never less.
#
# P111-I  `set -o pipefail` + `grep -q` INVERTS AN EARLY MATCH.
#   `printf '%s' "$body" | grep -q PAT` is false when PAT matches EARLY: grep
#   exits at the first hit, the writer takes SIGPIPE (141), and pipefail makes
#   that the pipeline's status. Measured here, not reasoned about: oppia/oppia
#   contains `pull_request` 39 times, first in the opening workflow, and the
#   piped form reported ci_on_pr=0 while the runner probe — whose term appears
#   LATE — reported 1 from the same bytes. Every body probe therefore greps a
#   FILE. The failure is silent, it points the wrong way, and it is worst
#   exactly where the signal is strongest.
#
# P1040  AN UNREAD ROW IS NEVER ZERO. rc!=0 emits UNREAD with empty metrics,
#   so a fetch failure is never arithmetically indistinguishable from a repo
#   that genuinely ships no tests.
# ---------------------------------------------------------------------------
#
# VERDICT LADDER (one per row, decision-grade, worst to best):
#   UNREAD       fetch failed; no claim made
#   no-code      no source files at HEAD -> verification not applicable (P111-F)
#   bare         has source, no suite, no CI -> you are on your own
#   tests-only   suite present, no CI -> runnable, but nobody runs it
#   ci-only      CI present, no suite -> the pipeline builds; nothing verifies
#   fossil-ci    suite present, but the only CI is a dead service (P111-D)
#   partial      suite + live CI, but no test runner named OR no PR trigger
#   checked      suite + live CI naming a runner AND triggering on pull_request
#
# Output TSV:
#   slug rc files vendor_stripped src_files test_files test_cfg ci_files
#   ci_systems ci_names_runner ci_on_pr verdict
set -uo pipefail
cd "$(dirname "$0")"

list="${1:-addresses.txt}"
workroot="${P111_WORK:-${TMPDIR:-/tmp}/p111work}"
# BASE lets the test suite point this same code at real git repositories
# served over file:// — the script is never handed a mock, only a different
# transport.
BASE="${P111_BASE:-https://github.com}"
# P111_NO_BODY=1 skips stage B. It exists so the P111-H contribution can be
# MEASURED on this shelf rather than asserted, never to report a figure.
NO_BODY="${P111_NO_BODY:-0}"

mkdir -p "$workroot"

# P111-D. Systems that still run builds for open-source repositories.
live_ci() { # ci_systems csv -> 1 if at least one live system present
  case ",$1," in
    *,gha,*|*,gitlab,*|*,circle,*|*,jenkins,*|*,azure,*|*,drone,*|\
    *,woodpecker,*|*,bitbucket,*|*,buildkite,*|*,teamcity,*) return 0 ;;
  esac
  return 1
}

printf 'slug\trc\tfiles\tvendor_stripped\tsrc_files\ttest_files\ttest_cfg\tci_files\tci_systems\tci_names_runner\tci_on_pr\tverdict\n'

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

  # Promisor config FIRST, so the lazy blob fetch of stage B has a remote to
  # resolve against (P111-H).
  git --git-dir="$d" remote add origin "$url" 2>/dev/null
  git --git-dir="$d" config remote.origin.promisor true
  git --git-dir="$d" config remote.origin.partialclonefilter blob:none

  filtered=1
  if ! git --git-dir="$d" fetch -q --depth=1 --filter=blob:none origin HEAD 2>/dev/null; then
    # One retry without the partial-clone filter: a few servers refuse it.
    # Blobs then arrive eagerly, so stage B still works, offline.
    filtered=0
    if ! git --git-dir="$d" fetch -q --depth=1 origin HEAD 2>/dev/null; then
      printf '%s\t1\t\t\t\t\t\t\t\t\t\tUNREAD\n' "$slug"
      rm -rf "$d"
      continue
    fi
  fi

  tree=$(git --git-dir="$d" ls-tree -r FETCH_HEAD 2>/dev/null)
  if [ -z "$tree" ]; then
    printf '%s\t0\t0\t0\t0\t0\t0\t0\t-\t\t\tno-code\n' "$slug"
    rm -rf "$d"
    continue
  fi

  cishas="$d.cishas"; : > "$cishas"
  eval "$(printf '%s\n' "$tree" | awk -v cisha="$cishas" -f classify.awk)"

  runner=""; onpr=""
  if [ "$ci" -gt 0 ] && [ "$NO_BODY" != 1 ] && [ -s "$cishas" ]; then
    # Stage B: ONE batched read for every CI file in this repo (P111-H).
    # P111-I. The body goes to a FILE and every probe greps the FILE. It must
    # never be piped into `grep -q` under `set -o pipefail`: grep exits on the
    # first match, the writer takes SIGPIPE, and pipefail reports the whole
    # pipeline as failed -- so a signal appearing EARLY in the body reads as
    # ABSENT. Measured on oppia/oppia at pass 111: `pull_request` occurs 39
    # times, first in the opening workflow, and the piped form returned "no".
    # The bug is silent and it points the wrong way, hardest at the rows with
    # the strongest signal.
    bodyf="$d.body"
    cut -f1 "$cishas" | timeout 180 git --git-dir="$d" cat-file --batch \
      > "$bodyf" 2>/dev/null
    if [ -s "$bodyf" ]; then
      if grep -qiE \
        'pytest|[^a-z]tox[^a-z]|unittest|nosetests|npm (run )?test|yarn test|pnpm test|jest|vitest|mocha|karma|ava |cypress|playwright test|go test|gotestsum|mvn .*test|gradle.* test|phpunit|behat|codeception|rspec|minitest|cargo test|dotnet test|ctest|bats|rake test|pest|vendor/bin/phpunit|python -m test|make test|make check|tox -e' \
        "$bodyf"; then runner=1; else runner=0; fi
      if grep -qiE 'pull_request|merge_request|pull-request' "$bodyf"; then
        onpr=1; else onpr=0; fi
    fi
    rm -f "$bodyf"
  fi
  rm -f "$cishas"; rm -rf "$d"

  # ---- verdict ladder -----------------------------------------------------
  if [ "$src" -eq 0 ]; then
    verdict=no-code                                   # P111-F
  elif [ "$tests" -eq 0 ] && [ "$ci" -eq 0 ]; then
    verdict=bare
  elif [ "$tests" -gt 0 ] && [ "$ci" -eq 0 ]; then
    verdict=tests-only
  elif [ "$tests" -eq 0 ] && [ "$ci" -gt 0 ]; then
    verdict=ci-only
  elif ! live_ci "$systems"; then
    verdict=fossil-ci                                 # P111-D
  elif [ "$runner" = 1 ] && [ "$onpr" = 1 ]; then
    verdict=checked                                   # P111-G
  else
    verdict=partial
  fi

  printf '%s\t0\t%d\t%d\t%d\t%d\t%d\t%d\t%s\t%s\t%s\t%s\n' \
    "$slug" "$files" "$vendor" "$src" "$tests" "$testcfg" "$ci" \
    "$systems" "$runner" "$onpr" "$verdict"
done < "$list"
