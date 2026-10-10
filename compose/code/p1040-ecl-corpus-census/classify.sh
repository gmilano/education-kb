#!/usr/bin/env bash
# Pure functions for p1040. No network, no filesystem outside the paths given.
# Sourced by census.sh / holder.sh / newaddr.sh and exercised by test_p1040.sh.
#
# WHY THIS FILE EXISTS: p1029's classify_payload returns UNRECOGNISED for every
# ECL-2.0 payload, because the real ECL text names the "Apache 2.0 license" in
# lower case and never contains the string "Apache License" that the Apache
# branch keys on. Pass 105 measured that (Gap 398), wrote the remedy as
# classify_ecl in p1035/ecl.sh, and did NOT wire it into the instrument the next
# census would run. This file is that wiring, and it is the whole point of the
# limb: a remedy that lives beside the instrument is not a remedy.

# --- the p1029 classifier, carried over UNCHANGED ---------------------------
# Order is load-bearing: AFFERO and LESSER must be tested before plain GPL,
# because both contain the string "GNU GENERAL PUBLIC LICENSE" by reference.
classify_payload() {
  local f="$1"
  [ -s "$f" ] || { echo "EMPTY"; return 0; }
  local t
  t=$(tr -d '\r' < "$f")

  case "$t" in
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*) echo "AGPL-3.0"; return 0 ;;
    *"GNU LESSER GENERAL PUBLIC LICENSE"*) echo "LGPL-3.0"; return 0 ;;
  esac
  case "$t" in
    *"Apache License"*)
      case "$t" in *"Version 2.0"*) echo "Apache-2.0"; return 0 ;; esac
      echo "Apache-OTHER"; return 0 ;;
  esac
  case "$t" in
    *"GNU GENERAL PUBLIC LICENSE"*)
      case "$t" in
        *"Version 3"*) echo "GPL-3.0"; return 0 ;;
        *"Version 2"*) echo "GPL-2.0"; return 0 ;;
      esac
      echo "GPL-OTHER"; return 0 ;;
  esac
  case "$t" in
    *"Permission is hereby granted, free of charge"*) echo "MIT"; return 0 ;;
    *"Permission to use, copy, modify, and/or distribute this software for any purpose"*) echo "ISC"; return 0 ;;
    *"This is free and unencumbered software released into the public domain"*) echo "Unlicense"; return 0 ;;
    *"Mozilla Public License Version 2.0"*) echo "MPL-2.0"; return 0 ;;
    *"Eclipse Public License"*) echo "EPL"; return 0 ;;
  esac
  case "$t" in
    *"Redistribution and use in source and binary forms"*)
      case "$t" in
        *"Neither the name"*) echo "BSD-3-Clause"; return 0 ;;
      esac
      echo "BSD-2-Clause"; return 0 ;;
  esac
  case "$t" in
    *"Creative Commons"*) echo "CC-FAMILY"; return 0 ;;
  esac
  echo "UNRECOGNISED"
}

# --- the remedy, lifted from p1035/ecl.sh VERBATIM --------------------------
# ECL-2.0 IS the Apache-2.0 text with section 3's patent grant narrowed to
# education, so it is PERMISSIVE and Globant can build on it.
classify_ecl() {
  local f="$1" t
  [ -s "$f" ] || { echo "NOT-ECL"; return 0; }
  t=$(tr -d '\r' < "$f")
  case "$t" in
    *"Educational Community License"*)
      case "$t" in
        *"scope of the patent grant in section 3"*) echo "PERMISSIVE/ECL-2.0" ; return 0 ;;
      esac
      echo "PERMISSIVE/ECL-UNPINNED" ; return 0 ;;
  esac
  echo "NOT-ECL"
}

# --- NEW IN p1040: the two composed, so a census cannot miss ECL ------------
# classify_grant <file> -> the family, with ECL VISIBLE.
# The ECL probe runs FIRST and only overrides when classify_payload has failed
# to recognise the text. That ordering is deliberate and testable: if a future
# ECL payload ever does carry the Apache title, classify_payload will name it
# Apache-2.0 and this function must NOT silently relabel it -- the divergence
# is a finding (P1039's live detector), and divergence_flag() below reports it.
classify_grant() {
  local f="$1"
  local base ecl extra restricted

  # A restricting payload is settled FIRST and never falls through to a grant
  # branch. This ordering is the whole safety property of the function.
  restricted=$(classify_restricted "$f")
  case "$restricted" in -) : ;; *) echo "$restricted"; return 0 ;; esac

  base=$(classify_payload "$f")
  case "$base" in UNRECOGNISED|EMPTY) : ;; *) echo "$base"; return 0 ;; esac

  # Only now, with the p1029 classifier having declined to name it, do the
  # recovery probes run. They can therefore never OVERRIDE a reading p1029
  # made -- they only fill a silence, which is what Gap 398 asked for.
  ecl=$(classify_ecl "$f")
  case "$ecl" in PERMISSIVE/*) echo "${ecl#PERMISSIVE/}"; return 0 ;; esac

  extra=$(classify_extra "$f")
  case "$extra" in -) : ;; *) echo "$extra"; return 0 ;; esac

  echo "$base"
}

# divergence_flag <file> -> how the ECL probe and the p1029 classifier relate.
# Kept as a separate observation from the family, because pass 105's whole
# finding was that one label (UNRECOGNISED) held three different facts.
divergence_flag() {
  local f="$1" base ecl
  base=$(classify_payload "$f")
  ecl=$(classify_ecl "$f")
  local extra restricted
  restricted=$(classify_restricted "$f")
  case "$restricted" in
    -) : ;;
    *) case "$base" in
         UNRECOGNISED|EMPTY) echo "NAMED-AS-NON-GRANT" ;;
         *)                  echo "RESTRICTED-OVER/$base" ;;
       esac
       return 0 ;;
  esac
  case "$ecl" in
    PERMISSIVE/*)
      case "$base" in
        UNRECOGNISED) echo "RECOVERED-BY-ECL" ;;
        Apache-2.0)   echo "MISLABEL-AS-APACHE" ;;
        *)            echo "DISAGREE/$base" ;;
      esac
      return 0 ;;
  esac
  case "$base" in
    UNRECOGNISED|EMPTY)
      extra=$(classify_extra "$f")
      case "$extra" in -) echo "-" ;; *) echo "RECOVERED-BY-EXTRA" ;; esac
      return 0 ;;
  esac
  echo "-"
}


# --- NEW IN p1040, limb A2: the families the hand-read found --------------
# unread.sh read all 54 UNRECOGNISED rows from the first corpus census. ECL was
# ONE blind spot; reading the rest found five more mechanisms, each of which put
# a real grant in no bucket at all. Every branch below is keyed on a string
# MEASURED in a live payload this pass, and every one has a test.
#
#   1. EUPL        -- the EU's own licence. 8 rows, all one EMEA publisher.
#   2. CASE        -- "GNU Affero General Public License" in title case. The
#                     p1029 branches key on the ALL-CAPS title only.
#   3. PUNCTUATION -- "Mozilla Public License, version 2.0": one comma and a
#                     lowercase v defeated the MPL branch.
#   4. LANGUAGE    -- "LICENCA PUBLICA GERAL AFFERO GNU". The classifier was
#                     English-only, and a Brazilian K-12 SIS paid for it.
#   5. NON-GRANT   -- Elastic 2.0, BUSL, PolyForm, bespoke click-through terms.
#                     These were sitting in UNRECOGNISED beside real grants.
#                     Recovering a permissive row is an opportunity; mistaking
#                     one of THESE for permissive is a legal problem, so they
#                     get a bucket of their own and can never be promoted.

# classify_restricted <file> -> a NAMED non-grant, or "-".
# Runs BEFORE every grant branch: a payload that says "Noncommercial" must
# never fall through to a branch that happens to match some other phrase in it.
classify_restricted() {
  local f="$1" t
  [ -s "$f" ] || { echo "-"; return 0; }
  t=$(tr -d '\r' < "$f")

  # THE GENERAL RULE, arrived at by three measured regressions in this
  # instrument's OWN code, each caught by diffing two census runs:
  #
  #   ECL                  -- "Educational Community License" CONTAINS the
  #                           substring "Community License", so the bespoke
  #                           branch swallowed the exact permissive family this
  #                           pass exists to recover: 10 rows.
  #   huggingface/transformers, mlflow/mlflow, masakhane-ner
  #                        -- a conventional "All rights reserved" copyright
  #                           line sits ABOVE a full Apache-2.0 text. A generic
  #                           branch on that phrase demoted three real
  #                           Apache-2.0 rows to non-grant.
  #   caviraoss/pagelm     -- an MIT grant plus 7.5 KB of other terms.
  #
  # So: a restriction branch must never fire UNCHALLENGED on a payload that
  # DECLARES a known grant family. Where both are present the answer is not a
  # silent pick either way -- it is a CONFLICT a human has to read (P1036),
  # because the payload may be dual-licensed (P1030) or may be a restricted
  # licence quoting a grant. Reported as such; never auto-promoted.
  #
  # The generic English "All rights reserved" branch is GONE entirely. It is a
  # copyright formula, not a restriction: it appears inside BSD notices, which
  # are grants. Only an explicit restriction, or the Chinese all-rights text
  # pass 104 read in full, names a non-grant here.
  local declared t_strip
  declared=$(declares_known_grant "$f")

  # AND the second half of the rule, which the first version of it got wrong:
  # a restriction pattern that is a SUBSTRING OF A DECLARED LICENCE'S OWN NAME
  # is a collision, not a conflict. "Educational Community License" contains
  # "Community License", so the general conflict rule -- correct for an MIT
  # payload carrying 7.5 KB of extra terms -- re-broke ECL by calling it a
  # CONFLICT instead of a grant.
  #
  # So the declared titles are STRIPPED before any restriction string is
  # sought. What remains is the text that is not part of a licence's name, and
  # only a hit there is evidence of a restriction.
  #
  # AND THE STRIP MUST RUN ON FLATTENED TEXT, which cost a third attempt to
  # get right. Licence files are hard-wrapped at ~72 columns, so a multi-word
  # pattern can straddle a newline. In the Sakai ECL payload the title appears
  # five times; the fifth, at line 195, wraps as "Licensed under the
  # Educational\nCommunity License, Version 2.0". A strip keyed on the unwrapped
  # title removed four of five and left a bare "Community License" at the start
  # of line 196 -- so ECL came back a CONFLICT again, from one line break.
  #
  # p1035 hit the same hazard from the other side ("the version may sit on its
  # own line below the title, so a title-only match splits ONE grant into two
  # families on line-wrapping alone"). Collapsing whitespace first is the fix
  # for both, and it is applied to every substring test in this function.
  t_strip=$(printf '%s' "$t" | tr '\n' ' ' | tr -s ' ' \
            | sed -e 's/Educational Community License//g' \
                  -e 's/European Union Public Licence//g')

  local hit="-"
  case "$t_strip" in
    *"Elastic License 2.0"*)            hit="Elastic-2.0"     ;;
    *"Business Source License"*)        hit="BUSL"            ;;
    *"PolyForm Noncommercial"*)         hit="PolyForm-NC"     ;;
    *"PolyForm Strict"*)                hit="PolyForm-Strict" ;;
    *"BY DOWNLOADING"*)                 hit="BESPOKE-TOU"     ;;
    *"Evaluation Dataset License"*)     hit="BESPOKE-TOU"     ;;
    *"Community License"*)              hit="BESPOKE-TOU"     ;;
  esac
  case "$t" in
    *"保留所有权利"*)                    echo "ALL-RIGHTS-RESERVED" ; return 0 ;;
  esac
  case "$t_strip" in
    *"proprietary and confidential"*)   hit="PROPRIETARY"     ;;
    *"is proprietary"*)                 hit="PROPRIETARY"     ;;
    *"Proprietary License"*)            hit="PROPRIETARY"     ;;
  esac

  case "$hit" in
    -) echo "-"; return 0 ;;
  esac
  case "$declared" in
    -) echo "$hit"; return 0 ;;
    *) echo "GRANT+RESTRICTION-CONFLICT"; return 0 ;;
  esac
}

# declares_known_grant <file> -> the grant family a payload DECLARES, or "-".
# Title/phrase presence only. It answers "does this payload contain a grant at
# all", which is the question the restriction branches have to ask before they
# fire -- not "which grant governs", which is classify_grant's job.
declares_known_grant() {
  local f="$1" t lower
  [ -s "$f" ] || { echo "-"; return 0; }
  t=$(tr -d '\r' < "$f")
  lower=$(printf '%s' "$t" | tr 'A-Z' 'a-z')
  case "$t" in
    *"Educational Community License"*)              echo "ECL"    ; return 0 ;;
    *"Apache License"*)                             echo "Apache" ; return 0 ;;
    *"Permission is hereby granted, free of charge"*) echo "MIT"  ; return 0 ;;
    *"Redistribution and use in source and binary forms"*) echo "BSD" ; return 0 ;;
    *"This is free and unencumbered software released into the public domain"*) echo "Unlicense" ; return 0 ;;
  esac
  case "$lower" in
    *"mozilla public license"*)        echo "MPL"  ; return 0 ;;
    *"gnu affero general public license"*) echo "AGPL" ; return 0 ;;
    *"gnu lesser general public license"*) echo "LGPL" ; return 0 ;;
    *"gnu general public license"*)     echo "GPL"  ; return 0 ;;
    *"eupl"*)                           echo "EUPL" ; return 0 ;;
    *"creative commons"*)               echo "CC"   ; return 0 ;;
  esac
  echo "-"
}

# classify_extra <file> -> a family the p1029 branches miss, or "-".
classify_extra() {
  local f="$1" t lower
  [ -s "$f" ] || { echo "-"; return 0; }
  t=$(tr -d '\r' < "$f")
  lower=$(printf '%s' "$t" | tr 'A-Z' 'a-z')

  # 1. EUPL. Named by reference in a 300-700 B payload, so the branch must
  #    match the NAME and not a licence body (P742: grant body vs reference).
  case "$lower" in
    *"eupl, version 1.2"*|*"eupl v1.2"*|*"european union public licence v. 1.2"*)
      echo "EUPL-1.2" ; return 0 ;;
    *"eupl, version 1.1"*|*"eupl v1.1"*|*"european union public licence v. 1.1"*)
      echo "EUPL-1.1" ; return 0 ;;
    *"eupl"*) echo "EUPL-UNPINNED" ; return 0 ;;
  esac

  # 4. LANGUAGE -- Portuguese AGPL/GPL, measured at 35 326 B in two repositories.
  case "$t" in
    *"LICEN"*"A P"*"BLICA GERAL AFFERO GNU"*) echo "AGPL-3.0" ; return 0 ;;
    *"LICEN"*"A P"*"BLICA GERAL GNU"*)        echo "GPL-FAMILY-PT" ; return 0 ;;
  esac

  # 3. PUNCTUATION -- comma and lowercase "version" defeated the MPL branch.
  #
  # ORDER IS LOAD-BEARING, and a measured regression proves it: MPL-2.0 section
  # 3.3 NAMES the GNU GPL, LGPL and AGPL as "Secondary Licenses". So the full
  # MPL text matches the case-folded GNU branch below, and dequelabs/axe-core
  # -- 15 921 B of plain MPL-2.0 -- was classified GPL-3.0 when MPL came after.
  # This is the same hazard classify_payload documents for AFFERO before GPL,
  # one level up: a licence that REFERENCES another family must be settled
  # before the family it references.
  case "$lower" in
    *"mozilla public license"*)
      case "$lower" in *"2.0"*) echo "MPL-2.0" ; return 0 ;; esac
      echo "MPL-FAMILY" ; return 0 ;;
  esac

  # 2. CASE -- fold case and re-test the GNU titles. Order matters here for the
  #    same reason it does in classify_payload: AFFERO and LESSER first.
  case "$lower" in
    *"gnu affero general public license"*)
      case "$lower" in *"version 3"*) echo "AGPL-3.0" ; return 0 ;; esac
      echo "AGPL-FAMILY" ; return 0 ;;
    *"gnu lesser general public license"*) echo "LGPL-3.0" ; return 0 ;;
  esac
  case "$lower" in
    *"gnu general public license"*)
      case "$lower" in
        *"version 3"*) echo "GPL-3.0" ; return 0 ;;
        *"version 2"*) echo "GPL-2.0" ; return 0 ;;
      esac
      echo "GPL-FAMILY" ; return 0 ;;
  esac

  # Short permissive texts the p1029 phrase branches do not reach.
  case "$t" in
    *"BSD Zero Clause License"*)   echo "0BSD" ; return 0 ;;
    *"ISC License"*)               echo "ISC"  ; return 0 ;;
    *"CC0 1.0 Universal"*)         echo "CC0-1.0" ; return 0 ;;
    *"Open Software License"*)     echo "OSL-3.0" ; return 0 ;;
  esac
  case "$lower" in
    *"the linux kernel is provided under"*) echo "GPL-2.0" ; return 0 ;;
  esac
  echo "-"
}

# --- P1037: name the bucket by the PROPERTY, never by a member list ---------
# Pass 104 published "permissive (MIT / Apache-2.0 / BSD)" -- a name with no
# room for ECL in it, so even a perfect classifier upstream could not have
# counted it. These names enumerate nothing.
bucket_of() {
  case "$1" in
    MIT|Apache-2.0|Apache-OTHER|BSD-3-Clause|BSD-2-Clause|ISC|Unlicense|ECL-2.0|ECL-UNPINNED|0BSD)
      echo "PERMISSIVE" ;;
    AGPL-3.0|AGPL-FAMILY|LGPL-3.0|GPL-3.0|GPL-2.0|GPL-OTHER|GPL-FAMILY|GPL-FAMILY-PT|OSL-3.0|MPL-2.0|MPL-FAMILY|EPL|EUPL-1.1|EUPL-1.2|EUPL-UNPINNED)
      echo "COPYLEFT" ;;
    CC-FAMILY|CC0-1.0)
      echo "CC" ;;
    Elastic-2.0|BUSL|PolyForm-NC|PolyForm-Strict|BESPOKE-TOU|PROPRIETARY|ALL-RIGHTS-RESERVED)
      echo "NON-GRANT" ;;
    GRANT+RESTRICTION-CONFLICT)
      echo "UNREAD" ;;
    EMPTY|UNRECOGNISED)
      echo "UNREAD" ;;
    *)
      echo "UNREAD" ;;
  esac
}
