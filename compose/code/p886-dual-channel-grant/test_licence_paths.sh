#!/bin/sh
# p886 controls for the case-complete ladder. No network.
. ./licence_paths.sh
fail=0; pass=0
has() { for p in $LICENCE_PATHS; do [ "$p" = "$1" ] && return 0; done; return 1; }
ck()  { if has "$1"; then pass=$((pass+1)); else echo "FAIL: missing $1 ($2)"; fail=$((fail+1)); fi; }
# the two entries whose absence p886 MEASURED as a manufactured absence
ck LICENSE.TXT  "openedx/XBlock + openedx/xblock-sdk, Apache-2.0, sha256_12 cfc7749b96f6"
ck LICENSE.rst  "the Open edX / Python-ecosystem convention"
# every entry p885's ladder already had must survive, or p886 is a regression
for p in LICENSE LICENSE.md LICENSE.txt license.txt COPYING COPYING.txt COPYING.TXT LICENCE; do
  ck "$p" "carried from p885's ladder"
done
# the first four must stay the first four: 156/167 rows exit there
first4=$(printf '%s' "$LICENCE_PATHS" | tr -s ' \n' '\n\n' | head -4 | tr '\n' ' ')
case "$first4" in
  "LICENSE LICENSE.md LICENSE.txt LICENSE.TXT ") pass=$((pass+1)) ;;
  *) echo "FAIL: probe order changed, got [$first4]"; fail=$((fail+1)) ;;
esac
# no duplicates: a duplicate is a wasted request on every single repo
dups=$(printf '%s' "$LICENCE_PATHS" | tr -s ' \n' '\n\n' | sort | uniq -d)
if [ -n "$dups" ]; then echo "FAIL: duplicate paths: $dups"; fail=$((fail+1)); else pass=$((pass+1)); fi
echo "p886 licence-path controls: $pass passed, $fail failed"
[ "$fail" -eq 0 ]
