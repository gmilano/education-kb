#!/usr/bin/env bash
# promotion-audit.sh — ACTION p837-A
#
# WHY THIS EXISTS
#   Three times now this base has published "<address> — Filed to <shelf>" in an
#   append-only trending file while the address was absent from that shelf:
#     p597 claimed six, p677 audited p597 and claimed the same six, p837 found all
#     six still absent. The measurements were never wrong; the FILING was, and the
#     mechanism is a rewrite of a curated shelf that drops rows while the running
#     row count keeps counting ADDITIONS only. See T130.
#
# WHAT IT DOES
#   Extracts every (address, shelf) pair published in the two append-only trending
#   files and greps the named shelf for the address. Exits non-zero if any pair fails.
#
# USAGE
#   ingest/promotion-audit.sh            # audit every published pair
#   ingest/promotion-audit.sh --quiet    # only print failures
#
# LIMITS, stated so a later pass does not over-trust it
#   - It matches the "Filed to"/"filed to" shelf path inside the SAME table row as a
#     github.com/owner/repo address. Prose claims outside a table row are not caught.
#   - Owner/repo matching is case-insensitive, because GitHub is (this base has
#     published both `anubislms/anubis` and `AnubisLMS/Anubis` for one repository).
#   - A PASS means the slug appears somewhere in the shelf, not that the row is good.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

QUIET=0
[ "${1:-}" = "--quiet" ] && QUIET=1

TRENDING=(agents/trending.md repos/trending.md)
pass=0; fail=0

while IFS=$'\t' read -r slug shelf src; do
  [ -z "${slug:-}" ] && continue
  if [ ! -f "$shelf" ]; then
    printf 'MISSING-SHELF  %-55s -> %s   (claimed in %s)\n' "$slug" "$shelf" "$src"
    fail=$((fail+1)); continue
  fi
  if grep -qi -- "$slug" "$shelf"; then
    pass=$((pass+1))
    [ "$QUIET" -eq 0 ] && printf 'PASS           %-55s -> %s\n' "$slug" "$shelf"
  else
    printf 'ABSENT         %-55s -> %s   (claimed in %s)\n' "$slug" "$shelf" "$src"
    fail=$((fail+1))
  fi
done < <(
  for f in "${TRENDING[@]}"; do
    [ -f "$f" ] || continue
    grep -ioE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+[^|]*\|[^|]*\|[^|]*\|[^|]*(agents/top|repos/foundations|verticals/solutions|intel/market|intel/trends|compose/patterns)\.md' "$f" |
    while IFS= read -r row; do
      s=$(printf '%s' "$row" | grep -oE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' | head -1 | sed 's#github\.com/##; s#\.git$##')
      sh=$(printf '%s' "$row" | grep -oE '(agents/top|repos/foundations|verticals/solutions|intel/market|intel/trends|compose/patterns)\.md' | tail -1)
      [ -n "$s" ] && [ -n "$sh" ] && printf '%s\t%s\t%s\n' "$s" "$sh" "$f"
    done
  done | sort -u
)

echo
echo "promotion-audit: ${pass} pass, ${fail} absent-or-unshelved"
[ "$fail" -gt 0 ] && exit 1
exit 0
