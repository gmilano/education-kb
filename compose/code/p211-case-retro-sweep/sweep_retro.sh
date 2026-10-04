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

# P237 CERRADO en el pase 101 (P312).  Esta copia inline se REWIREO a la libreria
# compartida.  La razon declarada en el pase 100 para no hacerlo era concreta y correcta
# --«el control compartido todavia no es un superconjunto de las copias» (BUSL, Elastic y
# PolyForm vivian SOLO aca)-- asi que el pase 101 primero las agrego a
# `lib/license_family.sh` con sus controles negativos (6 aserciones nuevas) y DESPUES
# rewireo.  Parchar la copia era el antipatron que P237 existe para nombrar.
#
# El vocabulario de esta copia y el de la libreria COINCIDEN exactamente (AGPL-3.0, LGPL,
# GPL-3.0, GPL-2.0, Apache-2.0, MIT, BSD, MPL-2.0, UNCLASSIFIED), asi que no hace falta
# traduccion: los TSV ya publicados siguen siendo comparables.  Y la copia GANA lo que la
# libreria tiene y ella no: el eje de uso comercial (P250/P312), 0BSD, ISC, ECL-2.0,
# Unlicense, la rama CC compuesta y las tres familias no-OSI.
. "$(dirname "$0")/../lib/license_family.sh"

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
