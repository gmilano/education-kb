#!/usr/bin/env bash
# test_p116.sh -- offline suite for the p116 lock-agreement axis.
#
# NO MOCKS, NO NETWORK. Every fixture is a REAL git repository committed on
# disk and served to the REAL agree.sh over file:// via P116_BASE. agree.sh
# does not know it is under test: it runs the same fetch, the same tree walk,
# the same batched blob read and the same comparator it runs against
# github.com. If a test here passes, that code path passed.
#
# Stage 1  agree.py directly   -- the comparator's grammar, per ecosystem
# Stage 2  agree.sh end-to-end -- fetch, root-only rule, worst-wins, controls
set -uo pipefail
cd "$(dirname "$0")"
HERE="$(pwd)"
W="${TMPDIR:-/tmp}/p116test.$$"
rm -rf "$W"; mkdir -p "$W/fix" "$W/repos"
PASS=0; FAIL=0

ok()   { PASS=$((PASS+1)); }
bad()  { FAIL=$((FAIL+1)); printf '  FAIL %s\n    expected: %s\n    actual:   %s\n' "$1" "$2" "$3"; }
eq()   { if [ "$2" = "$3" ]; then ok; else bad "$1" "$2" "$3"; fi; }
has()  { case "$3" in *"$2"*) ok ;; *) bad "$1" "contains '$2'" "$3" ;; esac; }
nothas(){ case "$3" in *"$2"*) bad "$1" "NOT contains '$2'" "$3" ;; *) ok ;; esac; }

w() { mkdir -p "$(dirname "$W/fix/$1")"; cat > "$W/fix/$1"; }

# ---------------------------------------------------------------- stage 1 ----
echo "stage 1: agree.py grammar"

w npm-agree.json      <<'J'
{"dependencies":{"left-pad":"^1.0.0","react":"18.2.0"},"devDependencies":{"jest":"^29"}}
J
w npm-agree.lock      <<'J'
{"lockfileVersion":3,"packages":{"":{"name":"x"},"node_modules/left-pad":{"version":"1.3.0"},"node_modules/react":{"version":"18.2.0"},"node_modules/jest":{"version":"29.7.0"}}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/npm-agree.lock" t/1)
eq "npm v3 all present -> agree"      "t/1	npm	3	3	0	agree	" "$r"

w npm-drift.lock <<'J'
{"lockfileVersion":3,"packages":{"":{"name":"x"},"node_modules/left-pad":{"version":"1.3.0"}}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/npm-drift.lock" t/2)
has "npm missing 2 -> drift"          "drift"   "$r"
has "npm drift counts present"        "	3	1	2	" "$r"
has "npm drift names jest"            "jest"    "$r"
has "npm drift names react"           "react"   "$r"

w npm-v1.lock <<'J'
{"lockfileVersion":1,"dependencies":{"left-pad":{"version":"1.3.0"},"react":{"version":"18.2.0"},"jest":{"version":"29.7.0"}}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/npm-v1.lock" t/3)
has "npm v1 grammar -> agree"         "agree"   "$r"

w npm-scoped.json <<'J'
{"dependencies":{"@babel/core":"^7.0.0","@types/node":"^20"}}
J
w npm-scoped.lock <<'J'
{"lockfileVersion":3,"packages":{"node_modules/@babel/core":{"version":"7.0.0"},"node_modules/@types/node":{"version":"20.1.0"}}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-scoped.json" "$W/fix/npm-scoped.lock" t/4)
has "npm scoped names survive split"  "agree"   "$r"

w npm-nested.lock <<'J'
{"lockfileVersion":3,"packages":{"node_modules/left-pad":{},"node_modules/react":{},"node_modules/jest/node_modules/left-pad":{}}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/npm-nested.lock" t/5)
has "npm nested path -> deepest seg"  "drift"   "$r"
has "npm nested: jest still missing"  "jest"    "$r"

# P116-E: peerDependencies excluded by default, counted under the control
w npm-peer.json <<'J'
{"dependencies":{"react":"18.2.0"},"peerDependencies":{"react-dom":"18.2.0"}}
J
w npm-peer.lock <<'J'
{"lockfileVersion":3,"packages":{"node_modules/react":{"version":"18.2.0"}}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-peer.json" "$W/fix/npm-peer.lock" t/6)
has "P116-E peer excluded -> agree"   "agree"   "$r"
nothas "P116-E peer not in names"     "react-dom" "$r"
r=$(P116_PEER=1 python3 -I "$HERE/agree.py" npm "$W/fix/npm-peer.json" "$W/fix/npm-peer.lock" t/6)
has "P116-E control: peer -> drift"   "drift"   "$r"
has "P116-E control names react-dom"  "react-dom" "$r"

r=$(P116_NO_DEV=1 python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/npm-drift.lock" t/7)
has "NO_DEV drops devDependencies"    "	2	1	1	" "$r"
nothas "NO_DEV: jest not counted"     "jest"    "$r"

w npm-optional.json <<'J'
{"optionalDependencies":{"fsevents":"^2"}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-optional.json" "$W/fix/npm-drift.lock" t/8)
has "optionalDependencies counted"    "fsevents" "$r"

w npm-empty.json <<'J'
{"name":"no-deps","version":"1.0.0"}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-empty.json" "$W/fix/npm-agree.lock" t/9)
has "no deps declared -> empty"       "empty-manifest" "$r"

w bad.json <<'J'
{"dependencies": {"a":
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/bad.json" "$W/fix/npm-agree.lock" t/10)
has "unparseable manifest reported"   "manifest-unparseable" "$r"
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/bad.json" t/11)
has "unparseable lock reported"       "lock-unparseable" "$r"
: > "$W/fix/zero.json"
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/zero.json" "$W/fix/npm-agree.lock" t/12)
has "empty manifest file reported"    "manifest-empty-file" "$r"
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/zero.json" t/13)
has "P116-N empty lock != drift"      "lock-empty-file" "$r"
nothas "P116-N empty lock not drift"  "drift" "$r"
printf '   \n\n  \n' > "$W/fix/ws-only.lock"
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/ws-only.lock" t/13b)
has "P116-N whitespace-only lock too" "lock-empty-file" "$r"

r=$(python3 -I "$HERE/agree.py" npm "$W/fix/nope.json" "$W/fix/npm-agree.lock" t/14)
has "absent blob reported"            "blob-missing" "$r"
r=$(python3 -I "$HERE/agree.py" perl "$W/fix/npm-agree.json" "$W/fix/npm-agree.lock" t/15)
has "unknown ecosystem reported"      "unsupported-eco" "$r"
r=$(python3 -I "$HERE/agree.py" npm 2>/dev/null; echo "rc=$?")
has "bad argv exits 0, never raises"  "rc=0"    "$r"

# composer
w comp.json <<'J'
{"require":{"php":">=8.1","ext-mbstring":"*","lib-curl":"*","composer-runtime-api":"^2","monolog/monolog":"^3"},"require-dev":{"phpunit/phpunit":"^10"}}
J
w comp.lock <<'J'
{"packages":[{"name":"monolog/monolog","version":"3.5.0"}],"packages-dev":[{"name":"phpunit/phpunit","version":"10.5.0"}]}
J
r=$(python3 -I "$HERE/agree.py" composer "$W/fix/comp.json" "$W/fix/comp.lock" t/16)
has "P116-F platform pkgs excluded"   "agree"   "$r"
has "P116-F declared is 2 not 6"      "	2	2	0	" "$r"
nothas "P116-F php not in names"      "php"     "$r"

w comp-drift.lock <<'J'
{"packages":[{"name":"monolog/monolog","version":"3.5.0"}],"packages-dev":[]}
J
r=$(python3 -I "$HERE/agree.py" composer "$W/fix/comp.json" "$W/fix/comp-drift.lock" t/17)
has "composer dev missing -> drift"   "drift"   "$r"
has "composer names phpunit"          "phpunit/phpunit" "$r"
r=$(P116_NO_DEV=1 python3 -I "$HERE/agree.py" composer "$W/fix/comp.json" "$W/fix/comp-drift.lock" t/18)
has "composer NO_DEV -> agree"        "agree"   "$r"

# cargo
w cargo.toml <<'T'
[package]
name = "x"
version = "0.1.0"

[dependencies]
serde = "1.0"
tokio = { version = "1", features = ["full"] }

[dev-dependencies]
criterion = "0.5"

[profile.release]
lto = true
T
w cargo.lock <<'T'
[[package]]
name = "serde"
version = "1.0.1"

[[package]]
name = "tokio"
version = "1.35.0"

[[package]]
name = "criterion"
version = "0.5.1"
T
r=$(python3 -I "$HERE/agree.py" cargo "$W/fix/cargo.toml" "$W/fix/cargo.lock" t/19)
has "cargo all present -> agree"      "agree"   "$r"
has "cargo declared 3 (not profile)"  "	3	3	0	" "$r"
nothas "cargo ignores [profile] keys" "lto"     "$r"
nothas "cargo ignores [package] name" "version	" "$r"

w cargo-drift.lock <<'T'
[[package]]
name = "serde"
version = "1.0.1"
T
r=$(python3 -I "$HERE/agree.py" cargo "$W/fix/cargo.toml" "$W/fix/cargo-drift.lock" t/20)
has "cargo missing -> drift"          "drift"   "$r"
has "cargo names criterion"           "criterion" "$r"
has "cargo names tokio"               "tokio"   "$r"
r=$(P116_NO_DEV=1 python3 -I "$HERE/agree.py" cargo "$W/fix/cargo.toml" "$W/fix/cargo-drift.lock" t/21)
nothas "cargo NO_DEV drops criterion" "criterion" "$r"
r=$(python3 -I "$HERE/agree.py" cargo "$W/fix/cargo.toml" "$W/fix/zero.json" t/21b)
has "P116-N cargo empty lock too"     "lock-empty-file" "$r"
nothas "P116-N cargo empty != drift"  "drift" "$r"

# P116-G: workspace-inherited deps declare nothing at this manifest
w ws.toml <<'T'
[dependencies]
serde = { workspace = true }
tokio = { workspace = true }
T
r=$(python3 -I "$HERE/agree.py" cargo "$W/fix/ws.toml" "$W/fix/cargo-drift.lock" t/22)
has "P116-G workspace=true -> empty"  "empty-manifest" "$r"


# ---- P116-I: the other two npm lock flavours --------------------------------
w yarn-v1.lock <<'Y'
# THIS IS AN AUTOGENERATED FILE. DO NOT EDIT THIS FILE DIRECTLY.
# yarn lockfile v1


left-pad@^1.0.0:
  version "1.3.0"
  resolved "https://registry.yarnpkg.com/left-pad/-/left-pad-1.3.0.tgz#abc"

react@18.2.0:
  version "18.2.0"
  resolved "https://registry.yarnpkg.com/react/-/react-18.2.0.tgz#def"

jest@^29:
  version "29.7.0"
  resolved "https://registry.yarnpkg.com/jest/-/jest-29.7.0.tgz#ghi"
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/yarn-v1.lock" t/30)
has "yarn v1 head parse -> agree"     "agree"  "$r"
has "yarn v1 declared 3/3"            "	3	3	0	" "$r"

w yarn-v1-drift.lock <<'Y'
# yarn lockfile v1

left-pad@^1.0.0:
  version "1.3.0"
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/yarn-v1-drift.lock" "$W/fix/yarn-v1-drift.lock" t/31) # manifest unparseable on purpose
has "yarn: a lock as manifest fails"  "manifest-unparseable" "$r"
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/yarn-v1-drift.lock" t/32)
has "yarn v1 real drift detected"     "drift"  "$r"
has "yarn v1 drift names react"       "react"  "$r"

w yarn-multi.lock <<'Y'
# yarn lockfile v1

"@babel/core@^7.0.0", "@babel/core@^7.1.0":
  version "7.0.0"

"@types/node@^20":
  version "20.1.0"
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-scoped.json" "$W/fix/yarn-multi.lock" t/33)
has "yarn comma-joined heads + scoped" "agree" "$r"

w yarn-berry.lock <<'Y'
__metadata:
  version: 6

"left-pad@npm:^1.0.0":
  version: 1.3.0

"react@npm:18.2.0":
  version: 18.2.0

"jest@npm:^29":
  version: 29.7.0
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/yarn-berry.lock" t/34)
has "yarn berry @npm: spelling"       "agree"  "$r"
nothas "berry __metadata not a name"  "__metadata" "$r"

# P116-K: an ALIASED dependency is keyed under the alias
w npm-alias.json <<'J'
{"dependencies":{"codemirror-v5.17.0":"npm:codemirror@5.17.0","jquery3":"npm:jquery@^3.7.1"}}
J
w yarn-alias.lock <<'Y'
# yarn lockfile v1

"codemirror-v5.17.0@npm:codemirror@5.17.0":
  version "5.17.0"

"jquery3@npm:jquery@^3.7.1":
  version "3.7.1"
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-alias.json" "$W/fix/yarn-alias.lock" t/35)
has "P116-K alias keyed by alias"     "agree"  "$r"
nothas "P116-K no phantom drift"      "drift"  "$r"

w pnpm-v9.lock <<'Y'
lockfileVersion: '9.0'

importers:
  .:
    dependencies:
      left-pad:
        specifier: ^1.0.0
        version: 1.3.0

packages:

  left-pad@1.3.0:
    resolution: {integrity: sha512-aaa}

  react@18.2.0:
    resolution: {integrity: sha512-bbb}

  jest@29.7.0:
    resolution: {integrity: sha512-ccc}

snapshots:

  left-pad@1.3.0: {}
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/pnpm-v9.lock" t/36)
has "pnpm v9 name@version keys"       "agree"  "$r"
nothas "pnpm: 'specifier' not a name" "specifier" "$r"
nothas "pnpm: importers not scanned"  "importers" "$r"

w pnpm-v5.lock <<'Y'
lockfileVersion: 5.4

packages:

  /left-pad/1.3.0:
    resolution: {integrity: sha512-aaa}

  /react/18.2.0:
    resolution: {integrity: sha512-bbb}

  /jest/29.7.0:
    resolution: {integrity: sha512-ccc}
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/pnpm-v5.lock" t/37)
has "pnpm v5 /name/version keys"      "agree"  "$r"

w pnpm-v6-scoped.lock <<'Y'
lockfileVersion: '6.0'

packages:

  /@babel/core@7.0.0:
    resolution: {integrity: sha512-aaa}

  /@types/node@20.1.0:
    resolution: {integrity: sha512-bbb}
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-scoped.json" "$W/fix/pnpm-v6-scoped.lock" t/38)
has "pnpm v6 scoped /@s/n@v keys"     "agree"  "$r"

w pnpm-drift.lock <<'Y'
lockfileVersion: '9.0'

packages:

  left-pad@1.3.0:
    resolution: {integrity: sha512-aaa}
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/pnpm-drift.lock" t/39)
has "pnpm real drift detected"        "drift"  "$r"
has "pnpm drift names jest"           "jest"   "$r"


# ---- P116-Q: pnpm keys an ALIAS under its TARGET in `packages:` -------------
# The real shape, from PrairieLearn/PrairieLearn: the alias is recorded only
# under `importers:`, so a census reading `packages:` alone calls it missing.
w pnpm-alias.json <<'J'
{"devDependencies":{"@typescript/native":"npm:typescript@^7.0.2","typescript":"npm:@typescript/typescript6@^6.0.2"}}
J
w pnpm-alias.lock <<'Y'
lockfileVersion: '9.0'

importers:

  .:
    devDependencies:
      '@typescript/native':
        specifier: npm:typescript@^7.0.2
        version: typescript@7.0.2
      typescript:
        specifier: npm:@typescript/typescript6@^6.0.2
        version: '@typescript/typescript6@6.0.2'

  apps/web:
    dependencies:
      left-pad:
        specifier: ^1.0.0
        version: 1.3.0

packages:

  typescript@7.0.2:
    resolution: {integrity: sha512-aaa}

  '@typescript/typescript6@6.0.2':
    resolution: {integrity: sha512-bbb}
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/pnpm-alias.json" "$W/fix/pnpm-alias.lock" t/50)
has "P116-Q pnpm alias via importers" "agree" "$r"
has "P116-Q declared 2/2"             "	2	2	0	" "$r"
nothas "P116-Q no phantom drift"      "drift" "$r"

# `specifier` and `version` are FIELDS of a dep, never dependency names
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-empty.json" "$W/fix/pnpm-alias.lock" t/51)
has "P116-Q empty manifest unaffected" "empty-manifest" "$r"
w pnpm-field-probe.json <<'J'
{"dependencies":{"specifier":"^1.0.0","version":"^1.0.0","resolution":"^1.0.0"}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/pnpm-field-probe.json" "$W/fix/pnpm-alias.lock" t/52)
has "P116-Q dep FIELDS are not names"  "drift" "$r"
has "P116-Q all three missing"         "	3	0	3	" "$r"

# an importer's deps still count when there is no `packages:` block at all
w pnpm-importers-only.lock <<'Y'
lockfileVersion: '9.0'

importers:

  .:
    dependencies:
      left-pad:
        specifier: ^1.0.0
        version: 1.3.0
      react:
        specifier: 18.2.0
        version: 18.2.0
    devDependencies:
      jest:
        specifier: ^29
        version: 29.7.0
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/pnpm-importers-only.lock" t/53)
has "P116-Q importers-only lock reads" "agree" "$r"

# a non-dependency section under an importer must NOT contribute names
w pnpm-other-sec.lock <<'Y'
lockfileVersion: '9.0'

importers:

  .:
    publishDirectory:
      dist:
        specifier: x
        version: y
Y
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-agree.json" "$W/fix/pnpm-other-sec.lock" t/54)
has "P116-Q non-dep section ignored"  "drift" "$r"
nothas "P116-Q 'dist' not a name"     "dist"  "$r"

# P116-J: a non-registry spec has no lock entry by design
w npm-local.json <<'J'
{"dependencies":{"left-pad":"^1.0.0","my-ui":"workspace:*","my-lib":"link:../lib","vendored":"file:./vendor/x","rel":"../sibling"}}
J
w npm-local.lock <<'J'
{"lockfileVersion":3,"packages":{"node_modules/left-pad":{}}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-local.json" "$W/fix/npm-local.lock" t/40)
has "P116-J local specs excluded"     "agree"  "$r"
has "P116-J declared is 1 not 5"      "	1	1	0	" "$r"
nothas "P116-J workspace: not counted" "my-ui" "$r"

# P116-L: a workspace-local package name is excluded via the supplied set
printf 'my-pkg-a\nmy-pkg-b\n' > "$W/fix/wsnames.txt"
w npm-ws.json <<'J'
{"dependencies":{"left-pad":"^1.0.0","my-pkg-a":"*","my-pkg-b":">=2"}}
J
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-ws.json" "$W/fix/npm-local.lock" t/41)
has "P116-L without ws set -> drift"  "drift"  "$r"
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-ws.json" "$W/fix/npm-local.lock" t/41 "$W/fix/wsnames.txt")
has "P116-L with ws set -> agree"     "agree"  "$r"
has "P116-L declared net of ws = 1"   "	1	1	0	" "$r"
r=$(python3 -I "$HERE/agree.py" npm "$W/fix/npm-ws.json" "$W/fix/npm-local.lock" t/41 "$W/fix/nosuch.txt")
has "P116-L absent ws file tolerated" "drift"  "$r"

# -------------------------------------------------------------- stage 2 ------
echo "stage 2: agree.sh end-to-end over real git repos on file://"

mkrepo() { # mkrepo <name> ; files arrive as "path<NUL>content" via mkfile
  R="$W/repos/$1"; mkdir -p "$R"; git init -q "$R"
  git -C "$R" config user.email t@t; git -C "$R" config user.name t
  git -C "$R" config commit.gpgsign false
}
mkfile() { mkdir -p "$(dirname "$R/$1")"; cat > "$R/$1"; }
commit() { git -C "$R" add -A; git -C "$R" commit -q -m c; git -C "$R" branch -M main; }

run() { P116_BASE="file://$W/repos" P116_WORK="$W/work.$RANDOM" ./agree.sh "$1"; }
field() { awk -F'\t' -v s="$2" -v n="$3" 'NR>1 && $1==s {print $n}' <<<"$1"; }

mkrepo e2e-agree
mkfile package.json      < "$W/fix/npm-agree.json"
mkfile package-lock.json < "$W/fix/npm-agree.lock"
commit

mkrepo e2e-drift
mkfile package.json      < "$W/fix/npm-agree.json"
mkfile package-lock.json < "$W/fix/npm-drift.lock"
commit

mkrepo e2e-shrinkwrap
mkfile package.json        < "$W/fix/npm-agree.json"
mkfile npm-shrinkwrap.json < "$W/fix/npm-agree.lock"
commit

mkrepo e2e-nolock
mkfile package.json < "$W/fix/npm-agree.json"
commit

mkrepo e2e-multi            # npm agrees, composer drifts -> worst wins
mkfile package.json      < "$W/fix/npm-agree.json"
mkfile package-lock.json < "$W/fix/npm-agree.lock"
mkfile composer.json     < "$W/fix/comp.json"
mkfile composer.lock     < "$W/fix/comp-drift.lock"
commit

mkrepo e2e-subdir-drift     # P116-B: the drift is NOT at the root
mkfile package.json      < "$W/fix/npm-agree.json"
mkfile package-lock.json < "$W/fix/npm-agree.lock"
mkfile web/package.json      < "$W/fix/npm-agree.json"
mkfile web/package-lock.json < "$W/fix/npm-drift.lock"
commit

mkrepo e2e-cargo
mkfile Cargo.toml < "$W/fix/cargo.toml"
mkfile Cargo.lock < "$W/fix/cargo-drift.lock"
commit

mkrepo e2e-nomanifest
mkfile README.md <<'M'
nothing to resolve here
M
commit

mkrepo e2e-workspace        # P116-L end to end: dep satisfied from inside the tree
mkfile package.json <<'J'
{"workspaces":["packages/*"],"dependencies":{"left-pad":"^1.0.0","@acme/inner":"*"}}
J
mkfile package-lock.json <<'J'
{"lockfileVersion":3,"packages":{"node_modules/left-pad":{"version":"1.3.0"}}}
J
mkfile packages/inner/package.json <<'J'
{"name":"@acme/inner","version":"1.0.0"}
J
commit

mkrepo e2e-yarn
mkfile package.json < "$W/fix/npm-agree.json"
mkfile yarn.lock    < "$W/fix/yarn-v1.lock"
commit

mkrepo e2e-pnpm
mkfile package.json    < "$W/fix/npm-agree.json"
mkfile pnpm-lock.yaml  < "$W/fix/pnpm-drift.lock"
commit

mkrepo e2e-pnpm-alias       # P116-Q end to end, the PrairieLearn shape
mkfile package.json   < "$W/fix/pnpm-alias.json"
mkfile pnpm-lock.yaml < "$W/fix/pnpm-alias.lock"
commit

mkrepo e2e-lockpref        # package-lock.json wins over yarn.lock when both exist
mkfile package.json      < "$W/fix/npm-agree.json"
mkfile package-lock.json < "$W/fix/npm-agree.lock"
mkfile yarn.lock         < "$W/fix/yarn-v1-drift.lock"
commit

cat > "$W/addr.txt" <<'A'
e2e-pnpm-alias
e2e-workspace
e2e-yarn
e2e-pnpm
e2e-lockpref
e2e-agree
e2e-drift
e2e-shrinkwrap
e2e-nolock
e2e-multi
e2e-subdir-drift
e2e-cargo
e2e-nomanifest
# a comment line must be skipped
A
OUT="$(run "$W/addr.txt")"

eq "e2e rows emitted"            "13" "$(($(wc -l <<<"$OUT")-1))"
eq "P116-Q e2e pnpm alias agrees" "agree" "$(field "$OUT" e2e-pnpm-alias 8)"
eq "P116-L e2e workspace dep excluded" "agree" "$(field "$OUT" e2e-workspace 8)"
eq "P116-L e2e declared net = 1" "1"     "$(field "$OUT" e2e-workspace 5)"
eq "P116-I e2e yarn.lock read"   "agree" "$(field "$OUT" e2e-yarn 8)"
eq "P116-I e2e pnpm drift seen"  "drift" "$(field "$OUT" e2e-pnpm 8)"
eq "P116-I lock preference order" "agree" "$(field "$OUT" e2e-lockpref 8)"
eq "e2e agree verdict"           "agree" "$(field "$OUT" e2e-agree 8)"
eq "e2e agree rc=0"              "0"     "$(field "$OUT" e2e-agree 2)"
eq "e2e agree root_ecos"         "npm"   "$(field "$OUT" e2e-agree 3)"
eq "e2e drift verdict"           "drift" "$(field "$OUT" e2e-drift 8)"
eq "e2e drift missing count"     "2"     "$(field "$OUT" e2e-drift 7)"
has "e2e drift detail names"     "jest"  "$(field "$OUT" e2e-drift 9)"
eq "e2e shrinkwrap honoured"     "agree" "$(field "$OUT" e2e-shrinkwrap 8)"
eq "e2e no lock at root"         "no-lock-grammar" "$(field "$OUT" e2e-nolock 8)"
eq "e2e no lock measured=0"      "0"     "$(field "$OUT" e2e-nolock 4)"
eq "e2e multi worst-wins"        "drift" "$(field "$OUT" e2e-multi 8)"
eq "e2e multi measured both"     "2"     "$(field "$OUT" e2e-multi 4)"
has "e2e multi shows npm agree"  "npm=agree" "$(field "$OUT" e2e-multi 9)"
has "e2e multi shows comp drift" "composer=drift" "$(field "$OUT" e2e-multi 9)"
eq "e2e multi declared summed"   "5"     "$(field "$OUT" e2e-multi 5)"
eq "P116-B subdir drift ignored" "agree" "$(field "$OUT" e2e-subdir-drift 8)"
eq "P116-B subdir measured=1"    "1"     "$(field "$OUT" e2e-subdir-drift 4)"
eq "e2e cargo drift"             "drift" "$(field "$OUT" e2e-cargo 8)"
eq "e2e cargo root_ecos"         "cargo" "$(field "$OUT" e2e-cargo 3)"
eq "e2e no manifest at root"     "no-lock-grammar" "$(field "$OUT" e2e-nomanifest 8)"
eq "e2e no manifest ecos '-'"    "-"     "$(field "$OUT" e2e-nomanifest 3)"
nothas "comment line not a row"  "a comment" "$OUT"

# unreadable address must be a row, never a crash and never a silent drop
cat > "$W/addr2.txt" <<'A'
e2e-agree
does-not-exist-at-all
A
OUT2="$(run "$W/addr2.txt")"
eq "unreadable still emits a row" "2" "$(($(wc -l <<<"$OUT2")-1))"
eq "unreadable -> UNREAD"      "UNREAD" "$(field "$OUT2" does-not-exist-at-all 8)"
eq "unreadable rc=1"           "1"      "$(field "$OUT2" does-not-exist-at-all 2)"
eq "good row unaffected"       "agree"  "$(field "$OUT2" e2e-agree 8)"

# controls end-to-end
mkrepo e2e-peer
mkfile package.json      < "$W/fix/npm-peer.json"
mkfile package-lock.json < "$W/fix/npm-peer.lock"
commit
echo e2e-peer > "$W/addr3.txt"
eq "control: peer excluded by default" "agree" "$(field "$(run "$W/addr3.txt")" e2e-peer 8)"
eq "control: P116_PEER=1 -> drift" "drift" \
   "$(field "$(P116_PEER=1 run "$W/addr3.txt")" e2e-peer 8)"

# idempotence: the same census twice must produce identical bytes
A1="$(run "$W/addr.txt")"; A2="$(run "$W/addr.txt")"
eq "census is idempotent" "same" "$([ "$A1" = "$A2" ] && echo same || echo differs)"

# the header contract the prose and the .tsv both depend on
eq "header is 9 columns" "9" "$(head -1 <<<"$OUT" | awk -F'\t' '{print NF}')"
eq "header col 8 is verdict" "verdict" "$(head -1 <<<"$OUT" | cut -f8)"

printf '\n%s passed / %s failed\n' "$PASS" "$FAIL"
rm -rf "$W"
[ "$FAIL" = 0 ]
