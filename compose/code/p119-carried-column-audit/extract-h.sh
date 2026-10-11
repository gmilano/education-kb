#!/usr/bin/env bash
# p119 ACTION H. p118's extract.sh, plus the one fix p118 pre-registered as F7:
# a cell that NAMES a licence in order to RETRACT it is not claiming it.
#
# This KB's retraction grammar, as actually written on the pages:
#     | ... | GPL-3.0 (WARN) **was MIT** |      <- claims GPL-3.0, retracts MIT
#     | ... | AGPL-3.0, p117 said GPL-3  |      <- claims AGPL-3.0, retracts GPL-3
# So within each CELL, everything from the first retraction marker onward is
# commentary about a SUPERSEDED value. Tokens there are dropped; tokens before
# the marker are kept. The row still yields its real claim, which is why this
# is narrower than dropping the whole row.
#
# Markers, deliberately conservative: the warning sign, "was", "said",
# "published as", "carried as", "corrected". Anything else stays a claim.
set -u
for f in "$@"; do
  awk -v F="$f" '
    /^[ \t]*\|/ {
      line=$0
      if (line !~ /github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+/) next
      slug=""
      if (match(line, /github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+/)) {
        slug=substr(line, RSTART+11, RLENGTH-11); sub(/[.)]+$/, "", slug)
      }
      if (slug == "") next

      # ---- ACTION H: per-cell retraction truncation -------------------------
      n = split(line, cells, "|")
      kept = ""
      for (i = 1; i <= n; i++) {
        c = cells[i]
        # find the EARLIEST retraction marker in this cell and cut there
        cut = length(c) + 1
        split("\342\232\240|[Ww]as |[Ss]aid |published as|carried as|corrected", mk, "|")
        for (j = 1; j <= 6; j++) {
          if (mk[j] == "") continue
          if (match(c, mk[j]) && RSTART < cut) cut = RSTART
        }
        kept = kept " " substr(c, 1, cut - 1)
      }
      rest = kept
      # ----------------------------------------------------------------------

      toks=""
      while (match(rest, /AGPL-3(\.0)?|LGPL-[0-9]+(\.[0-9]+)?|GPL-3(\.0)?|GPL-2(\.0)?|Apache-2(\.0)?|BSD-[234](-Clause)?|ECL-2(\.0)?|MPL-2(\.0)?|EPL-[12](\.0)?|CC-BY-SA|CC-BY-NC|CC-BY|CC0|Unlicense|MIT|AGPL|LGPL|GPL|BSD/)) {
        t=substr(rest, RSTART, RLENGTH)
        if (t ~ /^(A?GPL|LGPL)-[0-9]+$/) t = t ".0"
        if (t ~ /^(Apache|ECL|MPL|EPL)-[0-9]+$/) t = t ".0"
        if (index(" " toks " ", " " t " ") == 0) toks = (toks=="" ? t : toks "," t)
        rest=substr(rest, RSTART+RLENGTH)
      }
      if (toks == "") next
      printf "%s\t%d\t%s\t%s\n", F, FNR, slug, toks
    }
  ' "$f"
done
