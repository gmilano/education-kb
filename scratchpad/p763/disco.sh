#!/bin/bash
# p763 discovery: education-data-warehouse / statutory-return register
q() {
  echo "### QUERY: $1"
  gh api -X GET search/repositories -f q="$1" -f sort=stars -f order=desc -f per_page=10 2>/dev/null \
  | python3 -I -c "
import json,sys
try: d=json.load(sys.stdin)
except Exception as e: print('  ERR',e); raise SystemExit
print('  total_count',d.get('total_count'))
for i in d.get('items',[]):
    lic=(i.get('license') or {}).get('spdx_id')
    print('  %-50s %7d  %-14s %-9s %s %s' % (i['full_name'], i['stargazers_count'], lic, i['default_branch'], i['pushed_at'][:10], 'ARCHIVED' if i['archived'] else ''))
"
}
for Q in "$@"; do q "$Q"; done
