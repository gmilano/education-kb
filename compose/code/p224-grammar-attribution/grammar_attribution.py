"""p224 - ACTION RU's instrument: attribute every bare GNU mention to a ROW, then to its
ecosystem GRAMMAR.

`ACTION RU` was p222's registered highest-priority action for p223, carried unrun into
p224 ("p224 has no excuse"). It asks whether p221's headline is restatable:

    limb 1: 50+ of the 2 208 bare GNU mentions attach to a row whose grant was read
            from a CRAN `DESCRIPTION` or an Odoo `__manifest__.py` -> the 94.3% must be
            restated and the census republished with a grammar column.
    limb 2: 0-49 -> the grammar finding is real but numerically small, and 94.3% stands
            as a token count with a footnote.

Why the question is not rhetorical. p221 counted bare GNU *tokens*. p222 then showed
that `-only`/`-or-later` is SPDX's notation, and that in CRAN (`DESCRIPTION`) and Odoo
(`__manifest__.py`) the bound is carried by OMISSION - a bare `GPL-3` there is a
POSITIVE `only`, not a silence. So a bare token on a CRAN- or Odoo-read row is not an
unspecified grant; it is a specified one, spelled in that ecosystem's grammar. Those
mentions are in p221's numerator and should not be.

p221's census is aggregated BY TOKEN (24 rows, `evidence/rh-range-census...tsv`), so the
attribution this action needs was never built. That is what this module adds.

THE UNIT. Eight consecutive passes have had a unit mismatch in the headline, so it is
stated before the code: p221's unit was the TOKEN; p222's correction operates on the
ECOSYSTEM GRAMMAR; the unit here is the (mention -> ROW -> grammar) edge. A mention that
cannot be attributed to exactly one row is NOT attributed - it is reported. p222 produced
two false `GRANT-CONFLICT`s by attributing a token to whichever slug shared its line,
when the token belonged to a comparison, so multi-slug lines are a declared state here
rather than a guess.

Bareness is not re-implemented. p221's `parse_range()` is imported and called, so "bare"
means exactly what it meant when the 2 208 was published. If that definition is wrong,
both numbers are wrong together and the comparison still holds.
"""

import importlib.util
import os
import re

_P221 = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', 'p221-licence-version-range', 'version_range.py',
)


def _load_p221():
    """Import p221's instrument by path, so the bare/bound definition is literally p221's."""
    spec = importlib.util.spec_from_file_location('p221_version_range', os.path.normpath(_P221))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_p221 = _load_p221()
parse_range = _p221.parse_range

# A GNU token as p221 matches it. Re-used rather than re-derived.
_TOKEN = re.compile(r'\b(a?gpl|lgpl)-([0-9](?:\.[0-9])?)\b', re.I)

# `AGPL-6 d` in a liveness table is a DAY COUNT. p221 found exactly one and kept the
# guard because the next table would have more. It is kept here for the same reason.
_DAYCOUNT = re.compile(r'\b(?:a?gpl|lgpl)-[0-9]+(?:\.[0-9])?\s*d\b', re.I)

# An `owner/repo` slug. Deliberately NOT anchored to github.com: these shelves cite the
# same row as a bare slug, as a full URL and inside a raw.githubusercontent.com path.
#
# The OWNER half forbids a dot, and that is not cosmetic. GitHub account names are
# alphanumeric-and-hyphen only, so a dotted "owner" is always a HOSTNAME - and this
# instrument's own first run proved why it matters: `https://github.com/openeducat/
# openeducat_erp` yielded the phantom row `github.com/openeducat` ALONGSIDE the real
# one, which made a line naming ONE row look like a line naming TWO, sent it to
# `bare_ambiguous_line`, and would have reported a false limb 2 with attribution near
# zero. The phantom is already visible in the shelves' own grep counts (112 x
# `github.com/openeducat`, 15 x `github.com/odoo`).
#
# T224-2, and the eighth consecutive unit mismatch: the unit is the SLUG, not the
# adjacent path pair.
_SLUG = re.compile(r'(?:[a-z][a-z0-9+.-]*://[^\s)\]]*?/)?'
                   r'\b([A-Za-z0-9][A-Za-z0-9-]*)/([A-Za-z0-9][A-Za-z0-9._-]*)\b')

# Path segments that look like `owner/repo` but are not rows. Without this the file's own
# evidence links (`evidence/foo.tsv`) and doc links become phantom rows.
_NOT_A_SLUG = {
    'evidence', 'compose', 'intel', 'agents', 'repos', 'verticals', 'archive', 'code',
    'docs', 'lang', 'main', 'master', 'HEAD', 'refs', 'blob', 'tree', 'raw', 'www',
    'github', 'com', 'org', 'net', 'http', 'https', 'tmp', 'home', 'user', 'etc',
    'README', 'LICENSE',
}

# A token whose span puts it in a DEPENDENCY's scope is not the row's own grant.
#
# T224-3, found by inspecting this instrument's own output rather than trusting it.
# `repos/trending.md` l.12548 carries ONE row - `CambridgeAssessmentResearch/KernEqWPS`,
# an MIT package - and the tokens `GPL-2` and `GPL-3` on that line belong to its R
# dependency `MASS`. The single-slug guard cannot catch it: the line names exactly one
# row, and the real subject of the token (`MASS`) is not a GitHub slug at all. Counting
# them put ACTION RU's numerator at 85 when its own population is 83.
#
# So p222's false-GRANT-CONFLICT defect has a second shape, and the rule generalises:
# the unit is the grant's SUBJECT, not the row sharing its line. Ninth consecutive unit
# mismatch in this KB's headline series, and the first one this KB found in its own
# live output before publishing it.
_DEPENDENCY_SCOPE = re.compile(
    r'\b(?:imports?|depends?|suggests?|requires?|dependenc(?:y|ies)|vendored|bundled|'
    r'upstream|transitive|sub[-\s]?dependenc)\b', re.I)

# Span window around a token, in characters. The bound may sit either side of the token
# (`GPL-3.0-or-later`, "GPL-3.0, or any later version", "LGPL-3 (non-upgradable)"), and
# p223's rule - the unit is the matched SPAN, not the line - is why this is a window and
# not the whole line: a bound belonging to a DIFFERENT token elsewhere on the line must
# not exonerate this one.
_SPAN = 48


def _is_slug(owner, repo):
    if '.' in owner:          # a hostname, never a GitHub account name
        return False
    if owner in _NOT_A_SLUG or repo in _NOT_A_SLUG:
        return False
    if owner.lower() in {s.lower() for s in _NOT_A_SLUG}:
        return False
    # a file name, not a repo
    if re.search(r'\.(md|tsv|py|json|php|txt|csv|yml|yaml|sh|html)$', repo, re.I):
        return False
    return True


_HOST = re.compile(r'\b(?:[a-z][a-z0-9+.-]*://)?(?:[a-z0-9-]+\.)+[a-z]{2,}/', re.I)


def slugs_on(line):
    """Distinct `owner/repo` rows named on one line, lowercased (GitHub slugs are
    case-insensitive, and these shelves carry 47 case-variant clusters).

    URL hosts are removed FIRST so that `github.com/owner/repo` contributes the row and
    not the host pair - see `_SLUG` for why that distinction decides the verdict.
    """
    text = _HOST.sub(' ', line or '')
    out = []
    for owner, repo in _SLUG.findall(text):
        if not _is_slug(owner, repo):
            continue
        s = '{}/{}'.format(owner.lower(), repo.lower())
        if s not in out:
            out.append(s)
    return out


def mentions_in_line(line):
    """Every GNU token on one line, each with its own span verdict.

    Returns a list of dicts: {'token', 'bare', 'span'}. Bareness is decided on the
    SPAN, not the line, and the day-count artefact is stripped first.
    """
    raw = _DAYCOUNT.sub(' ', line or '')
    out = []
    for m in _TOKEN.finditer(raw):
        lo = max(0, m.start() - _SPAN)
        hi = min(len(raw), m.end() + _SPAN)
        span = raw[lo:hi]
        parsed = parse_range(span)
        dep = bool(_DEPENDENCY_SCOPE.search(span))
        out.append({
            'token': m.group(0).upper(),
            'bare': bool(parsed['gnu']) and parsed['bound'] == 'unspecified' and not dep,
            'dependency_scoped': dep,
            'span': span,
        })
    return out


def attribute(lines, grammar_of):
    """Attribute each BARE GNU mention to a row and to that row's ecosystem grammar.

    `grammar_of` maps a lowercased slug to its grammar ('cran', 'odoo', 'spdx', ...).
    A slug absent from the map is 'unread' - its grant's channel is not recorded, which
    is a state, not a zero.

    Returns a dict with the counts ACTION RU's limbs are stated in, plus the states that
    would otherwise be invisible: mentions on a line naming several rows, and mentions
    on a line naming none.
    """
    totals = {
        'gnu_mentions': 0,
        'bare_mentions': 0,
        'qualified_mentions': 0,
        'bare_attributed': 0,
        'bare_ambiguous_line': 0,
        'bare_no_slug_on_line': 0,
        'dependency_scoped': 0,
        'by_grammar': {},
        'by_row': {},
    }
    for line in lines:
        ms = mentions_in_line(line)
        if not ms:
            continue
        rows = slugs_on(line)
        for mention in ms:
            totals['gnu_mentions'] += 1
            if mention.get('dependency_scoped'):
                totals['dependency_scoped'] += 1
                continue
            if not mention['bare']:
                totals['qualified_mentions'] += 1
                continue
            totals['bare_mentions'] += 1
            if len(rows) == 0:
                totals['bare_no_slug_on_line'] += 1
                continue
            if len(rows) > 1:
                totals['bare_ambiguous_line'] += 1
                continue
            row = rows[0]
            totals['bare_attributed'] += 1
            gram = grammar_of.get(row, 'unread')
            totals['by_grammar'][gram] = totals['by_grammar'].get(gram, 0) + 1
            totals['by_row'][row] = totals['by_row'].get(row, 0) + 1
    return totals


def verdict(totals, threshold=50):
    """ACTION RU's registered limbs, evaluated on the omission-grammar subtotal."""
    n = totals['by_grammar'].get('cran', 0) + totals['by_grammar'].get('odoo', 0)
    return {
        'omission_grammar_bare_mentions': n,
        'threshold': threshold,
        'limb': 1 if n >= threshold else 2,
        'means': (
            'restate the 94.3%: these mentions are POSITIVE only-grants, not silences'
            if n >= threshold else
            'the grammar finding is real but numerically small; 94.3% stands as a token '
            'count with a footnote'
        ),
    }
