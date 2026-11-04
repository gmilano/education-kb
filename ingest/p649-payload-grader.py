import sys, os
BODY = 1027
def split_payload(p):
    lines = p.split(b"\n"); title=None
    for l in lines:
        if l.strip(): title=l; break
    cpy=None
    for l in lines:
        if l[:9].lower()==b"copyright": cpy=l; break
    return title, cpy
for path in sorted(sys.argv[1:]):
    p=open(path,'rb').read(); m=len(p)
    t,c=split_payload(p)
    name=os.path.basename(path).replace('~','/')
    if t is None: print(f"{name}\t{m}\tUNGRADEABLE\t-\t-"); continue
    tl=t.strip().lower()
    if tl==b"mit license":
        if c is None: print(f"{name}\t{m}\tMIT-NO-CPR\t-\t-"); continue
        pred=BODY+len(t)+len(c); r=m-pred
        print(f"{name}\t{m}\tMIT\t{pred}\t{r:+d}\ttitle={len(t)}\tcpr={len(c)}")
    elif b"apache license" in p[:400].lower():
        r=m-11357
        nl = "Y" if p.endswith(b"\n") else "N"
        crlf = "CRLF" if b"\r\n" in p else "LF"
        lead = "BLANK-LEAD" if p.startswith(b"\n") else "-"
        appx = "APPX-FILLED" if b"Copyright [yyyy]" not in p else "APPX-PLACEHOLDER"
        print(f"{name}\t{m}\tApache-2.0\t11357\t{r:+d}\tfinal_nl={nl}\t{crlf}\t{lead}\t{appx}\tlines={p.count(chr(10).encode())}")
    else:
        print(f"{name}\t{m}\tOTHER\t-\t-")
