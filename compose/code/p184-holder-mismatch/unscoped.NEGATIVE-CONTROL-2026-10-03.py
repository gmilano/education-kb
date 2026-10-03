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
COPY = re.compile(
    r'copyright\s*(?:\(c\)|©|\bc\b)?\s*'
    r'(?:[0-9]{4}(?:\s*[-–,]\s*[0-9]{4})?)?\s*'
    r'(?:\(c\)|©)?\s*'
    r'([^\n\r]{2,90})', re.I)
PLACEHOLDER = re.compile(r'\[?(yyyy|year|name of copyright owner|fullname|your name|'
                         r'copyright holders?|owner)\]?', re.I)

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
        return h[:90]
    return None

def toks(s):
    return {t for t in re.split(r'[^a-z0-9]+', s.lower()) if len(t) > 2}

def classify(slug, text):
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
    body = sys.stdin.read()
    v, h = classify(slug, body)
    print(f'{slug}\t{v}\t{h}')
