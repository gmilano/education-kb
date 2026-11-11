#!/usr/bin/env python3
"""p767 / ACTION p766-E. Re-DETECT over-wide markdown rows live and (with --fix)
extend the owning table's header and separator ADDITIVELY so the renderer stops
discarding the extra cell.

Why re-detection and not the p765 ledger: evidence/overwide-rows.2026-11-11-p765.tsv
stores ABSOLUTE LINE NUMBERS into APPEND-ONLY shelves. p766 prepended a dated
section to both trending files, shifting every line. The ledger's coordinates were
stale before either p765-G or p766-E could act on them. Content addressing, not
line addressing.
"""
import sys, re
SEP = re.compile(r'^\|[\s\-:|]+\|$')
def cells(line):
    """p767 defect, reproduced from this base's own record (agents/trending.md:21182,
    'table-width probe counted escaped \\| as separators'): in GFM only an UNESCAPED
    pipe splits a cell. Strip \\| before counting or every row that quotes a markdown
    table in a cell scores over-wide. First run of this detector reported 48 rows;
    34 of them were this defect."""
    s = line.strip().replace('\\|', '\x00')
    if not (s.startswith('|') and s.endswith('|')): return None
    return len(s.split('|')) - 2
def tables(src):
    """yield (hdr_idx, sep_idx, [row_idx...]) for every pipe table"""
    i = 0
    while i < len(src) - 1:
        if cells(src[i]) and SEP.match(src[i+1].strip()) and cells(src[i+1]) == cells(src[i]):
            h, s = i, i+1
            rows, j = [], i+2
            while j < len(src) and cells(src[j]):
                rows.append(j); j += 1
            yield h, s, rows
            i = j
        else:
            i += 1
def main(paths, fix=False, newcol="p276 correction"):
    total = 0
    for p in paths:
        src = open(p, encoding='utf-8').read().split('\n')
        edits = {}
        for h, s, rows in tables(src):
            w = cells(src[h])
            over = [r for r in rows if cells(src[r]) > w]
            if not over: continue
            extra = max(cells(src[r]) for r in over) - w
            total += len(over)
            for r in over:
                print(f"{p}\t{r+1}\t{cells(src[r])}\t{w}\t{src[r].strip()[:70]}")
            if fix:
                edits[h] = src[h].rstrip() + (f" {newcol} |" * extra)
                dash = src[s].strip().strip('|').split('|')[-1]
                edits[s] = src[s].rstrip() + (f"{dash}|" * extra)
        if fix and edits:
            for k, v in edits.items(): src[k] = v
            open(p, 'w', encoding='utf-8').write('\n'.join(src))
            print(f"# {p}: extended {len(edits)//2} table header(s)")
    print(f"# TOTAL over-wide rows: {total}")
    return total
if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x != '--fix']
    main(a, fix='--fix' in sys.argv)
