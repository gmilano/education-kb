#!/usr/bin/env python3
"""ACTION AG — no licence token may be read without reading what SCOPES it.

p122, p123 and p124 each shipped a first build that was refuted by its own
fixtures, and p124's `P124-H` named the shared cause: a token was matched
without reading the clause it sits in. Four instances were known:

  1. GPL-2.0's PREAMBLE names the Lesser GPL
     ("Some other Free Software Foundation software is covered by the GNU
      Lesser General Public License instead.")
  2. EPL-2.0's SECONDARY-LICENCE clause names GPL-2.0
     ("'Secondary License' means either the GNU General Public License,
      Version 2.0, or any later versions…")
  3. CC 4.0's own BOILERPLATE RECOMMENDS CC0
     ("Creative Commons recommends the use of CC0 Public Domain Dedication…")
  4. `CC BY` matches INSIDE the longer token `CC BY-SA 4.0`
     (the hyphen is a word boundary, so `\\bCC[ -]?BY\\b` succeeds)

Each was fixed as an instance. This module makes the CLASS a standing check:
every match is labelled with the clause that scopes it, and a match scoped by
anything but a grant is DISCARDED.

    GRANT           the operative clause -- the only label that survives
    PREAMBLE        rationale before the terms begin
    RECOMMENDATION  a licence the document suggests for OTHER work
    SECONDARY       a compatibility/secondary-licence definition
    SUBSTRING       the match is inside a longer licence token
    CONTRAST        a comparison clause: "neither restriction exists under X"
    OUT-OF-TREE     a grant over something this repository is not
    DOCUMENT-TEXT   a grant over the LICENCE DOCUMENT, not over the material

CONTRAST and OUT-OF-TREE are p125's additions, and neither was hypothesised:
`compose/patterns.md:1486` says *"Neither restriction exists under AGPL-3"*
about a repository that is Elastic-2.0, and `ankitects/anki`'s grant file says
*"Binary distributions also include copies of Qt translation files (LGPL)"* --
a licence over files the source tree does not contain.

Offline. No network, no clock, no environment.
"""
import re

LABELS = ("GRANT", "PREAMBLE", "RECOMMENDATION", "SECONDARY", "SUBSTRING",
          "CONTRAST", "OUT-OF-TREE", "DOCUMENT-TEXT")
SURVIVES = ("GRANT",)

# A token, with the alternatives ordered LONGEST-FIRST so that `CC BY-SA 4.0`
# is consumed before `CC BY` can match its prefix. Rule 4 is a property of the
# ordering, not of a lookahead bolted on afterwards.
# 🔴 THE ALTERNATION IS WRAPPED IN \b ... \b, and leaving it off was this
# module's own first-build defect -- the fifth instance of the very class it
# exists to prevent. `MIT` matched inside `LIMITED` and `ISC` inside
# `DISCLAIMED`, so every BSD-3 and Apache-2.0 warranty disclaimer on earth
# yielded a spurious MIT grant. The SUBSTRING check could not see it: it
# compares a span against other LICENCE tokens, and `LIMITED` is not one.
TOKEN = re.compile(
    r"\b(?P<tok>"
    r"Creative Commons Attribution[- ]NonCommercial[- ]ShareAlike(?: \d\.\d)?|"
    r"Creative Commons Attribution[- ]ShareAlike(?: \d\.\d)?|"
    r"Creative Commons Attribution(?: \d\.\d)?|"
    r"CC[ -]?BY[ -]?NC[ -]?SA(?:[ -]\d(?:\.\d)?)?|"
    r"CC[ -]?BY[ -]?NC[ -]?ND(?:[ -]\d(?:\.\d)?)?|"
    r"CC[ -]?BY[ -]?SA(?:[ -]\d(?:\.\d)?)?|"
    r"CC[ -]?BY[ -]?NC(?:[ -]\d(?:\.\d)?)?|"
    r"CC[ -]?BY(?:[ -]\d(?:\.\d)?)?|"
    r"CC0(?:[ -]1\.0)?|"
    r"GNU Affero General Public License|GNU Lesser General Public License|"
    r"GNU General Public License|"
    r"Apache License|Apache[ -]2(?:\.0)?|"
    r"AGPL(?:[ -]?3(?:\.0)?)?|LGPL(?:[ -]?[23](?:\.[01])?)?|"
    r"GPL(?:[ -]?[23](?:\.0)?)?|"
    r"BSD[ -]3(?:[ -]Clause)?|BSD[ -]2(?:[ -]Clause)?|"
    r"MPL[ -]?2\.0|EPL[ -]?2\.0|EUPL[ -]?1\.[12]|"
    r"Elastic[ -]?2\.0|BUSL[ -]?1\.1|MulanPSL[ -]?2\.0|ECL[ -]?2\.0|"
    r"Unlicense|MIT|ISC"
    r")\b")

# ------------------------------------------------------------------- cues
# Each cue is matched in a WINDOW around the token, and the window is what
# makes this a scope read rather than a document-level guess.
PREAMBLE_CUE = re.compile(
    r"\bPreamble\b|is intended to guarantee|take away your\s+freedom|"
    r"\bis covered by\b|\binstead\.\)|"
    r"we want its recipients to know|\bpermits making a modified version\b|"
    r"\bthis result may fail to come about\b", re.I)
RECOMMEND_CUE = re.compile(
    r"\brecommends?\b|\bshould consider\b|\bconsider (?:using|applying)\b|"
    r"\bmay (?:wish to )?use\b.{0,40}\bfor\b|\bis recommended\b", re.I)
SECONDARY_CUE = re.compile(
    r"\"?Secondary Licen[sc]e\"?\s+means|\bSecondary Licen[sc]es?\b|"
    r"\bcompatible licen[sc]e\b|[-\s]compatible licen[sc]e|"
    r"\beither the\b.{0,30}\bor any later versions?\b|"
    # AGPL-3 section 13 and its GPL-3 counterpart: a COMPATIBILITY grant over
    # a work being combined with this one, not over this one. Found by the
    # agpl3 control, which yielded five spurious GPL grants from one AGPL file
    # -- enough to make every AGPL-3.0 repository in the corpus look dual.
    r"\bUse with the\b|\bpermission to link or combine\b|"
    r"\bcombine any covered work with a work licen[sc]ed\b|"
    r"\bCorresponding Source for any work covered by\b|"
    r"\bthe work with which it is combined\b|"
    r"\ba work licen[sc]ed\s+under\b|\bany work covered by\b",
    re.I | re.S)
CONTRAST_CUE = re.compile(
    r"\bneither\b.{0,60}\b(?:exists?|applies|appear)|"
    r"\bno such (?:restriction|duty|clause)\b.{0,40}\bunder\b|"
    r"\bunlike\b|\bwhereas under\b|\bdoes not exist under\b|"
    r"\bcompared (?:to|with)\b|"
    # A licence named in a HISTORY clause to say this is NOT it. AGPL-3's
    # preamble spends a paragraph on the older Affero GPL for exactly this
    # purpose, and both mentions survived as grants until the control said so.
    r"\bnot a version of\b|\ban older licen[sc]e,? called\b|"
    r"\bis\s+a different licen[sc]e\b|"
    r"\bdesigned to accomplish similar goals\b", re.I | re.S)
OUT_OF_TREE_CUE = re.compile(
    r"\bbinary distributions?\b|\bthird[- ]party\b|\bvendored\b.{0,30}"
    r"\belsewhere\b|\blibraries that this code references\b|"
    r"\bdependenc(?:y|ies)\b|\bthe upstream project\b|\bnot (?:included|"
    r"contained) in this repositor", re.I)
# p124 described its own third instance as "the CC 4.0 legalcode RECOMMENDS
# CC0 in its own boilerplate". The sentence in the file says something else:
# "The text of the Creative Commons public licenses is dedicated to the public
# domain under the CC0 Public Domain Dedication." That is a real grant with a
# real verb -- its SUBJECT is the licence document, not the licensed material.
# A gate built to p124's description looks for `recommends` and finds nothing.
DOCUMENT_TEXT_CUE = re.compile(
    r"\bthe text of\b.{0,80}\blicen[sc]es?\b|"
    r"\btext of (?:the|this) (?:licen[sc]e|agreement)\b|"
    r"\bthis licen[sc]e document\b|"
    r"\bcopy and distribute verbatim copies\s+of this licen[sc]e document\b",
    re.I | re.S)

# A grant must have an operative verb. Without one a token is a mention.
GRANT_CUE = re.compile(
    r"\b(?:licen[sc]ed under|is licen[sc]ed|available under|released under|"
    r"distributed under|governed by|under the terms of|"
    r"the licen[sc]e is|licen[sc]e:|SPDX-Licen[sc]e-Identifier|"
    r"are available under|use a licen[sc]e|is covered by the terms)\b", re.I)

WINDOW_BACK = 220
WINDOW_FWD = 90


def _window(text, start, end):
    return text[max(0, start - WINDOW_BACK):min(len(text), end + WINDOW_FWD)]


def label_span(text, start, end):
    """The clause that scopes the span [start, end). One of LABELS.

    Takes a RAW SPAN rather than a match of this module's own pattern, which
    is the whole point: the four known instances were produced by NAIVE
    detectors, and a gate that can only label its own matches cannot be shown
    to catch them. Instance 4 in particular exists only as a naive span --
    this module's longest-first ordering never emits `CC BY` inside
    `CC BY-SA 4.0`, so the gate must be able to judge a span it would not
    itself have proposed.
    """
    # SUBSTRING is decided on the TEXT, not on a window: a longer token that
    # strictly contains this span and starts no later.
    for other in TOKEN.finditer(text):
        if (other.start("tok") <= start and other.end("tok") > end
                and (other.end("tok") - other.start("tok")) > (end - start)):
            return "SUBSTRING"
    win = _window(text, start, end)
    # Order matters: a recommendation inside a preamble is still not a grant,
    # and the most specific disqualifier is reported.
    if DOCUMENT_TEXT_CUE.search(win):
        return "DOCUMENT-TEXT"
    if SECONDARY_CUE.search(win):
        return "SECONDARY"
    if RECOMMEND_CUE.search(win):
        return "RECOMMENDATION"
    if CONTRAST_CUE.search(win):
        return "CONTRAST"
    if OUT_OF_TREE_CUE.search(win):
        return "OUT-OF-TREE"
    if PREAMBLE_CUE.search(win):
        return "PREAMBLE"
    if GRANT_CUE.search(win):
        return "GRANT"
    # The TITLE LINE of a bare grant file is the grant, with no verb anywhere
    # -- `BSD 3-Clause License` followed by a copyright line and the terms.
    # p124's ACTION AD reached the same conclusion from the other direction
    # ("title line first, because it is the only channel the CC0 boilerplate
    # cannot poison"), and a gate that labels it PREAMBLE discards every
    # verb-less licence file in the corpus.
    head = text[:start]
    if "\n" not in head.strip("\n") and start < 120:
        return "GRANT"
    return "PREAMBLE" if start < 400 else "GRANT"


def label(text, m):
    """`label_span` for a match of this module's own TOKEN pattern."""
    return label_span(text, m.start("tok"), m.end("tok"))


def scoped_tokens(text):
    """[(token, label, offset)] for every match, in document order."""
    out = []
    for m in TOKEN.finditer(text):
        out.append((m.group("tok"), label(text, m), m.start("tok")))
    return out


def grants(text):
    """Only the tokens a GRANT clause scopes."""
    return [(t, o) for t, lab, o in scoped_tokens(text) if lab in SURVIVES]


def discarded(text):
    return [(t, lab, o) for t, lab, o in scoped_tokens(text)
            if lab not in SURVIVES]


def main(argv):
    import sys
    for path in [a for a in argv if not a.startswith("-")]:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        if text[:1] == "﻿":
            text = text[1:]
        print("## %s" % path)
        for tok, lab, off in scoped_tokens(text):
            print("%-14s %-16s @%d" % (lab, tok, off))
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv[1:]))
