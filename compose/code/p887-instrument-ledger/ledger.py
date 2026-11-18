"""p887 — `886-G5`'s acceptance test: diff what the INSTRUMENTS know against what the SHELVES say.

🔴 THE CASE THAT OPENED THIS. `verticals/solutions.md` published
`OS4ED/openSIS-Classic` as *"GPL per README; no licence file"* and *"treat as all rights
reserved"*. Its grant is **GPL-2.0, 17,286 B, at `master/docs/License.txt`** — and the
refutation was ALREADY COMMITTED to this repository, in
`compose/code/pass275-grant-enumeration/enumeration_gate.py`'s own docstring, for roughly
**611 passes**, while three live shelves published the false absence.

🔵 `gate-enumeration` was BUILT on that row and PASSES. `gate-absence` PASSES. **Both read
the shelves; neither reads the instrument docstrings, which is where the answer lived.**

🟢 `886-G5`'s acceptance test, verbatim: *every `compose/code/*/README.md` and module
docstring that names an `owner/repo` AND a grant verdict is extracted into a ledger, and
that ledger is diffed against the live shelf cell for the same slug. Disagreements are
findings.* 🔴 `p886` corrected the one row it found BY ACCIDENT and did not build the
ledger, so **the size of this class was UNKNOWN**. This measures it.

🟢 `886-G3` COMPLIANCE: slugs come from `lib/slug_extract.py`, the tested helper, never
from an inline `grep -oE 'github\\.com/<a>/<b>'`. That is the whole point of `886-G3`.

Offline. No network. Controls: `python3 test_ledger.py`.
Run: `python3 -I ledger.py --root ../../.. --out <tsv>`
"""

import argparse
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..', 'lib')))

from slug_extract import extract_slugs  # noqa: E402

# The families this base publishes. Order matters: longest/most specific first, so
# `BSD-3-Clause` is never shortened to `BSD` and `AGPL-3.0` never to `GPL-3.0`.
FAMILY_RE = re.compile(r'''
    \b(
      AGPL-3\.0 | AGPL-?3 | AGPLv3
    | LGPL-2\.1 | LGPL-3\.0 | LGPL-\?
    | GPL-2\.0 | GPL-3\.0 | GPL-\?
    | Apache-2\.0 | Apache\s+2\.0 | Apache\s+License
    | BSD-3-Clause | BSD-2-Clause | BSD
    | MPL-2\.0 | EPL-2\.0 | ECL-2\.0 | CDDL
    | MulanPSL-2\.0 | ODbL-1\.0 | OFL-1\.1
    | CC-BY-SA-4\.0 | CC-BY-4\.0 | CC0-1\.0
    | Unlicense | ISC | Zlib | MIT
    | NOASSERTION | NO-GRANT-FILE | UNRECOGNISED
    )\b
''', re.VERBOSE)

# A verdict word must be NEAR the slug. 🔵 Why a WINDOW and not the same line: an
# instrument docstring writes the slug and its verdict as prose across two or three lines,
# which is exactly the shape `openSIS-Classic`'s refutation was in.
WINDOW = 3

# 🔴 THREE DEFECTS THIS LEDGER'S FIRST RUN HAD, measured and recorded rather than tuned
# away in silence.  The first run reported **70 DISAGREE**.  Every one inspected was a
# false positive, and they came from exactly three causes:
#
# 1. A MARKDOWN TABLE ROW IS A SELF-CONTAINED RECORD.
#    `compose/code/p441-tree-licence-enumeration/README.md:50` is a four-row table —
#    `openedx/XBlock`=Apache-2.0, `nvaccess/nvda`=GPL-2.0, `SchoolUtils/WebUntis`=MIT,
#    `veraPDF/veraPDF-library`=GPL-3.0+MPL-2.0.  A ±3-line window over it attributed all
#    five families to `XBlock`, whose own row says Apache-2.0 and agrees with the shelf.
#    🟢 Fix: a line beginning `|` is scoped to ITSELF.
#
# 2. A SNAPSHOT OF A SHELF IS NOT AN INSTRUMENT'S KNOWLEDGE.
#    `compose/code/p119-carried-column-audit/current/agents-trending.current.md` is a
#    COPY of a shelf, kept so that audit can diff it.  Diffing a shelf snapshot against
#    the live shelf is not `886-G5`'s question — `886-G5` asks what the INSTRUMENTS know.
#    🟢 Fix: `SNAPSHOT_HINT` excludes those corpora and the count reports them separately.
#
# 3. AN ENUMERATION OF FAMILIES IS NOT A VERDICT ABOUT A REPOSITORY.
#    A classifier's family table or a ladder's candidate list names eight families in six
#    lines.  🟢 Fix: a scope naming `ENUM_CEILING` or more distinct families is an
#    enumeration, not an assertion, and is recorded as such.
#
# 🔵 Stated plainly, because it is the finding and not a footnote: `886-G5`'s acceptance
# test says "names an `owner/repo` AND a grant verdict", and does NOT say what binds the
# two.  The binding is the whole instrument.  A ledger with the wrong binding produces 70
# findings that cost a pass to triage and teach nothing.
ENUM_CEILING = 3

# 🔴 DEFECT 4, found by HAND-ADJUDICATING the corrected run's 4 disagreements — which is
# the only reason it was found, and the reason this ledger must never be read as a verdict.
#
# A CORRECTION TABLE publishes BOTH the refuted family and the true one, in adjacent cells
# of ONE row.  A row-scoped read takes both and cannot tell which is which.  All three
# false positives in the corrected run are this one shape:
#
#   p117-second-channel/README.md:116   | `openedx/edx-ora2` | 🟢 Apache-2.0 | 🔴 AGPL-3.0 |
#       -> ledger read `Apache-2.0`; that is the column headed "published", i.e. the value
#          the instrument exists to REFUTE.  Shelf says AGPL-3.0.  Shelf is RIGHT.
#   p208-seeded-error-audit/README.md:65  "`openfun/ralph` was published **Apache-2.0** ...
#       while its blob is **MIT**"  -> ledger read Apache-2.0.  Shelf says MIT.  RIGHT.
#   grant-ladder-v4/README.md:38  | `portabilis/i-educar` | 🔴 LGPL-3.0 · 18 092 B | GPL-2.0 |
#       -> ledger read LGPL-3.0, the refuted value.  Shelf carries GPL-2.0.  RIGHT.
#
# 🔵 So an instrument that RECORDS a past error is indistinguishable, to a family-token
# scan, from an instrument that ASSERTS one.  This base is full of the former by design —
# that is what its correction records ARE.
#
# 🟢 These scopes are therefore classed `CORRECTION` and EXCLUDED from claims rather than
# resolved by guessing which cell is the truth.  Picking "the last family in the row" would
# have worked on all three above and is still a guess; `886-G4`'s rule applies — a document
# that needs reading must not be believed on structure alone.
REFUTATION_MARK = re.compile(
    r'(?:🔴|🟢\s*(?:published|was published)|'
    r'\bactually\b|\bwas published\b|\bpublished\b.{0,40}\bwhile\b|'
    r'\bcorrected\b|\bCORRECTION\b|\bREGRESSION\b|\bthe cell was never right\b|'
    r'\bshould read\b|\bnot\b.{0,20}\brelicensing\b)',
    re.IGNORECASE)

SNAPSHOT_HINT = ('/current/', '.current.md', '/snapshot', '/archive', 'archive/')

NORMALISE = {
    'Apache 2.0': 'Apache-2.0', 'Apache License': 'Apache-2.0',
    'AGPL3': 'AGPL-3.0', 'AGPL-3': 'AGPL-3.0', 'AGPLv3': 'AGPL-3.0',
}

# A FIXTURE tier, per `gate-slug-presence`'s rule: an instrument's own test fixtures are
# not holdings about the world, so a slug seen only inside a `fixtures/` path or a
# `test_*` file is recorded and excluded from the findings count.
FIXTURE_HINT = ('/fixtures', 'fixtures-', '/test_', 'test_')


def norm_family(f):
    f = re.sub(r'\s+', ' ', f).strip()
    return NORMALISE.get(f, f)


def is_fixture(relpath):
    low = relpath.lower()
    return any(h in low for h in FIXTURE_HINT)


def is_snapshot(relpath):
    low = relpath.lower()
    return any(h in low for h in SNAPSHOT_HINT)


def scope_for(lines, i):
    """The text a slug on line `i` may draw a verdict from.

    A markdown table row is its OWN scope — defect 1 above.  Anything else gets the
    ±WINDOW prose window, which is the shape `openSIS-Classic`'s refutation was in.
    """
    line = lines[i]
    if line.lstrip().startswith('|'):
        return line, 'ROW'
    lo = max(0, i - WINDOW)
    hi = min(len(lines), i + WINDOW + 1)
    return '\n'.join(lines[lo:hi]), 'WINDOW'


def harvest(root):
    """Every (instrument, slug, family, line) an instrument's own text asserts."""
    base = os.path.join(root, 'compose', 'code')
    rows = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in ('.git', '__pycache__')]
        for fn in filenames:
            if not fn.endswith(('.py', '.sh', '.md')):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, root)
            try:
                with open(path, encoding='utf-8') as fh:
                    lines = fh.read().splitlines()
            except (OSError, UnicodeDecodeError):
                continue
            for i, line in enumerate(lines):
                slugs = extract_slugs(line)
                if not slugs:
                    continue
                ctx, how = scope_for(lines, i)
                seen = []
                for m in FAMILY_RE.finditer(ctx):
                    f = norm_family(m.group(1))
                    if f not in seen:
                        seen.append(f)
                if not seen:
                    continue
                klass = ('ENUMERATION' if len(seen) >= ENUM_CEILING
                         else 'SNAPSHOT' if is_snapshot(rel)
                         else 'FIXTURE' if is_fixture(rel)
                         else 'CORRECTION' if (len(seen) >= 2
                                               and REFUTATION_MARK.search(ctx))
                         else 'CLAIM')
                for f in seen:
                    rows.append({
                        'instrument': rel, 'slug': slugs[0], 'family': f,
                        'line': i + 1, 'klass': klass, 'scope': how,
                        'quote': line.strip()[:160],
                    })
    return rows


SHELVES = ('agents/top.md', 'repos/foundations.md', 'verticals/solutions.md')


def shelf_index(root):
    """What the LIVE shelves say, per slug: every family asserted on a line naming it."""
    idx = {}
    for sh in SHELVES:
        path = os.path.join(root, sh)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8') as fh:
            lines = fh.read().splitlines()
        for i, line in enumerate(lines):
            for slug in extract_slugs(line):
                fams = {norm_family(m.group(1)) for m in FAMILY_RE.finditer(line)}
                if not fams:
                    continue
                e = idx.setdefault(slug.lower(), {'slug': slug, 'fams': set(),
                                                  'where': []})
                e['fams'] |= fams
                e['where'].append('%s:%d' % (sh, i + 1))
    return idx


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--out', required=True)
    a = ap.parse_args(argv)

    rows = harvest(a.root)
    shelf = shelf_index(a.root)

    holdings = [r for r in rows if r['klass'] == 'CLAIM']
    by_class = {}
    for r in rows:
        by_class[r['klass']] = by_class.get(r['klass'], 0) + 1

    # Collapse to one claim per (slug, family) with its first instrument citation.
    claims = {}
    for r in holdings:
        k = (r['slug'].lower(), r['family'])
        claims.setdefault(k, r)

    agree, absent_on_shelf, disagree = [], [], []
    for (slug_l, fam), r in sorted(claims.items()):
        e = shelf.get(slug_l)
        if e is None:
            absent_on_shelf.append((r, 'SLUG-NOT-ON-ANY-SHELF'))
        elif fam in e['fams']:
            agree.append((r, e))
        else:
            disagree.append((r, e))

    with open(a.out, 'w', encoding='utf-8') as w:
        w.write('verdict\tslug\tinstrument_family\tshelf_families\tinstrument\tline\t'
                'shelf_where\tquote\n')
        for r, e in disagree:
            w.write('DISAGREE\t%s\t%s\t%s\t%s\t%d\t%s\t%s\n'
                    % (r['slug'], r['family'], '+'.join(sorted(e['fams'])),
                       r['instrument'], r['line'], e['where'][0], r['quote']))
        for r, why in absent_on_shelf:
            w.write('%s\t%s\t%s\t-\t%s\t%d\t-\t%s\n'
                    % (why, r['slug'], r['family'], r['instrument'], r['line'],
                       r['quote']))
        for r, e in agree:
            w.write('AGREE\t%s\t%s\t%s\t%s\t%d\t%s\t%s\n'
                    % (r['slug'], r['family'], '+'.join(sorted(e['fams'])),
                       r['instrument'], r['line'], e['where'][0], r['quote']))

    print('# p887 instrument-ledger — 886-G5')
    print('# files walked under compose/code/: .py .sh .md')
    print('# raw (slug, family) mentions: %d' % len(rows))
    for k in sorted(by_class):
        print('#    %-12s %d' % (k, by_class[k]))
    print('# distinct instrument CLAIMS: %d' % len(claims))
    print('# slugs on live shelves carrying a family: %d' % len(shelf))
    print('')
    print('# AGREE                 %d' % len(agree))
    print('# DISAGREE              %d   <- 886-G5 findings' % len(disagree))
    print('# SLUG-NOT-ON-ANY-SHELF %d   <- an instrument knows a repo no shelf carries'
          % len(absent_on_shelf))
    if disagree:
        print('')
        print('## DISAGREEMENTS — an instrument and a shelf assert different families')
        for r, e in disagree:
            print('  %-34s instrument=%-14s shelf=%-22s %s:%d'
                  % (r['slug'], r['family'], '+'.join(sorted(e['fams'])),
                     r['instrument'], r['line']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
