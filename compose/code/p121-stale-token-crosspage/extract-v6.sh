#!/usr/bin/env bash
# P121 ACTION O. Claim-side extractor v5 = p120 v3 + WORD-BOUNDARY ANCHORING
# + the alternation WIDENED to the spellings anchoring exposed.
#
# v4 (anchoring alone) is kept as extract-v4.sh and is NOT the recommended
# instrument: anchoring rejects `BSD` inside `0BSD` and `LGPL` inside `LGPLv3`,
# so it converts a WRONG token into a MISSING ROW. That is p118's F5 fault
# recurring one level up -- the alternation cannot express the spelling the page
# actually uses, and the boundary check then silently drops the row instead of
# mislabelling it. v5 anchors AND widens, which is the only combination that
# neither invents nor loses a claim.
#
# Lineage: p118 extract.sh v2 fixed the short SPDX spellings (F5). p120
# extract-k.sh v3 added the source-available family so a REPAIRED row stays in
# the census. Both end their alternation with BARE tokens -- MIT, AGPL, LGPL,
# GPL, BSD, PROPRIETARY -- and awk's match() has no word boundary, so `MIT`
# matches inside `commit`, `submitted`, `COMMITTED`, `MITRE`, `transmit`.
#
# That direction of error is the dangerous one for a CENSUS: a table row that
# names a repo and happens to contain the word "commit" was counted as CLAIMING
# MIT, then scored against the tree. Where the tree is in fact MIT the row
# scores AGREE and inflates the agreement rate; where it is not, it manufactures
# a defect that no human wrote.
#
# v4 validates both edges of every match against [A-Za-z0-9] and advances by ONE
# character on rejection, so a rejected prefix cannot hide a valid token behind it.
set -u

anchored_ok() {  :; }   # documented in awk below; shell stub kept for readability

for f in "$@"; do
  awk -v F="$f" '
    # 1 if the match at position s of length l in string r has non-word chars
    # (or string ends) on both sides.
    function wordok(r, s, l,   c) {
      if (s > 1) { c = substr(r, s-1, 1); if (c ~ /[A-Za-z0-9]/) return 0 }
      if (s + l <= length(r)) { c = substr(r, s+l, 1); if (c ~ /[A-Za-z0-9]/) return 0 }
      return 1
    }
    /^[ \t]*\|/ {
      line=$0
      if (line !~ /github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+/) next
      slug=""
      if (match(line, /github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+/)) {
        slug=substr(line, RSTART+11, RLENGTH-11)
        sub(/[.)]+$/, "", slug)
      }
      if (slug == "") next
      toks=""; rest=line
      while (match(rest, /AGPL-3(\.0)?|AGPLv3|LGPL-[0-9]+(\.[0-9]+)?|LGPLv3|GPL-3(\.0)?|GPLv3|GPL-2(\.0)?|GPLv2|Apache-2(\.0)?|0BSD|BSD-[234](-Clause)?|ECL-2(\.0)?|MPL-2(\.0)?|EPL-[12](\.0)?|CC-BY-SA|CC-BY-NC|CC-BY|CC0|Unlicense|Elastic[- ]?2(\.0)?|Elastic License|Fair[- ]?Code( License)?|Sustainable Use( License)?|BUSL(-1\.1)?|Business Source( License)?|SSPL|Commons Clause|PolyForm|PROPRIETARY|MIT|AGPL|LGPL|GPL|BSD/)) {
        s=RSTART; l=RLENGTH; t=substr(rest, s, l)
        if (!wordok(rest, s, l)) { rest=substr(rest, s+1); continue }   # ACTION O
        if (t ~ /^(A?GPL|LGPL)-[0-9]+$/) t = t ".0"
        if (t ~ /^(Apache|ECL|MPL|EPL)-[0-9]+$/) t = t ".0"
        if (t == "AGPLv3") t = "AGPL-3.0"
        if (t == "LGPLv3") t = "LGPL-3.0"
        if (t == "GPLv3")  t = "GPL-3.0"
        if (t == "GPLv2")  t = "GPL-2.0"
        # the SPACE spelling is deliberately NOT matched: its only occurrence in this KB is inside a QUOTATION of the ECL-2.0 preamble ("consists of the Apache 2.0 license, modified"), which is a lineage note, not a claim
        # P121 defect 3: p118/p120 JOIN with "," but test membership with " "
        # delimiters, so only the FIRST token could ever match and every later
        # repeat leaked. 49 surplus token instances across 46 rows. Delimiters
        # must match the join character.
        if (index("," toks ",", "," t ",") == 0) toks = (toks=="" ? t : toks "," t)
        rest=substr(rest, s+l)
      }
      if (toks == "") next
      printf "%s\t%d\t%s\t%s\n", F, FNR, slug, toks
    }' "$f"
done
