#!/usr/bin/env bash
# derive-counts.sh -- Gap 543-E. Derive shelf counts FROM THE TABLES, never from prose.
#
# WHY: a count written in prose beside the rows it counts goes stale the moment a pass
# adds a row and forgets the sentence. p543 found agents/top.md's shelf heading stale by a
# whole pass; repos/foundations.md carries the same defect as Gap 534-E.
#
# WHAT p544 MEASURED, and the honest limit:
#   * agents/top.md's shelf table IS derivable: 64 data rows, which AGREES with its heading.
#   * The heading's SECOND figure ("72 with the eight filed in their own sections above")
#     is NOT derivable from any table -- those eight rows live in per-pass prose sections.
#   * repos/foundations.md is NOT derivable at all: 175 distinct GitHub addresses appear in
#     its table rows against a claimed seventy-two, because several of its sections are
#     CENSUSES (the Moodle MCP census alone covers 222 addresses) whose rows are not shelf rows.
#
# SO THE DURABLE FIX IS NOT A COUNTING GATE. It is a ROW-LEVEL DISPOSITION MARKER that a gate
# can count. Without one, a gate must GUESS which rows are shelf rows -- and an inferred count
# is exactly the "inference becomes wrong data" failure this base exists to avoid.
# This script therefore reports what IS derivable and ABSTAINS, loudly, on what is not.
#
# usage: bash ingest/derive-counts.sh [repo-root]
set -u
root="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
top="$root/agents/top.md"
fnd="$root/repos/foundations.md"
rc=0

# --- the one derivable figure: the shelf table of agents/top.md --------------------
# Bounded by its own "## Shelf" heading and the next "##" heading at the same level.
start=$(grep -nE '^## Shelf' "$top" | head -1 | cut -d: -f1)
if [ -z "${start:-}" ]; then
  echo "ABSTAIN agents/top.md: no '## Shelf' heading found; nothing to derive."
  exit 2
fi
end=$(awk -v s="$start" 'NR>s && /^## /{print NR; exit}' "$top")
[ -z "${end:-}" ] && end=$(wc -l < "$top")

rows=$(awk -v s="$start" -v e="$end" 'NR>s && NR<e && /^\|/' "$top" \
       | grep -vE '^\|[[:space:]-]*\|[[:space:]-]*\|' \
       | grep -vE '^\| *Agent *\|' | wc -l | tr -d ' ')
claimed=$(sed -n "${start}p" "$top" | grep -oE '[0-9]+' | head -1)

echo "agents/top.md  shelf table: derived=${rows}  claimed_in_heading=${claimed:-none}"
if [ -n "${claimed:-}" ] && [ "$rows" != "$claimed" ]; then
  echo "  RED  heading disagrees with its own table -- rewrite the heading, not the table."
  rc=1
else
  echo "  GREEN heading agrees with its table."
fi

# --- the figures that must NOT be guessed -----------------------------------------
addr=$(grep -E '^\|' "$fnd" | grep -oE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' \
       | sed 's#github.com/##' | sort -u | wc -l | tr -d ' ')
echo "repos/foundations.md: ${addr} distinct addresses in table rows."
echo "  ABSTAIN not a shelf count -- this file's censuses put non-shelf addresses in tables."
echo "  Gap 544-E: mark each row's disposition, then this becomes derivable."

exit $rc
