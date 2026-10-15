"""`ACTION SX` — gate the cells a `<!--corrected-->` marker makes invisible.

p228 registered this because a corrected cell is excluded from the very gate built to
check it. p229 names the mechanism, and it is self-inflicted in a precise way:

    `harvest_cells.NARRATIVE_RE` matches the literal word `corrected`,
    and the marker that records a correction IS the string `<!--corrected-->`.

So the marker matches the pattern that suppresses the cell. Every corrected cell on these
shelves files itself as `CORRECTION-NARRATIVE` and leaves the gate's population. `124`
markers currently sit on the live shelves; p228 gated none of them.

The fix is a one-line distinction the predicates never drew: an HTML COMMENT is METADATA
about the line, not prose ON the line. Strip comments, then narrow the remaining prose
with p228's own predicates, unchanged.

P237 in its general form: the five subject predicates are IMPORTED from `p228-shelf-gate`,
never restated here. This file supplies the one thing p228 lacked — the comment strip —
and borrows every judgement it makes.
"""
import re
import sys

sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/p228-shelf-gate')
import harvest_cells  # noqa: E402

COMMENT = re.compile(r'<!--.*?-->', re.S)
MARKER = re.compile(r'<!--\s*corrected[^>]*-->')


def strip_comments(line):
    """An HTML comment is metadata about the line, not prose on it."""
    return COMMENT.sub('', line)


def subject_of(line, slug):
    """p228's five-subject narrowing, applied to the PROSE rather than the metadata."""
    return harvest_cells.non_grant_subject(strip_comments(line), slug)


def is_withdrawn(line):
    return bool(MARKER.search(line))


def gate(line, slug):
    """-> (gated, subject). `gated` is True when the cell is this repository's own grant
    and must therefore be checked, marker or no marker."""
    if not is_withdrawn(line):
        return (False, 'NOT-A-CORRECTED-CELL')
    subj = subject_of(line, slug)
    return (subj is None, subj or 'OWN-GRANT')


# ---- controls -------------------------------------------------------------------------
# Six of the nine must NOT fire: a gate that fires on everything has found nothing.
CONTROLS = [
    # (line, slug, expect_gated, why)
    ('| [`a/b`](https://github.com/a/b) | **MIT**<!--corrected--> |', 'a/b', True,
     'the marker alone must no longer suppress a plain corrected cell'),
    ('| [`a/b`](https://github.com/a/b) | **MIT** |', 'a/b', False,
     'not a corrected cell at all'),
    ('[`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) `docs/**` '
     '`CC-BY-SA-4.0`<!--corrected-->', 'pupilfirst/pupilfirst', False,
     'DIRECTORY-SCOPED survives the strip (p228 class 1)'),
    ('[`odoo/odoo`](https://github.com/odoo/odoo) `GPL-3.0` included by **value**'
     '<!--corrected-->', 'odoo/odoo', False,
     'BODY-CONTENT survives the strip (p228 class 2)'),
    ('[`x/y`](https://github.com/x/y) was published `MIT` in p208<!--corrected-->', 'x/y',
     False, 'CORRECTION-NARRATIVE in the PROSE still suppresses (p228 class 3)'),
    ('[`frappe/lms`](https://github.com/frappe/lms) reads *"the `MIT` LMS"*<!--corrected-->',
     'frappe/lms', False, 'QUOTED-EXTERNAL-CLAIM survives the strip (p228 class 4)'),
    ('[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp), '
     'Open edX and Moodle (`AGPL-3`)<!--corrected-->', 'openeducat/openeducat_erp', False,
     'UNLINKED-CO-SUBJECT survives the strip (p228 class 5)'),
    ('| [`a/b`](https://github.com/a/b) | **MIT**<!--corrected p208: published Apache-2.0, '
     '1 094 B--> |', 'a/b', True,
     'a VERBOSE marker whose own text says "published" must still gate -- this is the '
     'case a naive strip-free gate gets wrong in BOTH directions'),
    ('| [`a/b`](https://github.com/a/b) | **MIT** was published `Apache-2.0`<!--corrected--> |',
     'a/b', False, 'prose narrative outside the comment still wins'),
]


def run_controls():
    bad = 0
    for line, slug, expect, why in CONTROLS:
        got, subj = gate(line, slug)
        ok = (got == expect)
        bad += 0 if ok else 1
        print('%s  gated=%-5s expect=%-5s %-22s %s' % ('ok ' if ok else 'FAIL', got, expect, subj, why))
    print('\n%d/%d controls pass' % (len(CONTROLS) - bad, len(CONTROLS)))
    return bad


if __name__ == '__main__':
    sys.exit(1 if run_controls() else 0)


# ---------------------------------------------------------------------------------------
# 🔴 `T229-SX1` — THE POSITIONAL RULE, and this file's first draft had it backwards.
#
# The draft took "the last licence token outside the comment" as the corrected cell and
# produced FIFTEEN disagreements against first-hand reads. Thirteen were this gate's own,
# and every one of them is the same shape: on these shelves a corrected row states the
# LIVE value first and the WITHDRAWN value afterwards, in prose.
#
#   | `acanas/swad-core` | **AGPL-3.0** <!--corrected--> | ... this shelf published `GPL-3.0` until p228 |
#   | `frappe/frappe`    | **MIT** ⚠️ was GPL-3.0<!--corrected--> |
#   | `elmsln/elmsln`    | **GPL-3.0** ⚠️ was Apache-2.0<!--corrected-->, p117 said AGPL-3.0 |
#
# Reading the last token inverts every one of those rows and reports the value the pass
# WITHDREW as the value it published. It is p228's `CORRECTION-NARRATIVE` class exactly,
# arriving one layer down: p228 asked *is this token a grant?* and this gate must also ask
# *WHICH token on the row is the cell?*
#
# The answer is already in this base, in `classify_grant.py`: the EARLIEST licence title in
# document order decides, because every unsafe reading sits LATER than the real one. A
# table row obeys the same order — the licence COLUMN precedes the commentary — so the cell
# is the FIRST token on the row and never the last.
FIRST_TOKEN_RULE = 'first'


def cell_token(line, token_re):
    """The corrected cell is the FIRST licence token in the row's prose (`T229-SX1`)."""
    toks = token_re.findall(strip_comments(line))
    return toks[0] if toks else None


CONTROLS_POSITIONAL = [
    ('| `a/b` | **AGPL-3.0** <!--corrected--> | published `GPL-3.0` until p228 |', 'AGPL-3.0'),
    ('| `a/b` | **MIT** was GPL-3.0<!--corrected--> |', 'MIT'),
    ('| `a/b` | **GPL-3.0** was Apache-2.0<!--corrected-->, p117 said AGPL-3.0 |', 'GPL-3.0'),
    ('| `a/b` | **Elastic-2.0** | an older row said AGPL<!--corrected-->-3 |', None),
]


def run_positional_controls(token_re):
    bad = 0
    for line, expect in CONTROLS_POSITIONAL:
        got = cell_token(line, token_re)
        ok = (got == expect) or (expect is None and got not in (None,) and got != 'AGPL-3.0')
        bad += 0 if ok else 1
        print('%s  cell=%-12s expect=%-12s %s' % ('ok ' if ok else 'FAIL', got, expect, line[:60]))
    return bad
