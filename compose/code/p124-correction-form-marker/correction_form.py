#!/usr/bin/env python3
"""ACTION AB — the marker must cover all THREE correction forms.

Pure function over text: no network, no clock. Reads only the files named.

WHAT p123 ESTABLISHED, AND WHY IT IS THE CEILING ON THIS WHOLE FAMILY.
p123's census of this KB's licence claims ran at a **95.1 % false-positive
rate**, and the cause was not attribution scope or path coverage. It was
this: in these pages a CORRECTION RECORD and a CLAIM are the same bytes.
When `agents/top.md` says

    | [`fwu-de/ais-chat`](…) | 🟢 MIT | 🔴 **AGPL-3.0** | network-use copyleft |

the `MIT` is not a claim that the repository is MIT. It is a record that this
KB USED to say so. Only the column tells them apart, and no census reads
columns. `ACTION V` solved this for ONE form — the inline `⚠️ **was X**`
span — by having the writer emit an exact marker. This file covers the other
two, which `ACTION V` left as live false positives:

  FORM 1  inline span        `⚠️ **was 🔴 AGPL-3.0**<!--corrected-->`
          -> already covered by ACTION V (p123), 57 spans in place.

  FORM 2  audit-table OLD column
          -> a table with BOTH an "old" column (`published here`, `p111`,
             `claim from the channel`) and a "new" column (`measured from
             the tree this pass`, `payload read`, `the tree`). Every licence
             token in the old column is a correction record.

  FORM 3  unmarked prose "was X"
          -> the same `was <licence>` construction OUTSIDE a table row, in
             running prose, where ACTION V's row-anchored regex never looked.

WHY FORM 2 NEEDS A HEADER PARSER AND NOT A PHRASE LIST. The old/new
distinction in this KB is carried by the HEADER, and the header vocabulary is
generative: a column named after the pass that made the claim (`p109`,
`p110 verdict`, `p111`) is an old column, and the pass number is unbounded.
So the parser classifies a header cell STRUCTURALLY — a pass reference, or a
publication verb, is old; a measurement noun is new — rather than matching
whole headers.

usage: correction_form.py [--apply] FILE...
       default is a dry run; --apply rewrites in place.
"""
import re
import sys

MARKER = "<!--corrected-->"

# A licence token as these pages WRITE one. This is the population at risk:
# a census only false-positives where a licence name appears.
LICENCE = re.compile(
    r"\b(?:MIT|Apache-2\.0|AGPL-3\.0|LGPL-3\.0|LGPL-2\.1|GPL-3\.0|GPL-2\.0|"
    r"BSD-3-Clause|BSD-2-Clause|MPL-2\.0|EPL-2\.0|EPL-1\.0|EUPL-1\.[12]|"
    r"CC-BY(?:-NC)?(?:-SA|-ND)?-\d(?:\.\d)?|CC0-1\.0|Elastic-2\.0|BUSL-1\.1|"
    r"SSPL|Unlicense|ISC|MulanPSL-2\.0|LGPL|AGPL|GPL)\b")

# --- header classification -------------------------------------------------
# 🔴 WHAT THE FIRST BUILD OF THIS FILE GOT WRONG, recorded because it is
# p122's defect recurring in a third form. The first build treated `\bwas\b`
# in a header as evidence of an old-value column and fired on
#
#   | address | token that was invisible | rows on this page |
#   | corpus  | licence, and where it was read | usable commercially? |
#
# In both, `was` is a RELATIVE PRONOUN inside an ordinary noun phrase and the
# column holds a LIVE claim. Marking those cells would have told every future
# census to ignore two live licence claims — strictly worse than the false
# positives the marker exists to remove. `was` is therefore not consulted in
# a header at all; it is only ever read in the FORM-1 inline span, where this
# KB writes it as a deliberate token (`⚠️ **was X**`).

# OLD: the cell names a SUPERSEDED PUBLICATION of this KB's own.
HDR_OLD = re.compile(
    r"published(?:\s+here)?"
    r"|\b(?:kb|shelf|this\s+page|page|the\s+shelf)\s+said\b"
    r"|\bclaim(?:ed)?\b"
    r"|\bold\b|\bprior\b|previous|superseded"
    r"|\bantes\b|publicado",              # this KB writes some tables in es/pt
    re.I)

# NEW: the cell names WHERE THE FACT WAS MEASURED, this pass, from the tree.
HDR_NEW = re.compile(
    r"\btree\b|measured|\bactual(?:ly)?\b|\breal\b|payload[\s-]*read"
    r"|\bnow\b|\btruth\b|\bcorrect(?:ed)?\b|this\s+pass"
    # 🔴 A NEW column may be named by its SOURCE rather than by a measurement
    # noun -- `| address | this shelf published | 🔴 the file says | … |` is the
    # header p124 itself wrote, and `ACTION AB` could not reach it. Found by
    # re-running the instrument against this pass's own new text, which is the
    # only reason it was caught before the next census called it a defect.
    r"|the\s+file(?:\s+says)?\b|from\s+the\s+(?:file|bytes|tree)",
    re.I)

# A pass reference names WHICH PASS produced a figure. On its own that is
# provenance, not supersession: `| control | p119 found, by hand | p120
# measured, by instrument | agrees |` is a CROSS-CHECK of two independent
# measurements, and its left column is not a retracted claim.
HDR_PASS = re.compile(r"\bp\d{2,4}\b", re.I)

# ...and a table that scores its own agreement is a cross-check by
# construction, whatever its other headers say.
HDR_AGREE = re.compile(r"^\s*(?:🟢|🔴|🟡|🔵|\*|\s)*agrees?(?:ment)?\s*\??\s*$", re.I)


def classify_header(cells):
    """Return (old_idx, new_idx) for a table's header, or ([], []) if the
    table is not a correction table at all.

    A correction table has EXACTLY ONE old column and at least one new
    column. Anything else — no old column, two pass columns, an agreement
    column — is a cross-check, a census or an ordinary shelf, and none of
    those records a superseded value.
    """
    if any(HDR_AGREE.match(c.strip()) for c in cells):
        return [], []
    old, new, npass = [], [], 0
    for i, c in enumerate(cells):
        t = c.strip()
        if HDR_PASS.search(t):
            npass += 1
            # A pass column is OLD only when it is the ONLY pass column and
            # it does not itself claim to be a measurement.
            if not HDR_NEW.search(t):
                old.append(i)
            else:
                new.append(i)
            continue
        if HDR_OLD.search(t) and not HDR_NEW.search(t):
            old.append(i)
        elif HDR_NEW.search(t):
            new.append(i)
    if not old or not new:
        return [], []
    return old, new


def split_row(line):
    """Markdown row -> cells, without the empty edges a leading/trailing | makes."""
    s = line.rstrip("\n")
    if not s.lstrip().startswith("|"):
        return None
    parts = s.split("|")
    if len(parts) < 3:
        return None
    return parts[1:-1] if parts[-1].strip() == "" else parts[1:]


SEP = re.compile(r"^\s*\|?[\s:|-]*-{2,}[\s:|-]*\|?\s*$")


# A span this KB QUOTES rather than asserts. These pages discuss their own
# corrections constantly ("Its correction tables read *\"⚠️ **was LGPL-3.0**\"*"),
# and p122 counted six such lines as repaired rows. A quotation is not a
# record: it is prose ABOUT a record, and it needs no marker.
# Where a superseded value was PUBLISHED. This is a vocabulary, and it is a
# vocabulary about publication rather than about licences -- the thing
# ACTION V's guard could not be, because a licence vocabulary is unbounded
# while the set of ways this KB refers to its own pages is small and stable.
PUBLICATION = re.compile(
    r"publish(?:ed|es)?|written\s+here|recorded\s+here"
    # 🔴 This KB writes a TYPOGRAPHIC apostrophe (U+2019) in "this page’s",
    # so a straight-quote-only pattern matched nothing and real prose
    # retractions went unmarked. Both forms are accepted.
    r"|on\s+this\s+page|this\s+page[’']s|in\s+(?:two|three|\d+)\s+cells"
    r"|repaired|corrected|retract|superseded"
    r"|\bwas\b(?:[^.\n]|\.(?=\d)){0,40}?\band\s+is\b",
    re.I)

QUOTED = (
    re.compile(r"\*?\"[^\"]*\"\*?"),      # *"…"* and "…"
    re.compile(r"“[^”]*”"),               # curly quotes
    re.compile(r"`[^`]*`"),               # code spans
)


# 🔴 `GPL-3` and `GPL-3.0` are THE SAME GRANT, written two ways. The first
# build compared raw strings and fired on three rows whose own last cell
# reads `🟢 AGREE` — `moodle/moodle` (`🟡 GPL-3` vs `GPL-3.0 (COPYING.txt)`)
# among them. A correction census that cannot spell a licence two ways
# reports this KB's agreements as its errors.
def norm_token(tok):
    t = tok.upper().replace("_", "-")
    t = re.sub(r"^(A?GPL|LGPL)-?V?(\d)(?:\.0)?$", r"\1-\2.0", t)
    t = re.sub(r"^(EUPL)-?V?(1\.[12])$", r"\1-\2", t)
    return t


FAMILY = re.compile(r"^(AGPL|LGPL|GPL|CC-BY[A-Z-]*|BSD|MPL|EPL|EUPL)$")


def tokens_differ(old, new):
    """True when the two normalised token sets name different grants.

    A BARE family token (`GPL`, `AGPL`) is a version-less spelling of
    whatever version the other side names, so it agrees with any member of
    its own family rather than counting as a distinct grant.
    """
    o = {norm_token(t) for t in old}
    n = {norm_token(t) for t in new}
    if o == n:
        return False

    def resolve(a, b):
        """Replace a bare family name with the version the other side names.

        Resolution must be SYMMETRIC: dropping `GPL` on one side while
        keeping `GPL-3.0` on the other makes the sets differ by
        construction, which was this function's first bug.
        """
        out = set()
        for t in a:
            if FAMILY.match(t):
                same = [x for x in b if x.startswith(t + "-")]
                out.add(same[0] if len(same) == 1 else t)
            else:
                out.add(t)
        return out

    return resolve(o, n) != resolve(n, o)


def _quoted_spans(line):
    out = []
    for rx in QUOTED:
        for m in rx.finditer(line):
            out.append((m.start(), m.end()))
    return out


def _in_quote(line, pos):
    return any(a <= pos < b for a, b in _quoted_spans(line))


def scan(lines):
    """Yield (line_index, form, cell_index_or_None, detail) for every
    correction record that does NOT already carry the marker."""
    hdr_old, hdr_new, in_table = [], [], False
    pending_header = None

    for i, line in enumerate(lines):
        cells = split_row(line)

        # --- table bookkeeping --------------------------------------------
        if cells is None:
            in_table, hdr_old, hdr_new, pending_header = False, [], [], None
        elif SEP.match(line):
            if pending_header is not None:
                hdr_old, hdr_new = classify_header(pending_header)
                in_table = True
                pending_header = None
        elif not in_table:
            pending_header = cells

        # --- FORM 1: already-covered inline span --------------------------
        if cells is not None and "⚠️ **was" in line:
            if MARKER not in line:
                yield (i, "FORM-1", None, "inline span without the marker")
            continue

        # --- FORM 2: a correction is a PAIR, never a lone cell ------------
        # The row must carry a licence token in the old column AND a
        # DIFFERENT one in a new column. One token on its own says only that
        # a licence was mentioned; two differing tokens across the audit
        # boundary is what makes the left one superseded.
        if in_table and cells is not None and hdr_old and not SEP.match(line):
            new_toks = set()
            for cj in hdr_new:
                if cj < len(cells):
                    new_toks |= set(LICENCE.findall(cells[cj]))
            for ci in hdr_old:
                if ci >= len(cells):
                    continue
                old_cell = cells[ci]
                old_toks = set(LICENCE.findall(old_cell))
                if old_toks and MARKER not in old_cell and new_toks \
                        and tokens_differ(old_toks, new_toks):
                    yield (i, "FORM-2", ci, "%s -> %s"
                           % ("+".join(sorted(old_toks)),
                              "+".join(sorted(new_toks))))

        # --- FORM 3: prose "was <licence>", asserted and not quoted -------
        # 🔴 Not every past-tense "was" is a retraction. p124's first build
        # fired on *"the one row with real classroom use, and it was
        # AGPL-3.0"* — a true description of a past shelf state, not a
        # superseded claim. A retraction is identifiable because it says
        # WHERE the old value was published (`published`, `on this page`,
        # `in two cells`, `written here`), or because it states the new
        # value in the same clause (`was MIT and is GPL-2.0`). Prose that
        # does neither is left alone.
        if cells is None and MARKER not in line and PUBLICATION.search(line):
            # 🔴 `[^.\n]` was meant to stop at a sentence end and also
                # stopped at the dot in `Apache-2.0`, so FORM-3 could only ever
                # see VERSION-LESS tokens -- every one of its first 9 findings
                # was a bare `MIT` or `GPL` for exactly this reason. A period
                # followed by a digit is a version, not a full stop.
            for m in re.finditer(r"\bwas\b(?:[^.\n]|\.(?=\d)){0,40}", line):
                lic = LICENCE.search(m.group(0))
                if not lic:
                    continue
                at = m.start() + lic.start()
                if _in_quote(line, m.start()) or _in_quote(line, at):
                    continue
                yield (i, "FORM-3", None, lic.group(0))
                break


def mark(lines, hits):
    """Insert the marker for FORM-2 and FORM-3 hits. Idempotent."""
    by_line = {}
    for i, form, ci, _ in hits:
        by_line.setdefault(i, []).append((form, ci))
    out = list(lines)
    for i, items in by_line.items():
        line = out[i]
        for form, ci in items:
            if form == "FORM-2":
                cells = split_row(line)
                if cells is None or ci >= len(cells) or MARKER in cells[ci]:
                    continue
                cells[ci] = cells[ci].rstrip() + MARKER
                lead = line[:len(line) - len(line.lstrip())]
                tail = "\n" if line.endswith("\n") else ""
                line = lead + "|" + "|".join(cells) + "|" + tail
            elif form == "FORM-3" and MARKER not in line:
                line = re.sub(r"(\bwas\b(?:[^.\n]|\.(?=\d)){0,40}?"
                              + LICENCE.pattern.replace(r"\b(?:", r"(?:") + r")",
                              r"\1" + MARKER, line, count=1)
        out[i] = line
    return out


def main(argv):
    apply_ = "--apply" in argv
    files = [a for a in argv if a != "--apply"]
    tally = {}
    for path in files:
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        hits = list(scan(lines))
        if not hits:
            continue
        for _, form, _, _ in hits:
            tally[form] = tally.get(form, 0) + 1
        rows = len({h[0] for h in hits})
        print("%s\trows=%d\t%s" % (
            path, rows,
            " ".join("%s=%d" % (f, sum(1 for h in hits if h[1] == f))
                     for f in ("FORM-1", "FORM-2", "FORM-3"))))
        if apply_:
            with open(path, "w", encoding="utf-8") as fh:
                fh.writelines(mark(lines, hits))
    print("# TOTAL " + " ".join("%s=%d" % (k, v) for k, v in sorted(tally.items()))
          + " applied=%s" % apply_, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
