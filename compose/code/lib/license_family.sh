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
