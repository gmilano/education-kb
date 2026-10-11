#!/usr/bin/env bash
# P120 ACTION K = p118 extract.sh with the CLAIM-side alternation extended.
#
# p118 v2 fixed the SHORT SPDX spellings (F5). ACTION K names the next gap: the
# alternation can only express OSI licences, so once a pass REPAIRS a row to
# "Fair Code License v1.0" or "Elastic-2.0" that row stops matching and silently
# LEAVES THE CENSUS. A repaired row that vanishes is worse than a wrong one: the
# page is right and the instrument can no longer see it.
#
# v3 adds the source-available family to the claim side, and the NOT-OSS marker
# this KB publishes with them, so a repaired row stays measurable.
#
# --- p118 ACTION E, otherwise unchanged ---
# P118 ACTION E. Extract every (file, line, slug, licence-tokens) triple from the
# LICENCE COLUMNS of this KB's live recommendation pages.
#
# A "licence column" row is a markdown table row that carries BOTH a github slug
# AND at least one SPDX-shaped token. Prose paragraphs are excluded: p117's Gap 406
# is about the TABLE's published conclusion, and a sentence is not a column.
#
# F5, the fault that nearly produced a false headline: v1's alternation had no
# entry for the SHORT spellings this KB actually uses -- `AGPL-3`, `GPL-3`,
# `BSD-3`, `Apache-2`. On `AGPL-3` the leftmost match that DID exist was the
# bare `GPL` inside it, so every page row correctly reading AGPL-3 was scored
# as claiming GPL and then called WRONG against an AGPL-3.0 tree. v2 matches the
# short forms and normalises them to x.0 at extraction.
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
      while (match(rest, /AGPL-3(\.0)?|LGPL-[0-9]+(\.[0-9]+)?|GPL-3(\.0)?|GPL-2(\.0)?|Apache-2(\.0)?|BSD-[234](-Clause)?|ECL-2(\.0)?|MPL-2(\.0)?|EPL-[12](\.0)?|CC-BY-SA|CC-BY-NC|CC-BY|CC0|Unlicense|Elastic[- ]?2(\.0)?|Elastic License|Fair[- ]?Code( License)?|Sustainable Use( License)?|BUSL(-1\.1)?|Business Source( License)?|SSPL|Commons Clause|PolyForm|PROPRIETARY|MIT|AGPL|LGPL|GPL|BSD/)) {
        t=substr(rest, RSTART, RLENGTH)
        if (t ~ /^(A?GPL|LGPL)-[0-9]+$/) t = t ".0"
        if (t ~ /^(Apache|ECL|MPL|EPL)-[0-9]+$/) t = t ".0"
        if (index(" " toks " ", " " t " ") == 0) toks = (toks=="" ? t : toks "," t)
        rest=substr(rest, RSTART+RLENGTH)
      }
      if (toks == "") next
      printf "%s\t%d\t%s\t%s\n", F, FNR, slug, toks
    }' "$f"
done
