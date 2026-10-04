#!/bin/bash
# P206 -- the ERP/administrative layer of the vertical, measured by PAYLOAD.
#
# Pass 70 opened the SIS / school-platform category and found it dominated by strong
# copyleft (ClassroomIO AGPL-3.0, Gibbon GPL-3.0), with the single permissive candidate
# (Fedena) measurable only in a MIRROR because the repo the source calls official 404s.
#
# That result was drawn on the SIS slice alone.  The ERP slice -- the administrative
# system a school actually runs fees, admissions and HR on -- was never measured, and the
# `open source platform education ERP CRM MIT Apache` channel has collapsed onto
# OpenEduCat SEO for nine consecutive passes, so the category was never enumerated.
#
# This instrument asks the license question of the ERP slice with the corrections this
# base has already paid for:
#   P170 -- ref HEAD, never a branch list.
#   P172 -- read the PAYLOAD (raw.githubusercontent.com); api.github.com is 403 here.
#   P184 -- the holder is only answerable from the license FILE for MIT/BSD/ISC, whose
#           standard text carries a FILLED holder line.  For GPL/AGPL/Apache the
#           copyright in the file belongs to the license STEWARD, not to the project.
#   P198 -- a 404 at the license names is only measurable on a repo we can REACH, so
#           tree reachability is probed separately and reported as its own column.
#
# TSV: slug \t verdict \t file \t bytes \t sha256-12 \t holder-class \t holder
slug="$1"
NAMES=$(cat "$(dirname "$0")/names.case-matrix.txt" 2>/dev/null || echo LICENSE)   # D1: case matrix, raw.githubusercontent.com is case-SENSITIVE

emit() { printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$1" "$2" "$3" "$4" "$5" "$6"; exit 0; }

get() { # path -> body on stdout, 0 if HTTP 200
  local out code
  out=$(curl -s --max-time 25 -w $'\n%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/$1" 2>/dev/null)
  code=$(printf '%s' "$out" | tail -1)
  [ "$code" = "200" ] || return 1
  printf '%s' "$out" | sed '$d'
}

# Family from the license TEXT, never from a repo badge or a secondary source.
family_of() {
  # D2 (P171): the family is read from the TITLE BLOCK, never from the body.  GPL-3.0 sec. 13
  # is literally headed "Use with the GNU Affero General Public License", so a body grep for
  # AGPL classifies every GPL-3.0 text as AGPL.  Only the first 40 lines are consulted.
  local t
  t=$(printf '%s' "$1" | head -40 | tr -s '[:space:]' ' ')
  case "$t" in
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*)  echo "AGPL-3.0"; return ;;
    *"GNU LESSER GENERAL PUBLIC LICENSE"*)  echo "LGPL"; return ;;
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

for f in $NAMES; do
  body=$(get "$f") || continue
  bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
  sha=$(printf '%s' "$body" | sha256sum | cut -c1-12)
  fam=$(family_of "$body")
  # P184: holder only readable for the filled-holder families.
  case "$fam" in
    MIT|BSD)
      holder=$(printf '%s' "$body" | grep -oiE 'copyright[[:space:]]*(\(c\)|©)?[[:space:]]*[0-9]{4}([[:space:]]*[-,][[:space:]]*[0-9]{4})?[[:space:]]*[^\n]{2,70}' | head -1 | tr -d '\n')
      [ -z "$holder" ] && { hclass="NO-HOLDER"; holder="(text present, holder line unfilled)"; } || hclass="READ"
      ;;
    *) hclass="NOT-APPLICABLE"; holder="(steward copyright, not the project's -- P184)" ;;
  esac
  emit "$fam" "$f" "$bytes" "sha256:$sha" "$hclass" "$holder"
done

# P198: distinguish "reachable and silent" from "unreachable".
for rm in README.md readme.md README.rst README docs/README.md README.markdown; do
  if get "$rm" >/dev/null; then
    emit "NO-CESSION" "-" "-" "-" "TREE-REACHABLE" "(404 at $(echo $NAMES | wc -w | tr -d ' ') license names, tree reachable via $rm)"
  fi
done
emit "UNREACHABLE" "-" "-" "-" "-" "(tree could not be resolved by this channel)"
