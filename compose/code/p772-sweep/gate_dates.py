#!/usr/bin/env python3
"""p772 — `gate-dates`, written from scratch after `make hooks` was denied a THIRD
consecutive session. ACTION p771-A named this gate specifically, because it is
"mechanically checkable without any repository code".

Contract (ACTION p279, as stated in the Makefile's own target description):
    THE KB MAY NOT *ASSERT* A DATE IT HAS ALREADY REFUTED.

Four dispositions for an occurrence of a refuted date, after the repo's own
documented classes (ASSERTED / ATTRIBUTED / QUOTED / CORRECTED):
    CORRECTED  — the occurrence sits on the line that records the refutation
    ATTRIBUTED — the occurrence names whose claim it is
    QUOTED     — the occurrence is inside a code span or quotation marks
    ASSERTED   — none of the above  => VIOLATION

Second, independent contract, needing no repository code:
    NO MEASUREMENT DATE MAY BE IN THE FUTURE.

No part of this file is copied from the repository's gate suite.
"""
import re, sys, datetime

ISO = re.compile(r'(?<![\d-])(20\d\d)-(\d{2})-(\d{2})(?![\d-])')
MONTHS = ('january february march april may june july august september october '
          'november december').split()
PROSE = re.compile(r'\b(\d{1,2})?\s*(' + '|'.join(MONTHS) + r')\s+(20\d\d)\b', re.I)

REFUTE = re.compile(
    r'refut|falsif|contradict|withdraw|unsettled|contested|disput|'
    r'is wrong|was wrong|no longer|supersed|retract|not the (?:date|figure)|'
    r'does not hold|corrected to|rather than', re.I)
# D6: a refutation must sit NEAR the date it refutes. These shelves hold
# 2,000-character paragraphs, so "same line" is not "about this date".
NEAR = 120
ATTRIB = re.compile(
    r'according to|per the|reports?|claims?|states?|attributed|'
    r'source[ds]?|—\s*[A-Z]|\bDfE\b|\bNCES\b|\bINEP\b|\bACARA\b|\bOECD\b|'
    r'aggregator|tracker|compilation|third-party|search-sourced', re.I)

MEASURED = re.compile(
    r'measured|probed|researched|verified|recorded|as at|as of|'
    r'byte-read|enumerated|updated:|sweep|this pass|retrieved|observed', re.I)

def spans_in_code_or_quotes(line):
    out = []
    for m in re.finditer(r'`[^`]*`|"[^"]*"|“[^”]*”|\*"[^"]*"\*', line):
        out.append(m.span())
    return out

def inside(pos, spans):
    return any(a <= pos < b for a, b in spans)

def near_refute(line, pos):
    return REFUTE.search(line[max(0, pos - NEAR):pos + NEAR]) is not None

def classify(line, pos):
    if near_refute(line, pos):
        return 'CORRECTED'
    if inside(pos, spans_in_code_or_quotes(line)):
        return 'QUOTED'
    if ATTRIB.search(line):
        return 'ATTRIBUTED'
    return 'ASSERTED'

def harvest_refuted(files):
    """A date is REFUTED if it appears on a line that records a refutation."""
    refuted = {}
    for path in files:
        for ln, line in enumerate(open(path, encoding='utf-8'), 1):
            if not REFUTE.search(line):
                continue
            for m in ISO.finditer(line):
                if near_refute(line, m.start()):
                    refuted.setdefault(m.group(0), []).append((path, ln))
            for m in PROSE.finditer(line):
                if near_refute(line, m.start()):
                    key = re.sub(r'\s+', ' ', m.group(0)).strip().lower()
                    refuted.setdefault(key, []).append((path, ln))
    return refuted

def run(files, today):
    refuted = harvest_refuted(files)
    violations, future = [], []
    for path in files:
        for ln, line in enumerate(open(path, encoding='utf-8'), 1):
            for m in ISO.finditer(line):
                d = m.group(0)
                try:
                    dt = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                except ValueError:
                    continue
                if (dt > today and MEASURED.search(line[max(0, m.start()-90):m.start()+90])
                        and not inside(m.start(), spans_in_code_or_quotes(line))):
                    future.append((path, ln, d))
                if d in refuted and classify(line, m.start()) == 'ASSERTED':
                    violations.append((path, ln, d, 'ASSERTED'))
            for m in PROSE.finditer(line):
                key = re.sub(r'\s+', ' ', m.group(0)).strip().lower()
                if key in refuted and classify(line, m.start()) == 'ASSERTED':
                    violations.append((path, ln, key, 'ASSERTED'))
    return refuted, violations, future

# ---------------- self-test: 10 controls, positive and negative ----------------
def selftest():
    import tempfile, os
    today = datetime.date(2026, 11, 11)
    cases = [
        # (text, expect_violation, label)
        ('🔴 The August 2026 date is refuted; the Omnibus moves it.\nAnnex III applies from August 2026.\n',
         True,  'P1 asserted after refutation'),
        ('🔴 The August 2026 date is refuted.\nAccording to the tracker, August 2026 was reported.\n',
         False, 'N1 ATTRIBUTED is allowed'),
        ('🔴 The August 2026 date is refuted.\nThe source says `August 2026` in a code span.\n',
         False, 'N2 QUOTED is allowed'),
        ('🔴 August 2026 is refuted and withdrawn here.\n',
         False, 'N3 CORRECTED line itself is allowed'),
        ('Nothing is refuted in this file at all.\nAnnex III applies from August 2026.\n',
         False, 'N4 never-refuted date is allowed'),
        ('🔴 2026-05-15 was contradicted by the release.\nThe register was measured 2026-05-15.\n',
         True,  'P2 ISO asserted after refutation'),
        ('A measurement dated 2027-01-01 appears here.\n',
         False, 'N5 future date is a separate finding, not a violation'),
        ('🔴 The 24,820 figure is wrong.\nThe spread is recorded, not averaged.\n',
         False, 'N6 no date, no finding'),
        # D6 control: a severity marker is not a refutation.
        ('🔴 A red finding mentioning August 2026 as a plain severity note.\n'
         'Annex III applies from August 2026.\n',
         False, 'N8 D6: red marker alone does not refute a date'),
        # D6 control: refutation far away in a long paragraph is not about this date.
        ('The figure is refuted. ' + 'filler word ' * 40 + 'August 2026 stands here.\n'
         'Annex III applies from August 2026.\n',
         False, 'N9 D6: refutation >120 chars away is not about this date'),
    ]
    passed = failed = 0
    for text, expect, label in cases:
        fd, p = tempfile.mkstemp(suffix='.md'); os.close(fd)
        open(p, 'w').write(text)
        _, v, _ = run([p], today)
        got = len(v) > 0
        ok = (got == expect)
        passed += ok; failed += (not ok)
        print(f'   {"PASS" if ok else "FAIL"}  {label}  (violations={len(v)})')
        os.unlink(p)
    # future-date control
    fd, p = __import__('tempfile').mkstemp(suffix='.md'); __import__('os').close(fd)
    open(p, 'w').write('Measured 2027-03-04 in the future.\n')
    _, _, fut = run([p], today)
    ok = len(fut) == 1
    print(f'   {"PASS" if ok else "FAIL"}  P3 future measurement date detected  (future={len(fut)})')
    passed += ok; failed += (not ok)
    __import__('os').unlink(p)
    fd, p = __import__('tempfile').mkstemp(suffix='.md'); __import__('os').close(fd)
    open(p, 'w').write('The Regulation applies from 2027-12-02 in all member states.\n')
    _, _, fut = run([p], today)
    ok = len(fut) == 0
    print(f'   {"PASS" if ok else "FAIL"}  N10 D7: a future LEGAL date is not a future measurement  (future={len(fut)})')
    passed += ok; failed += (not ok)
    __import__('os').unlink(p)
    fd, p = __import__('tempfile').mkstemp(suffix='.md'); __import__('os').close(fd)
    open(p, 'w').write('Measured 2026-11-11, which is today.\n')
    _, _, fut = run([p], today)
    ok = len(fut) == 0
    print(f'   {"PASS" if ok else "FAIL"}  N7 today is not future  (future={len(fut)})')
    passed += ok; failed += (not ok)
    __import__('os').unlink(p)
    print(f'   {passed} passed, {failed} failed')
    return failed == 0

if __name__ == '__main__':
    if '--self-test' in sys.argv:
        print('gate-dates self-test (13 controls):')
        sys.exit(0 if selftest() else 1)
    files = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    today = datetime.date(2026, 11, 11)
    refuted, violations, future = run(files, today)
    print(f'shelves scanned        : {len(files)}')
    print(f'refuted date records   : {len(refuted)}')
    print(f'ASSERTED violations    : {len(violations)}')
    print(f'future measurement dates: {len(future)}')
    print()
    for path, ln, d, k in violations[:40]:
        print(f'  🔴 {path}:{ln}  asserts refuted date  {d!r}')
    if len(violations) > 40:
        print(f'  ... and {len(violations)-40} more')
    print()
    for path, ln, d in future[:20]:
        print(f'  🔴 {path}:{ln}  future measurement date {d}')
    sys.exit(1 if (violations or future) else 0)
