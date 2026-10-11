#!/usr/bin/env python3
"""p120 ACTION J scoring. Joins the grant RESOLVED this pass (verdict.2026-10-11.tsv)
against every licence CLAIM this KB publishes for the same address (p118's
claims.v1.tsv, page + line), and names the disagreement.

The scoring rule is the finding, so it is stated here rather than implied:

  AGREE      - every grant the KB claims for the row is one the resolution found.
  OVERSTATED - the KB claims a PERMISSIVE grant (MIT/Apache/BSD/CC0) that the
               resolution did not find. This is the dangerous direction and is
               scored separately from a merely incomplete row, because a reader
               acts on a permissive token.
  UNGRANTED  - the resolution found NO grant at all, or only an author's claim
               with no licence file behind it, while the KB publishes a licence.
               `P118-K`: absence of a licence reads as permission.
  PHANTOM    - the row never claimed that licence. p118's claim-side alternation
               has no word boundary around `MIT`, so the token matches INSIDE
               `COMMITTED`, and three rows reading "deps COMMITTED" were counted
               as claiming MIT. Small (3 of 461 MIT claims) but it manufactures
               defects out of correct rows, which is the worst direction for an
               instrument to be wrong in.
  UNDERSPEC  - the row names a FAMILY where the tree names a version: bare `GPL`
               against GPL-3.0. p118's F1 was this confusion in the other
               direction, and it is a precision gap, never an error.
  OPEN-ANSWERED - the row does not assert a grant at all; it records that the KB
               could not read one ("unknown - do not assume GPL"). p120 resolves
               it. Scoring an honest open question as a defect would punish the
               one thing this KB most wants to reward.
  INCOMPLETE - the resolution found MORE grants than the row names, none of the
               row's own tokens being wrong.
"""
import csv, sys, re, os

# A row ALREADY REPAIRED by an earlier pass carries both tokens by this KB's
# convention: the measured grant plus the superseded one, marked "was X" or
# placed in a published|measured column pair. p118's extractor keeps both, and
# its verdict layer scores such a row by ANY-match. Scoring it by ALL-match
# reports a repaired row as a live defect, so the repair marker is read from the
# ROW TEXT - the only place the convention is actually recorded.
# A row that ALREADY states the grant is absent. Four rows say "NONE - no
# LICENSE, no COPYING", "No payload / 24" or "UNGRANTED ... must be
# RE-IMPLEMENTED", and name the MIT someone else claimed only to attribute it.
# Those rows are already right, so scoring them as defects would have produced
# a headline four cells too large.
# NOTE: `NO GRANT` is in this alternation because repair.py WRITES that marker.
# The first run of the repair wrote a token this scorer could not read, so the
# repaired row still measured UNGRANTED - an instrument disagreeing with its own
# repair. The marker vocabulary and the repair vocabulary are now the same list.
STATES_ABSENT = re.compile(r'\U0001F534\s*\*\*(NONE|NO GRANT)|\*\*NO GRANT\*\*|\U0001F534\s*\*\*NONE|\bUNGRANTED\b|No payload\s*/|'
                           r'no licence payload|carries no grant|'
                           r'\*\*NONE\*\*\s*\(paper states', re.I)
# A row that declines to assert a grant. Counting it as a wrong claim would
# score honesty as error.
OPEN = re.compile(r'no licence file|unknown\s*[-\u2014]\s*do not assume|'
                  r'almost certainly|no licence payload|do not assume', re.I)
# `MIT` with no word boundary matches inside COMMITTED / submitted / permitted.
PHANTOM_MIT = re.compile(r'\bMIT\b|`MIT`|\*\*MIT|MIT[- ]?[Ll]icen[cs]e')
REPAIRED = re.compile(r'\u26a0\ufe0f?\s*\*\*was\b|\bwas\s+\U0001F7E2|\bwas\s+(MIT|Apache|BSD|GPL|AGPL)', re.I)

# A CORRECTION TABLE states the superseded value in a "published" column and the
# measured one beside it. Such a row is a repair, not a claim - but it carries no
# "was X" marker, so the marker test alone scores three already-corrected rows as
# live defects. The table HEADER is what distinguishes them, so it is read.
# Widened in p120: this pass's own findings tables head their superseded-value
# column `was published here`, `published here` or `published`, and its
# per-region tables head the measured column `measured from the tree` or
# `p120 finding`. A row under any of those headers quotes a token on purpose.
CORRECTION_HDR = re.compile(
    r'\|\s*(?:was\s+)?published(?:\s+here)?\s*\|'
    r'|\|[^|]*\bmeasured (?:this pass|from the tree)\b[^|]*\|'
    r'|\|[^|]*\bp1\d\d finding\b[^|]*\|'
    r'|\|[^|]*\bwhat is actually there\b[^|]*\|'
    r'|\|[^|]*\bthis KB published\b[^|]*\|', re.I)

def in_correction_table(page, line, lookback=14):
    fp = os.path.join('/home/user/education-kb', page)
    try:
        lines = open(fp, encoding='utf-8').read().splitlines()
    except OSError:
        return False
    i = int(line) - 1
    for j in range(i, max(-1, i - lookback), -1):
        t = lines[j] if 0 <= j < len(lines) else ''
        if CORRECTION_HDR.search(t):
            return True
        if j < i and not t.lstrip().startswith('|'):
            break   # left the table before finding a header
    return False

def row_text(page, line):
    fp = os.path.join('/home/user/education-kb', page)
    try:
        with open(fp, encoding='utf-8') as fh:
            for i, t in enumerate(fh, 1):
                if i == int(line):
                    return t
    except OSError:
        pass
    return ''


PERMISSIVE = ('MIT', 'APACHE', 'BSD', 'CC0', 'ISC', 'UNLICENSE')

def norm(tok):
    t = tok.strip().upper().replace('_', '-')
    # "CC BY-NC-SA 4.0" and "CC-BY-NC-SA-4.0" are one token spelled two ways.
    # Normalising only the dashed form is how the first run of this scorer
    # called six AGREEING evaluators rows WRONG - the KB and the resolution
    # said the same thing in different punctuation.
    t = re.sub(r'\s+', '-', t)
    # The source-available family: a bespoke restrictive grant has no SPDX id,
    # so every spelling this KB uses for one maps to a single token. Without
    # this, a row correctly reading "Fair Code License" scores WRONG against a
    # resolution that calls the same file PROPRIETARY.
    if re.match(r'^(FAIR-?CODE|SUSTAINABLE-USE|ELASTIC|BUSL|BUSINESS-SOURCE|SSPL|'
                r'COMMONS-CLAUSE|POLYFORM|PROPRIETARY)', t):
        return 'PROPRIETARY'
    t = re.sub(r'^BSD.*', 'BSD', t)
    t = re.sub(r'^APACHE.*', 'APACHE-2.0', t)
    t = re.sub(r'^GPLV?3.*', 'GPL-3.0', t)
    t = re.sub(r'^GPLV?2.*', 'GPL-2.0', t)
    t = re.sub(r'^CC-?BY-NC.*', 'CC-BY-NC', t)
    t = re.sub(r'^CC-?BY(?!-NC).*', 'CC-BY', t)
    t = re.sub(r'^LGPL.*', 'LGPL-3.0', t)
    return t

def found_tokens(grant):
    """The grant tokens a resolution line actually establishes."""
    if grant.startswith(('NO-GRANT-FOUND', 'AUTHOR-CLAIM')):
        return set()
    if grant.startswith('PROPRIETARY-UNNAMED'):
        return {'PROPRIETARY'}
    body = grant.split(':', 1)[1] if ':' in grant else grant
    toks = re.split(r'[+,]| \+ ', body)
    out = set()
    for t in toks:
        t = t.split('=')[-1]
        t = re.sub(r'\s*\+\s*file\s+LICENSE', '', t, flags=re.I)
        if t.strip():
            out.add(norm(t))
    return {t for t in out if t and t != 'UNKNOWN'}

res = {}
for r in csv.reader(open('verdict.2026-10-11.tsv'), delimiter='\t'):
    if len(r) >= 4:
        res[r[0].lower()] = (r[2], r[3], found_tokens(r[2]))

rows, counts, phantoms = [], {}, []
for r in csv.reader(open('claims.now.tsv'), delimiter='\t'):
    if len(r) < 4:
        continue
    page, line, slug, claim = r[0], r[1], r[2], r[3]
    if slug.lower() not in res:
        continue
    grant, chan, found = res[slug.lower()]
    claimed = {norm(c) for c in claim.split(',') if c.strip()}
    text = row_text(page.replace('../../../', ''), line)
    pg = page.replace('../../../', '')
    repaired = bool(REPAIRED.search(text)) or in_correction_table(pg, line)
    # drop a phantom MIT before any scoring, and record that it was dropped
    if 'MIT' in claimed and not PHANTOM_MIT.search(text):
        claimed.discard('MIT')
        counts['PHANTOM'] = counts.get('PHANTOM', 0) + 1
        phantoms.append((page.replace('../../../', ''), line, slug))
        if not claimed:
            continue
    if STATES_ABSENT.search(text) and not found:
        v = 'ALREADY-CORRECT'
        counts[v] = counts.get(v, 0) + 1
        rows.append((v, pg, line, slug, claim, grant, chan))
        continue
    if OPEN.search(text):
        v = 'OPEN-ANSWERED'
        counts[v] = counts.get(v, 0) + 1
        rows.append((v, page.replace('../../../', ''), line, slug, claim, grant, chan))
        continue
    if not found:
        v = 'UNGRANTED-REPAIRED' if repaired else 'UNGRANTED'
    else:
        extra = claimed - found
        perm_extra = {c for c in extra if c.startswith(PERMISSIVE)}
        if perm_extra:
            v = 'CORRECTED' if repaired else 'OVERSTATED'
        elif extra and all(
                any(f.startswith(e.rstrip('-0123456789.')) for f in found) for e in extra):
            v = 'UNDERSPEC'
        elif extra:
            v = 'WRONG'
        elif found - claimed:
            v = 'INCOMPLETE'
        else:
            v = 'AGREE'
    counts[v] = counts.get(v, 0) + 1
    rows.append((v, page.replace('../../../', ''), line, slug, claim, grant, chan))

with open('score.2026-10-11.tsv', 'w', newline='') as fh:
    w = csv.writer(fh, delimiter='\t')
    for row in sorted(rows):
        w.writerow(row)

with open('phantom-claims.2026-10-11.tsv', 'w', newline='') as fh:
    csv.writer(fh, delimiter='\t').writerows(sorted(phantoms))

order = ['OVERSTATED', 'UNGRANTED', 'WRONG', 'UNDERSPEC', 'INCOMPLETE', 'AGREE',
         'CORRECTED', 'UNGRANTED-REPAIRED', 'OPEN-ANSWERED', 'ALREADY-CORRECT',
         'PHANTOM']
for k in order:
    if k in counts:
        print(f'{k:12} {counts[k]}')
print(f'{"TOTAL":12} {sum(counts.values())} claims over {len(res)} addresses')
