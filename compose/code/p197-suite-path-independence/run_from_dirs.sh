#!/bin/bash
# p197 -- the action p196 pre-registered: is `lib/test_license_family.sh` path-independent?
#
# p196 measured 207/207 from `lib/` and 179/181 "from one directory up" and recorded the
# gap as "26 assertions silently skipped".  This runner makes the claim falsifiable: it
# invokes THE SAME suite through SIX cwd/argv forms and records, per form, the total, the
# pass count, the FAIL lines and the SKIP lines.  It classifies nothing and it does not
# touch the classifier; it reads the suite's own last line (`N/M`) and its stderr.
#
# A form that cannot produce a total is recorded RUNFAIL -- never as a zero, and never as
# a pass.  That is the whole point: p196's defect was a suite that reported a SMALLER
# DENOMINATOR without saying so, and an instrument that cannot tell "did not run" from
# "ran and passed" would reproduce exactly that failure one level up.
#
# Usage:  run_from_dirs.sh [out.tsv]
#         SUITE_UNDER_TEST=/path/to/a/suite run_from_dirs.sh out.tsv   # for test_runner.sh
set -u
HERE="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}" 2>/dev/null || printf '%s' "${BASH_SOURCE[0]}")")" && pwd)"
SUITE_ABS="${SUITE_UNDER_TEST:-$HERE/../lib/test_license_family.sh}"
case "$SUITE_ABS" in /*) ;; *) SUITE_ABS="$(cd "$(dirname "$SUITE_ABS")" && pwd)/$(basename "$SUITE_ABS")" ;; esac
SDIR="$(cd "$(dirname "$SUITE_ABS")" && pwd)"; SFILE="$(basename "$SUITE_ABS")"
SPAR="$(cd "$SDIR/.." && pwd)";  SDIRN="$(basename "$SDIR")"
SGPAR="$(cd "$SPAR/.." && pwd)"; SPARN="$(basename "$SPAR")"
OUT="${1:-$HERE/result.$(date +%F)-p197.tsv}"

printf 'form\tcwd\targv\ttotal\tpassed\tfails\tskips\tverdict\n' > "$OUT"
TMPERR="$(mktemp -d)"; trap 'rm -rf "$TMPERR"' EXIT

run_form() { # name cwd argv
  local name="$1" cwd="$2" argv="$3" out last passed total fails skips verdict
  out="$(cd "$cwd" 2>/dev/null && bash "$argv" 2>"$TMPERR/e")" || true
  skips=$(grep -c '^SKIP' "$TMPERR/e" 2>/dev/null || true); skips=${skips:-0}
  last="$(printf '%s\n' "$out" | grep -Eo '^[0-9]+/[0-9]+$' | tail -1)"
  fails=$(printf '%s\n' "$out" | grep -c '^FAIL' || true); fails=${fails:-0}
  if [ -z "$last" ]; then
    passed=RUNFAIL; total=RUNFAIL; verdict=RUNFAIL
  else
    passed="${last%%/*}"; total="${last##*/}"
    if [ "$skips" -gt 0 ]; then verdict=SILENT-SKIP
    elif [ "$passed" = "$total" ]; then verdict=CLEAN
    else verdict=FAILING; fi
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$name" "$cwd" "$argv" "$total" "$passed" "$fails" "$skips" "$verdict" >> "$OUT"
  printf '%-18s total=%-8s passed=%-8s FAIL=%-3s SKIP=%-3s %s\n' "$name" "$total" "$passed" "$fails" "$skips" "$verdict"
}

run_form abs-from-tmp   "/tmp"   "$SUITE_ABS"
run_form in-suite-dir   "$SDIR"  "$SFILE"
run_form rel-from-par   "$SPAR"  "$SDIRN/$SFILE"
run_form rel-from-gpar  "$SGPAR" "$SPARN/$SDIRN/$SFILE"
SIB="$(mktemp -d "$SPAR/.p197sib.XXXXXX")"
run_form rel-up-sibling "$SIB"   "../$SDIRN/$SFILE"
rmdir "$SIB" 2>/dev/null || rm -rf "$SIB"
# The SYMLINK form is not a cwd question at all: ${BASH_SOURCE[0]} names the LINK, so a
# dirname of it points at a directory where license_family.sh is not.  Measured 19/163
# before the fix -- the classifier never loaded and the suite still PRINTED A TOTAL.
LNK="$(mktemp -d)"; ln -sf "$SUITE_ABS" "$LNK/suite.sh"
run_form via-symlink    "$LNK"   "./suite.sh"
rm -rf "$LNK"

echo "--- $OUT"
totals=$(awk -F'\t' 'NR>1{print $4}' "$OUT" | sort -u | tr '\n' ' ')
verds=$(awk -F'\t'  'NR>1{print $8}' "$OUT" | sort -u | tr '\n' ' ')
echo "totals seen: $totals"
echo "verdicts   : $verds"
if [ "$totals" = "$(awk -F'\t' 'NR==2{print $4}' "$OUT") " ] && [ "$verds" = "CLEAN " ]; then
  echo "PATH-INDEPENDENT: 6/6 forms agree on the total and every form is clean"; exit 0
fi
echo "NOT PATH-INDEPENDENT: forms disagree on the total, or a form is not clean"; exit 1
