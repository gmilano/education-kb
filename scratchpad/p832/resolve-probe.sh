#!/bin/bash
# p832 D832-1 REPAIR: resolve the BRANCH from the ref set before probing filenames.
# p773/grantprobe.sh takes the branch as a caller argument and has no resolution step,
# so one wrong branch nils all 31 filename paths and reads as a true absence.
slug="$1"
refs=$(timeout 30 git ls-remote --heads "https://github.com/$slug" 2>/dev/null | sed 's|.*refs/heads/||')
if [ -z "$refs" ]; then printf '%s\tNO-REFS\t-\t-\t-\n' "$slug"; return 2>/dev/null || exit 0; fi
# probe the plausible roots first, then every remaining head (bounded)
ordered=$( { echo "$refs" | grep -xE 'main|master|develop|dev|trunk'; echo "$refs"; } | awk '!seen[$0]++' | head -6 )
for br in $ordered; do
  out=$(bash /home/user/education-kb/compose/code/p773/grantprobe.sh "$slug" "$br" 2>/dev/null)
  if ! echo "$out" | grep -q 'NO-GRANT-AT-ROOT'; then
    printf '%s\t%s\n' "$(echo "$out" | cut -f2-4 | tr '\t' '\t')" "$br" | sed "s|^|$slug\t|"; exit 0
  fi
done
printf '%s\tNO-GRANT-AT-ROOT\t-\t-\t%s\n' "$slug" "$(echo "$ordered"|tr '\n' ',' )"
