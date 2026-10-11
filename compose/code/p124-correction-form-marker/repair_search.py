#!/usr/bin/env python3
"""ACTION AC — a repair must be a SEARCH, not an edit.

Offline: reads only the files named. No network, no clock.

WHY. p123 repaired [`xiaochong0302/course-tencent-cloud`](https://github.com/xiaochong0302/course-tencent-cloud)
from `MIT` to `GPL-2.0` and found that p121 had *already* repaired the same
address two passes earlier — and that two cells on the very page announcing
p121's repair still read `MIT`, one of them carrying the load-bearing
sentence *"the only permissive full MOOC platform on the shelf"*. A studio
reading that line picks GPL-2.0 code believing it is its one permissive
option.

The defect is not carelessness. It is that a repair was treated as an EDIT to
the row where the error was noticed, while the error lives in every place the
KB mentions that address. So the repair has to end with an assertion over the
whole corpus:

    for every repaired (address, old token):
        no page may carry that token on a line naming that address,
        unless the token sits inside a MARKED span.

A marked span is the correction record itself — `⚠️ **was X**<!--corrected-->`
(FORM 1), or a table cell carrying the marker (FORM 2/3, added by
`correction_form.py` this pass). Inside a marked span the old token is the
KB's own history and must stay. Outside one it is a live false claim.

usage: repair_search.py FILE...
exit 1 if any violation is found.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from correction_form import norm_token  # noqa: E402

MARKER = "<!--corrected-->"

INLINE_SPAN = re.compile(r"⚠️ \*\*was [^*]*\*\*" + re.escape(MARKER))
# FORM-3's marker sits at the end of a prose `was <licence>` span rather than
# inside a `⚠️ **…**` span, so it needs its own region pattern or every row
# p124 marked in prose reads back as an unmarked stale token.
PROSE_SPAN = re.compile(r"\bwas\b(?:[^.\n]|\.(?=\d)){0,60}?" + re.escape(MARKER))
ADDR = re.compile(r"github\.com/([A-Za-z0-9][\w.-]*/[A-Za-z0-9][\w.-]*)")
LICENCE = re.compile(
    r"\b(?:MIT|Apache-2\.0|AGPL-3\.0|LGPL-3\.0|LGPL-2\.1|GPL-3\.0|GPL-2\.0|"
    r"BSD-3-Clause|BSD-2-Clause|MPL-2\.0|EPL-2\.0|EUPL-1\.[12]|"
    r"CC-BY(?:-NC)?(?:-SA|-ND)?-\d(?:\.\d)?|CC0-1\.0|Elastic-2\.0|BUSL-1\.1|"
    r"Unlicense|ISC|MulanPSL-2\.0|LGPL|AGPL|GPL)\b")


def marked_regions(line):
    """Character ranges in which an old token is a RECORD, not a claim.

    🔴 THE REGION MUST BE THE NARROWEST ONE AVAILABLE, and getting this wrong
    inverted the whole instrument on its first run. A FORM-1 cell holds BOTH
    values:

        | 🟢 **Apache-2.0** ⚠️ **was 🔴 GPL-3.0**<!--corrected--> |

    Treating the whole cell as marked harvests `Apache-2.0` — the CORRECT,
    repaired value — as an old token. Every live correct claim about that
    repository then reads as a stale one, and the run reported 100+
    "violations" of which every single one was the KB being right. So: an
    inline span always wins inside its own cell, and the cell-wide region is
    used only for a cell that carries the marker WITHOUT an inline span
    (FORM 2 and FORM 3, where the cell holds the old value alone).
    """
    spans = [(m.start(), m.end()) for m in INLINE_SPAN.finditer(line)]
    spans += [(m.start(), m.end()) for m in PROSE_SPAN.finditer(line)]
    if not (line.lstrip().startswith("|") and MARKER in line):
        return spans
    out = list(spans)
    pos = 0
    for cell in line.split("|"):
        start, end = pos, pos + len(cell) + 1
        if MARKER in cell and not any(start <= a < end for a, _ in spans):
            out.append((start, end))
        pos = end
    return out


def in_marked(line, at, regions=None):
    regions = marked_regions(line) if regions is None else regions
    return any(a <= at < b for a, b in regions)


def repaired_pairs(paths):
    """(address, old token) for every repair this corpus records.

    The address is taken from the SAME LINE as the marked span: a correction
    row names the repository it corrects. A marked span on a line with no
    address contributes nothing, which is correct — there is no address to
    search for.
    """
    pairs = {}
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                if MARKER not in line:
                    continue
                addrs = {a.lower() for a in ADDR.findall(line)}
                if not addrs:
                    continue
                regions = marked_regions(line)
                inside, outside = set(), set()
                for m in LICENCE.finditer(line):
                    (inside if in_marked(line, m.start(), regions)
                     else outside).add(m.group(0))
                # 🔴 A token that is ALSO the live value was never superseded.
                # `| PrairieLearn | 🔴 AGPL-3.0, GPL | 🔴 AGPL-3.0 (CE) + MIT
                # + proprietary ee/ |` corrects an OMISSION: AGPL-3.0 is right
                # in both cells and only MIT was missing. Harvesting AGPL-3.0
                # as an old token makes every correct AGPL-3.0 row in the KB
                # a violation -- 7 of the first run's were exactly this.
                live = {norm_token(t) for t in outside}
                for tok in inside:
                    if norm_token(tok) in live:
                        continue
                    for addr in addrs:
                        pairs.setdefault((addr, tok), []).append(
                            "%s:%d" % (path, ln))
    return pairs


def violations(paths, pairs):
    """Lines that carry a repaired address's OLD token outside a marked span."""
    out = []
    by_addr = {}
    for (addr, tok) in pairs:
        by_addr.setdefault(addr, set()).add(tok)

    for path in paths:
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                addrs = {a.lower() for a in ADDR.findall(line)}
                if not addrs:
                    continue
                regions = marked_regions(line)
                for addr in addrs:
                    for tok in by_addr.get(addr, ()):
                        for m in re.finditer(
                                r"\b" + re.escape(tok) + r"\b", line):
                            if not in_marked(line, m.start(), regions):
                                out.append((path, ln, addr, tok,
                                            line.strip()[:160]))
                                break
    return out


def main(argv):
    paths = [a for a in argv if not a.startswith("-")]
    pairs = repaired_pairs(paths)
    vs = violations(paths, pairs)
    addrs = {a for a, _ in pairs}
    print("# repaired pairs=%d over %d addresses" % (len(pairs), len(addrs)))
    for path, ln, addr, tok, txt in vs:
        print("VIOLATION\t%s:%d\t%s\tstale `%s`\n          %s"
              % (path, ln, addr, tok, txt))
    print("# violations=%d over %d addresses"
          % (len(vs), len({v[2] for v in vs})), file=sys.stderr)
    return 1 if vs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
