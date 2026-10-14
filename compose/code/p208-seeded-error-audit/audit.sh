#!/usr/bin/env bash
# p208 -- ACTION PT. The audit, rebuilt as a SEPARATE, POINTABLE instrument.
#
# p205, p206 and p207 each ran an audit of this KB's licence column and each
# reported mismatches that were all false. 24 reported, 0 true. Two readings
# of that result are observationally identical from inside those passes:
#
#   (a) the column is clean and the audit is noisy, or
#   (b) the audit cannot detect a wrong cell AT ALL and three passes measured
#       nothing.
#
# The only way to tell them apart is to put errors in the column ON PURPOSE and
# ask whether the audit finds them. That requires the audit to be pointable at
# a DIRECTORY rather than at the repository it lives in -- which is why this
# file takes $1. p207's audit was ad hoc and could not be aimed anywhere.
#
# Ground truth is evidence/permissive-half-census.2026-10-14-p207.tsv: 185
# repositories whose licence family was read from their own blob at HEAD. No
# network: the blob side of the comparison is already on disk.
#
# Usage: ./audit.sh <kb-dir> [census.tsv]
set -u
KB="${1:-.}"
CENSUS="${2:-$KB/evidence/permissive-half-census.2026-10-14-p207.tsv}"

# Coarse family label. A published cell and a census cell must be compared at
# the same granularity or every "CC-unversioned" vs "CC0-1.0" pair is a finding.
fam() {
  local s
  s=$(printf '%s' "$1" | tr '[:lower:]' '[:upper:]')
  case "$s" in
    *AGPL*)                      echo AGPL ;;
    *LGPL*)                      echo LGPL ;;
    *GPL*)                       echo GPL ;;
    *APACHE*)                    echo APACHE ;;
    MIT*|*"MIT-"*|*" MIT"*)      echo MIT ;;
    *BSD*)                       echo BSD ;;
    *MPL*|*"MOZILLA"*)           echo MPL ;;
    *CC0*)                       echo CC0 ;;
    *CC-BY*|*"CC-UNVERSIONED"*)  echo CC ;;
    *UNLICENSE*)                 echo UNLICENSE ;;
    *ISC*)                       echo ISC ;;
    *ELASTIC*)                   echo ELASTIC ;;
    *EPL*)                       echo EPL ;;
    *)                           echo OTHER ;;
  esac
}

# Published families for one repo: every family token appearing on any line
# that also names the repository. This IS p205/p206/p207's extraction and its
# known weakness -- a line naming several repositories attributes every token
# on it to all of them. Reproducing the weakness is the point: PT asks whether
# THIS instrument can see a seeded error, not whether a better one could.
published_families() {
  local repo="$1"
  grep -rhF "$repo" --include='*.md' "$KB/agents" "$KB/repos" "$KB/verticals" "$KB/intel" "$KB/compose/patterns.md" 2>/dev/null \
  | grep -oE 'AGPL-?3(\.0)?|LGPL-?[23](\.[01])?|GPL-?[23](\.0)?|Apache-?2(\.0)?|\bMIT\b|BSD-[234]-Clause|MPL-?2(\.0)?|CC0-?1(\.0)?|CC-BY(-NC)?(-SA)?-4\.0|Unlicense|\bISC\b|Elastic-?2(\.0)?|EPL-?2(\.0)?' \
  | while read -r t; do fam "$t"; done | sort -u
}

printf 'repo\tcensus_family\tpublished_families\tverdict\n'
tail -n +2 "$CENSUS" | while IFS=$'\t' read -r repo p206f p207f bytes; do
  [ -n "${repo:-}" ] || continue
  truth=$(fam "$p207f")
  pubs=$(published_families "$repo" | paste -sd, -)
  if [ -z "$pubs" ]; then
    verdict=NO-PUBLISHED-TOKEN
  elif printf '%s' ",$pubs," | grep -q ",$truth,"; then
    verdict=AGREES
  else
    verdict=MISMATCH
  fi
  printf '%s\t%s\t%s\t%s\n' "$repo" "$truth" "${pubs:--}" "$verdict"
done
