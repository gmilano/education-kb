#!/usr/bin/env bash
# test_p114.sh — suite for the p114 lock-reach instrument.
#
# FULLY OFFLINE AND NOT A MOCK. The unit layer drives positions.awk and
# cover.awk directly with crafted path lists, which is how p112's suite drove
# manifests.awk. The integration layer builds REAL git repositories on disk,
# commits them, and serves them to the REAL reach.sh over `file://` via
# P114_BASE -- the script under test is never handed a stub, only a different
# transport. No network, no api.github.com, no fixtures that pretend to be
# git.
#
# Run:  ./test_p114.sh            (quiet)
#       VERBOSE=1 ./test_p114.sh  (print every assertion)
set -uo pipefail
cd "$(dirname "$0")"
here=$(pwd)

work="${TMPDIR:-/tmp}/p114test.$$"
rm -rf "$work"; mkdir -p "$work"
trap 'rm -rf "$work"' EXIT

pass=0; fail=0
ok()   { pass=$((pass+1)); [ "${VERBOSE:-0}" = 1 ] && printf '  ok   %s\n' "$1"; return 0; }
bad()  { fail=$((fail+1)); printf '  FAIL %s\n     expected: %s\n     actual:   %s\n' "$1" "$2" "$3"; }
eq()   { if [ "$2" = "$3" ]; then ok "$1"; else bad "$1" "$2" "$3"; fi; }
has()  { case "$2" in *"$3"*) ok "$1" ;; *) bad "$1" "contains <$3>" "$2" ;; esac; }
hasnt(){ case "$2" in *"$3"*) bad "$1" "NOT contains <$3>" "$2" ;; *) ok "$1" ;; esac; }

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
# positions: feed a newline path list, get positions.awk output
positions() { printf '%s\n' "$1" | awk -f "$here/positions.awk"; }

# cover: feed positions text (+ optional flat/extrapy), get one key's value
coverval() { # $1 positions text, $2 key, $3 flat, $4 extrapy
  printf '%s\n' "$1" | awk -F'\t' -v flat="${3:-0}" -v extrapy="${4:-}" \
    -f "$here/cover.awk" | awk -F= -v k="$2" '$1==k{sub(/^[^=]*=/,"");print}'
}

# mkrepo <name> <file:content>... — a real git repo with a real commit
mkrepo() {
  local name="$1"; shift
  local r="$work/remotes/$name"
  mkdir -p "$r"
  git init -q "$r"
  git -C "$r" config user.email t@t.t
  git -C "$r" config user.name t
  git -C "$r" config commit.gpgsign false
  local spec path content
  for spec in "$@"; do
    path="${spec%%::*}"; content="${spec#*::}"
    mkdir -p "$r/$(dirname "$path")"
    printf '%b' "$content" > "$r/$path"
  done
  git -C "$r" add -A
  git -C "$r" commit -qm "fixture $name"
  # a bare clone is what a transport actually serves
  git clone -q --bare "$r" "$work/remotes/$name.git" 2>/dev/null
  rm -rf "$r"
  mv "$work/remotes/$name.git" "$work/remotes/$name"
}

# run reach.sh over the planted remotes; echo the row for <slug>
runreach() { # $1 slug-list-file, rest: env assignments already exported
  ( cd "$here" && P114_BASE="file://$work/remotes" P114_WORK="$work/w" \
      ./reach.sh "$1" )
}
row() { awk -F'\t' -v s="$2" '$1==s' <<< "$1"; }
col() { awk -F'\t' -v n="$2" '{print $n}' <<< "$1"; }

echo "=== p114 lock-reach — test suite ==="
echo
echo "--- layer 1: positions.awk (path classification + POSITION) ---"

p=$(positions 'package.json
packages/a/package.json
packages/a/deep/nested/package.json')
eq "root manifest dir is the empty string"      "M	npm		package.json" "$(grep -m1 'package.json$' <<< "$p" | head -1)"
eq "nested manifest carries its directory"      "M	npm	packages/a	packages/a/package.json" "$(grep -m1 'packages/a/package.json' <<< "$p")"
eq "deep manifest carries its full directory"   "M	npm	packages/a/deep/nested	packages/a/deep/nested/package.json" "$(grep 'deep/nested/package.json' <<< "$p")"
eq "three manifests counted"                    "3" "$(awk -F'\t' '$1=="C"&&$2=="man"{print $3}' <<< "$p")"

p=$(positions 'package-lock.json
sub/yarn.lock
go.sum
Cargo.lock
poetry.lock')
eq "root lock position"        "L	npm		package-lock.json" "$(grep 'package-lock' <<< "$p")"
eq "nested lock position"      "L	npm	sub	sub/yarn.lock"     "$(grep 'yarn.lock' <<< "$p")"
eq "go.sum is the go lock"     "L	go		go.sum"            "$(grep 'go.sum' <<< "$p")"
eq "five lockfiles counted"    "5" "$(awk -F'\t' '$1=="C"&&$2=="lockf"{print $3}' <<< "$p")"

# P112-A inherited: basename matching, never substring
p=$(positions 'docs/requirements.rst
docs/requirements.md
requirements.txt
requirements-dev.txt
requirements_test.txt')
eq "requirements.rst is NOT a manifest (P112-A)" "" "$(grep 'requirements.rst' <<< "$p")"
eq "requirements.md is NOT a manifest"           "" "$(grep 'requirements.md' <<< "$p")"
eq "three real requirement files are manifests"  "3" "$(grep -c '^M	py' <<< "$p")"
eq "each requirement file is also an R row"      "3" "$(grep -c '^R' <<< "$p")"

p=$(positions 'description
pkg/description')
eq "root DESCRIPTION is the R ecosystem"     "1" "$(grep -c '^M	r' <<< "$p")"
eq "a nested description is not a manifest"  ""  "$(grep 'pkg/description' <<< "$p")"

p=$(positions 'node_modules/left-pad/package.json
vendor/github.com/x/y/go.mod
third_party/a/package.json
.venv/lib/site-packages/foo/setup.py
build/lib/x/setup.py
src/.tox/py39/x/setup.py
pkg.egg-info/PKG-INFO
package.json')
eq "vendored upstream manifests are stripped"   "1" "$(awk -F'\t' '$1=="C"&&$2=="man"{print $3}' <<< "$p")"
eq "a committed dependency tree is recorded"    "1" "$(awk -F'\t' '$1=="C"&&$2=="depstree"{print $3}' <<< "$p")"
eq "residue is stripped"                        "7" "$(awk -F'\t' '$1=="C"&&$2=="vendor"{print $3}' <<< "$p")"
# residue must NOT earn the vendored credit on its own
p2=$(positions '.venv/lib/site-packages/foo/setup.py
setup.py')
eq "residue alone earns no vendored credit"     "0" "$(awk -F'\t' '$1=="C"&&$2=="depstree"{print $3}' <<< "$p2")"

p=$(positions 'WORKSPACE
addon/__manifest__.py
mod/version.php
CMakeLists.txt')
eq "four foreign build systems detected" "4" "$(awk -F'\t' '$1=="C"&&$2=="foreign"{print $3}' <<< "$p")"
has "bazel is named" "$p" "F	bazel"
has "odoo is named"  "$p" "F	odoo"

p=$(positions 'Dockerfile
deploy/k8s.yaml
charts/app/Chart.yaml
docker-compose.prod.yml')
eq "deployment artefacts counted" "4" "$(awk -F'\t' '$1=="C"&&$2=="deploy"{print $3}' <<< "$p")"

# full ls-tree form, with a tree line and a submodule line that must be ignored
p=$(positions '100644 blob 1111111111111111111111111111111111111111	package.json
040000 tree 2222222222222222222222222222222222222222	packages
160000 commit 3333333333333333333333333333333333333333	ext/sub')
eq "ls-tree form parsed; sha captured"   "1" "$(grep -c '^M	npm' <<< "$p")"
eq "tree and commit entries ignored"     "1" "$(awk -F'\t' '$1=="C"&&$2=="files"{print $3}' <<< "$p")"

echo
echo "--- layer 2: cover.awk (the reach rule, P114-A/B/C/F/H) ---"

POS_ROOTBOTH=$'M\tnpm\t\tpackage.json\nL\tnpm\t\tpackage-lock.json\nC\tdepstree\t0'
eq "root manifest + root lock = full-reach"   "full-reach" "$(coverval "$POS_ROOTBOTH" verdict)"
eq "  covered counts the manifest"            "1"          "$(coverval "$POS_ROOTBOTH" covered)"
eq "  no orphans"                             "0"          "$(coverval "$POS_ROOTBOTH" orphans)"

# THE NEW FAILURE MODE: the lock exists, p112 counts it, nothing reaches the manifest
POS_BELOW=$'M\tnpm\t\tpackage.json\nL\tnpm\texamples/demo\texamples/demo/package-lock.json\nC\tdepstree\t0'
eq "lock BELOW the only manifest = no-reach"  "no-reach" "$(coverval "$POS_BELOW" verdict)"
eq "  orphan recorded"                        "1"        "$(coverval "$POS_BELOW" orphans)"
eq "  the orphan is at the root"              "1"        "$(coverval "$POS_BELOW" root_orphan)"
eq "  locks_live is empty — the lock reached nothing (P114-F)" "-" "$(coverval "$POS_BELOW" locks_live)"
has "  the orphan path is named"  "$(coverval "$POS_BELOW" orphan_paths)" "package.json"
# P114-H: p112's own rule, restored, must disagree — that disagreement IS the measurement
eq "SAME tree under p112's flat rule = full-reach (P114-H)" "full-reach" "$(coverval "$POS_BELOW" verdict 1)"

POS_MONO=$'M\tnpm\t\tpackage.json\nM\tnpm\tpackages/a\tpackages/a/package.json\nM\tnpm\tpackages/b\tpackages/b/package.json\nL\tnpm\t\tpackage-lock.json\nC\tdepstree\t0'
eq "root lock covers workspace members (P114-B)" "full-reach" "$(coverval "$POS_MONO" verdict)"
eq "  all three manifests covered"               "3"          "$(coverval "$POS_MONO" covered)"

POS_PARTIAL=$'M\tnpm\tpackages/a\tpackages/a/package.json\nM\tnpm\tpackages/b\tpackages/b/package.json\nL\tnpm\tpackages/a\tpackages/a/package-lock.json\nC\tdepstree\t0'
eq "a member lock covers only its member"  "partial-reach" "$(coverval "$POS_PARTIAL" verdict)"
eq "  one covered"                         "1"             "$(coverval "$POS_PARTIAL" covered)"
eq "  one orphan"                          "1"             "$(coverval "$POS_PARTIAL" orphans)"
eq "  deepest orphan depth is 2"           "2"             "$(coverval "$POS_PARTIAL" deepest_orphan)"
eq "  no ROOT orphan here"                 "0"             "$(coverval "$POS_PARTIAL" root_orphan)"
eq "  flat rule hides the orphan (P114-H)" "full-reach"    "$(coverval "$POS_PARTIAL" verdict 1)"

# a sibling lock is NOT an ancestor
POS_SIB=$'M\tnpm\tapps/web\tapps/web/package.json\nL\tnpm\tapps/api\tapps/api/package-lock.json\nC\tdepstree\t0'
eq "a sibling lock reaches nothing" "no-reach" "$(coverval "$POS_SIB" verdict)"

# prefix trap: apps/web-legacy must NOT be covered by a lock in apps/web
POS_PREFIX=$'M\tnpm\tapps/web-legacy\tapps/web-legacy/package.json\nL\tnpm\tapps/web\tapps/web/package-lock.json\nC\tdepstree\t0'
eq "a directory-name PREFIX is not an ancestor" "no-reach" "$(coverval "$POS_PREFIX" verdict)"

# ecosystem must match
POS_XECO=$'M\tpy\t\tsetup.py\nL\tnpm\t\tpackage-lock.json\nC\tdepstree\t0'
eq "an npm lock does not cover a python manifest" "no-reach" "$(coverval "$POS_XECO" verdict)"

# P112-K inherited: a lock whose ecosystem has no manifest credits nothing
POS_STRAY=$'L\truby\t\tGemfile.lock\nC\tdepstree\t0'
eq "a stray lock with no manifest = no-manifest" "no-manifest" "$(coverval "$POS_STRAY" verdict)"

# P114-D: the committed tree
POS_VEND=$'M\tnpm\t\tpackage.json\nC\tdepstree\t1'
eq "no lock but a committed tree = vendored (P114-D)" "vendored" "$(coverval "$POS_VEND" verdict)"
POS_NOVEND=$'M\tnpm\t\tpackage.json\nC\tdepstree\t0'
eq "no lock and nothing committed = no-reach"         "no-reach" "$(coverval "$POS_NOVEND" verdict)"

# P114-E: no claim where p112 made none
POS_MVN=$'M\tmaven\t\tpom.xml\nM\tmaven\tmod/a\tmod/a/pom.xml\nC\tdepstree\t0'
eq "maven only = self-pinned (P114-E)"  "self-pinned" "$(coverval "$POS_MVN" verdict)"
eq "  maven manifests are not in the denominator" "0" "$(coverval "$POS_MVN" lockable_man)"
POS_FB=$'F\tbazel\t\tWORKSPACE\nC\tdepstree\t0'
eq "bazel only = foreign-build (P114-E)" "foreign-build" "$(coverval "$POS_FB" verdict)"
has "  the build system is named" "$(coverval "$POS_FB" fbsys)" "bazel"
# a polyglot row is judged on its LOCKABLE half
POS_MIX=$'M\tmaven\t\tpom.xml\nM\tnpm\tui\tui/package.json\nL\tnpm\tui\tui/package-lock.json\nC\tdepstree\t0'
eq "maven + a covered npm half = full-reach" "full-reach" "$(coverval "$POS_MIX" verdict)"
eq "  only the npm manifest is in the denominator" "1" "$(coverval "$POS_MIX" lockable_man)"
eq "  the maven manifest is reported separately"   "1" "$(coverval "$POS_MIX" selfpin_man)"

eq "an empty tree = no-manifest" "no-manifest" "$(coverval "$(printf 'C\tdepstree\t0\n')" verdict)"

# P114-C: a pinned requirements.txt is a lock WHERE IT SITS
POS_REQ=$'M\tpy\t\tsetup.py\nM\tpy\tml\tml/requirements.txt\nR\tabc\tml\tml/requirements.txt\nC\tdepstree\t0'
eq "no stage-B credit: both python manifests orphaned" "no-reach" "$(coverval "$POS_REQ" verdict)"
eq "positional credit covers ml/ only (P114-C)" "partial-reach" "$(coverval "$POS_REQ" verdict 0 "ml")"
eq "  exactly one covered"                      "1"             "$(coverval "$POS_REQ" covered 0 "ml")"
eq "  the root setup.py is the orphan"          "1"             "$(coverval "$POS_REQ" root_orphan 0 "ml")"
# P114-G: the root credit covers the root manifest and NOT the one in ml/
eq "a root pinned requirements file covers its OWN directory only (P114-G)" "partial-reach" "$(coverval "$POS_REQ" verdict 0 "/")"
eq "  the root setup.py is the one covered"          "1"          "$(coverval "$POS_REQ" covered 0 "/")"
eq "  ml/requirements.txt is NOT certified by it"    "1"          "$(coverval "$POS_REQ" orphans 0 "/")"
eq "  reqpin_dirs reports the credit"                "1"          "$(coverval "$POS_REQ" reqpin_dirs 0 "/")"
# and both directories credited covers both
eq "crediting both directories covers both"          "full-reach" "$(coverval "$POS_REQ" verdict 0 "/,ml")"

echo
echo "--- layer 3: reach.sh over REAL git repositories (file:// transport) ---"
mkdir -p "$work/remotes"

mkrepo rootboth 'package.json::{"name":"x","dependencies":{"left-pad":"^1.0.0"}}' \
                'package-lock.json::{"lockfileVersion":3}'
mkrepo lockbelow 'package.json::{"name":"x","dependencies":{"left-pad":"^1.0.0"}}' \
                 'examples/demo/package-lock.json::{"lockfileVersion":3}'
mkrepo monorepo 'package.json::{"workspaces":["packages/*"]}' \
                'package-lock.json::{"lockfileVersion":3}' \
                'packages/a/package.json::{"name":"a"}' \
                'packages/b/package.json::{"name":"b"}'
mkrepo vendored 'package.json::{"name":"x"}' \
                'node_modules/left-pad/package.json::{"name":"left-pad"}' \
                'node_modules/left-pad/index.js::module.exports=1'
mkrepo mavenonly 'pom.xml::<project><modelVersion>4.0.0</modelVersion></project>'
mkrepo bazelonly 'WORKSPACE::workspace(name = "x")' 'src/main.cc::int main(){}'
mkrepo specsonly 'README.md::# a specification, no code' 'spec/qti.xsd::<xs:schema/>'
mkrepo reqpinned 'setup.py::from setuptools import setup\nsetup()' \
                 'ml/requirements.txt::torch==2.3.0\n# a comment\n\nnumpy==1.26.4  # trailing\n'
mkrepo reqvacuous 'requirements.txt::-r base.txt\n--index-url https://example.invalid\n' \
                  'setup.py::setup()'
mkrepo reqfloating 'requirements.txt::torch>=2.0\nnumpy\n'
mkrepo reqcrlf 'requirements.txt::torch==2.3.0\r\nnumpy==1.26.4\r\n'
mkrepo reqtwo 'requirements.txt::torch==2.3.0\n' \
              'svc/requirements.txt::flask==3.0.0\n' \
              'svc/setup.py::setup()'
mkrepo reqmixed 'requirements.txt::torch==2.3.0\n' \
                'dev/requirements-dev.txt::black\n'

cat > "$work/slugs.txt" <<'EOL'
rootboth
lockbelow
monorepo
vendored
mavenonly
bazelonly
specsonly
reqpinned
reqvacuous
reqfloating
reqcrlf
reqtwo
reqmixed
this-remote-does-not-exist
EOL

out=$(runreach "$work/slugs.txt")
v() { row "$out" "$1" | cut -f18; }
f() { row "$out" "$1" | cut -f"$2"; }

eq "rootboth    -> full-reach"    "full-reach"    "$(v rootboth)"
eq "lockbelow   -> no-reach"      "no-reach"      "$(v lockbelow)"
eq "  lockbelow saw the lock"     "1"             "$(f lockbelow 12)"
eq "  but it reached nothing"     "-"             "$(f lockbelow 15)"
eq "monorepo    -> full-reach"    "full-reach"    "$(v monorepo)"
eq "  three manifests covered"    "3"             "$(f monorepo 7)"
eq "vendored    -> vendored"      "vendored"      "$(v vendored)"
eq "mavenonly   -> self-pinned"   "self-pinned"   "$(v mavenonly)"
eq "bazelonly   -> foreign-build" "foreign-build" "$(v bazelonly)"
eq "specsonly   -> no-manifest"   "no-manifest"   "$(v specsonly)"
eq "reqpinned   -> partial-reach (P114-C positional)" "partial-reach" "$(v reqpinned)"
eq "  one requirement directory credited"  "1"    "$(f reqpinned 11)"
eq "  the root setup.py is orphaned"       "1"    "$(f reqpinned 10)"
eq "reqvacuous  -> no-reach (P112-J)"      "no-reach"   "$(v reqvacuous)"
eq "  no directory credited"               "0"    "$(f reqvacuous 11)"
eq "reqfloating -> no-reach"               "no-reach"   "$(v reqfloating)"
eq "reqcrlf     -> full-reach (CRLF bodies)" "full-reach" "$(v reqcrlf)"
eq "reqtwo      -> full-reach (two pinned files, two dirs; P112-H)" "full-reach" "$(v reqtwo)"
eq "  both requirement directories credited" "2"  "$(f reqtwo 11)"
eq "reqmixed    -> partial-reach (one pinned, one not)" "partial-reach" "$(v reqmixed)"
eq "a missing remote is UNREAD, never 0 (P1040)" "UNREAD" "$(v this-remote-does-not-exist)"
eq "  and its rc is 1"                           "1"      "$(f this-remote-does-not-exist 2)"
eq "  and its metrics are EMPTY, not zero"       ""       "$(f this-remote-does-not-exist 7)"

echo
echo "--- layer 4: the two controls, measured on the same trees ---"
out_flat=$(P114_FLAT=1 runreach "$work/slugs.txt")
vf() { row "$out_flat" "$1" | cut -f18; }
eq "FLAT: lockbelow reads full-reach — p112's rule (P114-H)" "full-reach" "$(vf lockbelow)"
eq "FLAT: rootboth unchanged"                               "full-reach" "$(vf rootboth)"
eq "FLAT: vendored unchanged"                               "vendored"   "$(vf vendored)"
# THREE mechanisms separate the rules, and the suite pins each of them:
#   lockbelow  a real lock sits BELOW the only manifest        (P114-B)
#   reqpinned  a DEEP pinned requirements file does not certify
#              the root package it sits under                  (P114-C)
#   reqmixed   a ROOT pinned requirements file does not certify
#              a deeper unpinned one                           (P114-G)
# Nothing else in the fixture set moves, which is the point: position only
# matters where position differs.
eq "FLAT: reqmixed reads full-reach — p112's rule (P114-G)"  "full-reach" "$(vf reqmixed)"
nd=$(paste <(cut -f1,18 <<< "$out") <(cut -f18 <<< "$out_flat") | awk -F'\t' 'NR>1 && $2!=$3' | wc -l)
eq "exactly three fixtures disagree between the rules"      "3"          "$nd"
eq "  and they are the three planted mechanisms" "lockbelow reqpinned reqmixed" "$(paste <(cut -f1,18 <<< "$out") <(cut -f18 <<< "$out_flat") | awk -F'\t' 'NR>1 && $2!=$3{printf "%s ", $1}' | sed 's/ $//')"

out_nb=$(P114_NO_BODY=1 runreach "$work/slugs.txt")
vn() { row "$out_nb" "$1" | cut -f18; }
eq "NO_BODY: reqpinned falls to no-reach — the P114-C contribution" "no-reach" "$(vn reqpinned)"
eq "NO_BODY: reqcrlf falls to no-reach"                             "no-reach" "$(vn reqcrlf)"
eq "NO_BODY: reqvacuous is unaffected"                              "no-reach" "$(vn reqvacuous)"
eq "NO_BODY: rootboth is unaffected"                                "full-reach" "$(vn rootboth)"

# the invariant that makes this pass safe to publish against p112
echo
echo "--- layer 5: the monotonicity invariant (no row may read MORE pinned) ---"
viol=0
while IFS=$'\t' read -r slug reachv flatv; do
  [ "$slug" = slug ] && continue
  # rank: the reach verdict may never be BETTER than the flat (p112) verdict
  rank() { case "$1" in no-reach|floating) echo 1;; vendored) echo 2;; partial-reach|partial-pin) echo 3;; self-pinned) echo 4;; full-reach|pinned) echo 5;; *) echo 0;; esac; }
  r=$(rank "$reachv"); fl=$(rank "$flatv")
  if [ "$r" -gt "$fl" ]; then viol=$((viol+1)); printf '     violation: %s reach=%s flat=%s\n' "$slug" "$reachv" "$flatv"; fi
done < <(paste <(cut -f1,18 <<< "$out") <(cut -f18 <<< "$out_flat"))
eq "no fixture reads more pinned under reach than under p112's rule" "0" "$viol"

echo
echo "=== $pass passed / $fail failed ==="
[ "$fail" -eq 0 ]
