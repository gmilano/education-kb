#!/usr/bin/env bash
# p869 -- 868-G4: enumerate the XBlock INTEGRATOR estate by OWNER, the way p867
# enumerated the PLATFORM estate by platform.  p867's platform split was
# 71 AGPL-3.0 / 21 Apache-2.0 / 1 BSD-3-Clause; a materially different split on the
# integrator side is itself the finding.
# THROTTLED at 4s between requests, deliberately: p869 measured that an unthrottled
# batch of 134 single-repo probes manufactured 23 false absences (23/23 resolved on
# retry), so an un-paced sweep would under-report this estate and look like a result.
set -u
printf 'owner\taddress\tlicence\tstars\tpushed\tarchived\tlanguage\n'
for owner in "$@"; do
  page=1
  while [ "$page" -le 3 ]; do
    sleep 4
    raw=$(gh api -X GET search/repositories -f q="user:$owner" -f per_page=100 -f page="$page" 2>/dev/null)
    n=$(printf '%s' "$raw" | jq -r '(.items|length) // 0' 2>/dev/null)
    case "$n" in ''|0) break ;; esac
    printf '%s' "$raw" | jq -r --arg o "$owner" '.items[] |
      [$o, .full_name, (.license.spdx_id // "NONE"), (.stargazers_count|tostring),
       (.pushed_at[0:10]), (.archived|tostring), (.language // "null")] | @tsv' 2>/dev/null
    [ "$n" -lt 100 ] && break
    page=$((page+1))
  done
done
