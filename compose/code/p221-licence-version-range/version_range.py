"""p221 - ACTION RH's instrument, built for the unit p220's own instrument could not see.

`ACTION RH` asked: run `p220`'s FILE-level read over every row whose grant was recorded
from a root `LICENSE` or a `README` only. Limb `1` was `3`+ further `FILE-NARROWER` rows.

It fires limb `2`. Across the `12` redistribution-shaped rows read first-hand on
2026-10-15, **`0`** new rows came back `FILE-NARROWER` in `p220`'s family terms. The
SCORM/Moodle pair p220 found was the distribution shape, not a general defect.

But the read did not come back empty, and what it found is bigger than what was
registered. `p220`'s `file_vs_repo()` compares LICENCE FAMILIES - it maps every GNU
variant onto `RECIPROCAL` - so it reports `AGREE` for all of these:

    shelf cell          the file that ships says              p220 verdict   truth
    GPL-3.0             "version 3 ... or (at your option)    AGREE          or-later
                         any later version"
    GPL-2.0             "version 2 of the License             AGREE          ONLY
                         (non-upgradable)"
    GPL-3.0             header: "GPLv2 or later"              AGREE          3-way
                        readme: "GPLv3"                                      CONFLICT
                        LICENSE: GPL-3.0

Those are not the same grant. `GPL-2.0-only` is incompatible with `GPL-3.0`, so a row
published as a bare `GPL-2.0` cannot be combined with a GPLv3 host (Moodle, for one) and
the shelf does not say so. `GPL-3.0-or-later` permits a studio to move forward to v4;
a bare `GPL-3.0` does not say whether it may.

So the deciding property is not the licence FAMILY and not the licence FILE. It is the
licence's VERSION RANGE - the `-only` / `-or-later` bound - and `94.3%` of this KB's
`2 342` GNU cell-mentions, across `337` distinct rows, do not carry one.

Sixth consecutive unit mismatch in this KB's headline series:

    T218-1  token            vs  axis
    T218-3  heading level    vs  pass boundary
    T218-4  line             vs  sentence
    T219-5  token            vs  packaging mode
    T220    repository       vs  FILE
    T221    licence FAMILY   vs  licence VERSION RANGE     <- this instrument
"""

import re

_GNU = ('agpl', 'lgpl', 'gpl')

# `ACTION QX` asked for a SENTENCE-based window and p220 recommended folding it into
# `RH`. This is where it lands. A GNU notice in a source file is wrapped to ~80
# columns inside a comment block, so the deciding phrase is split across lines:
#
#     * Foundation; either version 3.0 of the License, or (at your option) any later
#     * version.
#
# A line-based reading of that file sees "any later" and stops - which is exactly how
# p221's first BigBlueButton fixture came back `unspecified` against a grant that
# plainly says or-later. Normalising first is not a convenience; without it every
# wrapped grant on these shelves reads as unspecified. `bigbluebutton` also uses CRLF,
# so `\r` has to go before anything else looks at the text.
_LEADER = re.compile(r'(?m)^[ \t]*(?:[*#]+|//+|<!--)[ \t]?')
_WS = re.compile(r'\s+')


def _normalise(text):
    """Comment block -> one whitespace-collapsed sentence stream."""
    t = str(text or '').replace('\r\n', '\n').replace('\r', '\n')
    t = _LEADER.sub(' ', t)
    return _WS.sub(' ', t).strip()

# "or (at your option) any later version", "or later", "or-later", "GPLv2+"
_OR_LATER = (
    re.compile(r'or\s*\(at\s*your\s*option\)\s*any\s*later\s*version', re.I),
    re.compile(r'\bor[-\s]+later\b', re.I),
    re.compile(r'\bany\s+later\s+version\b', re.I),
    re.compile(r'\b(?:a|l)?gplv?[0-9](?:\.[0-9])?\+', re.I),
)

# "(non-upgradable)", "-only", "version 3 only"
_ONLY = (
    re.compile(r'non[-\s]?upgrad', re.I),
    re.compile(r'\bonly\b', re.I),
    re.compile(r'\bno\s+later\s+version\b', re.I),
)

_FAMILY = re.compile(r'\b(affero\s+general|lesser\s+general|a?gpl|lgpl|gpl)\b', re.I)
_VERSION = re.compile(r'(?:version|v)\s*([0-9](?:\.[0-9])?)\b', re.I)
_TOKEN = re.compile(r'\b(a?gpl|lgpl)-([0-9](?:\.[0-9])?)\b', re.I)

# `AGPL-6 d` in a liveness table is a DAY COUNT, not a licence. p221's census found
# exactly one and the guard is kept because the next table will have more.
_DAYCOUNT = re.compile(r'\b(?:a?gpl|lgpl)-[0-9]+(?:\.[0-9])?\s*d\b', re.I)


def _family_of(text):
    """Read the family from a token OR from the licence's spelled-out name.

    Both forms occur in the files read this pass and neither is optional:
    `oat-sa/lib-lti1p3-core` writes *"GNU General Public License"* and never the
    token `GPL`; `themeum/tutor` writes `GPLv2`, where a trailing `\b` after `gpl`
    fails on the `v`. Checking affero and lesser FIRST matters, because
    "Lesser General Public License" contains "General Public License".
    """
    t = str(text or '').lower()
    if 'affero' in t or re.search(r'\bagpl', t):
        return 'AGPL'
    if 'lesser' in t or re.search(r'\blgpl', t):
        return 'LGPL'
    if re.search(r'\bgpl', t) or 'general public license' in t:
        return 'GPL'
    return None


def parse_range(text):
    """Read a licence declaration - a shelf cell or a file header - as a VERSION RANGE.

    Returns {'family', 'version', 'bound', 'gnu'} where bound is one of:
      'or-later'     the grant names a version and permits any later one
      'only'         the grant names a version and refuses later ones
      'unspecified'  the grant names a version and says nothing about the bound
    A non-GNU or unreadable declaration comes back gnu=False, which is how a caller
    keeps Apache/MIT/BSD rows out of scope instead of guessing at them.
    """
    raw = _normalise(text)
    if _DAYCOUNT.search(raw):
        # strip the artefact before anything else reads a version out of it
        raw = _DAYCOUNT.sub(' ', raw)

    fam = _family_of(raw)
    if fam is None:
        return {'family': None, 'version': None, 'bound': None, 'gnu': False}

    ver = None
    m = _TOKEN.search(raw)
    if m:
        ver = m.group(2)
    else:
        m = _VERSION.search(raw)
        if m:
            ver = m.group(1)
    if ver and '.' not in ver:
        ver = ver + '.0'

    bound = 'unspecified'
    if any(p.search(raw) for p in _OR_LATER):
        bound = 'or-later'
    elif any(p.search(raw) for p in _ONLY):
        bound = 'only'
    if re.search(r'-or-later\b', raw, re.I):
        bound = 'or-later'
    elif re.search(r'-only\b', raw, re.I):
        bound = 'only'

    return {'family': fam, 'version': ver, 'bound': bound, 'gnu': True}


def range_compare(published, file_reading):
    """Compare what a shelf PUBLISHES against what the shipped file SAYS.

      OUT-OF-SCOPE          either side is not a GNU grant - say so, do not guess
      GRANT-CONFLICT        GPL vs LGPL vs AGPL, or two different VERSIONS - a
                            different grant, not a different bound on the same one
      RANGE-UNDERSPECIFIED  the file carries a bound and the published cell does not
                            -> the cell is not wrong, it is UNUSABLE without the bound
      RANGE-CONFLICT        both carry a bound and the bounds disagree
      BOTH-UNSPECIFIED      neither carries one; the ambiguity is in the SOURCE, and
                            a studio has to ask - this is not a KB defect
      AGREE                 same family, same version, same bound
    """
    p, f = parse_range(published), parse_range(file_reading)
    if not p['gnu'] or not f['gnu']:
        return 'OUT-OF-SCOPE'
    if p['family'] != f['family']:
        return 'GRANT-CONFLICT'
    if p['version'] and f['version'] and p['version'] != f['version']:
        return 'GRANT-CONFLICT'
    pb, fb = p['bound'], f['bound']
    if pb == 'unspecified' and fb == 'unspecified':
        return 'BOTH-UNSPECIFIED'
    if pb == 'unspecified':
        return 'RANGE-UNDERSPECIFIED'
    if fb == 'unspecified':
        return 'RANGE-UNDERSPECIFIED'
    return 'AGREE' if pb == fb else 'RANGE-CONFLICT'


def combinable_with(bound_a, version_a, version_b):
    """The question a studio actually asks: may this row go in a GPLv`version_b` host?

    `GPL-2.0-only` + a GPLv3 host is the case that bites: incompatible, and a bare
    `GPL-2.0` cell does not tell you. Returns True / False / None, where None means
    the bound is unspecified and the answer is genuinely unknown - which is the
    answer an SOW needs to carry, rather than an optimistic True.
    """
    if bound_a == 'or-later':
        return True
    if bound_a == 'only':
        return str(version_a) == str(version_b)
    return None


def audit_cell(published, file_reading, slug=None):
    """One row's verdict plus what to do about it."""
    state = range_compare(published, file_reading)
    f = parse_range(file_reading)
    action = {
        'RANGE-UNDERSPECIFIED': 'Republish the cell WITH the bound read from the file. '
                                'The cell is not wrong; it is unusable as it stands.',
        'RANGE-CONFLICT':       'Do not publish either. Two channels state different '
                                'bounds; record both and send it to counsel.',
        'GRANT-CONFLICT':       'Re-read both channels - this is a p220 FILE-NARROWER '
                                'candidate, not a range problem.',
        'BOTH-UNSPECIFIED':     'The SOURCE is ambiguous, not this KB. Record '
                                'UNSPECIFIED-AT-SOURCE and ask the maintainer.',
        'AGREE':                'Record both channels and move on.',
        'OUT-OF-SCOPE':         'Not a GNU grant on one side - this instrument has '
                                'nothing to say about it.',
    }[state]
    return {
        'slug': slug,
        'state': state,
        'published': parse_range(published),
        'file': f,
        'combinable_with_gpl3': combinable_with(f['bound'], f['version'], '3.0'),
        'next': action,
    }
