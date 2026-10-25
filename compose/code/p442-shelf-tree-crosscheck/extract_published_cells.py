#!/usr/bin/env python3
"""p442 — pull every PUBLISHED payload cell off this base's three sell shelves.

A shelf cell on this base reads `<path>` <bytes> B · `<sha256-12>` and, in a neighbouring
cell, the HEAD the row was read at.  Those are the numbers a reader trusts, so they are the
numbers this pass re-measures.  This script only PARSES; measuring is `sweep_published.sh`,
which sources `lib/payload_measure.sh` (`P834`: bytes come from the file, never a capture).

TSV out: file, line, slug, path, bytes, sha12, head
"""
import re, sys

# `1 531 B` — the shelves use NARROW NO-BREAK SPACE and THIN SPACE as the group separator,
# so the digit run is matched permissively and stripped to digits afterwards.
# `LICENSE` 1 531 B · `57c341d09920`, and the same cell with Markdown emphasis anywhere in it
# (`**35 149 B**`, `*1 064 B*`) — 🔴 a second defect this pass's own gate surfaced on this pass's
# own prose: v1 allowed only whitespace between the path and the digits, so every BOLDED byte
# count on these shelves was invisible to it, and the digest of such a cell was then mistaken
# for a commit.  The shelves bold a figure whenever it is the point of the sentence, which is
# exactly when it matters most that it reproduces.
EMPH = r'[*_\s]*'
PAYLOAD = re.compile(r'`([A-Za-z0-9._/-]+)`' + EMPH + r'([\d   , ]+?)' + EMPH +
                     r'B' + EMPH + r'\u00b7' + EMPH + r'`([0-9a-f]{12})`')
HEX12 = re.compile(r'`([0-9a-f]{12})`')
DIGEST_AFTER_BYTES = re.compile(r'B' + EMPH + r'\u00b7' + EMPH + r'`([0-9a-f]{12})`')
SLUG = re.compile(r'github\.com/([A-Za-z0-9._-]+/[A-Za-z0-9._-]+?)(?:[)\s#]|$)')


def rows(path):
    for ln, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 3:
            continue
        s = SLUG.search(cells[0])
        if not s:
            continue
        # 🔴 Found by this pass's own gate, on this pass's own prose.  v1 took the FIRST
        # payload cell in the row and then called any OTHER 12-hex token the commit — so a
        # row publishing TWO payloads (`p442`'s Chamilo row: the 35 147 B grant and the
        # 1 614 B pointer beside it) handed the sweep a PAYLOAD DIGEST as a ref and the
        # fetch 404'd.  🟢 Both halves are fixed by reading the row as a whole: every
        # payload cell in it is a published cell, and a HEAD candidate is a 12-hex token
        # that is not one of their digests.
        hits = [m for c in cells[1:] for m in PAYLOAD.finditer(c)]
        if not hits:
            continue
        # 🔴 Third defect the gate surfaced, and the subtlest: a DIGEST can sit in a cell
        # with no path in it — `| MIT · 1 071 B · \`22e7ab2dbddc\` |`, where the path lives in
        # the column HEADER — so excluding only the digests of matched payload cells left
        # such a digest looking like a commit, and the sweep then fetched at a tree-ish that
        # does not exist.  🟢 A digest is anything that follows `B ·`, path or no path.
        digests = {m.group(3) for m in hits} | set(DIGEST_AFTER_BYTES.findall(line))
        head = '-'
        for h in HEX12.findall(line):
            if h not in digests:
                head = h
                break
        for hit in hits:
            yield (path, ln, s.group(1), hit.group(1),
                   re.sub(r'\D', '', hit.group(2)), hit.group(3), head)


def main():
    print("file\tline\tslug\tpath\tbytes\tsha12\thead")
    n = 0
    for f in sys.argv[1:]:
        for r in rows(f):
            print("\t".join(map(str, r)))
            n += 1
    if not n:
        sys.stderr.write("🔴 p442: empty denominator — a parse fault, not an empty shelf (P355)\n")
        return 2
    sys.stderr.write("p442: %d published payload cells\n" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
