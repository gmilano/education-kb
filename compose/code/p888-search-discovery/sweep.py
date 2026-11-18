#!/usr/bin/env python3
"""p888-search-discovery: re-scoped discovery channel (887-G4).
Uses api.github.com/search/repositories, which this session CAN reach,
unlike /repos/{slug} (403). Records stars/forks/pushed/license/archived.
"""
import json, subprocess, sys, time, os

OUT = os.path.dirname(os.path.abspath(__file__))

LEGS = [
 ("tutor-mit",        'ai tutor education in:name,description,readme license:mit stars:>40 pushed:>2026-03-01'),
 ("tutor-apache",     'ai tutor education in:name,description,readme license:apache-2.0 stars:>40 pushed:>2026-03-01'),
 ("its",              'intelligent tutoring system in:name,description,readme stars:>25 pushed:>2026-01-01'),
 ("lessonplan",       'lesson plan generator AI in:name,description,readme stars:>15 pushed:>2026-01-01'),
 ("grading",          'automated grading LLM rubric in:name,description,readme stars:>20 pushed:>2026-01-01'),
 ("quizgen",          'quiz question generation LLM in:name,description,readme stars:>25 pushed:>2026-01-01'),
 ("learn-analytics",  'learning analytics student LLM in:name,description,readme stars:>20 pushed:>2026-01-01'),
 ("edu-agent",        'education agent LLM multi-agent classroom in:name,description,readme stars:>30 pushed:>2026-03-01'),
 ("lms-ai",           'moodle OR canvas OR openedx AI plugin in:name,description,readme stars:>20 pushed:>2026-01-01'),
 ("flashcard",        'flashcard spaced repetition AI in:name,description,readme stars:>50 pushed:>2026-03-01'),
 ("curriculum",       'curriculum generator syllabus AI in:name,description,readme stars:>15 pushed:>2026-01-01'),
 ("topic-edu-ai",     'topic:ai-in-education stars:>10'),
 ("topic-edtech",     'topic:edtech topic:ai stars:>15'),
 ("topic-its",        'topic:intelligent-tutoring-system'),
 ("grader-agent",     'essay scoring automated feedback in:name,description,readme stars:>20 pushed:>2026-01-01'),
 ("study-agent",      'study assistant notes quiz agent in:name,description,readme license:mit stars:>60 pushed:>2026-05-01'),
 ("knowledge-tracing",'knowledge tracing deep learning in:name,description,readme stars:>30'),
 ("proctor",          'exam proctoring open source in:name,description,readme stars:>15'),
 ("sped",             'accessibility special education AI in:name,description,readme stars:>10 pushed:>2026-01-01'),
 ("lang-tutor",       'language learning tutor LLM speech in:name,description,readme stars:>40 pushed:>2026-03-01'),
]

def gh(q, page=1):
    cmd = ["gh","api","-X","GET","search/repositories",
           "-f",f"q={q}","-f","per_page=50","-f",f"page={page}","-f","sort=stars"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    if r.returncode != 0:
        return None, r.stderr.strip()[:200]
    try:
        return json.loads(r.stdout), None
    except Exception as e:
        return None, str(e)[:200]

rows, legmeta = [], []
seen = set()
for name, q in LEGS:
    d, err = gh(q)
    if d is None:
        legmeta.append((name, q, "ERROR", 0, err)); print(f"[{name}] ERROR {err}", file=sys.stderr); continue
    tc = d.get("total_count", 0)
    items = d.get("items", [])
    legmeta.append((name, q, "OK", tc, f"{len(items)} returned"))
    print(f"[{name}] total_count={tc} returned={len(items)}", file=sys.stderr)
    for it in items:
        fn = it["full_name"]
        if fn.lower() in seen: continue
        seen.add(fn.lower())
        lic = it.get("license") or {}
        rows.append({
            "leg": name, "slug": fn,
            "stars": it.get("stargazers_count"), "forks": it.get("forks_count"),
            "spdx": lic.get("spdx_id") or "NONE",
            "license_name": lic.get("name") or "-",
            "pushed": (it.get("pushed_at") or "")[:10],
            "created": (it.get("created_at") or "")[:10],
            "archived": it.get("archived"), "is_fork": it.get("fork"),
            "branch": it.get("default_branch"), "lang": it.get("language") or "-",
            "desc": (it.get("description") or "").replace("\t"," ").replace("\n"," ")[:300],
        })
    time.sleep(2.2)

with open(f"{OUT}/raw-candidates.json","w") as f: json.dump(rows, f, indent=1)
with open(f"{OUT}/legs.tsv","w") as f:
    f.write("leg\tquery\tstatus\ttotal_count\tnote\n")
    for m in legmeta: f.write("\t".join(str(x) for x in m)+"\n")
print(f"\nTOTAL distinct candidates: {len(rows)}", file=sys.stderr)
