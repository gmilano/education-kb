#!/usr/bin/env bash
# p550 — DUPLICATE DEFINITION SWEEP.
#
# Why this instrument exists (P550, pass 45 del 2026-10-07).  `lib/license_family.sh` is this
# KB's SHARED hardened control: every licence verdict on the shelf is classified by it, and its
# own header says "source this, do not rewrite it".  It defines `commercial_use_ok()` TWICE.
# Bash keeps the LAST definition, so the live gate is the hardened one and every published
# verdict is sound -- but it is sound BY SOURCE ORDER, not by construction.  The first cut
# (pass 82, pure token-match over the body, no family gate) is still in the file as dead code,
# immediately above a comment block that explains why it was wrong.  The fix was APPENDED
# rather than SUBSTITUTED.
#
# This is a different failure class from P541/P542.  Those were instruments that exit 0 having
# measured nothing -- a false claim of cleanliness.  This is an instrument that measures
# CORRECTLY while carrying a second, contradictory implementation of the same gate, where the
# only thing standing between the shelf and an inverted verdict is which definition `source`
# reads last.  A suite cannot see it: the suite calls the name, the name resolves to one body,
# and 132/132 says nothing about the body that did not resolve.
#
# A duplicate definition is only a HAZARD when the bodies DIFFER.  Re-declaring a function
# with a byte-identical body is redundant, not dangerous, and this sweep says so rather than
# padding its own count.  A frozen control snapshot that inherited a duplicate from the file
# it snapshots is likewise declared, not accused: reproducing old behaviour is its job.
#
# P542's lesson is applied to this sweep itself: invoked with no roots it exits 2 and judges
# nothing, so "0 findings" can never be a reading of an empty run.
set -uo pipefail

SELFDIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

usage() { echo "usage: $0 <root> [root...]   (scans *.sh and *.py beneath each root)" >&2; }

[ "$#" -ge 1 ] || { usage; echo "p550: REFUSED — no root given, nothing judged" >&2; exit 2; }
for r in "$@"; do
  [ -d "$r" ] || { echo "p550: REFUSED — not a directory: $r" >&2; exit 2; }
done

# A control snapshot is a file whose name declares it frozen.  Named, not guessed.
is_frozen_control() {
  case "$(basename "$1")" in
    *PRE-P*-CONTROL-*|*.CONTROL-*|*.frozen.*) return 0 ;;
  esac
  return 1
}

# body_of <file> <name> <lang> <nth> -> the nth definition's body text on stdout.
body_of() {
  local f="$1" n="$2" lang="$3" nth="$4"
  if [ "$lang" = sh ]; then
    awk -v name="$n" -v want="$nth" '
      $0 ~ "^"name"\\(\\)" { c++ }
      c==want { print }
      c==want && /^}/ { exit }
    ' "$f"
  else
    awk -v name="$n" -v want="$nth" '
      $0 ~ "^def "name"\\(" { c++; if (c==want) { inb=1 } else if (inb) { exit } }
      inb { print }
      inb && c==want && NR>1 && /^[^ \t#]/ && $0 !~ "^def "name"\\(" { exit }
    ' "$f"
  fi
}

# P550b: the exit status is computed FROM the emitted table, never from a second counter
# kept in parallel with it.  The suite's M2 mutant (drop the increment) survived exactly that
# duplication -- a private counter that can disagree with the published rows is the same
# failure class this instrument exists to report.
ROWS=$(mktemp); trap 'rm -f "$ROWS"' EXIT
scanned=0

while IFS= read -r f; do
  case "$f" in *.sh) lang=sh; pat='^[a-zA-Z_][a-zA-Z0-9_]*\(\)' ;;
                *.py) lang=py; pat='^def [a-zA-Z_][a-zA-Z0-9_]*' ;;
                *) continue ;; esac
  scanned=$((scanned+1))
  # P550c: scan the file with heredoc bodies / triple-quoted strings blanked out, so a
  # fixture that merely CONTAINS a definition is not counted as one.
  stripped=$(awk -v lang="$lang" -f "$SELFDIR/strip_quoted.awk" "$f" 2>/dev/null)
  dups=$(printf '%s\n' "$stripped" | grep -oE "$pat" 2>/dev/null | sed 's/^def //; s/()$//' | sort | uniq -d)
  [ -n "$dups" ] || continue
  while IFS= read -r sym; do
    [ -n "$sym" ] || continue
    if [ "$lang" = sh ]; then
      n=$(printf '%s\n' "$stripped" | grep -cE "^${sym}\(\)")
    else
      n=$(printf '%s\n' "$stripped" | grep -cE "^def ${sym}\(")
    fi
    # Compare every body against the first.
    differ=no
    b1=$(body_of "$f" "$sym" "$lang" 1)
    i=2
    while [ "$i" -le "$n" ]; do
      bi=$(body_of "$f" "$sym" "$lang" "$i")
      [ "$bi" = "$b1" ] || differ=yes
      i=$((i+1))
    done
    # Which definition wins: bash keeps the LAST, python keeps the LAST too.
    live="last(#$n)"
    if is_frozen_control "$f"; then
      class=P550-FROZEN-CONTROL
    elif [ "$differ" = no ]; then
      class=P550-REDUNDANT-IDENTICAL
    else
      class=P550-SHADOWED-DIVERGENT
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$f" "$lang" "$sym" "$n" "$class" "$live" "$differ" >> "$ROWS"
  done <<< "$dups"
done < <(for r in "$@"; do find "$r" -type f \( -name '*.sh' -o -name '*.py' \); done)

printf 'file\tlang\tsymbol\tn_defs\tclass\tlive_def\tbodies\n'
cat "$ROWS"

# Both the summary and the verdict are read back out of the rows that were just published.
findings=$(awk -F'\t' '$5=="P550-SHADOWED-DIVERGENT"' "$ROWS" | wc -l | tr -d ' ')
echo "p550: scanned=$scanned files; SHADOWED-DIVERGENT=$findings" >&2
[ "$scanned" -gt 0 ] || { echo "p550: REFUSED — root(s) held no .sh/.py file, nothing judged" >&2; exit 2; }
[ "$findings" -eq 0 ]
