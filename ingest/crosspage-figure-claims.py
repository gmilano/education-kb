#!/usr/bin/env python3
"""p538 — Gap 538-C: cross-page contradiction sweep for NUMERIC claims.

WHY THIS EXISTS

  This base already has a cross-page contradiction sweep:
  compose/code/p121-stale-token-crosspage/crosspage.py, built at p121 after
  `FWU-DE/ais-chat` carried a stale licence token through three passes of
  corrections published ~65 lines away from it. It keys on LICENCE TOKENS.

  p538 found the same failure in a dimension p121 cannot see. agents/top.md
  said the Moodle MCP field "sums to under 40 stars" and that "nobody has above
  27 stars". repos/foundations.md had, since p529, headed its own Moodle section
  "222 addresses, not eleven; ceiling 52 and ungranted" and named
  loyaniu/moodle-mcp at 52 outright. The two pages contradicted each other for
  NINE passes, and the stale page LINKED TO the corrected one.

  A licence token is a small closed vocabulary, so p121 can match on it. A star
  count is an open integer, so nothing on this base compared one page's figure
  for an address against another page's figure for the same address. This does.

WHAT IT MEASURES

  For every GitHub address, every STAR CLAIM made about it on a curated page:

    STARS_COL    the address is in a table row, and the cell under the column
                 whose HEADER matches /star/i is a bare integer (optionally
                 bold, or space-/nbsp-grouped). Header-aware, because the first
                 cut of this instrument took any bare cell and could not tell a
                 Stars column from a Tools or Forks column -- on the Moodle
                 table that produced [1, 22, 27] for G36maid, which is one fork,
                 twenty-two tools and twenty-seven stars read as one claim.
    MARKED       the address's line carries `<n>*`, `<n> stars`, `<n> star`
                 within the same cell or sentence.

  Two claims CONTRADICT when they are about the same address, sit on different
  curated pages, and differ. Growth is not a defect -- a repository gains stars
  -- so the report ranks by RELATIVE gap and the caller judges. What the Moodle
  case looked like is a 27-vs-52 split that never closed.

WHAT IT DOES NOT DO -- stated so silence is not read as coverage

  1. Header-aware column matching removes the fork/tool confusion but not every
     case: a prose MARKED figure can still be a star count quoted from a
     different date, and a table with no /star/i header contributes nothing at
     all (silence, not coverage -- the count of such tables is reported).
     Precision is therefore BELOW 1 and is REPORTED, not asserted: --audit
     prints every claim with its source line so the rate can be measured by
     hand rather than trusted.
  2. It does not read the network. Every figure is a figure THIS BASE PUBLISHED.
     A contradiction means the base disagrees with itself; it does not say which
     side is right. Resolving that needs a first-hand read.
  3. Same-page contradictions are reported separately and are usually legitimate
     (a correction table quoting the value it supersedes).

MEASURED PRECISION AT p538 -- read this before trusting a row

  All nine rows the first run flagged were triaged by hand against their source
  lines. None was an actionable stale contradiction.

    BENIGN (3)  a real disagreement between passes, deliberately recorded as
                growth: dsvi-b/corretor-enem 6 -> 7, ArnaudGuiovanna/tutor-mcp
                57 -> 59, GarethManning/education-agent-skills 921 -> 926.
                The instrument is right and there is nothing to fix.

    ARTEFACT (6)  mitodl/learn-ai, anchore/syft, bruchris/canvas-lms-mcp,
                Selleo/mentingo, edulinq/autograder-py,
                learning-commons-org/evaluators. ALL SIX SHARE ONE CAUSE:
                this instrument reads a LINE, and the base's prose routinely
                puts a figure and the address it belongs to on DIFFERENT lines,
                because markdown wraps. "(Apache-2.0, **2 109**), [anchore/syft]
                (...)" attributes ORT's figure to syft, and the RENDERED
                sentence is correct -- only the line is not. Selleo/mentingo is
                the variant: one cell quotes four competitors' star counts
                without linking them, so four figures land on the one address
                the cell does name.

    ACTIONABLE (0)  no remaining instance of the Moodle shape -- a figure a
                later pass superseded and an earlier page still renders.

  So the honest reading of a 9-row queue is: the defect class this instrument
  was built for has ONE known instance, p538 fixed it, and the sweep finds no
  second. That is a result, not a blank.

  THE NEXT FIX, pre-registered: join wrapped lines into rendered sentences
  before attributing a figure, and attribute to the NEAREST address rather than
  to the only one on the line. That collapses all six artefacts and is the
  single change that would make this queue safe to act on without hand triage.

Usage:
  python3 -I ingest/crosspage-figure-claims.py
  python3 -I ingest/crosspage-figure-claims.py --tsv OUT.tsv
  python3 -I ingest/crosspage-figure-claims.py --audit ADDRESS
"""
import os
import re
import sys
import collections

ADDR = re.compile(
    r'github\.com/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)'
    r'/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)')

NOT_A_REPO = {
    'orgs', 'topics', 'features', 'about', 'pricing', 'marketplace', 'apps',
    'settings', 'sponsors', 'collections', 'trending', 'explore', 'login',
    'readme', 'site', 'blog', 'security', 'customer-stories',
}

CURATED = [
    'agents/top.md',
    'repos/foundations.md',
    'verticals/solutions.md',
    'compose/patterns.md',
    'intel/market.md',
    'intel/trends.md',
]

# A figure with an explicit star marker. The base writes stars as a bare
# number, as `n*`, or as `n stars`; thousands are grouped with a space or an
# nbsp, never a comma, so the group separator is part of the number.
NUM = r'(\d[\d  ]*\d|\d)'
MARKED = re.compile(NUM + r'\s*(?:★|stars?\b)', re.I)
# A table cell that is nothing but a number, with the base's bold and
# parenthetical decorations stripped off first.
BARE_CELL = re.compile(r'^' + NUM + r'$')

DECOR = re.compile(r'\*\*|~~|`|​')


def to_int(text):
    return int(re.sub(r'[  ]', '', text))


STAR_HEADER = re.compile(r'star', re.I)
SEPARATOR = re.compile(r'^\|[\s:|-]+\|?$')


def cells(line):
    """Table-row cells, or [] for a line that is not a table row."""
    stripped = line.strip()
    if not stripped.startswith('|'):
        return []
    return [c.strip() for c in stripped.strip('|').split('|')]


def star_column(row):
    """Index of the column whose header names stars, or None."""
    for i, cell in enumerate(row):
        if STAR_HEADER.search(DECOR.sub('', cell)):
            return i
    return None


def claims_on_line(line, star_idx):
    """Yield (value, kind) for every star claim the line appears to make.

    star_idx is the Stars column of the table this line belongs to, or None
    when the line is not in a table or the table declares no such column.
    """
    seen = set()
    for m in MARKED.finditer(line):
        v = to_int(m.group(1))
        if v not in seen:
            seen.add(v)
            yield v, 'MARKED'
    if star_idx is None:
        return
    row = cells(line)
    if star_idx >= len(row):
        return
    plain = DECOR.sub('', row[star_idx]).strip()
    # Drop a trailing parenthetical such as "27 (re-measured p538)".
    plain = re.sub(r'\s*\([^)]*\)\s*$', '', plain).strip()
    m = BARE_CELL.match(plain)
    if m:
        v = to_int(m.group(1))
        if v not in seen:
            yield v, 'STARS_COL'


def collect(root):
    """address -> list of (page, lineno, value, kind, line)."""
    found = collections.defaultdict(list)
    coverage = []
    for rel in CURATED:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            print(f'MISSING CURATED PAGE: {rel}', file=sys.stderr)
            continue
        star_idx = None
        tables, tables_with_stars = 0, 0
        with open(path, encoding='utf-8', errors='replace') as fh:
            for lineno, line in enumerate(fh, 1):
                row = cells(line)
                if not row:
                    # A blank or prose line ends the table, so a Stars column
                    # never leaks from one table into the next.
                    star_idx = None
                elif SEPARATOR.match(line.strip()):
                    pass
                elif star_idx is None and not ADDR.search(line):
                    # Candidate header: a table row carrying no address.
                    idx = star_column(row)
                    if idx is not None:
                        star_idx, tables_with_stars = idx, tables_with_stars + 1
                        tables += 1
                    else:
                        tables += 1
                addrs = {
                    f'{o.lower()}/{re.sub(r"[.]git$", "", r_).lower()}'
                    for o, r_ in ADDR.findall(line)
                    if o.lower() not in NOT_A_REPO
                }
                if len(addrs) != 1:
                    # Zero addresses: no claim to attribute. More than one: the
                    # figure cannot be attributed to a single address, so the
                    # line is skipped rather than guessed at.
                    continue
                addr = next(iter(addrs))
                for value, kind in claims_on_line(line, star_idx):
                    found[addr].append((rel, lineno, value, kind, line.rstrip()))
        coverage.append((rel, tables, tables_with_stars))
    return found, coverage


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    found, coverage = collect(root)

    if '--audit' in sys.argv:
        target = sys.argv[sys.argv.index('--audit') + 1].lower()
        rows = found.get(target, [])
        if not rows:
            print(f'no star claim found for {target}')
            return 0
        print(f'{target} — {len(rows)} claim(s)')
        for page, lineno, value, kind, line in rows:
            print(f'  {value:>8}  {kind:<10} {page}:{lineno}')
            print(f'            {line[:160]}')
        return 0

    cross, same = [], []
    for addr, rows in sorted(found.items()):
        by_page = collections.defaultdict(set)
        for page, _l, value, _k, _line in rows:
            by_page[page].add(value)
        pages = sorted(by_page)
        if len(pages) > 1:
            union = set().union(*by_page.values())
            if len(union) > 1:
                lo, hi = min(union), max(union)
                gap = (hi - lo) / hi if hi else 0.0
                cross.append((gap, addr, pages, sorted(union)))
        for page in pages:
            if len(by_page[page]) > 1:
                vals = sorted(by_page[page])
                same.append((addr, page, vals))

    cross.sort(reverse=True)

    out = [('address', 'relative_gap', 'values', 'pages')]
    for gap, addr, pages, values in cross:
        out.append((addr, f'{gap:.3f}',
                    ';'.join(str(v) for v in values), ';'.join(pages)))

    if '--tsv' in sys.argv:
        dest = sys.argv[sys.argv.index('--tsv') + 1]
        with open(dest, 'w', encoding='utf-8') as fh:
            for row in out:
                fh.write('\t'.join(row) + '\n')
        print(f'written: {dest}')

    print(f'curated pages scanned        : {len(CURATED)}')
    print(f'addresses with a star claim  : {len(found)}')
    print(f'CROSS-PAGE contradictions    : {len(cross)}'
          '   <- the Gap 538-C queue')
    print(f'same-page disagreements      : {len(same)}'
          '   (usually a correction table; not a defect by itself)')
    print()
    print('Stars-column coverage per page (tables with a /star/i header):')
    for rel, tables, with_stars in coverage:
        blind = tables - with_stars
        print(f'  {rel:<26} {with_stars}/{tables} tables'
              f'   {blind} table(s) contribute no STARS_COL claim')
    print()
    print('Top cross-page contradictions by relative gap:')
    for gap, addr, pages, values in cross[:20]:
        print(f'  {gap:.3f}  {addr}')
        print(f'         values {values}  pages {pages}')
    print()
    print('PRECISION IS BELOW 1 AND IS NOT ASSERTED. Re-read every row with')
    print('--audit ADDRESS before writing any of it onto a page. At p538 the')
    print('nine flagged rows triaged 3 benign / 6 artefact / 0 actionable --')
    print('see the MEASURED PRECISION block in this file for the breakdown.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
