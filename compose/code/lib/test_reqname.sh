#!/usr/bin/env bash
# test_reqname.sh -- the shared requirement-name predicate (lib/reqname.awk).
#
# Every case p114 recorded under `Gap 404` is here as a test, so the widening
# that closes it cannot be silently narrowed again by a later pass. The four
# real filenames from this shelf are named in the assertions that carry them.
set -uo pipefail
cd "$(dirname "$0")"
PASS=0; FAIL=0

# `is_reqname` is a function in a library file, so it is exercised through a
# one-line driver passed as a SECOND -f -- which is exactly how a consuming
# pass loads it. The driver lives in a file because awk cannot take its
# program on stdin while also reading data there.
DRV="${TMPDIR:-/tmp}/reqname-drv.$$.awk"
printf '%s\n' '{ print (is_reqname($0) ? "yes" : "no") }' > "$DRV"
trap 'rm -f "$DRV"' EXIT
q() { printf '%s\n' "$1" | awk -f reqname.awk -f "$DRV"; }

yes() {
  r=$(q "$1")
  if [ "$r" = yes ]; then PASS=$((PASS+1));
  else FAIL=$((FAIL+1)); printf '  FAIL %-34s expected yes, got %s   (%s)\n' "$1" "$r" "$2"; fi
}
no() {
  r=$(q "$1")
  if [ "$r" = no ]; then PASS=$((PASS+1));
  else FAIL=$((FAIL+1)); printf '  FAIL %-34s expected NO,  got %s   (%s)\n' "$1" "$r" "$2"; fi
}

# ---- what the narrow rule already matched, and must keep matching ----------
yes requirements.txt              "the plain spelling"
yes requirements-dev.txt          "hyphen suffix"
yes requirements_dev.txt          "underscore suffix"
yes requirements.dev.txt          "dot suffix"
yes requirements-test-extra.txt   "multi-segment suffix"

# ---- Gap 404: the prefixed spelling, all four seen on this shelf -----------
yes dev_requirements.txt          "Gap 404, Submitty"
yes system_requirements.txt       "Gap 404, Submitty"
yes latest_requirements.txt       "Gap 404, sdv-dev/sdv -- the one that moves a verdict"
yes test-requirements.txt         "Gap 404, hyphen prefix"
yes doc_requirements.txt          "Gap 404, generic"

# ---- what must STAY refused ------------------------------------------------
no  requirements.rst              "P112-A: prose, and really on this shelf"
no  requirements.md               "P112-A: prose"
no  requirements.in               "pip-compile INPUT, not a pinned file"
no  requirements.txt.bak          "not a .txt tail"
no  myrequirements.txt            "no separator -- the prefix group must not swallow a word"
no  arequirements.txt             "no separator"
no  requirementstxt               "no extension"
no  ""                            "the empty basename"
no  .txt                          "extension only"
no  requirements                  "no extension"
no  REQUIREMENTS.TXT              "case: the rule is lower-case by convention"

# A path is never passed to this predicate -- callers pass a BASENAME. The
# assertion records that contract rather than inventing path handling here.
no  "requirements/base.txt"       "a directory, not a basename -- callers pass basenames"

printf '\n%s passed / %s failed\n' "$PASS" "$FAIL"
[ "$FAIL" = 0 ]
