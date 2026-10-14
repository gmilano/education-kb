# ACTION P195-C — the DELIVERY verdict, which `family_of` alone does not give.
#
# THE FINDING THIS REPAIRS, measured on `CaviraOSS/PageLM` (LICENSE.md, 8 563 B):
#   title block says  "# PageLM Community License"
#   osi_family_of  -> MIT          (its 40-line title window catches MIT's canonical
#                                   "Permission is hereby granted, free of charge" sentence,
#                                   which this licence wears over a restrictive body)
#   commercial_use_ok -> ALLOWED   (P250's gate: "an identified OSI family permits commercial
#                                   use BY DEFINITION", so the body is never read)
#   the body, lines 46-51          -> "may not be sold, sublicensed, or included in any
#                                      product or service for commercial purposes"
#
# 🔴 Two hardened controls, each CORRECT in isolation, compose into the one wrong answer that
# costs a delivery.  P171 widened the title window to 40 lines so a REFLOWED AGPL would be
# caught; that same window swallows MIT's grant sentence out of a non-MIT licence.  P250 then
# trusts the family and skips the body.
#
# 🟢 THE REPAIR IS NOT A NEW CLASSIFIER (P237).  It is a SIZE-WITHIN-FAMILY control, and it is
# cheap because licence boilerplate is boilerplate: measured over this pass's own census,
# 218 MIT rows have median 1 071 B, p25 1 067, p75 1 080 -- a 13-byte interquartile spread.
# A payload claiming a family while sitting far outside that family's band has been MODIFIED,
# and a modified permissive licence must have its body read before anything ships.
#
# Emits: slug  path  bytes  family  band_verdict  commercial_axis  delivery
set -u
_HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$_HERE/../lib/payload_measure.sh"

# Canonical byte bands, derived from THIS pass's census, not from belief.  lo/hi inclusive.
band_of_family() {
  case "$1" in
    MIT)          echo "1000 1200" ;;
    Apache-2.0)   echo "10000 11800" ;;
    BSD|0BSD|ISC) echo "700 1700" ;;
    CC0-1.0)      echo "6000 7500" ;;
    *)            echo "- -" ;;
  esac
}

# Pure, offline-testable: does this size sit inside the family's band?
band_verdict() {
  local fam="$1" sz="$2" lo hi
  read -r lo hi <<<"$(band_of_family "$fam")"
  [ "$lo" = "-" ] && { printf 'NO-BAND'; return; }
  if [ "$sz" -lt "$lo" ]; then printf 'UNDER'; return; fi
  if [ "$sz" -gt "$hi" ]; then printf 'OVER';  return; fi
  printf 'IN-BAND'
}

if [ "${1:-}" = "--self-test" ]; then
  t=0; p=0
  chk() { t=$((t+1)); if [ "$2" = "$3" ]; then p=$((p+1)); else echo "FAIL $1: got '$2' want '$3'"; fi; }
  chk "canonical MIT in band"      "$(band_verdict MIT 1071)"        IN-BAND
  chk "PageLM MIT is OVER"         "$(band_verdict MIT 8563)"        OVER
  chk "46-byte MIT is UNDER"       "$(band_verdict MIT 46)"          UNDER
  chk "writeAlizer stub is UNDER"  "$(band_verdict MIT 47)"          UNDER
  chk "real Apache in band"        "$(band_verdict Apache-2.0 11348)" IN-BAND
  chk "ECL has no band yet"        "$(band_verdict ECL-2.0 11120)"   NO-BAND
  chk "AGPL has no band yet"       "$(band_verdict AGPL-3.0 33893)"  NO-BAND
  # the control that matters: the band must NOT be the delivery verdict on its own
  chk "boundary lo is in band"     "$(band_verdict MIT 1000)"        IN-BAND
  chk "boundary hi is in band"     "$(band_verdict MIT 1200)"        IN-BAND
  echo "$p/$t"; [ "$p" = "$t" ] || exit 1; exit 0
fi

for slug in "$@"; do
  path="$(awk -F'\t' -v s="$slug" '$1==s{print $2}' result.census.2026-10-14-p195.tsv)"
  [ -z "$path" ] || [ "$path" = "-" ] && continue
  tmp="$(mktemp)"
  code="$(curl -s -L --max-time 25 -o "$tmp" -w '%{http_code}' \
          "https://raw.githubusercontent.com/$slug/HEAD/$path" 2>/dev/null)" || code=000
  if [ "$code" != 200 ]; then rm -f "$tmp"; printf '%s\t%s\t-\t-\tFETCH-%s\t-\tINDETERMINATE\n' "$slug" "$path" "$code"; continue; fi
  sz="$(size_of_file "$tmp")"; fam="$(family_of_file "$tmp")"
  bv="$(band_verdict "$fam" "$sz")"
  body="$(cat "$tmp")"
  if commercial_use_ok "$body"; then cax=ALLOWED; else cax=PROHIBITED; fi
  # DELIVERY: the band is a TRIGGER TO READ, never a verdict by itself.
  if [ "$cax" = PROHIBITED ]; then del=BARRED
  elif [ "$bv" = IN-BAND ]; then del=GO
  elif [ "$bv" = NO-BAND ]; then del=GO-SUBJECT-TO-FAMILY
  else del=MUST-READ-BODY; fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$path" "$sz" "$fam" "$bv" "$cax" "$del"
  rm -f "$tmp"
done
