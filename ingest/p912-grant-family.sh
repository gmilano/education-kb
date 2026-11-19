#!/usr/bin/env bash
# p912 — grant-family byte-read, corrected supersettof `p880-licence-byteread.sh`.
#
# WHY THIS EXISTS. `ingest/p880-licence-byteread.sh` has been this base's licence AUTHORITY
# since p880 — every `N B · sha256_12` cell on these shelves came from it. p912 ran it over
# five Ethiopian examination repositories and it was wrong on TWO of the five, in opposite
# directions.  Both are reproduced here as controls:
#
#   🔴 FALSE POSITIVE (the serious one).  `Nugestudent2026/EdTech` is the **Boost Software
#      License 1.0**.  p880 reports **MIT**.  Cause: Boost's text contains the exact string
#      `Permission is hereby granted, free of charge, to any person or organization`, and
#      p880's MIT detector greps for `Permission is hereby granted, free of charge`.  Boost
#      is a PREFIX-COLLISION of the MIT trigger phrase.  Every MIT verdict p880 ever emitted
#      over a Boost payload is wrong.  Both grants are permissive, so no commercial
#      conclusion in this base inverts — but the NOTICE obligation differs (Boost 1.0 does
#      not require reproducing the licence for binary-only distribution; MIT does), and this
#      base publishes notice obligations.
#      Fix: specific-before-generic.  Boost is tested BEFORE MIT and suppresses it.
#
#   🔴 FALSE NEGATIVE.  `hasensaramii977-cpu/Grade-12-National-Exam-Training-Model` is
#      **CC0-1.0** (`Creative Commons Legal Code / CC0 1.0 Universal`, 7,048 B).  p880
#      reports `UNKNOWN-TEMPLATE`, because it carries ZERO Creative Commons detectors
#      (`grep -ci 'creative commons\|CC0\|CC-BY' p880-licence-byteread.sh` → 0).
#      🔵 This matters more than one row: `T25` records that education's licence trap has
#      moved to DATA AND CONTENT assets and `T32` that the agent-skill tier is appearing
#      under Creative Commons.  The authority instrument could not read the licence family
#      those two trends are about.
#
# 🔵 In BOTH misses the GitHub `license.spdx_id` field was RIGHT and this base's own
# instrument was WRONG.  `T19` says published licence metadata errs in both directions; it
# does not say the byte-read channel is itself a source of error.  It is.  See `912-F2`.
#
# NOT A SILENT REPLACEMENT.  p880 is left in place and unmodified: 30-odd passes of cells
# were produced by it and `Gap 245`'s rule is that a correction and a re-measurement do not
# ship in one pass.  This script is additive and is the authority for p912's rows only.
# A later pass retires p880 against the two controls below.
set -uo pipefail

OUT="${1:?usage: p912-grant-family.sh OUT.tsv slug [slug ...]}"; shift
# Gap 245 class: refuse empty input rather than emit an empty-but-green result.
if [ "$#" -eq 0 ]; then
  echo "🔴 refusing empty slug list (Gap 245): nothing to measure" >&2
  exit 2
fi

D=$(mktemp -d); trap 'rm -rf "$D"' EXIT

NAMES=(LICENSE LICENSE.txt LICENSE.md LICENSE.TXT LICENCE LICENCE.txt COPYING COPYING.txt
       license license.txt license.md licence licence.txt LICENSE.rst LICENSE-MIT LICENSE-APACHE)

printf 'repo\tdefault_branch\tbranch\tpath\thttp\tbytes\tsha256_12\tfamilies\tverdict\tnote\n' > "$OUT"

for slug in "$@"; do
  db=$(gh api -X GET search/repositories -f q="repo:$slug" \
        --jq '.items[0].default_branch // ""' 2>/dev/null)
  sleep 2
  branches=(); [ -n "$db" ] && branches+=("$db")
  for b in main master develop; do [ "$b" != "$db" ] && branches+=("$b"); done

  found=0
  for br in "${branches[@]}"; do
    for f in "${NAMES[@]}"; do
      code=$(curl -sS -o "$D/x" -w '%{http_code}' \
             "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
      [ "$code" = "200" ] || continue
      bytes=$(wc -c < "$D/x" | tr -d ' '); m=$(sha256sum "$D/x" | cut -c1-12)

      fam=(); note=""
      # --- specific-before-generic.  Boost MUST precede MIT (912-F2 control). ---
      boost=0
      grep -qi "Boost Software License" "$D/x" && { fam+=("BSL-1.0"); boost=1; }
      grep -qi "Apache License" "$D/x"                               && fam+=("Apache-2.0")
      if [ "$boost" -eq 0 ] \
         && grep -q "Permission is hereby granted, free of charge" "$D/x"; then fam+=("MIT"); fi
      grep -qi "Redistribution and use in source and binary" "$D/x"  && fam+=("BSD")
      grep -qi "GNU AFFERO GENERAL PUBLIC LICENSE" "$D/x"            && fam+=("AGPL-3.0")
      grep -qi "GNU LESSER GENERAL PUBLIC LICENSE" "$D/x"            && fam+=("LGPL")
      if grep -qi "GNU GENERAL PUBLIC LICENSE" "$D/x" \
         && ! grep -qi "AFFERO\|LESSER" "$D/x"; then fam+=("GPL"); fi
      grep -qi "Mozilla Public License" "$D/x"                       && fam+=("MPL")
      grep -qi "Permission to use, copy, modify, and.*distribute this software" "$D/x" \
        && fam+=("ISC")
      grep -qi "This is free and unencumbered software released into the public domain" "$D/x" \
        && fam+=("Unlicense")
      # --- the family p880 could not see at all (T25, T32). ---
      if grep -qi "CC0 1.0 Universal" "$D/x"; then fam+=("CC0-1.0")
      elif grep -qi "Creative Commons Attribution-ShareAlike" "$D/x"; then fam+=("CC-BY-SA")
      elif grep -qi "Creative Commons Attribution-NonCommercial" "$D/x"; then fam+=("CC-BY-NC")
      elif grep -qi "Creative Commons Attribution" "$D/x"; then fam+=("CC-BY")
      elif grep -qi "Creative Commons" "$D/x"; then fam+=("CC-UNSPECIFIED"); fi

      if [ "${#fam[@]}" -eq 0 ]; then
        v="UNKNOWN-TEMPLATE"
        if [ "$bytes" -lt 200 ] && grep -qiE "GPL|MIT|Apache|BSD" "$D/x"; then
          v="DECLARATION-ONLY"
          note="$bytes B, names a licence but carries NO licence text: $(tr -d '\n' < "$D/x" | cut -c1-60)"
        fi
      elif [ "${#fam[@]}" -eq 1 ]; then
        v="${fam[0]}"
        # a CC grant on a CODE repository is a flag, not a verdict
        case "$v" in CC-*|CC0-*) note="Creative Commons grant — content licence, read scope before building on it" ;; esac
      else
        v="CONJUNCTIVE"
        note="two or more LIVE families in one payload — notice obligation of ${#fam[@]}"
      fi
      printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
        "$slug" "${db:-?}" "$br" "$f" "$code" "$bytes" "$m" \
        "$(IFS=+; echo "${fam[*]:-none}")" "$v" "$note" >> "$OUT"
      found=1; break 2
    done
  done
  [ $found -eq 0 ] && printf '%s\t%s\t-\t-\t404\t0\t-\tnone\tNO-LICENCE-FILE-FOUND\tsearched %d names over %d branches\n' \
      "$slug" "${db:-?}" "${#NAMES[@]}" "${#branches[@]}" >> "$OUT"
done
cat "$OUT"
