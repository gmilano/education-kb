#!/usr/bin/env bash
# p1040 limb C -- place a row by P1035's rule, applied to EMEA this time.
#
# Usage: bash holder.sh <slug-list>
#
# Pass 105's lead #2, verbatim: "P1035 cuts both ways. If a university name
# cannot place a row in LATAM, it cannot place one in EMEA either -- and
# fwu-de / dini-ag-kim were placed on org-name reasoning this pass has just
# invalidated."
#
# So the org name `fwu-de` is NOT evidence here, and neither is `dini-ag-kim`.
# A row places only on a ccTLD, a country word, or a nationally unique system
# name -- and the string that placed it gets published beside the region.
# Everything else returns UNPLACED, which is a finding and not a failure.
set -u
cd "$(dirname "$0")"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

# place_string <text> -> "<region>\t<placing string>"
# Deliberately narrow. P1035's correction came from `universidad de Cordoba`
# resolving to two continents, so an institution name alone never places.
place_string() {
  local t="$1" hit
  # 1. ccTLD, the strongest signal: a country-coded domain the publisher owns.
  hit=$(printf '%s' "$t" | grep -aoiE '\b[a-z0-9-]+\.(de|fi|no|se|dk|nl|fr|es|it|pl|uk|ie|at|ch|be|pt|gr|cz)\b' | head -1)
  if [ -n "$hit" ]; then printf 'EMEA\tccTLD:%s\n' "$hit"; return 0; fi
  hit=$(printf '%s' "$t" | grep -aoiE '\b[a-z0-9-]+\.(br|mx|ar|cl|co|pe|uy|ec|bo|py|ve|cr|gt)\b' | head -1)
  if [ -n "$hit" ]; then printf 'LATAM\tccTLD:%s\n' "$hit"; return 0; fi
  hit=$(printf '%s' "$t" | grep -aoiE '\b[a-z0-9-]+\.(jp|cn|kr|in|sg|au|nz|id|my|th|vn|ph|tw|hk)\b' | head -1)
  if [ -n "$hit" ]; then printf 'APAC\tccTLD:%s\n' "$hit"; return 0; fi
  # 2. a country word in the publisher's own text.
  hit=$(printf '%s' "$t" | grep -aoiE '\b(germany|deutschland|finland|suomi|norway|norge|sweden|denmark|netherlands|nederland|france|spain|espana|italy|poland|austria|switzerland|belgium|portugal|ireland)\b' | head -1)
  if [ -n "$hit" ]; then printf 'EMEA\tcountry:%s\n' "$hit"; return 0; fi
  hit=$(printf '%s' "$t" | grep -aoiE '\b(brazil|brasil|mexico|argentina|chile|colombia|peru|uruguay|ecuador|bolivia|paraguay|venezuela)\b' | head -1)
  if [ -n "$hit" ]; then printf 'LATAM\tcountry:%s\n' "$hit"; return 0; fi
  # 3. a nationally unique SYSTEM name -- not an institution name.
  hit=$(printf '%s' "$t" | grep -aoE '\b(SIGAA|UNAM|KOSKI|Opetushallitus|Utdanningsdirektoratet|Kennisnet|BNCC)\b' | head -1)
  if [ -n "$hit" ]; then
    case "$hit" in
      SIGAA|UNAM|BNCC) printf 'LATAM\tsystem:%s\n' "$hit"; return 0 ;;
      *)               printf 'EMEA\tsystem:%s\n' "$hit"; return 0 ;;
    esac
  fi
  printf 'UNPLACED\t-\n'
}

printf 'slug\tholder_line\tregion\tplaced_by\tsource\n'
while IFS= read -r slug; do
  case "$slug" in ''|'#'*) continue ;; esac
  holder="-"; src="-"
  # The HOLDER line, which is what the lead actually asked for: the copyright
  # attribution inside the grant, not the org segment of the address.
  for f in LICENSE LICENSE.md LICENCE COPYING NOTICE README.md; do
    code=$(curl -sS --max-time 40 -o "$TMP/p" -w '%{http_code}' \
            "https://raw.githubusercontent.com/${slug}/HEAD/${f}" 2>/dev/null) || code=000
    [ "$code" = "200" ] || continue
    h=$(grep -aiE 'copyright|urheberrecht|\(c\)|©' "$TMP/p" \
        | grep -aviE 'copyright \[?yyyy\]?|copyright \(c\) <|copyright holder:|copyright notice' \
        | head -1 | sed 's/^[[:space:]]*//' | cut -c1-90 | tr '\t' ' ')
    if [ -n "$h" ]; then holder="$h"; src="$f"; break; fi
  done
  # Place on the holder line FIRST; fall back to the README only if the holder
  # line carries no placing string, and say which was used.
  pl=$(place_string "$holder")
  reg=$(printf '%s' "$pl" | cut -f1); by=$(printf '%s' "$pl" | cut -f2)
  if [ "$reg" = "UNPLACED" ]; then
    code=$(curl -sS --max-time 40 -o "$TMP/r" -w '%{http_code}' \
            "https://raw.githubusercontent.com/${slug}/HEAD/README.md" 2>/dev/null) || code=000
    if [ "$code" = "200" ]; then
      pl=$(place_string "$(cat "$TMP/r")")
      reg=$(printf '%s' "$pl" | cut -f1); by=$(printf '%s' "$pl" | cut -f2)
      [ "$reg" != "UNPLACED" ] && src="$src+README.md"
    fi
  fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$holder" "$reg" "$by" "$src"
done < "$1"
