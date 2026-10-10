#!/usr/bin/env bash
# p1026 — archive regression census.
#
# Measures which GitHub addresses exist in archive/<snapshot>/ and in NO live page.
# A reset followed by growth hides its own losses: the live corpus can be twice the
# size of the archive and still be missing a sixth of the archive's addresses.
#
# Usage:  bash census.sh [repo-root] [archive-dir]
# Output: TSV on stdout — class<TAB>slug
#         class = LOST   (in archive, in no live page, not a control)
#                 CONTROL(deliberate ABSENT probe or a non-repo URL: /topics/, .git suffix)
# Exit:   0 always; the census is a measurement, not a gate.
set -uo pipefail

ROOT="${1:-.}"
ARCHIVE="${2:-$ROOT/archive}"
EXCLUDE="${EXCLUDE:-$(dirname "$0")/excluded-controls.txt}"

slugs() {
  # owner/repo, lowercased, trailing punctuation stripped. Reads stdin.
  grep -oE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' \
    | sed 's|github\.com/||' \
    | sed 's/[.)]*$//' \
    | tr 'A-Z' 'a-z' \
    | sort -u
}

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

find "$ARCHIVE" -type f -name '*.md' -print0 2>/dev/null \
  | xargs -0 cat 2>/dev/null | slugs > "$tmp/archive.slugs"

# Live = every tracked file that is NOT under the archive dir. Code and TSVs count:
# an address cited only by an instrument is still held by this repository.
#
# SELF-REFERENCE: this instrument's own committed result lists the lost addresses,
# so leaving it in the live corpus makes the NEXT run return zero. Its outputs are
# excluded by name, not by directory, so a result copied elsewhere still counts.
find "$ROOT" -type f \( -name '*.md' -o -name '*.sh' -o -name '*.py' -o -name '*.tsv' -o -name '*.txt' \) \
     -not -path "$ARCHIVE/*" -not -path "$ROOT/.git/*" \
     -not -name 'result.*.tsv' -not -name 'held-only-in-a-worklist.*.txt' \
     -not -name 'lost-addresses.*.txt' -not -name 'excluded-controls.txt' -print0 2>/dev/null \
  | xargs -0 cat 2>/dev/null | slugs > "$tmp/live.slugs"

comm -23 "$tmp/archive.slugs" "$tmp/live.slugs" > "$tmp/lost.all"

if [ -r "$EXCLUDE" ]; then
  sort "$EXCLUDE" | grep -v '^[[:space:]]*$' > "$tmp/excl"
else
  : > "$tmp/excl"
fi

comm -23 "$tmp/lost.all" "$tmp/excl" | sed 's/^/LOST\t/'
comm -12 "$tmp/lost.all" "$tmp/excl" | sed 's/^/CONTROL\t/'

{
  printf '#\tarchive_addresses\t%s\n' "$(wc -l < "$tmp/archive.slugs" | tr -d ' ')"
  printf '#\tlive_addresses\t%s\n'    "$(wc -l < "$tmp/live.slugs" | tr -d ' ')"
  printf '#\tlost_total\t%s\n'        "$(wc -l < "$tmp/lost.all" | tr -d ' ')"
} >&2
