#!/usr/bin/env bash
# P121 verification probe. Re-reads the licence of each ACTION P defect address
# from the LIVE tree via raw.githubusercontent.com (github.com and api.github.com
# are both 403 from this runner -- see P117-A on transport x endpoint).
# Nothing here trusts p118's or p120's recorded verdict: the point is to confirm
# the defect against the tree at THIS pass's timestamp.
set -u
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md license license.md license.txt
       COPYING COPYING.txt LICENSE-MIT LICENSE.rst docs/License.txt .github/LICENSE"
while IFS=$'\t' read -r slug branch; do
  [ -z "${slug:-}" ] && continue
  hit=""
  for p in $PATHS; do
    u="https://raw.githubusercontent.com/$slug/$branch/$p"
    code=$(curl -sS -o "/tmp/p121.body" -w '%{http_code}' --max-time 25 "$u" 2>/dev/null || echo 000)
    if [ "$code" = "200" ]; then
      sz=$(wc -c < /tmp/p121.body)
      title=$(head -c 3000 /tmp/p121.body | tr -d '\r' | grep -m1 -oiE 'GNU AFFERO GENERAL PUBLIC LICENSE|GNU GENERAL PUBLIC LICENSE|GNU LESSER GENERAL PUBLIC LICENSE|Apache License|MIT License|The MIT License|BSD [0-9]-Clause|Mozilla Public License|Educational Community License|CC0 1\.0|Creative Commons|Elastic License|License: GNU GPL V3|保留所有权利' || echo '-')
      ver=$(head -c 3000 /tmp/p121.body | grep -m1 -oE 'Version [0-9]+(\.[0-9]+)?' || echo '')
      printf '%s\t%s\t%s\t200\t%s\t%s %s\n' "$slug" "$branch" "$p" "$sz" "$title" "$ver"
      hit=1; break
    fi
  done
  [ -z "$hit" ] && printf '%s\t%s\t-\tNONE\t0\tno licence file at %s probed paths\n' "$slug" "$branch" "$(echo $PATHS|wc -w)"
done
