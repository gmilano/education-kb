#!/usr/bin/env bash
# p205 — offline regression test. Runs with NO NETWORK against ./fixtures,
# which are real licence bodies captured 2026-10-14. Every case that fails
# under p203's classifier is marked REGRESSION.
cd "$(dirname "$0")" || exit 1
source ./classify.sh
OLD=../p203-grant-blob-reader/classify.sh
pass=0; fail=0
check() { # check <fixture> <expected>
  local got; got=$(classify_grant "$(cat "fixtures/$1")")
  if [ "$got" = "$2" ]; then pass=$((pass+1)); printf '  ok    %-28s -> %s\n' "$1" "$got"
  else fail=$((fail+1)); printf '  FAIL  %-28s -> %s (expected %s)\n' "$1" "$got" "$2"; fi
}
echo "p205 classifier — 12 real bodies"
check gpl-3.0.txt            GPL-3.0
check gpl-3.0-moodle.txt     GPL-3.0
check agpl-3.0.txt           AGPL-3.0
check mpl-2.0.txt            MPL-2.0
check ecl-2.0.txt            ECL-2.0
check bsl-1.1.txt            NON-OSI-BSL
check apache-2.0.txt         Apache-2.0
check mit.txt                MIT
check cc-by-sa-4.0.txt       CC-BY-SA-4.0
check cc-by-4.0-twoscope.md  TWO-SCOPE
check cc-by-sa-4.0-deed.md   CC-BY-SA-4.0-DEED
check apache-2.0-kaldi-prefixed.txt Apache-2.0
check lgpl.txt               LGPL-3.0
echo "  --- empty-input control"
[ "$(classify_grant '')" = "EMPTY" ] && { pass=$((pass+1)); echo "  ok    empty -> EMPTY"; } || { fail=$((fail+1)); echo "  FAIL  empty"; }
echo "  --- two-scope detector (Carpentries shape)"
[ "$(scope_headings "$(cat fixtures/cc-by-4.0-twoscope.md)")" = "2" ] && { pass=$((pass+1)); echo "  ok    scope_headings -> 2"; } || { fail=$((fail+1)); echo "  FAIL  scope_headings"; }

echo; echo "Same fixtures under p203's classifier (the regression this fixes):"
if [ -f "$OLD" ]; then
  ( source "$OLD"
    for f in gpl-3.0.txt gpl-3.0-moodle.txt mpl-2.0.txt ecl-2.0.txt bsl-1.1.txt; do
      printf '  p203: %-22s -> %s\n' "$f" "$(classify_grant "$(cat "fixtures/$f")")"
    done )
else echo "  (p203 classifier not found)"; fi
echo; echo "pass=$pass fail=$fail"; [ "$fail" -eq 0 ]
