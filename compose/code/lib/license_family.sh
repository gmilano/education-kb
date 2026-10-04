# SHARED license-family classifier — source this, do not rewrite it.
#
# Why this file exists (P237, pass 77 del 2026-10-03).  This base had already paid for the
# GPL-3.0/AGPL-3.0 defect and registered it as P171: section 13 of GPL-3.0 is TITLED "Use with
# the GNU Affero General Public License", so a classifier that greps the BODY for "affero"
# labels every GPL-3.0 payload AGPL-3.0.  The hardened instruments (p114, p170, p206, p211,
# p230) all classify on the TITLE BLOCK and say so in their headers; p206 even ships a
# regression test with the section-13 fixture.
#
# And pass 77 reintroduced the defect anyway, in two fresh instruments, because it wrote a new
# classifier from scratch instead of reusing a hardened one.  The correction did not travel: it
# lived in five instruments and in prose, and a sixth instrument inherited none of it.  A rule
# that has to be remembered is not a control.  This file is the control.
#
# family_of <payload> -> SPDX-ish family on stdout
#   Classifies on the TITLE BLOCK (first 40 lines), never the body (P171).
#   Falls back to a body test only for MIT/BSD, whose grant line IS their identity and whose
#   texts carry no confusable title.
osi_family_of() {
  local t
  t=$(printf '%s' "$1" | head -40 | tr -s '[:space:]' ' ')
  case "$t" in
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*) echo "AGPL-3.0"; return ;;
    *"GNU LESSER GENERAL PUBLIC LICENSE"*) echo "LGPL"; return ;;
  esac
  # P288 (pase 96).  La rama AGPL de arriba es un glob de `case`, o sea SENSIBLE A LA CAJA, y
  # TODAS las fixtures AGPL de la suite traian el titulo canonico EN MAYUSCULAS -- asi que las
  # 41 aserciones pasaban sin ejercitar nunca el caso donde esta rama puede fallar (P126 pt.2).
  # Un payload AGPL-3.0 REFLOWED (kuali/kfs, 33.755 B) no trae esa linea de titulo: caia por la
  # rama, y entonces lo atrapaba la rama GPL de abajo, que usa `grep -qi` y matchea el
  # PREAMBULO DE LA PROPIA AGPL -- «The GNU General Public License permits making a modified
  # version and letting the public access it on a server...».  Veredicto: GPL-3.0.  Es P171
  # reabierto por el eje de la CAJA, y sobre el par exacto que P171 existe para proteger.
  #
  # El ancla es la DEFINICION de la seccion 0, que es mutuamente excluyente:
  #   AGPL-3.0 -> «"This License" REFERS TO version 3 of the GNU Affero General Public License»
  #   GPL-3.0  -> «"This License" refers to version 3 of the GNU General Public License»
  # La seccion 13 de la GPL-3.0 nombra la AGPL, pero dice «licensed UNDER version 3 of the GNU
  # Affero...», no «refers to» -- por eso el ancla lleva «refers to» y P171 queda cerrado.
  # El control NEGATIVO que lo afirma vive en `p288-agpl-casefold/test_casefold.sh`.
  printf '%s' "$t" | grep -qi 'refers to version 3 of the GNU Affero General Public License' \
      && { echo "AGPL-3.0"; return; }
  if printf '%s' "$t" | grep -qi 'GNU GENERAL PUBLIC LICENSE'; then
     printf '%s' "$t" | grep -qi 'Version 3' && echo "GPL-3.0" || echo "GPL-2.0"; return; fi
  printf '%s' "$t" | grep -qi 'Educational Community License' && { echo "ECL-2.0"; return; }
  printf '%s' "$t" | grep -qi 'Apache License' && { echo "Apache-2.0"; return; }
  printf '%s' "$t" | grep -qi 'MIT License' && { echo "MIT"; return; }
  # Added in pass 82 (P250).  Three families reached this base's catalogue and all three came
  # back UNCLASSIFIED, so they are classified on the TITLE BLOCK like everything else (P171).
  printf '%s' "$t" | grep -qi 'BSD Zero Clause\|Zero-Clause BSD\|0BSD' && { echo "0BSD"; return; }
  printf '%s' "$t" | grep -qi 'ISC License' && { echo "ISC"; return; }
  if printf '%s' "$t" | grep -qi 'Creative Commons\|creativecommons.org'; then
    printf '%s' "$t" | grep -qi 'CC0\|Public Domain Dedication' && { echo "CC0-1.0"; return; }
    printf '%s' "$t" | grep -qi 'ShareAlike\|CompartirIgual\|BY-SA'   && { echo "CC-BY-SA-4.0"; return; }
    printf '%s' "$t" | grep -qi 'NonCommercial\|NoComercial\|BY-NC'    && { echo "CC-BY-NC-4.0"; return; }
    printf '%s' "$t" | grep -qi 'Attribution\|Atribuci'                && { echo "CC-BY-4.0"; return; }
    echo "CC-UNSPECIFIED"; return
  fi
  printf '%s' "$1" | grep -qi 'Permission is hereby granted, free of charge' && { echo "MIT"; return; }
  printf '%s' "$1" | grep -qi 'Redistribution and use in source and binary forms' && { echo "BSD"; return; }
  printf '%s' "$t" | grep -qi 'Mozilla Public License' && { echo "MPL-2.0"; return; }
  # The Unlicense. p170's inline classifier HAD this; this shared lib never did, so adopting
  # the lib would have LOST a family (FWU-DE/mem-mcp). P237 cuts both ways: the shared control
  # is only better than the copies once it is a superset of them.
  printf '%s' "$1" | grep -qi 'free and unencumbered software released into the public domain' \
      && { echo "Unlicense"; return; }

  # DECLARATION FALLBACK, added in pass 77 after frappe/education.
  #
  # A license FILE is not always a license TEXT.  frappe/education ships a `license.txt` whose
  # entire content is one line -- "License: GNU GPL V3" -- and the title-block rule above
  # correctly refuses it: there is no title block, so it returns UNCLASSIFIED.  That is the
  # right failure, but it is still a failure, and this base already knew the answer ("leida en
  # license.txt, no en el README").
  #
  # The fallback is only safe because of the SIZE GUARD.  P171 exists because a full license
  # BODY contains the names of OTHER licenses (GPL-3.0 sec.13 names the AGPL), so a token match
  # over a body is unsound.  A SHORT payload has no body to be confused by: there is nothing in
  # 200 bytes but the declaration itself.  So the token match runs ONLY under the guard, and
  # the guard is what keeps this from re-opening P171.
  local bytes; bytes=$(printf '%s' "$1" | wc -c | tr -d ' ')
  if [ "$bytes" -le 400 ]; then
    local d; d=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')
    case "$d" in
      *agpl*|*affero*)              echo "AGPL-3.0 (declaracion)"; return ;;
      *lgpl*)                       echo "LGPL (declaracion)"; return ;;
      *"gpl v3"*|*"gpl-3"*|*gplv3*) echo "GPL-3.0 (declaracion)"; return ;;
      *"gpl v2"*|*"gpl-2"*|*gplv2*) echo "GPL-2.0 (declaracion)"; return ;;
      *apache*)                     echo "Apache-2.0 (declaracion)"; return ;;
      *mit*)                        echo "MIT (declaracion)"; return ;;
      *bsd*)                        echo "BSD (declaracion)"; return ;;
    esac
  fi
  echo "UNCLASSIFIED"
}

# affero_lines <payload> -> how many lines name the AGPL.
# The secondary discriminator this base did not have a number for, measured in pass 77:
# a GPL-3.0 payload names the AGPL on 3 lines (its section 13); a real AGPL-3.0 payload names
# it on 15.  GPL-2.0 names it on 0 — it predates the AGPL, so only GPL-3.0 was ever at risk.
affero_lines() { printf '%s' "$1" | grep -ci affero; }

# commercial_use_ok <payload> -> exit 0 if nothing in the payload forbids commercial use.
#
# A SECOND, independent axis (P250, pass 82).  Family and commercial-use are not the same
# question: `CC-BY-SA-4.0` is a real family AND a problem for a client deliverable, while
# `Apache-2.0` is a real family and no problem.  Asking them separately keeps a restriction
# from being hidden behind a family name -- or behind UNCLASSIFIED.
commercial_use_ok() {
  local d; d=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' ' ')
  case "$d" in
    *"non-commercial"*|*"noncommercial"*|*"not-for-profit"*|*"non-profit purposes"*) return 1 ;;
    *"obtain a commercial license"*|*"commercial licence must"*|*"for academic research or other not-for-profit"*) return 1 ;;
    *"excludes any service or part of selling a service"*) return 1 ;;
  esac
  return 0
}

# ---------------------------------------------------------------------------
# P250, pass 82 — commercial use as a SECOND axis, and the gate that makes it sound.
#
# The first cut of this detector token-matched the payload for "non-commercial" and
# friends. It then reported THREE AGPL-3.0 repos and The Unlicense as commercial-use
# PROHIBITED, which is the opposite of true:
#   * AGPL-3.0 / GPL-3.0 say "occasionally and noncommercially" in section 6 (line 259 of
#     the real payload) -- describing a CONDITION, not a restriction on the licensee.
#   * The Unlicense grants use "for any purpose, commercial or non-commercial" -- the most
#     permissive text there is, flagged by the word it uses to GRANT the permission.
# This is precisely the unsoundness P171 names: a full licence BODY contains the vocabulary
# of other terms, so a token match over a body cannot be trusted. The gate is the fix -- an
# identified OSI family permits commercial use BY DEFINITION and is never token-matched.
# ---------------------------------------------------------------------------

# commercial_use_ok <payload> -> exit 0 if nothing in the payload forbids commercial use.
commercial_use_ok() {
  # THE GATE. Identified OSI family -> allowed, no token match, no false positive.
  [ "$(osi_family_of "$1")" = "UNCLASSIFIED" ] || return 0
  local d; d=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' ' ')
  case "$d" in
    *"non-commercial"*|*"noncommercial"*|*"not-for-profit"*|*"non-profit purposes"*) return 1 ;;
    *"obtain a commercial license"*|*"commercial licence must"*) return 1 ;;
    *"excludes any service or part of selling a service"*) return 1 ;;
  esac
  return 0
}

# family_of <payload> -> OSI family, or NONCOMMERCIAL-NOT-OSI when the payload is not a
# known licence AND forbids commercial use. UNCLASSIFIED and "commercial use is PROHIBITED"
# are opposite answers to the only question this KB exists to answer; they must never be
# the same string.
family_of() {
  local f; f=$(osi_family_of "$1")
  if [ "$f" = "UNCLASSIFIED" ] && ! commercial_use_ok "$1"; then
    echo "NONCOMMERCIAL-NOT-OSI"; return
  fi
  echo "$f"
}

# ---------------------------------------------------------------------------
# P255, pass 85 — the HOLDER question gets the shared control the FAMILY
# question got in P237, and the payload that proves it was needed is GPL-2.0.
#
# This base asks "who is the holder?" in THREE instruments, and until this pass they
# gave THREE different answers on the same GPL payload:
#
#   * p184/extract_holder.py  (pass 66) -> NOT-APPLICABLE, gated on the family.  CORRECT.
#   * p198/holder_of.sh       (pass 69) -> filters ONE hardcoded string,
#                                          'Copyright \(C\) [0-9]{4} Free Software Foundation'.
#   * p204/sweep_payload_license.sh (pass 70) -> `grep -m1 -i copyright`, no gate at all.
#
# Measured this pass on the two real payloads, not on a fixture:
#
#   GPL-2.0 (OpenEMIS/core, 15.518 B) -- the FSF line reads
#       "Copyright (C) 1989, 1991 Free Software Foundation, Inc."
#     TWO years separated by a comma, so `[0-9]{4} Free` does NOT match and p198's filter
#     LETS IT THROUGH.  p198 reports the Free Software Foundation as the holder of OpenEMIS.
#
#   GPL-3.0 (gibbonedu/core, 35.121 B) -- the FSF line IS caught, and then the anchor
#     `^[[:space:]]*(Copyright|\(c\))` matches WRAPPED BODY PROSE instead:
#       "copyright on the Program, and are irrevocable provided the stated"
#     A sentence out of section 8 is reported as a holder.
#
# Both are wrong, in opposite directions, and the root cause is the one P237 already fixed
# for the family question: the question is sound only when it is GATED ON THE FAMILY FIRST.
# A holder is present in the grant text BY CONSTRUCTION for MIT/BSD/ISC/0BSD and absent BY
# CONSTRUCTION for every GPL-family, Apache-2.0, MPL-2.0, ECL-2.0, Unlicense and CC0 text --
# in those the only copyright line belongs to the license's OWN author (the FSF, the ASF),
# never to the project.  So the correct answer for them is not a name and not an empty
# string: it is NOT-APPLICABLE, which is what p184 has said since pass 66.
#
# P197 is why this is a FILE and not a note: a correction survives only if the instrument
# that re-measures knows it.  p184 knew; the two instruments written AFTER it inherited
# nothing, because there was nothing to inherit.
#
# holder_of <payload> -> the project's holder line, or NOT-APPLICABLE (<family>: ...),
#                        or NO-HOLDER-LINE when the family should carry one and does not.
holder_of() {
  local payload="$1" fam
  fam=$(osi_family_of "$payload")

  case "$fam" in
    # Carries the holder in the grant text by construction -> ask.
    MIT|BSD|ISC|0BSD) ;;
    # A short DECLARATION ("License: GNU GPL V3", 19 B in frappe/education) names a family
    # and cedes nothing, so it has no holder to carry.  Kept separate from the families
    # below because the REASON differs: not "the license has its own author" but
    # "there is no license text here at all" (P179: identifier, not cession).
    *"(declaracion)"*)
      echo "NOT-APPLICABLE ($fam: a declaration carries no holder -- P179)"; return ;;
    UNCLASSIFIED|NONCOMMERCIAL-NOT-OSI)
      # No family to gate on, so the question is still open -- but it is asked ONLY of the
      # title block, never of a body this function cannot vouch for.
      ;;
    *)
      echo "NOT-APPLICABLE ($fam: holder not in the license text by construction)"; return ;;
  esac

  # THE ANCHOR.  Only the title block (first 40 lines) -- the same bound P171 put on the
  # family question, and for the same reason: a license BODY contains the vocabulary of the
  # question being asked.  gibbonedu/core is the proof that an unbounded anchor returns prose.
  local line
  line=$(printf '%s' "$payload" | head -40 \
    | grep -iE '^[[:space:]]*(Copyright|\(c\)|©)' \
    | grep -viE 'Free Software Foundation|Apache Software Foundation|Open Source Initiative' \
    | grep -viE 'copyright notice (and|shall)|COPYRIGHT HOLDERS? BE LIABLE|copyright holder, and you' \
    | head -1 | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]\+/ /g')

  # A YEAR IS NOT A HOLDER, AND NEITHER IS A YEAR A REQUIREMENT.
  #
  # The first cut of this guard demanded a digit right after "Copyright (c)", and that cost a
  # real finding on its FIRST sweep -- not in the suite, in the barrido, which is where this
  # base's new instruments keep failing their first honest test.
  #
  #   katoj65/emis -- the EMIS of the Ministry of Education of Uganda -- ships an MIT text of
  #   1.090 B whose holder line is
  #       "Copyright (c) Jonathan Reinink <jonathan@reinink.ca>"
  #   NO YEAR AT ALL.  The year-first guard returned NO-HOLDER-LINE and so HID the holder --
  #   and the holder is the whole point here, because Jonathan Reinink is the author of
  #   Inertia.js / Ping CRM, not of a Ugandan ministry EMIS.  That is a textbook P184
  #   HOLDER-UNRELATED: an INHERITED license, not a granted one.  A guard that suppresses the
  #   very signal P184 exists to raise is worse than no guard.
  #
  # So the test is for a NAME, not for a year: strip the keyword, the (c), the years and the
  # punctuation, and ask whether an alphabetic token survives.
  if [ -n "$line" ]; then
    local rest
    rest=$(printf '%s' "$line" \
      | sed -E 's/^[[:space:]]*[Cc]opyright//; s/\((c|C)\)//g; s/©//g' \
      | sed -E 's/[0-9]{4}//g; s/[0-9]//g' \
      | sed -E 's/[[:punct:]]+/ /g' | tr -s ' ')
    if printf '%s' "$rest" | grep -qE '[A-Za-z]{2}'; then echo "$line"; return; fi
  fi
  echo "NO-HOLDER-LINE"
}
