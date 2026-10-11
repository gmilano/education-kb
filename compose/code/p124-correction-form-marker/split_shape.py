#!/usr/bin/env python3
"""ACTION AA — detect a split grant by its SHAPE, not by its phrasing.

Pure function over text: no network, no filesystem, no clock.

WHY THIS EXISTS. p123 built a split detector out of `SPLIT_MARKERS`, a list
of sentences that real split-grant files had been observed to contain
("portions of this software are licensed as follows", "usa duas licenças",
…). That list is unbounded by construction: every new way of saying "part of
this repo is X and part is Y" is a new miss. p123's own instrument proved it
on `Elgg/Elgg`, whose `LICENSE.txt` opens

    Bundled plugins (the contents of the "/mod" directory) are available
    only under the GPLv2 license.

    The remainder of the project is available under either MIT or GPLv2.

No marker matches that, so the classifier fell through to the title anchor,
found "The MIT License (MIT)" further down the file, and returned a bare
`MIT` for a repository whose plugin directory is GPL-2.0 only.

WHAT A SPLIT GRANT ACTUALLY IS. Not a phrasing — a STRUCTURE. A split grant
binds a SCOPE (a subset of the repository) to a LICENCE, at least twice,
with the scopes and the licences both differing. That is checkable without
knowing how the sentence is worded:

    BINDING := SCOPE ... GRANT-VERB ... LICENCE   (within a window)
    SPLIT   := >= 2 BINDINGs with >= 2 distinct SCOPEs
                                 and >= 2 distinct LICENCEs

WHAT THIS DELIBERATELY WILL NOT DO. A file that names two licences is not a
split grant. Three constructs name a second licence while granting one:

  1. GPL-2.0's PREAMBLE names the Lesser GPL.
  2. EPL-2.0's SECONDARY LICENSE clause names GPL-2.0 as a downstream option.
  3. A dual grant ("either MIT or GPLv2") names two licences for ONE scope —
     the licensee chooses. That is one binding, not two.

The scope vocabulary below is therefore a closed list of ARTIFACT CLASSES —
the parts a repository is actually divided into — and `software`, `program`,
`work` and `library` are EXCLUDED on purpose: they denote the whole work, so
a preamble sentence about "software covered by the Lesser GPL" cannot form a
binding. Case 3 is excluded by requiring two distinct scopes.
"""
import re

# Artifact classes a repository is divisible INTO. Whole-work nouns
# (software, program, work, library, package) are excluded: see module docstring.
ARTIFACT = (
    r"(?:source\s+code|sources?|code|documentation|docs?|datasets?|data|"
    r"contents?|content|plugins?|modules?|themes?|examples?|samples?|"
    r"assets?|media|images?|icons?|fonts?|tests?|translations?|"
    r"remainder|rest|everything\s+else)"
)

# A determiner or scoping qualifier may precede the artifact noun. "bundled",
# "the remainder of" and "the rest of" are qualifiers, not phrasings: they
# scope, they do not grant.
QUAL = r"(?:the\s+|all\s+(?:of\s+the\s+)?|any\s+|every\s+|bundled\s+|other\s+)*"

SCOPE_NP = re.compile(QUAL + ARTIFACT, re.I)

# A filesystem path is the other way a scope gets named. Require a slash that
# is attached to a path-ish token, so "and/or" and "MIT/GPL" cannot match.
SCOPE_PATH = re.compile(r"[\"'`(]?(?:/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.*-]+)*/?"
                        r"|[A-Za-z0-9_.-]+/(?:[A-Za-z0-9_.*-]+/?)*)[\"'`)]?")

# Only paths that look like a directory a repo really has. Without this,
# every URL in a licence file becomes a scope.
PATH_OK = re.compile(r"^[\"'`(]?/?(?:src|lib|mod|mods|modules|plugins|themes|"
                     r"docs?|doc|data|datasets?|assets|media|images|img|fonts|"
                     r"examples?|samples?|tests?|test|vendor|third[_-]?party|"
                     r"contrib|tools|scripts|bin|app|apps|packages?|core|"
                     r"content|static|public|web|www)\b", re.I)

GRANT_VERB = re.compile(
    r"(?:is|are|shall\s+be|may\s+be|can\s+be)?\s*"
    r"(?:licen[cs]ed|available|released|distributed|provided|published|"
    r"covered|governed|offered)\s+"
    r"(?:only\s+|solely\s+|exclusively\s+)?"
    r"(?:under|by|pursuant\s+to|with)"
    r"|(?:is|are)\s+(?:under|subject\s+to)"
    r"|(?:applies|apply)\s+to"
    r"|licen[cs]e\s*:",
    re.I)

# Licence tokens as NAMED in prose. Deliberately narrower than the
# classifier's full table: a shape binding needs a name, not a body.
LICENCE_TOKEN = [
    (re.compile(r"\bCC[ -]?BY[ -]?NC[ -]?SA(?:[ -]?\d(?:\.\d)?)?\b|"
                r"attribution[- ]noncommercial[- ]sharealike", re.I), "CC-BY-NC-SA"),
    (re.compile(r"\bCC[ -]?BY[ -]?NC(?:[ -]?\d(?:\.\d)?)?\b|"
                r"attribution[- ]noncommercial(?![- ]sharealike)", re.I), "CC-BY-NC"),
    (re.compile(r"\bCC[ -]?BY[ -]?SA(?:[ -]?\d(?:\.\d)?)?\b|"
                r"attribution[- ]sharealike", re.I), "CC-BY-SA"),
    # 🔴 `\bCC[ -]?BY\b` matches INSIDE `CC BY-SA 4.0`, because the hyphen
    # is a word boundary. That made every CC-BY-SA file look like it named two
    # licences, and two CC-BY-SA repositories were reported as split grants
    # until the fixtures were read. The element suffixes must be excluded
    # explicitly, on the short form as well as the spelled one.
    (re.compile(r"\bCC[ -]?BY(?![ -]?(?:NC|SA|ND))(?:[ -]?\d(?:\.\d)?)?\b|"
                r"creative\s+commons\s+attribution(?![- ](?:non|share|no))", re.I), "CC-BY"),
    (re.compile(r"\bCC0\b|public\s+domain\s+dedication", re.I), "CC0"),
    (re.compile(r"\bAGPL\s*-?\s*v?3?|affero\s+general\s+public", re.I), "AGPL-3.0"),
    (re.compile(r"\bLGPL\s*-?\s*v?(?:3|2\.1)?|lesser\s+general\s+public", re.I), "LGPL"),
    (re.compile(r"\bGPL\s*-?\s*v?3(?:\.0)?\b|"
                r"gnu\s+general\s+public\s+licen[cs]e,?\s*version\s*3", re.I), "GPL-3.0"),
    (re.compile(r"\bGPL\s*-?\s*v?2(?:\.0)?\b|"
                r"gnu\s+general\s+public\s+licen[cs]e,?\s*version\s*2", re.I), "GPL-2.0"),
    (re.compile(r"\bapache(?:\s+licen[cs]e)?[ ,-]*2(?:\.0)?\b", re.I), "Apache-2.0"),
    (re.compile(r"\bBSD\b", re.I), "BSD"),
    (re.compile(r"\bMPL\b|mozilla\s+public", re.I), "MPL"),
    (re.compile(r"\bMIT\b", re.I), "MIT"),
]

# Constructs that name a second licence WITHOUT splitting the work. These are
# not phrasings of a split; they are phrasings of a NON-split, and each one is
# a real construct from a real licence body (see module docstring cases 1-3).
NON_SPLIT_CTX = re.compile(
    r"secondary\s+licen[cs]e"            # EPL-2.0 s.4 / MPL-2.0
    r"|instead\s+of\s+this\s+licen[cs]e"  # GPL-2.0 preamble -> LGPL
    r"|either\s+(?:version\s+)?\S+\s+or"  # dual grant: ONE scope, licensee picks
    r"|at\s+your\s+option"
    r"|dual[- ]licen[cs]ed",
    re.I)

WINDOW = 200          # chars from scope start to licence token
BIND_GAP = 90         # chars from grant verb to licence token


def _licences_at(text, start, end):
    """Licence tokens named in text[start:end], longest-name-first order."""
    seg = text[max(0, start):end]
    out = []
    for rx, tok in LICENCE_TOKEN:
        m = rx.search(seg)
        if m:
            out.append((m.start(), tok))
    seen, toks = set(), []
    for _, t in sorted(out):
        if t not in seen:
            seen.add(t)
            toks.append(t)
    return toks


def _scopes(text):
    """Yield (position, canonical scope) for every scope expression."""
    for m in SCOPE_NP.finditer(text):
        raw = re.sub(r"\s+", " ", m.group(0)).strip().lower()
        key = re.sub(r"^(?:the|all|of|any|every|other)\s+", "", raw)
        yield m.start(), ("np:" + key)
    for m in SCOPE_PATH.finditer(text):
        tok = m.group(0)
        if PATH_OK.match(tok) and "://" not in tok:
            yield m.start(), ("path:" + tok.strip("\"'`()").strip("/").lower())


def bindings(text):
    """Every (scope, licence) binding the text's SHAPE establishes."""
    found = []
    for pos, scope in _scopes(text):
        tail = text[pos:pos + WINDOW]
        gv = GRANT_VERB.search(tail)
        if not gv:
            continue
        # The licence must follow the grant verb closely, not merely sit
        # somewhere in the window.
        lic_from = pos + gv.end()
        toks = _licences_at(text, lic_from, lic_from + BIND_GAP)
        if not toks:
            continue
        ctx = text[pos:lic_from + BIND_GAP]
        if NON_SPLIT_CTX.search(ctx):
            # A dual grant still binds its scope -- to a CHOICE, which is one
            # licence position, so record only the first token.
            toks = toks[:1]
        for t in toks:
            found.append((scope, t))
    return found


def split_by_shape(text):
    """Return (is_split, sorted licence tokens, binding count).

    SPLIT requires >= 2 bindings whose scopes differ AND whose licences
    differ. Two scopes under one licence is a scoped single grant; one scope
    under two licences is a dual grant. Neither is a split.
    """
    bs = bindings(text)
    scopes = {s for s, _ in bs}
    lics = {l for _, l in bs}
    is_split = len(bs) >= 2 and len(scopes) >= 2 and len(lics) >= 2
    return is_split, sorted(lics), len(bs)


if __name__ == "__main__":
    import sys
    t = sys.stdin.read()
    sp, lics, n = split_by_shape(t)
    print("SHAPE-SPLIT:" + "+".join(lics) if sp else "NO-SHAPE-SPLIT")
    print("bindings=%d" % n, file=sys.stderr)
