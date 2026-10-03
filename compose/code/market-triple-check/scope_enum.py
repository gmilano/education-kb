import json,urllib.request,urllib.parse,re,tarfile,io
ANCHOR=re.compile(r'^package/(licen[cs]e|copying)[^/]*$',re.I)
def enumerate_scope(scope):
    q=urllib.parse.quote(f'scope:{scope}',safe='')
    url=f"https://registry.npmjs.org/-/v1/search?text={q}&size=250"
    d=json.load(urllib.request.urlopen(url))
    names=sorted({o['package']['name'] for o in d.get('objects',[]) if o['package']['name'].startswith(f'@{scope}/')})
    print(f"@{scope}/* -> search endpoint reporta total={d.get('total')}, nombres del alcance recuperados={len(names)}")
    return names
def licence(pkg):
    enc=pkg.replace('/','%2F')
    d=json.load(urllib.request.urlopen(f"https://registry.npmjs.org/{enc}/latest"))
    raw=urllib.request.urlopen(d['dist']['tarball']).read()
    tf=tarfile.open(fileobj=io.BytesIO(raw)); nm=tf.getnames()
    hits=[n for n in nm if ANCHOR.match(n)]
    txt=''
    if hits:
        b=tf.extractfile(hits[0]).read(); txt=f"{hits[0]} ({len(b)}b)"
    return d.get('version'), d.get('license'), (txt or 'SIN TEXTO'), len(nm)
for scope in ['timeback','ink-waffle']:
    print(f"\n===== ALCANCE @{scope}/* =====")
    try: names=enumerate_scope(scope)
    except Exception as e: print(f"  ERROR enumerando: {type(e).__name__}: {e}"); continue
    con=sin=0
    for n in names:
        try:
            v,lic,txt,nf=licence(n)
            flag='TEXTO' if txt!='SIN TEXTO' else 'sin texto'
            if txt!='SIN TEXTO': con+=1
            else: sin+=1
            print(f"  {n:34s} {str(v):8s} campo={str(lic):10s} {flag:9s} {txt if txt!='SIN TEXTO' else ''} [{nf} archivos]")
        except Exception as e:
            print(f"  {n:34s} ERROR {type(e).__name__}")
    print(f"  --> {len(names)} paquetes enumerados: {con} con texto / {sin} sin texto")
