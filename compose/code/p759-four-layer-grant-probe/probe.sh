#!/bin/bash
# p759 — the FOUR-LAYER grant probe.  Pass 59, 2026-10-08.
#
# WHY THIS EXISTS, AND WHAT IT DELIBERATELY DOES NOT DO
# -----------------------------------------------------
# Pass 59's finding (`P755`/Trend 1) is that re-implementing a vetted CLASSIFIER is the
# most expensive mistake available in this KB: the pass hand-rolled a `§13 present` test
# and it read `moodle/moodle` as AGPL-3.0, because GPL-3.0 titles its §13 "Use with the
# GNU Affero General Public License" and names Affero three times (`P753`).
#
# So this script LOCATES grants.  It does NOT classify them.  Classification goes to
# `compose/code/p419-copyleft-identity/`, which windows to the title line and quarantines
# kinship in a separate field, and has done so correctly since pass 123.
#
# The four layers exist because a grant is not always in a licence file (`P760`):
#   1  licence file, 15 filenames                      -> most repos
#   2  BELOW a reference inside that file               -> openeducat/openeducat_erp (LGPL-3.0, P742)
#   3  manifest / registry (the only DATED oracle)      -> PyLTI1p3's 2022-11-20 (P741)
#   4  SOURCE FILE HEADERS, with no licence file at all -> onbirdev/moodle-webservice_mcp (P757)
# Only when all four are empty is the verdict ALL RIGHTS RESERVED -- which is a verdict,
# not an absence (`P476`, `P628`).
#
# PROVENANCE: `refs/heads` SHA from `git ls-remote` (`P732`), because `api.github.com` is
# 403 here and `raw.githubusercontent.com` silently resolves `master` to the default
# branch, so a branch name is not provenance (`P714`).
#
# EXISTENCE: NOT `curl -sI https://github.com/<slug>`.  That returns 403 for a real repo
# and 403 for an invented one -- a blind channel (`P770`).  Existence is `ls-remote`
# returning a SHA, cross-checked by `raw` answering 200/404.
#
# BYTES: stored bytes (`P704`).  Bytes identify a TEXT, never a FAMILY: GPL-3.0 is
# 35 147 B and AGPL-3.0 is 35 136 B, eleven bytes apart (`P754`).

set -u
NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENSE-MIT LICENSE-APACHE \
COPYING COPYING.txt COPYING.LESSER LICENSE.rst license license.md LICENSE.code LICENSE-CODE"
MANIFESTS="setup.py pyproject.toml package.json composer.json Cargo.toml"
HEADERS="version.php lib.php __init__.py index.js main.go src/lib.rs"
RAW=https://raw.githubusercontent.com

die() { echo "p759: $*" >&2; exit 2; }
[ $# -ge 1 ] || die "no slug given.  usage: probe.sh owner/repo [owner/repo ...]  (or --self-test)"

probe_one() {
  local slug="$1" sha ref code bytes n hits=0
  case "$slug" in */*) ;; *) die "not a slug: '$slug'" ;; esac
  echo "================ $slug ================"

  sha=$(timeout 30 git ls-remote "https://github.com/$slug" HEAD 2>/dev/null | awk '{print $1}')
  if [ -z "$sha" ]; then
    echo "  EXISTENCE: ls-remote returned no SHA -> treat as NOT REACHABLE (not as 'ungranted')"
    return 0
  fi
  echo "  provenance: HEAD sha $sha   (P732)"
  ref="$sha"

  echo "  -- layer 1: licence file, $(echo $NAMES | wc -w) filenames"
  for n in $NAMES; do
    code=$(curl -s -o /tmp/p759.body -m 20 -w "%{http_code}" "$RAW/$slug/$ref/$n")
    if [ "$code" = "200" ]; then
      hits=$((hits+1)); bytes=$(wc -c < /tmp/p759.body)
      echo "     FOUND $n  ${bytes}B (stored, P704)"
      echo "       title-line: $(grep -m1 -iE 'GENERAL PUBLIC LICENSE|Apache License|MIT License|BSD|Mozilla|Eclipse' /tmp/p759.body | sed 's/^ *//')"
      echo "       version   : $(grep -m1 -oE 'Version [0-9](\.[0-9])?' /tmp/p759.body)"
      # layer 2: a file that OPENS with a pointer may still grant below it (P742)
      if head -c 200 /tmp/p759.body | grep -qiE 'see the (COPYRIGHT|LICENSE|NOTICE)|please see'; then
        echo "       !! layer 2: opens with a REFERENCE -- read BELOW it, the grant may be in this same file (P742)"
      fi
      echo "       -> CLASSIFY with p419-copyleft-identity.  Do NOT grep for 'affero' (P753)."
    fi
  done
  [ "$hits" = 0 ] && echo "     none"

  echo "  -- layer 3: manifest / registry (the only DATED oracle, P741)"
  for m in $MANIFESTS; do
    code=$(curl -s -o /tmp/p759.m -m 15 -w "%{http_code}" "$RAW/$slug/$ref/$m")
    [ "$code" = "200" ] && { hits=$((hits+1)); echo "     FOUND $m  grant-strings: $(grep -ioE '"?licen[cs]e"?[^,}]{0,60}' /tmp/p759.m | head -2 | tr '\n' '|')"; }
  done

  echo "  -- layer 4: source-file headers (a grant with NO licence file, P757)"
  for h in $HEADERS; do
    code=$(curl -s -o /tmp/p759.h -m 15 -w "%{http_code}" "$RAW/$slug/$ref/$h")
    if [ "$code" = "200" ] && grep -qiE 'General Public License|Apache License|MIT License|Permission is hereby granted' /tmp/p759.h; then
      hits=$((hits+1))
      echo "     FOUND in $h: $(grep -m1 -iE 'General Public License|Apache License|MIT License|Permission is hereby granted' /tmp/p759.h | sed 's|^[/# *]*||')"
    fi
  done

  [ "$hits" = 0 ] && echo "  VERDICT: no grant at ANY of the four layers -> ALL RIGHTS RESERVED (a verdict, P476)"
  return 0
}

# ---- known-answer controls.  Offline-safe only in the sense that it states what it needs.
self_test() {
  local fail=0
  echo "p759 --self-test: known-answer controls (needs ls-remote + raw, both measured 200/OK on 2026-10-08)"

  # control 1: the blind channel.  A real repo and an invented one must be INDISTINGUISHABLE
  # on github.com HTML -- this is the control that keeps anyone re-adding `curl -sI` (P770).
  local a b
  a=$(curl -s -o /dev/null -m 20 -w '%{http_code}' -I https://github.com/moodle/moodle)
  b=$(curl -s -o /dev/null -m 20 -w '%{http_code}' -I https://github.com/zzz-no-such-org-zzz/nope)
  if [ "$a" = "$b" ]; then echo "  OK   github.com HTML is blind ($a for real AND invented) -- do not use it (P770)"
  else echo "  CHANGED  github.com HTML now discriminates ($a vs $b) -- re-measure P770"; fi

  # control 2: ls-remote DOES discriminate
  if timeout 25 git ls-remote https://github.com/moodle/moodle HEAD >/dev/null 2>&1 \
     && ! timeout 25 git ls-remote https://github.com/zzz-no-such-org-zzz/nope HEAD >/dev/null 2>&1; then
    echo "  OK   ls-remote discriminates (real=SHA, invented=fail)"
  else echo "  FAIL ls-remote no longer discriminates"; fail=1; fi

  # control 3: the §13 trap itself.  GPL-3.0's payload must NAME Affero while BEING GPL.
  curl -s -m 20 "$RAW/moodle/moodle/f20534726a59a4b64d168bc4a70fc9518251613e/COPYING.txt" -o /tmp/p759.gpl
  local naff title
  naff=$(grep -ci affero /tmp/p759.gpl); title=$(grep -m1 -i 'GENERAL PUBLIC LICENSE' /tmp/p759.gpl)
  if [ "$naff" -ge 1 ] && ! echo "$title" | grep -qi affero; then
    echo "  OK   P753 holds: GPL-3.0 payload names Affero ${naff}x, and its TITLE LINE does not"
  else echo "  FAIL P753 control did not reproduce (naff=$naff)"; fail=1; fi

  # control 4: layer 4 must find a grant where layer 1 finds nothing (P757)
  local lic hdr
  lic=$(curl -s -o /dev/null -m 15 -w '%{http_code}' "$RAW/onbirdev/moodle-webservice_mcp/198246e5d7121b7658e72e44549006753136ac70/LICENSE")
  hdr=$(curl -s -m 15 "$RAW/onbirdev/moodle-webservice_mcp/198246e5d7121b7658e72e44549006753136ac70/version.php" | grep -ci 'General Public License')
  if [ "$lic" = "404" ] && [ "$hdr" -ge 1 ]; then
    echo "  OK   P757 holds: LICENSE=404 and the source header grants GPL -- layer 1 alone would say 'ungranted'"
  else echo "  FAIL P757 control did not reproduce (LICENSE=$lic header-hits=$hdr)"; fail=1; fi

  [ "$fail" = 0 ] && echo "p759 --self-test: PASS" || echo "p759 --self-test: FAIL"
  return $fail
}

[ "${1:-}" = "--self-test" ] && { self_test; exit $?; }
for s in "$@"; do probe_one "$s"; done
