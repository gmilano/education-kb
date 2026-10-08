#!/usr/bin/env bash
# p782 -- the POLICY gate.  Gap 278's bounded remedy, as an instrument.
#
# Every recipe on this shelf gates on LICENCE.  P764 is the counter-example that shows a
# licence gate is not sufficient: `algorithm0r/canvas-lms-mcp` is MIT and exposes grading,
# comments and rubrics -- it passes every licence check this KB has written, and in several
# jurisdictions the FUNCTION it exposes is gated or prohibited regardless of its licence.
#
# This gate answers: "may this FUNCTION be deployed in this JURISDICTION?"  It reads
# `intel/policy-matrix.tsv` -- data, not prose -- and never guesses.
#
# Exit status is the verdict:
#   0 = clear (UNREGULATED, or MANDATED which is a duty, not a bar)
#   3 = GATED      -- deployable with named obligations; the caller must read them
#   4 = PROHIBITED -- do not build it for this jurisdiction
#   5 = PROPOSED   -- not in force; the row exists so nobody plans against a bill
#   6 = NO ROW     -- this pair was never measured.  NOT a green light (P476).
#
# Usage: gate.sh <function> [jurisdiction|region]
#        gate.sh --functions | --jurisdictions | --region <REGION>
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
TSV="${POLICY_MATRIX:-$HERE/../../../intel/policy-matrix.tsv}"
[ -r "$TSV" ] || { echo "FATAL: cannot read $TSV" >&2; exit 2; }

# rows(): the data minus comments and minus the header line.  One place, so a change to the
# file's comment convention cannot silently halve the denominator (P344).
rows() { grep -v '^#' "$TSV" | awk -F'\t' 'NR>1 && NF>=4'; }

case "${1:-}" in
  --functions)     rows | cut -f3 | sort -u; exit 0 ;;
  --jurisdictions) rows | cut -f2 | sort -u; exit 0 ;;
  --region)
    r="${2:?--region needs a value}"
    # Region is a CLOSED vocabulary; a typo must fail loudly, not return an empty set that
    # reads exactly like "nothing is regulated there".
    case "$r" in
      "North America"|EMEA|APAC|LATAM|Global) ;;
      *) echo "FATAL: '$r' is not one of the five regions (North America|EMEA|APAC|LATAM|Global)" >&2; exit 2 ;;
    esac
    n=$(rows | awk -F'\t' -v r="$r" '$1==r' | wc -l | tr -d ' ')
    echo "== $r -- $n row(s)"
    rows | awk -F'\t' -v r="$r" '$1==r {printf "   %-22s %-30s %-12s %s\n", $2, $3, $4, $5}'
    [ "$n" -gt 0 ] || { echo "   (no rows -- UNMEASURED, which is not the same as unregulated)"; exit 6; }
    exit 0 ;;
esac

fn="${1:?usage: gate.sh <function> [jurisdiction|region]}"
scope="${2:-}"

if [ -n "$scope" ]; then
  match=$(rows | awk -F'\t' -v f="$fn" -v s="$scope" '$3==f && ($2==s || $1==s)')
else
  match=$(rows | awk -F'\t' -v f="$fn" '$3==f')
fi

if [ -z "$match" ]; then
  echo "NO ROW: function='$fn'${scope:+ scope='$scope'} was never measured."
  echo "  >> This is an UNMEASURED pair, not a permission (P476).  Measure it or say so."
  exit 6
fi

printf '%s\n' "$match" | awk -F'\t' '{printf "  %-14s %-22s %-28s %-12s %-12s %s\n", $1, $2, $3, $4, $5, $6}'
echo "  -- band: every row above is REPORTED, never payload-read.  See the header of"
echo "     intel/policy-matrix.tsv for why that is a property of the channel, not a choice."

# The strictest verdict present decides, because a deployment spans the jurisdictions it
# ships to.  Order matters: PROHIBITED dominates GATED dominates PROPOSED.
verds=$(printf '%s\n' "$match" | cut -f4 | sort -u)
case "$verds" in
  *PROHIBITED*) echo "  VERDICT: PROHIBITED (strictest row wins)"; exit 4 ;;
esac
case "$verds" in
  *GATED*)      echo "  VERDICT: GATED -- read the obligations in the note column"; exit 3 ;;
esac
case "$verds" in
  *PROPOSED*)   echo "  VERDICT: PROPOSED only -- not in force; do not plan against it"; exit 5 ;;
esac
echo "  VERDICT: clear (UNREGULATED/MANDATED)"
exit 0
