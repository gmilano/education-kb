#!/usr/bin/env bash
# test_p112.sh — offline test suite for the p112 dependency-closure census.
#
# NO MOCKS. Every fixture is a REAL git repository, committed on disk and
# served to the real depclosure.sh over `file://` via P112_BASE. The script
# under test is never handed a stub: only a different transport. A fixture
# address that does not exist exercises the UNREAD path for real, and the
# stage-B body read goes through a real `git cat-file --batch` against a real
# promisor remote.
set -uo pipefail
cd "$(dirname "$0")"
HERE="$(pwd)"

ROOT="${TMPDIR:-/tmp}/p112test.$$"
rm -rf "$ROOT"; mkdir -p "$ROOT/fx"
trap 'rm -rf "$ROOT"' EXIT

pass=0; fail=0
ok()   { pass=$((pass+1)); printf '  ok   %s\n' "$1"; }
bad()  { fail=$((fail+1)); printf '  FAIL %s\n       want=[%s] got=[%s]\n' "$1" "$2" "$3"; }
eq()   { if [ "$2" = "$3" ]; then ok "$1"; else bad "$1" "$2" "$3"; fi; }

# ---- fixture builder ------------------------------------------------------
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
row() {
  local slug="$1"
  printf '%s\n' "$slug" > "$ROOT/list"
  P112_BASE="file://$ROOT/fx" P112_WORK="$ROOT/work" \
    "$HERE/depclosure.sh" "$ROOT/list" 2>/dev/null | awk 'NR==2'
}
col() { printf '%s' "$1" | cut -f"$2"; }
field() { printf '%s' "$1" | grep "^$2=" ; }

# column indices of the output TSV
C_RC=2; C_FILES=3; C_VENDOR=4; C_MAN=5; C_ECOS=6; C_LOCKABLE=7
C_LOCKED=8; C_LOCKF=9; C_DEPSTREE=10; C_REQPIN=11; C_DEPLOY=12; C_VERDICT=13

echo "== A. classifier: P112-A a manifest is a basename, never a substring =="
out=$(printf '%s\n' docs/requirements.rst doc/requirements.md \
      curriculum/package.json.sample notes/go.mod.txt \
      fixtures/composer.json.tpl README.md | awk -f ../lib/reqname.awk -f manifests.awk)
eq "requirements.rst / .json.sample / .mod.txt / .json.tpl -> 0 manifests" \
   "man=0" "$(field "$out" man)"
out=$(printf '%s\n' package.json requirements.txt composer.json Gemfile \
      go.mod Cargo.toml pom.xml build.gradle mix.exs pubspec.yaml \
      Package.swift app/App.csproj DESCRIPTION pyproject.toml | awk -f ../lib/reqname.awk -f manifests.awk)
eq "fourteen real manifests are all found" "man=14" "$(field "$out" man)"
eq "  ... and they resolve to 13 ecosystems in stable order" \
   "ecos=npm,py,php,ruby,go,rust,maven,gradle,elixir,dart,swift,dotnet,r" \
   "$(field "$out" ecos)"

echo "== B. classifier: requirements variants, and only real ones =="
for f in requirements.txt requirements-dev.txt requirements_test.txt \
         requirements.prod.txt reqs/requirements-ci.txt; do
  out=$(printf '%s\n' "$f" | awk -f ../lib/reqname.awk -f manifests.awk)
  eq "requirement file: $f" "reqs=1" "$(field "$out" reqs)"
done
out=$(printf '%s\n' requirements/base.in requirements.rst | awk -f ../lib/reqname.awk -f manifests.awk)
eq "a .in and a .rst are not requirement files" "reqs=0" "$(field "$out" reqs)"

echo "== C. classifier: lockfiles map to their ecosystem =="
out=$(printf '%s\n' package-lock.json | awk -f ../lib/reqname.awk -f manifests.awk)
eq "package-lock.json -> npm lock" "locks=npm" "$(field "$out" locks)"
for pair in "yarn.lock npm" "pnpm-lock.yaml npm" "bun.lockb npm" \
            "poetry.lock py" "uv.lock py" "Pipfile.lock py" \
            "composer.lock php" "Gemfile.lock ruby" "go.sum go" \
            "Cargo.lock rust" "mix.lock elixir" "pubspec.lock dart" \
            "Package.resolved swift" "packages.lock.json dotnet" \
            "renv.lock r" "gradle.lockfile gradle"; do
  set -- $pair
  out=$(printf '%s\n' "$1" | awk -f ../lib/reqname.awk -f manifests.awk)
  eq "lock $1 -> $2" "locks=$2" "$(field "$out" locks)"
done
out=$(printf '%s\n' gradle/dependency-locks/compileClasspath.lockfile | awk -f ../lib/reqname.awk -f manifests.awk)
eq "gradle dependency-locks dir -> gradle" "locks=gradle" "$(field "$out" locks)"

# P112-K. A lock is evidence only about an ecosystem the repo DECLARES.
out=$(printf '%s\n' Gemfile.lock src/app.rb | awk -f ../lib/reqname.awk -f manifests.awk)
eq "a stray lock with no manifest is reported ..." "locks=ruby" "$(field "$out" locks)"
eq "  ... and never credited" "lockedlist=-" "$(field "$out" lockedlist)"
eq "  ... so it cannot inflate the locked count" "lockedcnt=0" "$(field "$out" lockedcnt)"
out=$(printf '%s\n' Gemfile Gemfile.lock | awk -f ../lib/reqname.awk -f manifests.awk)
eq "manifest + its lock IS credited" "lockedlist=ruby" "$(field "$out" lockedlist)"

echo "== D. classifier: P112-B maven is self-pinning, not lockable =="
out=$(printf '%s\n' pom.xml | awk -f ../lib/reqname.awk -f manifests.awk)
eq "pom.xml is not lockable" "lockable=0" "$(field "$out" lockable)"
eq "pom.xml is self-pinning"  "selfpin=1" "$(field "$out" selfpin)"
out=$(printf '%s\n' build.gradle | awk -f ../lib/reqname.awk -f manifests.awk)
eq "gradle IS lockable (it can lock, and mostly does not)" \
   "lockable=1" "$(field "$out" lockable)"
out=$(printf '%s\n' go.mod | awk -f ../lib/reqname.awk -f manifests.awk)
eq "go is lockable: go.mod without go.sum is an unverified resolve" \
   "lockable=1" "$(field "$out" lockable)"

echo "== E. classifier: P112-D committed deps credited, residue not =="
out=$(printf '%s\n' node_modules/left-pad/package.json src/app.js package.json \
      | awk -f ../lib/reqname.awk -f manifests.awk)
eq "node_modules stripped from the manifest count" "man=1" "$(field "$out" man)"
eq "  ... and recorded as a committed dependency tree" "depstree=1" "$(field "$out" depstree)"
for v in vendor/x/go.mod third_party/y/package.json Pods/A/A.podspec \
         bower_components/b/package.json Godeps/_workspace/x.go; do
  out=$(printf '%s\n' "$v" | awk -f ../lib/reqname.awk -f manifests.awk)
  eq "committed dep tree: $v" "depstree=1" "$(field "$out" depstree)"
done
for r in .venv/lib/site-packages/p/setup.py .tox/py39/lib/x.py \
         foo.egg-info/PKG-INFO venv/lib/x.py; do
  out=$(printf '%s\n' "$r" | awk -f ../lib/reqname.awk -f manifests.awk)
  eq "build residue is NOT a dependency tree: $r" "depstree=0" "$(field "$out" depstree)"
done

echo "== F. classifier: P112-G deployable shape =="
for dpl in Dockerfile Dockerfile.prod docker-compose.yml compose.yaml \
           Procfile k8s/deploy.yaml charts/app/Chart.yaml helm/values.yaml \
           Vagrantfile deploy/prod.yml; do
  out=$(printf '%s\n' "$dpl" | awk -f ../lib/reqname.awk -f manifests.awk)
  eq "deployable: $dpl" "deploy=1" "$(field "$out" deploy)"
done
out=$(printf '%s\n' docs/docker.md src/dockerfiles.py | awk -f ../lib/reqname.awk -f manifests.awk)
eq "prose about docker is not a deployment" "deploy=0" "$(field "$out" deploy)"

echo "== G. end to end: the verdict ladder over real repositories =="
mkrepo nomanifest; addf nomanifest README.md; addf nomanifest spec/openbadges.md; seal nomanifest
r=$(row nomanifest)
eq "a specification repo -> no-manifest" "no-manifest" "$(col "$r" $C_VERDICT)"
eq "  ... rc=0, it was READ" "0" "$(col "$r" $C_RC)"

mkrepo floating; addf floating package.json '{"dependencies":{"react":"^18"}}'
addf floating src/app.js; seal floating
r=$(row floating)
eq "manifest, no lock -> floating" "floating" "$(col "$r" $C_VERDICT)"
eq "  ... one lockable ecosystem" "1" "$(col "$r" $C_LOCKABLE)"
eq "  ... zero locked" "0" "$(col "$r" $C_LOCKED)"

mkrepo pinned; addf pinned package.json '{"dependencies":{"react":"^18"}}'
addf pinned package-lock.json '{"lockfileVersion":3}'; addf pinned src/app.js; seal pinned
r=$(row pinned)
eq "manifest + lock -> pinned" "pinned" "$(col "$r" $C_VERDICT)"

mkrepo partial; addf partial package.json '{}' ; addf partial requirements.txt 'django>=4'
addf partial poetry.lock 'x'; addf partial src/app.py; seal partial
r=$(row partial)
eq "py locked, npm not -> partial-pin" "partial-pin" "$(col "$r" $C_VERDICT)"
eq "  ... two lockable ecosystems" "2" "$(col "$r" $C_LOCKABLE)"
eq "  ... one locked" "1" "$(col "$r" $C_LOCKED)"

mkrepo selfpin; addf selfpin pom.xml '<project><version>1.2.3</version></project>'
addf selfpin src/main/java/A.java; seal selfpin
r=$(row selfpin)
eq "maven only -> self-pinned" "self-pinned" "$(col "$r" $C_VERDICT)"

mkrepo vendored; addf vendored package.json '{"dependencies":{"q":"^1"}}'
addf vendored node_modules/q/index.js; addf vendored node_modules/q/package.json '{}'
addf vendored src/app.js; seal vendored
r=$(row vendored)
eq "no lock but deps committed -> vendored (P112-D)" "vendored" "$(col "$r" $C_VERDICT)"
eq "  ... vendor files were stripped and counted" "2" "$(col "$r" $C_VENDOR)"

r=$(row does-not-exist-anywhere)
eq "a fetch that fails -> UNREAD (P1040)" "UNREAD" "$(col "$r" $C_VERDICT)"
eq "  ... rc=1" "1" "$(col "$r" $C_RC)"
eq "  ... and its metrics are EMPTY, never 0" "" "$(col "$r" $C_LOCKABLE)"

echo "== H. end to end: P112-F a pinned requirements.txt IS a lock =="
mkrepo reqpinned
addf reqpinned requirements.txt '# runtime' 'django==4.2.11' 'celery==5.3.6' \
  'requests==2.31.0  # with a trailing comment'
addf reqpinned src/app.py; seal reqpinned
r=$(row reqpinned)
eq "all-== requirements.txt -> pinned" "pinned" "$(col "$r" $C_VERDICT)"
eq "  ... reqs_pinned flag set" "1" "$(col "$r" $C_REQPIN)"

mkrepo reqfloat
addf reqfloat requirements.txt 'django>=4.2' 'celery==5.3.6'
addf reqfloat src/app.py; seal reqfloat
r=$(row reqfloat)
eq "one unpinned line is enough -> floating" "floating" "$(col "$r" $C_VERDICT)"
eq "  ... reqs_pinned flag clear" "0" "$(col "$r" $C_REQPIN)"

mkrepo reqopts
addf reqopts requirements.txt '-r base.txt' '--index-url https://pypi.org/simple' \
  '-e .' '# nothing else'
addf reqopts src/app.py; seal reqopts
r=$(row reqopts)
eq "P112-J a vacuous requirements file is not a lock" "floating" "$(col "$r" $C_VERDICT)"
eq "  ... reqs_pinned clear on a vacuous file" "0" "$(col "$r" $C_REQPIN)"

mkrepo reqdirect
addf reqdirect requirements.txt 'pkg @ git+https://example.invalid/p@abc123' \
  'django==4.2.11'
addf reqdirect src/app.py; seal reqdirect
r=$(row reqdirect)
eq "a PEP 508 direct reference counts as pinned" "pinned" "$(col "$r" $C_VERDICT)"

echo "== I. P112-H the batch stream's headers are not requirements =="
# Three requirement files, every line pinned. The batch output therefore
# carries three `<sha> blob <size>` header lines between the bodies. If those
# are read as requirement lines this row reports floating -- and the error
# grows with the number of files, i.e. worst where the signal is strongest.
mkrepo reqmulti
addf reqmulti requirements.txt 'django==4.2.11'
addf reqmulti requirements-dev.txt 'pytest==8.0.0'
addf reqmulti requirements/extra.txt 'boto3==1.34.0'
addf reqmulti src/app.py; seal reqmulti
r=$(row reqmulti)
eq "three fully pinned requirement files -> pinned, not floating" \
   "pinned" "$(col "$r" $C_VERDICT)"
eq "  ... all three were seen" "1" "$(col "$r" $C_REQPIN)"

echo "== J. a real lockfile and a pinned requirements set do not double-count =="
mkrepo reqboth
addf reqboth requirements.txt 'django==4.2.11'
addf reqboth poetry.lock 'x'
addf reqboth package.json '{}'
addf reqboth src/app.py; seal reqboth
r=$(row reqboth)
eq "py locked twice still counts once -> partial-pin" "partial-pin" "$(col "$r" $C_VERDICT)"
eq "  ... locked never exceeds lockable" "1" "$(col "$r" $C_LOCKED)"
eq "  ... lockable is 2 (py + npm)" "2" "$(col "$r" $C_LOCKABLE)"

echo "== K. stage B is the measured contribution, not an assertion =="
printf '%s\n' reqpinned > "$ROOT/list"
nob=$(P112_BASE="file://$ROOT/fx" P112_WORK="$ROOT/work" P112_NO_BODY=1 \
      "$HERE/depclosure.sh" "$ROOT/list" 2>/dev/null | awk 'NR==2' | cut -f$C_VERDICT)
eq "without stage B the same repo reads floating" "floating" "$nob"
eq "  ... so P112-F changes this row's verdict" "pinned" \
   "$(col "$(row reqpinned)" $C_VERDICT)"

echo "== L. deployable + floating is the quadrant that matters =="
mkrepo appfloat; addf appfloat package.json '{"dependencies":{"q":"^1"}}'
addf appfloat Dockerfile 'FROM node:20'; addf appfloat src/app.js; seal appfloat
r=$(row appfloat)
eq "a deployed app with no lock -> floating" "floating" "$(col "$r" $C_VERDICT)"
eq "  ... and it is flagged deployable" "1" "$(col "$r" $C_DEPLOY)"
mkrepo libfloat; addf libfloat x.gemspec 'spec'; addf libfloat lib/x.rb; seal libfloat
r=$(row libfloat)
eq "a library with no lock -> floating too" "floating" "$(col "$r" $C_VERDICT)"
eq "  ... but it is NOT deployable, which is the distinction" "0" "$(col "$r" $C_DEPLOY)"

echo "== M2. P112-N a declaration this instrument cannot resolve is not absent =="
for fbp in WORKSPACE MODULE.bazel app/BUILD.bazel rules/defs.bzl \
           addons/x/__manifest__.py addons/y/__openerp__.py \
           blocks/chat/version.php CMakeLists.txt conanfile.txt vcpkg.json; do
  out=$(printf '%s\n' "$fbp" | awk -f ../lib/reqname.awk -f manifests.awk)
  eq "foreign build system: $fbp" "foreign=1" "$(field "$out" foreign)"
done
mkrepo bazelrepo; addf bazelrepo WORKSPACE 'workspace(name="x")'
addf bazelrepo app/BUILD.bazel 'java_library()'; addf bazelrepo app/src/A.java; seal bazelrepo
r=$(row bazelrepo)
eq "a Bazel repo -> foreign-build, NOT no-manifest" "foreign-build" "$(col "$r" $C_VERDICT)"
mkrepo odoorepo; addf odoorepo addons/edu/__manifest__.py "{'depends': ['base']}"
addf odoorepo addons/edu/models/x.py; seal odoorepo
r=$(row odoorepo)
eq "an Odoo addon -> foreign-build" "foreign-build" "$(col "$r" $C_VERDICT)"
mkrepo moodleplug; addf moodleplug version.php 'dependencies = array();'
addf moodleplug lib.php; seal moodleplug
r=$(row moodleplug)
eq "a Moodle plugin -> foreign-build" "foreign-build" "$(col "$r" $C_VERDICT)"
# A foreign build system NEVER outranks a real manifest it ships beside.
mkrepo bazelnpm; addf bazelnpm WORKSPACE 'w'; addf bazelnpm package.json '{}'
addf bazelnpm package-lock.json '{}'; addf bazelnpm src/a.js; seal bazelnpm
r=$(row bazelnpm)
eq "bazel + a locked package.json -> pinned, not foreign-build" "pinned" "$(col "$r" $C_VERDICT)"
# And a repo with NEITHER is still no-manifest: foreign-build is not a catch-all.
mkrepo plainc; addf plainc src/main.c 'int main(){}'; addf plainc Makefile 'all:'; seal plainc
r=$(row plainc)
eq "a plain Makefile repo is still no-manifest" "no-manifest" "$(col "$r" $C_VERDICT)"

echo "== N. nix pins by hash, and flake.lock is its lock =="
out=$(printf '%s\n' flake.nix | awk -f ../lib/reqname.awk -f manifests.awk)
eq "flake.nix is a manifest" "ecos=nix" "$(field "$out" ecos)"
out=$(printf '%s\n' flake.lock | awk -f ../lib/reqname.awk -f manifests.awk)
eq "flake.lock is a lock" "locks=nix" "$(field "$out" locks)"
mkrepo nixrepo; addf nixrepo flake.nix 'x'; addf nixrepo flake.lock 'y'
addf nixrepo src/a.py; seal nixrepo
r=$(row nixrepo)
eq "flake.nix + flake.lock -> pinned" "pinned" "$(col "$r" $C_VERDICT)"

echo "== M. an empty tree is read, not guessed =="
mkrepo emptyish; addf emptyish .gitkeep; seal emptyish
r=$(row emptyish)
eq "a repo with one empty marker file -> no-manifest" "no-manifest" "$(col "$r" $C_VERDICT)"

printf '\n%d passed / %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
