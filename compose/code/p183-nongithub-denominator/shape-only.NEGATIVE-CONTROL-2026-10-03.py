#!/usr/bin/env python3
"""P183 — The denominator of `agents/top.md` rows that carry NO github.com URL.

Pass 65 left an action written over "the 249 rows of agents/top.md WITHOUT a GitHub URL,
which have been outside every license denominator for 14 passes".  Executing it needs the
denominator stated first, and the figure 249 cannot be reproduced: it was never produced by
a versioned instrument.  This is that instrument (rule 1 of P126).

The measurement has two layers, because "a row without a GitHub URL" is NOT one population:

  LAYER 1 — every data row of every markdown table.  A data row is a line starting with '|'
            that follows a header + separator pair.  Lines that merely start with '|' and
            belong to no table (continuation prose, fenced output) are NOT rows.
  LAYER 2 — of those, the ENTITY rows: the ones in a table whose header declares a piece,
            a repo, a package, a license or a star count.  A method table ("Magnitud ·
            Valor", "Estado · n · %") has rows, and those rows are not entities.  Asking a
            license question of them is a category error, and counting them inflates the
            denominator with nothing that can ever be licensed.

Only LAYER 2 rows without a github.com URL are candidates for the payload sweep.  Of those,
the sweep can only reach the ones that NAME a package: the output separates
  PKG-NAMED      a backticked npm/PyPI-shaped name is present -> reachable by registry
  NO-CHANNEL     no package name, no repo URL -> not measurable by ANY channel this KB has

Usage:  python3 denominator.py [path]            # the report
        python3 denominator.py [path] --tsv      # the LAYER-2 rows, TSV
"""
import re, sys

ENTITY_HDR = re.compile(
    r'licen[cs]|\bpieza\b|\brepo\b|\bpaquete\b|\bnombre\b|\bagente\b|\bpuerta\b|'
    r'\bconector\b|\bcorpus\b|\bbiblioteca\b|\bestándar\b|\bestandar\b|\bLMS\b|'
    r'\bcandidat|\bproveedor\b|\bfork\b|\bstars\b|★|\bcommits\b|\btool\b|\bmodelo\b',
    re.I)

# npm: optional @scope/, lowercase, dashes/dots/underscores.  PyPI: same shape.
# Anchored inside backticks so prose words are never harvested (the P171 rule: classify on a
# DECLARATION, never on a word appearing somewhere).
PKG = re.compile(r'`(@[a-z0-9][a-z0-9._-]*/[a-z0-9][a-z0-9._-]*|[a-z][a-z0-9]*(?:[-_][a-z0-9]+){1,4})`')
# Shapes that are backticked but are never package names.
NOT_PKG = re.compile(r'^(get_|set_|add_|list_|delete_|update_|create_|read_|write_|'
                     r'[a-z]+_(records?|table|provider|hint|manually|workflow|grade|'
                     r'submissions?|metadata|userlist|json|yml|yaml|php|py|sh|ttl|owl))')

def tables(lines):
    """Yield (header_lineno, header_text, [(lineno, row_text), ...]) per markdown table."""
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
        if s.startswith('|') and re.fullmatch(r'\|[\s:|-]+\|', nxt):
            j, data = i + 2, []
            while j < len(lines) and lines[j].strip().startswith('|'):
                data.append((j + 1, lines[j].strip()))
                j += 1
            yield i + 1, s, data
            i = j
        else:
            i += 1

def pkg_names(row):
    out = []
    for m in PKG.finditer(row):
        n = m.group(1)
        if NOT_PKG.match(n):
            continue
        out.append(n)
    return sorted(set(out))

def main():
    path = 'agents/top.md'
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if args:
        path = args[0]
    tsv = '--tsv' in sys.argv
    lines = open(path, encoding='utf-8').read().split('\n')

    l1 = l1_nogh = 0
    ent = ent_nogh = 0
    named, nochan = [], []
    for hln, hdr, data in tables(lines):
        is_ent = bool(ENTITY_HDR.search(hdr))
        for ln, row in data:
            l1 += 1
            gh = 'github.com' in row
            if not gh:
                l1_nogh += 1
            if is_ent:
                ent += 1
                if not gh:
                    ent_nogh += 1
                    pk = pkg_names(row)
                    (named if pk else nochan).append((ln, hdr, row, pk))

    if tsv:
        for ln, hdr, row, pk in sorted(named + nochan):
            print('\t'.join([str(ln),
                             'PKG-NAMED' if pk else 'NO-CHANNEL',
                             ','.join(pk) or '-',
                             row[:160].replace('\t', ' ')]))
        return

    print(f'file                                : {path}')
    print(f'LAYER 1  data rows, all tables       : {l1}')
    print(f'LAYER 1  of those, no github.com URL : {l1_nogh}')
    print(f'LAYER 2  rows in ENTITY tables       : {ent}')
    print(f'LAYER 2  of those, no github.com URL : {ent_nogh}   <-- the real denominator')
    print(f'         PKG-NAMED  (registry-reachable) : {len(named)}')
    print(f'         NO-CHANNEL (no package, no repo) : {len(nochan)}')

if __name__ == '__main__':
    main()
