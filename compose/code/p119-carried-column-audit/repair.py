#!/usr/bin/env python3
"""p119 star repair. Driven ONLY by this pass's verdict + claims files, so it
cannot touch a cell the sweep did not measure.

Keyed on the RAW cell text the extractor captured, not on a re-derived string:
four of the seven wrong cells are written in k-form ("1.2k", "1.1k", "1.3k"),
so a repair that searched for the PARSED integer found nothing and silently
no-opped. A no-op that prints nothing is how a repair pass reports success it
did not achieve, so every miss is printed and counted.

Rounded cells are rewritten to the exact measured count on purpose: "1.2k" was
never a measurement, and leaving it rounded preserves the very defect P119-A
is about.
"""
import re, sys, csv

def fmt(n):
    s = str(n)
    if len(s) <= 4:
        return s
    parts = []
    while len(s) > 3:
        parts.insert(0, s[-3:]); s = s[:-3]
    parts.insert(0, s)
    return ' '.join(parts)

def load(claims_path, verdict_path):
    raws = {}
    for r in csv.reader(open(claims_path, encoding='utf-8'), delimiter='\t'):
        if len(r) >= 7:
            raws[(r[1], r[2], r[3], r[5])] = r[4]
    jobs = []
    for r in csv.reader(open(verdict_path, encoding='utf-8'), delimiter='\t'):
        if len(r) >= 8 and r[0] == 'WRONG':
            key = (r[2], r[3], r[4], r[5])
            jobs.append((r[2], int(r[3]), r[4], raws.get(key, r[5]), int(r[6])))
    return jobs

def main(claims_path, verdict_path, apply):
    jobs = load(claims_path, verdict_path)
    by_page = {}
    for p, ln, slug, raw, meas in jobs:
        by_page.setdefault(p, []).append((ln, slug, raw, meas))

    fixed = missed = 0
    for page, items in sorted(by_page.items()):
        text = open(page, encoding='utf-8').read().split('\n')
        for ln, slug, raw, meas in sorted(items):
            old = text[ln - 1]
            want = fmt(meas)
            # strip the raw token of decoration, then match it as a whole number
            core = re.sub(r'^[^\d~]*|[^\dkK]*$', '', raw).strip()
            new = old
            for cand in (core, raw.strip()):
                if not cand:
                    continue
                pat = r'(?<!\d)' + re.escape(cand) + r'(?!\d)'
                if re.search(pat, new):
                    new = re.sub(pat, want, new, count=1)
                    break
            if new == old:
                print(f'  !! MISS {page}:{ln} {slug} raw={raw!r} -> {want}')
                missed += 1
                continue
            text[ln - 1] = new
            fixed += 1
            print(f'  {page}:{ln} {slug}  {raw} -> {want}')
        if apply:
            open(page, 'w', encoding='utf-8').write('\n'.join(text))
    tag = '' if apply else '  (DRY RUN)'
    print(f'\n{fixed} repaired, {missed} missed, {len(jobs)} targeted{tag}')
    return 1 if missed else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], '--apply' in sys.argv))
