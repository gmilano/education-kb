# SHARED PACKAGE→REPOSITORY MAPPING — the NETWORK-FREE half.  Source this, or call
# `lib/pkgrepo`.  Do not rewrite it.
#
# Pass 75 of 2026-10-09, closing `Gap 329`.
#
# ─── Why this file exists ─────────────────────────────────────────────────────────────────
#
# `P15` (the licence-closure gate) needs stage 3: probe the payload of each CORE DEPENDENCY.
# 🔴 A PyPI/npm/Packagist name is not a GitHub path, and nothing on this shelf mapped one to
# the other.  `core_deps_of` and `repo_of_pypi` were NAMED in `P15` and never written, so the
# most expensive stage of the gate still needed a human — the arrangement `Gap 328` existed
# to end.  `73-C`'s `PyMuPDF` finding (a permissive root grant over an AGPL-or-commercial
# core dependency) was made BY HAND.
#
# ─── The seam, per `P838` ─────────────────────────────────────────────────────────────────
#
# 🟢 `P838` says split a shared instrument on the capability the environment DENIES, not on
# its calling convention.  Measured this pass, not inferred:
#
#   | host                                        | result            |
#   |---------------------------------------------|-------------------|
#   | `pypi.org/pypi/<name>/json`                 | 🟢 **200**        |
#   | `registry.npmjs.org/<name>`                 | 🟢 **200**        |
#   | `repo.packagist.org/p2/<vendor>/<pkg>.json` | 🟢 **200**        |
#   | `eur-lex.europa.eu`                         | 🔴 403 to CONNECT |
#
# 🔵 All three registries are in the proxy's `noProxy` list, so the network limb WORKS here —
# unlike `Gap 328`'s payload probe.  The seam is kept anyway: every PARSE is in this file and
# testable offline, so the suite stays green in a session whose egress differs.  An instrument
# that only works where it was written is the failure `P838` names.
#
# ─── The verdict vocabulary, and why absence must be loud ─────────────────────────────────
#
# 🟢 `lib/measure` set the precedent: a missing payload is `NO-PAYLOAD`, never `0 B`.  Same
# discipline here, and it buys something this shelf has wanted:
#
#   `owner/repo`   a resolved GitHub path — the only verdict `P15` stage 3 can probe
#   `NO-REPO`      metadata exists and declares NO source → 🔴 this is `Gap 327`'s category
#   `NON-GITHUB`   source declared on GitLab/Bitbucket/other → real, but not probeable here
#   `NO-METADATA`  the registry has no such package
#   `UNRESOLVABLE-HOST`  source declared at an SSH-config ALIAS, resolvable only by the
#                  publisher → a grant whose subject has no public address
#
# 🔵 `NO-REPO` is the valuable one.  `Gap 327` ("permissive but sourceless": a grant with no
# subject) was hit three times in one chain and caught BY HAND every time.  A mapping that
# refuses to invent a path turns that category into a MEASUREMENT instead of a noticing.
# 🔴 Never collapse `NO-REPO` into `NO-METADATA`: the first is a package that exists and
# publishes no source, the second is a name that does not exist.  Those license opposite next
# actions — ask upstream for a repo, vs. correct the name — and this shelf has written both
# in the same voice before (`P827`, `Gap 301`).

_PKGREPO_LIB_DIR="${_PKGREPO_LIB_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"

# ── normalisation ─────────────────────────────────────────────────────────────────────────
# Turns any declared source URL into `owner/repo`, or a loud verdict.  This is where the
# registry formats actually differ, so it is the one function the suite hammers.
normalise_repo_url() {
  local u="$1"
  [ -z "$u" ] && { printf 'NO-REPO\n'; return 0; }

  # npm shorthands: `github:owner/repo`, `owner/repo`, `gh:owner/repo`
  case "$u" in
    github:*|gh:*) u="https://github.com/${u#*:}" ;;
  esac

  # strip VCS prefixes and scp-style ssh, both of which appear in npm `repository.url`
  u="${u#git+}"
  u="${u#git://}"
  u="${u#ssh://}"
  u="${u#git@}"
  u="${u#https://}"
  u="${u#http://}"
  u="${u#www.}"
  u="${u/github.com:/github.com/}"   # scp-style `github.com:owner/repo`

  # 🔴 An scp-style address whose host is an SSH CONFIG ALIAS resolves for nobody outside the
  # publisher.  Measured live this pass: `@iblai/iblai-web-mentor` declares
  # `git@ibl_connection:iblai/iblai-web-mentor.git` under an MIT licence.  `ibl_connection` is
  # not a host, so this is `Gap 327` in its sharpest form — a grant whose SUBJECT has an
  # address only the vendor can resolve.
  # 🔴 Before this check the parser emitted `ibl_connection:iblai/iblai-web-mentor` and exited
  # 0, so a caller would have probed a GitHub path THAT WAS NEVER DECLARED.  Per `P827` a
  # guessed path is not a measurement: the alias is reported, never resolved.
  case "${u%%/*}" in
    *:*) printf 'UNRESOLVABLE-HOST\n'; return 0 ;;
  esac

  case "$u" in
    github.com/*) : ;;
    gitlab.com/*|bitbucket.org/*|codeberg.org/*|git.sr.ht/*|*.gitlab.io/*)
      printf 'NON-GITHUB\n'; return 0 ;;
    */*)
      # a bare `owner/repo` with no host is npm's shorthand for GitHub
      case "$u" in
        *.*/*) printf 'NON-GITHUB\n'; return 0 ;;
        *) u="github.com/$u" ;;
      esac ;;
    *) printf 'NO-REPO\n'; return 0 ;;
  esac

  u="${u#github.com/}"
  u="${u%.git}"
  u="${u%/}"
  # drop anything past `owner/repo`: `/tree/main`, `/issues`, `#readme`, `?tab=`
  u="${u%%#*}"; u="${u%%\?*}"
  local owner repo
  owner="${u%%/*}"; u="${u#*/}"; repo="${u%%/*}"
  repo="${repo%.git}"
  [ -z "$owner" ] || [ -z "$repo" ] && { printf 'NO-REPO\n'; return 0; }
  printf '%s/%s\n' "$owner" "$repo"
}

# ── registry metadata → repo (offline: takes a FILE of already-fetched JSON) ──────────────
# PyPI puts the useful field in `info.project_urls`, whose KEYS ARE FREE TEXT.  Order matters:
# `Source`/`Repository`/`Code` are repos; `Homepage` is often a docs site, so it is last.
repo_from_pypi_json() {
  local f="$1" u=""
  [ -s "$f" ] || { printf 'NO-METADATA\n'; return 0; }
  u=$(python3 -I -c '
import json,sys
try: d=json.load(open(sys.argv[1]))
except Exception: print(""); sys.exit()
info=d.get("info") or {}
urls=info.get("project_urls") or {}
pref=("source","repository","source code","code","github","homepage")
low={str(k).strip().lower():v for k,v in urls.items() if v}
for k in pref:
    if k in low and "github.com" in str(low[k]).lower(): print(low[k]); sys.exit()
for k in pref:
    if k in low: print(low[k]); sys.exit()
for v in low.values():
    if "github.com" in str(v).lower(): print(v); sys.exit()
print(info.get("home_page") or "")
' "$f" 2>/dev/null)
  normalise_repo_url "$u"
}

# npm `repository` is EITHER a string shorthand OR an object with `url`.  Both occur.
repo_from_npm_json() {
  local f="$1" u=""
  [ -s "$f" ] || { printf 'NO-METADATA\n'; return 0; }
  u=$(python3 -I -c '
import json,sys
try: d=json.load(open(sys.argv[1]))
except Exception: print(""); sys.exit()
r=d.get("repository")
if not r:
    vs=d.get("versions") or {}
    dt=(d.get("dist-tags") or {}).get("latest")
    r=((vs.get(dt) or {}).get("repository")) if dt else None
if isinstance(r,str): print(r)
elif isinstance(r,dict): print(r.get("url") or "")
else: print(d.get("homepage") or "")
' "$f" 2>/dev/null)
  normalise_repo_url "$u"
}

# Packagist p2 wraps versions under `packages.<vendor/name>` as a LIST, newest first.
repo_from_packagist_json() {
  local f="$1" u=""
  [ -s "$f" ] || { printf 'NO-METADATA\n'; return 0; }
  u=$(python3 -I -c '
import json,sys
try: d=json.load(open(sys.argv[1]))
except Exception: print(""); sys.exit()
pk=d.get("packages") or {}
for _,vers in pk.items():
    if isinstance(vers,list) and vers:
        for v in vers:
            s=(v.get("source") or {}).get("url")
            if s: print(s); sys.exit()
        print(vers[0].get("homepage") or ""); sys.exit()
print("")
' "$f" 2>/dev/null)
  normalise_repo_url "$u"
}

# ── manifests → core dependency NAMES (`core_deps_of`, named by `P15` and never written) ──
# "Core" means the RUNTIME closure only.  Dev/test/optional extras are excluded on purpose:
# `P15` asks what a DEPLOYED artefact carries, and a test-only GPL tool is not in it.
core_deps_of_requirements() {
  sed -e 's/#.*//' -e 's/[[:space:]]//g' "$1" 2>/dev/null \
    | grep -v '^$' | grep -v '^-' \
    | sed -e 's/\[.*\]//' -e 's/[<>=!~;].*//' \
    | grep -v '^$' | sort -u
}

core_deps_of_package_json() {
  python3 -I -c '
import json,sys
try: d=json.load(open(sys.argv[1]))
except Exception: sys.exit()
for k in sorted((d.get("dependencies") or {})): print(k)
' "$1" 2>/dev/null
}

core_deps_of_pyproject() {
  # 🔴 A non-greedy `\[(.*?)\]` is WRONG here: it stops at the first `]`, which for a dep
  # like `httpx[http2]==0.27.0` is INSIDE the entry, silently dropping every later dep.
  # 🔵 Same shape as `P831`'s substring trap — a delimiter that also occurs in the data — and
  # it was caught by a fixture, not by eye.  🟢 Bracket DEPTH scan instead.
  python3 -I -c '
import re,sys
try: t=open(sys.argv[1]).read()
except Exception: sys.exit()
m=re.search(r"^[ \t]*dependencies[ \t]*=[ \t]*\[", t, re.M)
out=[]
if m:
    i=m.end()-1; depth=0; j=i
    while j < len(t):
        if t[j]=="[": depth+=1
        elif t[j]=="]":
            depth-=1
            if depth==0: break
        j+=1
    body=t[i+1:j]
    for s in re.findall(r"[\x27\"]([^\x27\"]+)[\x27\"]", body):
        n=re.split(r"[<>=!~;\[ ]", s.strip())[0]
        if n: out.append(n)
for n in sorted(set(out)): print(n)
' "$1" 2>/dev/null
}
