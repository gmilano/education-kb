#!/usr/bin/env python3
"""p779 instrument (p778-E): census a public-sector estate on the claim channel.

T800 ("the licence is the delivery team's template, not the subject") rests on
ONE estate, DFE-Digital. This censuses a second and third the same way so the
claim can be tested rather than repeated. The specific test T800 names: does
grant rate cluster by repository-NAME FAMILY rather than by subject?

Name family = the leading hyphen/underscore-delimited token(s) of the repo name,
which is how a delivery team's cookiecutter stamps its output.
Emits one TSV row per repository; prints nothing it did not read.
"""
import json, subprocess, sys, collections

def fetch(owner):
    rows, page = [], 1
    while True:
        out = subprocess.run(
            ["gh","api","-X","GET","search/repositories",
             "-f",f"q=user:{owner}","-f","per_page=100","-f",f"page={page}"],
            capture_output=True, text=True, timeout=120)
        if out.returncode != 0:
            print(f"# ERROR {owner} page {page}: {out.stderr[:200]}", file=sys.stderr); break
        d = json.loads(out.stdout)
        items = d.get("items", [])
        rows += items
        tot = d.get("total_count", 0)
        if not items or len(rows) >= tot or page >= 10: 
            print(f"# {owner}: total_count={tot}, fetched={len(rows)}", file=sys.stderr); break
        page += 1
    return rows

def family(name):
    t = name.replace("_","-").split("-")
    return t[0].lower() if t else name.lower()

def main(owners):
    allrows = []
    print("owner\trepo\tspdx\tstars\tpushed\tarchived\tfork\tlang\tfamily")
    for o in owners:
        for r in fetch(o):
            lic = (r.get("license") or {}).get("spdx_id") or "NONE"
            row = (r["owner"]["login"], r["name"], lic, r.get("stargazers_count",0),
                   (r.get("pushed_at") or "")[:10], r.get("archived"), r.get("fork"),
                   r.get("language") or "-", family(r["name"]))
            allrows.append(row)
            print("\t".join(str(x) for x in row))
    # summary to stderr so the TSV stays clean
    e = sys.stderr
    print(f"\n# ===== {len(allrows)} repositories =====", file=e)
    byl = collections.Counter(r[2] for r in allrows)
    print(f"# licence: {dict(byl.most_common())}", file=e)
    gr = lambda rs: (sum(1 for r in rs if r[2] not in ("NONE","NOASSERTION")), len(rs))
    print("\n# --- grant rate by NAME FAMILY (families with >=3 repos) ---", file=e)
    fam = collections.defaultdict(list)
    for r in allrows: fam[(r[0],r[8])].append(r)
    for (o,f), rs in sorted(fam.items(), key=lambda kv: -len(kv[1])):
        if len(rs) < 3: continue
        g, n = gr(rs)
        print(f"#   {o}/{f:<22} {g:>3}/{n:<3} = {100.0*g/n:>5.1f}%   "
              f"{sorted(set(x[2] for x in rs))}", file=e)
    print("\n# --- grant rate by LANGUAGE (>=3) ---", file=e)
    lang = collections.defaultdict(list)
    for r in allrows: lang[r[7]].append(r)
    for l, rs in sorted(lang.items(), key=lambda kv: -len(kv[1])):
        if len(rs) < 3: continue
        g, n = gr(rs)
        print(f"#   {l:<24} {g:>3}/{n:<3} = {100.0*g/n:>5.1f}%", file=e)
    print("\n# --- grant rate by ARCHIVED ---", file=e)
    for key in (True, False):
        rs = [r for r in allrows if r[5] is key]
        if rs:
            g,n = gr(rs); print(f"#   archived={key}: {g}/{n} = {100.0*g/n:.1f}%", file=e)

main(sys.argv[1:])
