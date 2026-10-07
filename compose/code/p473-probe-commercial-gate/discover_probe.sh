#!/bin/bash
# P473 — a DISCOVERY probe that is shelf-ready, i.e. it emits P250's commercial-use column.
#
# Why this exists.  P237 says: do not rewrite the licence classifier, source the shared one.
# P250 says: licence FAMILY and COMMERCIAL USE are two questions in two columns, because
# UNKNOWN is indistinguishable from "commercial use is PROHIBITED" and those are opposite
# answers to the only question this KB exists to answer.
#
# Both were hardened on the SHELF instruments.  Pass 36 then wrote a throwaway discovery
# sweep -- new code, outside both controls -- and it reported CC-BY-NC-4.0 as "GRANTED".
# A control that is not in the path of new code is documentation, not a control.  This file
# puts the control in the path: it is the probe a discovery pass runs INSTEAD of a fresh one.
#
# P475 is folded in: the EXISTENCE check decides whether a repo is real, so it gets the same
# case-variation the licence check gets.  MathTutor's README is `master/Readme.md`; with three
# README spellings it would have earned the negative control's verdict.
#
# Usage:  ./discover_probe.sh owner/repo [owner/repo ...]
#         ./discover_probe.sh --self-test
# Output: TSV -- slug, status, family, commercial_use, hit_path, bytes

here="$(cd "$(dirname "$0")" && pwd)"
. "$here/../lib/license_family.sh"

LIC_NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt license license.md
license.txt LICENSE-MIT LICENSE-APACHE LICENSE-2.0.txt COPYING COPYING.txt COPYING.md NOTICE
MIT-LICENSE.txt LICENSE.rst LICENSE-ECL.txt"
# P475: case variation on the existence family too, not only on licences.
EXIST_NAMES="README.md readme.md Readme.md ReadMe.md README.rst README.txt README
package.json pyproject.toml composer.json setup.py requirements.txt Cargo.toml go.mod pom.xml"
BRANCHES="main master"

classify() {   # classify <payload> -> "family<TAB>commercial"
  local p="$1" fam cu
  fam="$(family_of "$p")"
  if commercial_use_ok "$p"; then cu="OK"; else cu="PROHIBIDO"; fi
  printf '%s\t%s' "$fam" "$cu"
}

probe_repo() {
  local slug="$1" br fn code tmp sz
  tmp="$(mktemp)"
  for br in $BRANCHES; do
    for fn in $LIC_NAMES; do
      code=$(curl -s -o "$tmp" -w '%{http_code}' --max-time 15 \
             "https://raw.githubusercontent.com/$slug/$br/$fn")
      if [ "$code" = "200" ]; then
        sz=$(wc -c < "$tmp")
        printf '%s\tLICENSED\t%s\t%s/%s\t%s\n' \
          "$slug" "$(classify "$(cat "$tmp")")" "$br" "$fn" "$sz"
        rm -f "$tmp"; return 0
      fi
    done
  done
  for br in $BRANCHES; do
    for fn in $EXIST_NAMES; do
      code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 \
             "https://raw.githubusercontent.com/$slug/$br/$fn")
      if [ "$code" = "200" ]; then
        printf '%s\tUNGRANTED\t-\tSIN-DETERMINAR\t%s/%s\t-\n' "$slug" "$br" "$fn"
        rm -f "$tmp"; return 0
      fi
    done
  done
  printf '%s\tNO-PAYLOAD\t-\tSIN-DETERMINAR\t-\t-\n' "$slug"
  rm -f "$tmp"; return 0
}

self_test() {
  local pass=0 fail=0 got want f
  check() { # check <label> <got> <want>
    if [ "$2" = "$3" ]; then pass=$((pass+1)); printf '  ok   %-42s %s\n' "$1" "$2"
    else fail=$((fail+1)); printf '  FAIL %-42s got=%s want=%s\n' "$1" "$2" "$3"; fi
  }
  for f in "$here"/fixtures/*.LICENSE; do
    [ -e "$f" ] || continue
    want="$(head -1 "${f%.LICENSE}.expected")"
    got="$(classify "$(cat "$f")" | tr '\t' '/')"
    check "$(basename "$f")" "$got" "$want"
  done
  # The regression that defines this instrument: an NC grant must never read as usable.
  got="$(classify "$(cat "$here/fixtures/cc-by-nc-4.0-crss-ai.LICENSE")" | cut -f2)"
  check "NC payload is not commercially usable" "$got" "PROHIBIDO"
  # And the inverse: a real permissive grant must not be suppressed.
  got="$(classify "$(cat "$here/fixtures/mit-bandup.LICENSE")" | cut -f2)"
  check "MIT payload is commercially usable" "$got" "OK"
  # P475: every case variant of README must be in the existence list.
  for f in README.md readme.md Readme.md; do
    case " $EXIST_NAMES " in *" $f "*) got=present ;; *) got=absent ;; esac
    check "existence list contains $f" "$got" "present"
  done
  printf '\n%d/%d\n' "$pass" "$((pass+fail))"
  [ "$fail" -eq 0 ]
}

case "${1:-}" in
  --self-test) self_test ;;
  "" ) echo "usage: $0 owner/repo [...] | --self-test" >&2; exit 2 ;;
  * ) printf 'slug\tstatus\tfamily\tcommercial\thit_path\tbytes\n'
      for s in "$@"; do probe_repo "$s"; done ;;
esac
