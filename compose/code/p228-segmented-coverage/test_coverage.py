#!/usr/bin/env python3
"""Controls for P227 + P228.

Rule 2 of P126: a positive control only enables an instrument if it exercises the case where
the instrument can FAIL.  The case that matters here is the one pass 74 actually got wrong --
Google Classroom's share quoted in USERS against Canvas's in INSTITUTIONS -- so the control
pair is (Classroom K-12/users, Canvas HigherEd/institutions), which MUST be refused, held
next to a same-cohort pair that must be ranked normally.  A control built only from
well-formed cohorts would pass without ever exercising the refusal.

The negative control at the end is a permissive ranker that ignores segment and unit.  It
reproduces pass 74's "inverse attention" conclusion from the same inputs, which is the
evidence that the refusal -- not the arithmetic -- is what this module adds.
"""
import sys
from coverage import Row, Refusal, aggregate, inversions, count_mentions, count_lines

# Shares are deliberately absent on EGRESS_BLOCKED rows: passes 74 and 75 both failed to
# reach a market-share source, so only the ORDER is asserted here (P224 step 4).
K12 = [
    Row('Google Classroom', 'K-12', 'institutions', rank=1, self_hostable=False),
    Row('Canvas', 'K-12', 'institutions', rank=2, aliases=('Instructure',), self_hostable=False),
    Row('Schoology', 'K-12', 'institutions', rank=3, self_hostable=False),
    Row('Moodle', 'K-12', 'institutions', rank=4, self_hostable=True),
]
HIGHER = [
    Row('Canvas', 'HigherEd', 'institutions', rank=1, aliases=('Instructure',)),
    Row('Moodle', 'HigherEd', 'institutions', rank=2, self_hostable=True),
    Row('Google Classroom', 'HigherEd', 'institutions', rank=3),
]

DOCS = {
    'a.md': 'Canvas and Instructure ship canvas-lms-mcp. Moodle too.\nMoodle again.',
    'b.md': 'Moodle, Moodle, Moodle. A D2LX gateway is not D2L.\nCleverly is not Clever.',
}
READ = lambda p: DOCS[p]


def main():
    ok = n = 0

    def check(name, cond, detail=''):
        nonlocal ok, n
        n += 1
        if cond:
            ok += 1
            print(f'PASS {name}')
        else:
            print(f'FAIL {name}: {detail}')

    # --- P227: the file set must be named -------------------------------------------------
    try:
        aggregate([], K12, read=READ)
        check('P227: empty file set is refused', False, 'no Refusal raised')
    except Refusal as e:
        check('P227: empty file set is refused', 'unnamed' in str(e).lower())

    try:
        aggregate(['a.md', 'a.md'], K12, read=READ)
        check('P227: repeated path is refused (would double-count)', False, 'no Refusal')
    except Refusal as e:
        check('P227: repeated path is refused (would double-count)', 'repeats' in str(e))

    agg = aggregate(['a.md', 'b.md'], K12, read=READ)
    check('P227: the aggregate carries its file set back out',
          agg['fileset'] == ['a.md', 'b.md'], agg['fileset'])

    # --- word-boundary anchoring: what a bare `grep -oi` gets wrong ------------------------
    d2l = Row('D2L', 'HigherEd', 'institutions', rank=9)
    clever = Row('Clever', 'K-12', 'institutions', rank=9)
    check('anchor: D2LX does not count as D2L',
          count_mentions(DOCS['b.md'], d2l) == 1, count_mentions(DOCS['b.md'], d2l))
    check('anchor: Cleverly does not count as Clever',
          count_mentions(DOCS['b.md'], clever) == 1, count_mentions(DOCS['b.md'], clever))
    check('alias: Instructure counts toward Canvas',
          count_mentions(DOCS['a.md'], K12[1]) == 3, count_mentions(DOCS['a.md'], K12[1]))
    check('lines and occurrences are reported apart',
          agg['coverage']['Moodle']['lines'] == 3
          and agg['coverage']['Moodle']['occurrences'] == 5,
          agg['coverage']['Moodle'])
    check('absence is flagged, not silently zero',
          agg['coverage']['Schoology']['absent'] is True
          and agg['coverage']['Moodle']['absent'] is False)

    # --- P228: THE CASE THAT MATTERS ------------------------------------------------------
    mixed = [
        Row('Google Classroom', 'K-12', 'users', rank=1),
        Row('Canvas', 'HigherEd', 'institutions', rank=2, aliases=('Instructure',)),
    ]
    try:
        inversions(mixed, agg['coverage'])
        check('P228 THE CASE THAT MATTERS: users vs institutions is refused',
              False, 'the pass-74 comparison was computed instead of refused')
    except Refusal as e:
        check('P228 THE CASE THAT MATTERS: users vs institutions is refused',
              'no common denominator' in str(e), str(e))

    try:
        inversions([K12[0], HIGHER[0]], agg['coverage'])
        check('P228: same unit, different segment is still refused', False, 'no Refusal')
    except Refusal as e:
        check('P228: same unit, different segment is still refused', 'cohorts' in str(e))

    # --- ranking inside one cohort does work ----------------------------------------------
    inv = inversions(K12, agg['coverage'])
    pairs = {(i['expected_higher'], i['expected_lower']) for i in inv}
    check('K-12 cohort: Classroom(1) under Moodle(4) is an inversion',
          ('Google Classroom', 'Moodle') in pairs, sorted(pairs))
    check('K-12 cohort: Classroom(1) under Canvas(2) is an inversion',
          ('Google Classroom', 'Canvas') in pairs, sorted(pairs))
    check('a zero-coverage platform reports factor None, not a division by zero',
          all(i['factor'] is None for i in inv if i['occ_higher'] == 0))
    check('HigherEd cohort: Canvas(1) over Moodle(2) is NOT an inversion '
          '(the segment that justifies this KB)',
          ('Canvas', 'Moodle') not in
          {(i['expected_higher'], i['expected_lower'])
           for i in inversions(HIGHER, aggregate(['a.md'], HIGHER, read=READ)['coverage'])})

    # --- negative control -----------------------------------------------------------------
    # A ranker that ignores cohort reproduces pass 74's conclusion from these same rows.
    # If this control ever stops finding the inversion, the control has gone blind and the
    # refusal above is no longer evidence of anything.
    n += 1
    permissive = sorted(mixed, key=lambda r: r.rank)
    naive = agg['coverage'][permissive[0].platform]['occurrences'] \
        < agg['coverage'][permissive[1].platform]['occurrences']
    if naive:
        ok += 1
        print('PASS negative control: a cohort-blind ranker DOES report the pass-74 '
              'inversion, so the refusal is what differs')
    else:
        print('FAIL negative control: the cohort-blind ranker found nothing; '
              'the control no longer exercises the defect')

    print(f'\n{ok}/{n} checks passed')
    return 0 if ok == n else 1


if __name__ == '__main__':
    sys.exit(main())
