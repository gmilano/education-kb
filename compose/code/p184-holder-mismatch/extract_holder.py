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
        if SENTENCE.search(h) or STEWARD.search(h):
            continue
        return h[:90]
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
    if not family.upper().startswith(HOLDER_FAMILIES):
        return 'NOT-APPLICABLE', f'({family}: holder not in the license text by construction)'
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
