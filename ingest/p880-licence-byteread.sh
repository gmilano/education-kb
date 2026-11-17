#!/usr/bin/env bash
# p880 — byte-read a repository's licence.  `spdx_id` screens; BYTES decide.
#
# Built because p880's first cut of this read got TWO repositories wrong, and both
# misses are now controls:
#
#   🔴 frappe/education — reported NO-LICENCE-FILE-FOUND.  False.  Its default branch
#      is `develop` (not main/master) and its licence file is lowercase `license.txt`.
#      An absence claim is only as good as the filename list behind it, so this script
#      resolves the DEFAULT BRANCH from the search index first and carries a wider,
#      case-varied filename list.
#   🔴 apereo/java-cas-client — classified BSD-family on a first-match grep.  False, or
#      rather half-true: the payload carries an Apache-2.0 notice AND a separate JA-SIG
#      BSD-3-Clause "License for Use".  A first-match classifier reports whichever
#      family it happens to hit.  Families are now detected CUMULATIVELY and a payload
#      with more than one is reported CONJUNCTIVE (cf. p427's gate), never collapsed.
#
#   🔴 THIRD defect, and the one that would have been worst to publish: the first cut emitted
#      MD5.  This corpus hashes licence payloads with SHA-256 truncated to 12 hex characters, and
#      every `8,241 B · 528f84036800`-style cell already on these shelves is sha256.  An md5 column
#      at the same byte count reads as a CONTRADICTION of a row that actually agrees with it: the
#      first run appeared to disagree with the base on frappe/education and openeducat_erp, and the
#      bytes were identical in both cases.  A hash is only evidence against the same algorithm.
#
# Usage: p880-licence-byteread.sh OUT.tsv slug [slug ...]
set -uo pipefail
OUT="${1:?usage: p880-licence-byteread.sh OUT.tsv slug [slug...]}"; shift
D=$(mktemp -d)
trap 'rm -rf "$D"' EXIT

NAMES=(LICENSE LICENSE.txt LICENSE.md LICENSE.TXT LICENCE LICENCE.txt COPYING COPYING.txt
       license license.txt license.md licence licence.txt LICENSE.rst LICENSE-MIT LICENSE-APACHE)

printf 'repo\tdefault_branch\tbranch\tpath\thttp\tbytes\tsha256_12\tfamilies\tverdict\tnote\n' > "$OUT"

for slug in "$@"; do
  # the default branch is a FACT to look up, not a guess to iterate over
  db=$(gh api -X GET search/repositories -f q="repo:$slug" \
        --jq '.items[0].default_branch // ""' 2>/dev/null)
  sleep 2
  branches=()
  [ -n "$db" ] && branches+=("$db")
  for b in main master develop; do [ "$b" != "$db" ] && branches+=("$b"); done

  found=0
  for br in "${branches[@]}"; do
    for f in "${NAMES[@]}"; do
      code=$(curl -sS -o "$D/x" -w '%{http_code}' \
             "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
      [ "$code" = "200" ] || continue
      b=$(wc -c < "$D/x" | tr -d ' '); m=$(sha256sum "$D/x" | cut -c1-12)

      # CUMULATIVE family detection — a payload may carry more than one grant
      fam=()
      grep -qi "Apache License" "$D/x"                                   && fam+=("Apache-2.0")
      grep -q  "Permission is hereby granted, free of charge" "$D/x"     && fam+=("MIT")
      grep -qi "Redistribution and use in source and binary" "$D/x"     && fam+=("BSD")
      grep -qi "GNU AFFERO GENERAL PUBLIC LICENSE" "$D/x"               && fam+=("AGPL-3.0")
      grep -qi "GNU LESSER GENERAL PUBLIC LICENSE" "$D/x"               && fam+=("LGPL")
      if grep -qi "GNU GENERAL PUBLIC LICENSE" "$D/x" \
         && ! grep -qi "AFFERO\|LESSER" "$D/x"; then fam+=("GPL"); fi
      grep -qi "Mozilla Public License" "$D/x"                          && fam+=("MPL")

      note=""
      if [ "${#fam[@]}" -eq 0 ]; then
        v="UNKNOWN-TEMPLATE"
        # a grant may be DECLARED without any licence text at all
        if [ "$b" -lt 200 ] && grep -qiE "GPL|MIT|Apache|BSD" "$D/x"; then
          v="DECLARATION-ONLY"
          note="$b B, names a licence but carries NO licence text: $(tr -d '\n' < "$D/x" | cut -c1-60)"
        fi
      elif [ "${#fam[@]}" -eq 1 ]; then
        v="${fam[0]}"
      else
        v="CONJUNCTIVE"
        note="two or more LIVE families in one payload — notice obligation of ${#fam[@]}"
      fi
      printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
        "$slug" "${db:-?}" "$br" "$f" "$code" "$b" "$m" \
        "$(IFS=+; echo "${fam[*]:-none}")" "$v" "$note" >> "$OUT"
      found=1; break 2
    done
  done
  [ $found -eq 0 ] && printf '%s\t%s\t-\t-\t404\t0\t-\tnone\tNO-LICENCE-FILE-FOUND\tsearched %d names over %d branches\n' \
      "$slug" "${db:-?}" "${#NAMES[@]}" "${#branches[@]}" >> "$OUT"
done
cat "$OUT"
