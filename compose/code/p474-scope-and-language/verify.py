import subprocess, hashlib, sys, os, json

PATHS = ["LICENSE","LICENSE.md","LICENSE.txt","license","license.md","license.txt",
         "COPYING","COPYING.txt","LICENCE","LICENCE.md","LICENSE-MIT","MIT-LICENSE",
         "docs/LICENSE",".github/LICENSE"]

ADDRS = [
 "PolyOS-Team/Atolye.Platform","bncc-dev/bncc-benchmark","bncc-dev/bncc-pacotes",
 "bncc-dev/bncc-dados","Handshake-AI-Research/studentbench","kaushikatla-cell/EduSafeBench",
 "RandMelville/slm-writing-feedback-tutor-ptbr","richer-richard/arquimedes",
 "chenhz01/scireason-forge","Simon-zj1/eyedot","Benjamin-KY/open-harness-atlas",
 "AksharaRgsu2024/LLM_Factuality_Evaluation","ipti/br.tag",
 "prefeiturasp/SME-PratoAberto-Edu","prefeiturasp/dados-educacao","mecpy/mec-opendata",
 "datauy/ElijoEstudiar","agn3si/ResultadosUNAM---data","cortega26/chile-hub",
 "portabilis/pre-matricula-digital","pguso/agents-from-scratch",
 "huseyingulsin/Acik-Kaynak-Bilgisayar-Bilimleri","Turkish-AI-Community/hsd-agu-egitim",
 "Apereo-Learning-Analytics-Initiative/OpenLRW","sakaiproject/sakai",
 "gpassero/uol-redacoes-xml",
 "globant-education-kb/this-address-does-not-exist",   # negative control
]

os.makedirs("payloads", exist_ok=True)

def sh(cmd, t=90):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=t)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"

rows=[]
for a in ADDRS:
    rc,out,err = sh(f"git ls-remote --symref https://github.com/{a} HEAD")
    branch=head=None
    if rc==0 and out.strip():
        for line in out.splitlines():
            if line.startswith("ref:"):
                branch=line.split()[1].replace("refs/heads/","")
            elif "\tHEAD" in line:
                head=line.split()[0]
    if not head:
        rows.append(dict(addr=a,resolved="UNRESOLVED",branch="-",head="-",
                         grant_path="-",http="-",bytes="-",digest="-",line1="-"))
        print(f"UNRESOLVED  {a}")
        continue
    found=None
    for p in PATHS:
        url=f"https://raw.githubusercontent.com/{a}/{branch}/{p}"
        safe=a.replace("/","__")+"__"+p.replace("/","_")
        f=f"payloads/{safe}"
        rc2,out2,_ = sh(f'curl -sS -o "{f}" -w "%{{http_code}}" "{url}"', 60)
        code=out2.strip()[-3:]
        if code=="200" and os.path.getsize(f)>0:
            b=open(f,"rb").read()
            dg=hashlib.sha256(b).hexdigest()[:12]
            l1=""
            for ln in b.decode("utf-8","replace").splitlines():
                if ln.strip(): l1=ln.strip(); break
            found=dict(grant_path=f"{branch}/{p}",http="200",bytes=str(len(b)),
                       digest=dg,line1=l1[:95])
            break
        else:
            if os.path.exists(f): os.remove(f)
    if found:
        rows.append(dict(addr=a,resolved="OK",branch=branch,head=head[:12],**found))
        print(f"GRANT       {a}  {found['grant_path']}  {found['bytes']}B {found['digest']}  | {found['line1'][:60]}")
    else:
        rows.append(dict(addr=a,resolved="OK",branch=branch,head=head[:12],
                         grant_path=f"UNGRANTED@{len(PATHS)}probed",http="404",
                         bytes="-",digest="-",line1="-"))
        print(f"UNGRANTED   {a}  ({len(PATHS)} paths probed, branch={branch})")

cols=["addr","resolved","branch","head","grant_path","http","bytes","digest","line1"]
with open("grant-class.2026-10-27-p474.tsv","w") as fh:
    fh.write("\t".join(cols)+"\n")
    for r in rows: fh.write("\t".join(str(r.get(c,"-")) for c in cols)+"\n")
print(f"\n--- {len(rows)} addresses; granted={sum(1 for r in rows if r['http']=='200')}, "
      f"ungranted={sum(1 for r in rows if r['http']=='404')}, "
      f"unresolved={sum(1 for r in rows if r['resolved']=='UNRESOLVED')}")
