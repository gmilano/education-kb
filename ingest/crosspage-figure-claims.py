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

p539 — THE PRE-REGISTERED FIX, APPLIED, AND WHAT IT TURNED OUT TO BE

  p538 pre-registered: "join wrapped lines into rendered sentences before
  attributing a figure, and attribute to the NEAREST address rather than to the
  only one on the line." That is now implemented, and reading the six artefacts
  first-hand changed what the fix had to be.

  THE WRAP IS NOT A PARAGRAPH BREAKING IN HALF. It is a figure stranded at the
  START of a line by the address it belongs to sitting at the END of the one
  above. All five wrap artefacts have the same silhouette:

      > (Apache-2.0, **2 109★**), [`anchore/syft`](...)        <- market.md
      > (MIT, **1★**) and stopped. [`mitodl/learn-ai`](...)    <- top.md
        MIT, 308★; [`bruchris/canvas-lms-mcp`](...)            <- patterns.md
      > MIT, 7★), [`edulinq/autograder-py`](...)               <- market.md
        164★, [`evaluators`](...) 87★),                        <- foundations.md

  In every one the figure is a TRAILING FRAGMENT of the previous address's
  clause, and the line's own address is the next item in a list. Attributing
  "the figure on this line" to "the address on this line" is therefore wrong
  in the one direction that matters, and `foundations.md:361` is the case that
  proves nearest-address is the right rule rather than a heuristic: it carries
  164★ and 87★ around ONE address, and only the second belongs to it.

  SO THE UNIT CHANGED FROM A LINE TO A RENDERED UNIT:
    * prose      a BLOCK of consecutive non-table, non-heading lines, joined
                 as markdown renders them -- which puts the previous clause's
                 address back in front of its own figure;
    * table row  the row, which markdown does not wrap.

  AND ONE RULE WAS ADDED THAT THE PRE-REGISTRATION DID NOT ANTICIPATE.
  Nearest-address cannot fix `Selleo/mentingo`, because that artefact has no
  competing address to be nearer to: a single cell quotes four competitors'
  star counts (3 353, 2 430, 1 290, 213) beside Mentingo's own 101, and all
  five land on the only address present. The rule that fixes it is the
  converse of the first and follows from the same principle -- PER ADDRESS PER
  UNIT, KEEP ONLY THE NEAREST FIGURE. A comparison quoted around an address is
  context; the figure adjacent to it is the claim.

  🔴 AND THE PRE-REGISTERED FIX, RUN ALONE, MADE THE QUEUE WORSE: 9 -> 14.

  This is recorded because it is the more useful half of the result. Joining
  blocks does not only re-attribute figures -- it DROPS p538's guard, which was
  "skip any line carrying more than one address". That guard was suppressing
  real claims as well as bad ones, so recall rose, and the new recall arrived
  with two further artefact shapes that a line-based reader could never have
  produced. Both are now rules, and both were found by reading the residue
  rather than by reasoning about it:

  ORDERED PAIR. A unit may name k addresses and then state k figures IN THE
  SAME ORDER, which is how this base writes a two-component seam:

      | [vishalsachdev/canvas-mcp](...) (read) + [bruchris/canvas-lms-mcp](...)
        (write) | 🟢 **MIT** · 308★ / 10★ |

  Nearest-address gives `bruchris` the 308, because 308 is the first figure
  after it. The rendered sentence pairs them BY RANK: 308 is canvas-mcp's and
  10 is canvas-lms-mcp's, and this base's own `top.md` files bruchris at 10.
  So when a unit holds k addresses and exactly k figures and every figure
  follows every address, the pairing is ORDINAL, not nearest.

  RANGE. A figure pair written as a span describes a SET, not a member:

      > institutional 0★–5★ repositories, not products

  `5★` here is the top of a range covering four repositories. Nearest-address
  attributed it to whichever address the block named next. A span is detected
  and both of its endpoints are dropped, because neither is a claim about any
  one address.

  AND THE UNIT IS A SENTENCE, NOT A PARAGRAPH. p538 wrote "rendered sentences"
  and the first cut of this fix joined whole blockquotes instead -- which let a
  figure be attributed to an address twenty lines away. Blocks are joined and
  then SPLIT on sentence boundaries, and an attribution further than
  MAX_ATTRIBUTION_CHARS from its address is refused outright. A figure that far
  from any address is not a claim about it.

  AND TWO MORE RULES WERE NEEDED, BOTH OF THEM DEFECTS THIS PASS INTRODUCED
  INTO ITS OWN READER. They are recorded because the shape generalises: every
  widening of what counts as a number widened what counts as two numbers.

    COMMA. p538 asserted the separator is "a space or an nbsp, never a comma".
    False on this base's own pages -- top.md and market.md write `458,181*`
    while trends.md writes `458 181`. The comma-less pattern matched only the
    trailing `181`, so the READER manufactured a 181-vs-458 181 contradiction
    between two pages that agree.

    AND THE COMMA FIX THEN MANUFACTURED A SECOND ONE. A separator class of
    `[comma nbsp space]*` glues any two nearby numbers: `(BSD-3, 1 370*)`
    parsed as the single value 31370, inventing a contradiction on
    jupyter/nbgrader and the identical shape on ucbds-infra/otter-grader and
    submitty/submitty. A thousands separator joins groups of EXACTLY THREE
    digits, so the pattern now requires that, and `3, 1 370` falls back to two
    numbers of which only one carries a star.

  MEASURED AT p539, same tree, at each state:

      p538, line-based                       9   3 benign, 6 artefact, 0 actionable
      + block join + nearest ONLY           14   <- the pre-registration, alone
      + sentence bound, range, ordinal       7
      + comma                                8
      + blocker anchors, aggregate, cell     6
      + strict thousands separator           3   3 benign, 0 artefact, 0 actionable

  THE THREE SURVIVORS ARE p538's THREE BENIGN ROWS, UNCHANGED: dsvi-b/
  corretor-enem 6->7, ArnaudGuiovanna/tutor-mcp 57->59, GarethManning/
  education-agent-skills 921->926 -- real growth, deliberately recorded between
  passes. So all six artefacts collapsed, every benign row survived, and the
  queue reports no actionable contradiction on this tree.

  🔵 THE GENERALISABLE RESULT, which is worth more than the 3:

    1. THE PRE-REGISTERED FIX WAS NECESSARY AND NOWHERE NEAR SUFFICIENT. Run
       alone it made the queue WORSE (9 -> 14), because joining blocks also
       drops p538's "skip any line with more than one address" guard. That
       guard was suppressing bad attributions AND real claims at once; removing
       it raised recall and exposed four further artefact shapes. A fix
       pre-registered from a hand triage of six rows predicted one of the six
       rules this took.

    2. FOUR OF THE SIX RULES ARE ABOUT WHAT A NUMBER IS NOT -- not a range
       endpoint, not a set total, not a figure across a cell boundary, not a
       digit run glued to its neighbour. Attribution was never the hard part.

    3. ONE RULE WAS A LESSON THIS BASE HAD ALREADY LEARNED AND NOT CARRIED.
       p530 taught the address ledger that a repository is named two ways, URL
       and bare backticked slug. Figure attribution still read one channel, so
       `avit`'s 0* went to the nearest URL -- `portabilis/i-educar`, at 722*.
       An instrument fixed in one place stays broken in every other place that
       shares its assumption, and nothing here looks for that.

  ⚠️ WHAT STILL IS NOT COVERED, so silence is not read as coverage. A block
  that names two addresses and states ONE figure exactly between them is a
  coin toss, and this instrument will pick the nearer by character offset with
  no way to know it is right. None of the six artefacts had that shape and the
  sweep reports no instance of it on the tree, but it is unbounded above and is
  recorded as `Gap 539-C` rather than claimed as solved.

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
# p539: COMMA ADDED. p538 asserted "thousands are grouped with a space or an
# nbsp, never a comma, so the group separator is part of the number". That is
# false on this base's own pages: agents/top.md and intel/market.md both write
# `458,181★` for freeCodeCamp while intel/trends.md writes `458 181`. The
# comma-less pattern matched only the trailing `181`, so the reader
# MANUFACTURED a 181-vs-458181 cross-page contradiction out of two pages that
# AGREE. The separator set is now space, nbsp and comma.
# ...and the comma had to be made STRICT, which is the second defect this one
# line has now produced. A separator class of `[, nbsp space]*` glues any two
# nearby numbers: `(BSD-3, 1 370★)` parsed as the single value 31370 and
# invented a 1 370-vs-31 370 contradiction on jupyter/nbgrader, plus the same
# shape on otter-grader and submitty. A thousands separator joins groups of
# EXACTLY THREE digits, so that is what the pattern now requires; `3, 1 370`
# falls back to two separate numbers, and only `1 370` carries a star marker.
NUM = r'(\d{1,3}(?:[,  ]\d{3})+|\d+)'
MARKED = re.compile(NUM + r'\s*(?:★|stars?\b)', re.I)
# A table cell that is nothing but a number, with the base's bold and
# parenthetical decorations stripped off first.
BARE_CELL = re.compile(r'^' + NUM + r'$')

DECOR = re.compile(r'\*\*|~~|`|​')


def to_int(text):
    return int(re.sub(r'[  ,]', '', text))


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


# p539: THE SECOND ADDRESS CHANNEL, as an attribution BLOCKER.
# p530 measured that this base names a repository two ways -- a github.com URL
# and a bare backticked slug -- and taught the address ledger to count both.
# That lesson was never carried into figure attribution, and it produced a
# cross-page contradiction on `portabilis/i-educar`:
#
#   ... (`corretor-enem` 7*, `avit` 0*, plus the pre-release `tutor-ai-agent`),
#   while its shipped open-source strength remains school management --
#   [`portabilis/i-educar`](https://github.com/portabilis/i-educar) ...
#
# The 0* is `avit`'s. `avit` is backticked, not linked, so a URL-only reader
# cannot see it and hands the 0 to the nearest URL -- which is i-educar, a
# 722* repository. A bare name therefore does not need to RESOLVE to be
# load-bearing: it needs to STOP attribution travelling through it.
BACKTICKED = re.compile(r'`([A-Za-z0-9][A-Za-z0-9._/-]{2,})`')
# Backticked nouns that are not repositories. Over-blocking costs recall;
# under-blocking costs correctness, and the Moodle case is what the latter
# looks like, so this list is deliberately short.
NOT_A_NAME = re.compile(
    r'\.(md|py|sh|json|tsv|txt|yml|yaml|toml|lock|rst|csv)$|^p\d+$|^--')


def addr_spans(text, blockers=True):
    """[(key_or_None, start, end)] for every ANCHOR occurrence, in order.

    key is the match_key for a github.com URL, and None for a bare backticked
    repo name -- an anchor that blocks attribution without claiming it.
    """
    out = []
    for m in ADDR.finditer(text):
        owner, repo = m.group(1), m.group(2)
        if owner.lower() in NOT_A_REPO:
            continue
        key = f'{owner.lower()}/{re.sub(r"[.]git$", "", repo).lower()}'
        out.append((key, m.start(), m.end()))
    if blockers:
        url_spans = [(s_, e_) for _k, s_, e_ in out]
        for m in BACKTICKED.finditer(text):
            name = m.group(1)
            if NOT_A_NAME.search(name) or not re.search(r'[-/_]', name):
                continue
            # A backtick inside a markdown link label is the SAME anchor as the
            # URL beside it, not a second one.
            if any(s_ - 60 <= m.start() <= e_ + 60 for s_, e_ in url_spans):
                continue
            out.append((None, m.start(), m.end()))
    out.sort(key=lambda t: t[1])
    return out


# p539: a figure further than this from any anchor is not a claim about it.
# Set from the widest TRUE attribution observed on the tree (a table row whose
# figure cell sits beyond a long description cell), with headroom.
MAX_ATTRIBUTION_CHARS = 240

# A span of two marked figures -- `0*-5*`, `6* - 7*`. Neither endpoint is a
# claim about a single address; the whole thing describes a set.
RANGE = re.compile(NUM + r'\s*(?:★|stars?\b)\s*[–—-]\s*'
                   + NUM + r'\s*(?:★|stars?\b)', re.I)

# Sentence boundary: a terminator followed by whitespace.
SENT_SPLIT = re.compile(r'(?<=[.!?])\s+')


def sentences(text):
    """Yield (sentence, offset) for each rendered sentence in a joined block.

    p538 pre-registered "rendered sentences" and the first cut of this fix
    joined whole blockquotes instead, which let a figure be attributed to an
    address twenty lines away. The block is the join unit; the SENTENCE is the
    attribution unit.
    """
    pos = 0
    for part in SENT_SPLIT.split(text):
        idx = text.find(part, pos)
        if idx < 0:
            idx = pos
        yield part, idx
        pos = idx + len(part)


def nearest(spans, pos_start, pos_end):
    """The address span nearest to a figure, by edge distance.

    p539: this is the rule the five wrap artefacts needed. A figure stranded at
    the start of a line belongs to the address that ended the line above, and
    once the block is joined that address is simply the nearer one.
    """
    best, best_d = None, None
    for key, s_, e_ in spans:
        if e_ <= pos_start:
            d = pos_start - e_          # address before the figure
        elif s_ >= pos_end:
            d = s_ - pos_end            # address after the figure
        else:
            d = 0                       # overlapping (figure inside the link)
        if best_d is None or d < best_d:
            best, best_d = key, d
    return best, best_d


# A figure introduced as a SET TOTAL is not a claim about any member.
# "There are three permissive autograders totalling 2 337*  ([nbgrader](...), ..."
# handed nbgrader's 1 370 a 2 337 rival out of a sum across three repositories.
AGGREGATE = re.compile(
    r'(?:total(?:ling|s|led)?|combined|sum(?:ming)?|aggregate|across|between'
    r'|altogether)\b[^.]{0,40}$', re.I)


def marked_claims(text, cell_of=None):
    """Yield (match_key, value, distance) for every marked figure in a unit.

    The rules, in the order they fire:
      1. RANGE endpoints dropped -- a span describes a set, not a member.
      2. AGGREGATE figures dropped -- a total is not a member's value.
      3. ORDINAL pairing when a unit names k addresses and states exactly k
         figures, all of them after the last address.
      4. otherwise NEAREST ANCHOR. If that anchor is a bare backticked name it
         is a BLOCKER and the figure is dropped, because the figure belongs to
         a repository this reader cannot resolve -- not to the nearest URL.
      5. inside a table row, an address in the figure's OWN CELL wins over a
         nearer address across a `|` boundary.
      6. per address, only the single nearest surviving figure is kept.
    """
    spans = addr_spans(text)
    if not any(k for k, _s, _e in spans):
        return

    masked = [False] * (len(text) + 1)
    for m in RANGE.finditer(text):
        for i in range(m.start(), m.end()):
            masked[i] = True

    figures = []
    for m in MARKED.finditer(text):
        if masked[m.start()] or AGGREGATE.search(text[:m.start()]):
            continue
        figures.append((to_int(m.group(1)), m.start(), m.end()))
    if not figures:
        return

    keys = []
    for key, _s, _e in spans:
        if key and key not in keys:
            keys.append(key)

    last_addr_end = max(e for _k, _s, e in spans)
    if (len(keys) > 1 and len(figures) == len(keys)
            and all(fs >= last_addr_end for _v, fs, _fe in figures)):
        for key, (value, _fs, _fe) in zip(keys, figures):
            yield key, value, 0
        return

    best_per_addr = {}
    for value, fs, fe in figures:
        pool = spans
        if cell_of is not None:
            same = [t for t in spans if cell_of(t[1]) == cell_of(fs)]
            if any(k for k, _s, _e in same):
                pool = same
        key, dist = nearest(pool, fs, fe)
        if key is None or dist > MAX_ATTRIBUTION_CHARS:
            continue      # no anchor, a BLOCKER anchor, or simply too far
        prev = best_per_addr.get(key)
        if prev is None or dist < prev[1]:
            best_per_addr[key] = (value, dist)
    for key, (value, dist) in best_per_addr.items():
        yield key, value, dist


def cell_indexer(line):
    """A function mapping a character offset to its table-cell number."""
    bounds = [i for i, ch in enumerate(line) if ch == '|']
    if not bounds:
        return None

    def which(pos):
        n = 0
        for b in bounds:
            if b < pos:
                n += 1
            else:
                break
        return n
    return which


def stars_col_claim(line, star_idx):
    """The value in the declared Stars column, or None.

    Unchanged from p538: a header-matched column is a far stronger signal than
    proximity, and it is read per ROW because markdown does not wrap a row.
    """
    if star_idx is None:
        return None
    row = cells(line)
    if star_idx >= len(row):
        return None
    plain = DECOR.sub('', row[star_idx]).strip()
    plain = re.sub(r'\s*\([^)]*\)\s*$', '', plain).strip()
    m = BARE_CELL.match(plain)
    return to_int(m.group(1)) if m else None


HEADING = re.compile(r'^\s*(#{1,6}\s|---\s*$|===)')


def collect(root):
    """address -> list of (page, lineno, value, kind, line).

    p539: the scan walks RENDERED UNITS, not lines. A run of consecutive
    non-table, non-heading, non-blank lines is one prose block and is joined
    with single spaces before any figure is attributed, because that is how
    markdown renders it and the five wrap artefacts were all created by reading
    the halves separately.
    """
    found = collections.defaultdict(list)
    coverage = []
    for rel in CURATED:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            print(f'MISSING CURATED PAGE: {rel}', file=sys.stderr)
            continue
        with open(path, encoding='utf-8', errors='replace') as fh:
            lines = fh.readlines()

        star_idx = None
        tables, tables_with_stars = 0, 0
        block, block_start = [], None

        def flush():
            """Attribute every claim in the pending prose block."""
            if not block:
                return
            text = ' '.join(l.strip().lstrip('> ').strip()
                             for l in block)
            for sent, _off in sentences(text):
                for key, value, _d in marked_claims(sent):
                    found[key].append((rel, block_start, value, 'MARKED',
                                       sent[:200]))

        for lineno, raw in enumerate(lines, 1):
            line = raw.rstrip('\n')
            row = cells(line)

            if row:
                flush()
                block, block_start = [], None
                if SEPARATOR.match(line.strip()):
                    continue
                if star_idx is None and not ADDR.search(line):
                    idx = star_column(row)
                    tables += 1
                    if idx is not None:
                        star_idx, tables_with_stars = idx, tables_with_stars + 1
                    continue
                # A row is its own rendered unit.
                for key, value, _d in marked_claims(
                        line, cell_of=cell_indexer(line)):
                    found[key].append((rel, lineno, value, 'MARKED', line))
                v = stars_col_claim(line, star_idx)
                if v is not None:
                    addrs = [t for t in addr_spans(line, blockers=False)
                             if t[0]]
                    if len(set(k for k, _s, _e in addrs)) == 1:
                        found[addrs[0][0]].append(
                            (rel, lineno, v, 'STARS_COL', line))
                continue

            # Not a table row: the table (and its Stars column) has ended.
            star_idx = None
            if not line.strip() or HEADING.match(line):
                flush()
                block, block_start = [], None
                continue
            if block_start is None:
                block_start = lineno
            block.append(line)

        flush()
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
    print('--audit ADDRESS before writing any of it onto a page. At p539, after')
    print('six attribution rules, the queue is 3 rows and all three are real')
    print('growth recorded between passes -- 0 artefact, 0 actionable. The')
    print('p538 run of the same tree was 9 rows, 6 of them artefacts. See the')
    print('MEASURED blocks in this file before trusting or distrusting a row.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
