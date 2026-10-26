import subprocess, os, sys, datetime, json
CL = sys.argv[1]
def git(d, *a):
    r = subprocess.run(['git','-C',d]+list(a), capture_output=True, text=True)
    return r.stdout.strip() if r.returncode==0 else None
now = datetime.datetime(2026,10,26,1,41,58, tzinfo=datetime.timezone.utc)
rows=[]
for name in sorted(os.listdir(CL)):
    d=os.path.join(CL,name); slug=name.replace('__','/')
    head=git(d,'rev-parse','HEAD')
    if not head: print("NOHEAD",slug,file=sys.stderr); continue
    for off in range(1,15):
        T = now - datetime.timedelta(days=off)
        T2 = T + datetime.timedelta(days=1)
        pin = git(d,'rev-list','-1','--before='+T.isoformat(),'HEAD')
        nxt = git(d,'rev-list','-1','--before='+T2.isoformat(),'HEAD')
        if not pin or not nxt: continue
        cd = git(d,'show','-s','--format=%cI',pin)
        if not cd: continue
        try: pd = datetime.datetime.fromisoformat(cd)
        except Exception: continue
        age_h = (T - pd).total_seconds()/3600.0
        if age_h < 0: continue
        rows.append(dict(slug=slug, off=off, pin=pin[:12], held=(pin==nxt), age_h=round(age_h,2)))
json.dump(rows, open(os.path.join(CL,'..','calib.json'),'w'))
print("observations:", len(rows), "repos:", len({r['slug'] for r in rows}))
