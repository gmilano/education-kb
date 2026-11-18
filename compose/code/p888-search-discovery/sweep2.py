#!/usr/bin/env python3
"""p888 sweep2: precise education-native legs. No broad OR legs, no star-sort
dominance - sort by updated to reach the live mid-tail where education sits."""
import json, subprocess, sys, time, os
OUT=os.path.dirname(os.path.abspath(__file__))
LEGS=[
 ("its-live",      'intelligent tutoring system in:name,description pushed:>2026-06-01','updated'),
 ("ai-tutor-name", '"ai tutor" in:name,description pushed:>2026-06-01','updated'),
 ("tutoring-sys",  'tutoring system agent in:name,description pushed:>2026-06-01','updated'),
 ("lesson-plan",   '"lesson plan" in:name,description pushed:>2026-06-01','updated'),
 ("autograde",     'autograder OR autograding in:name,description pushed:>2026-03-01','updated'),
 ("rubric",        'rubric grading in:name,description pushed:>2026-03-01','updated'),
 ("knowledge-tr",  '"knowledge tracing" in:name,description','stars'),
 ("lti",           'LTI 1.3 in:name,description,readme pushed:>2026-01-01','updated'),
 ("scorm",         'scorm xapi in:name,description pushed:>2026-01-01','updated'),
 ("moodle-plugin", 'moodle in:name,description pushed:>2026-06-01','updated'),
 ("openedx-xblock",'xblock openedx in:name,description','updated'),
 ("student-info",  '"student information system" in:name,description','stars'),
 ("quiz-gen2",     '"question generation" education in:name,description,readme','stars'),
 ("essay-score",   '"automated essay" scoring in:name,description,readme','stars'),
 ("pronunciation", 'pronunciation assessment in:name,description','stars'),
 ("edu-rag",       'education RAG tutor in:name,description pushed:>2026-06-01','updated'),
 ("teacher-agent", 'teacher assistant agent in:name,description pushed:>2026-06-01','updated'),
 ("curriculum2",   '"curriculum" generator in:name,description pushed:>2026-03-01','updated'),
 ("adaptive-learn",'adaptive learning platform in:name,description pushed:>2026-03-01','updated'),
 ("sis-erp",       'school management system in:name,description pushed:>2026-06-01','updated'),
 ("exam-gen",      'exam generator question bank in:name,description pushed:>2026-03-01','updated'),
 ("mastery",       'mastery learning spaced in:name,description pushed:>2026-03-01','updated'),
]
def gh(q,sort,page=1):
    cmd=["gh","api","-X","GET","search/repositories","-f",f"q={q}","-f","per_page=50","-f",f"page={page}","-f",f"sort={sort}"]
    r=subprocess.run(cmd,capture_output=True,text=True,timeout=90)
    if r.returncode!=0: return None,r.stderr.strip()[:160]
    try: return json.loads(r.stdout),None
    except Exception as e: return None,str(e)[:160]
rows=[];legmeta=[];seen=set()
for name,q,sort in LEGS:
    d,err=gh(q,sort)
    if d is None:
        legmeta.append((name,q,sort,"ERROR",0,err));print(f"[{name}] ERROR {err}",file=sys.stderr);continue
    tc=d.get("total_count",0);items=d.get("items",[])
    legmeta.append((name,q,sort,"OK",tc,f"{len(items)} returned"))
    print(f"[{name}] tc={tc} n={len(items)}",file=sys.stderr)
    for it in items:
        fn=it["full_name"]
        if fn.lower() in seen: continue
        seen.add(fn.lower())
        lic=it.get("license") or {}
        rows.append({"leg":name,"slug":fn,"stars":it.get("stargazers_count"),"forks":it.get("forks_count"),
          "spdx":lic.get("spdx_id") or "NONE","pushed":(it.get("pushed_at") or "")[:10],
          "created":(it.get("created_at") or "")[:10],"archived":it.get("archived"),"is_fork":it.get("fork"),
          "branch":it.get("default_branch"),"lang":it.get("language") or "-",
          "desc":(it.get("description") or "").replace("\t"," ").replace("\n"," ")[:300]})
    time.sleep(2.2)
json.dump(rows,open(f"{OUT}/raw2.json","w"),indent=1)
with open(f"{OUT}/legs2.tsv","w") as f:
    f.write("leg\tquery\tsort\tstatus\ttotal_count\tnote\n")
    for m in legmeta: f.write("\t".join(str(x) for x in m)+"\n")
print(f"\nTOTAL distinct: {len(rows)}",file=sys.stderr)
