#!/usr/bin/env bash
# `P840` — package→repository mapping.  Suite for `lib/package_repo.sh`, closing `Gap 329`.
#
# Pass 75 of 2026-10-09.  SINGLE FILE ON PURPOSE: it writes its own fixtures to a temp dir,
# so it carries no sibling-import hazard and runs identically however it is invoked — the
# cheapest route out of `Gap 300` (41 suites unreadable because `python3 -I` implies `-P`).
#
# Negative controls, per `P126`-2: a case where a WRONG instrument would also pass is not a
# test.  So every verdict class is asserted INCLUDING the ones that must NOT resolve, and
# `NO-REPO` is asserted to be distinguishable from `NO-METADATA`.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")"
. ../lib/package_repo.sh

pass=0; fail=0
ck() { # ck <label> <expected> <actual>
  if [ "$2" = "$3" ]; then pass=$((pass+1)); printf '  OK   %s\n' "$1"
  else fail=$((fail+1)); printf '  FAIL %s\n         expected: %s\n         actual:   %s\n' "$1" "$2" "$3"; fi
}
F="$(mktemp -d)"; trap 'rm -rf "$F"' EXIT

echo "-- normalise_repo_url: the formats the three registries actually emit --"
ck "plain https"            "HKUDS/DeepTutor"  "$(normalise_repo_url 'https://github.com/HKUDS/DeepTutor')"
ck "git+https with .git"    "Cvmcosta/ltijs"   "$(normalise_repo_url 'git+https://github.com/Cvmcosta/ltijs.git')"
ck "git:// protocol"        "Cvmcosta/ltijs"   "$(normalise_repo_url 'git://github.com/Cvmcosta/ltijs.git')"
ck "scp-style ssh"          "Cvmcosta/ltijs"   "$(normalise_repo_url 'git@github.com:Cvmcosta/ltijs.git')"
ck "ssh:// url"             "Cvmcosta/ltijs"   "$(normalise_repo_url 'ssh://git@github.com/Cvmcosta/ltijs.git')"
ck "npm github: shorthand"  "owner/thing"      "$(normalise_repo_url 'github:owner/thing')"
ck "npm bare shorthand"     "owner/thing"      "$(normalise_repo_url 'owner/thing')"
ck "www. prefix"            "moodle/moodle"    "$(normalise_repo_url 'https://www.github.com/moodle/moodle')"
ck "deep path is trimmed"   "moodle/moodle"    "$(normalise_repo_url 'https://github.com/moodle/moodle/tree/main/lib')"
ck "fragment is trimmed"    "moodle/moodle"    "$(normalise_repo_url 'https://github.com/moodle/moodle#readme')"
ck "query is trimmed"       "moodle/moodle"    "$(normalise_repo_url 'https://github.com/moodle/moodle?tab=readme')"
ck "trailing slash"         "moodle/moodle"    "$(normalise_repo_url 'https://github.com/moodle/moodle/')"

echo "-- the verdicts that must NOT become a GitHub path (negative controls) --"
ck "empty is NO-REPO"       "NO-REPO"          "$(normalise_repo_url '')"
ck "gitlab is NON-GITHUB"   "NON-GITHUB"       "$(normalise_repo_url 'https://gitlab.com/group/proj')"
ck "bitbucket NON-GITHUB"   "NON-GITHUB"       "$(normalise_repo_url 'https://bitbucket.org/team/proj')"
ck "codeberg NON-GITHUB"    "NON-GITHUB"       "$(normalise_repo_url 'https://codeberg.org/u/p')"
ck "a docs host, not a repo" "NON-GITHUB"      "$(normalise_repo_url 'https://docs.example.org/guide')"
ck "a bare word is NO-REPO" "NO-REPO"          "$(normalise_repo_url 'educhain')"

echo "-- regressions found by LIVE execution, not by the offline fixtures above --"
# 🔴 All three of these passed the 32/32 offline suite and were still wrong or absent until
# the fetch limb ran against the real registries.  `Gap 328` warned its own closure shipped an
# UNEXECUTED fetch branch; this is that warning landing.
ck "ssh alias host → UNRESOLVABLE-HOST" "UNRESOLVABLE-HOST" \
   "$(normalise_repo_url 'git@ibl_connection:iblai/iblai-web-mentor.git')"
ck "a real github scp still resolves"   "Cvmcosta/ltijs" \
   "$(normalise_repo_url 'git@github.com:Cvmcosta/ltijs.git')"
ck "alias verdict is not NO-REPO" "differ" \
   "$([ "$(normalise_repo_url 'git@ibl_connection:iblai/x.git')" != "$(normalise_repo_url '')" ] && echo differ || echo same)"
cat > "$F/npm_alias.json" <<'J'
{"name":"@iblai/iblai-web-mentor","license":"MIT",
 "repository":{"type":"git","url":"git@ibl_connection:iblai/iblai-web-mentor.git"}}
J
ck "MIT over an alias address → UNRESOLVABLE-HOST" "UNRESOLVABLE-HOST" \
   "$(repo_from_npm_json "$F/npm_alias.json")"
# PyPI `fitz` as measured live: version 0.0.0, no licence, no URLs — and `fitz` is PyMuPDF's
# IMPORT name, so a manifest that lists it audits an unrelated stub.
cat > "$F/pypi_stub.json" <<'J'
{"info":{"name":"fitz","version":"0.0.0","summary":"","license":null,
 "home_page":null,"project_urls":null}}
J
ck "an all-null stub → NO-REPO" "NO-REPO" "$(repo_from_pypi_json "$F/pypi_stub.json")"

echo "-- PyPI: project_urls keys are free text, and Homepage is often NOT the repo --"
cat > "$F/pypi_source.json" <<'J'
{"info":{"name":"x","home_page":"https://example.org/docs",
 "project_urls":{"Documentation":"https://rtd.example.org","Source":"https://github.com/acme/x"}}}
J
ck "Source beats home_page" "acme/x" "$(repo_from_pypi_json "$F/pypi_source.json")"

cat > "$F/pypi_lowercase.json" <<'J'
{"info":{"name":"x","project_urls":{"repository":"https://github.com/acme/y.git"}}}
J
ck "key case is ignored"    "acme/y" "$(repo_from_pypi_json "$F/pypi_lowercase.json")"

cat > "$F/pypi_homepage_only.json" <<'J'
{"info":{"name":"x","home_page":"https://github.com/acme/z","project_urls":null}}
J
ck "home_page used as last resort" "acme/z" "$(repo_from_pypi_json "$F/pypi_homepage_only.json")"

cat > "$F/pypi_sourceless.json" <<'J'
{"info":{"name":"x","home_page":"","project_urls":{"Documentation":"https://rtd.example.org"}}}
J
ck "docs-only → NO-REPO (Gap 327)" "NO-REPO" "$(repo_from_pypi_json "$F/pypi_sourceless.json")"
: > "$F/empty.json"
ck "absent metadata → NO-METADATA" "NO-METADATA" "$(repo_from_pypi_json "$F/empty.json")"
ck "NO-REPO is not NO-METADATA" "differ" \
   "$([ "$(repo_from_pypi_json "$F/pypi_sourceless.json")" != "$(repo_from_pypi_json "$F/empty.json")" ] && echo differ || echo same)"

echo "-- npm: repository is a STRING or an OBJECT, and both occur --"
cat > "$F/npm_obj.json" <<'J'
{"name":"ltijs","repository":{"type":"git","url":"git+https://github.com/Cvmcosta/ltijs.git"}}
J
ck "object form"  "Cvmcosta/ltijs" "$(repo_from_npm_json "$F/npm_obj.json")"
cat > "$F/npm_str.json" <<'J'
{"name":"t","repository":"github:acme/t"}
J
ck "string shorthand" "acme/t" "$(repo_from_npm_json "$F/npm_str.json")"
cat > "$F/npm_ver.json" <<'J'
{"name":"t","dist-tags":{"latest":"2.0.0"},
 "versions":{"2.0.0":{"repository":{"url":"https://github.com/acme/v2"}}}}
J
ck "falls back to dist-tags latest" "acme/v2" "$(repo_from_npm_json "$F/npm_ver.json")"
cat > "$F/npm_none.json" <<'J'
{"name":"@iblai/iblai-js","version":"1.0.0"}
J
ck "sourceless SDK → NO-REPO" "NO-REPO" "$(repo_from_npm_json "$F/npm_none.json")"

echo "-- Packagist: p2 nests a version LIST under packages.<vendor/name> --"
cat > "$F/pkg.json" <<'J'
{"packages":{"rusticisoftware/tincan":[
  {"version":"3.0.0","source":{"type":"git","url":"https://github.com/RusticiSoftware/TinCanPHP.git"}},
  {"version":"2.0.0","source":{"type":"git","url":"https://github.com/old/old.git"}}]}}
J
ck "newest entry wins" "RusticiSoftware/TinCanPHP" "$(repo_from_packagist_json "$F/pkg.json")"

echo "-- core_deps_of: RUNTIME closure only, which is what P15 stage 3 asks for --"
cat > "$F/requirements.txt" <<'J'
# a comment
fitz>=1.23.0
pymupdf==1.24.1  ; python_version >= "3.9"
uvicorn[standard]~=0.30

-r dev-requirements.txt
--extra-index-url https://example.org/simple
J
got=$(core_deps_of_requirements "$F/requirements.txt" | tr '\n' ' ' | sed 's/ $//')
ck "extras/markers/pins stripped; -r and flags dropped" "fitz pymupdf uvicorn" "$got"

cat > "$F/package.json" <<'J'
{"dependencies":{"ltijs":"^5.9.0","express":"^4.19.2"},
 "devDependencies":{"jest":"^29.0.0"},"optionalDependencies":{"fsevents":"*"}}
J
got=$(core_deps_of_package_json "$F/package.json" | tr '\n' ' ' | sed 's/ $//')
ck "dev and optional excluded" "express ltijs" "$got"

cat > "$F/pyproject.toml" <<'J'
[project]
name = "x"
dependencies = [
  "pymupdf>=1.24",
  "httpx[http2]==0.27.0",
]
[project.optional-dependencies]
dev = ["pytest"]
J
got=$(core_deps_of_pyproject "$F/pyproject.toml" | tr '\n' ' ' | sed 's/ $//')
ck "optional-dependencies excluded" "httpx pymupdf" "$got"

echo
if [ "$fail" -eq 0 ]; then echo "test_package_repo.sh: $pass/$pass checks passed"; exit 0
else echo "test_package_repo.sh: $fail FAILED, $pass passed"; exit 1; fi
