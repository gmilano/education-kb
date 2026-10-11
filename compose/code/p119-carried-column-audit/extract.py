#!/usr/bin/env python3
"""p119 ACTION I - extract CARRIED star-count claims from the KB.

Two claim shapes, because p118's P118-PAT-0 showed a column-level repair
cannot reach a token embedded in a recommendation sentence:

  COLUMN  a table row whose header names a star column  -> the cell
  INLINE  "<slug> ... 1 234*" anywhere in a cell         -> the number

Emits TSV: shape, page, line, slug, raw_claim, parsed_int
"""
import re, sys, os

SLUG = re.compile(r'github\.com/([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*?)(?=[)\s/#]|$)')
# a star column header: contains the star glyph or the word stars, and no slug
STAR_HDR = re.compile(r'(\u2605|\bstars?\b)', re.I)
# a cell that is PURELY a star count: optional bold/emoji, digits with space/comma/dot
# separators, optional k suffix, optional star glyph. Nothing else.
PURE = re.compile(r'^(?:[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F\s*_~"]|\&nbsp;)*'
                  r'(~|about\s+)?'
                  r'(\d[\d \u00a0.,]*)\s*(k)?'
                  r'(?:\u2605|\s*stars?)?'
                  r'(?:[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F\s*_~"]|\&nbsp;)*$', re.I)
# inline: a number immediately followed by the star glyph
INLINE = re.compile(r'(~?\d[\d \u00a0.,]*k?)\s*\u2605')

def parse_n(raw):
    """'41 103'->41103  '~12k'->12000  '1.7k'->1700. None if unparseable."""
    m = re.match(r'^~?\s*(\d[\d \u00a0.,]*?)\s*(k)?$', raw.strip(), re.I)
    if not m: return None
    num, k = m.group(1), m.group(2)
    num = num.replace('\u00a0', ' ')
    if k:
        # a k-suffixed figure: dot is a decimal point, space/comma are separators
        num = num.replace(' ', '').replace(',', '')
        try: return int(round(float(num) * 1000))
        except ValueError: return None
    # no k: space and comma are thousands separators. A dot with exactly 3
    # trailing digits is also a separator (de/es style); otherwise decimal.
    num = num.replace(' ', '').replace(',', '')
    if re.match(r'^\d{1,3}(\.\d{3})+$', num): num = num.replace('.', '')
    try: return int(float(num))
    except ValueError: return None

def split_row(line):
    s = line.strip()
    if not s.startswith('|'): return None
    s = s[1:]
    if s.endswith('|'): s = s[:-1]
    return s.split('|')

def is_sep(cells):
    return cells and all(re.match(r'^[\s:\-]+$', c) for c in cells)

def main(paths):
    out = []
    for p in paths:
        hdr = None
        star_cols = []
        with open(p, encoding='utf-8') as fh:
            for ln, line in enumerate(fh, 1):
                cells = split_row(line)
                if cells is None:
                    hdr, star_cols = None, []
                    continue
                if is_sep(cells):
                    continue
                row_has_slug = bool(SLUG.search(line))
                # a header candidate: no slug anywhere, and some cell names stars
                if not row_has_slug and any(STAR_HDR.search(c) for c in cells):
                    hdr = cells
                    star_cols = [i for i, c in enumerate(cells) if STAR_HDR.search(c)]
                    continue
                if not row_has_slug:
                    continue
                slugs = SLUG.findall(line)
                # COLUMN claims: need an unambiguous single slug for the row
                if star_cols and len(set(slugs)) == 1:
                    o, r = slugs[0]
                    for i in star_cols:
                        if i >= len(cells): continue
                        cell = cells[i]
                        if SLUG.search(cell): continue
                        m = PURE.match(cell.strip())
                        if not m: continue
                        raw = (m.group(2) + (m.group(3) or '')).strip()
                        n = parse_n(raw)
                        if n is None: continue
                        out.append(('COLUMN', p, ln, f'{o}/{r}',
                                    cell.strip()[:60], n, hdr[i].strip()[:40] if hdr else ''))
                # INLINE claims: a number+star glyph in the SAME cell as a slug
                for cell in cells:
                    cs = SLUG.findall(cell)
                    if len(set(cs)) != 1: continue
                    o, r = cs[0]
                    for im in INLINE.finditer(cell):
                        n = parse_n(im.group(1))
                        if n is None: continue
                        out.append(('INLINE', p, ln, f'{o}/{r}',
                                    im.group(0).strip()[:60], n, 'inline'))
    seen = set()
    for rec in out:
        key = (rec[0], rec[1], rec[2], rec[3], rec[5])
        if key in seen: continue
        seen.add(key)
        print('\t'.join(str(x) for x in rec))

if __name__ == '__main__':
    main(sys.argv[1:])
