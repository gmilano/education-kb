import sys,csv,urllib.request,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from norm import grade
rows=list(csv.DictReader(open('/tmp/education-kb/evidence/canonical-grant-normalisation.2026-10-30-p561.tsv'),delimiter='\t'))
ok=bad=0
for r in rows:
    try:
        b=urllib.request.urlopen(r['url'],timeout=60).read()
    except Exception as e:
        print("FETCHFAIL",r['source'],e); continue
    g=grade(b)
    checks=[('raw_B',int(r['raw_B']),g['raw_B']),('sha12_raw',r['sha12_raw'],g['sha_raw']),
            ('ws_B',int(r['ws_B']),g['ws_B']),('sha12_ws',r['sha12_ws'],g['sha_ws']),
            ('sha12_punct',r['sha12_punct'],g['sha_punct'])]
    diffs=[(n,a,b2) for n,a,b2 in checks if a!=b2]
    if diffs:
        bad+=1; print("MISMATCH",r['family'],r['source'],diffs)
    else:
        ok+=1; print("OK      ",r['family'],r['source'])
print(f"\nCALIBRATION: {ok} reproduce, {bad} mismatch, of {len(rows)}")
