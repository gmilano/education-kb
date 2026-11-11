#!/bin/bash
# repo.sh owner/name... -> authoritative metadata via search (repos/ endpoint is scoped-blocked)
for R in "$@"; do
  gh api -X GET search/repositories -f q="repo:$R" -f per_page=1 2>/dev/null | python3 -I -c "
import json,sys
d=json.load(sys.stdin)
it=d.get('items') or []
if not it: print('  %-54s NOT-FOUND-VIA-SEARCH' % '$R'); raise SystemExit
i=it[0]
lic=(i.get('license') or {}).get('spdx_id')
print('  %-54s %7d  %-14s %-10s %s %s' % (i['full_name'], i['stargazers_count'], lic, i['default_branch'], i['pushed_at'][:10], 'ARCHIVED' if i['archived'] else ''))
"
done
