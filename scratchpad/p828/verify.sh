#!/bin/bash
# p828 verification harness.
# Channel A: gh api search/repositories repo: -> existence + metadata (bidirectional control: live=1, invented=HTTP422)
# Channel B: raw.githubusercontent byte-read of LICENSE -> ACTUAL grant text (T27: the field lies in both directions)
out=verified2.tsv
printf 'slug\texists\tfield_lic\tstars\tforks\tpushed\tcreated\tfork\tbytes_lic\tsha\tsize\tdesc\n' > $out
while read -r slug; do
  [ -z "$slug" ] && continue
  meta=$(timeout 45 gh api -X GET search/repositories -f q="repo:$slug" \
    --jq '.total_count as $t | if $t==0 then "0\t-\t-\t-\t-\t-\t-\t-" else (.items[0] | [$t,(.license.spdx_id // "NONE"),.stargazers_count,.forks_count,(.pushed_at|.[0:10]),(.created_at|.[0:10]),(.fork|tostring),((.description // "")|gsub("[\t\n]";" ")|.[0:150])]|join("\t")) end' 2>/dev/null)
  if [ -z "$meta" ]; then meta="422-NOTFOUND\t-\t-\t-\t-\t-\t-\t-"; fi
  blic="-"; sha="-"; size="-"
  for br in main master; do
    for fn in LICENSE LICENSE.md LICENSE.txt COPYING LICENCE; do
      body=$(timeout 25 curl -sfL "https://raw.githubusercontent.com/$slug/$br/$fn" 2>/dev/null)
      if [ -n "$body" ]; then
        size=$(printf '%s' "$body" | wc -c | tr -d ' ')
        sha=$(printf '%s' "$body" | sha256sum | cut -c1-12)
        if   printf '%s' "$body" | grep -qi 'Apache License'; then blic=Apache-2.0
        elif printf '%s' "$body" | grep -qi 'GNU AFFERO'; then blic=AGPL-3.0
        elif printf '%s' "$body" | grep -qi 'GNU LESSER'; then blic=LGPL
        elif printf '%s' "$body" | grep -qi 'GNU GENERAL PUBLIC'; then blic=GPL
        elif printf '%s' "$body" | grep -qi 'Mozilla Public License'; then blic=MPL-2.0
        elif printf '%s' "$body" | grep -qi 'PolyForm'; then blic=POLYFORM-NONCOMMERCIAL
        elif printf '%s' "$body" | grep -qi 'Business Source License'; then blic=BUSL
        elif printf '%s' "$body" | grep -qi 'NonCommercial\|Creative Commons'; then blic=CC
        elif printf '%s' "$body" | grep -qi 'Permission is hereby granted, free of charge'; then
             if printf '%s' "$body" | grep -qi 'BUT NOT LIMITED TO THE WARRANTIES'; then blic=MIT; else blic=MIT-MODIFIED; fi
        elif printf '%s' "$body" | grep -qi 'Redistribution and use in source and binary'; then blic=BSD
        else blic=UNRECOGNISED; fi
        break 2
      fi
    done
  done
  printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$meta" "$blic" "$sha" "$size" >> $out
done < cands.txt
