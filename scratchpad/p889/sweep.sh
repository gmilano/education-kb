#!/bin/bash
# p889 discovery sweep: api.github.com/search/repositories (200 in this session)
OUT=sweep.tsv
: > $OUT
: > sweep.log
while IFS= read -r q; do
  [ -z "$q" ] && continue
  enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")
  code=$(curl -s -w '%{http_code}' -o resp.json "https://api.github.com/search/repositories?q=${enc}&sort=stars&order=desc&per_page=30")
  echo "$code	$q	$(python3 -c "import json;d=json.load(open('resp.json'));print(d.get('total_count','ERR'))" 2>/dev/null)" >> sweep.log
  if [ "$code" = "200" ]; then
    python3 - "$q" <<'PY' >> $OUT
import json,sys
q=sys.argv[1]
d=json.load(open('resp.json'))
for r in d.get('items',[]):
    lic=(r.get('license') or {}).get('spdx_id') or 'NONE'
    desc=(r.get('description') or '').replace('\t',' ').replace('\n',' ')[:200]
    print('\t'.join([r['full_name'],str(r.get('stargazers_count',0)),lic,(r.get('pushed_at') or '')[:10],(r.get('created_at') or '')[:10],str(r.get('open_issues_count',0)),desc,q]))
PY
  fi
  sleep 7
done < queries.txt
