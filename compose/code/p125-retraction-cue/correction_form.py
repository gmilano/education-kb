#!/usr/bin/env python3
"""ACTION AF — the correction marker over ALL EIGHT surface forms.

p124's `ACTION AC` enumerated nine surface forms of this KB's correction
apparatus and reached five of them (1, 2, 3, 9 covered; 4-8 unreached). The
27 outstanding `ACTION AC` violations are every line where a correction
RECORD sits in one of the unreached forms, so a repair-search assertion reads
it as a live stale claim.

p125 covers forms 4-8:

  FORM 4  ``⚠️ *was X*``                 italic, not bold
  FORM 5  ``⚠️ **KB said X**``           a different verb
  FORM 6  ``(New, published Old)``       reversed prose order
  FORM 7  ``as X not Y``                 prose contrast
  FORM 8  ``| 🟢 MIT | 🔴 NO GRANT |``   OLD column, NEW cell has no token

FORM 8 is not a vocabulary problem. p124's pair rule -- a correction must be
an old token AND a differing new token -- is what removed 56 false positives,
and it is also what makes a correction TO NOTHING invisible: "no licence file
at any of 22 probed paths" has no new token to pair with. So the pair rule
gains one admissible non-token NEW value, enumerated and closed:
`NO GRANT`, `NO GRANT FILE`, `NO-FILE`, `UNLICENSED`, `no licence file`.

Offline. Reads only the files named on the command line. No network, clock,
or environment dependence.

usage:
  correction_form.py [--apply] FILE...       mark unmarked correction rows
  correction_form.py --forms FILE...         report the form of each hit
"""
import re
import sys

MARKER = "<!--corrected-->"

# ---------------------------------------------------------------- vocabulary
# One place only. Any token added here is visible to every form.
LICENCE = re.compile(
    r"\b(?:MIT|Apache-2\.0|Apache-2|AGPL-3\.0|LGPL-3\.0|LGPL-2\.1|GPL-3\.0|"
    r"GPL-2\.0|GPL-3|GPL-2|BSD-3-Clause|BSD-2-Clause|BSD-3|MPL-2\.0|EPL-2\.0|"
    r"EUPL-1\.[12]|CC-BY(?:-NC)?(?:-SA|-ND)?-\d(?:\.\d)?|CC0-1\.0|"
    r"Elastic-2\.0|BUSL-1\.1|Unlicense|ISC|MulanPSL-2\.0|ECL-2\.0|"
    r"LGPL|AGPL|GPL)\b")

# p124's token vocabulary, kept EXACTLY alongside the p125 one. The two
# differ by five spellings (`Apache-2`, `GPL-3`, `GPL-2`, `BSD-3`, `ECL-2.0`),
# and a violation count is not comparable across vocabularies -- so the
# baseline uses p124's.
BASE_LICENCE = re.compile(
    r"\b(?:MIT|Apache-2\.0|AGPL-3\.0|LGPL-3\.0|LGPL-2\.1|GPL-3\.0|GPL-2\.0|"
    r"BSD-3-Clause|BSD-2-Clause|MPL-2\.0|EPL-2\.0|EUPL-1\.[12]|"
    r"CC-BY(?:-NC)?(?:-SA|-ND)?-\d(?:\.\d)?|CC0-1\.0|Elastic-2\.0|BUSL-1\.1|"
    r"Unlicense|ISC|MulanPSL-2\.0|LGPL|AGPL|GPL)\b")


def vocab():
    return BASE_LICENCE if BASELINE else LICENCE


# The admissible NON-TOKEN new values -- FORM 8's whole content.
NO_GRANT = re.compile(
    r"\b(?:NO[ -]GRANT(?: FILE)?|NO-FILE|UNLICENSED|"
    r"no lic[es]nce file|without a lic[es]nce)\b", re.I)


def norm_token(tok):
    """`GPL-3` and `GPL-3.0` are the same grant; `Apache-2` and `Apache-2.0`."""
    t = tok.strip()
    t = re.sub(r"^(A?GPL|LGPL|Apache|BSD)-(\d)$", r"\1-\2.0", t)
    if t == "BSD-3.0":
        t = "BSD-3-Clause"
    return t


# ------------------------------------------------------------- marked spans
# FORM 1 (bold) and FORM 4 (italic) differ only in the asterisk count, and
# FORM 5 only in the verb. One pattern, three alternatives -- so a future
# verb is one word, not one more regex.
VERB = r"(?:was|KB said|published|shelf said|page said)"
INLINE_SPAN = re.compile(
    r"⚠️\s*(?:\*\*" + VERB + r"[^*]*\*\*|\*" + VERB + r"[^*]*\*)"
    + re.escape(MARKER))
# A prose span ends at a sentence end, but `.` inside `Apache-2.0` is a
# version separator, not a full stop -- p124's `[^.\n]` made every
# versioned token structurally invisible to prose forms.
_NOT_END = r"(?:[^.\n]|\.(?=\d))"
PROSE_SPAN = re.compile(
    r"\b" + VERB + r"\b" + _NOT_END + r"{0,60}?" + re.escape(MARKER))
# FORM 6 reverses the order: the NEW token leads and the old one follows a
# publication verb inside parentheses.
REVERSED_SPAN = re.compile(
    r"\(" + _NOT_END + r"{0,40}?\b(?:published|was|KB said)\b"
    + _NOT_END + r"{0,40}?\)" + re.escape(MARKER))
# FORM 7: `as X not Y` -- Y is the superseded token.
ASNOT_SPAN = re.compile(
    r"\bas\b" + _NOT_END + r"{0,30}?\bnot\b" + _NOT_END + r"{0,30}?"
    + re.escape(MARKER))

SPAN_FORMS = (("1/4/5", INLINE_SPAN), ("3", PROSE_SPAN),
              ("6", REVERSED_SPAN), ("7", ASNOT_SPAN))

# p124's recognizer, kept EXACTLY, so p125 can reproduce p124's 27-violation
# baseline with one module rather than by trusting a number off a page. It
# sees only bold `⚠️ **was X**` and prose `was X`, and its prose window stops
# at the dot inside `Apache-2.0`.
BASE_INLINE = re.compile(r"⚠️ \*\*was [^*]*\*\*" + re.escape(MARKER))
BASE_PROSE = re.compile(r"\bwas\b(?:[^.\n]|\.(?=\d)){0,60}?"
                        + re.escape(MARKER))
BASE_FORMS = (("1", BASE_INLINE), ("3", BASE_PROSE))

# Set by `--baseline`. Module-level because `in_marked` is called from
# repair_search with no plumbing for it, and the two modes are never mixed
# within one run.
BASELINE = False


def marked_regions(line):
    """Character ranges in which a superseded token is a RECORD, not a claim.

    The region must be the NARROWEST available: a FORM-1 cell holds the old
    AND the new value, so a cell-wide region harvests the repaired, correct
    token as a stale one. An inline or prose span therefore always wins
    inside its own cell, and the cell-wide region is used only for a cell
    carrying the marker with no span inside it (FORM 2 and FORM 8, where the
    cell holds the old value alone).
    """
    spans = []
    for _, pat in (BASE_FORMS if BASELINE else SPAN_FORMS):
        spans += [(m.start(), m.end()) for m in pat.finditer(line)]
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


# ------------------------------------------------------- header recognition
# A correction table is recognised by its HEADER, because only the column
# tells a correction record apart from a claim. Carried from p124 with its
# two hard-won rules: a table may carry MORE THAN ONE old column, and the
# word is `actually`, not `actual`.
HDR_OLD = re.compile(
    r"\b(?:published|publishe[ds]|this KB (?:said|published)|"
    r"this shelf published|KB said|p\d+ (?:said|published|found)|"
    r"prior|previous(?:ly)?|old|stale|was)\b", re.I)
HDR_NEW = re.compile(
    r"\b(?:actually|really|corrected|the file says|the file reads|"
    r"reads|measured|verdict|now|repaired|truth|p\d+ reads)\b", re.I)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def classify_header(line):
    """-> (old_col_indexes, new_col_index) or None."""
    if not line.lstrip().startswith("|"):
        return None
    cells = split_row(line)
    if len(cells) < 2:
        return None
    old = [i for i, c in enumerate(cells) if HDR_OLD.search(c)]
    new = [i for i, c in enumerate(cells) if HDR_NEW.search(c)]
    # An old column must be LEFT of the new one; a header cell matching both
    # (`previously measured`) counts as old only.
    new = [j for j in new if j not in old]
    if not old or not new:
        return None
    j = max(new)
    old = [i for i in old if i < j]
    return (old, j) if old else None


def _is_quote(line):
    """Prose ABOUT the marker, or a fenced/quoted construction, is not a row."""
    s = line.strip()
    return s.startswith(">") or s.startswith("```")


def table_hits(path):
    """FORM 2 and FORM 8 hits: (lineno, old_col, new_col, old_tok, new_tok)."""
    hits = []
    hdr = None
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    for ln, line in enumerate(lines, 1):
        if not line.lstrip().startswith("|"):
            hdr = None
            continue
        if _is_quote(line):
            continue
        h = classify_header(line)
        if h:
            hdr = h
            continue
        if re.match(r"^\s*\|[\s:|-]+\|\s*$", line):
            continue
        if hdr is None:
            continue
        cells = split_row(line)
        olds, j = hdr
        if j >= len(cells):
            continue
        new_cell = cells[j]
        new_toks = {norm_token(t) for t in LICENCE.findall(new_cell)}
        new_absent = bool(NO_GRANT.search(new_cell))
        for i in olds:
            if i >= len(cells):
                continue
            old_toks = [t for t in LICENCE.findall(cells[i])]
            if not old_toks:
                continue
            if MARKER in cells[i]:
                continue
            superseded = [t for t in old_toks
                          if norm_token(t) not in new_toks]
            if not superseded:
                continue        # an omission corrected, not a token replaced
            if new_toks:
                form = "2"
            elif new_absent:
                form = "8"      # corrected TO NOTHING -- p124's blind spot
            else:
                continue        # no new value at all: not a correction
            hits.append((ln, i, j, ",".join(superseded),
                         ",".join(sorted(new_toks)) or "NO-GRANT", form))
    return hits


# --------------------------------------------------------- prose forms 3-7
PROSE_UNMARKED = (
    ("3", re.compile(r"\bwas\b(?:" + _NOT_END + r"){0,60}?"
                     r"(?P<tok>" + LICENCE.pattern[2:-2] + r")")),
    ("4/5", re.compile(r"⚠️\s*\*{1,2}(?:was|KB said)\s*"
                       r"(?:[^*]*?)(?P<tok>" + LICENCE.pattern[2:-2] + r")")),
    ("6", re.compile(r"\((?:" + _NOT_END + r"){0,40}?"
                     r"\b(?:published|KB said)\b\s*"
                     r"(?P<tok>" + LICENCE.pattern[2:-2] + r")")),
    ("7", re.compile(r"\bas\b\s*\**(?:" + LICENCE.pattern[2:-2] + r")\**"
                     r"\s*\**not\**\s*"
                     r"(?P<tok>" + LICENCE.pattern[2:-2] + r")")),
)
# A relative pronoun, not a copula: "the token that WAS invisible". p124
# measured 56 of 88 first-run hits as exactly this.
REL_PRONOUN = re.compile(r"\b(?:that|which|where|when|who|it|this)\s+was\b",
                         re.I)


def prose_hits(path):
    """(lineno, form, superseded token) for unmarked prose retractions."""
    hits = []
    with open(path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            if MARKER in line or _is_quote(line):
                continue
            if line.lstrip().startswith("|"):
                continue
            for form, pat in PROSE_UNMARKED:
                for m in pat.finditer(line):
                    if form == "3" and REL_PRONOUN.search(
                            line[max(0, m.start() - 24):m.start() + 4]):
                        continue
                    hits.append((ln, form, m.group("tok")))
                    break
    return hits


def apply_marks(path, dry=True):
    """Append the marker to every unmarked correction row. Idempotent."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    tbl = {ln: (i, form) for ln, i, _j, _o, _n, form in table_hits(path)}
    pro = {}
    for ln, form, tok in prose_hits(path):
        pro.setdefault(ln, (form, tok))
    changed = 0
    for ln in sorted(set(tbl) | set(pro)):
        line = lines[ln - 1]
        if MARKER in line:
            continue
        if ln in tbl:
            i, _form = tbl[ln]
            cells = line.rstrip("\n").split("|")
            # split("|") on a pipe table yields a leading "" cell, so the
            # logical column i is physical cell i+1.
            k = i + 1
            if k >= len(cells):
                continue
            cells[k] = cells[k].rstrip() + MARKER + " "
            lines[ln - 1] = "|".join(cells) + "\n"
        else:
            form, tok = pro[ln]
            idx = line.find(tok)
            if idx < 0:
                continue
            cut = idx + len(tok)
            lines[ln - 1] = line[:cut] + MARKER + line[cut:]
        changed += 1
    if not dry and changed:
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(lines)
    return changed


def main(argv):
    apply_ = "--apply" in argv
    forms = "--forms" in argv
    paths = [a for a in argv if not a.startswith("-")]
    total = 0
    for p in paths:
        if forms:
            for ln, i, j, old, new, form in table_hits(p):
                print("FORM%s\t%s:%d\tcol%d->col%d\t%s -> %s"
                      % (form, p, ln, i, j, old, new))
            for ln, form, tok in prose_hits(p):
                print("FORM%s\t%s:%d\tprose\t%s" % (form, p, ln, tok))
            continue
        n = apply_marks(p, dry=not apply_)
        total += n
        print("%-26s %d" % (p, n))
    print("TOTAL\t%d" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
