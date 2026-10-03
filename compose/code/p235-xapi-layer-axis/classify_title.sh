#!/bin/bash
# P236 — the discriminator between GPL-3.0 and AGPL-3.0 is the TITLE BLOCK, never the body.
#
# Measured defect, found in this pass's own first instrument: GPL-3.0 section 13 is titled
# "Use with the GNU Affero General Public License" and the phrase "GNU Affero General Public
# License" appears THREE times in the GPL-3.0 body.  Any classifier that greps the body for
# "affero" before testing "general public" therefore reports every GPL-3.0 payload as AGPL-3.0.
#
# Verified both ways in this run:
#   LearningLocker/learninglocker  body-grep -> AGPL-3.0 (WRONG)  title-block -> GPL-3.0 (right,
#                                  and concordant with package.json "GPL-3.0" + README badge)
#
# The rule: read the TITLE, which is the first non-blank line of an FSF license file.  AGPL-3.0
# says "GNU AFFERO GENERAL PUBLIC LICENSE"; GPL-3.0 says "GNU GENERAL PUBLIC LICENSE" and only
# MENTIONS Affero in section 13.  A mention is not a grant.
#
# Usage: classify_title.sh <slug> ...   TSV: slug \t file \t class \t title_line \t concordancia
set -u
NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt"

class_of_title() {
  local t; t=$(tr '[:upper:]' '[:lower:]')
  case "$t" in
    *"affero general public license"*) echo "AGPL-3.0" ;;
    *"lesser general public license"*) echo "LGPL" ;;
    *"general public license"*)        echo "GPL" ;;
    *"apache license"*)                echo "Apache-2.0" ;;
    *"mozilla public license"*)        echo "MPL-2.0" ;;
    *"educational community license"*) echo "ECL-2.0" ;;
    *"mit license"*)                   echo "MIT" ;;
    *) echo "TITULO-NO-CANONICO" ;;
  esac
}

for slug in "$@"; do
  hit=0
  for n in $NAMES; do
    o=$(curl -s --max-time 25 -w $'\n%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/${n}" 2>/dev/null)
    [ "$(printf '%s' "$o" | tail -1)" = "200" ] || continue
    body=$(printf '%s' "$o" | sed '$d')
    # title block = the first 3 non-blank lines; a license text puts its name there
    title=$(printf '%s' "$body" | grep -vE '^[[:space:]]*$' | head -3 | tr '\n' ' ' | sed -E 's/[[:space:]]+/ /g')
    cls=$(printf '%s' "$title" | class_of_title)
    # GPL/AGPL version lives on the title line too
    case "$cls" in
      GPL|AGPL-3.0|LGPL)
        v=$(printf '%s' "$title" | grep -oiE 'version [0-9]+' | head -1 | grep -oE '[0-9]+')
        [ -n "${v:-}" ] && cls="${cls%%-*}-${v}.0" ;;
    esac
    # independent channel: does a manifest agree?
    man="-"
    for m in package.json composer.json pyproject.toml Cargo.toml; do
      mo=$(curl -s --max-time 20 -w $'\n%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/${m}" 2>/dev/null)
      [ "$(printf '%s' "$mo" | tail -1)" = "200" ] || continue
      man=$(printf '%s' "$mo" | sed '$d' | grep -oiE '"licen[sc]e"[[:space:]]*:[[:space:]]*"[^"]+"|^[[:space:]]*license[[:space:]]*=[[:space:]]*"[^"]+"' \
            | head -1 | sed -E 's/.*"([^"]+)"$/\1/')
      [ -n "$man" ] && break || man="-"
    done
    conc="(sin manifiesto)"
    if [ "$man" != "-" ]; then
      if printf '%s' "$man" | grep -qiF "${cls%%-*}"; then conc="CONCORDANTE ($man)"; else conc="DISCORDANTE ($man)"; fi
    fi
    printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$n" "$cls" "$(printf '%s' "$title" | cut -c1-48)" "$conc"
    hit=1; break
  done
  [ "$hit" = 0 ] && printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "7x404" "SIN-ARCHIVO" "-" "-"
done
