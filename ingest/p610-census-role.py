#!/usr/bin/env python3
"""p610 — answers 609-A-open: does a substring census distinguish a published
shelf row from a published refusal?

Attributes every GitHub address mention on a sell shelf to the ROLE of the table
that encloses it, read from that table's HEADER. p609's detector read markers on
the mention's own line and measured poor precision; shelved rows carry red cells
too, so the line is not the discriminator -- the governing header is.

Also applies 609-M's SHAPE rejector inline, so 607-C's non-repository class
(ratios like `10/10`, this base's own file paths) cannot enter the census.

Usage: p610-census-role.py FILE...   -> TSV: file, line, slug, role, header
"""
import re, sys

SLUG = re.compile(r'github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)')
BARE = re.compile(r'`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`')
SEP  = re.compile(r'^\|[\s:|-]+\|\s*$')

# --- 609-M SHAPE stage, inlined (offline, free) -------------------------------
BASE_DIRS = re.compile(r'^(evidence|ingest|agents|repos|intel|verticals|compose|archive|'
                       r'scratchpad|docs|raw|assets|figures|scripts|tools|configs|'
                       r'examples|data|code|results)$', re.I)
NOT_OWNER = re.compile(r'^(main|master|develop|blob|tree|topics|orgs|sponsors|settings|'
                       r'features|about|pricing|login|join|search|trending|collections|'
                       r'events|marketplace|apps|users|new|notifications|explore|readme|'
                       r'license)$', re.I)
NOT_REPO  = re.compile(r'^(license|licence|license\.md|license\.txt|readme|readme\.md|'
                       r'copying|main|master|head)$', re.I)
OWNER_OK  = re.compile(r'^[A-Za-z0-9][A-Za-z0-9-]{0,38}$')
REPO_OK   = re.compile(r'^[A-Za-z0-9._-]{1,100}$')

def shape_ok(slug):
    if slug.count('/') != 1: return False
    own, rep = slug.split('/')
    if BASE_DIRS.match(own) or NOT_OWNER.match(own): return False
    if NOT_REPO.match(rep): return False
    if not OWNER_OK.match(own) or not REPO_OK.match(rep): return False
    if own.isdigit() and rep.isdigit(): return False   # ratios: 10/10, 4/4
    return True

# --- role vocabulary ----------------------------------------------------------
REFUSE = ('not promoted','not shelved','rejected','disqualified','refused','excluded',
          'reason','not taken','why not')
ADDR   = ('repo','repos','platform','agent','layer','component','name','tier','project',
          'address','engine','tool','framework','library','solution','suite',
          'platform / component','repo / org','harness','connector')
ATTR   = ('licence','license','grant','★','stars','star','region','last push','pushed',
          'size','what it','description','licencia','seam','does')

def norm(c):
    return re.sub(r'\*\*|`|🟢|🔴|🟡|🔵|🆕|\*', '', c).strip().lower()

def header_role(cells):
    if not cells: return 'METRIC'
    cs = [norm(c) for c in cells]
    if any(any(k in c for k in REFUSE) for c in cs): return 'REFUSAL'
    first_is_addr = any(cs[0] == a or cs[0].startswith(a) for a in ADDR)
    has_addr = any(c == a for c in cs for a in ADDR)
    has_attr = any(any(k in c for k in ATTR) for c in cs[1:])
    if (first_is_addr or has_addr) and has_attr: return 'SELL'
    return 'METRIC'

def scan(path):
    out = []
    lines = open(path, encoding='utf-8', errors='replace').readlines()
    role, hdr = 'PROSE', ''
    prev = None
    for i, ln in enumerate(lines, 1):
        tbl = ln.lstrip().startswith('|')
        if tbl and SEP.match(ln.strip()):
            if prev is not None:
                role = header_role(prev[0]); hdr = prev[1].strip()[:120]
            continue
        if not tbl:
            if ln.strip() == '': role, hdr = 'PROSE', ''
            prev = None
            cur = 'PROSE'
        else:
            cells = ln.strip().strip('|').split('|')
            prev = (cells, ln)
            cur = role if role in ('SELL','REFUSAL','METRIC') else 'METRIC'
        seen = set()
        for m in SLUG.finditer(ln):
            s = f'{m.group(1)}/{m.group(2)}'.rstrip('.,);').lower()
            if s in seen or not shape_ok(s): continue
            seen.add(s); out.append((path, i, s, cur, hdr))
        for m in BARE.finditer(ln):
            s = m.group(1).rstrip('.,);').lower()
            if s in seen or not shape_ok(s): continue
            seen.add(s); out.append((path, i, s, cur, hdr))
    return out

if __name__ == '__main__':
    print('file\tline\tslug\trole\theader')
    for p in sys.argv[1:]:
        for r in scan(p):
            print('\t'.join(str(x) for x in r))
