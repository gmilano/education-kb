import json,sys
q=sys.argv[1]; d=json.load(open(sys.argv[2]))
for r in d.get('items',[]):
    lic=(r.get('license') or {}).get('spdx_id') or 'NONE'
    desc=(r.get('description') or '').replace('\t',' ').replace('\n',' ')[:200]
    print('\t'.join([r['full_name'],str(r.get('stargazers_count',0)),lic,(r.get('pushed_at') or '')[:10],(r.get('created_at') or '')[:10],str(r.get('open_issues_count',0)),desc,q]))
