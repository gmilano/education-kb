#!/usr/bin/env python3
"""p129 ACTION AS repair: carry a re-measured tag figure onto every LIVE site that names the
project, marking the old value with this KB's own correction marker.

Rules this pass had to adopt, each learned from the lineage:
  * the append-only pages are NEVER edited — a dated section at their top carries the
    correction (p128's ACTION AQ);
  * repairs run BEFORE a pass prepends its sections, because prepending invalidates every
    coordinate below the insertion (p126's P126-A);
  * the marker is emitted OUTSIDE the emphasis span it corrects, or the nested '**' closes
    the figure's own bold and the row renders as literal asterisks.
A site is a (page, line) where the line names the project — by address or by short name — and
carries the old figure.
"""
import re, sys, os

MARKER = "⚠️ **was %s**<!--corrected-->"
LIVE = ["README.md","agents/top.md","repos/foundations.md","verticals/solutions.md",
        "intel/market.md","intel/trends.md","intel/open-gaps.md","compose/patterns.md"]
APPEND_ONLY = ["agents/trending.md","repos/trending.md"]
JOBS = [
    (["seb-server","SafeExamBrowser"], 194, 108),
    (["Jasig/SSP","ssp-2.9.0"], 57, 29),
    (["ojd_daps_skills"], 8, 7),
    (["opencred","OpenCred"], 30, 21),
    (["catsim"], 38, 37),
    (["moodle/moodle"], 590, 591),
    (["edx-platform"], 451, 5896),
    (["ai_course_assistant"], 295, 296),
    (["speechocean762"], 0, 1),
    (["kolibri"], 16, 542),
]

def grouped(n):
    return re.sub(r'(?<=\d)(?=(\d{3})+$)', ' ', str(n))

def noun(n):
    return "tag" if n == 1 else "tags"

APPARATUS = re.compile(r'\u26a0\ufe0f \*\*was [^*]*\*\*<!--corrected-->')

def spans(line):
    """The correction apparatus is a SCOPE, not a token: a figure inside it is a record of a
    retracted claim, never a live one. p124 read a token without its scope; this reads the scope."""
    return [(m.start(), m.end()) for m in APPARATUS.finditer(line)]

def repair_line(line, old, new):
    """Return (line, n_sites). Every live form of the figure on the line is corrected; no form
    inside the apparatus ever is."""
    o, nw, mark = str(old), grouped(new), MARKER % ("%s %s" % (old, noun(old)))
    pats = [
        (r'\*\*%s(\s+)tags?\*\*' % o,              lambda m: "**%s%s%s** %s" % (nw, m.group(1), noun(new), mark)),
        (r'\*\*%s\*\*(\s*)tags?' % o,              lambda m: "**%s**%s%s %s" % (nw, m.group(1), noun(new), mark)),
        (r'(?<![\d\u202f\u00a0])%s(\s+)tags?' % o,  lambda m: "%s%s%s %s" % (nw, m.group(1), noun(new), mark)),
        (r'\*\*%s\*\*(?=\s*\|)' % o,              lambda m: "**%s** %s" % (nw, mark)),
    ]
    total = 0
    for pat, rep in pats:
        while True:
            prot = spans(line)
            hit = None
            for m in re.finditer(pat, line):
                if any(a <= m.start() < b for a, b in prot): continue
                hit = m; break
            if hit is None: break
            line = line[:hit.start()] + rep(hit) + line[hit.end():]
            total += 1
    return line, total

def run(root, apply):
    total, per = 0, {}
    for page in LIVE:
        path = os.path.join(root, page)
        lines = open(path).read().split("\n")
        changed = 0
        for i, line in enumerate(lines):
            for names, old, new in JOBS:
                if not any(k in line for k in names): continue
                lines[i], n = repair_line(lines[i], old, new)
                changed += n
        if changed:
            per[page] = changed; total += changed
            if apply: open(path,"w").write("\n".join(lines))
    for p, c in per.items(): print("%-26s %d site(s)" % (p, c))
    print("TOTAL sites: %d  (append-only untouched: %s)" % (total, ", ".join(APPEND_ONLY)))
    return total

if __name__ == "__main__":
    run(sys.argv[1], apply=(len(sys.argv) > 2 and sys.argv[2] == "--apply"))
