#!/usr/bin/env bash
# p870 -- 869-G3: collect BOTH trend veins in p868-org-sweep.sh's schema, so p868's committed
# DOMAIN PREDICATE can score them without being re-written for this pass.  The comparison the
# gap asks for is only meaningful if the same predicate judges both veins.
#   arm 1  push-recency, keyed on OWNER   (user:<owner> pushed:>SINCE)
#   arm 2  star-ranked, keyed on KEYWORD  (<terms> pushed:>SINCE, sort=stars)
# Throttled at 4s per request BY CONSTRUCTION (p869's false-absence measurement).
set -u
SINCE="${1:?usage: p870-vein-sweep.sh SINCE_YYYY-MM-DD}"
emit() { # $1=vein label
  jq -r --arg v "$1" 'if (.total_count // 0)==0 then empty else .items[]? |
      [$v, .full_name, (.owner.type // "-"), (.stargazers_count|tostring),
       (.forks_count|tostring), ((.license.spdx_id)//"NONE"), (.pushed_at[0:10]),
       (.archived|tostring), ((.default_branch)//"-"),
       ((.description)//"-"|gsub("[\t\n\r]";" ")),
       ((.topics // [])|join(","))] | @tsv end' 2>/dev/null
}
printf 'vein\taddress\towner_type\tstars\tforks\tlicence\tpushed\tarchived\tdefault_branch\tdescription\ttopics\n'
for o in open-craft eduNEXT raccoongang edly-io cmmedu openfun IONISx openedxou collabassess Abstract-Tech openedx overhangio edx mitodl; do
  for page in 1 2; do
    sleep 4
    gh api -X GET search/repositories -f q="user:$o pushed:>$SINCE" -f per_page=100 -f page="$page" -f sort=updated 2>/dev/null | emit "push-recency"
  done
done
while IFS= read -r q; do
  [ -z "$q" ] && continue
  sleep 4
  gh api -X GET search/repositories -f q="$q pushed:>$SINCE" -f per_page=100 -f sort=stars -f order=desc 2>/dev/null | emit "star-ranked"
done <<'QQ'
education AI agent
tutoring AI
lms openedx
learning platform AI
xblock
edtech AI
QQ
