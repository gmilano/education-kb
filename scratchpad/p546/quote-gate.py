#!/usr/bin/env python3
"""p546 quote gate — Gap 545-A.

A curated row may attribute a quoted phrase to a named GitHub artefact. p545
found one row (maiatechdev/avit) quoting "janela pedagogica", a phrase that does
not occur in the artefact's README, and noted that no re-reading of the base can
catch it: the string really is present, one page over, as this base's own gloss.

The gate therefore matches each quote against the PAYLOAD, not against the base.

Stage 1 (this file, --parse): extract (row, slug, quote) triples from a curated
markdown page's tables. Stage 2 (--probe) resolves each slug's default branch and
fetches its README; stage 3 (--match) normalises and greps.
"""
import argparse
import json
import re
import sys
import unicodedata

# A slug reference inside a markdown link: [owner/repo](https://github.com/owner/repo)
SLUG_RE = re.compile(r"\[([A-Za-z0-9._-]+/[A-Za-z0-9._-]+)\]\(https://github\.com/[^)]+\)")

# Quoted spans. Three shapes occur on this base:
#   *"..."*   italicised verbatim quote (the dominant shape)
#   "..."     bare double quote
#   “...”     typographic
QUOTE_RES = [
    re.compile(r'\*"([^"]{12,400})"\*'),
    re.compile(r'\*“([^”]{12,400})”\*'),
    re.compile(r'(?<!\*)"([^"]{12,400})"(?!\*)'),
    re.compile(r'(?<!\*)“([^”]{12,400})”(?!\*)'),
]

# A quote is charged to the ARTEFACT only if the base is not quoting ITSELF.
# The first draft of this gate charged p538's own sentence "the live EMEA gap is
# maturity." to oaknational/oak-open-curriculum-ecosystem and would have failed
# the row. A self-quote is recognisable mechanically: the cell attributes it to a
# pass id, to this base, or to another page of it.
#
# Two defects in this regex's own first draft, recorded rather than quietly
# fixed, because a gate that mis-classifies silently is worse than none:
#   1. it listed "its own README states the thesis" as self-attribution. That
#      phrase marks the OPPOSITE — it is the strongest payload marker on the
#      page — and it dropped beltromatti/get-it's real README quote.
#   2. a bare pass id anywhere in 140 preceding characters counted. The note
#      "(re-measured `p537`)" is a MEASUREMENT note, not a quotation, and it
#      dropped HKUDS/DeepTutor's own tagline.
# A pass id now marks self-attribution only when a quoting verb follows it.
SELF_ATTRIB_RE = re.compile(
    r"(this base|this shelf|this pass|this page|this KB"
    r"|\]\(\.\./|\]\(\./"
    r"|\bp\d{2,4}\b[^|]{0,40}?\b(said|says|concluded|asked|noted|called|put it"
    r"|recorded|stated|wrote)\b)", re.I)

# Shapes that are markup rather than prose, and must not be probed as quotes.
NOT_PROSE_RE = re.compile(r"(^\s*[*#|-]\s|Topics:|\||^\s*`)")

# A quote's column is its field, and its field decides which payload it is
# matched against. The column INDEX cannot carry that: this page holds 31 tables
# with different layouts, and a fixed index map put 16 prose quotes in a "Stars"
# column. The field is read from each table's own HEADER instead.
HEADER_FIELDS = [
    ("licence", re.compile(r"licen[cs]e", re.I)),
    ("region", re.compile(r"region|origin", re.I)),
    ("description", re.compile(r"what it does|description|notes?|summary|finding", re.I)),
    ("stars", re.compile(r"stars?|forks?", re.I)),
    ("address", re.compile(r"repo|address|url|agent|name|platform|project", re.I)),
]


def header_map(cells):
    """col index -> field name, read off a table's own header row."""
    out = {}
    for i, c in enumerate(cells):
        t = c.strip()
        if not t:
            continue
        for name, rx in HEADER_FIELDS:
            if rx.search(t):
                out[i] = name
                break
        else:
            out[i] = "prose"
    return out


def is_payload_quote(quote: str, cell: str) -> tuple[bool, str]:
    """Return (chargeable, reason). Only chargeable quotes reach the network.

    The attribution test is scoped to the 140 characters PRECEDING the quote,
    not to the whole cell. A cell routinely carries both a pass reference and a
    real payload quote ("Promotion owed since `p420`" sits in the same cell as
    corretor-enem's About line), so a cell-wide test discards good quotes.
    """
    if NOT_PROSE_RE.search(quote):
        return False, "not-prose"
    at = cell.find(quote)
    ctx = cell[max(0, at - 140):at] if at >= 0 else cell
    if SELF_ATTRIB_RE.search(ctx):
        return False, "self-attributed"
    return True, "payload"


def norm(s: str) -> str:
    """Fold everything that differs between a README and a quote of it.

    READMEs hard-wrap, so a one-line quote routinely spans a newline in the
    payload; markdown emphasis, typographic punctuation and NBSP all vary.
    Matching without this normalisation produces false FAILs, which on a gate
    whose output is a verdict is worse than no gate at all.
    """
    s = unicodedata.normalize("NFKC", s)
    s = (s.replace("“", '"').replace("”", '"')
          .replace("‘", "'").replace("’", "'")
          .replace("–", "-").replace("—", "-")
          .replace(" ", " ").replace("​", ""))
    # D4: markdown LINK syntax. The base quotes the RENDERED text; the payload
    # carries the source. learning-commons-org/evaluators' LICENSE.md line 1 is
    # "The Evaluator code is licensed under [MIT](https://opensource.org/...)",
    # the row quotes it without the brackets and URL, and matching the raw bytes
    # failed a correct row. Reduce [text](url) to text before anything else.
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<https?://[^>]*>", "", s)
    s = re.sub(r"[*_`]+", "", s)          # markdown emphasis / code ticks
    s = re.sub(r"\s+", " ", s)            # hard wraps -> single spaces
    return s.strip().lower()


def parse_page(path):
    """Yield one record per (table row, slug, quote). Skips separator rows."""
    out = []
    hmap, prev_cells = {}, None
    with open(path, encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.startswith("|"):
                hmap, prev_cells = {}, None     # a table ended
                continue
            cells = line.rstrip("\n").split("|")
            if re.fullmatch(r"\|[\s|:-]+\|?\s*", line):
                # The separator row identifies the line before it as a header.
                if prev_cells:
                    hmap = header_map(prev_cells)
                continue
            prev_cells = cells
            slugs = SLUG_RE.findall(line)
            if not slugs:
                continue
            # The subject of the row is the FIRST slug on it: later slugs are
            # cross-references (corpora, credits, alias partners) and a quote
            # must not be charged to them.
            slug = slugs[0]
            quotes, seen = [], set()
            # Only columns AFTER the address column can carry a description
            # quote; the address column's own link text is not a quote.
            # Route by CELL, not by row. A 200-character context window spans
            # columns on this table and reported "licence AND about AND readme"
            # for most rows, because the Licence column always names the sidebar
            # and the grant file. The column a quote sits in names its field
            # exactly, and that is what decides which payload it is charged to.
            for col, cell in enumerate(cells):
                if col < 3:            # marker, name, address — no prose quotes
                    continue
                for rx in QUOTE_RES:
                    for q in rx.findall(cell):
                        k = norm(q)
                        if len(k) >= 12 and k not in seen:
                            seen.add(k)
                            quotes.append((col, q, cell))
            for col, q, cell in quotes:
                ok, why = is_payload_quote(q, cell)
                out.append({"line": lineno, "slug": slug, "quote": q,
                            "col": col, "field": hmap.get(col, "prose"),
                            "charge": ok, "class": why,
                            "extra_slugs": slugs[1:]})
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("pages", nargs="+")
    ap.add_argument("--out", default="-")
    args = ap.parse_args()
    recs = []
    for p in args.pages:
        for r in parse_page(p):
            r["page"] = p
            recs.append(r)
    fh = sys.stdout if args.out == "-" else open(args.out, "w", encoding="utf-8")
    json.dump(recs, fh, ensure_ascii=False, indent=1)
    if fh is not sys.stdout:
        fh.close()
    slugs = sorted({r["slug"] for r in recs})
    print(f"\n# {len(recs)} quote-claims across {len(slugs)} slugs", file=sys.stderr)
