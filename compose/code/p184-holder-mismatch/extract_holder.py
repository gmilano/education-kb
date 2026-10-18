#!/usr/bin/env python3
"""P184 — the holder named in a license file, and whether it belongs to the project.

Pass 66 found a row whose license file passes EVERY layer this KB measures and still
states the wrong terms.  `MaybeItsAdam/tutors` ships `LICENSE.md` = the full MIT text,
1.075 B, with a real holder and year -- `Copyright (c) 2024 tldraw Inc.` -- while its
README says the governing terms are the tldraw SDK license, which requires preserving a
"Made with tldraw" watermark.  MIT has no such condition.

The file question (P170), the payload question (P172) and the identifier-vs-cession
question (P179) all pass it.  The HOLDER is what gives it away: a 2024 tldraw Inc.
copyright on a 2026 tutoring project by `MaybeItsAdam` does not belong to the project.

This module extracts the holder and classifies the relation to the repo slug:

  HOLDER-MATCH      the owner or the repo name appears in the holder, or vice versa
  HOLDER-UNRELATED  a holder is named and shares NO token with owner or repo -> READ IT
  NO-HOLDER         license text present, no copyright line filled in (the Apache-2.0
                    appendix ships `Copyright [yyyy] [name of copyright owner]` unfilled)

HOLDER-UNRELATED is NOT a verdict of wrongness: a personal name rarely matches a GitHub
handle, so the class is a READING LIST, not a finding.  What makes it useful is that the
list is short enough to read, and the tldraw case is in it.
"""
import re, sys

# A filled copyright line.  The unfilled Apache/BSD placeholders are excluded by
# construction: they are the thing we are trying to detect as NO-HOLDER.
# D8 -- EVERY QUANTIFIER HERE IS SAME-LINE, and that is not cosmetic.  The first build
# used `\s*` between the word "copyright" and the holder.  `\s` matches a NEWLINE, so a
# copyright line with NO holder -- `Copyright (c) 2026` and nothing else -- silently
# reached across the blank line and published the next paragraph of the licence,
# `Permission is hereby granted, free of charge, to any person obtaining a copy`, as the
# holder.  The NO-HOLDER class the instrument exists to return was therefore UNREACHABLE
# for exactly the files that need it: MIT texts with a year and no name.  Measured on the
# 2026-10-07 shelf sweep, that was 7 of 61 rows in the reading list.  See the four D8
# controls in `test_holder.py`.
COPY = re.compile(
    r'copyright[ \t]*(?:\(c\)|©|\bc\b)?[ \t]*'
    r'(?:[0-9]{4}(?:[ \t]*[-–,][ \t]*[0-9]{4})*)?[ \t]*'
    r'(?:\(c\)|©)?[ \t]*'
    r'([^\n\r]{2,90})', re.I)
PLACEHOLDER = re.compile(r'\[?(yyyy|year|name of copyright owner|fullname|your name|'
                         r'copyright holders?|owner)\]?', re.I)

# D6 -- THE LICENSE TEXT'S OWN COPYRIGHT IS NOT THE PROJECT'S.  The first build ran over the
# 160 files P170 had measured and returned 87 HOLDER-UNRELATED, which is not a reading list,
# it is a broken instrument.  Two causes, both found by reading the output:
#
#  * Apache-2.0 (29 of the 30 rows): the regex matched a SENTENCE of the body -- "...
#    copyright notice that is included in or attached to the work ..." -- and published it as
#    a holder.  Apache's own holder line lives in an APPENDIX that ships unfilled.
#  * GPL/AGPL (21 rows): `Copyright (C) 2007 Free Software Foundation, Inc. <fsf.org>` is the
#    copyright of the LICENSE TEXT, which every copy of the GPL carries.  The project's own
#    copyright is not in the file at all -- it is in the SOURCE HEADERS, which is exactly the
#    channel pass 65 measured for the Moodle plugins (P172/P179).
#
# So the holder question is only answerable from the license FILE for the families whose
# standard text has a FILLED holder line by construction: MIT, BSD, ISC.  For the rest the
# verdict is NOT-APPLICABLE with its reason, and the holder has to be sought in the payload.
HOLDER_FAMILIES = ('MIT', 'BSD', 'ISC')

# Copyright lines that belong to the license STEWARD, never to the project.
STEWARD = re.compile(r'free software foundation|creative commons|open source initiative|'
                     r'regents of the university of california\b.{0,0}$', re.I)
# D8b -- the plural.  `\bholder\b` does not match `HOLDERS`, so the warranty clause
# `... AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM ...` passed the sentence
# filter and was published as a holder by 3 of the 7 D8 rows.
# A match that is a clause of the body rather than a name.
SENTENCE = re.compile(r'\b(notices?|owners?|holders?|laws?|works?|licen[sc]e[ds]?|means|'
                      r'shall|defined|rights?|that|which|upon|include[ds]?|attached|'
                      r'permission|hereby|granted|liable|damages|claim)\b', re.I)

# 🔴 p280: THE `SENTENCE` VOCABULARY IS A FLOOR, and the real GPL-3.0 text defeats it.
# `GibbonEdu/core`'s `LICENSE` (the verbatim GPL-3.0, 35 121 B, read first-hand 2026-10-18)
# yields `'on the Program, and are irrevocable provided the stated'` -- a fragment of the
# licence's own body, published as a holder.  Not one of its words is in `SENTENCE`:
# `Program`, `irrevocable` and `stated` are simply not on the list, and adding them is the
# third floor-widening of this pass (`is_bundled` took two).
# 🟢 So the guard is STRUCTURAL instead of lexical: a copyright holder is a NAME, and a name
# does not contain a run of function words.  THREE OR MORE CONSECUTIVE ALL-LOWERCASE WORDS
# is prose, whatever the words are.
# 🔵 Deliberately NOT "starts with a lowercase letter", which was the first draft: `openSUSE
# Project`, `ownCloud GmbH` and `iText Group` are real lowercase-initial holders, and a
# predicate that rejects them trades a false negative for a false positive.  Measured on the
# controls: every expected holder in this file has at most ONE lowercase word in a row.
BODY_FRAGMENT = re.compile(r'(?:^|\s)[a-z][a-z\'-]*(?:\s+[a-z][a-z\'-]*){2,}(?:\s|[,.;:]|$)')


def looks_like_prose(h):
    """-> True when a candidate is a fragment of the licence body rather than a name.

    MEASURED, not designed: every one of the 29 `Copyright`-anchored candidates the real
    GPL-3.0 text yields was listed and graded (`evidence/holder-candidates.2026-10-18-p280
    .tsv`).  `STEWARD` catches the FSF line, `PLACEHOLDER` the unfilled appendix, `SENTENCE`
    nineteen of them and the lowercase-run rule six more -- and exactly ONE survived all
    four: `'are not'`.  Two lowercase words is below the run threshold, so the threshold was
    not the predicate.
    """
    if BODY_FRAGMENT.search(h):
        return True
    # A NAME carries a capital or a digit somewhere.  A multi-word candidate with neither is
    # prose -- and the word count matters: a SINGLE lowercase word may be a real holder
    # (`tldraw`, `ownCloud`'s lowercase sibling forms), so it is left to the other guards.
    if len(h.split()) > 1 and not re.search(r'[A-Z0-9]', h):
        return True
    return False

def holder(text):
    """The first FILLED copyright holder in the license text, or None."""
    for m in COPY.finditer(text):
        h = m.group(1).strip().strip('.,;:-—').strip()
        h = re.sub(r'\s+', ' ', h)
        h = re.sub(r'^(and|the)\s+', '', h, flags=re.I)
        # Strip a trailing sentence that is not part of the name.
        h = re.split(r'\s+(?:All rights reserved|Permission is|This program|Licensed under)',
                     h, flags=re.I)[0].strip().strip('.,;:')
        if not h or PLACEHOLDER.search(h) or len(h) < 2:
            continue
        if re.fullmatch(r'[\[\]\(\)<>0-9\s.,;:-]+', h):
            continue
        if SENTENCE.search(h) or STEWARD.search(h) or looks_like_prose(h):
            continue
        return h[:90]
    return None

# 🟢 p280: THE DATED-APPENDIX READER.  The copyleft/Apache families carry tens of kilobytes
# of prose ABOUT copyright, and `p184`'s `D7` control already proved no stop-word list closes
# that class.  But a FILLED appendix notice differs from body prose structurally and not
# lexically: it carries a YEAR between the word `Copyright` and the name.  Measured over the
# three real full texts this base holds --
#
#   GibbonEdu/core  LICENSE  (GPL-3.0, filled)    -> ('2010', 'Gibbon Foundation')
#   moodle/moodle   COPYING  (GPL-3.0, UNfilled)  -> none
#   HKUDS/DeepTutor LICENSE  (Apache-2.0, filled) -> ('2025', 'Data Intelligence Lab, The
#                                                     University of Hong Kong')
#
# -- exactly one candidate each, and ZERO prose fragments.  `holder()` on the same Apache
# text returns `'statement to Your modifications and'`, so the year is doing the work.
# 🔵 NOT used for MIT/BSD/ISC: `p237-grant-payload-shapes` controls YEAR-LESS MIT grants, so
# requiring a year there would reject real holders.  The year is required only where the
# alternative is prose.
DATED_COPY = re.compile(r'copyright[ \t]*(?:\(c\)|\(C\)|©)?[ \t]*'
                        r'((?:19|20)\d{2}(?:[ \t]*[-–,][ \t]*(?:19|20)?\d{2,4})?)[ \t]+'
                        r'([^\n\r]{2,90})', re.I)


def dated_holder(text):
    """The first FILLED, DATED copyright holder, or None.  For the families whose template
    puts the holder in an appendix rather than in the terms."""
    for m in DATED_COPY.finditer(text):
        h = re.sub(r'\s+', ' ', m.group(2).strip().strip('.,;:-—').strip())[:90]
        h = re.sub(r'^(and|the)\s+', '', h, flags=re.I)
        if not h or PLACEHOLDER.search(h) or STEWARD.search(h):
            continue
        if SENTENCE.search(h) or looks_like_prose(h):
            continue
        return h
    return None


def toks(s):
    return {t for t in re.split(r'[^a-z0-9]+', s.lower()) if len(t) > 2}

def classify(slug, text, family=None):
    # D7 -- THE FAMILY IS A REQUIRED INPUT, and that is the finding, not a limitation.
    # Patching the sentence filter was the wrong move and the controls proved it: over the
    # FULL Apache and GPL texts a family-blind build still published `patent, trademark, and`
    # and `permission, other than the making of an` as holders.  Every such fragment follows
    # the word "copyright" in prose, so no stop-word list closes the class -- the texts are
    # tens of kilobytes of prose ABOUT copyright.
    #
    # P170 removed the BRANCH dimension from the license question and P171 moved the family
    # question to the TITLE; both made the question less dependent on context, and that was
    # right.  The holder dimension does not go that way: whether a license file names the
    # project's holder AT ALL is a property OF THE FAMILY.  So this instrument refuses to
    # answer without one instead of guessing.
    if family is None:
        return 'FAMILY-REQUIRED', '(the holder question is not answerable family-blind)'
    # 🔴 p280: THE `by construction` ARGUMENT IS REFUTED BY A REAL PAYLOAD, 96 passes on.
    # This branch returned `NOT-APPLICABLE` for every copyleft family, on the ground that
    # "the project's own copyright is not in the file at all".  That is true of the GPL's
    # TERMS and false of its APPENDIX: `GibbonEdu/core`'s `LICENSE` (verbatim GPL-3.0,
    # 35 121 B, read first-hand 2026-10-18) fills the interactive-notice template at line
    # 655 with its own real values --
    #
    #     Core  Copyright (C) 2010  Gibbon Foundation
    #
    # -- so for this repository the holder IS in the licence text, stated plainly, and the
    # instrument answered "not answerable".
    # 🔵 WHY IT SURVIVED SO LONG: the control for this branch is `moodle/moodle`'s real
    # `COPYING`, which ships the appendix UNFILLED (`<year> <name of author>`).  The argument
    # was validated on the unfilled case only, and `PLACEHOLDER` -- already in this file --
    # is exactly what tells the two apart.
    # 🟢 So the family no longer decides the ANSWER, it decides the FALLBACK: an unfilled
    # appendix is still `NOT-APPLICABLE` by construction, and a FILLED one is a holder like
    # any other.  Both arms are controlled, on the two real payloads, in `test_holder.py`.
    # 🔴 AND THE FIRST FIX FOR IT RE-OPENED THE DEFECT `D7` WAS BUILT TO CLOSE.  Letting
    # every copyleft text fall through to `holder()` made `HKUDS/DeepTutor`'s FULL Apache
    # payload publish `'statement to Your modifications and'` as a holder -- `D7`'s own
    # sentence, re-committed by the fix for the branch `D7` wrote.  The appendix reader is
    # therefore the DATED one, which is structural rather than lexical.
    if not family.upper().startswith(HOLDER_FAMILIES):
        h = dated_holder(text)
        if h is None:
            return ('NOT-APPLICABLE',
                    f'({family}: holder not in the license text by construction — '
                    f'appendix unfilled or absent)')
    else:
        h = holder(text)
        if h is None:
            return 'NO-HOLDER', '-'
    owner, _, repo = slug.partition('/')
    ht, pt = toks(h), toks(owner) | toks(repo)
    # Also compare with separators removed, so THU-MAIC matches thumaic.
    flat_h = re.sub(r'[^a-z0-9]', '', h.lower())
    flat_p = [re.sub(r'[^a-z0-9]', '', x.lower()) for x in (owner, repo)]
    if ht & pt:
        return 'HOLDER-MATCH', h
    for f in flat_p:
        if len(f) > 3 and (f in flat_h or flat_h in f):
            return 'HOLDER-MATCH', h
    # A token-level containment, which the control for `GibbonEdu/core` forced: the holder
    # token `gibbon` is a prefix of the project token `gibbonedu`, and a whole-string
    # comparison misses it.  Bounded at 4 characters so short tokens cannot collide.
    for a in ht:
        for b in pt:
            if len(a) > 3 and len(b) > 3 and (a in b or b in a):
                return 'HOLDER-MATCH', h
    return 'HOLDER-UNRELATED', h

if __name__ == '__main__':
    slug = sys.argv[1]
    fam = sys.argv[2] if len(sys.argv) > 2 else None
    body = sys.stdin.read()
    v, h = classify(slug, body, fam)
    print(f'{slug}\t{v}\t{h}')
