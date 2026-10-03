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

printf '\n%d/%d\n' "$((n-fail))" "$n"
[ "$fail" = 0 ] || exit 1
