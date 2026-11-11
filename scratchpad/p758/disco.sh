#!/bin/bash
# p758 discovery: register-shaped searches on the live search channel (T521/T418 instrument)
q() {
  echo "### QUERY: $1"
  gh api -X GET search/repositories -f q="$1" -f sort=stars -f order=desc -f per_page=12 2>/dev/null \
  | python3 -I -c "
import json,sys
try: d=json.load(sys.stdin)
except Exception as e: print('  ERR',e); raise SystemExit
print('  total_count',d.get('total_count'))
for i in d.get('items',[]):
    lic=(i.get('license') or {}).get('spdx_id')
    print('  %-52s %8d  %-16s %-10s %s %s' % (i['full_name'], i['stargazers_count'], lic, i['default_branch'], i['pushed_at'][:10], 'ARCHIVED' if i['archived'] else ''))
"
}
for Q in "$@"; do q "$Q"; done
