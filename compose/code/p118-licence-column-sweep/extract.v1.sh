#!/usr/bin/env bash
# P118 ACTION E. Extract every (file, line, slug, licence-tokens) triple from the
# LICENCE COLUMNS of this KB's live recommendation pages.
#
# A "licence column" row is a markdown table row that carries BOTH a github slug
# AND at least one SPDX-shaped token. Prose paragraphs are excluded: p117's Gap 406
# is about the TABLE's published conclusion, and a sentence is not a column.
#
# Rows corrected by a prior pass carry TWO tokens (published | measured). Both are
# kept: the verdict layer treats the row as AGREEING if the tree matches ANY token,
# so a pass that already published a correction is not re-flagged as wrong.
set -u
for f in "$@"; do
  awk -v F="$f" '
    /^[ \t]*\|/ {
      line=$0
      if (line !~ /github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+/) next
      slug=""
      if (match(line, /github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+/)) {
        slug=substr(line, RSTART+11, RLENGTH-11)
        sub(/[.)]+$/, "", slug)
      }
      if (slug == "") next
      toks=""
      rest=line
      while (match(rest, /AGPL-3\.0|LGPL-[0-9]+\.[0-9]+|LGPL|GPL-3\.0|GPL-2\.0|Apache-2\.0|BSD-3-Clause|BSD-2-Clause|ECL-2\.0|MPL-2\.0|EPL-[0-9]+\.[0-9]+|CC-BY-SA|CC-BY-NC|CC-BY|CC0|Unlicense|MIT|BSD|GPL/)) {
        t=substr(rest, RSTART, RLENGTH)
        if (index(" " toks " ", " " t " ") == 0) toks = (toks=="" ? t : toks "," t)
        rest=substr(rest, RSTART+RLENGTH)
      }
      if (toks == "") next
      printf "%s\t%d\t%s\t%s\n", F, FNR, slug, toks
    }' "$f"
done
