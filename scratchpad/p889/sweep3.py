import json,subprocess,time,urllib.parse,sys
qs=[l.strip() for l in open('queries3.txt') if l.strip()]
out=open('sweep3.tsv','w'); log=open('sweep3.log','w')
for q in qs:
    enc=urllib.parse.quote(q)
    url=f"https://api.github.com/search/repositories?q={enc}&sort=stars&order=desc&per_page=30"
    p=subprocess.run(['curl','-s','-w','\n%{http_code}',url],capture_output=True,text=True)
    body,_,code=p.stdout.rpartition('\n')
    tc='ERR';n=0
    if code.strip()=='200':
        try:
            d=json.loads(body); tc=d.get('total_count','ERR')
            for r in d.get('items',[]):
                lic=(r.get('license') or {}).get('spdx_id') or 'NONE'
                desc=(r.get('description') or '').replace('\t',' ').replace('\n',' ')[:200]
                out.write('\t'.join([r['full_name'],str(r.get('stargazers_count',0)),lic,(r.get('pushed_at') or '')[:10],(r.get('created_at') or '')[:10],str(r.get('forks_count',0)),desc,q])+'\n')
                n+=1
        except Exception as e: tc=f'PARSE:{e}'
    log.write(f"{code.strip()}\t{q}\t{tc}\t{n}\n"); log.flush(); out.flush()
    time.sleep(8)
print("done", len(qs))
