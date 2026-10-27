#!/bin/bash
# p487 — SHA-pinned licence reader. Closes Gap 486-B: a fingerprint taken at a
# branch ref measures whatever the branch pointed at, at an unrecorded moment.
# This resolves HEAD to a COMMIT SHA first, then reads the payload AT THAT SHA.
# Every fingerprint it emits is therefore reproducible by a third party.
set -u
printf 'slug\tdefault_ref\tcommit_sha\tfile\thttp\tbytes\tsha256_12\tfamily\n'
for slug in "$@"; do
  # stage 1: existence + default ref + commit SHA (the discriminating oracle;
  # curl -sI is 403 for real and fabricated slugs alike, measured p450/p487)
  ref_out=$(timeout 45 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$ref_out" ]; then
    printf '%s\t-\t-\t-\tUNREACHABLE\t-\t-\t-\n' "$slug"; continue
  fi
  dref=$(printf '%s' "$ref_out" | awk '/^ref:/{print $2; exit}')
  csha=$(printf '%s' "$ref_out" | awk '!/^ref:/{print $1; exit}')
  found=0
  for f in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING LICENSE-MIT; do
    url="https://raw.githubusercontent.com/$slug/$csha/$f"
    out=$(timeout 45 curl -sS -o /tmp/claude-0/p487/.body -w '%{http_code} %{size_download}' "$url" 2>/dev/null)
    code=${out%% *}; size=${out##* }
    [ "$code" != "200" ] && continue
    # a 404 can arrive as a 200-shaped 14-byte body: d5558cd419c8 is the named
    # REFUSAL fingerprint (p256/p257). Gate on BOTH code and body.
    h=$(sha256sum /tmp/claude-0/p487/.body | cut -c1-12)
    [ "$h" = "d5558cd419c8" ] && continue
    low=$(tr 'A-Z' 'a-z' < /tmp/claude-0/p487/.body)
    # order matters: "gnu lesser" is tested BEFORE "gnu general public",
    # and AGPL before GPL, else GPLv3's closing paragraph mis-grades (p450)
    if   printf '%s' "$low" | grep -q 'gnu affero'; then fam=AGPL
    elif printf '%s' "$low" | grep -q 'gnu lesser';  then fam=LGPL
    elif printf '%s' "$low" | grep -q 'gnu general public'; then fam=GPL
    elif printf '%s' "$low" | grep -q 'apache license'; then fam=Apache-2.0
    elif printf '%s' "$low" | grep -q 'mozilla public'; then fam=MPL
    elif printf '%s' "$low" | grep -q 'redistributions of source code'; then fam=BSD
    elif printf '%s' "$low" | grep -q 'permission is hereby granted, free of charge'; then fam=MIT
    elif printf '%s' "$low" | grep -q 'creative commons'; then fam=CC
    else fam=UNCLASSIFIED; fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$dref" "${csha:0:12}" "$f" "$code" "$size" "$h" "$fam"
    found=1; break
  done
  [ "$found" = 0 ] && printf '%s\t%s\t%s\t-\tNO_LICENCE_FILE\t-\t-\tNONE\n' "$slug" "$dref" "${csha:0:12}"
done
