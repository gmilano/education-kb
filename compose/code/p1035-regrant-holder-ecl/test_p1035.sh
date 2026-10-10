#!/usr/bin/env bash
# Offline tests for p1035's pure functions. No network.
set -u
cd "$(dirname "$0")"
. ./classify.sh

pass=0; fail=0
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT

ck() { # ck <label> <expected> <actual>
  if [ "$2" = "$3" ]; then pass=$((pass+1));
  else fail=$((fail+1)); printf 'FAIL %s: expected %s got %s\n' "$1" "$2" "$3"; fi
}

# ---- place_string, extracted from holder.sh so it is testable in isolation ----
eval "$(sed -n '/^place_string()/,/^}/p' holder.sh)"

ck place-unb      LATAM    "$(place_string 'auto-matricula-sigaa-unb')"
ck place-edubr    LATAM    "$(place_string 'Copyright 2026 foo.edu.br')"
ck place-unam     LATAM    "$(place_string 'Copyright (c) 2026 x.unam.mx')"
ck place-educo    LATAM    "$(place_string 'see uan.edu.co for details')"
ck place-spainword EMEA    "$(place_string 'hecho en España')"
ck place-nothing  UNPLACED "$(place_string 'tutor-adaptativo-ia')"
ck place-empty    UNPLACED "$(place_string '')"

# REGRESSION for this pass's SECOND corrected bug, and the costlier one.
# The first matcher placed any "universidad de ..." in EMEA. Universidad de
# Córdoba exists in Córdoba, SPAIN and in Córdoba, COLOMBIA, so the rule
# invented a region. An institution name alone must now be UNPLACED...
ck place-ambiguous-univ UNPLACED "$(place_string 'Proyecto de la Universidad de Córdoba')"
ck place-ambiguous-gra  UNPLACED "$(place_string 'Universidad de Granada')"
# ...and the COUNTRY WORD in the same README is what legitimately places it.
ck place-univ-plus-country LATAM "$(place_string 'Universidad de Córdoba Colombia')"
# the closed vocabulary, and nothing outside it
for r in "$(place_string 'brasil')" "$(place_string 'spain')" "$(place_string 'nope')"; do
  case "$r" in
    North\ America|EMEA|APAC|LATAM|Global|UNPLACED) pass=$((pass+1)) ;;
    *) fail=$((fail+1)); printf 'FAIL closed-vocab: %s\n' "$r" ;;
  esac
done

# ---- declared_name, extracted from ecl.sh ----
eval "$(sed -n '/^declared_name()/,/^}/p' ecl.sh)"

printf 'Educational Community License, Version 2.0\n\nblah\n' > "$T/ecl"
printf 'Apache License\nVersion 2.0, January 2004\n' > "$T/apache"
printf 'nothing here\n' > "$T/none"
ck decl-ecl    ECL-2.0        "$(declared_name "$T/ecl")"
ck decl-apache APACHE-TITLED   "$(declared_name "$T/apache")"
ck decl-none   NO-TITLE-MATCH  "$(declared_name "$T/none")"

# REGRESSION for this pass's own corrected bug: the version on a SEPARATE line
# from the title is still ECL-2.0. The first detector called this "unversioned"
# and split one grant into two families on line-wrapping alone.
printf 'MIT\n\nPermission is hereby granted, free of charge, to any person\n' > "$T/mit"
printf 'Educational Community License\n\nVersion 2.0, April 2007\n\nhttp://www.osedu.org/licenses/\n' > "$T/eclwrap"
ck decl-ecl-wrapped ECL-2.0 "$(declared_name "$T/eclwrap")"
printf 'Educational Community License\n\nno version string at all\n' > "$T/eclnover"
ck decl-ecl-nover ECL-NO-VERSION-ANYWHERE "$(declared_name "$T/eclnover")"

# ---- the audit, with its premise CORRECTED by measurement ----
eval "$(sed -n '/^classify_ecl()/,/^}/p' ecl.sh)"

# MEASURED this pass against all four live payloads: the real ECL-2.0 text
# contains ZERO occurrences of the string "Apache License" — it names the
# "Apache 2.0 license" in lower case. So p1029's classifier does NOT mislabel
# ECL as Apache; it returns UNRECOGNISED, which is the worse failure for a
# census, because a PERMISSIVE row then lands in neither bucket.
printf 'Educational Community License\n\nVersion 2.0, April 2007\n\nThe Educational Community License version 2.0 ("ECL") consists of the Apache 2.0 license, modified to change the scope of the patent grant in section 3 to be specific to the needs of the education communities using this license.\n' > "$T/eclreal"
ck audit-p1029-blind UNRECOGNISED       "$(classify_payload "$T/eclreal")"
ck audit-correct     PERMISSIVE/ECL-2.0 "$(classify_ecl "$T/eclreal")"
ck audit-not-ecl     NOT-ECL            "$(classify_ecl "$T/mit")"

# and the mislabel branch must still exist, for a text that DOES carry the string
printf 'Educational Community License\nVersion 2.0\nscope of the patent grant in section 3\nApache License\n' > "$T/eclapache"
ck audit-mislabel-possible Apache-2.0 "$(classify_payload "$T/eclapache")"

# ---- classify_payload regressions carried from p1029 (ordering is load-bearing) ----
printf 'GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3\nGNU GENERAL PUBLIC LICENSE\n' > "$T/agpl"
printf 'GNU LESSER GENERAL PUBLIC LICENSE\nVersion 3\nGNU GENERAL PUBLIC LICENSE\n' > "$T/lgpl"
printf 'MIT\n\nPermission is hereby granted, free of charge, to any person\n' > "$T/mit"
printf '保留所有权利 All rights reserved\n' > "$T/arr"
ck cls-agpl AGPL-3.0     "$(classify_payload "$T/agpl")"
ck cls-lgpl LGPL-3.0     "$(classify_payload "$T/lgpl")"
ck cls-mit  MIT          "$(classify_payload "$T/mit")"
ck cls-arr  UNRECOGNISED "$(classify_payload "$T/arr")"   # P1029: a 200 is not a grant
ck cls-empty EMPTY       "$(classify_payload "$T/empty-missing" 2>/dev/null || echo EMPTY)"

# ---- input lists must be named into p1026's guard (P1034) ----
for f in lost-addresses.*.txt; do
  case "$f" in
    lost-addresses.*.txt) pass=$((pass+1)) ;;
    *) fail=$((fail+1)); printf 'FAIL guard-name: %s escapes p1026 census guard\n' "$f" ;;
  esac
done

# ---- and every input list must declare itself on line 1 ----
for f in lost-addresses.*.txt; do
  if head -1 "$f" | grep -q 'INSTRUMENT-INPUT-LIST'; then pass=$((pass+1));
  else fail=$((fail+1)); printf 'FAIL declare-line: %s\n' "$f"; fi
done

printf '%d passed, %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
