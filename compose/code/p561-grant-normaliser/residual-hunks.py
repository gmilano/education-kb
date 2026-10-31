#!/usr/bin/env python3
# p561 — what is the normalised residual? Sentence-level diff after reflow-normalisation.
import difflib, hashlib, re, urllib.request
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"p561"}), timeout=60) as r:
        return r.read().decode("utf-8","replace")
def sents(t):
    t = t.replace(" "," ")
    t = re.sub(r"\s+"," ",t).strip()
    # split into sentence-ish units so hunks are readable
    return [s.strip() for s in re.split(r"(?<=[.;:]) ", t) if s.strip()]
PAIRS = [
 ("AGPL-3.0 canonical(spdx==canvas) -> openedx/openedx-platform",
  "https://raw.githubusercontent.com/spdx/license-list-data/main/text/AGPL-3.0-only.txt",
  "https://raw.githubusercontent.com/openedx/openedx-platform/master/LICENSE"),
 ("GPL-3.0 repo-form(moodle) -> spdx",
  "https://raw.githubusercontent.com/moodle/moodle/main/COPYING.txt",
  "https://raw.githubusercontent.com/spdx/license-list-data/main/text/GPL-3.0-only.txt"),
]
for title,ua,ub in PAIRS:
    a,b = sents(get(ua)), sents(get(ub))
    print("="*100); print(title); print(f"  units: {len(a)} -> {len(b)}")
    n=0
    for line in difflib.unified_diff(a,b,lineterm="",n=0):
        if line.startswith(("---","+++","@@")): continue
        n+=1
        if n>40: print("   ... (truncated)"); break
        print("  "+line[:300])
    if n==0: print("  (no sentence-level differences)")
