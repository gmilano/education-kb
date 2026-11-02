#!/bin/bash
# p610 grant harness: existence (606-E) -> real default branch -> grant byte-read -> size
# controls: a fabricated sibling for every real address
printf 'slug\texist\tbranch\tgrant_path\tcode\tbytes\tfamily\n'
while read -r s; do
  [ -z "$s" ] && continue
  ex=$(curl -s -o /dev/null -w '%{http_code}' --max-time 25 "https://github.com/$s/info/refs?service=git-upload-pack")
  if [ "$ex" != "200" ]; then printf '%s\t%s\t-\t-\t-\t-\tABSENT\n' "$s" "$ex"; continue; fi
  br=$(gh api -X GET search/repositories -f q="repo:$s" --jq '.items[0].default_branch' 2>/dev/null)
  [ -z "$br" ] || [ "$br" = "null" ] && br=$(git ls-remote --symref "https://github.com/$s" HEAD 2>/dev/null | awk '/^ref:/{sub("refs/heads/","",$2);print $2}')
  [ -z "$br" ] && br=main
  found=0
  for p in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.txt COPYING COPYING.txt LICENSE-APACHE LICENSE-MIT LICENSE.rst license; do
    r=$(curl -s -w '\n%{http_code}|%{size_download}' --max-time 25 "https://raw.githubusercontent.com/$s/$br/$p")
    code=$(echo "$r" | tail -1 | cut -d'|' -f1); byt=$(echo "$r" | tail -1 | cut -d'|' -f2)
    if [ "$code" = "200" ] && [ "$byt" -gt 100 ]; then
      body=$(echo "$r" | head -n -1)
      fam=UNKNOWN
      echo "$body" | grep -qi 'Apache License' && fam=Apache-2.0
      echo "$body" | grep -qi 'MIT License' && fam=MIT
      echo "$body" | grep -q 'Permission is hereby granted, free of charge' && fam=MIT
      echo "$body" | grep -qi 'Redistributions of source code must retain' && { echo "$body" | grep -qi 'Neither the name' && fam=BSD-3-Clause || fam=BSD-2-Clause; }
      echo "$body" | grep -qi 'GNU GENERAL PUBLIC LICENSE' && fam=GPL
      echo "$body" | grep -qi 'GNU AFFERO' && fam=AGPL
      echo "$body" | grep -qi 'GNU LESSER' && fam=LGPL
      echo "$body" | grep -qi 'Mozilla Public License' && fam=MPL-2.0
      echo "$body" | grep -qi 'Creative Commons' && fam=CC
      echo "$body" | grep -qi 'ISC License' && fam=ISC
      printf '%s\t200\t%s\t%s\t%s\t%s\t%s\n' "$s" "$br" "$p" "$code" "$byt" "$fam"
      found=1; break
    fi
  done
  [ "$found" = 0 ] && printf '%s\t200\t%s\t-\t404\t-\tNO-GRANT\n' "$s" "$br"
done
