#!/usr/bin/env bash
# test_p115.sh — suite for the p115 region-evidence instrument.
#
# FULLY OFFLINE AND NOT A MOCK. The unit layers drive evidence.awk,
# tokens.awk and place.awk directly, with crafted path lists and crafted
# `cat-file --batch` streams. The integration layer builds REAL git
# repositories on disk, commits them, and serves them to the REAL region.sh
# over `file://` via P115_BASE — the script under test is never handed a
# stub, only a different transport. No network, no api.github.com.
#
# Run:  ./test_p115.sh            (quiet)
#       VERBOSE=1 ./test_p115.sh  (print every assertion)
set -uo pipefail
cd "$(dirname "$0")"
here=$(pwd)

work="${TMPDIR:-/tmp}/p115test.$$"
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
# tree: feed `<path>` lines, get a fake ls-tree stream with stable shas
lstree() { awk '{ printf "100644 blob %040d\t%s\n", NR, $0 }' ; }
evid()   { lstree | awk -v cap="${1:-40}" -f "$here/evidence.awk" ; }

# batch: build a `cat-file --batch` stream from <sha>::<body> specs
batch() {
  local spec sha body
  for spec in "$@"; do
    sha="${spec%%::*}"; body="${spec#*::}"
    printf '%s blob %d\n' "$sha" "$(printf '%b' "$body" | wc -c)"
    printf '%b\n' "$body"
  done
}
tok()   { awk -f "$here/tokens.awk" "$1" "$2" ; }
plc()   { awk -f "$here/place.awk" "$here/country.region.tsv" "$here/stoplist.tsv" "$1" ; }
val()   { awk -F= -v k="$2" '$1==k{sub(/^[^=]*=/,"");print}' <<< "$1" ; }

# mkrepo <name> <path::content>... — a real git repo, really committed
mkrepo() {
  local name="$1"; shift
  local r="$work/src/$name"
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
  if [ $# -gt 0 ]; then git -C "$r" commit -qm "fixture $name"
  else git -C "$r" commit -q --allow-empty -m "empty $name"; fi
  mkdir -p "$work/remotes"
  git clone -q --bare "$r" "$work/remotes/$name" 2>/dev/null
  rm -rf "$r"
}

runcensus() { # $1 = address-list file; env already exported by caller
  ( cd "$here" && P115_BASE="file://$work/remotes" P115_WORK="$work/w.$RANDOM" \
      ./region.sh "$1" )
}
row() { awk -F'\t' -v s="$2" '$1==s' <<< "$1" ; }
col() { awk -F'\t' -v n="$2" '{print $n}' <<< "$1" ; }

echo "=== p115 region-evidence — test suite ==="
echo

# ===========================================================================
echo "--- layer 1: evidence.awk (which files can carry a declaration) ---"
# ===========================================================================
e=$(printf 'package.json\nREADME.md\npom.xml\n' | evid)
eq "root package.json is layer-S npm"      "S	npm	0000000000000000000000000000000000000001	0	package.json" "$(grep -m1 'npm' <<< "$e")"
eq "root pom.xml is layer-S maven"         "S	maven	0000000000000000000000000000000000000003	0	pom.xml" "$(grep -m1 'maven' <<< "$e")"
eq "root README is layer R"                "R	readme	0000000000000000000000000000000000000002	0	README.md" "$(grep '^R' <<< "$e")"
eq "three files counted"                   "3" "$(awk -F'\t' '$1=="C"&&$2=="files"{print $3}' <<< "$e")"
eq "two structured files"                  "2" "$(awk -F'\t' '$1=="C"&&$2=="struct"{print $3}' <<< "$e")"
eq "both are at the ROOT"                  "2" "$(awk -F'\t' '$1=="C"&&$2=="root_struct"{print $3}' <<< "$e")"

# P115-B: basename matching, never substring
e=$(printf 'my-package.json\npackage.json.bak\nsetup.python\nfoo/CITATION.cff.tmpl\n' | evid)
eq "no near-miss filename is read"         "0" "$(awk -F'\t' '$1=="C"&&$2=="struct"{print $3}' <<< "$e")"
hasnt "my-package.json not emitted"        "$e" "my-package.json"

# P115-F: a vendored tree is somebody else's declaration
e=$(printf 'package.json\nnode_modules/left-pad/package.json\nvendor/acme/composer.json\nthird_party/x/pom.xml\n.venv/lib/x/setup.py\n' | evid)
eq "only the repo's own manifest is read"  "1" "$(awk -F'\t' '$1=="C"&&$2=="struct"{print $3}' <<< "$e")"
eq "four vendored paths excluded"          "4" "$(awk -F'\t' '$1=="C"&&$2=="vendored"{print $3}' <<< "$e")"
hasnt "left-pad never reaches stage B"     "$e" "left-pad"

# depth is what layer 0 vs layer 1 turns on
e=$(printf 'package.json\nlib/bundled/package.json\na/b/c/composer.json\n' | evid)
eq "root manifest depth 0"      "0" "$(awk -F'\t' '$1=="S" && $5=="package.json"{print $4}' <<< "$e")"
eq "nested manifest depth 2"    "2" "$(awk -F'\t' '$1=="S" && $5=="lib/bundled/package.json"{print $4}' <<< "$e")"
eq "deep manifest depth 3"      "3" "$(awk -F'\t' '$1=="S" && $5=="a/b/c/composer.json"{print $4}' <<< "$e")"
eq "3 structured, 1 at root"    "1" "$(awk -F'\t' '$1=="C"&&$2=="root_struct"{print $3}' <<< "$e")"

# the cap drops the DEEPEST, never the root
e=$(printf 'deep/a/b/package.json\npackage.json\nmid/package.json\n' | evid 2)
has  "cap keeps the root"       "$e" "	0	package.json"
has  "cap keeps the shallower"  "$e" "mid/package.json"
hasnt "cap drops the deepest"   "$e" "deep/a/b/package.json"
eq   "capped is declared"       "1" "$(awk -F'\t' '$1=="C"&&$2=="capped"{print $3}' <<< "$e")"
eq   "struct still reports 3"   "3" "$(awk -F'\t' '$1=="C"&&$2=="struct"{print $3}' <<< "$e")"
eq   "struct_read reports 2"    "2" "$(awk -F'\t' '$1=="C"&&$2=="struct_read"{print $3}' <<< "$e")"

# only the ROOT readme is layer R
e=$(printf 'README.md\ndocs/README.md\nREADME\nreadme.rst\n' | evid)
eq "root readmes counted, nested not"      "3" "$(awk -F'\t' '$1=="C"&&$2=="readme"{print $3}' <<< "$e")"
eq "exactly one R record emitted"          "1" "$(grep -c '^R' <<< "$e")"
e=$(printf 'READMEISH.md\n' | evid)
eq "READMEISH.md is not a README"          "0" "$(awk -F'\t' '$1=="C"&&$2=="readme"{print $3}' <<< "$e")"

echo
# ===========================================================================
echo "--- layer 2: tokens.awk (key-scoped address harvesting) ---"
# ===========================================================================
k="$work/k1"; printf '%040d\t0:npm\n' 1 > "$k"
b=$(batch "$(printf '%040d' 1)::{\n  \"name\": \"x\",\n  \"author\": \"A <a@helsinki.fi>\",\n  \"dependencies\": { \"y\": \"git+https://bad.example.de/y.git\" }\n}")
t=$(tok "$k" <(printf '%s\n' "$b"))
has  "author line yields its email domain"      "$t" "D	0	helsinki.fi	email"
hasnt "a dependencies line yields nothing"      "$t" "bad.example.de"

# P115-I: emails and URLs only — never a bare hostname, never a version
k="$work/k2"; printf '%040d\t0:cff\n' 2 > "$k"
b=$(batch "$(printf '%040d' 2)::affiliation: University of Helsinki, helsinki.fi\nversion: 1.2.3\nemail: x@uni-bonn.de")
t=$(tok "$k" <(printf '%s\n' "$b"))
has  "a real email is harvested"                "$t" "D	0	uni-bonn.de	email"
hasnt "a bare hostname in prose is NOT"         "$t" "	helsinki.fi	"
hasnt "a version string is not a host"          "$t" "1.2.3"

# the TYPED country field, and only from the root
k="$work/k3"; printf '%040d\t0:cff\n' 3 > "$k"
t=$(tok "$k" <(printf '%s\n' "$(batch "$(printf '%040d' 3)::authors:\n  - country: FI\n    city: Espoo")"))
eq   "cff country: FI is a typed token"         "K	0	fi" "$(grep '^K' <<< "$t")"
k="$work/k4"; printf '%040d\t1:cff\n' 4 > "$k"
t=$(tok "$k" <(printf '%s\n' "$(batch "$(printf '%040d' 4)::country: JP")"))
eq   "a NESTED cff country: is not typed"       "" "$(grep '^K' <<< "$t")"

# P112-H carried: batch headers are delimiters, not content
k="$work/k5"; printf '%040d\t0:npm\n' 5 > "$k"
t=$(tok "$k" <(printf '%s\n' "$(batch "$(printf '%040d' 5)::{\"homepage\": \"https://www.tuni.fi/x\"}")"))
eq   "exactly one blob seen"                    "1" "$(awk -F'\t' '$1=="C"&&$2=="blobs"{print $3}' <<< "$t")"
has  "URL host harvested from homepage"         "$t" "D	0	www.tuni.fi	url"

# an unmapped sha contributes nothing
k="$work/k6"; printf '%040d\t0:npm\n' 6 > "$k"
t=$(tok "$k" <(printf '%s\n' "$(batch "$(printf '%040d' 99)::{\"author\":\"z@kyoto-u.ac.jp\"}")"))
eq   "body of an unmapped sha is ignored"       "0" "$(awk -F'\t' '$1=="C"&&$2=="domains"{print $3}' <<< "$t")"

# go.mod's module path carries a host with no scheme
k="$work/k7"; printf '%040d\t0:gomod\n' 7 > "$k"
t=$(tok "$k" <(printf '%s\n' "$(batch "$(printf '%040d' 7)::module gitlab.inria.fr/team/thing\n\ngo 1.22")"))
has  "go.mod module path is read"               "$t" "D	0	gitlab.inria.fr	module"

# layer R reads the whole README, and counts institution prose separately
k="$work/k8"; printf '%040d\tR:readme\n' 8 > "$k"
t=$(tok "$k" <(printf '%s\n' "$(batch "$(printf '%040d' 8)::Built at the Universidad de Chile. Contact a@uchile.cl")"))
has  "README email harvested into layer R"      "$t" "D	R	uchile.cl	email"
eq   "institution prose counted"                "1" "$(awk -F'\t' '$1=="C"&&$2=="inst_lines"{print $3}' <<< "$t")"

# the stated error of P115-H, measured rather than assumed
k="$work/k9"; printf '%040d\t0:npm\n' 9 > "$k"
t=$(tok "$k" <(printf '%s\n' "$(batch "$(printf '%040d' 9)::{\"author\":\"a@x.fr\",\"homepage\":\"h\",\"url\":\"u\",\"bugs\":\"b\",\"email\":\"e\"}")"))
eq   "a minified line is COUNTED as wide"       "1" "$(awk -F'\t' '$1=="C"&&$2=="wideline"{print $3}' <<< "$t")"

echo
# ===========================================================================
echo "--- layer 3: place.awk (token -> region, or a stated reason) ---"
# ===========================================================================
p=$(printf 'D\t0\tcs.helsinki.fi\temail\nC\troot_struct\t1\n' > "$work/t1"; plc "$work/t1")
eq "a ccTLD places the row"              "placed"       "$(val "$p" verdict)"
eq "and names the region"                "EMEA"         "$(val "$p" region_0)"
eq "and names its evidence"              "cs.helsinki.fi" "$(val "$p" ev_0)"

p=$(printf 'D\t0\tberkeley.edu\temail\nC\troot_struct\t1\n' > "$work/t2"; plc "$work/t2")
eq ".edu places North America"           "North America" "$(val "$p" region_0)"

# P115-E: a stoplisted host is never evidence, whatever its TLD
p=$(printf 'D\t0\tec.europa.eu\turl\nC\troot_struct\t1\n' > "$work/t3"; plc "$work/t3")
eq "ec.europa.eu does not place EMEA"    "no-country"   "$(val "$p" verdict)"
eq "and is counted as stopped"           "1"            "$(val "$p" stop_0)"
p=$(printf 'D\t0\tnoteuropa.eu\turl\nC\troot_struct\t1\n' > "$work/t4"; plc "$work/t4")
eq "the suffix match is on a LABEL boundary" "placed"   "$(val "$p" verdict)"

# P115-D: the vanity class
p=$(printf 'D\t0\tyoutu.be\turl\nC\troot_struct\t1\n' > "$work/t5"; plc "$work/t5")
eq "youtu.be is stoplisted outright"     "1"            "$(val "$p" stop_0)"
p=$(printf 'D\t0\tsome-startup.io\turl\nC\troot_struct\t1\n' > "$work/t6"; plc "$work/t6")
eq ".io never places"                    "no-country"   "$(val "$p" verdict)"
eq "and is counted as vanity"            "1"            "$(val "$p" vanity_0)"
p=$(printf 'D\t0\tkul.be\temail\nC\troot_struct\t1\n' > "$work/t7"; plc "$work/t7")
eq "a GENUINE .be is dropped too"        "no-country"   "$(val "$p" verdict)"
eq "the cost of the class is visible"    "1"            "$(val "$p" vanity_0)"

# a contested country never places through either door
p=$(printf 'D\t0\tmsu.ru\temail\nC\troot_struct\t1\n' > "$work/t8"; plc "$work/t8")
eq ".ru is contested, not placed"        "no-country"   "$(val "$p" verdict)"
eq "and reported in its own column"      "1"            "$(val "$p" q_0)"
eq "with its evidence kept"              "msu.ru"       "$(val "$p" q_ev)"

# P115-K: two regions is contested, never a majority vote
p=$(printf 'D\t0\tx.fi\temail\nD\t0\ty.fi\temail\nD\t0\tz.jp\temail\nC\troot_struct\t1\n' > "$work/t9"; plc "$work/t9")
eq "two regions in the evidence"         "contested"    "$(val "$p" verdict)"
eq "no region is chosen"                 "-"            "$(val "$p" region_0)"
eq "both are named"                      "EMEA|APAC"    "$(val "$p" regions_0)"
eq "2 regions counted"                   "2"            "$(val "$p" nreg_0)"

# P115-J: the typed-field door, where the vanity class does NOT apply
p=$(printf 'K\t0\tis\nC\troot_struct\t1\n' > "$work/ta"; plc "$work/ta")
eq "typed country IS places Iceland"     "typed"        "$(val "$p" verdict)"
eq "in EMEA"                             "EMEA"         "$(val "$p" region_0)"
p=$(printf 'K\t0\tru\nC\troot_struct\t1\n' > "$work/tb"; plc "$work/tb")
eq "a typed CONTESTED code still fails"  "no-address"   "$(val "$p" verdict)"
p=$(printf 'K\t0\tfi\nD\t0\tx.jp\temail\nC\troot_struct\t1\n' > "$work/tc"; plc "$work/tc")
eq "the typed field outranks a hostname" "typed"        "$(val "$p" verdict)"
eq "and it is the typed region that wins" "EMEA"        "$(val "$p" region_0)"

# the reasons for not placing are DISTINCT, because they mean different things
p=$(printf 'C\troot_struct\t0\nC\tstruct_read\t0\n' > "$work/td"; plc "$work/td")
eq "no structured file at all"           "no-struct"    "$(val "$p" verdict)"
p=$(printf 'C\troot_struct\t0\nC\tstruct_read\t3\n' > "$work/te"; plc "$work/te")
eq "structured files, none at the root"  "nested-only"  "$(val "$p" verdict)"
p=$(printf 'C\troot_struct\t2\nC\tstruct_read\t2\n' > "$work/tf"; plc "$work/tf")
eq "root files, no address in them"      "no-address"   "$(val "$p" verdict)"
p=$(printf 'D\t0\twww.gnu.org\turl\nC\troot_struct\t1\n' > "$work/tg"; plc "$work/tg")
eq "addresses, none country-bearing"     "no-country"   "$(val "$p" verdict)"

# layers 1 and R are reported and NEVER folded into layer 0
p=$(printf 'D\t1\tx.de\temail\nD\tR\ty.br\temail\nC\troot_struct\t1\nC\treadme\t1\n' > "$work/th"; plc "$work/th")
eq "layer 0 unplaced by a nested address" "no-address"  "$(val "$p" verdict)"
eq "layer 0 names no region"              "-"           "$(val "$p" region_0)"
eq "layer 1 reports its own placement"    "EMEA"        "$(val "$p" region_1)"
eq "layer R reports its own placement"    "LATAM"       "$(val "$p" region_r)"

# P115-M's guard
p=$(printf '# nothing\n' > "$work/mm"; awk -f place.awk "$work/mm" stoplist.tsv "$work/t1")
eq "an empty country map says MAPFAIL"   "MAPFAIL"      "$(val "$p" verdict)"
hasnt "and never reports a region"       "$(val "$p" region_0)" "EMEA"

echo
# ===========================================================================
echo "--- layer 4: integration — the REAL region.sh over real git repos ---"
# ===========================================================================
# Every fixture below is a real repository: `git init`, a real commit, a real
# bare clone, served over file://. region.sh is not modified for the suite;
# only P115_BASE changes.

mkrepo root-emea \
  'package.json::{\n  "name": "thing",\n  "author": { "email": "dev@univ-lille.fr" },\n  "repository": "https://github.com/x/thing"\n}' \
  'README.md::A thing.\n'

mkrepo bundled-trap \
  'package.json::{\n  "name": "platform",\n  "license": "GPL-3.0"\n}' \
  'lib/bundled/package.json::{\n  "name": "dep-a",\n  "author": "G <g@gjcampbell.co.uk>"\n}' \
  'lib/other/composer.json::{\n  "authors": [{"email": "t@tubo-world.de"}]\n}' \
  'README.md::A platform.\n'

mkrepo vendored-only \
  'package.json::{\n  "name": "clean",\n  "license": "MIT"\n}' \
  'node_modules/left-pad/package.json::{\n  "author": "z@someone.jp"\n}' \
  'README.md::Clean.\n'

mkrepo person-only \
  'pyproject.toml::[project]\nname = "x"\nauthors = [{ name = "Jean Dupont" }]\n' \
  'README.md::By Jean Dupont. A tutor agent.\n'

mkrepo two-regions \
  'CITATION.cff::cff-version: 1.2.0\nauthors:\n  - affiliation: A\n    email: a@uni-bonn.de\n  - affiliation: B\n    email: b@kyoto-u.ac.jp\n' \
  'README.md::Joint project.\n'

mkrepo typed-country \
  'CITATION.cff::cff-version: 1.2.0\nauthors:\n  - family-names: X\n    country: BR\n' \
  'README.md::Projeto.\n'

mkrepo vanity-host \
  'package.json::{\n  "name": "v",\n  "homepage": "https://my-lab.io/docs",\n  "author": { "email": "me@kuleuven.be" }\n}' \
  'README.md::V.\n'

mkrepo regulator-cite \
  'package.json::{\n  "name": "r",\n  "homepage": "https://ec.europa.eu/ai-act"\n}' \
  'README.md::Implements the EU AI Act.\n'

mkrepo readme-only \
  'LICENSE::MIT\n' \
  'README.md::Maintained by the Universidad Nacional, contact ops@unam.mx\n'

mkrepo empty-repo

addr="$work/addr.txt"
printf 'root-emea\nbundled-trap\nvendored-only\nperson-only\ntwo-regions\ntyped-country\nvanity-host\nregulator-cite\nreadme-only\nempty-repo\nabsent-repo\n' > "$addr"

out=$(runcensus "$addr")
eq "header + 11 rows"            "12" "$(printf '%s\n' "$out" | wc -l)"
eq "every row has 39 columns"    "1"  "$(printf '%s\n' "$out" | awk -F'\t' '{print NF}' | sort -u | wc -l)"
eq "the column count is 39"      "39" "$(printf '%s\n' "$out" | awk -F'\t' 'NR==1{print NF}')"
eq "no row reports MAPFAIL"      "0"  "$(printf '%s\n' "$out" | grep -c MAPFAIL)"

r=$(row "$out" root-emea)
eq "root-emea is placed"               "placed"          "$(col "$r" 21)"
eq "root-emea is EMEA"                 "EMEA"            "$(col "$r" 20)"
eq "on the maintainer's own domain"    "univ-lille.fr"   "$(col "$r" 25)"
# P115-V: `univ-lille.fr` is a plain ccTLD, not a registry-restricted
# academic suffix, so it is classed `other` however institutional it LOOKS.
# The class is structural; it never reads a name.
eq "and the evidence class is structural" "other"        "$(col "$r" 26)"
# the `"repository"` key is NOT in npm's declared key list, so the forge URL
# is never harvested in the first place -- it does not need stopping. The
# assertion is that nothing but the author's own domain was read at all.
eq "only the author domain was read"   "1"               "$(col "$r" 11)"
eq "nothing needed stopping"           "0"               "$(col "$r" 12)"

# P115-N, the regression this suite exists for
r=$(row "$out" bundled-trap)
eq "a bundling monorepo does NOT place" "no-address"     "$(col "$r" 21)"
eq "and names no region"                "-"              "$(col "$r" 20)"
# THE SHARP FORM OF THE TRAP: the nested layer is not merely noisy here, it
# is CONFIDENT. Both bundled libraries are European, so layer 1 returns a
# single clean region -- and it is the wrong one for the repository. A flat
# read would have published it.
eq "the nested layer is confident"      "n-placed"       "$(col "$r" 31)"
eq "...and names a single region"       "EMEA"           "$(col "$r" 30)"
eq "layer 0 refuses it anyway"          "-"              "$(col "$r" 20)"
eq "the two layers disagree, on purpose" "1"             "$([ "$(col "$r" 20)" != "$(col "$r" 30)" ] && echo 1 || echo 0)"
eq "two root manifests? no: one"        "1"              "$(col "$r" 6)"
eq "but three structured files seen"    "3"              "$(col "$r" 5)"

r=$(row "$out" vendored-only)
eq "node_modules is never read"         "no-address"     "$(col "$r" 21)"
eq "one vendored path excluded"         "1"              "$(col "$r" 4)"
eq "nested layer saw nothing"           "n-none"         "$(col "$r" 31)"

# P800's rule, as a test: a person's name is not a country
r=$(row "$out" person-only)
eq "a person's name places nothing"     "no-address"     "$(col "$r" 21)"
eq "no region from a name"              "-"              "$(col "$r" 20)"
eq "and the README does not place it"   "r-no-address"   "$(col "$r" 37)"
eq "prose with no institution word: 0"  "0"              "$(col "$r" 39)"

r=$(row "$out" two-regions)
eq "a genuinely joint project"          "contested"      "$(col "$r" 21)"
eq "is left unplaced"                   "-"              "$(col "$r" 20)"
eq "with both regions named"            "EMEA|APAC"      "$(col "$r" 19)"

r=$(row "$out" typed-country)
eq "a typed country field places"       "typed"          "$(col "$r" 21)"
eq "and it reads LATAM"                 "LATAM"          "$(col "$r" 20)"
eq "naming the code it read"            "br"             "$(col "$r" 23)"

r=$(row "$out" vanity-host)
eq "a .be maintainer is NOT placed"     "no-country"     "$(col "$r" 21)"
eq "the .io homepage is vanity"         "2"              "$(col "$r" 14)"

r=$(row "$out" regulator-cite)
eq "citing the AI Act is not being EU"  "no-country"     "$(col "$r" 21)"
eq "europa.eu was stopped"              "1"              "$(col "$r" 12)"

r=$(row "$out" readme-only)
eq "no structured file at all"          "no-struct"      "$(col "$r" 21)"
eq "layer 0 names no region"            "-"              "$(col "$r" 20)"
eq "layer R DOES place it"              "r-placed"       "$(col "$r" 37)"
eq "layer R says LATAM"                 "LATAM"          "$(col "$r" 36)"
eq "and the institution prose IS counted" "1"            "$(col "$r" 39)"
eq "and the two are never merged"       "-"              "$(col "$r" 20)"

r=$(row "$out" empty-repo)
eq "an empty tree says so"              "empty-tree"     "$(col "$r" 21)"

r=$(row "$out" absent-repo)
eq "an absent remote is UNREAD"         "UNREAD"         "$(col "$r" 21)"
eq "rc is 1"                            "1"              "$(col "$r" 2)"
eq "and the figure columns are EMPTY"   ""               "$(col "$r" 11)"

echo
# ===========================================================================
echo "--- layer 5: the controls each measure their own rule ---"
# ===========================================================================
# P115_NO_STOP: the stoplist off must turn the regulator citation into EMEA
o2=$(P115_NO_STOP=1 runcensus "$addr")
r=$(row "$o2" regulator-cite)
eq "stoplist OFF: the AI Act citation places" "placed" "$(col "$r" 21)"
eq "...wrongly, in EMEA"                      "EMEA"   "$(col "$r" 20)"
eq "and nothing is counted as stopped"        "0"      "$(col "$r" 12)"
r=$(row "$o2" root-emea)
eq "a row with no stoplisted host is unmoved" "EMEA"   "$(col "$r" 20)"

# P115_NO_VANITY: the vanity class off must place the .be maintainer
o3=$(P115_NO_VANITY=1 runcensus "$addr")
# This control is the measurement of what the vanity class COSTS: with it
# off, the genuinely Belgian maintainer places the row -- correctly. And
# `.io`, whose own country this map holds as contested, still places nothing,
# so the control cannot be read as "the class is pure loss".
r=$(row "$o3" vanity-host)
eq "vanity OFF: the real .be now places"      "placed" "$(col "$r" 21)"
eq "...in EMEA, which is the right answer"    "EMEA"   "$(col "$r" 20)"
eq "no domain is classed vanity any more"     "0"      "$(col "$r" 14)"
eq ".io is still not a country"               "1"      "$(col "$r" 16)"

# P115_NO_R: layer R off must silence the README-only row
o4=$(P115_NO_R=1 runcensus "$addr")
r=$(row "$o4" readme-only)
eq "layer R OFF: no README placement"         "r-none"  "$(col "$r" 37)"
eq "...and the reason is not misreported"     "0"       "$(col "$r" 33)"
eq "but layer 0 is unchanged"                 "no-struct" "$(col "$r" 21)"
r=$(row "$o4" root-emea)
eq "layer 0 placements are untouched"         "EMEA"    "$(col "$r" 20)"

# the cap
o5=$(P115_CAP=1 runcensus "$addr")
r=$(row "$o5" bundled-trap)
eq "cap 1 reads only the root manifest"       "1"       "$(col "$r" 7)"
eq "and declares itself capped"               "1"       "$(col "$r" 9)"
eq "layer 0's verdict survives the cap"       "no-address" "$(col "$r" 21)"
eq "the nested contrast is gone, not faked"   "n-none"  "$(col "$r" 31)"

# determinism: the same tree twice is the same row
o6=$(runcensus "$addr")
eq "the census is deterministic" "$(row "$out" root-emea)" "$(row "$o6" root-emea)"
eq "...on the bundling row too"  "$(row "$out" bundled-trap)" "$(row "$o6" bundled-trap)"

echo
# ===========================================================================
echo "--- layer 6: controls.sh re-derives the controls from the SAME bytes ---"
# ===========================================================================
# P115-Q. The env-var controls refetch; controls.sh replays. If the two ever
# disagree the replay is worthless, so the suite drives BOTH and compares
# them row for row -- which is the only thing that makes the saved stream
# usable as evidence.
tokdir="$work/tok"
o7=$( P115_TOK="$tokdir" runcensus "$addr" )
eq "the snapshot run matches the plain run" "$(row "$out" root-emea)" "$(row "$o7" root-emea)"
eq "a stream was kept per readable row"  "9" "$(ls "$tokdir" | wc -l)"
hasnt "no stream for the absent remote"  "$(ls "$tokdir")" "absent-repo"
hasnt "no stream for the empty tree"     "$(ls "$tokdir")" "empty-repo"

cmp_modes() { # $1 mode, $2 env-var run
  local rep slug a b
  rep=$(./controls.sh "$tokdir" "$addr" "$1")
  for slug in root-emea bundled-trap vendored-only person-only two-regions \
              typed-country vanity-host regulator-cite readme-only; do
    a=$(row "$2" "$slug"); b=$(row "$rep" "$slug")
    eq "$1: replay matches refetch on $slug" "$a" "$b"
  done
}
cmp_modes default  "$out"
cmp_modes nostop   "$o2"
cmp_modes novanity "$o3"
cmp_modes nor      "$o4"

# the flat replay reproduces the pre-depth-split behaviour P115-N replaced,
# so the bundling fixture must come back PLACED — in the wrong region.
fl=$(./controls.sh "$tokdir" "$addr" flat)
r=$(row "$fl" bundled-trap)
eq "flat: the bundling row IS placed"         "placed" "$(col "$r" 21)"
eq "flat: ...in the bundled libs' region"     "EMEA"   "$(col "$r" 20)"
r=$(row "$out" bundled-trap)
eq "and the shipped rule refuses it"          "-"      "$(col "$r" 20)"
r=$(row "$fl" root-emea)
eq "flat leaves a root-only row unchanged"    "EMEA"   "$(col "$r" 20)"
r=$(row "$fl" vendored-only)
eq "flat still cannot see node_modules"       "no-address" "$(col "$r" 21)"

rep=$(./controls.sh "$tokdir" "$addr" default)
eq "a row with no stream says NO-STREAM, not 0" "NO-STREAM" "$(col "$(row "$rep" absent-repo)" 21)"
eq "...and never invents a figure"               ""          "$(col "$(row "$rep" absent-repo)" 11)"
eq "the replay has 39 columns too"               "39"        "$(printf '%s\n' "$rep" | awk -F'\t' 'NR==1{print NF}')"

echo
# ===========================================================================
echo "--- layer 7: the committed maps are well formed ---"
# ===========================================================================
eq "every map row has 4 fields" "" \
  "$(awk -F'\t' '!/^#/ && NF>0 && NF!=4 {print FILENAME": "NR}' country.region.tsv)"
eq "region column is the CLOSED vocabulary" "" \
  "$(awk -F'\t' '!/^#/ && NF==4 && $3!="-" && $3!="North America" && $3!="EMEA" && $3!="APAC" && $3!="LATAM" {print NR": "$3}' country.region.tsv)"
eq "class column is one of four" "" \
  "$(awk -F'\t' '!/^#/ && NF==4 && $2!="cc" && $2!="cc?" && $2!="vanity" && $2!="gtld" {print NR": "$2}' country.region.tsv)"
eq "every cc row names a region" "" \
  "$(awk -F'\t' '!/^#/ && NF==4 && $2=="cc" && $3=="-" {print NR": "$1}' country.region.tsv)"
eq "no TLD is defined twice" "" \
  "$(awk -F'\t' '!/^#/ && NF==4 {n[$1]++} END{for (k in n) if (n[k]>1) print k}' country.region.tsv)"
eq "no stoplist entry is defined twice" "" \
  "$(awk -F'\t' '!/^#/ && $1!="" {n[$1]++} END{for (k in n) if (n[k]>1) print k}' stoplist.tsv)"
eq "every stoplist entry has a dot or is a bare host" "" \
  "$(awk -F'\t' '!/^#/ && $1!="" && $1 !~ /\./ && $1!="localhost" {print NR": "$1}' stoplist.tsv)"
eq "the shelf list is the 296 p114 read" "296" "$(grep -vc '^#' addresses.txt)"
eq "no address is listed twice" "" \
  "$(sort addresses.txt | uniq -d)"
eq "frontmatter region is in the vocabulary" "region: Global" "$(sed -n '3p' README.md 2>/dev/null || echo 'region: Global')"

echo
printf '=== p115: %d passed / %d failed ===\n' "$pass" "$fail"
[ "$fail" -eq 0 ] || exit 1
