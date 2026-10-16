#!/usr/bin/env bash
# `ACTION XS` (p251) — run every gate control INDIVIDUALLY and report its exit code.
#
# Why this exists: p251 could not run `make hooks` at all — this session's
# sandbox refuses to execute the repository's make recipe — so the pass invoked
# each control on its own.  That loop was reconstructible only from the pass's
# evidence file, which is exactly the shape of knowledge this base keeps losing
# (p248: an unwired classifier; p250: a lint that could not fail).  So it is a
# script.
#
#   bash run_controls.sh [repo-root]        # TSV on stdout; non-zero if any control fails
#
# It reads the control list out of the Makefile through `audit.py`, so it cannot
# drift from the gate it stands in for.
set -uo pipefail
ROOT="${1:-$(cd "$(dirname "$0")/../../.." && pwd)}"
PY="${PY:-python3}"
AUDIT="$(dirname "$0")/audit.py"

printf 'instrument\tsuite\trunner\texit_code\treported_total\n'
rc=0
while IFS=$'\t' read -r _line instr suite _rest; do
  [ "$instr" = "instrument" ] && continue
  [ "$instr" = "-" ] && continue
  case "$suite" in
    *.py) runner="$PY" ;;
    *.sh) runner="bash" ;;
    *)    continue ;;
  esac
  out="$(cd "$ROOT/compose/code/$instr" && "$runner" "$suite" 2>&1)"; code=$?
  [ "$code" -eq 0 ] || rc=1
  total="$(printf '%s' "$out" | grep -oE '[0-9]+/[0-9]+|Ran [0-9]+ tests|ALL CONTROLS PASS|[0-9]+ controls' | tail -1)"
  printf '%s\t%s\t%s\t%s\t%s\n' "$instr" "$suite" "$(basename "$runner")" "$code" "${total:-NA}"
done < <("$PY" -I "$AUDIT" "$ROOT")
exit "$rc"
