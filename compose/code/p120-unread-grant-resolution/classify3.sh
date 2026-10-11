#!/usr/bin/env bash
# P120 classifier v3 = p118's classify2.sh v2.1 plus ONE new branch, added
# because `ACTION J` found a grant that v2.1 could only call UNKNOWN.
#
#  F4 UNNAMED PROPRIETARY GRANTS. v2.1 detects source-available licences by
#     NAME -- Elastic, BUSL, SSPL, Commons Clause, PolyForm. A BESPOKE licence
#     has no name to match, so it falls through to UNKNOWN, where p118's own
#     `P118-K` warns that "absence of a licence reads as permission".
#
#     Two of this KB's addresses are exactly that shape:
#       * yuanjiusheng/cloud-learning-ce commits a Chinese EULA that reserves
#         all rights, forbids commercial use without a purchased licence, and
#         forbids derivative versions for redistribution. Published here as MIT.
#       * leemonade/leemons commits a "Fair Code License" billing EUR 100 000.
#         p119 found it BY HAND; v2.1 still cannot name it.
#
#     v3 therefore matches RESTRICTION SEMANTICS, not licence names: a reserved
#     -rights assertion, a non-commercial restriction, or a fee trigger. This is
#     deliberately the LAST branch before UNKNOWN, so every named grant above
#     still wins -- a real MIT file that happens to say "all rights reserved" in
#     a copyright header is classified MIT, not proprietary.
#
#     The branch carries CJK and Latin tokens together because the one address
#     that forced it is Chinese and the one that motivated it is Spanish-authored
#     English. An English-only restriction probe is `P471`'s defect again.
#
# --- inherited from p118 classify2.sh v2.1, unchanged ---
# P118 classifier v2. Takes a licence FILE and names the grant(s) it EMBODIES.
#
# Three faults of v1, all caught before publishing, drive this rewrite:
#
#  F1 VERSION SPELLING. v1 emitted "LGPL-3" where the KB publishes "LGPL-3.0",
#     then the verdict layer called the row WRONG. Two spellings of one licence,
#     which is `Gap 408`'s defect at the token level. v2 normalises to x.0.
#
#  F2 MULTI-GRANT FILES. v1 read the FIRST meaningful line, so PrairieLearn's
#     "Portions copyright (c) 2013-2021 University of Illinois..." became MIT by
#     the grant-sentence fallback -- when the file's own prose puts the Community
#     Edition under AGPL-3.0 and MIT only on contributed portions. A file that
#     embodies two grants has no single answer, so v2 REPORTS the plurality
#     instead of picking a winner from position.
#
#  F3 ALL-CAPS ANCHOR. v1 and p117 both fought GPL-3 section 13, whose title
#     NAMES the AGPL. The embedded licence TEXT always carries an ALL-CAPS
#     heading; a cross-reference inside running prose is mixed case. Anchoring on
#     the all-caps form removes the trap structurally rather than by exclusion
#     list -- `P471`'s shape, fixed at the anchor instead of the filter.
set -u
f="$1"
[ -s "$f" ] || { echo "EMPTY"; exit 0; }
g=""
add() { case " $g " in *" $1 "*) ;; *) g="${g:+$g,}$1" ;; esac; }

gnuver() { # version from the line following the ALL-CAPS GNU heading
  awk -v pat="$1" 'index($0,pat){found=NR} found && NR>=found && NR<=found+3 {
    if (match($0,/Version [0-9]+/)) { v=substr($0,RSTART+8,RLENGTH-8); print v; exit } }' "$f"
}
if grep -q 'GNU AFFERO GENERAL PUBLIC LICENSE' "$f"; then
  v=$(gnuver 'GNU AFFERO GENERAL PUBLIC LICENSE'); add "AGPL-${v:-3}.0"
fi
if grep -q 'GNU LESSER GENERAL PUBLIC LICENSE' "$f"; then
  v=$(gnuver 'GNU LESSER GENERAL PUBLIC LICENSE'); add "LGPL-${v:-3}.0"
fi
# Plain GPL: the all-caps heading, excluding the AFFERO/LESSER variants of it.
if grep -q 'GNU GENERAL PUBLIC LICENSE' "$f"; then
  v=$(gnuver 'GNU GENERAL PUBLIC LICENSE'); add "GPL-${v:-3}.0"
fi
grep -qi 'Educational Community License' "$f" && add "ECL-2.0"
if grep -qiE '^[[:space:]]*Apache License' "$f" || grep -q 'TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION' "$f"; then
  add "Apache-2.0"
fi
grep -qi 'Mozilla Public License' "$f" && add "MPL-2.0"
grep -qi 'Eclipse Public License' "$f" && add "EPL-2.0"
grep -q 'Permission is hereby granted, free of charge' "$f" && add "MIT"
grep -q 'Redistribution and use in source and binary forms' "$f" && add "BSD"
grep -qi 'Creative Commons Attribution' "$f" && add "CC-BY"
grep -qi 'This is free and unencumbered software released into the public domain' "$f" && add "Unlicense"
grep -qi 'Permission to use, copy, modify, and/or distribute this software' "$f" && add "ISC"

# --- v2.1, added after the first full census returned 18 UNKNOWN and the bucket
# --- turned out to be four distinct, nameable classes rather than one failure.
#
# (a) NON-ENGLISH GRANTS. The classifier was English-only, and the addresses it
#     could not read were Brazilian and Chinese -- a REGIONAL blind spot in a KB
#     whose whole brief is to place findings by region. portabilis/i-diario and
#     portabilis/pre-matricula-digital commit the AGPL-3 in Portuguese
#     ("LICENCA PUBLICA GERAL AFFERO GNU"). `P471` recorded the mirror image of
#     this defect: a gap extractor that was Spanish-only.
# (b) CC0 reads "Creative Commons Legal Code" + "CC0 1.0 Universal" and never the
#     word "Attribution", so the CC branch missed public-domain dedications.
# (c) SOURCE-AVAILABLE licences are not open source and must never fall through to
#     UNKNOWN, where a reader may mistake silence for permission. Elastic License
#     2.0, BUSL, SSPL, Commons Clause and PolyForm restrict USE, not just
#     distribution: a client cannot ship a derivative at all.
# (d) A LICENCE BY REFERENCE is a pointer, not a grant. frappe/education's
#     license.txt is the single line "License: GNU GPL V3" with no licence body,
#     and R packages commit a 45-byte YEAR/COPYRIGHT HOLDER field stub whose
#     actual licence is named in DESCRIPTION. Both are reported as such rather
#     than resolved, because resolving a pointer is a different measurement.
grep -qiE 'Elastic License' "$f" && add "ElasticLicense-2.0-NOT-OSS"
grep -qiE 'Business Source License' "$f" && add "BUSL-1.1-NOT-OSS"
grep -qiE 'Server Side Public License' "$f" && add "SSPL-NOT-OSS"
grep -qiE 'Commons Clause' "$f" && add "CommonsClause-NOT-OSS"
grep -qiE 'PolyForm' "$f" && add "PolyForm-NOT-OSS"
# CC0 is a dedication, not an attribution licence: if the file is CC0 it is CC0
# and nothing else, so the generic CC branch must not also fire.
if grep -qiE 'CC0 1\.0 Universal' "$f"; then add "CC0-1.0"
elif grep -qiE 'Creative Commons Legal Code' "$f"; then add "CC"; fi
# Portuguese / Spanish renderings of the GNU family. Anchored on the ASCII tail
# of the title ("GERAL AFFERO GNU"), because the accented head is multi-BYTE and
# a `.` in a POSIX bracket expression matches one byte, not one character -- so
# `LICEN.A` does not match `LICENÇA`. That near-miss is `P471`'s shape again:
# a probe written in the wrong alphabet for the data it has to read.
grep -qiE 'GERAL AFFERO GNU|GENERAL AFFERO GNU' "$f" && add "AGPL-3.0"
if grep -qiE 'P.?.?BLICA GERAL GNU|P.?.?BLICA GENERAL GNU' "$f" && ! grep -qi 'AFFERO' "$f"; then add "GPL-3.0"; fi
# A pointer with no body. Checked LAST so a real grant always wins.
if [ -z "$g" ]; then
  if [ "$(wc -c < "$f")" -lt 220 ] && grep -qiE '^(YEAR|COPYRIGHT HOLDER)' "$f"; then
    echo "GRANT-IN-MANIFEST"; exit 0
  fi
  ref=$(grep -ioE '(GNU )?(A?GPL|LGPL|MIT|Apache|BSD)[ -]*(v?[0-9](\.[0-9])?)?' "$f" | head -1)
  if [ -n "$ref" ] && [ "$(wc -l < "$f")" -lt 6 ]; then
    echo "GRANT-BY-REFERENCE:$(printf '%s' "$ref" | tr -s ' ' ' ')"; exit 0
  fi
fi

# --- v3, F4: unnamed proprietary / source-available grants. LAST before UNKNOWN.
if [ -z "$g" ]; then
  restrict=0
  # reserved-rights assertion
  grep -qiE 'All rights reserved' "$f" && restrict=$((restrict+1))
  grep -qF '保留所有权利' "$f" && restrict=$((restrict+1))
  # non-commercial restriction
  grep -qiE 'non-?commercial purposes|not (be )?(used )?for commercial' "$f" && restrict=$((restrict+1))
  grep -qF '非商业用途' "$f" && restrict=$((restrict+1))
  grep -qF '商业用途' "$f" && restrict=$((restrict+1))
  grep -qF '商业授权' "$f" && restrict=$((restrict+1))
  # fee / royalty trigger
  grep -qiE 'ONE HUNDRED THOUSAND|royalt(y|ies)|licen[cs]e fee' "$f" && restrict=$((restrict+1))
  # self-declared fair-code family
  grep -qiE 'Fair Code|Sustainable Use License' "$f" && restrict=$((restrict+1))
  if [ "$restrict" -ge 2 ]; then
    echo "PROPRIETARY-UNNAMED-NOT-OSS:restriction-signals=$restrict"; exit 0
  fi
fi

[ -z "$g" ] && { echo "UNKNOWN"; exit 0; }
n=$(printf "%s" "$g" | awk -F, "{print NF}")
if [ "$n" -gt 1 ]; then echo "MULTI-GRANT:$g"; else echo "$g"; fi
