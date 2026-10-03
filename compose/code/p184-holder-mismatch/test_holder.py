#!/usr/bin/env python3
"""Controls for P184.  Rule 2 of P126: a positive control only enables an instrument if it
exercises the case where the instrument can FAIL.  The case that matters here is a holder
that is a real, unrelated legal entity on a project that is not theirs -- so the control
pair is THU-MAIC/OpenMAIC (must MATCH) and MaybeItsAdam/tutors (must be UNRELATED).  The
two have different vocabularies: one holder is the org handle itself, the other is a
third-party company.  A control built only from matching pairs would pass without ever
exercising the detection."""
import sys
from extract_holder import classify, holder

MIT = 'MIT License\n\nCopyright (c) {y} {h}\n\nPermission is hereby granted, free of charge, to any person'
APACHE_APPENDIX = ('''                                 Apache License
                           Version 2.0, January 2004

   APPENDIX: How to apply the Apache License to your work.

      Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");''')

CASES = [
    # (name, slug, text, expected verdict, expected holder substring or None)
    ('match: holder IS the org handle',
     'THU-MAIC/OpenMAIC', MIT.format(y=2026, h='THU-MAIC'), 'HOLDER-MATCH', 'THU-MAIC'),
    ('match: separators differ (THU-MAIC vs Thu Maic)',
     'THU-MAIC/OpenMAIC', MIT.format(y=2026, h='Thu Maic'), 'HOLDER-MATCH', 'Thu Maic'),
    ('THE CASE THAT MATTERS: third-party company as holder',
     'MaybeItsAdam/tutors', MIT.format(y=2024, h='tldraw Inc.'), 'HOLDER-UNRELATED', 'tldraw Inc'),
    ('match: holder is the repo name, not the owner',
     'adity982/OpenTutor', MIT.format(y=2026, h='OpenTutor Authors'), 'HOLDER-MATCH', 'OpenTutor'),
    ('unrelated: a personal name on a handle that does not spell it',
     'adity982/OpenTutor', MIT.format(y=2026, h='Zijin Zhang'), 'HOLDER-UNRELATED', 'Zijin Zhang'),
    ('no holder: the Apache appendix ships its placeholder unfilled',
     '1EdTech/OpenCASE', APACHE_APPENDIX, 'NO-HOLDER', None),
    ('no holder: bracketed placeholder is not a holder',
     'x/y', MIT.format(y=2026, h='[fullname]'), 'NO-HOLDER', None),
    ('no holder: "year" placeholder is not a holder',
     'x/y', 'Copyright (c) [year] [your name]\n\nPermission is hereby granted', 'NO-HOLDER', None),
    ('holder survives a trailing "All rights reserved."',
     'GibbonEdu/core', 'Copyright (c) 2026 Gibbon Foundation. All rights reserved.',
     'HOLDER-MATCH', 'Gibbon Foundation'),
    ('GPL header form: holder after a year range',
     'marcusgreen/moodle-tool_aiconnect',
     '@copyright 2024-2026 Marcus Green\nThis program is free software',
     'HOLDER-MATCH', 'Marcus Green'),
]

REAL = [
    # D6 controls, built from the REAL texts and not from excerpts.  The first build of this
    # instrument passed a trimmed Apache fixture and still published a sentence of the full
    # text as a holder -- rule 2 of P126, failed on this very module: a control only enables
    # an instrument if it exercises the case where the instrument can fail, and an excerpt is
    # not the case.
    ('D6 Apache-2.0, FULL real text: no holder, and no sentence published as one',
     'HKUDS/DeepTutor', 'fixtures/apache-2.0-deeptutor.txt', 'Apache-2.0', 'NOT-APPLICABLE'),
    ('D7 Apache-2.0, FULL real text, family WITHHELD: the instrument REFUSES, not guesses',
     'HKUDS/DeepTutor', 'fixtures/apache-2.0-deeptutor.txt', None, 'FAMILY-REQUIRED'),
    ("D6 GPL-3.0, FULL real text: the FSF's copyright on the TEXT is not the project's",
     'moodle/moodle', 'fixtures/gpl-3.0-moodle-COPYING.txt', 'GPL', 'NOT-APPLICABLE'),
    ('D7 GPL-3.0, FULL real text, family WITHHELD: the instrument REFUSES, not guesses',
     'moodle/moodle', 'fixtures/gpl-3.0-moodle-COPYING.txt', None, 'FAMILY-REQUIRED'),
]


def main():
    n = ok = 0
    for name, slug, text, want_v, want_h in CASES:
        got_v, got_h = classify(slug, text, 'MIT')
        n += 1
        good = got_v == want_v
        if good and want_h:
            good = want_h.lower() in got_h.lower()
        if good:
            ok += 1
            print(f'PASS {name}')
        else:
            print(f'FAIL {name}: want {want_v}/{want_h!r}, got {got_v}/{got_h!r}')
    for name, slug, path, fam, want_v in REAL:
        n += 1
        try:
            text = open(path, encoding='utf-8', errors='replace').read()
        except OSError as e:
            print(f'FAIL {name}: fixture missing ({e})')
            continue
        got_v, got_h = classify(slug, text, fam)
        if got_v == want_v:
            ok += 1
            print(f'PASS {name}')
        else:
            print(f'FAIL {name}: want {want_v}, got {got_v}/{got_h!r}')

    # The negative control, stated as its own assertion: an instrument that accepted any
    # copyright line would call the Apache appendix a holder.  This asserts it does not.
    n += 1
    if holder(APACHE_APPENDIX) is None:
        ok += 1
        print('PASS negative control: the unfilled Apache appendix yields NO holder')
    else:
        print(f'FAIL negative control: got {holder(APACHE_APPENDIX)!r}')
    print(f'\n{ok}/{n} checks passed')
    return 0 if ok == n else 1

if __name__ == '__main__':
    sys.exit(main())
