#!/usr/bin/env python3
"""ACTION AJ -- bind a licence token to an ADDRESS, not to a line.

p125's assertion pairs a token with an address by CO-OCCURRENCE: `violations`
takes every address on the line and every superseded token of that address,
and reports a hit if the token appears unmarked anywhere on that line. A row
reading

    | `moodle` GPL-3.0 | `canvas-lms` AGPL-3.0 |

therefore charges `moodle` with AGPL-3.0 and `canvas-lms` with GPL-3.0.

The binding rule, in two parts:

  * A SHORT NAME beats everything. `**MIT** (`pyBKT`) + **BSD-3-Clause**
    (`catsim`)` names its own binding, and a backticked identifier within a
    short window of the token that matches an address's owner or repository
    name binds the token to THAT address. This rule exists because the row it
    was built for is the one p125 called the defect worth the pass, and both
    the cell rule and the distance rule get it wrong.
  * Otherwise, ORDINAL PAIRING. `| `moodle` *or* `canvas-lms` | GPL-3.0 /
    **AGPL-3.0** |` lists k addresses in one cell and k tokens in another, and
    the reader pairs them by position. Where the counts agree and k > 1, the
    i-th token binds to the i-th address.
  * Otherwise, in a TABLE ROW the cell is a wall. A token binds only to
    addresses in its own cell; if its own cell names none, it binds to the
    row's SUBJECT -- the addresses in the leftmost cell that names any.
  * Otherwise, in PROSE, a token binds to the NEAREST address by character
    distance, preceding address winning a tie.

A violation is EXPLAINED BY MIS-BINDING when the old co-occurrence rule paired
(address, token) on a line where the binding rule does not.

Offline. usage: binding.py PAGE...
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "p125-retraction-cue"))
import correction_form                                     # noqa: E402
import repair_search                                        # noqa: E402
from correction_form import in_marked, marked_regions, vocab  # noqa: E402

ADDR = repair_search.ADDR


def _clean(a):
    return a.lower().rstrip(".,);")


def cells(line):
    """-> [(start, end)] half-open spans of a markdown row's cells."""
    if not line.lstrip().startswith("|"):
        return []
    out, pos = [], 0
    for cell in line.split("|"):
        out.append((pos, pos + len(cell) + 1))
        pos += len(cell) + 1
    return out


def addresses(line):
    return [(m.start(), _clean(m.group(1))) for m in ADDR.finditer(line)]


NAME = __import__("re").compile(r"`([A-Za-z0-9][\w.-]*)`")
WINDOW = 30


def short_name(line, addrs, start, end):
    """-> address named by a backticked short name beside the token, or None.

    Looks AFTER the token first -- `**MIT** (`pyBKT`)` is the published
    spelling -- then before it. A short name matches an address when it equals
    the repository name or the owner, case-folded.
    """
    index = {}
    for _, a in addrs:
        owner, _, repo = a.partition("/")
        index.setdefault(repo.lower(), a)
        index.setdefault(owner.lower(), a)
    for text, base in ((line[end:end + WINDOW], end),
                       (line[max(0, start - WINDOW):start], None)):
        hits = [m.group(1).lower() for m in NAME.finditer(text)]
        if base is None:
            hits = list(reversed(hits))
        for h in hits:
            if h in index:
                return index[h]
    return None


def _cell_of(spans, at):
    for i, (a, b) in enumerate(spans):
        if a <= at < b:
            return i
    return None


def subject_cell(spans, addrs):
    """The leftmost cell naming any address -- the row's subject."""
    best = None
    for p, _a in addrs:
        c = _cell_of(spans, p)
        if c is not None and (best is None or c < best):
            best = c
    return best


def ordinal(line, spans, addrs, toks):
    """-> {tok_start: address} where k addresses and k tokens pair by order.

    Only fires when the addresses sit in ONE cell, the tokens in ONE other
    cell, the two counts agree, and there is more than one of each.
    """
    if not spans or len(addrs) < 2 or len(toks) != len(addrs):
        return {}
    acells = {_cell_of(spans, p) for p, _ in addrs}
    tcells = {_cell_of(spans, at) for at, _ in toks}
    if len(acells) != 1 or len(tcells) != 1 or acells == tcells:
        return {}
    order = [a for _, a in sorted(addrs)]
    return {at: order[i] for i, (at, _t) in enumerate(sorted(toks))}


def bind(line):
    """-> [(tok_start, token, bound_address or None)] for every token."""
    spans = cells(line)
    addrs = addresses(line)
    toks = [(m.start(), m.group(0)) for m in vocab().finditer(line)]
    ordpair = ordinal(line, spans, addrs, toks)
    out = []
    for m in vocab().finditer(line):
        tok, at = m.group(0), m.start()
        named = short_name(line, addrs, at, m.end()) if addrs else None
        if named:
            out.append((at, tok, named))
            continue
        if at in ordpair:
            out.append((at, tok, ordpair[at]))
            continue
        if spans:
            ci = _cell_of(spans, at)
            same = [(p, a) for p, a in addrs if _cell_of(spans, p) == ci]
            if not same:
                subject = None
                for p, a in addrs:
                    cj = _cell_of(spans, p)
                    if subject is None or cj < subject:
                        subject = cj
                same = [(p, a) for p, a in addrs
                        if _cell_of(spans, p) == subject]
            pool = same
        else:
            pool = addrs
        if not pool:
            out.append((at, tok, None))
            continue
        best = min(pool, key=lambda pa: (abs(pa[0] - at), pa[0] > at))
        out.append((at, tok, best[1]))
    return out


def bound_pairs(line):
    """-> {(address, token)} actually asserted by the line."""
    return {(a, t) for _, t, a in bind(line) if a}


def is_substring_only(line, tok):
    """True when every `\btok\b` hit lies INSIDE a longer vocabulary token.

    p125's `violations` tests `re.escape(tok)` with word boundaries instead of
    the vocabulary, so the family token `GPL` matches inside `GPL-3.0` -- the
    SUBSTRING class `ACTION AG` catalogued for token READING, recurring in the
    violation CHECK that AG never reached.
    """
    hits = list(re.finditer(r"\b" + re.escape(tok) + r"\b", line))
    if not hits:
        return False
    spans = [(m.start(), m.end()) for m in vocab().finditer(line)]
    for h in hits:
        if any(a == h.start() and b == h.end() for a, b in spans):
            return False          # a real token in its own right
    return True


def explains(line, addr, tok):
    """Is (addr, tok) on this line an artefact of co-occurrence?"""
    if is_substring_only(line, tok):
        return True, "SUBSTRING of a longer token; not a token on this line"
    regions = marked_regions(line)
    live = set()
    for at, t, a in bind(line):
        if not in_marked(line, at, regions) and a:
            live.add((a, t))
    if (addr, tok) in live:
        return False, "bound"
    # the token is on the line and unmarked, but bound elsewhere
    others = sorted({a for a, t in live if t == tok})
    if others:
        return True, "bound instead to " + ", ".join(others)
    return True, "token not live on this line under binding"


def relocate(pages):
    """-> {(page, addr, tok): [lineno,...]} from the CURRENT pages."""
    pairs = repair_search.repaired_pairs(pages)
    found = {}
    for path, ln, addr, tok, _ in repair_search.violations(pages, pairs):
        found.setdefault((path, addr, tok), []).append(ln)
    return found


def main(pages):
    """Print every line whose co-occurrence pairs and bound pairs differ."""
    pairs = repair_search.repaired_pairs(pages)
    for path, ln, addr, tok, _ in repair_search.violations(pages, pairs):
        with open(path, encoding="utf-8") as fh:
            line = fh.readlines()[ln - 1]
        mis, why = explains(line, addr, tok)
        print("%s\t%s:%d\t%s\t%s\t%s"
              % ("MISBOUND" if mis else "BOUND", path, ln, addr, tok, why))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
