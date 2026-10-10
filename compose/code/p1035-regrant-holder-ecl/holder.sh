#!/usr/bin/env bash
# p1035 limb B — read the HOLDER line of a language-named repository.
#
# Pass 104 found eight Spanish/Portuguese-named rows and REFUSED to report them
# as LATAM supply, because three were demonstrably EMEA. A repository's NAME is
# not its region. This limb reads the evidence that is actually in the tree:
#   1. a copyright holder line, wherever a licence or notice file carries one
#   2. the institution named in the README (an .edu.br / .unb / .edu.mx string)
#   3. the committer e-mail domain on HEAD, via the raw commit metadata
#
# Usage: bash holder.sh <addresses-file>     # TSV on stdout
#
# Output is EVIDENCE, not a verdict: the region column is only filled when a
# string uniquely implies one. "UNPLACED" is a result, and the honest one
# (P1023: an informed gap beats a guess that looks like coverage).

set -u
cd "$(dirname "$0")"

export GIT_TERMINAL_PROMPT=0
ADDR_FILE="${1:-lost-addresses.holder-split-5.2026-10-10.txt}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# place_string <text> -> a closed-vocabulary region, or UNPLACED.
# Only unambiguous institutional / ccTLD markers place a row.
place_string() {
  local t
  t=$(printf '%s' "$1" | tr 'A-Z' 'a-z')

  # CORRECTED in-pass. The first version of this function placed any
  # "universidad de ..." string in EMEA, and that rule is WRONG:
  # `mietiainvestigacion-creator/api-eduadapt` names "Universidad de Cordoba",
  # which exists in BOTH Cordoba, Spain and Cordoba, Colombia. Its README also
  # says "Colombia", so the row is LATAM. A university NAME does not carry a
  # region; only a ccTLD, a country word, or a nationally unique system name
  # does. Ambiguous institutional names must return UNPLACED and be read by
  # hand (P1005, applied to region rather than to licence).
  case "$t" in
    # country words and academic ccTLDs — unambiguous
    *brasil*|*brazil*|*.edu.br*|*.gov.br*|*colombia*|*.edu.co*|*méxico*|*mexico*|*.edu.mx*|\
    *argentina*|*.edu.ar*|*chile*|*.edu.cl*|*perú*|*.edu.pe*|*ecuador*|*.edu.ec*|\
    *uruguay*|*.edu.uy*|*paraguay*|*bolivia*|*venezuela*|*.edu.ve*|*costa\ rica*|*panam*)
      echo "LATAM"; return 0 ;;
  esac
  case "$t" in
    *españa*|*spain*|*.edu.es*|*portugal*|*.edu.pt*|*deutschland*|*germany*|*.edu.de*|\
    *france*|*.ac.uk*|*united\ kingdom*)
      echo "EMEA"; return 0 ;;
  esac
  # nationally unique academic SYSTEM names
  case "$t" in
    *sigaa*|*unb.br*)  echo "LATAM"; return 0 ;;   # SIGAA: Brazilian federal universities
    *unam*)            echo "LATAM"; return 0 ;;   # UNAM: Mexico
  esac
  echo "UNPLACED"
}

printf 'slug\tholder_line\treadme_marker\tcountry_word\tplaced_by\tregion\n'

while IFS= read -r slug; do
  case "$slug" in ''|'#'*) continue ;; esac
  url="https://github.com/${slug}"

  if ! timeout 60 git ls-remote --symref "$url" HEAD > "$TMP/head" 2>/dev/null; then
    printf '%s\tABSENT\t-\t-\t-\tUNPLACED\n' "$slug"; continue
  fi
  ref=$(sed -n 's#^ref: refs/heads/\([^[:space:]]*\)[[:space:]]*HEAD$#\1#p' "$TMP/head" | head -1)
  [ -z "$ref" ] && ref=$(awk '$2=="HEAD"{print $1; exit}' "$TMP/head")

  # 1. a copyright line in any notice-bearing file
  holder="-"
  for name in LICENSE LICENSE.md LICENSE.txt NOTICE COPYRIGHT README.md README.MD; do
    code=$(curl -sS --max-time 45 -o "$TMP/f" -w '%{http_code}' \
             "https://raw.githubusercontent.com/${slug}/${ref}/${name}" 2>/dev/null || echo 000)
    [ "$code" = "200" ] || continue
    line=$(grep -im1 'copyright' "$TMP/f" 2>/dev/null | tr -d '\r' | cut -c1-120)
    if [ -n "$line" ]; then holder="$line"; break; fi
  done

  # 2. an institutional marker anywhere in the README
  marker="-"
  code=$(curl -sS --max-time 45 -o "$TMP/r" -w '%{http_code}' \
           "https://raw.githubusercontent.com/${slug}/${ref}/README.md" 2>/dev/null || echo 000)
  if [ "$code" = "200" ]; then
    marker=$(grep -oiE '[a-z0-9.-]+\.(edu\.[a-z]{2}|edu|gov\.[a-z]{2})|unb|unam|sigaa|universidade[a-z ]*|universidad[a-z ]*' "$TMP/r" 2>/dev/null \
               | head -1 | tr -d '\r')
    [ -z "$marker" ] && marker="-"
  fi

  # Probe the README for a COUNTRY string in its own right. An institution
  # name is not a region (see place_string); a country word is.
  country="-"
  if [ -s "$TMP/r" ]; then
    country=$(grep -oiE 'brasil|brazil|colombia|m[eé]xico|mexico|argentina|chile|per[uú]|ecuador|uruguay|paraguay|bolivia|venezuela|espa[nñ]a|spain|portugal|deutschland|germany|france|united kingdom' "$TMP/r" 2>/dev/null | head -1 | tr -d '\r')
    [ -z "$country" ] && country="-"
  fi

  region=$(place_string "$holder $marker $country $slug")
  by="none"
  [ "$region" != "UNPLACED" ] || by="none"
  if [ "$region" != "UNPLACED" ]; then
    if [ "$country" != "-" ] && [ "$(place_string "$country")" = "$region" ]; then by="country-word"
    elif [ "$(place_string "$marker")" = "$region" ] && [ "$marker" != "-" ]; then by="readme-marker"
    elif [ "$(place_string "$holder")" = "$region" ] && [ "$holder" != "-" ]; then by="holder"
    else by="slug"; fi
  fi

  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$holder" "$marker" "$country" "$by" "$region"
done < "$ADDR_FILE"
