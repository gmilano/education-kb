#!/usr/bin/env bash
# p752-prose-vs-committed-results
#
# Asks one question before a pass publishes a licence claim about a slug:
#
#     "Does this KB already hold a committed, machine-readable answer
#      that contradicts what I am about to write?"
#
# WHY THIS EXISTS (P752). Pass 57 published that `openeducat/openeducat_erp`
# has no locatable licence grant ("reference-to-nothing"). At that moment this
# repository already contained, committed, in at least eight result TSVs across
# several instruments:
#
#     openeducat/openeducat_erp   LICENSE   8241   LGPL
#     openeducat/openeducat_erp   AGREE     LGPL   LGPL   LGPL
#
# ...plus a README paragraph from pass 53 quoting the payload title verbatim,
# and `p560-epl-mpl-version-read` / `p637-cross-instrument-licence-agreement`
# using the repo as a FIXTURE for the LGPL-3.0 version read.
#
# So pass 57's error was NOT a measurement failure -- no network was required to
# avoid it. It was a failure to consult the KB's own data shelf. That is a
# different and more tractable class of defect than anything in P725-P751:
# every other licence defect this KB has found needed a better probe, and this
# one needed a `grep` of files already on disk.
#
# NOTE ON SCOPE (P744): this instrument reads ONLY local committed files. It
# enumerates nothing on the network, so the bulk-enumeration constraint that
# blocks Gap 273's full sweep does not apply to it. This is the cheapest
# verification layer this KB has, and it was the last one built.
#
# Usage:
#   ./check_claim.sh <owner/repo>            # print every committed verdict held
#   ./check_claim.sh <owner/repo> UNGRANTED  # exit 1 if the KB contradicts you
#   ./check_claim.sh --self-test
#
# Exit codes: 0 = no contradiction found; 1 = CONTRADICTION; 2 = usage error.

set -uo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"   # -> compose/
KB="$(cd "$ROOT/.." && pwd)"                  # -> repo root

FAMILIES='MIT|Apache|AGPL|LGPL|GPL|BSD|MPL|EPL|ISC|CC|Unlicense|WTFPL|BSL|OTHER'

usage() { echo "usage: $0 <owner/repo> [asserted_family_or_UNGRANTED]" >&2; exit 2; }

self_test() {
  local fail=0
  # The regression this instrument was built for must be caught.
  if evidence="$(gather openeducat/openeducat_erp)" && [ -n "$evidence" ]; then
    echo "PASS  openeducat evidence is discoverable on disk"
  else
    echo "FAIL  openeducat evidence not found"; fail=1
  fi
  if ! "$0" openeducat/openeducat_erp UNGRANTED >/dev/null 2>&1; then
    echo "PASS  asserting UNGRANTED for openeducat is flagged as a contradiction"
  else
    echo "FAIL  the pass-57 regression was NOT caught"; fail=1
  fi
  if "$0" openeducat/openeducat_erp LGPL >/dev/null 2>&1; then
    echo "PASS  asserting LGPL for openeducat is accepted"
  else
    echo "FAIL  the correct family was rejected"; fail=1
  fi
  if "$0" no-such-owner/no-such-repo UNGRANTED >/dev/null 2>&1; then
    echo "PASS  a slug the KB holds nothing on yields no contradiction"
  else
    echo "FAIL  unknown slug wrongly flagged"; fail=1
  fi
  [ "$fail" = 0 ] && echo "4/4 green" || echo "self-test FAILED"
  return "$fail"
}

# Every committed line that mentions the slug, from result/payload/sweep data
# and from prose, with its source file.
gather() {
  local slug="$1"
  grep -rIn --include='*.tsv' --include='*.txt' --include='*.md' \
       -F "$slug" "$KB/compose/code" "$KB/README.md" 2>/dev/null \
    | grep -viE 'p752-prose-vs-committed-results' || true
}

[ "$#" -ge 1 ] || usage
[ "$1" = "--self-test" ] && { self_test; exit $?; }

slug="$1"; asserted="${2:-}"
evidence="$(gather "$slug")"

if [ -z "$evidence" ]; then
  echo "NO_PRIOR_EVIDENCE  $slug — this KB holds nothing committed on it."
  exit 0
fi

# Families named on the same committed line as the slug, in TSV data only.
held="$(printf '%s\n' "$evidence" \
        | grep -E '\.tsv:' \
        | grep -oiE "\b($FAMILIES)(-[0-9.]+)?\b" \
        | tr '[:lower:]' '[:upper:]' \
        | sed 's/^\(AGPL\|LGPL\|GPL\|MIT\|APACHE\|BSD\|MPL\|EPL\|ISC\|CC\|UNLICENSE\|WTFPL\|BSL\|OTHER\).*/\1/' \
        | sort | uniq -c | sort -rn)"

echo "=== committed evidence this KB already holds for $slug ==="
printf '%s\n' "$evidence" | sed "s|^$KB/||" | head -40
echo
echo "=== licence families named alongside it in committed TSVs ==="
printf '%s\n' "${held:-  (none)}"

[ -z "$asserted" ] && exit 0

a_up="$(printf '%s' "$asserted" | tr '[:lower:]' '[:upper:]')"
top="$(printf '%s\n' "$held" | awk 'NR==1{print $2}')"

if [ -z "$top" ]; then
  echo
  echo "NO_FAMILY_HELD  cannot adjudicate '$asserted' from committed data."
  exit 0
fi

case "$a_up" in
  UNGRANTED|NONE|NO_GRANT|NO_PAYLOAD)
    echo
    echo "🔴 CONTRADICTION: you are asserting '$asserted', and this KB holds"
    echo "   committed evidence of a '$top' grant for $slug."
    echo "   This is the pass-57 regression shape (P752). Read the payload again"
    echo "   before publishing — and scan the whole licence file for a grant"
    echo "   body rather than resolving a reference inside it (P742)."
    exit 1 ;;
esac

if [ "$a_up" != "$top" ]; then
  echo
  echo "🟡 DIVERGENCE: you assert '$asserted'; committed data most often says '$top'."
  echo "   Not necessarily an error — a relicence or a version read may explain it —"
  echo "   but say which, in the pass, rather than letting the shelves disagree."
  exit 1
fi

echo
echo "🟢 AGREES with committed data ('$top')."
exit 0
