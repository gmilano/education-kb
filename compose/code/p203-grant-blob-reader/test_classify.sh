#!/usr/bin/env bash
# Offline regression suite for classify.sh. NO NETWORK, so it runs in any pass.
# Each case is a real body read from a real blob at p203, or a recorded regression.
set -uo pipefail
. "$(dirname "$0")/classify.sh"
pass=0; fail=0
ck() { # ck <expected> <got> <label>
  if [ "$1" = "$2" ]; then pass=$((pass+1)); else fail=$((fail+1)); echo "FAIL [$3] expected=$1 got=$2"; fi
}

# --- real bodies, p203 blob reads -------------------------------------------
ck MIT          "$(classify_grant 'MIT License

Copyright (c) 2026 Rohit Ghumare

Permission is hereby granted, free of charge, to any person obtaining a copy')" "rohitg00 MIT"
ck Apache-2.0   "$(classify_grant '                  Apache License
                       Version 2.0, January 2004')" "ADL_LRS Apache"
ck GPL-2.0      "$(classify_grant '          GNU GENERAL PUBLIC LICENSE
             Version 2, June 1991')" "lxHive GPL-2.0"
ck GPL-3.0      "$(classify_grant '### GNU GENERAL PUBLIC LICENSE

Version 3, 29 June 2007')" "Edlib GPL-3.0 markdown-headed"
ck BSD-3-Clause "$(classify_grant 'BSD 3-Clause License

Copyright (c) 2020, Andre Dietrich
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
3. Neither the name of the copyright holder nor')" "LiaScript BSD-3"
ck CC-BY-SA-4.0 "$(classify_grant 'CREATIVE COMMONS ATTRIBUTION-SHAREALIKE 4.0 INTERNATIONAL')" "SCOBot CC-BY-SA"
ck CC-BY-4.0    "$(classify_grant 'Attribution 4.0 International

=======================================================================')" "spatialaudio CC-BY"
ck CC0-1.0      "$(classify_grant 'Creative Commons Legal Code

CC0 1.0 Universal')" "Awesome-CS-OpenCourse CC0"

# --- regressions this instrument must not re-break --------------------------
# R1: CC-BY-SA must NOT collapse to CC-BY. ShareAlike is copyleft on content and
#     CC-BY is not; p202 showed the two answer "can we ship a closed adaptation"
#     in opposite directions.
ck CC-BY-SA-4.0 "$(classify_grant 'This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.')" "R1 CC-BY-SA not CC-BY"
# R2: CC0 must NOT collapse to CC-BY: no attribution duty at all.
ck CC0-1.0      "$(classify_grant 'Creative Commons Legal Code CC0 1.0 Universal  CREATIVE COMMONS CORPORATION')" "R2 CC0 not CC-BY"
# R3: AGPL must NOT be read as GPL. Different obligation over a network service.
ck AGPL-3.0     "$(classify_grant 'GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007')" "R3 AGPL not GPL"
# R4: LGPL must NOT be read as GPL (Grid2Op-class rows in sibling KBs).
ck LGPL         "$(classify_grant 'GNU LESSER GENERAL PUBLIC LICENSE Version 2.1, February 1999')" "R4 LGPL not GPL"
# R5: an unversioned GPL must be reported as unversioned, never guessed.
ck GPL-unversioned "$(classify_grant 'GNU GENERAL PUBLIC LICENSE  Everyone is permitted to copy')" "R5 no version guess"
# R6: empty body is EMPTY, never MIT-by-default.
ck EMPTY        "$(classify_grant '')" "R6 empty not defaulted"
# R7: a non-OSI 'fair code' notice must not pass as open source (leemons, p202).
ck NON-OSI-faircode "$(classify_grant 'Fair Code License v1.0')" "R7 faircode non-OSI"
# R8: an unknown body must say UNRECOGNISED rather than pick a neighbour.
ck UNRECOGNISED "$(classify_grant 'This software is governed by a bespoke agreement.')" "R8 unknown not guessed"

# --- scope_headings: the Carpentries two-scope instrument -------------------
ck 2 "$(scope_headings '---
title: "Licenses"
---
## Instructional Material
All Carpentries instructional material is made available under the CC BY license.
## Software
Except where otherwise noted, the example programs and other software provided
by The Carpentries are made available under the OSI-approved MIT license.')" "S1 two-scope detected"
ck 0 "$(scope_headings 'MIT License

Copyright (c) 2026')" "S2 single-scope is zero"
# S3: prose mentioning software must not be counted as a scope heading.
ck 0 "$(scope_headings 'This software is free software. The software is provided as is.')" "S3 prose is not a heading"

echo "----"
echo "p203 classify suite: ${pass} passed, ${fail} failed"
[ "$fail" -eq 0 ] || exit 1
