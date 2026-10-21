#!/bin/bash
# `p349-name-collision/canonical_address.sh` — WHICH address is the canonical one.
#
# The HEAD-equality run answers "these two addresses are one repository" and then stops,
# and p348's reading of that answer — "two rows, one project, a denominator error" —
# turns out to be only half of it.  GitHub keeps EVERY former address of a transferred or
# renamed repository answering forever, by redirect.  So an alias group is normally not
# two projects and not even two addresses in use: it is ONE repository plus the addresses
# it used to have, all of which still resolve, clone and serve raw payloads.
#
# 🔴 That is why a stale address on a shelf never looks stale: it answers.  The canonical
# name has moved and the KB's row has not, and nothing in the HEAD-equality channel says
# which of the two is current.
#
# 🟢 The HTML address does say, with a 301 and a `location:` header.  An address that
# answers 200 is canonical; one that answers 301 names its successor.
#
#   canonical_address.sh <addresses-file>  -> TSV: address  code  canonical
set -uo pipefail
IN="${1:?usage: canonical_address.sh <addresses-file>}"
printf 'address\tcode\tcanonical\n'
while read -r addr; do
  [ -z "${addr:-}" ] && continue
  out="$(curl -sS -o /dev/null --max-time 30 -w '%{http_code}\t%{redirect_url}' \
         "https://github.com/$addr" 2>/dev/null || echo -e "000\t-")"
  code="${out%%$'\t'*}"; loc="${out#*$'\t'}"
  case "$code" in
    200) printf '%s\t200\tSELF\n' "$addr" ;;
    30*) printf '%s\t%s\t%s\n' "$addr" "$code" "${loc#https://github.com/}" ;;
    *)   printf '%s\t%s\tUNRESOLVED\n' "$addr" "$code" ;;
  esac
done < "$IN"
