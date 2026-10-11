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

[ -z "$g" ] && { echo "UNKNOWN"; exit 0; }
n=$(printf "%s" "$g" | awk -F, "{print NF}")
if [ "$n" -gt 1 ]; then echo "MULTI-GRANT:$g"; else echo "$g"; fi
