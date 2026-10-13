#!/bin/bash
# ACTION JO (p172) — HOSTILE detection on the TITLE BLOCK, per P237/P171.
# p172's own first attempt used a phrase search for withholding language and produced 34 raw
# hits, of which 26 were Apache-2.0 and LGPL bodies. T224 re-fired on p172's instrument.
set -u
DIR="$1"
printf 'file\tsha256_12\tproprietary_class\n'
for f in "$DIR"/*.txt "$DIR"/*.html; do
  [ -f "$f" ] || continue
  b=$(basename "$f"); t=$(head -40 "$f" | tr -s ' \t\n' ' ')
  c=OPEN
  printf '%s' "$t" | grep -qi 'Binary Code License Agreement' && c=SUN-BCL
  printf '%s' "$t" | grep -qi 'SOFTWARE LICENSE AGREEMENT and ENTITLEMENT' && c=SUN-ENTITLEMENT
  printf '%s' "$t" | grep -qi 'WILLING TO LICENSE THIS SPECIFICATION TO YOU' && c=SUN-SPEC-CLICKTHROUGH
  printf '%s' "$t" | grep -qi 'personal, non-exclusive, non-transferable license to use one copy' && c=PROPRIETARY-SINGLE-SEAT
  printf '%s\t%s\t%s\n' "$b" "$(sha256sum "$f"|cut -c1-12)" "$c"
done
