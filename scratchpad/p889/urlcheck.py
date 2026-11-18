import json,subprocess,urllib.parse
rows=[l.strip() for l in open('urls.txt') if l.strip()]
# discriminating existence check: repo search by exact full_name via search API, plus raw default-branch probe
print("slug\tsearch_exact\traw_probe")
bad=[]
for s in rows:
    owner,_,name=s.partition('/')
    q=f'repo:{s}'
    url="https://api.github.com/search/repositories?q="+urllib.parse.quote(q)
    p=subprocess.run(['curl','-s',url],capture_output=True,text=True)
    hit='NO'
    try:
        d=json.loads(p.stdout)
        for it in d.get('items',[]):
            if it['full_name'].lower()==s.lower(): hit='YES'
    except Exception as e: hit=f'ERR'
    raw='NO'
    for br in ('main','master'):
        r=subprocess.run(['curl','-sL','-o','/dev/null','-w','%{http_code}',f"https://raw.githubusercontent.com/{s}/{br}/README.md"],capture_output=True,text=True)
        if r.stdout.strip()=='200': raw=f'200@{br}'; break
    print(f"{s}\t{hit}\t{raw}")
    if hit!='YES': bad.append(s)
print("\nFAILED_EXACT:", bad if bad else "none")
