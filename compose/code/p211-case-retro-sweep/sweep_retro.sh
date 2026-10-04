#!/bin/bash
# P211 -- the RETROACTIVE case re-measure that pass 71 said this base owed itself.
#
# Pass 71 found that raw.githubusercontent.com is CASE-SENSITIVE and that two false
# NO-CESSION verdicts (frappe/education, frappe/erpnext) came from probing only
# upper-case file names.  It then wrote, explicitly, that EVERY published
# NO-CESSION / UNLICENSED verdict of this base was therefore CONDITIONED BY CASE --
# "not wrong: not closed".
#
# This instrument closes the condition on the largest such population: the 32 rows
# that P170 (pass 64, re-run 2026-10-03) returned as UNLICENSED.
#
# What is DIFFERENT from P170, and why the re-measure is not a repetition:
#   P170 probed 14 names.  Of the three case boxes a project can use
#   (UPPER / lower / Title) it only ever asked UPPER and lower, and only for the
#   LICENSE stem -- it never asked `License`, never asked `copying`/`Copying`,
#   never asked `licence` in lower or Title, and never asked `COPYRIGHT`.
#   This sweep asks 28 names covering all three boxes for every stem P170 used,
#   so a flip can only come from a box P170 did not ask.
#
# Falsifiable hypothesis, written BEFORE the run (pass 72):
#   If the case defect is GENERAL, at least one of the 32 flips to LICENSED.
#   If it was specific to the ERP slice pass 71 measured, all 32 hold and the
#   condition pass 71 opened closes BENIGNLY -- which is itself the finding.
#
# Carries the corrections this base already paid for:
#   P170 -- ref HEAD, never a branch list.
#   P172 -- read the PAYLOAD; api.github.com and github.com are 403 in this environment.
#   P171 -- the family is read from the TITLE BLOCK (first 40 lines), never the body:
#           GPL-3.0 section 13 is headed "Use with the GNU Affero General Public
#           License", so a body grep classifies every GPL-3.0 text as AGPL.
#   P198 -- "reachable and silent" is a different verdict from "unreachable", and the
#           difference is measured with a positive control on the same tree.
#
# TSV: slug \t verdict \t file \t bytes \t sha256-12 \t family \t note
set -u
here="$(cd "$(dirname "$0")" && pwd)"
NAMES=$(cat "$here/names.matrix28.txt")
P170_NAMES=" LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt license license.md license.txt LICENCE LICENCE.md LICENSE-MIT LICENSE-APACHE LICENSE.rst LICENSE-MIT.txt "

get() { # path -> body on stdout, 0 if HTTP 200
  local out code
  out=$(curl -s --max-time 25 -w $'\n%{http_code}' "https://raw.githubusercontent.com/${1}/HEAD/$2" 2>/dev/null)
  code=$(printf '%s' "$out" | tail -1)
  [ "$code" = "200" ] || return 1
  printf '%s' "$out" | sed '$d'
}

family_of() {
  local t
  t=$(printf '%s' "$1" | head -40 | tr -s '[:space:]' ' ')
  case "$t" in
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*) echo "AGPL-3.0"; return ;;
    *"GNU LESSER GENERAL PUBLIC LICENSE"*) echo "LGPL"; return ;;
  esac
  if printf '%s' "$t" | grep -qi 'GNU GENERAL PUBLIC LICENSE'; then
     printf '%s' "$t" | grep -qi 'Version 3' && echo "GPL-3.0" || echo "GPL-2.0"; return; fi
  printf '%s' "$t" | grep -qi 'Apache License' && { echo "Apache-2.0"; return; }
  printf '%s' "$t" | grep -qi 'MIT License' && { echo "MIT"; return; }
  printf '%s' "$1" | grep -qi 'Permission is hereby granted, free of charge' && { echo "MIT"; return; }
  # P304 (pase 99): hueco ACOTADO Y DENTRO DE LA ORACION entre los dos tokens -- la identidad
  # de BSD es una secuencia ORDENADA de palabras, no una frase contigua.  Especimen real:
  # instructure/QTIMigrationTool inserta «of this software» y «(where applicable)».  El arreglo
  # canonico vive en lib/license_family.sh; esta copia inline lo replica y el rewiring a la
  # libreria compartida queda PRE-REGISTRADO (P237 sigue abierto para este archivo).
  printf '%s' "$1" | tr -s '[:space:]' ' ' | grep -qiE 'redistribution and use[^.]{0,40}in source and binary forms' && { echo "BSD"; return; }
  printf '%s' "$t" | grep -qi 'Mozilla Public License' && { echo "MPL-2.0"; return; }
  echo "UNCLASSIFIED"
}

sweep() {
  local slug="$1" body bytes sha fam note
  for f in $NAMES; do
    body=$(get "$slug" "$f") || continue
    bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
    sha=$(printf '%s' "$body" | sha256sum | cut -c1-12)
    fam=$(family_of "$body")
    case "$P170_NAMES" in
      *" $f "*) note="FLIP-NOT-CASE (name was already in the P170 list)" ;;
      *)        note="FLIP-BY-CASE (name absent from the P170 list)" ;;
    esac
    printf '%s\tLICENSED\t%s\t%s\tsha256:%s\t%s\t%s\n' "$slug" "$f" "$bytes" "$sha" "$fam" "$note"
    return
  done
  for rm in README.md readme.md README.rst README docs/README.md README.markdown README.MD; do
    if get "$slug" "$rm" >/dev/null; then
      printf '%s\tNO-CESSION\t-\t-\t-\t-\tHOLDS: 404 at 28 names in 3 case boxes; tree reachable via %s\n' "$slug" "$rm"
      return
    fi
  done
  printf '%s\tUNREACHABLE\t-\t-\t-\t-\tno positive control resolved on this tree\n' "$slug"
}

if [ $# -gt 0 ]; then sweep "$1"; else while read -r s; do [ -n "$s" ] && sweep "$s"; done < "$here/slugs.input.txt"; fi
