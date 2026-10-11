#!/usr/bin/env bash
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

[ -z "$g" ] && { echo "UNKNOWN"; exit 0; }
n=$(printf "%s" "$g" | awk -F, "{print NF}")
if [ "$n" -gt 1 ]; then echo "MULTI-GRANT:$g"; else echo "$g"; fi
