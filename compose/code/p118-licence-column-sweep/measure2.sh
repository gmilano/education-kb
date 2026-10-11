#!/usr/bin/env bash
# P118 ACTION E, measurement v2. Reads the licence file from the repository's
# DEFAULT branch (resolved over the git transport by defaultbranch.sh) and
# classifies it with classify2.sh.
#
# Why the default branch matters, measured rather than assumed: 37 of these 249
# addresses default to neither `main` nor `master`, and five default to a
# TAG-SHAPED ref (v31.0.00, 19.0, 2.12, v6.2.0, v3.0.x-develop) that no
# main/master/develop probe reaches at all. v1 of this instrument, and p117's
# licence.sh before it, read whichever candidate answered FIRST -- which on
# frappe/frappe is a stale `master` carrying an MIT file while `develop`, the
# branch the project actually ships, carries GPL-3.0.
set -u
slug="$1"; br="$2"; STREAMDIR="${3:-streams2}"
mkdir -p "$STREAMDIR"
safe=$(printf '%s' "$slug" | tr '/' '%')
for p in LICENSE LICENSE.txt LICENSE.md LICENCE LICENCE.txt COPYING COPYING.txt license.txt LICENSE-MIT; do
  f="$STREAMDIR/$safe@$br@$(printf '%s' "$p" | tr '/' '%')"
  code=$(curl -sS -o "$f" -w '%{http_code}' --max-time 20 \
    "https://raw.githubusercontent.com/$slug/$br/$p" 2>/dev/null || echo 000)
  if [ "$code" != "200" ] || [ ! -s "$f" ]; then rm -f "$f"; continue; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$p" "$(./classify2.sh "$f")" "$(wc -c < "$f" | tr -d ' ')"
  exit 0
done
printf '%s\t%s\t-\tNO-LICENCE-FILE\t0\n' "$slug" "$br"
