#!/bin/bash
# Regression test for lib/license_family.sh.  Run: ./test_license_family.sh
#
# The fixture that matters is GPL3_S13: the real section 13 of GPL-3.0.  Any classifier that
# greps the body returns AGPL-3.0 for it.  This is the defect P171 named, p206's D2 test pinned,
# and pass 77 reintroduced in a fresh instrument -- which is why the classifier now lives in one
# file with one test instead of being retyped per sweep.
#
# NOTE ON COVERAGE, and it is the point of the test: a license classifier validated only on the
# class you care about scores 100% while broken.  Pass 77 checked five AGPL repos and got 5/5,
# because AGPL -> AGPL is right by accident.  The defect is visible ONLY on GPL-3.0 input.
# So GPL-3.0 is a REQUIRED case here, not an optional one.
set -u
cd "$(dirname "$0")" && . ./license_family.sh

GPL3='                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply.'
GPL2='                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991'
AGPL3='                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007'
LGPL='                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007'
APACHE='                                 Apache License
                           Version 2.0, January 2004'
MIT='MIT License

Copyright (c) 2014 Transcordia

Permission is hereby granted, free of charge, to any person obtaining a copy'
MITNOTITLE='Copyright (c) 2019 fffnite

Permission is hereby granted, free of charge, to any person obtaining a copy'
BSD='Copyright (c) 2026 Someone

Redistribution and use in source and binary forms, with or without modification'
ECL='                        Educational Community License, Version 2.0'

fail=0; n=0
check() { # name expected actual
  n=$((n+1))
  if [ "$2" = "$3" ]; then printf 'ok   %-46s %s\n' "$1" "$3"
  else printf 'FAIL %-46s expected=%s got=%s\n' "$1" "$2" "$3"; fail=$((fail+1)); fi
}
check "GPL-3.0 with sec.13 is NOT AGPL (P171)" GPL-3.0   "$(family_of "$GPL3")"
check "GPL-2.0 predates the AGPL"              GPL-2.0   "$(family_of "$GPL2")"
check "real AGPL-3.0 by title"                 AGPL-3.0  "$(family_of "$AGPL3")"
check "LGPL is not GPL"                        LGPL      "$(family_of "$LGPL")"
check "Apache-2.0 by title"                    Apache-2.0 "$(family_of "$APACHE")"
check "MIT by title"                           MIT       "$(family_of "$MIT")"
check "MIT with no title line, by grant"       MIT       "$(family_of "$MITNOTITLE")"
check "BSD by grant line"                      BSD       "$(family_of "$BSD")"
check "ECL-2.0 before Apache (it names Apache)" ECL-2.0  "$(family_of "$ECL")"
check "empty payload is UNCLASSIFIED, not MIT" UNCLASSIFIED "$(family_of "")"
# the quantitative discriminator measured in pass 77
check "affero lines: GPL-3.0 payload"          3 "$(affero_lines "$GPL3")"
check "affero lines: GPL-2.0 payload"          0 "$(affero_lines "$GPL2")"

# DECLARATION FALLBACK (pass 77, frappe/education): a license FILE need not be a license TEXT.
# The size guard is the whole safety argument, so it gets a test on BOTH sides of itself.
DECL='License: GNU GPL V3'
check "one-line declaration is read"  "GPL-3.0 (declaracion)" "$(family_of "$DECL")"
check "declaration: MIT"              "MIT (declaracion)"     "$(family_of "License: MIT")"
check "declaration: AGPL before GPL"  "AGPL-3.0 (declaracion)" "$(family_of "License: AGPL-3.0")"
# THE GUARD: a full GPL-3.0 BODY must never reach the token match, or P171 reopens.  Padding it
# past the threshold must still yield GPL-3.0 from the TITLE, never AGPL from the sec.13 text.
check "guard holds: full GPL-3.0 body stays GPL-3.0" GPL-3.0 "$(family_of "$GPL3")"
check "guard holds: body over 400 B is not token-matched" GPL-3.0 \
      "$(family_of "$GPL3$GPL3")"
# And an unrecognisable short payload must stay UNCLASSIFIED, not guess.
check "short but unrecognisable stays UNCLASSIFIED" UNCLASSIFIED "$(family_of "see COPYRIGHT")"


# ============================================================================
# P250, pass 82 — the three families that reached the catalogue as UNCLASSIFIED,
# and the axis that matters more than any of them.
# ============================================================================

ZEROBSD='BSD Zero Clause License

Copyright (c) 2025 Someone <someone@example.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY.'
check "0BSD by title block" 0BSD "$(family_of "$ZEROBSD")"

ISCL='ISC License

Copyright (c) 2024 Someone

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.'
check "ISC is not read as 0BSD" ISC "$(family_of "$ISCL")"

CCBYSA='# Licencia Creative Commons Atribucion-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)

Este repositorio se distribuye bajo los terminos de la licencia Creative Commons
Atribucion-CompartirIgual 4.0 Internacional, https://creativecommons.org/licenses/by-sa/4.0/'
check "CC BY-SA 4.0 by title block" CC-BY-SA-4.0 "$(family_of "$CCBYSA")"

CC0='Creative Commons CC0 1.0 Universal Public Domain Dedication

The person who associated a work with this deed has dedicated the work to the
public domain by waiving all of his or her rights to the work worldwide.'
check "CC0 is not read as CC-BY" CC0-1.0 "$(family_of "$CC0")"

# ---- THE case.  Real payload shape of dssg/student-early-warning, which sat in
# ---- agents/top.md reading UNCLASSIFIED while forbidding commercial use outright.
UCHI='BY DOWNLOADING THE STUDENT EARLY WARNING PROGRAM YOU AGREE TO THE FOLLOWING TERMS OF USE:

Copyright 2018.  The University of Chicago ("Chicago"). All Rights Reserved.

Permission to use, copy, modify, and distribute this software, including all object code
and source code, and any accompanying documentation (together the "Program") for academic
research or other not-for-profit scholarly purposes which are undertaken at a non-profit or
government institution and publishing in connection therewith, without fee and without a
signed licensing agreement, is hereby granted, provided that the above copyright notice,
this paragraph and the following two paragraphs appear in all copies, modifications, and
distributions. For the avoidance of doubt, educational and not-for-profit research purposes
excludes any service or part of selling a service that uses the Program. To obtain a
commercial license for the Program, contact the Technology Commercialization and Licensing,
Polsky Center for Entrepreneurship and Innovation, University of Chicago.'
check "non-commercial payload is NAMED, never UNCLASSIFIED" NONCOMMERCIAL-NOT-OSI \
      "$(family_of "$UCHI")"
# It opens with "Permission to use, copy, modify, and distribute this software" -- one word
# from ISC/0BSD.  A permissive body match would have labelled it ISC.  That is why the
# permissive families are decided on the TITLE and this one on the RESTRICTION.
if commercial_use_ok "$UCHI"; then
  check "commercial use on the UChicago payload" "forbidden" "allowed"
else
  check "commercial use on the UChicago payload" "forbidden" "forbidden"
fi

# ---- NEGATIVE CONTROLS.  The detector must not fire on anything permissive, or every
# ---- recommendable row in this KB turns into a false alarm.  This is the half of the
# ---- test that would have caught the detector being too greedy.
for pair in "GPL3:$GPL3" ; do :; done
check_ok() {  # name, payload -> commercial use must be ALLOWED
  if commercial_use_ok "$2"; then check "commercial OK: $1" allowed allowed
  else check "commercial OK: $1" allowed forbidden; fi
}
check_ok "Apache-2.0"   "$APACHE"
check_ok "MIT"          "$MIT"
check_ok "GPL-3.0"      "$GPL3"
check_ok "AGPL-3.0"     "$AGPL3"
check_ok "0BSD"         "$ZEROBSD"
check_ok "ISC"          "$ISCL"
check_ok "CC0-1.0"      "$CC0"
check_ok "CC BY-SA 4.0" "$CCBYSA"
# And the families themselves must be untouched by the new branches.
check "Apache still Apache after P250" Apache-2.0 "$(family_of "$APACHE")"
check "AGPL still AGPL after P250"     AGPL-3.0   "$(family_of "$AGPL3")"
check "empty still UNCLASSIFIED"       UNCLASSIFIED "$(family_of "")"


# ============================================================================
# The controls that the first cut of P250 did NOT have, and that it needed.
#
# The detector shipped a body token match and reported three AGPL-3.0 repos and
# The Unlicense as commercial-use PROHIBITED. The negative controls above did not
# catch it because they used TRUNCATED fixtures -- title blocks with no section 6
# and no grant sentence. A fixture short enough to be convenient is short enough
# to miss the defect. These two carry the exact sentences that caused the error.
# ============================================================================

# Section 6 of the real GPL-3.0/AGPL-3.0 text. "noncommercially" here describes a
# CONDITION on conveying object code, not a restriction on the licensee.
AGPL_S6='                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

  Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

                       TERMS AND CONDITIONS

  6. Conveying Non-Source Forms.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.  A separable portion of the object code,
    whose source code is excluded from the Corresponding Source as a
    System Library, need not be included in conveying the object code
    work.  Such an alternative is allowed only occasionally and
    noncommercially, and only if you received the object code with such
    an offer, in accord with subsection 6b.'
check "AGPL-3.0 body with section 6 is still AGPL-3.0" AGPL-3.0 "$(family_of "$AGPL_S6")"
if commercial_use_ok "$AGPL_S6"; then
  check "AGPL sec.6 'noncommercially' is NOT a commercial-use ban" allowed allowed
else
  check "AGPL sec.6 'noncommercially' is NOT a commercial-use ban" allowed forbidden
fi

# The Unlicense. It GRANTS permission using the very token the detector matched on.
UNLIC='This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain.'
check "The Unlicense is a NAMED family, not UNCLASSIFIED" Unlicense "$(family_of "$UNLIC")"
if commercial_use_ok "$UNLIC"; then
  check "The Unlicense permits commercial use (it says so)" allowed allowed
else
  check "The Unlicense permits commercial use (it says so)" allowed forbidden
fi

# THE GATE itself: an identified OSI family is never token-matched, so no OSI payload
# can ever come back PROHIBIDO however its body is worded.
check "gate: osi_family_of is what decides whether tokens run" AGPL-3.0 \
      "$(osi_family_of "$AGPL_S6")"
# ...and the restriction detector still fires when there is NO family to gate on.
if commercial_use_ok "$UCHI"; then
  check "gate does not disarm the real restriction" forbidden allowed
else
  check "gate does not disarm the real restriction" forbidden forbidden
fi

printf '\n%d/%d\n' "$((n-fail))" "$n"
[ "$fail" = 0 ] || exit 1
