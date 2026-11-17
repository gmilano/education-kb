#!/usr/bin/env bash
# p870 -- 869-G3: a PUSH-RECENCY trend vein keyed on OWNER rather than stars.
#
# 869-G3's measurement: 8 of the 9 permissive XBlocks p869 found were pushed within 4 days of
# the filing and 0 of them had more than 3 stars, so a star-ranked sweep CANNOT see the estate
# institutions have already paid integrators to build.  This vein asks the index the other
# question: who pushed, not who is popular.
#
# Throttled at 4s per request BY CONSTRUCTION -- p869 measured that an unpaced sweep returns
# false absences (23 of 23 resolved on retry), so an unthrottled trend sweep under-reports the
# estate and looks exactly like a result.
set -u
SINCE="${2:?usage: p870-push-recency.sh OWNERFILE SINCE_YYYY-MM-DD}"
printf 'vein\towner\taddress\tlicence\tstars\tpushed\tlanguage\n'
while IFS= read -r o; do
  [ -z "$o" ] && continue
  for page in 1 2; do
    sleep 4
    gh api -X GET search/repositories \
      -f q="user:$o pushed:>$SINCE" -f per_page=100 -f page="$page" -f sort=updated 2>/dev/null \
    | jq -r --arg o "$o" '
        if (.total_count // 0) == 0 then empty
        else .items[]? | "push-recency\t" + $o + "\t" + .full_name + "\t"
             + ((.license.spdx_id) // "NONE") + "\t" + (.stargazers_count|tostring) + "\t"
             + (.pushed_at[0:10]) + "\t" + ((.language) // "null")
        end' 2>/dev/null
  done
done < "$1"
