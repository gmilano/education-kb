import re,hashlib
def sha12(b):
    if isinstance(b,str): b=b.encode('utf-8')
    return hashlib.sha256(b).hexdigest()[:12]
def ws(b):
    t=b.decode("utf-8","replace").replace(" "," ")
    return re.sub(r"\s+"," ",t).strip().encode()
_MAP=(("“",'"'),("”",'"'),("‘","'"),("’","'"),
      ("–","-"),("—","-"),("©","(C)"),("®","(R)"),
      ("http://fsf.org/","https://fsf.org/"),
      ("http://www.fsf.org/","https://fsf.org/"),
      ("http://www.gnu.org/","https://www.gnu.org/"))
def punct(b):
    t=b.decode("utf-8","replace")
    for a,c in _MAP: t=t.replace(a,c)
    return t.encode()
def grade(raw):
    w=ws(raw); p=punct(w)
    return dict(raw_B=len(raw),sha_raw=sha12(raw),
                ws_B=len(w),sha_ws=sha12(w),sha_punct=sha12(p))
