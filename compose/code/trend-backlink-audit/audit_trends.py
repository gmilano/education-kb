#!/usr/bin/env python3
"""Resolve every TREND citation in the eight KB files against its definition.

Pase 48, action 2, stated the problem: that pase went looking for `tendencia
210` with a grep of headers, did not find it, and nearly published a "dangling
backlink" that did not exist -- 210 lives in a TABLE ROW, not in a `## `. The
false finding was caught by the positive control, not by the instrument.

So the citation is what a client follows, and it is worth an instrument.

    python3 audit_trends.py            # the report
    python3 audit_trends.py --tsv      # one row per citation

WHAT THIS MEASURES, and the correction it makes to its own brief: the action
said this base numbers trends in TWO forms (header and row). It numbers them in
THREE, and the third is the one that holds trends 1-156:

  1. `## 57. Title`                      -- a numbered header (the majority)
  2. `## Las tendencias 211-219, ...`    -- a header declaring a RANGE, whose
                                            members are table rows below it
  3. `| **217** | ... |`                 -- the row itself

Form 3 is NOT self-identifying: `| **103** |` is a GAP row, and gaps and trends
share the integer namespace. A row therefore counts as a trend definition only
when the nearest preceding header is a trends header. Guessing otherwise would
credit gap numbers as trends and silence real dangling citations.
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

KB_FILES = [
    "agents/top.md", "agents/trending.md",
    "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "compose/patterns.md",
    "intel/market.md", "intel/trends.md",
]
TRENDS_FILE = "intel/trends.md"

DASH = r"[-‐‑‒–—]"

#: form 1 -- a numbered header.
H_NUM = re.compile(r"^#+\s*(?:[^\w\s#]\s*)?(\d{1,3})\.\s+\S")
#: form 2 -- a header declaring a range of trends.
H_RANGE = re.compile(r"^#+.*?[Tt]endencias?\s+\**(\d{1,3})\**\s*%s\s*\**(\d{1,3})\**" % DASH)
#: a header that is ABOUT trends (so the rows under it are trend rows).
H_TREND_CTX = re.compile(r"^#+.*[Tt]endencias?\b", re.I)
#: any header, to track the nearest preceding one.
H_ANY = re.compile(r"^#+\s")
#: form 3 -- a table row whose first cell is a bold integer.
ROW = re.compile(r"^\|\s*\**(\d{1,3})\**\s*\|")

#: a citation: "tendencia 216", "tendencias 213, 216 y 217", "tendencias 197-210".
#: A separator must not require whitespace that the previous `\s*` already ate.
#: Pase 49's own control caught this: "las tendencias 213, 216 y 217" returned
#: only [213, 216], because `\s*(?:\sy\s)?\s*` can never match -- the space
#: before "y" is consumed first. It is the same shape of defect as the `\b`
#: that cost pase 47 44 % of its figure inventory: a lossy extractor reports a
#: smaller, confident number.
CITE = re.compile(
    r"tendencias?\s+((?:\**\d{1,3}\**(?:\s*(?:%s|,|\by\b|\be\b)\s*)?)+)" % DASH,
    re.I)
NUM = re.compile(r"\d{1,3}")


def defined_trends(path):
    """Every trend number this base DEFINES, with the form that defines it."""
    defs = {}
    ctx_is_trends = False
    for lineno, line in enumerate(open(path).read().split("\n"), 1):
        if H_ANY.match(line):
            ctx_is_trends = bool(H_TREND_CTX.match(line))
            m = H_RANGE.match(line)
            if m:
                lo, hi = int(m.group(1)), int(m.group(2))
                if lo <= hi and hi - lo < 100:
                    for n in range(lo, hi + 1):
                        defs.setdefault(n, ("range-header", lineno))
                continue
            m = H_NUM.match(line)
            if m:
                defs.setdefault(int(m.group(1)), ("numbered-header", lineno))
            continue
        if ctx_is_trends:
            m = ROW.match(line)
            if m:
                defs.setdefault(int(m.group(1)), ("table-row", lineno))
    return defs


def citations():
    """Every trend citation in the eight files."""
    out = []
    for rel in KB_FILES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        for lineno, line in enumerate(open(path).read().split("\n"), 1):
            for m in CITE.finditer(line):
                blob = m.group(1)
                nums = [int(x) for x in NUM.findall(blob)]
                ranged = re.search(r"\d\s*%s\s*\d" % DASH, blob) and len(nums) == 2
                if ranged and nums[0] < nums[1] and nums[1] - nums[0] < 100:
                    nums = list(range(nums[0], nums[1] + 1))
                for n in nums:
                    out.append((rel, lineno, n, re.sub(r"\s+", " ", line).strip()))
    return out


def main():
    defs = defined_trends(os.path.join(ROOT, TRENDS_FILE))
    cites = citations()
    tsv = "--tsv" in sys.argv

    if tsv:
        print("file\tline\ttrend\tresolved\tform")
        for rel, lineno, n, _ in cites:
            form = defs.get(n, ("DANGLING", 0))[0]
            print("%s\t%d\t%d\t%s\t%s" % (rel, lineno, n,
                                          "yes" if n in defs else "NO", form))
        return 0

    forms = {}
    for n, (form, _) in defs.items():
        forms[form] = forms.get(form, 0) + 1
    print("-- trend DEFINITIONS in %s --" % TRENDS_FILE)
    for form in sorted(forms):
        print("  %-16s %4d" % (form, forms[form]))
    print("  %-16s %4d  (max %d)" % ("TOTAL", len(defs), max(defs) if defs else 0))

    missing = sorted(set(range(1, max(defs) + 1)) - set(defs)) if defs else []
    print("\n-- numbers with NO definition, below the maximum --")
    print("  %d: %s" % (len(missing), ", ".join(map(str, missing)) or "none"))

    print("\n-- every trend CITATION, resolved --")
    dangling = [c for c in cites if c[2] not in defs]
    by_file = {}
    for rel, lineno, n, _ in cites:
        by_file.setdefault(rel, [0, 0])
        by_file[rel][0] += 1
        if n not in defs:
            by_file[rel][1] += 1
    print("  %-26s %8s %9s" % ("file", "cites", "dangling"))
    for rel in KB_FILES:
        if rel in by_file:
            print("  %-26s %8d %9d" % (rel, by_file[rel][0], by_file[rel][1]))
    print("  %-26s %8d %9d" % ("TOTAL", len(cites), len(dangling)))

    if dangling:
        print("\n-- DANGLING: cited and never defined --")
        seen = set()
        for rel, lineno, n, ctx in dangling:
            if (rel, lineno, n) in seen:
                continue
            seen.add((rel, lineno, n))
            print("  %s:%d  tendencia %d" % (rel, lineno, n))
            print("      %s" % ctx[:150])
    else:
        print("\n  no dangling citation: every cited trend resolves.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
