#!/usr/bin/env python3
"""p689: extend the p684 primary-README-language channel from CJK (which is
decidable by codepoint) to Latin-script languages, which are not.  Method:
function-word density.  Function words are closed-class, so they cannot be
imported by a loanword the way content words can, and they appear at a rate
that does not depend on the subject matter.  Controls below are run at both
signs: two READMEs known to be Portuguese and three known to be English."""
import subprocess, re, sys
ES = set("el la los las de del y que en un una para con por como más este esta pero o su sus al lo le se no son sobre entre cuando donde desde hasta".split())
PT = set("o a os as de do da dos das e que em um uma para com por como mais este esta mas ou seu seus ao lo lhe se nao não sao são sobre entre quando onde desde ate até você".split())
EN = set("the of and to in a is for with on that as are this be by or from it an at not you your can we".split())
def probe(slug, ref):
    for f in ('README.md','readme.md','README.rst','README.pt.md'):
        r = subprocess.run(['curl','-sfL','--max-time','25',
            f'https://raw.githubusercontent.com/{slug}/{ref}/{f}'],capture_output=True,text=True)
        if r.stdout.strip():
            t = re.sub(r'```.*?```','',r.stdout,flags=re.S)
            t = re.sub(r'`[^`]*`','',t)
            t = re.sub(r'!?\[[^\]]*\]\([^)]*\)','',t)
            t = re.sub(r'https?://\S+','',t)
            w = re.findall(r"[a-zA-ZáéíóúàâãçêôõüñÁÉÍÓÚÀÂÃÇÊÔÕÜÑ']+", t.lower())
            n = len(w) or 1
            d = {k: 100*sum(1 for x in w if x in s)/n for k,s in (('ES',ES),('PT',PT),('EN',EN))}
            win = max(d, key=d.get)
            print(f"{slug:42s} {f:12s} words={n:6d}  EN={d['EN']:5.1f}%  ES={d['ES']:5.1f}%  PT={d['PT']:5.1f}%  -> {win}")
            return
    print(f"{slug:42s} NO-README")
print("--- positive controls (known Portuguese) ---")
probe('Mcp-Brasil/mcp-brasil','main'); probe('portabilis/i-diario','1.6')
print("--- negative controls (known English) ---")
for s,r in [('torvalds/linux','master'),('moodle/moodle','main'),('pacewisdomhq/TutorLoom','main')]: probe(s,r)
print("--- subjects ---")
for s,r in [('DavidLMS/learnmcp-xapi','main'),('onemnemo/mnemo','main'),('iblai/lms','main'),
            ('SJRiz/pytogether','main'),('ZhijieXiong/pyedmine','main'),('langx/langx','main'),
            ('smlfg/ilias-mcp','main'),('ideas-edu/ideas','master'),('theopenem/oneroster.net','master')]:
    probe(s,r)
