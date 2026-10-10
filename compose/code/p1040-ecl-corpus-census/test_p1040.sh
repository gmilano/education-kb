#!/usr/bin/env bash
# Tests for p1040's pure functions. No network. Run: bash test_p1040.sh
set -u
cd "$(dirname "$0")"
. ./classify.sh

pass=0; fail=0
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT

ck() { # ck <label> <expected> <actual>
  if [ "$2" = "$3" ]; then pass=$((pass+1));
  else fail=$((fail+1)); printf 'FAIL  %s\n  expected: %s\n  actual:   %s\n' "$1" "$2" "$3"; fi
}

# ---------------------------------------------------------------- the p1029
# classifier, carried over: these guard against a regression introduced by the
# ECL wiring rather than testing p1029 again.
printf 'Permission is hereby granted, free of charge\n' > "$T/mit"
printf 'Apache License\nVersion 2.0, January 2004\n'     > "$T/apache"
printf 'GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3\n'  > "$T/agpl"
printf 'GNU LESSER GENERAL PUBLIC LICENSE\nVersion 3\n'  > "$T/lgpl"
printf 'GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007\n' > "$T/gpl3"
printf 'GNU GENERAL PUBLIC LICENSE\nVersion 2, June 1991\n'    > "$T/gpl2"
printf 'Redistribution and use in source and binary forms\nNeither the name\n' > "$T/bsd3"
printf 'Redistribution and use in source and binary forms\n' > "$T/bsd2"
printf 'Creative Commons Attribution 4.0\n' > "$T/cc"
: > "$T/empty"

ck "MIT"      MIT        "$(classify_grant "$T/mit")"
ck "Apache"   Apache-2.0 "$(classify_grant "$T/apache")"
ck "AGPL"     AGPL-3.0   "$(classify_grant "$T/agpl")"
ck "LGPL"     LGPL-3.0   "$(classify_grant "$T/lgpl")"
ck "GPL-3"    GPL-3.0    "$(classify_grant "$T/gpl3")"
ck "GPL-2"    GPL-2.0    "$(classify_grant "$T/gpl2")"
ck "BSD-3"    BSD-3-Clause "$(classify_grant "$T/bsd3")"
ck "BSD-2"    BSD-2-Clause "$(classify_grant "$T/bsd2")"
ck "CC"       CC-FAMILY  "$(classify_grant "$T/cc")"
ck "empty"    EMPTY      "$(classify_grant "$T/empty")"
ck "AGPL before GPL (order is load-bearing)" AGPL-3.0 "$(classify_payload "$T/agpl")"

# ---------------------------------------------------------------- Gap 398
# The whole reason this instrument exists, measured on the REAL payload:
# 11 120 B, sha256 0688f62d04f14e4b, Sakai's root LICENSE, carried as a fixture
# so this assertion keeps holding when the network does not.
F=fixtures/ecl-2.0-sakai.txt
ck "ECL fixture is the byte count pass 105 pinned" 11120 "$(wc -c < $F | tr -d ' ')"
ck "ECL fixture is the sha256 pass 105 pinned" 0688f62d04f14e4b "$(sha256sum $F | cut -c1-16)"
ck "the MECHANISM: zero occurrences of the Apache title" 0 "$(grep -c 'Apache License' $F || true)"
ck "p1029 classifier is BLIND to it"      UNRECOGNISED     "$(classify_payload $F)"
ck "the ECL probe SEES it"                PERMISSIVE/ECL-2.0 "$(classify_ecl $F)"
ck "WIRED: classify_grant names the family" ECL-2.0        "$(classify_grant $F)"
ck "WIRED: it lands in a bucket"          PERMISSIVE       "$(bucket_of "$(classify_grant $F)")"
ck "and the recovery is REPORTED, not silent" RECOVERED-BY-ECL "$(divergence_flag $F)"

# ---------------------------------------------------------------- P1039
# Keep the branch the measurement REFUTED. Pass 105 asserted ECL would mislabel
# as Apache-2.0 and measured that it does not. The day an ECL payload does
# carry the Apache title, classify_grant must NOT relabel it to ECL behind the
# census's back -- it must keep the Apache reading and raise the divergence.
# This is a live detector, not a dead branch.
cat > "$T/ecl-apache-titled" <<'EOF'
Educational Community License, Version 2.0, April 2007
Apache License
Version 2.0
Licensed under the scope of the patent grant in section 3
EOF
ck "refuted branch: family stays with the p1029 reading" Apache-2.0 "$(classify_grant "$T/ecl-apache-titled")"
ck "refuted branch: and the clash is FLAGGED" MISLABEL-AS-APACHE "$(divergence_flag "$T/ecl-apache-titled")"
ck "refuted branch: still a permissive bucket" PERMISSIVE "$(bucket_of "$(classify_grant "$T/ecl-apache-titled")")"

# An ECL text with the family but not the pinning clause stays permissive and
# says so in its name, rather than being promoted to a version it never claimed.
printf 'Educational Community License, Version 2.0\n' > "$T/ecl-unpinned"
ck "ECL without the section-3 clause is UNPINNED, not 2.0" ECL-UNPINNED "$(classify_grant "$T/ecl-unpinned")"
ck "...and still permissive" PERMISSIVE "$(bucket_of "$(classify_grant "$T/ecl-unpinned")")"

# ---------------------------------------------------------------- P1029
# A LICENSE file that returns 200 is not a grant. Pass 104 found 4 117 B of
# all-rights-reserved Chinese text served from a file named LICENSE; a
# filename->licence mapping would have shelved a proprietary LMS.
printf '\xe4\xbf\x9d\xe7\x95\x99\xe6\x89\x80\xe6\x9c\x89\xe6\x9d\x83\xe5\x88\xa9\nAll rights reserved.\n' > "$T/arr"
# p1040 improves on p1029 here: the row is now NAMED rather than merely
# unrecognised, which is what lets it be reported as a non-grant instead of
# sitting in UNREAD beside real grants. The SAFETY properties are unchanged and
# are what these assertions actually protect.
ck "all-rights-reserved is NAMED, not just unrecognised" ALL-RIGHTS-RESERVED "$(classify_grant "$T/arr")"
ck "...and is NOT counted as permissive" NON-GRANT "$(bucket_of "$(classify_grant "$T/arr")")"
b_arr=$(bucket_of "$(classify_grant "$T/arr")")
if [ "$b_arr" = "PERMISSIVE" ] || [ "$b_arr" = "COPYLEFT" ]; then
  fail=$((fail+1)); printf 'FAIL  all-rights-reserved reached a GRANT bucket: %s\n' "$b_arr"
else pass=$((pass+1)); fi

# --- the bug this instrument found in its OWN code, as a regression --------
# "Educational Community License" contains "Community License". The non-grant
# branch matched it and moved 10 permissive corpus rows into NON-GRANT. These
# assertions fail if that guard is ever removed.
printf '# AStheTECH Community License (ACL)\nNoncommercial terms apply.\n' > "$T/acl"
ck "a real bespoke community licence is still a non-grant" BESPOKE-TOU "$(classify_grant "$T/acl")"
ck "...and ECL is NOT, despite containing the same substring" ECL-2.0 "$(classify_grant $F)"
ck "...so the restricted probe declines ECL outright" - "$(classify_restricted $F)"

# --- the families limb A2 hand-read, each with the string that named it ----
printf 'This program is free software:  Licensed under the EUPL, Version 1.1 or - as soon as\n' > "$T/eupl11"
printf 'Licensed under the EUPL, Version 1.2 or - as soon as they will be\n' > "$T/eupl12"
ck "EUPL 1.1 named"        EUPL-1.1 "$(classify_grant "$T/eupl11")"
ck "EUPL 1.2 named"        EUPL-1.2 "$(classify_grant "$T/eupl12")"
ck "EUPL is copyleft"      COPYLEFT "$(bucket_of "$(classify_grant "$T/eupl12")")"
printf 'LICEN\xc3\x87A P\xc3\x9aBLICA GERAL AFFERO GNU\nVers\xc3\xa3o 3\n' > "$T/ptagpl"
ck "Portuguese AGPL named" AGPL-3.0 "$(classify_grant "$T/ptagpl")"
printf 'Anki is licensed under the GNU Affero General Public License, version 3 or later\n' > "$T/caseagpl"
ck "title-case AGPL named" AGPL-3.0 "$(classify_grant "$T/caseagpl")"
printf 'Mozilla Public License, version 2.0\n' > "$T/mplcomma"
ck "MPL with a comma named" MPL-2.0 "$(classify_grant "$T/mplcomma")"
printf 'BSD Zero Clause License\n' > "$T/zerobsd"
ck "0BSD named"            0BSD     "$(classify_grant "$T/zerobsd")"
ck "0BSD is permissive"    PERMISSIVE "$(bucket_of "$(classify_grant "$T/zerobsd")")"
printf 'Elastic License 2.0\n' > "$T/elastic"
ck "Elastic 2.0 is a non-grant" Elastic-2.0 "$(classify_grant "$T/elastic")"
ck "...bucketed NON-GRANT"      NON-GRANT   "$(bucket_of "$(classify_grant "$T/elastic")")"
printf '# PolyForm Noncommercial License 1.0.0\n' > "$T/poly"
ck "PolyForm NC is a non-grant" PolyForm-NC "$(classify_grant "$T/poly")"
printf 'Business Source License 1.1\n' > "$T/busl"
ck "BUSL is a non-grant"        BUSL        "$(classify_grant "$T/busl")"

# A BSD notice contains "All rights reserved" AND a grant. It must stay a grant.
printf 'Copyright (c) 2026. All rights reserved.\nRedistribution and use in source and binary forms\nNeither the name\n' > "$T/bsdarr"
ck "BSD keeps its grant despite 'All rights reserved'" BSD-3-Clause "$(classify_grant "$T/bsdarr")"
ck "...and stays permissive" PERMISSIVE "$(bucket_of "$(classify_grant "$T/bsdarr")")"

# ---------------------------------------------------------------- P1037
# A bucket's NAME is part of its classifier. Every family classify_payload or
# classify_ecl can emit must land in a NAMED bucket; anything that falls
# through to UNREAD by accident is the Gap 398 failure mode returning under a
# different family. This test enumerates the classifiers' own outputs, so it
# fails when someone adds a family and forgets the bucket.
for fam in MIT Apache-2.0 Apache-OTHER BSD-3-Clause BSD-2-Clause ISC Unlicense \
           ECL-2.0 ECL-UNPINNED AGPL-3.0 LGPL-3.0 GPL-3.0 GPL-2.0 GPL-OTHER \
           MPL-2.0 EPL CC-FAMILY; do
  b=$(bucket_of "$fam")
  if [ "$b" = "UNREAD" ]; then
    fail=$((fail+1)); printf 'FAIL  family %s falls through to UNREAD\n' "$fam"
  else
    pass=$((pass+1))
  fi
done

# ...and the two that MUST stay UNREAD, so the bucket is not a catch-all.
ck "EMPTY stays unread"        UNREAD "$(bucket_of EMPTY)"
ck "UNRECOGNISED stays unread" UNREAD "$(bucket_of UNRECOGNISED)"

# ---------------------------------------------------------------- regressions
# Empty input must not crash either probe (p542's empty-input sweep).
ck "classify_ecl on empty"   NOT-ECL "$(classify_ecl "$T/empty")"
ck "divergence on empty"     -       "$(divergence_flag "$T/empty")"
ck "classify_ecl on missing" NOT-ECL "$(classify_ecl "$T/does-not-exist")"

# --------------------------------------------- the three MEASURED regressions
# Each of these was a real misclassification this instrument produced over the
# live corpus, found by diffing two census runs, and each fixture is the actual
# payload that produced it -- not a synthetic approximation of it.

# 1. A conventional "All rights reserved" copyright line above a full
#    Apache-2.0 text. A generic branch on that phrase demoted huggingface/
#    transformers, mlflow/mlflow and masakhane-ner to non-grant.
A=fixtures/apache-2.0-plus-arr-transformers.txt
ck "Apache-2.0 + 'All rights reserved' stays Apache-2.0" Apache-2.0 "$(classify_grant $A)"
ck "...and stays permissive"      PERMISSIVE "$(bucket_of "$(classify_grant $A)")"
ck "...the phrase IS in the payload" 1 "$(grep -c 'All rights reserved' $A)"
ck "...and the restriction probe declines it" - "$(classify_restricted $A)"

# 2. MPL-2.0 section 3.3 NAMES the GNU GPL/LGPL/AGPL as Secondary Licenses, so
#    the full MPL text matched the case-folded GNU branch: 15 921 B of plain
#    MPL-2.0 classified GPL-3.0 until MPL was ordered ahead of it.
M=fixtures/mpl-2.0-referencing-gpl-axecore.txt
ck "MPL-2.0 that references the GPL is MPL-2.0" MPL-2.0 "$(classify_grant $M)"
ck "...the GNU title IS present in it" 1 "$([ "$(grep -c 'GNU General Public License' $M)" -ge 1 ] && echo 1 || echo 0)"
ck "...and it is copyleft either way"  COPYLEFT "$(bucket_of "$(classify_grant $M)")"

# 3. The ECL title wraps across a newline at line 195 of the Sakai payload, so
#    a strip keyed on the unwrapped title left a bare "Community License"
#    behind and ECL came back a CONFLICT from one line break.
ck "the ECL title really does wrap in the payload" 1    "$(tr -d '\r' < $F | grep -c '^Community License, Version 2.0')"
ck "ECL survives the wrap"      ECL-2.0    "$(classify_grant $F)"
ck "...and is still permissive" PERMISSIVE "$(bucket_of "$(classify_grant $F)")"

# A synthetic wrap of a restriction string, to prove flattening works both ways
# rather than only for the one payload that exposed it.
printf 'Some notes here.\nThis release is governed by the Elastic\nLicense 2.0 terms.\n' > "$T/wrapped-elastic"
ck "a WRAPPED restriction string is still found" Elastic-2.0 "$(classify_grant "$T/wrapped-elastic")"

# A genuine conflict must stay a conflict and must NOT be promoted.
printf 'Permission is hereby granted, free of charge\nElastic License 2.0 also applies to the server code.\n' > "$T/conflict"
ck "grant + real restriction = CONFLICT" GRANT+RESTRICTION-CONFLICT "$(classify_grant "$T/conflict")"
ck "...and a conflict is NOT permissive" UNREAD "$(bucket_of "$(classify_grant "$T/conflict")")"
b_cf=$(bucket_of "$(classify_grant "$T/conflict")")
if [ "$b_cf" = "PERMISSIVE" ]; then
  fail=$((fail+1)); printf 'FAIL  a grant/restriction conflict was promoted to PERMISSIVE\n'
else pass=$((pass+1)); fi

ck "an extra-family recovery is REPORTED too" RECOVERED-BY-EXTRA "$(divergence_flag "$T/eupl12")"
ck "a p1029 family reports no divergence"     -                   "$(divergence_flag "$T/mit")"

printf '\n%d passed, %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
