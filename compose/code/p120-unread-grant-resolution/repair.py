#!/usr/bin/env python3
"""p120 repair. Content-anchored, verified, idempotent.

v1 of this script anchored each repair on a LINE NUMBER, which was correct when
it ran and wrong twenty minutes later: this pass then PREPENDED its findings
sections to the same pages and every anchor moved. A repair script that cannot
be re-run against the tree it repaired is not a repair script, it is a log.

v2 therefore anchors on (page, slug, old-token). A row is identified by the
repository it is about, which does not move, and the repair is applied only
where that row still carries the superseded token. The script refuses to write
unless it matches exactly the expected number of rows, so a page that has
drifted fails loudly instead of silently repairing nothing.
"""
import sys, os, re, pathlib

# P174-KC: the KB root comes from THIS file, never from a clone path. The
# instrument lives at <kb>/compose/code/<instrument>/, so parents[3] is <kb>.
KB = str(pathlib.Path(__file__).resolve().parents[3])
G, R, W = '\U0001F7E2', '\U0001F534', '⚠️'

# (page, slug, old-token, new-token, expected row count)
REPAIRS = [
    # ais-chat: AGPL-3.0 was measured by p117 and published in correction tables
    # on two pages. This row's superseded value was Apache-2.0, not the MIT those
    # corrections looked for, so a repair keyed on the expected wrong value never
    # reached it.
    ('agents/top.md', 'FWU-DE/ais-chat', f'{G} Apache-2.0',
     f'{R} **AGPL-3.0** {W} **was {G} Apache-2.0** — network copyleft', 1),

    # cloud-learning-ce: the root LICENSE is a proprietary Chinese EULA.
    # Commercial use needs a purchased licence; redistributable derivatives are
    # forbidden outright.
    ('verticals/solutions.md', 'yuanjiusheng/cloud-learning-ce', f'{G} MIT',
     f'{R} **proprietary EULA — NOT OSS** {W} **was {G} MIT**', 2),

    # No grant at any of 22 probed paths, and nothing in the repo's own metadata.
    ('agents/top.md', 'lovejzzz/CourseMapper', f'{G} MIT',
     f'{R} **NO GRANT — no licence file on the default branch** {W} **was {G} MIT**', 1),
    ('intel/market.md', 'xgabrielcv/auto-matricula-sigaa-unb', f'{G} MIT',
     f'{R} **NO GRANT — "License: Open Source" badge, no licence file** '
     f'{W} **was {G} MIT**', 1),
    ('intel/market.md', 'Zion-support/curriculum-alignment-checker', f'{G} MIT',
     f'{R} **NO GRANT — no licence file on the default branch** {W} **was {G} MIT**', 1),

    # openbadges-specification carries no grant, and this row tokened it GREEN
    # inside a RECOMMENDATION -- P119-PAT-0's defect, one page over.
    ('compose/patterns.md', '1EdTech/openbadges-specification',
     f'{G} [`1EdTech/openbadges-specification`]',
     f'{R} [`1EdTech/openbadges-specification`]', 1),
]


def is_table_row(t):
    return t.lstrip().startswith('|')


# A row inside a table whose HEADER names a published-vs-measured column pair is
# a NARRATIVE correction row: it quotes the superseded token on purpose, beside
# the measured one. v2 of this script matched three such rows -- all written by
# THIS PASS to describe its own findings -- and "repaired" the quotation,
# producing a doubled marker. They were caught and reverted by hand, which is
# not a safety net.
#
# The guard is the table header, the same signal score.py uses to tell a
# repaired row from a live claim. A repair must never touch a row that is ABOUT
# a repair.
CORRECTION_HDR = re.compile(r'\|\s*(?:was\s+)?published(?:\s+here)?\s*\|', re.I)


def in_correction_table(lines, i, lookback=14):
    for j in range(i, max(-1, i - lookback), -1):
        t = lines[j]
        if CORRECTION_HDR.search(t):
            return True
        if j < i and not is_table_row(t):
            break
    return False


def main():
    dry = '--dry-run' in sys.argv
    fixed = clean = 0
    for page, slug, old, new, want in REPAIRS:
        fp = os.path.join(KB, page)
        lines = open(fp, encoding='utf-8').read().splitlines(keepends=True)
        hit, already = [], 0
        for i, t in enumerate(lines):
            if slug.lower() not in t.lower() or not is_table_row(t):
                continue
            if in_correction_table(lines, i):
                continue
            if new in t:
                already += 1
            elif old in t:
                hit.append(i)
        if already >= want and not hit:
            print(f'skip  {page} [{slug}] already repaired ({already})')
            clean += 1
            continue
        if len(hit) != want:
            print(f'FAIL  {page} [{slug}] expected {want} row(s) carrying {old!r}, '
                  f'found {len(hit)} (already repaired: {already})')
            return 1
        for i in hit:
            lines[i] = lines[i].replace(old, new, 1)
        if not dry:
            open(fp, 'w', encoding='utf-8').write(''.join(lines))
        print(f'{"would fix" if dry else "fixed"} {page} [{slug}] x{len(hit)}')
        fixed += len(hit)
    print(f'\n{fixed} repaired, {clean} already clean')
    return 0


if __name__ == '__main__':
    sys.exit(main())
