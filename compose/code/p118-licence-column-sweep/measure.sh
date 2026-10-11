#!/usr/bin/env bash
# P118 ACTION E, measurement layer. One slug per invocation so it can be fanned out.
#
# Identifies a licence by the TITLE LINE of the committed licence file -- p117's
# `P117-K` fix. v1 of p117's classifier matched the PHRASE "GNU Affero General
# Public License", which GPL-3 section 13 merely NAMES, and it mis-read three
# GPL-3 repos as AGPL. A licence is identified by its title, never by a phrase
# one licence uses to name another.
#
# Writes the body to STREAMDIR: the stream is the evidence, the TSV a derivation.
set -u
slug="$1"; STREAMDIR="${2:-streams}"
mkdir -p "$STREAMDIR"
safe=$(printf '%s' "$slug" | tr '/' '%')
for br in main master develop trunk; do
  for p in LICENSE LICENSE.txt LICENSE.md LICENCE LICENCE.txt COPYING COPYING.txt LICENSE-MIT; do
    f="$STREAMDIR/$safe@$br@$p"
    code=$(curl -sS -o "$f" -w '%{http_code}' --max-time 20 \
      "https://raw.githubusercontent.com/$slug/$br/$p" 2>/dev/null || echo 000)
    if [ "$code" != "200" ] || [ ! -s "$f" ]; then rm -f "$f"; continue; fi
    # TITLE LINE: first meaningful line, skipping copyright/version/preamble noise.
    title=$(sed -n '1,14p' "$f" | tr -d '\r' | tr -s ' \t' ' ' \
      | sed 's/^ //;s/ $//' \
      | grep -viE '^$|^copyright|^\(c\)|fsf\.org|gnu\.org|^version |everyone is permitted|^preamble|^all rights reserved' \
      | head -1)
    ver=$(sed -n '1,8p' "$f" | grep -oiE 'Version [0-9]+(\.[0-9]+)?' | head -1 | grep -oE '[0-9]+(\.[0-9]+)?')
    spdx="UNKNOWN"
    lt=$(printf '%s' "$title" | tr 'A-Z' 'a-z')
    case "$lt" in
      *"affero general public license"*) spdx="AGPL-3.0" ;;
      *"lesser general public license"*) spdx="LGPL-${ver:-?}" ;;
      *"general public license"*)        spdx="GPL-${ver:-?}.0" ;;
      *"apache license"*)                spdx="Apache-${ver:-2.0}" ;;
      *"educational community license"*) spdx="ECL-${ver:-2.0}" ;;
      *"mozilla public license"*)        spdx="MPL-${ver:-2.0}" ;;
      *"eclipse public license"*)        spdx="EPL-${ver:-2.0}" ;;
      *"mit license"*|*"the mit license"*) spdx="MIT" ;;
      *"bsd "*|*" bsd"*)                 spdx="BSD" ;;
      *"creative commons"*)              spdx="CC" ;;
      *"unlicense"*)                     spdx="Unlicense" ;;
      *"isc license"*)                   spdx="ISC" ;;
      *)
        # No recognisable title. Fall back to the grant sentence, which is the
        # only other thing that CONFERS rather than cross-references.
        if grep -qi 'permission is hereby granted, free of charge' "$f"; then spdx="MIT"
        elif grep -qi 'redistribution and use in source and binary forms' "$f"; then spdx="BSD"
        fi ;;
    esac
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$p" "$spdx" "$(wc -c < "$f" | tr -d ' ')" "$title"
    exit 0
  done
done
printf '%s\t-\t-\tNO-LICENCE-FILE\t0\t-\n' "$slug"
