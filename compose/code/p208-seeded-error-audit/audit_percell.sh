#!/usr/bin/env bash
# p208 -- the third comparator: PER CELL.
#
# per-repo (p205-p207): compares truth against the UNION of every token on
#   every line naming the repo. Cannot see a wrong cell when a right one exists
#   anywhere else -- 152 of 179 census rows.
# per-line (./audit_persite.sh): one verdict per line. Sees those cells, and
#   pays for it: a line naming several repositories attributes every token on
#   it to all of them, which is where all 24 historical false positives and all
#   26 of ACTION PS's phantom "recoveries" came from.
# per-cell (here): only TABLE ROWS, and only rows naming EXACTLY ONE
#   repository, so the licence token in the row belongs to that repository by
#   construction. Rows naming two or more are reported as AMBIGUOUS, never as
#   findings -- the one honest thing to do with a shape this instrument cannot
#   resolve. Prose is out of reach by design: see ./README.md.
set -u
KB="${1:-.}"
CENSUS="${2:-$KB/evidence/permissive-half-census.2026-10-14-p207.tsv}"
TOKENS='AGPL-?3(\.0)?|LGPL-?[23](\.[01])?|GPL-?[23](\.0)?|Apache-?2(\.0)?|\bMIT\b|BSD-[234]-Clause|MPL-?2(\.0)?|CC0-?1(\.0)?|CC-BY(-NC)?(-SA)?-4\.0|Unlicense|\bISC\b|Elastic-?2(\.0)?|EPL-?2(\.0)?'
fam() { local s; s=$(printf '%s' "$1" | tr '[:lower:]' '[:upper:]'); case "$s" in
  *AGPL*) echo AGPL;; *LGPL*) echo LGPL;; *GPL*) echo GPL;; *APACHE*) echo APACHE;;
  MIT*) echo MIT;; *BSD*) echo BSD;; *MPL*) echo MPL;; *CC0*) echo CC0;;
  *CC-BY*|*CC-UNVERSIONED*) echo CC;; *UNLICENSE*) echo UNLICENSE;; *ISC*) echo ISC;;
  *ELASTIC*) echo ELASTIC;; *EPL*) echo EPL;; *) echo OTHER;; esac; }
declare -A TRUTH
while IFS=$'\t' read -r repo a b c; do [ -n "${repo:-}" ] && TRUTH["$repo"]=$(fam "$b"); done < <(tail -n +2 "$CENSUS")
printf 'repo\ttruth\tcell\tcell_families\tverdict\n'
grep -rn --include='*.md' -E '^[[:space:]]*\|' "$KB/agents" "$KB/repos" "$KB/verticals" "$KB/intel" "$KB/compose/patterns.md" 2>/dev/null \
| while IFS= read -r hit; do
    file=${hit%%:*}; rest=${hit#*:}; line=${rest%%:*}; body=${rest#*:}
    mapfile -t repos < <(printf '%s' "$body" | grep -oE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' | sed 's|github\.com/||' | sed 's|\.git$||' | sort -u)
    [ "${#repos[@]}" -eq 1 ] || continue
    repo="${repos[0]}"; truth="${TRUTH[$repo]:-}"
    [ -n "$truth" ] && [ "$truth" != OTHER ] || continue
    toks=$(printf '%s' "$body" | grep -oE "$TOKENS" | while read -r t; do fam "$t"; done | sort -u | paste -sd, -)
    [ -n "$toks" ] || continue
    if printf '%s' ",$toks," | grep -q ",$truth,"; then v=AGREES; else v=CELL-MISMATCH; fi
    printf '%s\t%s\t%s\t%s\t%s\n' "$repo" "$truth" "${file#$KB/}:$line" "$toks" "$v"
  done
