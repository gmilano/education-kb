#!/usr/bin/env python3
"""The instrument for P227 + P228 -- the two rules that pass 74 stated but could not enforce.

P224 (pass 74) wrote down the PROCEDURE for measuring coverage against the installed base
instead of against the KB's own history.  It then made two errors that no instrument in this
tree could catch, because none existed:

  P227  It published the aggregate "229 lines / 389 occurrences in the 4 content files" in
        SEVEN files.  Exactly one of them (agents/top.md) names which four; the other six do
        not -- including compose/patterns.md, the file P224 wrote so that "no other KB needs
        a pass 74".  So the copy meant to travel is the unnamed one.  Pass 75 reproduced the
        figure only by searching all 70 four-subsets at the cited commit; exactly one
        matches.  An aggregate whose file set is not named next to it is not reproducible,
        so this module refuses to aggregate over an unnamed set.

  P228  It compared a share expressed in USERS (Google Classroom, ~150M, K-12-weighted)
        against a share expressed in INSTITUTIONS (Canvas, US higher ed) and concluded the
        KB's attention was "inversely proportional to the installed base".  Those two
        numbers do not share a denominator.  A share figure means nothing without its
        SEGMENT (K-12 vs higher ed) and its UNIT (users / institutions / installations), so
        this module refuses to rank across either.

The refusals are the point.  A permissive version of this instrument would reproduce pass
74's conclusion, which is why `test_coverage.py` keeps one as a negative control.
"""
import re

SEGMENTS = ('K-12', 'HigherEd')
UNITS = ('institutions', 'users', 'installations')
# Provenance of a share figure.  This tree has never once reached a market-share source:
# passes 74 and 75 both measured EGRESS_BLOCKED on all of them, so SOURCE-VERIFIED is a
# value the data has never carried.  It stays in the vocabulary so that the day a source is
# reachable, the figure can be distinguished from one that came off a search snippet.
PROVENANCE = ('SOURCE-VERIFIED', 'SEARCH-CHANNEL', 'EGRESS_BLOCKED')


class Refusal(Exception):
    """Raised instead of returning a number that would not mean anything."""


class Row:
    """One platform's installed-base datum.  Share is optional: the ORDER survives an
    EGRESS_BLOCKED channel even when the percentage does not (P224 step 4)."""

    def __init__(self, platform, segment, unit, rank, share=None,
                 provenance='EGRESS_BLOCKED', aliases=(), self_hostable=None):
        if segment not in SEGMENTS:
            raise Refusal(f'unknown segment {segment!r}; closed vocabulary is {SEGMENTS}')
        if unit not in UNITS:
            raise Refusal(f'unknown unit {unit!r}; closed vocabulary is {UNITS}')
        if provenance not in PROVENANCE:
            raise Refusal(f'unknown provenance {provenance!r}')
        if share is not None and provenance == 'EGRESS_BLOCKED':
            raise Refusal(
                f'{platform}: a share of {share} cannot be published with provenance '
                'EGRESS_BLOCKED -- publish the rank and leave share=None (P224 step 4)')
        self.platform = platform
        self.segment = segment
        self.unit = unit
        self.rank = rank
        self.share = share
        self.provenance = provenance
        self.aliases = tuple(aliases)
        self.self_hostable = self_hostable

    @property
    def cohort(self):
        """The only scope inside which two rows may be compared."""
        return (self.segment, self.unit)

    def names(self):
        return (self.platform,) + self.aliases


def count_mentions(text, row):
    """Occurrences of a platform in one file's text, counting each alias once per hit.

    Anchored on word boundaries, which is what a bare `grep -oi` is not: without \\b,
    'D2L' matches inside 'D2LX' and 'Clever' inside 'Cleverly'.  Rule 1 of P126 -- run the
    versioned instrument, not a grep written during the pass.
    """
    total = 0
    for name in row.names():
        total += len(re.findall(r'(?<!\w)' + re.escape(name) + r'(?!\w)', text, re.I))
    return total


def count_lines(text, row):
    """Lines mentioning the platform.  Reported separately from occurrences because the two
    diverge badly in this tree: one line can carry a platform eight times."""
    hits = 0
    for line in text.splitlines():
        if any(re.search(r'(?<!\w)' + re.escape(n) + r'(?!\w)', line, re.I) for n in row.names()):
            hits += 1
    return hits


def aggregate(fileset, rows, read=None):
    """Coverage of each platform over a NAMED set of files.

    `fileset` is an explicit, ordered list of paths.  Refuses an empty one: P227 exists
    because "the 4 content files" named nothing and cost pass 75 a 70-subset search to
    reproduce.  The returned dict carries the file set back out so a caller cannot publish
    the number without it.
    """
    if not fileset:
        raise Refusal('refusing to aggregate over an unnamed/empty file set (P227)')
    if len(set(fileset)) != len(fileset):
        raise Refusal(f'file set repeats a path, which would double-count: {fileset}')
    read = read or (lambda p: open(p, encoding='utf-8', errors='replace').read())
    texts = {p: read(p) for p in fileset}
    out = {}
    for row in rows:
        occ = sum(count_mentions(t, row) for t in texts.values())
        lines = sum(count_lines(t, row) for t in texts.values())
        out[row.platform] = {'lines': lines, 'occurrences': occ, 'absent': occ == 0}
    return {'fileset': list(fileset), 'coverage': out}


def inversions(rows, coverage):
    """Platforms whose KB attention runs against their installed-base rank.

    Refuses a cohort mismatch.  This is the P228 enforcement: pass 74 ranked a users figure
    against an institutions figure, and that is the one comparison this function will not
    make.  Rows must agree on BOTH segment and unit.
    """
    cohorts = {r.cohort for r in rows}
    if len(cohorts) > 1:
        raise Refusal(
            'refusing to rank across cohorts ' + ', '.join(f'{s}/{u}' for s, u in sorted(cohorts))
            + ' -- a share in users and a share in institutions have no common denominator '
              '(P228). Rank within one cohort, or rank neither.')
    ranked = sorted(rows, key=lambda r: r.rank)
    found = []
    for i, hi in enumerate(ranked):
        for lo in ranked[i + 1:]:
            a = coverage[hi.platform]['occurrences']
            b = coverage[lo.platform]['occurrences']
            if a < b:
                found.append({
                    'expected_higher': hi.platform, 'expected_lower': lo.platform,
                    'occ_higher': a, 'occ_lower': b, 'cohort': hi.cohort,
                    'factor': None if a == 0 else round(b / a, 1),
                })
    return found
