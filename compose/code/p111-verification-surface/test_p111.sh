#!/usr/bin/env bash
# test_p111.sh — offline test suite for the p111 verification-surface census.
#
# NO MOCKS. Every fixture is a REAL git repository, committed on disk and
# served to the real vsurface.sh over `file://` via P111_BASE. The script
# under test is never handed a stub: only a different transport. A fixture
# address that does not exist exercises the UNREAD path for real.
set -uo pipefail
cd "$(dirname "$0")"
HERE="$(pwd)"

ROOT="${TMPDIR:-/tmp}/p111test.$$"
rm -rf "$ROOT"; mkdir -p "$ROOT/fx"
trap 'rm -rf "$ROOT"' EXIT

pass=0; fail=0
ok()   { pass=$((pass+1)); printf '  ok   %s\n' "$1"; }
bad()  { fail=$((fail+1)); printf '  FAIL %s\n       want=[%s] got=[%s]\n' "$1" "$2" "$3"; }
eq()   { if [ "$2" = "$3" ]; then ok "$1"; else bad "$1" "$2" "$3"; fi; }

# ---- fixture builder ------------------------------------------------------
# mkrepo <name> then addf <name> <path> [content...]
mkrepo() {
  local n="$1"; mkdir -p "$ROOT/fx/$n"
  git -C "$ROOT/fx/$n" init -q -b main
  git -C "$ROOT/fx/$n" config user.email t@example.invalid
  git -C "$ROOT/fx/$n" config user.name  tester
}
addf() {
  local n="$1" p="$2"; shift 2
  mkdir -p "$ROOT/fx/$n/$(dirname "$p")"
  if [ "$#" -gt 0 ]; then printf '%s\n' "$@" > "$ROOT/fx/$n/$p"
  else printf 'x\n' > "$ROOT/fx/$n/$p"; fi
}
seal() {
  local n="$1"
  git -C "$ROOT/fx/$n" add -A
  git -C "$ROOT/fx/$n" commit -qm "fixture $n"
}

# run vsurface over a one-line address list, return the row for that slug
row() {
  local slug="$1"
  printf '%s\n' "$slug" > "$ROOT/list"
  P111_BASE="file://$ROOT/fx" P111_WORK="$ROOT/work" \
    "$HERE/vsurface.sh" "$ROOT/list" 2>/dev/null | awk 'NR==2'
}
col() { printf '%s' "$1" | cut -f"$2"; }

# column indices of the output TSV
C_RC=2; C_FILES=3; C_VENDOR=4; C_SRC=5; C_TESTS=6; C_TCFG=7
C_CI=8; C_SYS=9; C_RUNNER=10; C_ONPR=11; C_VERDICT=12

echo "== A. classifier: P111-A false positives are not tests =="
# All five shapes occur on the real shelf; tutor alone carries testimonials.
out=$(printf '%s\n' docs/testimonials.rst src/latest.py contest/entry.py \
      protest.js greatest.h lib/attestation.go README.md | awk -f classify.awk)
eq "testimonials/latest/contest/protest/greatest/attestation -> 0 tests" \
   "tests=0" "$(printf '%s' "$out" | grep '^tests=')"
eq "  ... and they are still counted as source" \
   "src=5" "$(printf '%s' "$out" | grep '^src=')"

echo "== B. classifier: real suite conventions are found =="
for f in tests/test_cli.py test/foo_test.go spec/foo_spec.rb __tests__/a.test.ts \
         src/FooTest.java src/BarTests.cs lib/x_test.php e2e/login.spec.ts \
         testing/helper.py conftest.py; do
  out=$(printf '%s\n' "$f" | awk -f classify.awk)
  eq "test file: $f" "tests=1" "$(printf '%s' "$out" | grep '^tests=')"
done

echo "== C. classifier: P111-E runner config is its own axis =="
out=$(printf '%s\n' tox.ini phpunit.xml jest.config.js .rspec | awk -f classify.awk)
eq "4 runner configs counted as test_cfg" "testcfg=4" "$(printf '%s' "$out" | grep '^testcfg=')"
out=$(printf '%s\n' pyproject.toml package.json setup.cfg | awk -f classify.awk)
eq "build manifests are NOT runner config" "testcfg=0" "$(printf '%s' "$out" | grep '^testcfg=')"

echo "== D. classifier: P111-C vendor trees are stripped =="
out=$(printf '%s\n' node_modules/left-pad/test/index.js vendor/foo/tests/a_test.go \
      third_party/x/spec/y_spec.rb .venv/lib/site-packages/p/tests/t.py \
      Pods/A/Tests/a.m src/app.py | awk -f classify.awk)
eq "5 vendored test files stripped" "vendor=5" "$(printf '%s' "$out" | grep '^vendor=')"
eq "  ... and none counted as this repo's tests" "tests=0" "$(printf '%s' "$out" | grep '^tests=')"

echo "== E. classifier: CI systems are identified =="
for p in ".github/workflows/ci.yml gha" ".gitlab-ci.yml gitlab" ".travis.yml travis" \
         ".circleci/config.yml circle" "Jenkinsfile jenkins" "azure-pipelines.yml azure" \
         ".drone.yml drone" "bitbucket-pipelines.yml bitbucket"; do
  set -- $p
  out=$(printf '%s\n' "$1" | awk -f classify.awk)
  eq "ci system: $1 -> $2" "systems=$2" "$(printf '%s' "$out" | grep '^systems=')"
done
out=$(printf '%s\n' .github/workflows/README.md | awk -f classify.awk)
eq "a README inside workflows/ is not CI" "ci=0" "$(printf '%s' "$out" | grep '^ci=')"

echo "== F. end to end: verdict ladder over real git repos =="

# F1 checked: suite + gha naming a runner and triggering on pull_request
mkrepo checked
addf checked src/app.py "def f(): return 1"
addf checked tests/test_app.py "def test_f(): assert 1"
addf checked .github/workflows/ci.yml \
  "name: ci" "on:" "  pull_request:" "  push:" "jobs:" "  t:" \
  "    steps:" "      - run: pytest -q"
seal checked
r=$(row checked)
eq "checked: verdict"      "checked" "$(col "$r" $C_VERDICT)"
eq "checked: ci_on_pr"     "1"       "$(col "$r" $C_ONPR)"
eq "checked: names_runner" "1"       "$(col "$r" $C_RUNNER)"
eq "checked: test_files"   "1"       "$(col "$r" $C_TESTS)"
eq "checked: src_files"    "1"       "$(col "$r" $C_SRC)"
eq "checked: rc"           "0"       "$(col "$r" $C_RC)"

# F2 P111-I REGRESSION. `pull_request` is the FIRST trigger line and the
# runner term is the LAST line of the body. Under the piped `grep -q` form
# this row returned ci_on_pr=0 -- the bug that shipped in the first draft.
mkrepo earlypr
addf earlypr src/a.js "module.exports = 1"
addf earlypr __tests__/a.test.js "test('x', () => {})"
addf earlypr .github/workflows/a.yml \
  "on:" "  pull_request:" "jobs:" "  t:" "    steps:" \
  "      - run: echo padding" "      - run: echo padding" \
  "      - run: echo padding" "      - run: npm test"
seal earlypr
r=$(row earlypr)
eq "P111-I: early pull_request is FOUND" "1" "$(col "$r" $C_ONPR)"
eq "P111-I: late runner term is FOUND"   "1" "$(col "$r" $C_RUNNER)"
eq "P111-I: verdict"                "checked" "$(col "$r" $C_VERDICT)"

# F3 partial: CI runs a suite but only on push to upstream's own branches,
# so a fork's topic branch and its PR are never checked (P111-G).
mkrepo pushonly
addf pushonly src/app.py "def f(): return 1"
addf pushonly tests/test_app.py "def test_f(): assert 1"
addf pushonly .github/workflows/ci.yml \
  "on:" "  push:" "    branches: [main]" "jobs:" "  t:" "    steps:" \
  "      - run: pytest"
seal pushonly
r=$(row pushonly)
eq "partial (no PR trigger): verdict" "partial" "$(col "$r" $C_VERDICT)"
eq "partial (no PR trigger): on_pr"   "0"       "$(col "$r" $C_ONPR)"
eq "partial (no PR trigger): runner"  "1"       "$(col "$r" $C_RUNNER)"

# F4 partial: PR-triggered CI that never names a test runner (lint only)
mkrepo lintonly
addf lintonly src/app.py "def f(): return 1"
addf lintonly tests/test_app.py "def test_f(): assert 1"
addf lintonly .github/workflows/lint.yml \
  "on:" "  pull_request:" "jobs:" "  l:" "    steps:" "      - run: ruff check ."
seal lintonly
r=$(row lintonly)
eq "partial (no runner named): verdict" "partial" "$(col "$r" $C_VERDICT)"
eq "partial (no runner named): runner"  "0"       "$(col "$r" $C_RUNNER)"
eq "partial (no runner named): on_pr"   "1"       "$(col "$r" $C_ONPR)"

# F5 tests-only: a suite nobody runs
mkrepo testsonly
addf testsonly src/app.py "def f(): return 1"
addf testsonly tests/test_app.py "def test_f(): assert 1"
seal testsonly
r=$(row testsonly)
eq "tests-only: verdict"   "tests-only" "$(col "$r" $C_VERDICT)"
eq "tests-only: ci_files"  "0"          "$(col "$r" $C_CI)"
eq "tests-only: ci_systems" "-"         "$(col "$r" $C_SYS)"

# F6 ci-only: a pipeline with nothing to verify
mkrepo cionly
addf cionly src/app.py "def f(): return 1"
addf cionly .github/workflows/build.yml "on:" "  push:" "jobs:" "  b:" \
  "    steps:" "      - run: make dist"
seal cionly
r=$(row cionly)
eq "ci-only: verdict"    "ci-only" "$(col "$r" $C_VERDICT)"
eq "ci-only: test_files" "0"       "$(col "$r" $C_TESTS)"

# F7 bare: source, no suite, no CI
mkrepo bare
addf bare src/app.py "def f(): return 1"
addf bare README.md "# bare"
seal bare
r=$(row bare)
eq "bare: verdict" "bare" "$(col "$r" $C_VERDICT)"

# F8 P111-F no-code: a spec / dataset / awesome-list is not a defect
mkrepo nocode
addf nocode README.md "# awesome education"
addf nocode data/curriculum.csv "a,b"
addf nocode spec/openbadges.md "# spec"
seal nocode
r=$(row nocode)
eq "no-code: verdict"    "no-code" "$(col "$r" $C_VERDICT)"
eq "no-code: src_files"  "0"       "$(col "$r" $C_SRC)"

# F9 P111-D fossil-ci: a suite whose only CI is a dead service
mkrepo fossil
addf fossil src/app.py "def f(): return 1"
addf fossil tests/test_app.py "def test_f(): assert 1"
addf fossil .travis.yml "language: python" "script: pytest"
seal fossil
r=$(row fossil)
eq "fossil-ci: verdict"    "fossil-ci" "$(col "$r" $C_VERDICT)"
eq "fossil-ci: ci_systems" "travis"    "$(col "$r" $C_SYS)"

# F10 a live system alongside the fossil is NOT a fossil
mkrepo fossilplus
addf fossilplus src/app.py "def f(): return 1"
addf fossilplus tests/test_app.py "def test_f(): assert 1"
addf fossilplus .travis.yml "script: pytest"
addf fossilplus .github/workflows/ci.yml "on:" "  pull_request:" "jobs:" "  t:" \
  "    steps:" "      - run: pytest"
seal fossilplus
r=$(row fossilplus)
eq "travis + gha: verdict is not fossil" "checked" "$(col "$r" $C_VERDICT)"

# F11 P111-C end to end: a committed node_modules must not buy a verdict
mkrepo vendored
addf vendored src/app.js "module.exports=1"
addf vendored node_modules/dep/test/dep.test.js "test('x',()=>{})"
addf vendored node_modules/dep/index.js "module.exports=2"
seal vendored
r=$(row vendored)
eq "vendored suite: verdict stays bare" "bare" "$(col "$r" $C_VERDICT)"
eq "vendored suite: tests not counted"  "0"    "$(col "$r" $C_TESTS)"
eq "vendored suite: strip is counted"   "2"    "$(col "$r" $C_VENDOR)"
eq "vendored suite: vendor src excluded too" "1" "$(col "$r" $C_SRC)"

# F12 P1040 an unread row is never zero
r=$(row no-such-repo-at-all)
eq "UNREAD: verdict"   "UNREAD" "$(col "$r" $C_VERDICT)"
eq "UNREAD: rc"        "1"      "$(col "$r" $C_RC)"
eq "UNREAD: metrics are EMPTY, not 0" "" "$(col "$r" $C_TESTS)"

# F13 gitlab merge_request counts as a PR trigger
mkrepo glab
addf glab src/app.py "def f(): return 1"
addf glab tests/test_app.py "def test_f(): assert 1"
addf glab .gitlab-ci.yml "test:" "  rules:" \
  "    - if: \$CI_PIPELINE_SOURCE == 'merge_request_event'" "  script: pytest"
seal glab
r=$(row glab)
eq "gitlab: ci_systems"         "gitlab"  "$(col "$r" $C_SYS)"
eq "gitlab: merge_request = PR trigger" "1" "$(col "$r" $C_ONPR)"
eq "gitlab: verdict"            "checked" "$(col "$r" $C_VERDICT)"

# F14 P111-H the body is read, not the filename: a suite is found in
# `main.yml`, and a file NAMED test.yml that runs no suite is not a pass.
mkrepo bodyread
addf bodyread src/app.py "def f(): return 1"
addf bodyread tests/test_app.py "def test_f(): assert 1"
addf bodyread .github/workflows/main.yml "on:" "  pull_request:" "jobs:" "  t:" \
  "    steps:" "      - run: tox -e py3"
seal bodyread
r=$(row bodyread)
eq "P111-H: runner found in main.yml" "1" "$(col "$r" $C_RUNNER)"
mkrepo namedtest
addf namedtest src/app.py "def f(): return 1"
addf namedtest tests/test_app.py "def test_f(): assert 1"
addf namedtest .github/workflows/test.yml "on:" "  pull_request:" "jobs:" "  d:" \
  "    steps:" "      - run: docker build ."
seal namedtest
r=$(row namedtest)
eq "P111-H: test.yml that runs no suite is not checked" "partial" "$(col "$r" $C_VERDICT)"
eq "P111-H:   ... and names no runner"                  "0"       "$(col "$r" $C_RUNNER)"

# F15 P111_NO_BODY makes stage B's contribution measurable, not assumed
printf 'checked\n' > "$ROOT/list"
r=$(P111_BASE="file://$ROOT/fx" P111_WORK="$ROOT/work2" P111_NO_BODY=1 \
     "$HERE/vsurface.sh" "$ROOT/list" 2>/dev/null | awk 'NR==2')
eq "NO_BODY: runner column empty" "" "$(col "$r" $C_RUNNER)"
eq "NO_BODY: falls back to partial, never to checked" "partial" "$(col "$r" $C_VERDICT)"

echo
printf 'test_p111.sh: %d passed / %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
