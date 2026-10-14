#!/usr/bin/env bash
# p208 -- the repaired comparator. PER SITE, not per repo.
#
# The defect ACTION PT exposed is in the COMPARISON, not the classifier and not
# the column: p205-p207 compared the TRUE family against the UNION of every
# family token printed on every line that names the repository. A row whose
# true family is printed at two or more sites therefore cannot produce a
# mismatch no matter what any one cell says -- 152 of 179 rows in the census.
#
# This comparator asks the question one site at a time. A site is a LINE that
# names the repository and carries at least one family token, and a site is
# flagged when NONE of its tokens is the true family. It costs false positives
# on lines that name several repositories -- measured, not assumed, in
# ./README.md -- and it is the only shape that can see a single wrong cell.
set -u
KB="${1:-.}"
CENSUS="${2:-$KB/evidence/permissive-half-census.2026-10-14-p207.tsv}"
TOKENS='AGPL-?3(\.0)?|LGPL-?[23](\.[01])?|GPL-?[23](\.0)?|Apache-?2(\.0)?|\bMIT\b|BSD-[234]-Clause|MPL-?2(\.0)?|CC0-?1(\.0)?|CC-BY(-NC)?(-SA)?-4\.0|Unlicense|\bISC\b|Elastic-?2(\.0)?|EPL-?2(\.0)?'
fam() { local s; s=$(printf '%s' "$1" | tr '[:lower:]' '[:upper:]'); case "$s" in
  *AGPL*) echo AGPL;; *LGPL*) echo LGPL;; *GPL*) echo GPL;; *APACHE*) echo APACHE;;
  MIT*) echo MIT;; *BSD*) echo BSD;; *MPL*) echo MPL;; *CC0*) echo CC0;;
  *CC-BY*|*CC-UNVERSIONED*) echo CC;; *UNLICENSE*) echo UNLICENSE;; *ISC*) echo ISC;;
  *ELASTIC*) echo ELASTIC;; *EPL*) echo EPL;; *) echo OTHER;; esac; }
printf 'repo\ttruth\tsite\tsite_families\tverdict\n'
tail -n +2 "$CENSUS" | while IFS=$'\t' read -r repo p206f p207f bytes; do
  [ -n "${repo:-}" ] || continue
  truth=$(fam "$p207f")
  [ "$truth" = OTHER ] && continue        # comparator cannot name it; not a finding
  grep -rnF "$repo" --include='*.md' "$KB/agents" "$KB/repos" "$KB/verticals" "$KB/intel" "$KB/compose/patterns.md" 2>/dev/null \
  | while IFS= read -r hit; do
      line=${hit#"$KB"/}
      body=${hit#*:*:}
      toks=$(printf '%s' "$body" | grep -oE "$TOKENS" | while read -r t; do fam "$t"; done | sort -u | paste -sd, -)
      [ -n "$toks" ] || continue
      if printf '%s' ",$toks," | grep -q ",$truth,"; then v=AGREES; else v=SITE-MISMATCH; fi
      printf '%s\t%s\t%s\t%s\t%s\n' "$repo" "$truth" "${line%%:*}:$(printf '%s' "$hit" | cut -d: -f2)" "$toks" "$v"
    done
done
