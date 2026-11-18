import subprocess,re
slugs=[l.strip() for l in open('all47.txt') if l.strip()]
terms=re.compile(r'\b(education|educational|school|schools|university|universities|student|students|teacher|teachers|classroom|learning management|LMS|pupil|EdTech|edtech|Annex III|admission|exam|assessment of students|vocational)\b',re.I)
out=open('eduprobe.tsv','w')
out.write("slug\treadme_http\tbytes\thits\tterms\n")
nf=0;hit=0
for s in slugs:
    got=None
    for br in ('main','master'):
        for p in ('README.md','readme.md','README.MD','README.rst'):
            r=subprocess.run(['curl','-sL','-w','\n%{http_code}',f"https://raw.githubusercontent.com/{s}/{br}/{p}"],capture_output=True,text=True)
            b,_,c=r.stdout.rpartition('\n')
            if c.strip()=='200' and b.strip(): got=b; break
        if got: break
    if got is None:
        nf+=1; out.write(f"{s}\tNOFILE\t0\t0\t-\n"); continue
    ms=terms.findall(got)
    uniq=sorted(set(m.lower() for m in ms))
    if ms: hit+=1
    out.write(f"{s}\t200\t{len(got)}\t{len(ms)}\t{','.join(uniq)}\n")
out.close()
print("slugs",len(slugs),"no-readme",nf,"with-any-edu-term",hit)
