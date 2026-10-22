#!/usr/bin/env python3
"""p378 -- `ACTION p377-B`: a licence TEXT is not its PRESENTATION, and p312 was counting both.

`ACTION p377-B` asked whether `7768d3beb7949a85` -- the MIT digest `p376-C` pinned from one
payload -- is a real template or one project's edit.  Ten MIT payloads drawn first-hand from
ten unrelated repositories all landed on the canonical `16d6b7b5799875f6` and none on it, so
the count of one was the answer.  Diffing it then made the answer sharper than the question:

    the untitled variant differs from the canonical payload by its TITLE LINE and its
    LINE WRAPPING, and by not one operative word.

## Why that is a defect and not a curiosity

`p312-template-identity` exists so a family is identified by TEMPLATE and never by a byte
band.  Its own docstring says a band "always answers, and at the edges it answers wrongly and
silently".  But `normalise()` folds case and the holder slot and leaves wrapping alone, so
re-wrapping a LICENSE file -- which any editor, formatter or paste can do, and which changes
no word of the grant -- mints a NEW template identity.  A registry that moves on reflow is a
byte band wearing a digest's clothes.  `p377` moved its corpus ratchet **4 -> 5** on exactly
such a reflow and published it as "a THIRD distinct MIT template".

## What this instrument does, and what it deliberately does not

It computes a SECOND digest beside `p312`'s, over text with the title line and all wrapping
removed, and reports **"N texts in M presentations"**.  `p312`'s `normalise()` and
`template_digest()` are left byte-for-byte alone: editing them would silently re-key every
digest this base has published since `p312` and break every historical citation.  Same reason
`p377` renumbered its pattern to 31 instead of repairing `Gap 506` retroactively.

## The title list is CLOSED, and that is the whole safety argument

Stripping "a first line that looks like a title" would be a wildcard, and a wildcard would
eat operative text.  Only the exact title forms in `TITLES` are stripped, each one observed
first-hand on a payload on these shelves.  The untitled payload's own first line is
`Copyright 2020 Center for 21st Century Universities` -- operative text -- and it must
survive the fold.  That is a control, not a comment.

## What it must never do

Fold two DIFFERENT licences together.  The 137-byte CC0 paraphrase `p378` read at
`12britz/awesome-free-models` must not fold onto CC0's real legal code; CC0's Statement of
Purpose must not fold onto CC0's full Legal Code; MIT must not fold onto Apache-2.0.  Each is
a control below, with the payload that prompted it.
"""
import hashlib
import os
import re
import sys

# 🟢 `p312`'s normaliser is REUSED, not restated: this instrument folds PRESENTATION on top
# of the case-and-holder fold `p312` already owns, so the two cannot drift apart.  The path
# is derived from `__file__` rather than the cwd, because `python3 -I` strips the script's
# directory from `sys.path` and `p355-cwd-portability` is the class of bug that kept a
# working gate a one-off for eleven passes.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p312-template-identity"))
import template_identity as _ti  # noqa: E402

# 🟢 CLOSED list.  Every form observed first-hand on a payload these shelves carry.  A form
# added here without a payload behind it would be the band this instrument exists to retire.
TITLES = (
    "MIT License",
    "The MIT License (MIT)",
    "The MIT License",
    "BSD 2-Clause License",
    "BSD 3-Clause License",
)

_WS = re.compile(r"\s+")


def strip_title(text):
    """Remove a leading line that is EXACTLY one of `TITLES`.  Returns (text, title|None).

    🔵 Only the FIRST non-empty line is eligible, and only on an exact case-insensitive
    match of the whole line.  A copyright line, a paragraph of grant text, or a title form
    not in the list is left where it is.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        for t in TITLES:
            if line.strip().lower() == t.lower():
                return "\n".join(lines[:i] + lines[i + 1:]), t
        return text, None
    return text, None


def collapse(text):
    """Collapse every run of whitespace to one space: destroys WRAPPING, keeps WORDS."""
    return _WS.sub(" ", text).strip()


def fold(text):
    """The presentation-folded form.

    Three folds, in order, each one owned by whoever built it:
      1. `p312.normalise()`  -- case, and the copyright HOLDER slot
      2. `strip_title()`     -- a leading line that is exactly one of `TITLES`
      3. `collapse()`        -- every whitespace run, so WRAPPING stops being identity

    🔵 Step 1 is why this is not a second normaliser competing with `p312`'s: two payloads
    that differ only in holder were already one template there, and are one text here.
    """
    body, _ = strip_title(_ti.normalise(text))
    return collapse(body)


def presentation_digest(text):
    return hashlib.sha256(fold(text).encode("utf-8")).hexdigest()


def same_text(a, b):
    """Are two payloads the SAME LEGAL TEXT in different presentations?"""
    return presentation_digest(a) == presentation_digest(b)


def group(payloads):
    """{presentation_digest: [name, ...]} over a {name: text} mapping."""
    out = {}
    for name, text in payloads.items():
        out.setdefault(presentation_digest(text), []).append(name)
    for names in out.values():
        names.sort()
    return out


def texts_in_presentations(payloads):
    """The sentence this instrument exists to let a pass write."""
    c = census(payloads, _ti.template_digest)
    return "%d payload(s) · %d text(s) · %d template digest(s) · inflation %+d" % (
        c["payloads"], c["texts"], c["template_digests"], c["inflation"])


def census(payloads, template_digest_of=None):
    """"N texts in M presentations", with the presentations named.

    `template_digest_of` stays injectable so the suite can prove the two instruments
    disagree in exactly the way this pass says they do, rather than taking it on trust.
    """
    if template_digest_of is None:
        template_digest_of = _ti.template_digest
    texts = group(payloads)
    tmpl = {}
    for name, text in payloads.items():
        tmpl.setdefault(template_digest_of(text), []).append(name)
    return {
        "payloads": len(payloads),
        "texts": len(texts),
        "template_digests": len(tmpl),
        "inflation": len(tmpl) - len(texts),
        "by_text": {d[:16]: names for d, names in texts.items()},
    }
