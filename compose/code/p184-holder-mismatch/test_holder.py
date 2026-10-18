#!/usr/bin/env python3
"""Controls for P184.  Rule 2 of P126: a positive control only enables an instrument if it
exercises the case where the instrument can FAIL.  The case that matters here is a holder
that is a real, unrelated legal entity on a project that is not theirs -- so the control
pair is THU-MAIC/OpenMAIC (must MATCH) and MaybeItsAdam/tutors (must be UNRELATED).  The
two have different vocabularies: one holder is the org handle itself, the other is a
third-party company.  A control built only from matching pairs would pass without ever
exercising the detection."""
import sys
from extract_holder import classify, holder, dated_holder, looks_like_prose

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
    # 🔴 p280 (`p279` item 2, generalised): THESE TWO ROWS NAMED REAL REPOSITORIES AND
    # ASSERTED PAYLOADS THEY DO NOT SERVE -- and this table runs EVERY row under the
    # `'MIT'` family, so they also claimed a family both repositories contradict.
    # Read first-hand 2026-10-18: `GibbonEdu/core`'s `LICENSE` is the verbatim GPL-3.0
    # text (35 121 B) whose ONLY copyright line is the FSF's own, and
    # `marcusgreen/moodle-tool_aiconnect`'s `version.php` carries `@copyright 2024 Marcus
    # Green` -- a SINGLE year, not the range the control asserted.
    # 🔵 The row's subject is the PREDICATE, not either repository, so the fix is not to
    # delete the control: it is to give it a DECLARED SYNTHETIC subject, and to assert the
    # real repositories in `REAL[]`, which is the convention this very file already owns.
    # 🔵 And the synthetic has to CARRY THE PROPERTY the control relies on: the first
    # replacement (`example/aiconnect-shaped`) turned a HOLDER-MATCH control into
    # HOLDER-UNRELATED, because the predicate under test matches the holder against the
    # SLUG'S OWN TOKENS and `marcusgreen` is what spells `Marcus Green`.  A synthetic
    # subject is not a free rename.
    ('holder survives a trailing "All rights reserved."',
     'example/gibbon-shaped', 'Copyright (c) 2026 Gibbon Foundation. All rights reserved.',
     'HOLDER-MATCH', 'Gibbon Foundation'),
    ('GPL header form: holder after a year range',
     'example/marcusgreen-aiconnect',
     '@copyright 2024-2026 Marcus Green\nThis program is free software',
     'HOLDER-MATCH', 'Marcus Green'),
]

REAL = [
    # D6 controls, built from the REAL texts and not from excerpts.  The first build of this
    # instrument passed a trimmed Apache fixture and still published a sentence of the full
    # text as a holder -- rule 2 of P126, failed on this very module: a control only enables
    # an instrument if it exercises the case where the instrument can fail, and an excerpt is
    # not the case.
    # 🔴 p280: THIS CONTROL'S OWN FIXTURE REFUTES IT.  `DeepTutor`'s real Apache-2.0
    # `LICENSE` FILLS the appendix -- `Copyright 2025 Data Intelligence Lab, The University
    # of Hong Kong` -- so "no holder" was never true of this payload; the instrument simply
    # could not see it, and the control asserted the blindness as the answer.
    # 🟡 The verdict is `HOLDER-UNRELATED` and that is the INSTRUMENT's honest limit, not a
    # fork signal: `HKUDS` is HKU's Data Science group, so the holder and the account ARE
    # the same institution and no token test bridges the acronym.  `p184`'s own rule applies
    # -- HOLDER-UNRELATED shortens the reading list, it does not decide it.
    ('D6 Apache-2.0, FULL real text: the FILLED appendix holder is read (p280)',
     'HKUDS/DeepTutor', 'fixtures/apache-2.0-deeptutor.txt', 'Apache-2.0',
     'HOLDER-UNRELATED'),
    ('D7 Apache-2.0, FULL real text, family WITHHELD: the instrument REFUSES, not guesses',
     'HKUDS/DeepTutor', 'fixtures/apache-2.0-deeptutor.txt', None, 'FAMILY-REQUIRED'),
    ("D6 GPL-3.0, FULL real text: the FSF's copyright on the TEXT is not the project's",
     'moodle/moodle', 'fixtures/gpl-3.0-moodle-COPYING.txt', 'GPL', 'NOT-APPLICABLE'),
    ('D7 GPL-3.0, FULL real text, family WITHHELD: the instrument REFUSES, not guesses',
     'moodle/moodle', 'fixtures/gpl-3.0-moodle-COPYING.txt', None, 'FAMILY-REQUIRED'),

    # 🟢 p280: the two rows above, as the repositories actually serve them.  Captured with
    # `slug/ref/head_sha/sha256/date` in `pass280-package-provenance/fixtures/PROVENANCE.tsv`.
    ('p280 GibbonEdu/core REAL GPL-3.0 FILLS its appendix: the holder IS in the text',
     'GibbonEdu/core',
     '../pass280-package-provenance/fixtures/GibbonEdu-core.LICENSE.txt',
     'GPL-3.0', 'HOLDER-MATCH'),
    ('p280 moodle-tool_aiconnect REAL version.php: the source header DOES carry the holder',
     'marcusgreen/moodle-tool_aiconnect',
     '../pass280-package-provenance/fixtures/moodle-tool_aiconnect.version.php',
     'MIT', 'HOLDER-MATCH'),

    # D8 controls, added 2026-10-07 (pass 25).  The 503-slug shelf sweep returned 61
    # HOLDER-UNRELATED rows and SEVEN of them were the instrument misreading a licence
    # with NO holder.  `\s*` between "copyright" and the capture matches a NEWLINE, so
    # `Copyright (c) 2026` followed by a blank line adopted the next paragraph as its
    # holder; and `\bholder\b` does not match the plural in `... COPYRIGHT HOLDERS BE
    # LIABLE ...`.  All four fixtures are the REAL payloads, byte-for-byte, not excerpts.
    ('D8 MIT, year present and NO name: must be NO-HOLDER, not the next paragraph',
     'AbdelStark/eu-ai-act-toolkit', 'fixtures/d8-mit-year-only-eu-ai-act-toolkit.txt',
     'MIT', 'NO-HOLDER'),
    ('D8 MIT, GitHub template placeholder shipped verbatim: NO-HOLDER',
     'lebmatter/exampro', 'fixtures/d8-mit-template-placeholder-exampro.txt',
     'MIT', 'NO-HOLDER'),
    ('D8 MIT, copyright line deleted entirely: NO-HOLDER, not the warranty clause',
     'adlnet/lrs-conformance-test-suite', 'fixtures/d8-mit-no-copyright-line-adlnet.txt',
     'MIT', 'NO-HOLDER'),
    # D8 POSITIVE control.  Three negatives alone would pass an instrument that returned
    # NO-HOLDER for everything; this is the row that forbids that fix.
    ('D8 positive: a REAL filled MIT holder is still read, and is UNRELATED to the account',
     'academic-innovation/django-lti', 'fixtures/d8-mit-filled-holder-django-lti.txt',
     'MIT', 'HOLDER-UNRELATED'),
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

    # 🟢 p280: THE DISCRIMINATING PAIR.  The `by construction` argument was validated on an
    # UNFILLED appendix only, so the two arms are asserted against the two real payloads
    # that differ in exactly that respect -- one file, one difference, two verdicts.
    for label, path, want in (
            ('a FILLED GPL-3.0 appendix yields its holder',
             '../pass280-package-provenance/fixtures/GibbonEdu-core.LICENSE.txt',
             'Gibbon Foundation'),
            ('an UNFILLED GPL-3.0 appendix yields NO holder',
             'fixtures/gpl-3.0-moodle-COPYING.txt', None)):
        n += 1
        got = holder(open(path, encoding='utf-8', errors='replace').read())
        if got == want:
            ok += 1
            print('PASS p280 %s' % label)
        else:
            print('FAIL p280 %s: want %r, got %r' % (label, want, got))

    # 🔴 p280: and the DATED reader is what keeps the Apache arm from re-opening `D7`.  Asked
    # family-blind, `holder()` returns a prose fragment from this very payload.
    n += 1
    _ap = open('fixtures/apache-2.0-deeptutor.txt', encoding='utf-8', errors='replace').read()
    if dated_holder(_ap) == 'Data Intelligence Lab, The University of Hong Kong' \
            and holder(_ap) == 'statement to Your modifications and':
        ok += 1
        print('PASS p280 dated reader finds the appendix where holder() finds prose')
    else:
        print('FAIL p280 dated reader: dated=%r holder=%r'
              % (dated_holder(_ap), holder(_ap)))

    # 🔵 p280: THE NEGATIVE CONTROLS FOR THE STRUCTURAL WIDENING.  `looks_like_prose` exists
    # because a lexical list could not reject `'are not'`; it must not start rejecting real
    # holders that happen to be lowercase.  Without these six, the widening is unbounded --
    # which is the mistake `p279` made twice with a path vocabulary in one hour.
    for cand, want in (('are not', True),
                       ('on the Program, and are irrevocable provided the stated', True),
                       ('if you do', True),
                       ('tldraw', False),
                       ('openSUSE Project', False),
                       ('Gibbon Foundation', False)):
        n += 1
        got = looks_like_prose(cand)
        if got is want:
            ok += 1
            print('PASS p280 looks_like_prose(%r) is %s' % (cand, want))
        else:
            print('FAIL p280 looks_like_prose(%r): want %s got %s' % (cand, want, got))

    print(f'\n{ok}/{n} checks passed')
    return 0 if ok == n else 1

if __name__ == '__main__':
    sys.exit(main())
