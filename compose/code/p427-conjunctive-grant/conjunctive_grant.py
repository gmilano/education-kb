"""p427 — a grant file may carry two families CONJUNCTIVELY, and this base had no
instrument for that shape.

`p228.dual_grant` already answers the DISJUNCTIVE question — a payload whose preamble
offers a CHOICE ("either MIT or GPLv2"), where the first title is one option rather than
the licence.  Its docstring scopes it to exactly that: *a body whose own preamble offers a
CHOICE*.

This file answers the other shape, found first-hand at `p427` on
`HyNuwa/UniMCP`'s `LICENSE` (`1 980` B, `sha256(12) 727b864af003`):

    MIT License
    Copyright (c) 2026 MaxiFG
    ...
    ---------------------------------------------------------------------------
    Portions of this software are derived from utn-mcp and remain under its
    original license:

    ISC License
    Copyright (c) 2026 Joaquín Peñalva
    ...

Both grants are LIVE AND SIMULTANEOUS.  Nothing is chosen: MIT governs the work, ISC
governs the derived portions, and a distributor owes BOTH notices.  Measured at `p427`,
all six declared classifiers on this base answer `MIT` on this payload and none reports
the ISC segment — including `p228.dual_grant`, which returns `None` because the payload
offers no choice, and `p419.menciones_cruzadas`, whose needle vocabulary is
copyleft-only (`affero`, `lesser general public`) so a permissive-to-permissive
cross-grant is outside it.  Neither is a bug; both are correct within their scope.  The
gap is that no scope covered this payload.

🔴 THE COST IS AN UNDERSTATED NOTICE OBLIGATION, AND IT PASSES EVERY TIER CHECK.
Both families are permissive, so `commercial_use` is unaffected and no licence gate on
this base goes red.  A studio that reads the cell as `MIT` ships one notice where it owes
two, and drops a named third party's copyright.  That is why this is checked by shape
rather than left to the tier verdict.

🔵 WHY THE NAIVE FORM IS WRONG, MEASURED ON A REAL PAYLOAD.  Stock GPL-3.0
(`35 149` B, as carried by `EduardoKrausME/moodle-local_mcp`) contains, in its own text,
`13. Use with the GNU Affero General Public License.` — a second family named in a
title-shaped way — plus `at your option` twice and `either` ten times.  A detector that
looks for "a second family name in the body" reports stock GPL-3.0 as dual, and so does a
naive DISJUNCTIVE detector.  Two guards are therefore load-bearing:

  1. A family title counts only as a STANDALONE TITLE LINE — the stripped line is the
     title and nothing else.  `13. Use with the GNU Affero General Public License.` is
     prose and does not qualify; `ISC License` on its own line does.
  2. A CONJUNCTIVE verdict additionally requires a SCOPE SENTENCE (`portions of`,
     `derived from`, `remain under`, `third-party`, `bundled`, ...) in the window above
     the second title.  Stock GPL-3.0 contains none of these markers at all.

No network.
"""

import re
import unicodedata

# A family title as it appears on a line of its own.  Deliberately narrow: this is the
# TITLE channel (`p198`'s subject), not a body-phrase channel.
TITLES = (
    (re.compile(r'^(?:the\s+)?mit\s+licen[cs]e$', re.I), 'MIT'),
    (re.compile(r'^isc\s+licen[cs]e$', re.I), 'ISC'),
    (re.compile(r'^bsd\s+(?:2|3)[- ]clause.*$', re.I), 'BSD'),
    (re.compile(r'^apache\s+licen[cs]e$', re.I), 'Apache-2.0'),
    (re.compile(r'^(?:gnu\s+)?general\s+public\s+licen[cs]e$', re.I), 'GPL'),
    (re.compile(r'^(?:gnu\s+)?affero\s+general\s+public\s+licen[cs]e$', re.I), 'AGPL'),
    (re.compile(r'^(?:gnu\s+)?lesser\s+general\s+public\s+licen[cs]e$', re.I), 'LGPL'),
    (re.compile(r'^mozilla\s+public\s+licen[cs]e.*$', re.I), 'MPL'),
)

# Guard 2: the sentence that gives a second grant its SCOPE.  Its presence is what makes
# two titles a composition rather than a restatement.
SCOPE_MARKERS = (
    'portions of',
    'portion of',
    'derived from',
    'remain under',
    'remains under',
    'original license',
    'original licence',
    'third-party',
    'third party',
    'bundled',
    'vendored',
    'included in this',
    'subject to the following additional',
)

# p228 owns this shape.  Detected here only so it is never MISREPORTED as conjunctive.
DISJUNCTIVE_MARKERS = (
    'under either',
    'available under either',
    'dual-licensed under',
    'dual licensed under',
    'licensed under either',
)

# How far above a title to look for its scope sentence.  The UniMCP separator plus its
# two-line scope sentence sits 3 lines above the `ISC License` title.
SCOPE_WINDOW_LINES = 6

# A holder notice must carry a REAL four-digit year.  That single requirement is what
# separates a notice from the three shapes that otherwise contaminate the result, all
# three measured first-hand at `p427`:
#   - wrapped prose:      `copyright notice and this permission notice appear in all...`
#                         (ISC and MIT both wrap this way, so it is not an edge case)
#   - clause text:        `copyright holder, and you cure the violation prior to...` (GPL-3.0 §8)
#   - template placeholder: `Copyright (C) <year>  <name of author>` (GPL-3.0 appendix)
# `<year>` is not four digits, so the appendix placeholder is excluded by the same rule
# rather than by a special case.
HOLDER_RE = re.compile(
    r'^copyright\s*(?:\((?:c|C)\)|©)?\s*'
    r'(?P<year>[0-9]{4}(?:\s*[-,–]\s*[0-9]{4})?)'
    r'\s+(?P<who>\S.*?)\s*$',
    re.I,
)
# `derived from <name>` — the lineage the payload itself declares.
DERIVED_RE = re.compile(r'derived from\s+([A-Za-z0-9._/-]+)', re.I)


def _norm(s):
    """Casefold and strip accents, so `Joaquín` and `joaquin` are one identity."""
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.casefold().strip()


def title_hits(body):
    """Every STANDALONE family title line, in document order, as (line_no, family)."""
    out = []
    for i, raw in enumerate(body.splitlines()):
        line = raw.strip().rstrip('.')
        if not line:
            continue
        for rx, fam in TITLES:
            if rx.match(line):
                out.append((i, fam))
                break
    return out


def _scope_above(lines, line_no):
    """The scope marker governing a title at `line_no`, or None."""
    lo = max(0, line_no - SCOPE_WINDOW_LINES)
    window = ' '.join(lines[lo:line_no]).casefold()
    for m in SCOPE_MARKERS:
        if m in window:
            return m
    return None


def holders(body):
    """Every copyright holder named in the payload, deduplicated, in document order."""
    out = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line.lower().startswith('copyright'):
            continue
        m = HOLDER_RE.match(line)
        if not m:
            continue
        who = (m.group('who') or '').strip(' .')
        # Stock-text boilerplate: the GPL/Apache texts carry the steward's own copyright,
        # which is never the project's holder.  Excluded by name, not by guesswork.
        if not who or _norm(who).startswith(('free software foundation', 'the copyright owner')):
            continue
        if who not in out:
            out.append(who)
    return out


def classify(body):
    """Grade one licence payload.

    Returns a dict:
      mode      SINGLE | CONJUNCTIVE | DISJUNCTIVE
      families  the family set the payload actually grants under, document order
      scope     the scope marker that made it conjunctive (None otherwise)
      derived_from  the upstream the payload NAMES, if it names one
      holders   every copyright holder named
    """
    lines = body.splitlines()
    hits = title_hits(body)
    fams = []
    for _, fam in hits:
        if fam not in fams:
            fams.append(fam)

    head = '\n'.join(lines[:40]).casefold()
    disjunctive = any(m in head for m in DISJUNCTIVE_MARKERS)

    result = {
        'mode': 'SINGLE',
        'families': fams[:1],
        'scope': None,
        'derived_from': None,
        'holders': holders(body),
    }

    if disjunctive:
        # p228's subject.  Reported, never re-adjudicated here.
        result['mode'] = 'DISJUNCTIVE'
        result['families'] = fams
        return result

    if len(fams) < 2:
        return result

    # Two or more distinct standalone titles.  Conjunctive only if a later title carries
    # a scope sentence — guard 2, the one that keeps stock GPL-3.0 out.
    for line_no, fam in hits[1:]:
        if fam == hits[0][1]:
            continue
        scope = _scope_above(lines, line_no)
        if scope:
            result['mode'] = 'CONJUNCTIVE'
            result['families'] = fams
            result['scope'] = scope
            d = DERIVED_RE.search(body)
            if d:
                result['derived_from'] = d.group(1)
            return result

    # Titles present but unscoped: a restatement, not a second grant.  `p419`'s
    # `menciones_cruzadas` records this as parentage, and so do we — without upgrading it.
    return result


def notice_obligation(body):
    """How many distinct attribution notices a distributor owes for this payload.

    This is the number the `MIT` cell understated on `HyNuwa/UniMCP`.
    """
    r = classify(body)
    if r['mode'] == 'DISJUNCTIVE':
        return 1  # the distributor chooses one option and owes that one
    return max(1, len(r['holders']))
