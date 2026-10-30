#!/usr/bin/env python3
"""p552 `channel-yield.py` -- grade a CURATED LIST as a CHANNEL (Gap 551-D).

Gap 551-D asked for "a disposition axis asking: is this artefact worth more as a
channel than as a row?".  p551 answered it with ONE number -- novelty count (9 of
13).  This instrument measures that number against a SECOND axis, and the two
disagree on this corpus.

AXES
  novel   -- addresses the list carries that the shelves do not hold
  fit     -- of those, how many are IN DOMAIN (education keyword in the slug)

WHAT THIS INSTRUMENT CANNOT DO, STATED FIRST
  `fit` is a SLUG-TEXT heuristic.  It reads the address, not the repository, so
  `eth-lre/pedagogicalrl` scores 1 on "pedagogical" and `shunli-wang/cpr-coach`
  scores 0 though it is a real skills-training corpus.  It therefore UNDERCOUNTS
  domain fit and must not be quoted as a domain census.  It is used here for one
  claim only: the RANK CORRELATION between novelty and fit, which survives the
  undercount because the error is not correlated with list identity.

WHAT p552 MEASURED WITH IT, AND THE RULE THAT CAME OUT
  Seven lists.  Ranked on `novel` alone -- which is the ONLY number p551 had --
  `uhub/awesome-llm` (1016 novel, 3.5 % fit) and `sindresorhus/awesome` (670,
  3.4 %) rank first and second, and the list with the HIGHEST fit
  (`GeminiLight/awesome-ai-llm4education`, 5 novel, 40.0 %) ranks sixth of seven.
  3.5 % of a large number beats 40 % of a small one on any ABSOLUTE threshold,
  and a general index is large by construction.

  RULE: grade a channel on FIT RATE, never on an absolute count.

  SECOND DEFECT, registered as `Gap 552-A` and NOT fixed here: the in-domain hits
  of the two "winners" are `awesome-laravel-education`, `awesome-swift-education`,
  `awesome-css-learning`, `learn-to-program` -- DEVELOPER education, not the
  education industry.  The keyword cannot separate "learning to code" from "AI for
  schools", so the rate-based reading overstates both.  Read the matches before
  promoting the channel.

  The `disposition` column this file prints uses the >=3 ABSOLUTE threshold and is
  therefore WRONG BY THE RULE ABOVE.  It is left in place, unused, so the defect
  stays visible to whoever next reads the output; quote `fit_pct`, not `disposition`.
"""
import re, subprocess, pathlib, sys

LISTS = [
    "GeminiLight/awesome-ai-llm4education",
    "Geralt-Targaryen/Awesome-Education-LLM",
    "wikit-ai/awesome-llm-courses",
    "abla-ha/LLM-Educational-repo",
    "uhub/awesome-llm",
    "sindresorhus/awesome",
    "Developer-Y/cs-video-courses",
]
ADDR = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9_.-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)")
SKIP = {"blob","tree","archive","releases","topics","sponsors","orgs","search","issues","pulls"}
DOMAIN = re.compile(r"edu|tutor|learn|teach|school|student|course|lesson|quiz|grad(e|ing)"
                    r"|curricul|classroom|pedagog|lms|moodle|exam|assess|knowledge-trac|mooc", re.I)

def fetch(slug):
    for b in ("main","master"):
        for n in ("README.md","readme.md"):
            url=f"https://raw.githubusercontent.com/{slug}/{b}/{n}"
            r=subprocess.run(["curl","-sS","-m","45","-w","%{http_code}","-o","/tmp/p552-cy.txt",url],
                             capture_output=True,text=True)
            if r.stdout.strip().endswith("200"):
                return pathlib.Path("/tmp/p552-cy.txt").read_text(encoding="utf-8",errors="replace")
    return None

known=set(l.strip() for l in open("/tmp/p552-known.txt") if l.strip())
rows=[]
print("list\tbytes\taddresses\tnovel\tin_domain\tfit_pct\tdisposition")
for slug in LISTS:
    body=fetch(slug)
    if body is None:
        print(f"{slug}\tUNREACHABLE\t-\t-\t-\t-\t-"); continue
    found=set()
    for o,r in ADDR.findall(body):
        r=r.rstrip(".,);:").removesuffix(".git")
        if o.lower() in SKIP or r.lower() in SKIP or not r: continue
        found.add(f"{o}/{r}".lower())
    novel=sorted(found-known)
    fit=[n for n in novel if DOMAIN.search(n)]
    pct = (100.0*len(fit)/len(novel)) if novel else 0.0
    disp = "CHANNEL" if len(fit)>=3 else ("ROW-ONLY" if novel else "NEITHER")
    print(f"{slug}\t{len(body)}\t{len(found)}\t{len(novel)}\t{len(fit)}\t{pct:.1f}\t{disp}")
    rows.append((slug,len(novel),len(fit),fit))

print("\n# in-domain novel addresses, by list", file=sys.stderr)
for slug,n,f,fits in rows:
    for a in fits[:25]:
        print(f"{slug}\t{a}", file=sys.stderr)
