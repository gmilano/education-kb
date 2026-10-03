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
family_of() {
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
  printf '%s' "$1" | grep -qi 'Permission is hereby granted, free of charge' && { echo "MIT"; return; }
  printf '%s' "$1" | grep -qi 'Redistribution and use in source and binary forms' && { echo "BSD"; return; }
  printf '%s' "$t" | grep -qi 'Mozilla Public License' && { echo "MPL-2.0"; return; }

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
