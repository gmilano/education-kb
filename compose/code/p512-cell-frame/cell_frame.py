#!/usr/bin/env python3
"""p512 — the star-cell frame, defined by TABLE STRUCTURE rather than by typography.

Why this exists
---------------
p510 framed its star-cell census on BOLDED cells; p511 framed on the live shelves'
star cells classified by provenance suffix and roundness. Both frames are features
of the WRITING, and p512 measured what they cost:

    bolded cells wrong 8/30 = 27 %      plain cells wrong 17/61 = 28 %

Typography does not discriminate. Roundness does (82 % vs 15 %) but with only
56 % recall, so it is a SCREEN and never a verdict. Framed on the table's own
`★` column instead, 39 cells were wrong against p511's four.

Two arms, and only one of them needs the adjacency safeguard
------------------------------------------------------------
COLUMN ARM  — a table header names a `★` column, so the column is read BY INDEX and
              the address comes from the repo column. No adjacency needed.
              Requiring one-address-per-row (Gap 509-B's safeguard) excluded
              26 of 119 cells (22 %) and 2 of the 26 were wrong -> Gap 512-C.
PROSE ARM   — `NNN★` inline. Here there is no column to index, so the single-address
              precondition DOES apply, and it still produces false positives when a
              line correctly QUOTES a wrong historical value (Gap 511-A's class,
              tenth instance: educhain's "~12,000★ was a stale carry").

Checks
------
check_against_api(api)  every shelf cell equals its p512 API read
check_agreement()       Gap 512-B: an address with cells in >1 live file must agree

Both ran green at p512: 111 re-read cells 0 wrong; 39 multiply-present addresses
0 disagreeing. `make hooks` was DENIED this pass, so this is the attestation.
"""
import re, sys, collections, os

LIVE = ["agents/top.md", "repos/foundations.md", "verticals/solutions.md",
        "intel/market.md", "intel/trends.md", "compose/patterns.md"]
ADDR = re.compile(r'github\.com/([A-Za-z0-9][\w.-]*)/([\w.-]+?)(?=[)\]`,.\s]|$)')
STARHDR = re.compile(r'^\s*(★|stars?)\s*$', re.I)
NUMCELL = re.compile(r'^\s*\*{0,2}([\d,]+)\*{0,2}\s*★?\s*(?:\s*\*\(.*\)\*)?\s*$')


def _cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def column_arm(root='.'):
    """Yield (file, line, slug, cell_text) for every star-COLUMN cell in the live files."""
    for f in LIVE:
        path = os.path.join(root, f)
        lines = open(path, encoding='utf-8').read().split('\n')
        h1 = next(i for i, l in enumerate(lines) if l.startswith('# '))
        # compose/patterns.md titles its live recipes "## 🆕 Pnnn-1", so it has no
        # history boundary -- the whole file is current. The others stop at the
        # first "## 🆕" after the H1, which is where the dated history begins.
        stop = (len(lines) if f == "compose/patterns.md"
                else next((i for i in range(h1 + 1, len(lines))
                           if lines[i].startswith('## 🆕')), len(lines)))
        col = None
        for i in range(h1, stop):
            line = lines[i]
            if not line.lstrip().startswith('|'):
                col = None
                continue
            c = _cells(line)
            if col is None:
                hits = [k for k, v in enumerate(c) if STARHDR.match(v.replace('*', ''))]
                if hits:
                    col = hits[0]
                continue
            if set(''.join(c)) <= set('-: ') or col >= len(c):
                continue
            m = NUMCELL.match(c[col])
            if not m:
                continue
            slug = None
            for k in range(col):          # the address is left of the star column
                g = ADDR.search(c[k])
                if g:
                    slug = f"{g.group(1)}/{g.group(2)}"
                    break
            if slug:
                yield f, i + 1, slug, m.group(1)


def check_against_api(api, root='.'):
    bad = []
    n = 0
    for f, ln, slug, txt in column_arm(root):
        if slug not in api:
            continue
        n += 1
        if api[slug] != int(txt.replace(',', '')):
            bad.append((f, ln, slug, txt, api[slug]))
    return n, bad


def check_agreement(root='.'):
    seen = collections.defaultdict(list)
    for f, ln, slug, txt in column_arm(root):
        seen[slug].append((f, ln, txt))
    multi = {k: v for k, v in seen.items() if len(v) > 1}
    bad = {k: v for k, v in multi.items()
           if len({t.replace(',', '') for _, _, t in v}) > 1}
    return len(multi), bad


if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    api = {}
    if len(sys.argv) > 2:
        for l in open(sys.argv[2]):
            s, v = l.rstrip('\n').split('\t')
            api[s] = int(v)
        n, bad = check_against_api(api, root)
        print(f"API agreement: {n} cells re-read, {len(bad)} wrong")
        for b in bad:
            print("  🔴", b)
    m, dis = check_agreement(root)
    print(f"Cross-file agreement (Gap 512-B): {m} addresses in >1 live file, {len(dis)} disagreeing")
    for k, v in dis.items():
        print("  🔴", k, v)
    sys.exit(1 if dis or (api and bad) else 0)
