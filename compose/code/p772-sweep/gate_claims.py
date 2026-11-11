#!/usr/bin/env python3
"""p772 — `gate-dates`, SUBJECT-BOUND form. Written from scratch.

The bare-date form of ACTION p279's contract is unimplementable on this base and
p772 proved why: the standard pass heading is

    "## Pass 406 — reads and commit both 2026-10-23 — ... REFUTES ..."

so every pass date sits within 120 characters of a refutation verb that refers to
a GAP PREMISE, not to the date. 2,897 "violations" are that artefact.

A date is not a claim. The checkable unit is a (SUBJECT, DATE) pair that this base
has itself recorded as contradicted. Those pairs are declared here, from the base's
own 'Primary verification' row at intel/open-gaps.md, and each occurrence is graded
ASSERTED / ATTRIBUTED / QUOTED / CORRECTED.
"""
import re, sys, json

# Contested claims, each taken verbatim from this base's own record of contradiction.
CLAIMS = [
    # RESOLVED AT p772 by T752. Reg. (EU) 2026/1744 (in force 27 July 2026) moved the
    # Annex III education obligations from 2 August 2026 to 2 December 2027, so BOTH
    # dates were correct, on either side of the Omnibus. '2 December 2027' is now the
    # settled value and may be asserted freely; only the SUPERSEDED 'August 2026'
    # still needs attribution, and that is the only thing this claim now checks.
    {'id': 'C1-euaiact-annexiii-SUPERSEDED-DATE',
     'subject': r'annex\s*iii|ai act|high-risk',
     'dates': [r'(?:2\s*)?august\s*2026', r'2026-08-02'],
     'why': "RESOLVED at p772 (T752): the Annex III education date is 2 December 2027. "
            "'August 2026' is correct-but-SUPERSEDED and may not be asserted bare"},
    {'id': 'C2-england-statutory-guidance',
     'subject': r'supporting pupils (?:at school )?with medical conditions|'
                r's\.?\s*100\b|section\s*100\b|children and families act',
     'dates': [r'september\s*2026'],
     'why': "p771 'Primary verification': whether England's replacement statutory "
            "guidance was ever FINALLY PUBLISHED; in force *intended* September 2026"},
]

ATTRIB = re.compile(
    r'according to|per the|reports?|claims?|states?|attributed|contradict|'
    r'source[ds]?|aggregator|tracker|compilation|third-party|search-sourced|'
    r'unsettled|not endorsed|intended|consultation|one source|directly', re.I)
REFUTE = re.compile(
    r'refut|falsif|contradict|withdraw|unsettled|contested|disput|'
    r'is wrong|no longer|supersed|retract|not settled|NOT OBTAINED', re.I)
NEAR = 200

def code_or_quote_spans(line):
    return [m.span() for m in re.finditer(r'`[^`]*`|"[^"]*"|“[^”]*”', line)]

def grade(line, pos):
    w = line[max(0, pos - NEAR):pos + NEAR]
    if REFUTE.search(w):
        return 'CORRECTED'
    if any(a <= pos < b for a, b in code_or_quote_spans(line)):
        return 'QUOTED'
    if ATTRIB.search(w):
        return 'ATTRIBUTED'
    return 'ASSERTED'

def main(listfile):
    files = [l.strip() for l in open(listfile) if l.strip()]
    tally = {c['id']: {'ASSERTED': [], 'ATTRIBUTED': 0, 'QUOTED': 0, 'CORRECTED': 0}
             for c in CLAIMS}
    for path in files:
        for ln, line in enumerate(open(path, encoding='utf-8'), 1):
            for c in CLAIMS:
                if not re.search(c['subject'], line, re.I):
                    continue
                for dpat in c['dates']:
                    for m in re.finditer(dpat, line, re.I):
                        g = grade(line, m.start())
                        if g == 'ASSERTED':
                            tally[c['id']]['ASSERTED'].append((path, ln, m.group(0)))
                        else:
                            tally[c['id']][g] += 1
    import collections
    total_bad = 0
    for c in CLAIMS:
        fc = collections.Counter(a[0] for a in tally[c['id']]['ASSERTED'])
        tally[c['id']]['byfile'] = fc
    for c in CLAIMS:
        t = tally[c['id']]
        print(f"── {c['id']}")
        print(f"   why contested: {c['why']}")
        print(f"   CORRECTED {t['CORRECTED']:4d} · ATTRIBUTED {t['ATTRIBUTED']:4d} · "
              f"QUOTED {t['QUOTED']:4d} · 🔴 ASSERTED {len(t['ASSERTED']):4d}")
        if t['byfile']:
            print('   ASSERTED by shelf: ' + ' · '.join(f'{k}={v}' for k, v in t['byfile'].most_common()))
        for path, ln, d in t['ASSERTED'][:6]:
            print(f"      🔴 {path}:{ln} asserts {d!r} as fact")
        if len(t['ASSERTED']) > 6:
            print(f"      ... and {len(t['ASSERTED'])-6} more")
        total_bad += len(t['ASSERTED'])
        print()
    print(f"gate-dates (subject-bound): {total_bad} ASSERTED violation(s)")
    return 1 if total_bad else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
