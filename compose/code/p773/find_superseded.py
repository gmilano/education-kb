#!/usr/bin/env python3
"""p773 -- narrow, SUBJECT-BOUND finder for the superseded Annex III education date.
A bare 'August 2026' is NOT a defect by itself: Article 50 transparency duties
genuinely apply from 2 August 2026, and many sites date unrelated events. A site
is a defect only if, on the same line, it (a) names the Annex III / high-risk
education obligation AND (b) gives 2 August 2026 as its application date AND
(c) does NOT carry the settled 2 December 2027 value or a supersession marker.
"""
import re,sys,json
SUBJ=re.compile(r"annex\s*iii|high[- ]risk",re.I)
EDU =re.compile(r"educat|admission|student|exam|proctor|assess",re.I)
DATE=re.compile(r"2\s*august\s*2026|august\s*2026|2026-08-02",re.I)
GOOD=re.compile(r"2\s*december\s*2027|2027-12-02|supersed|refut|stale|wrong|"
                r"pre-amendment|contradict|unresolved|conflict|mov(ed|ing)|deferr|"
                r"push(ed)?|shift(ed)?|slip|the original|one guide|one source|"
                r"sources? (place|disagree|split)|claim|slated",re.I)
# D8 (p773): the check must run over a PARAGRAPH WINDOW, not a line. This base's
# prose is hard-wrapped, so the supersession marker routinely sits on the next
# line from the date. Line-bound checking reports the wrap as a defect -- which is
# how a "75 site" count is produced from a clean shelf.
WIN=3
out=[]
for p in sys.argv[1:]:
    L=open(p,encoding="utf-8",errors="replace").read().split("\n")
    for i,l in enumerate(L,1):
        if not (SUBJ.search(l) and EDU.search(l) and DATE.search(l)):
            continue
        ctx="\n".join(L[max(0,i-1-WIN):i+WIN])
        if GOOD.search(ctx):
            continue
        out.append({"file":p,"line":i,"text":l.strip()[:200]})
print(json.dumps(out,indent=1,ensure_ascii=False))
print("SUBJECT-BOUND DEFECT SITES: %d"%len(out),file=sys.stderr)
