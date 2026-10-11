#!/usr/bin/env python3
"""P121 ACTION P -- the CROSS-PAGE stale-token sweep.

The clause, verbatim from p120's pre-registration:

  "re-measure every row whose superseded value a prior pass recorded as `was X`,
   checking the OTHER pages for the same address against values that are NOT `X`.
   REFUTED if no second address carries a stale licence token differing from the
   one its own correction table names."

Why the clause is shaped that way. p117 measured `FWU-DE/ais-chat` as AGPL-3.0.
Both `agents/top.md` and `intel/market.md` then published a correction table
naming the superseded value as *"was MIT"*. The actual cell in the top table
said **Apache-2.0** -- a THIRD value. A repair keyed on the value you expect to
find cannot fix a row that is wrong in a different way, so the cell survived
three passes of corrections ~65 lines from its own correction table.

So this instrument does NOT look for "the token named in the correction". It
takes the MEASURED truth and flags every live claim that disagrees with it,
then reports whether the disagreeing token is the one the correction named (a
known-shape miss) or a different one (the ais-chat shape).

Path is a parameter: p120's score.py hardcoded /home/user/education-kb, which
makes it unrunnable from any other checkout.
"""
import os, re, sys, csv
from collections import defaultdict

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
HERE = os.path.dirname(os.path.abspath(__file__))

# --- header guard, p120 vocabulary verbatim -------------------------------
CORRECTION_HDR = re.compile(
    r'\|\s*(?:was\s+)?published(?:\s+here)?\s*\|'
    r'|\|[^|]*\bmeasured (?:this pass|from the tree)\b[^|]*\|'
    r'|\|[^|]*\bp1\d\d finding\b[^|]*\|'
    r'|\|[^|]*\bwhat is actually there\b[^|]*\|'
    r'|\|[^|]*\bthis KB published\b[^|]*\|'
    # p121's own contradiction tables head their columns `manifest says` /
    # `committed file says`. P121-B recurring on this pass's own sections: a
    # census that reads header vocabulary needs every pass's vocabulary added to
    # it, which is a maintenance burden no pass has yet escaped.
    r'|\|[^|]*\bmanifest says\b[^|]*\|'
    r'|\|[^|]*\bcommitted file says\b[^|]*\|', re.I)

_cache = {}
def pagelines(page):
    if page not in _cache:
        try:
            _cache[page] = open(os.path.join(ROOT, page), encoding='utf-8').read().splitlines()
        except OSError:
            _cache[page] = []
    return _cache[page]

# P121-B. The header guard inherited from p120 is NOT sufficient, and this is the
# pass's own-instrument finding. This KB writes most of its corrections INLINE --
# `🔴 **NO GRANT ...** ⚠️ **was 🟢 MIT**` -- in a row under an ORDINARY header.
# A header-only guard scored 6 such rows as defects on the first run: they carry
# the right verdict AND quote the superseded token on purpose, in the same cell.
# The correction vocabulary and the census vocabulary had diverged.
INLINE_MARK = re.compile(r'(?:⚠️\s*)?\*\*was\s|\bwas\s+(?:🟢|🔴|🟡)|\bNO GRANT\b|\bNOT OSS\b'
                         r'|\bno grant\b|\bCite the validator\b'
                         # widened for p121's own rows, which disclose the defect
                         # in prose inside the cell rather than via a header
                         r'|\bno licence file\b|\bauthor claim only\b'
                         r'|\blicence-unresolved\b|\bsays only\b|\bdeclares\b', re.I)

def in_correction_table(page, line, lookback=14):
    lines = pagelines(page); i = int(line) - 1
    if 0 <= i < len(lines) and INLINE_MARK.search(lines[i]):
        return True                      # the ROW itself is a correction
    for j in range(i, max(-1, i - lookback), -1):
        t = lines[j] if 0 <= j < len(lines) else ''
        if CORRECTION_HDR.search(t): return True
        if not t.lstrip().startswith('|'): break
    return False

def row_text(page, line):
    lines = pagelines(page); i = int(line) - 1
    return lines[i] if 0 <= i < len(lines) else ''

# --- normalisation --------------------------------------------------------
def norm(t):
    t = t.strip().upper().replace('_', '-')
    t = {'APACHE-2': 'APACHE-2.0', 'GPL-3': 'GPL-3.0', 'GPL-2': 'GPL-2.0',
         'AGPL-3': 'AGPL-3.0', 'LGPL-3': 'LGPL-3.0', 'BSD-3-CLAUSE': 'BSD-3',
         'BSD-2-CLAUSE': 'BSD-2', 'CC0-1.0': 'CC0'}.get(t, t)
    return t

def family(t):
    """The licence FAMILY a measured verdict belongs to, for agreement testing."""
    t = norm(t)
    for f in ('AGPL-3.0','LGPL-3.0','GPL-3.0','GPL-2.0','APACHE-2.0','MIT',
              '0BSD','BSD-3','BSD-2','ECL-2.0','MPL-2.0','EPL-2.0','CC0',
              'CC-BY-SA','CC-BY-NC','CC-BY','ISC','UNLICENSE'):
        if f in t: return f
    return t

# --- truth table ----------------------------------------------------------
# precedence: p120 verdict (22, refined) > p118 ledger (hand-evidenced) > p118 machine sweep (249)
truth, source = {}, {}
def put(slug, val, src):
    truth[slug.lower()] = val; source[slug.lower()] = src

p118 = os.path.join(HERE, '..', 'p118-licence-column-sweep')
p120 = os.path.join(HERE, '..', 'p120-unread-grant-resolution')

for row in csv.reader(open(os.path.join(p118, 'measured2.2026-10-11.tsv')), delimiter='\t'):
    if len(row) >= 4: put(row[0], row[3], 'p118-sweep')
led = list(csv.reader(open(os.path.join(p118, 'ledger.2026-10-11.tsv')), delimiter='\t'))
corrected_published = {}
for row in led[1:]:
    if len(row) >= 3:
        put(row[0], row[2], 'p118-ledger')
        corrected_published[row[0].lower()] = row[1]
for row in csv.reader(open(os.path.join(p120, 'verdict.2026-10-11.tsv')), delimiter='\t'):
    if len(row) >= 3: put(row[0], row[2], 'p120-verdict')
for row in csv.reader(open(os.path.join(p120, 'defects.2026-10-11.tsv')), delimiter='\t'):
    if len(row) >= 6:
        put(row[3], row[5], 'p120-defect')
        corrected_published.setdefault(row[3].lower(), row[4])

# --- claims ---------------------------------------------------------------
claims = defaultdict(list)
for row in csv.reader(open(os.path.join(HERE, 'claims.v6.tsv')), delimiter='\t'):
    if len(row) < 4: continue
    page, line, slug, toks = row[0], row[1], row[2], row[3]
    claims[slug.lower()].append((page, line, slug, toks.split(',')))

UNGRANTED = ('NO-GRANT', 'AUTHOR-CLAIM', 'NOT-OSS', 'UNGRANTED')
OSI = ('AGPL-3.0','LGPL-3.0','GPL-3.0','GPL-2.0','APACHE-2.0','MIT','0BSD','BSD-3',
       'BSD-2','ECL-2.0','MPL-2.0','EPL-2.0','CC0','ISC','UNLICENSE')
PERMISSIVE = ('MIT','APACHE-2.0','BSD-3','BSD-2','0BSD','ISC','UNLICENSE','CC0')

# Bare GPL/AGPL/LGPL/BSD name a FAMILY without a version. Against a measured
# GPL-3.0 such a token is IMPRECISE, not WRONG, and conflating the two inflates
# a defect count with rows no human got wrong. Own-instrument fault found by
# reading all 30 candidate rows before believing any of them (p120-E's lesson).
BARE = {'GPL': ('GPL-2.0','GPL-3.0'), 'AGPL': ('AGPL-3.0',), 'LGPL': ('LGPL-3.0',),
        'BSD': ('BSD-2','BSD-3','0BSD')}

def families_in(verdict):
    """EVERY licence family a (possibly multi-grant) verdict names."""
    v = norm(verdict)
    found = [f for f in OSI if f in v]
    # "GNU GPL V3" / "GPLV3" spellings used by grant-by-reference licence files
    if not found:
        if re.search(r'GPL\s*V?3', v): found = ['GPL-3.0']
        elif re.search(r'GPL\s*V?2', v): found = ['GPL-2.0']
    return found

def permissive(t):
    return family(t) in PERMISSIVE

# ACTION P's clause scopes the sweep to addresses a PRIOR PASS CORRECTED (35 of
# 249). Pass `all` to widen the same test to every address with a measured
# licence: the defect class does not care whether a pass happened to correct the
# address before, and scoping to corrected addresses is a property of the
# instrument's history, not of the data.
WIDE = len(sys.argv) > 2 and sys.argv[2] == 'all'
domain = dict(corrected_published)
if WIDE:
    for s in truth:
        domain.setdefault(s, '(never corrected)')

out = []
for slug in sorted(domain):
    if slug not in truth: continue
    T = truth[slug]; named = domain[slug]
    fams = families_in(T)
    # A verdict is UNGRANTED only if it names an ungranted shape AND grants nothing.
    # "AGPL-3.0 (CE) + MIT (portions) + proprietary ee/" grants two licences and is
    # NOT ungranted -- treating it so flagged 5 rows that are in fact correct.
    ung = (any(k in T.upper() for k in UNGRANTED) or 'PROPRIETARY' in T.upper()) and not fams
    for page, line, orig, toks in claims.get(slug, []):
        if in_correction_table(page, line): continue      # row is ABOUT a correction
        ntoks = [norm(t) for t in toks]
        # Coarse truth, same fault ACTION Q hit: p118 recorded some committed
        # licences as a BARE FAMILY ("BSD", "CC-BY"). A page naming BSD-3 against
        # a truth of "BSD" is MORE precise, not wrong. Unfixed, this alone
        # produced ~120 of 145 flagged rows in the widened sweep.
        COARSE = {'BSD': ('BSD-2','BSD-3','0BSD','BSD'),
                  'CC-BY': ('CC-BY','CC-BY-SA','CC-BY-NC')}
        tfam = family(T)
        if tfam in COARSE and any(t in COARSE[tfam] for t in ntoks):
            continue
        if ung:
            bad = [t for t in ntoks if permissive(t)]
            if not bad: continue
            shape = 'UNGRANTED-PERMISSIVE'
        else:
            if any(f in ntoks for f in fams): continue        # row names a granted family
            # bare family token that COULD be the measured one -> imprecise, not wrong
            if any(t in BARE and any(f in BARE[t] for f in fams) for t in ntoks):
                out.append(('IMPRECISE', page, line, orig, ','.join(ntoks), T, named, source[slug]))
                continue
            bad = [t for t in ntoks if t not in fams]
            if not bad: continue
            shape = 'NAMED' if norm(named) in bad else 'THIRD-VALUE'
        out.append((shape, page, line, orig, ','.join(ntoks), T, named, source[slug]))

w = csv.writer(open(os.path.join(HERE, 'action-p.tsv'), 'w'), delimiter='\t', lineterminator='\n')
for r in out: w.writerow(r)

print(f"addresses in domain           : {len(domain)}  ({'ALL' if WIDE else 'corrected only'})")
print(f"of those with measured truth  : {sum(1 for s in domain if s in truth)}")
defects = [r for r in out if r[0] != 'IMPRECISE']
print(f"live rows flagged             : {len(out)}")
for s in ('UNGRANTED-PERMISSIVE','THIRD-VALUE','NAMED','IMPRECISE'):
    n = sum(1 for r in out if r[0]==s)
    print(f"  {s:22s} : {n}")
print(f"DEFECT rows (excl. IMPRECISE) : {len(defects)}")
print(f"distinct addresses, defects   : {len({r[3].lower() for r in defects})}")
