#!/usr/bin/env bash
# test_p113.sh -- the suite for p113-provider-binding.
#
# FULLY OFFLINE AND WITHOUT MOCKS. Every end-to-end case builds a REAL git
# repository on disk, commits real files into it, and serves it to the REAL
# bind.sh over `file://` through P113_BASE. The transport changes; the code
# under test does not. A suite that stubbed `git` would prove the stub works.
#
# P113-O  EVERY CONTAINMENT TRAP GETS A TEST AGAINST THE PAYLOAD SHAPE THAT
#   PRODUCES IT, NOT AGAINST A PARAPHRASE. p1040 lost a whole figure to
#   "Educational Community License" containing "Community License", found it by
#   diffing two census runs, and then needed a THIRD attempt because the real
#   payload split the title across two lines. The lesson taken here: the token
#   table is tested with `openai-whisper==20231117`, `langchain-openai>=0.2`,
#   `OPENAI_API_BASE=http://...`, `sentence-transformers` and `llama-cpp-python`
#   written the way a requirements file writes them.
set -uo pipefail
cd "$(dirname "$0")"
here="$(pwd)"

pass=0; fail=0
ok()   { pass=$((pass+1)); }
bad()  { fail=$((fail+1)); printf 'FAIL: %s\n' "$1" >&2; }
is()   { if [ "$2" = "$3" ]; then ok; else bad "$1: expected [$3] got [$2]"; fi; }
has()  { case "$2" in *"$3"*) ok ;; *) bad "$1: [$2] does not contain [$3]" ;; esac; }
hasnt(){ case "$2" in *"$3"*) bad "$1: [$2] unexpectedly contains [$3]" ;; *) ok ;; esac; }

T="$(mktemp -d)"
trap 'rm -rf "$T"' EXIT
export P113_WORK="$T/work"

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
# tok <<<body  -- run tokens.awk over one manifest payload, byte-exactly framed
tokrun() {                     # $1=kind  $2=body  -> the tokens.awk line
  local kind="$1" body="$2" sha="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  printf '%s\t%s\tf\n' "$sha" "$kind" > "$T/map"
  { printf '%s blob %d\n' "$sha" "${#body}"; printf '%s' "$body"; printf '\n'; } \
    | awk -v map="$T/map" -f tokens.awk
}
fld() { printf '%s' "$1" | cut -f"$2"; }

# mkrepo <name> -- a real git repo; files are added by the caller beforehand in
# $T/src/<name>, then committed here.
mkrepo() {
  local n="$1" s="$T/src/$1"
  git init -q "$s"
  git -C "$s" config user.email t@t; git -C "$s" config user.name t
  git -C "$s" add -A
  GIT_COMMITTER_DATE='2026-01-01T00:00:00Z' GIT_AUTHOR_DATE='2026-01-01T00:00:00Z' \
    git -C "$s" commit -q -m c
}
# run bind.sh over a list of repo names served from $T/src
bindrun() {
  local l="$T/list.$$"; : > "$l"
  for n in "$@"; do printf '%s\n' "$n" >> "$l"; done
  P113_BASE="file://$T/src" ./bind.sh "$l"
}
row() { printf '%s\n' "$1" | awk -v s="$2" -F'\t' '$1==s'; }

mkdir -p "$T/src"

# ===========================================================================
# 1. tokens.awk -- the containment table (P113-F, P113-O)
# ===========================================================================
r=$(tokrun manifest 'openai-whisper==20231117')
is  "whisper-local wins its own text"      "$(fld "$r" 3)" "whisper-local"
is  "openai-whisper is not hosted openai"  "$(fld "$r" 6)" "-"
is  "and the verdict inputs are clean"     "$(fld "$r" 2)" "0"

r=$(tokrun manifest 'sentence-transformers==3.0.1')
is  "sentence-transformers is one family"  "$(fld "$r" 3)" "sentence-transformers"

r=$(tokrun manifest 'transformers==4.44.0')
is  "bare transformers is local"           "$(fld "$r" 3)" "transformers"

r=$(tokrun manifest 'langchain-openai>=0.2.0')
is  "langchain-openai: broker"             "$(fld "$r" 4)" "langchain"
is  "langchain-openai: AND hosted"         "$(fld "$r" 6)" "openai"

r=$(tokrun env 'OPENAI_API_BASE=http://gw.internal/v1')
is  "OPENAI_API_BASE is an override"       "$(fld "$r" 5)" "openai-api-base"
is  "and is not read as hosted openai"     "$(fld "$r" 6)" "-"

r=$(tokrun manifest 'llama-cpp-python==0.3.1')
is  "llama-cpp-python is local"            "$(fld "$r" 3)" "llama.cpp"
is  "llama-cpp is not llama-index"         "$(fld "$r" 4)" "-"

r=$(tokrun manifest 'llama-index-core==0.11')
is  "llama-index is a broker"              "$(fld "$r" 4)" "llama-index"
is  "llama-index is not local"             "$(fld "$r" 3)" "-"

r=$(tokrun manifest 'azure-openai-sdk')
is  "azure-openai is its own family"       "$(fld "$r" 6)" "azure-openai"
hasnt "azure-openai is not plain openai"   "$(fld "$r" 6)" "openai,"

r=$(tokrun manifest 'openai==1.40.0')
is  "plain openai is hosted"               "$(fld "$r" 6)" "openai"

# generic endpoint names -- P113-G
r=$(tokrun manifest 'BASE_URL=https://example.org')
is  "bare base_url alone: no override"     "$(fld "$r" 5)" "-"
r=$(tokrun manifest 'openai
base_url')
is  "base_url next to a model: override"   "$(fld "$r" 5)" "base-url"

# a README is prose, never a declaration -- P113-A
r=$(tokrun readme 'Powered by OpenAI and Ollama.')
is  "readme sets no local"                 "$(fld "$r" 3)" "-"
is  "readme sets no hosted"                "$(fld "$r" 6)" "-"
has "readme lands in prose"                "$(fld "$r" 7)" "ollama"
has "readme prose keeps the hosted name"   "$(fld "$r" 7)" "openai"

# ===========================================================================
# 2. tokens.awk -- byte-exact framing (P113-E, P113-M)
# ===========================================================================
sha1=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
sha2=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
printf '%s\tmanifest\ta\n%s\tmanifest\tb\n' "$sha1" "$sha2" > "$T/map2"

# a payload whose own content is shaped exactly like a batch header
inner="cccccccccccccccccccccccccccccccccccccccc blob 99"
body="ollama
$inner
cohere"
r=$({ printf '%s blob %d\n' "$sha1" "${#body}"; printf '%s\n' "$body"; } \
      | awk -v map="$T/map2" -f tokens.awk)
is  "header-shaped content line: 1 record" "$(fld "$r" 1)" "1"
is  "header-shaped content line: 0 stray"  "$(fld "$r" 2)" "0"
is  "and the line after it still counts"   "$(fld "$r" 6)" "cohere"

# payload with NO trailing newline, followed by another record
r=$({ printf '%s blob 6\nollama\n' "$sha1"; printf '%s blob 7\ncohere\n\n' "$sha2"; } \
      | awk -v map="$T/map2" -f tokens.awk)
is  "no-trailing-newline: both records"    "$(fld "$r" 1)" "2"
is  "no-trailing-newline: no desync"       "$(fld "$r" 2)" "0"
is  "no-trailing-newline: first read"      "$(fld "$r" 3)" "ollama"
is  "no-trailing-newline: second read"     "$(fld "$r" 6)" "cohere"

# an empty payload is a record, and consumes its separator
r=$({ printf '%s blob 0\n\n' "$sha1"; printf '%s blob 6\nollama\n' "$sha2"; } \
      | awk -v map="$T/map2" -f tokens.awk)
is  "empty payload: still two records"     "$(fld "$r" 1)" "2"
is  "empty payload: no stray lines"        "$(fld "$r" 2)" "0"
is  "empty payload: next record read"      "$(fld "$r" 3)" "ollama"

# a missing object is counted, never classified
r=$(printf '%s missing\n' "$sha1" | awk -v map="$T/map2" -f tokens.awk)
is  "missing object: no record"            "$(fld "$r" 1)" "0"
is  "missing object: not stray"            "$(fld "$r" 2)" "0"

# a line outside any record is `anom`, never silently dropped (P1040)
r=$(printf 'loose ollama line\n' | awk -v map="$T/map2" -f tokens.awk)
is  "a loose line is counted"              "$(fld "$r" 2)" "1"
is  "a loose line is NOT classified"       "$(fld "$r" 3)" "-"

# ===========================================================================
# 3. select.awk -- what the tree offers the body stage (P113-A..D)
# ===========================================================================
sel() { awk -v CAP="${2:-60}" -f select.awk; }
tree_line() { printf '100644 blob %040d\t%s\n' "$1" "$2"; }

t=$( { tree_line 1 'requirements.txt'; tree_line 2 'pyproject.toml';
       tree_line 3 '.env.example';     tree_line 4 'docker-compose.yml';
       tree_line 5 'Modelfile';        tree_line 6 'README.md';
       tree_line 7 'docs/README.md';   tree_line 8 'src/app.py';
       tree_line 9 'node_modules/x/package.json'; } | sel )
is  "manifest selected"       "$(printf '%s\n' "$t" | awk -F'\t' '$3=="requirements.txt"{print $2}')" "manifest"
is  "pyproject selected"      "$(printf '%s\n' "$t" | awk -F'\t' '$3=="pyproject.toml"{print $2}')"   "manifest"
is  "env template selected"   "$(printf '%s\n' "$t" | awk -F'\t' '$3==".env.example"{print $2}')"     "env"
is  "compose selected"        "$(printf '%s\n' "$t" | awk -F'\t' '$3=="docker-compose.yml"{print $2}')" "compose"
is  "Modelfile selected"      "$(printf '%s\n' "$t" | awk -F'\t' '$3=="Modelfile"{print $2}')"        "modelfile"
is  "root README selected"    "$(printf '%s\n' "$t" | awk -F'\t' '$3=="README.md"{print $2}')"         "readme"
is  "nested README skipped (P113-B)" "$(printf '%s\n' "$t" | awk -F'\t' '$3=="docs/README.md"{print $2}')" ""
is  "program text skipped"    "$(printf '%s\n' "$t" | awk -F'\t' '$3=="src/app.py"{print $2}')"       ""
is  "node_modules stripped"   "$(printf '%s\n' "$t" | grep -c 'node_modules')"                        "0"
is  "tally counts the tree"   "$(printf '%s\n' "$t" | awk -F'\t' '/^#tally/{print $2}')"              "9"
is  "tally counts the strip"  "$(printf '%s\n' "$t" | awk -F'\t' '/^#tally/{print $3}')"              "1"
is  "tally counts selected"   "$(printf '%s\n' "$t" | awk -F'\t' '/^#tally/{print $4}')"              "6"
is  "nothing capped here"     "$(printf '%s\n' "$t" | awk -F'\t' '/^#tally/{print $5}')"              "0"

for v in vendor .venv venv site-packages .tox dist build third_party bower_components; do
  n=$(tree_line 1 "$v/x/package.json" | sel | grep -c "$v/x")
  is  "stripped without credit: $v" "$n" "0"
done
n=$(tree_line 1 'foo.egg-info/requirements.txt' | sel | grep -c 'egg-info')
is  "stripped without credit: egg-info" "$n" "0"

t=$( { tree_line 1 'a/requirements.txt'; tree_line 2 'b/requirements.txt';
       tree_line 3 'c/requirements.txt'; } | sel '' 2 )
is  "cap limits the read (P113-D)" "$(printf '%s\n' "$t" | grep -vc '^#tally')" "2"
is  "cap is reported, not hidden"  "$(printf '%s\n' "$t" | awk -F'\t' '/^#tally/{print $5}')" "1"

# requirements variants a real shelf uses
for f in requirements.txt requirements-dev.txt requirements_prod.txt; do
  is  "manifest variant $f" "$(tree_line 1 "$f" | sel | awk -F'\t' 'NR==1{print $2}')" "manifest"
done
for f in .env.sample .env.template .env.dist env.example; do
  is  "env variant $f" "$(tree_line 1 "$f" | sel | awk -F'\t' 'NR==1{print $2}')" "env"
done
is  "a .py named env is not an env file" "$(tree_line 1 'env.py' | sel | grep -vc '^#tally')" "0"
is  "compose.yaml is compose"            "$(tree_line 1 'compose.yaml' | sel | awk -F'\t' 'NR==1{print $2}')" "compose"

# ===========================================================================
# 4. bind.sh end to end, over REAL repositories served on file://
# ===========================================================================
mkdir -p "$T/src/r-local"      && printf 'ollama\nchromadb\n'            > "$T/src/r-local/requirements.txt"
mkdir -p "$T/src/r-broker"     && printf 'litellm==1.0\nopenai==1.4\n'   > "$T/src/r-broker/requirements.txt"
mkdir -p "$T/src/r-override"   && printf 'openai==1.4\n'                 > "$T/src/r-override/requirements.txt" \
                               && printf 'OPENAI_API_BASE=http://gw/v1\nOPENAI_API_KEY=\n' > "$T/src/r-override/.env.example"
mkdir -p "$T/src/r-hosted"     && printf 'openai==1.4\nanthropic==0.3\n' > "$T/src/r-hosted/requirements.txt"
mkdir -p "$T/src/r-nomodel"    && printf 'django==5.0\npsycopg2\n'       > "$T/src/r-nomodel/requirements.txt"
mkdir -p "$T/src/r-prose"      && printf 'django==5.0\n'                 > "$T/src/r-prose/requirements.txt" \
                               && printf '# App\n\nUses the OpenAI API for feedback.\n' > "$T/src/r-prose/README.md"
mkdir -p "$T/src/r-compose"    && printf 'services:\n  ollama:\n    image: ollama/ollama\n' > "$T/src/r-compose/docker-compose.yml"
mkdir -p "$T/src/r-modelfile"  && printf 'FROM llama3\n'                 > "$T/src/r-modelfile/Modelfile"
mkdir -p "$T/src/r-notrail"    && printf 'cohere==5.0'                   > "$T/src/r-notrail/requirements.txt"
mkdir -p "$T/src/r-vendored/node_modules/openai" \
                               && printf 'django==5.0\n'                 > "$T/src/r-vendored/requirements.txt" \
                               && printf '{"dependencies":{"openai":"4.0"}}\n' > "$T/src/r-vendored/node_modules/openai/package.json"
for n in r-local r-broker r-override r-hosted r-nomodel r-prose r-compose r-modelfile r-notrail r-vendored; do mkrepo "$n"; done

out=$(bindrun r-local r-broker r-override r-hosted r-nomodel r-prose r-compose r-modelfile r-notrail r-vendored)

v() { row "$out" "$1" | cut -f15; }
is  "ladder: local"             "$(v r-local)"      "local"
is  "ladder: broker over hosted" "$(v r-broker)"    "broker"
is  "ladder: override"          "$(v r-override)"   "override"
is  "ladder: hosted-only"       "$(v r-hosted)"     "hosted-only"
is  "ladder: no-model"          "$(v r-nomodel)"    "no-model"
is  "a README cannot promote (P113-A)" "$(v r-prose)" "no-model"
has "but the README is recorded"       "$(row "$out" r-prose | cut -f13)" "openai"
is  "compose ollama service is local (P113-I)" "$(v r-compose)" "local"
is  "a Modelfile is local"      "$(v r-modelfile)"  "local"
is  "no trailing newline, real repo" "$(v r-notrail)" "hosted-only"
is  "vendored node_modules cannot bind (P113-C)" "$(v r-vendored)" "no-model"
is  "the vendored strip is counted"  "$(row "$out" r-vendored | cut -f4)" "1"

is  "every row read cleanly"    "$(printf '%s\n' "$out" | awk -F'\t' 'NR>1 && $8!=0' | wc -l)" "0"
is  "every row rc=0"            "$(printf '%s\n' "$out" | awk -F'\t' 'NR>1 && $2!=0' | wc -l)" "0"
is  "one header plus ten rows"  "$(printf '%s\n' "$out" | wc -l)" "11"
is  "columns: 15 on the header" "$(printf '%s\n' "$out" | head -1 | awk -F'\t' '{print NF}')" "15"
is  "columns: 15 on every row"  "$(printf '%s\n' "$out" | awk -F'\t' 'NF!=15' | wc -l)" "0"

# the hosted row names BOTH providers, so the TSV is auditable without re-running
is  "hosted families are listed" "$(row "$out" r-hosted | cut -f12)" "anthropic,openai"
is  "override row keeps its provider" "$(row "$out" r-override | cut -f12)" "openai"

# UNREAD -- P113-K
out2=$(bindrun r-local no-such-repo-at-all)
is  "a dead remote is UNREAD"   "$(row "$out2" no-such-repo-at-all | cut -f15)" "UNREAD"
is  "UNREAD carries rc=1"       "$(row "$out2" no-such-repo-at-all | cut -f2)"  "1"
is  "UNREAD metrics are EMPTY, never 0 (P113-K)" "$(row "$out2" no-such-repo-at-all | cut -f3)" ""
is  "a live row beside it is unaffected" "$(row "$out2" r-local | cut -f15)" "local"

# the no-body control -- P113-L
out3=$(P113_NO_BODY=1 bindrun r-local r-hosted r-modelfile)
is  "control: no bodies read"   "$(printf '%s\n' "$out3" | awk -F'\t' 'NR>1 && $7!=0' | wc -l)" "0"
is  "control: local is lost"    "$(row "$out3" r-local | cut -f15)"     "no-model"
is  "control: hosted is lost"   "$(row "$out3" r-hosted | cut -f15)"    "no-model"
is  "control: selection is unchanged" "$(row "$out3" r-local | cut -f5)" "$(row "$out" r-local | cut -f5)"
is  "control: the Modelfile SURVIVES it (P113-P)" "$(row "$out3" r-modelfile | cut -f15)" "local"

# idempotence: the same tree twice gives the same row
out4=$(bindrun r-broker)
is  "a second run agrees"       "$(row "$out4" r-broker)" "$(row "$out" r-broker)"

# ===========================================================================
# 5. P113-Q -- the four containment false positives found on the real shelf,
#    each tested against the payload line that produced it
# ===========================================================================
r=$(tokrun manifest 'into what looks like one coherent run')
is  "\"coherent\" is not cohere (apache/ofbiz-framework)" "$(fld "$r" 6)" "-"
r=$(tokrun manifest '# This file was autogenerated by uv via the following command:')
is  "\"autogenerated\" is not autogen (ls1intum/Artemis)" "$(fld "$r" 4)" "-"
r=$(tokrun manifest 'github.com/aws/aws-sdk-go-v2/service/bedrockagentcore v1.36.4 // indirect')
is  "\"bedrockagentcore\" is not bedrock (temporalio/temporal)" "$(fld "$r" 6)" "-"
r=$(tokrun manifest 'we replicated the experiment')
is  "\"replicated\" is not replicate"                    "$(fld "$r" 6)" "-"
r=$(tokrun manifest 'diagnostics are agnostic to the magnolia theme')
is  "agno does not harvest diagnostic/agnostic/magnolia"   "$(fld "$r" 4)" "-"
# the token still matches when it IS the token
r=$(tokrun manifest 'cohere==5.0')
is  "cohere itself still matches"                          "$(fld "$r" 6)" "cohere"
r=$(tokrun manifest 'bedrock')
is  "bedrock itself still matches"                         "$(fld "$r" 6)" "bedrock"
r=$(tokrun manifest 'pyautogen==0.2')
is  "pyautogen IS autogen's distribution (P113-S)"         "$(fld "$r" 4)" "autogen"
r=$(tokrun manifest 'node -r esm types/tests/autogen.js && tsc')
is  "autogen.js is a FILENAME, not AutoGen (GibbonEdu/core)" "$(fld "$r" 4)" "-"
r=$(tokrun manifest 'autogen-agentchat>=0.4')
is  "autogen-agentchat is autogen"                         "$(fld "$r" 4)" "autogen"
# boundary consumption must not eat the next token
r=$(tokrun manifest 'litellm,openai')
is  "comma-separated: broker survives"                     "$(fld "$r" 4)" "litellm"
is  "comma-separated: hosted survives too"                 "$(fld "$r" 6)" "openai"
r=$(tokrun manifest 'ollama vllm transformers')
is  "space-separated locals all survive"                   "$(fld "$r" 3)" "ollama,transformers,vllm"
r=$(tokrun manifest 'openai/anthropic/cohere')
is  "slash-separated hosted all survive"                   "$(fld "$r" 6)" "anthropic,cohere,openai"
r=$(tokrun manifest 'llama.cpp')
is  "a dot in a token is literal, not any-char"            "$(fld "$r" 3)" "llama.cpp"
r=$(tokrun manifest 'llamaxcpp')
is  "and llamaxcpp is therefore NOT llama.cpp"             "$(fld "$r" 3)" "-"

# ===========================================================================
# 6. P113-R -- a self-name collision is flagged and NEVER suppressed
# ===========================================================================
sf() { local kind="$1" body="$2" slug="$3" sha="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  printf '%s\t%s\tf\n' "$sha" "$kind" > "$T/map"
  { printf '%s blob %d\n' "$sha" "${#body}"; printf '%s' "$body"; printf '\n'; } \
    | awk -v map="$T/map" -v slug="$slug" -f tokens.awk; }
r=$(sf manifest 'name = "aiverify-moonshot"' 'aiverify-foundation/moonshot')
is  "self-name is flagged"                "$(fld "$r" 8)" "moonshot"
r=$(sf manifest 'openai==1.4' 'nextcloud/integration_openai')
is  "self-name does NOT suppress hosted"  "$(fld "$r" 6)" "openai"
is  "and it is flagged at the same time"  "$(fld "$r" 8)" "openai"
r=$(sf manifest 'openai==1.4' 'some/other')
is  "no collision, no flag"               "$(fld "$r" 8)" "-"
# named after the real row that forced P113-R to flag rather than suppress
mkdir -p "$T/src/integration_openai" && printf 'openai==1.4\n' > "$T/src/integration_openai/requirements.txt"
mkrepo integration_openai
out5=$(bindrun integration_openai)
is  "end to end: the flag reaches the TSV" "$(row "$out5" integration_openai | cut -f14)" "openai"
is  "end to end: the verdict still stands" "$(row "$out5" integration_openai | cut -f15)" "hosted-only"

printf '\n%d passed / %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
