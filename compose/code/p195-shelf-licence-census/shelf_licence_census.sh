# ACTION P195-A — read the licence from BYTES for every LIVE slug on the shelf, via the raw lane.
#
# Pre-registered by p194: "Read licences from bytes for the remaining ~430 shelf slugs via the
# raw lane. Limb 1: the lane scales -> the whole shelf gets a byte-verified licence column.
# Limb 2: rate-limited or 404-noisy at volume -> the lane is a spot tool, not a census tool."
#
# DOCTRINE OBSERVED, because this KB has already paid for each of these:
#   P237 / lib/README.md  — a licence classifier is NOT forked to be fixed.  We source
#                           lib/payload_measure.sh, which sources lib/license_family.sh (P171,
#                           title-block classification, 207/207 today).  No inline classifier.
#   P834                  — no byte count is published from $(...).  size_of_file only.
#   P126-2                — a NEGATIVE verdict needs a negative control.  "NONE" is only
#                           emitted when the FULL ladder returned 404 and NOTHING returned a
#                           refusal/throttle code.  Any 403/429/5xx in the ladder makes the
#                           slug INDETERMINATE, never NONE.  p194 read "all 404" as "no
#                           licence" over 19 probes on 4 slugs; at census volume that
#                           inference is exactly what rate limiting would forge.
#
# Emits TSV on stdout: slug  licence_path  bytes  family  probes  worst_http  verdict

set -u

_HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$_HERE/../lib/payload_measure.sh"

# Frequency-ordered, so a hit costs 1-3 calls.  Still the FULL 19 of p194 before "NONE".
LADDER="LICENSE LICENSE.md LICENSE.txt COPYING license.txt LICENCE LICENSE.rst LICENCE.md \
license license.md licence.txt COPYING.txt COPYRIGHT NOTICE MIT-LICENSE MIT-LICENSE.txt \
LICENSE-MIT LICENSE-APACHE UNLICENSE"

RAW_BASE="${RAW_BASE:-https://raw.githubusercontent.com}"

# Pure: given the ladder outcome, decide the verdict.  Offline-testable, no network.
# $1 = licence_path ("" if none hit)  $2 = worst non-404 http seen ("" if none)
verdict_of() {
  local hit="$1" worst="$2"
  if [ -n "$hit" ]; then printf 'FOUND'; return 0; fi
  case "$worst" in
    ''|000) printf 'NONE' ;;
    *)      printf 'INDETERMINATE' ;;
  esac
}

# Is this http code a refusal/throttle that poisons a NONE verdict?
poisons_none() {
  case "$1" in
    404) return 1 ;;
    200) return 1 ;;
    *)   return 0 ;;
  esac
}

census_one() {
  local slug="$1" tmp fn code hit='' bytes=0 family='' probes=0 worst=''
  tmp="$(mktemp)"
  for fn in $LADDER; do
    probes=$((probes+1))
    code="$(curl -s -L --max-time 25 -o "$tmp" -w '%{http_code}' \
            "$RAW_BASE/$slug/HEAD/$fn" 2>/dev/null)" || code=000
    if [ "$code" = 200 ]; then hit="$fn"; break; fi
    if poisons_none "$code"; then worst="$code"; fi
  done
  if [ -n "$hit" ]; then
    bytes="$(size_of_file "$tmp")"       # P834: from the FILE, never from a capture
    family="$(family_of_file "$tmp")"    # P171/P237: the hardened classifier, not a new one
  fi
  rm -f "$tmp"
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "${hit:--}" "$bytes" "${family:--}" "$probes" "${worst:--}" "$(verdict_of "$hit" "$worst")"
}

if [ "${1:-}" = "--one" ]; then census_one "$2"; exit 0; fi
if [ "${1:-}" = "--self-test" ]; then
  # negative controls first: the verdict function must NOT say NONE under a refusal
  t=0; p=0
  chk() { t=$((t+1)); if [ "$2" = "$3" ]; then p=$((p+1)); else echo "FAIL $1: got '$2' want '$3'"; fi; }
  chk "hit wins over refusal"      "$(verdict_of LICENSE 429)"  FOUND
  chk "clean miss is NONE"         "$(verdict_of '' '')"        NONE
  chk "000 is still NONE-able"     "$(verdict_of '' 000)"       NONE
  chk "429 poisons NONE"           "$(verdict_of '' 429)"       INDETERMINATE
  chk "403 poisons NONE"           "$(verdict_of '' 403)"       INDETERMINATE
  chk "500 poisons NONE"           "$(verdict_of '' 500)"       INDETERMINATE
  poisons_none 404 && chk "404 benign" poisoned benign || chk "404 benign" benign benign
  poisons_none 200 && chk "200 benign" poisoned benign || chk "200 benign" benign benign
  poisons_none 429 && chk "429 poisons" poisons poisons || chk "429 poisons" benign poisons
  echo "$p/$t"
  [ "$p" = "$t" ] || exit 1
  exit 0
fi
echo "usage: shelf_licence_census.sh --one <slug> | --self-test" >&2; exit 2
