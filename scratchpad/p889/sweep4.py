import json,subprocess,urllib.parse
out=open('sweep4.tsv','w'); log=open('sweep4.log','w')
for q in [l.strip() for l in open('q4.txt') if l.strip()]:
    url="https://api.github.com/search/repositories?q="+urllib.parse.quote(q)+"&sort=stars&order=desc&per_page=30"
    p=subprocess.run(['curl','-s','-w','\n%{http_code}',url],capture_output=True,text=True)
    body,_,code=p.stdout.rpartition('\n'); code=code.strip(); tc='ERR'; n=0
    if code=='200':
        d=json.loads(body); tc=d.get('total_count')
        for r in d.get('items',[]):
            lic=(r.get('license') or {}).get('spdx_id') or 'NONE'
            desc=(r.get('description') or '').replace('\t',' ').replace('\n',' ')[:180]
            out.write('\t'.join([r['full_name'],str(r.get('stargazers_count',0)),lic,(r.get('pushed_at') or '')[:10],(r.get('created_at') or '')[:10],str(r.get('forks_count',0)),desc,q])+'\n'); n+=1
    log.write(f"{code}\t{q}\t{tc}\t{n}\n")
log.close(); out.close()
