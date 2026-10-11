#!/usr/bin/env bash
# count_tags.sh — the counting rule, as a pure function over an `ls-remote --tags` dump on stdin.
# Emits: lines<TAB>deref<TAB>real<TAB>latest
# A dereference line (`refs/tags/X^{}`) is the commit an ANNOTATED tag points at. It is the same
# tag, so a count of lines inflates a release count by the number of annotated tags — and by zero
# where the tags are lightweight (p128's P128-A). This file exists so the rule is testable offline.
set -uo pipefail
dump=$(cat)
total=$(printf '%s\n' "$dump" | grep -c 'refs/tags/')
deref=$(printf '%s\n' "$dump" | grep -c 'refs/tags/.*\^{}$')
latest=$(printf '%s\n' "$dump" | grep 'refs/tags/' | grep -v '\^{}$' | sed 's|.*refs/tags/||' | tail -1)
printf '%s\t%s\t%s\t%s\n' "$total" "$deref" "$((total-deref))" "$latest"
