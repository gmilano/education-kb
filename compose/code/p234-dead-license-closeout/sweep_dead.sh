#!/bin/bash
# P234 — close out the "dead repo => license not verified" table of repos/trending.md:3450.
#
# Pass 76 (P231) refuted the honesty note of that table for ONE of its five rows:
# jdolny/OneRoster.NET, filed as "— (no verificada: repo muerto)", is MIT and carries v1p2 —
# the only permissive piece of its layer with the live spec.  The note's reasoning
# ("a permissive license on a repo with no commits in a decade does not change the decision")
# is therefore already false once.  This instrument measures the rows that are STILL unmeasured.
#
# Channel: raw.githubusercontent.com only (api.github.com/repos -> 403 in this environment,
# trend 601).  Ref HEAD, never a branch list (P170).  Classify on the PAYLOAD (P172):
# read the license text itself, plus the holder line, never a repo badge.
#
# CORRECTED IN THIS PASS (P237).  The first build of this instrument defined its OWN family
# classifier with an AGPL-first grep over the body, which is exactly the P171 defect this base
# fixed five instruments ago -- it reported LearningLocker/learninglocker (GPL-3.0) as AGPL-3.0.
# The classifier now comes from ../lib/license_family.sh, which is tested.  Do not inline one.
#
# TSV: slug \t path \t http \t class \t holder
set -u
. "$(cd "$(dirname "$0")/../lib" && pwd)/license_family.sh"

NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE-MIT LICENSE.APACHE2 MIT-LICENSE MIT-LICENSE.txt UNLICENSE NOTICE"


for slug in "$@"; do
  found=0
  for n in $NAMES; do
    out=$(curl -s --max-time 25 -w $'\n%{http_code}' \
          "https://raw.githubusercontent.com/${slug}/HEAD/${n}" 2>/dev/null)
    code=$(printf '%s' "$out" | tail -1)
    body=$(printf '%s' "$out" | sed '$d')
    [ "$code" = "200" ] || continue
    cls=$(family_of "$body")
    # holder, under P184: the license FILE answers the holder question ONLY for MIT/BSD/ISC,
    # whose standard text carries a FILLED holder line.  Apache-2.0 keeps its holder in an
    # APPENDIX that ships as the unfilled template "Copyright [yyyy] [name of copyright owner]",
    # and the GPL family's copyright line belongs to the FSF, not to the project.  The first
    # build of this instrument grepped any line starting with "copyright" and so printed Apache
    # BOILERPLATE ("copyright notice that is included in or attached to the work") as if it were
    # a holder.  Measured in this pass: of the two Apache-2.0 rows, EASOL/edfi-to-oneroster
    # carries NO copyright line at all and gotranseo/oneroster carries the unfilled template.
    case "$cls" in
      MIT|BSD|ISC)
        holder=$(printf '%s' "$body" | grep -iE '^[[:space:]]*(copyright|\(c\))' | head -1 \
                 | sed -E 's/^[[:space:]]*//; s/[[:space:]]+/ /g' | cut -c1-90)
        [ -z "$holder" ] && holder="(texto permisivo SIN linea de titular)" ;;
      *)
        holder="(no respondible desde el archivo: $cls — P184)" ;;
    esac
    printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$n" "$code" "$cls" "$holder"
    found=1
    break
  done
  [ "$found" = 0 ] && printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$(echo $NAMES | wc -w)x404" "404" "SIN-ARCHIVO" "-"
done
