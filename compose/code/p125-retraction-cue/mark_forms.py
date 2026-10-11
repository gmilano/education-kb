#!/usr/bin/env python3
"""ACTION AF — one retraction CUE, not thirteen regexes.

p124's `ACTION AC` enumerated nine surface forms of this KB's correction
apparatus and reached four. p125 began by writing one pattern per unreached
form and stopped at thirteen, because enumeration is losing: every pass that
writes a correction invents a spelling, and the sweep that chases it ships one
pass later. The forms p125 found beyond p124's nine:

  FORM 10  `⚠️ was X` with NO emphasis at all   (19 of 61 violations)
  FORM 11  prose naming a PRIOR PASS's reading  ("`p1040` read Elastic-2.0 …")
  FORM 12  a `P###-x` finding SECTION whose heading announces the correction
  FORM 13  a licence named in a CONTRAST clause ("Neither restriction exists
           under AGPL-3") — not a claim about the repository at all

So the model changes from a form list to a two-part rule, which is the same
move p123 made for the grant (one token -> a SET) and p124 made for the split
(a phrase list -> a SHAPE):

  1. a RETRACTION CUE — a verb or sigil that announces a superseded value
  2. a SCOPE GATE — `scope_gate.py` (ACTION AG), which tells a retraction
     from a contrast, a quotation or a live claim

FORM 13 is handled by the gate rather than by a pattern, and that is the
point: a licence token in a comparison clause was never a claim, so it needs
no marker. Marking it would record a correction that never happened.

usage:
  mark_forms.py --report FILE...    what would be marked, by form
  mark_forms.py --apply  FILE...    append the marker; idempotent
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scope_gate                                        # noqa: E402
from correction_form import (LICENCE, MARKER,            # noqa: E402
                             classify_header, norm_token, split_row)

# A `.` inside `Apache-2.0` is a version separator, not a full stop. p124's
# `[^.\n]` window made every versioned token invisible to the prose forms.
_NE = r"(?:[^.\n|]|\.(?=\d))"
TOK = LICENCE.pattern[2:-2]          # the alternation, without its own \b..\b

# ---------------------------------------------------------------- the cues
# Each cue captures the SUPERSEDED token in group `tok`. The sigil forms
# accept zero, one or two asterisks, which is forms 1, 4, 5 and 10 at once.
CUES = (
    ("1/4/5/10", re.compile(
        r"⚠️\s*\*{0,2}\s*(?:was|KB said|shelf said|page said|published)\s*"
        r"\**\s*(?:🔴|🟢|🟡|🔵)?\s*\**\s*(?P<tok>" + TOK + r")")),
    ("6", re.compile(
        r"\((?:" + _NE + r"){0,46}?\b(?:published|KB said|was published)\b"
        r"(?:\s+as)?\s*\**\s*(?P<tok>" + TOK + r")")),
    ("3", re.compile(
        r"\bwas\s+(?:published|row-level|marked)?\s*\**\s*"
        r"(?:🔴|🟢|🟡|🔵)?\s*\**\s*(?:as\s+)?(?P<tok>" + TOK + r")")),
    ("7", re.compile(
        r"\b(?:as|but as)\s+\**(?:" + TOK + r")\**\s*,?\s*\**not\**\s+"
        r"(?P<tok>" + TOK + r")")),
    ("7b", re.compile(
        r"\bmarked\b(?:" + _NE + r"){0,90}?\bas\s+\**(?P<tok>" + TOK + r")")),
    ("11", re.compile(
        r"\b(?:p\d+|an older row(?: on this shelf)?|this cell)\s+"
        r"(?:read|said|named|published)\b(?:" + _NE + r"){0,60}?"
        r"\**\s*(?P<tok>" + TOK + r")")),
)
# FORM 8: the NEW cell holds no licence token, so the pair rule cannot fire.
# An enumerated, closed list of admissible non-token new values.
NO_GRANT = re.compile(
    r"\bNO[ -]GRANT(?:\s+FILE)?\b|\bNO-FILE\b|\bUNLICENSED\b|"
    r"\bnothing\b|\bno lic[es]nce file\b|\bbadge reads\b|"
    r"\bno\s+`?license`?\s+field\b|\bdoes not resolve\b", re.I)
# A relative pronoun is not a copula: "the token that WAS invisible".
REL = re.compile(r"\b(?:that|which|where|when|who|it|this|and)\s+was\b", re.I)
# A quotation, a fence, or a pre-registered ACTION clause is apparatus prose,
# not a row. `QUOTED-REFUTATION` rows exist to display a wrong claim.
APPARATUS = re.compile(
    r"^\s*>|^\s*```|\bACTION [A-Z]{1,2}\b|\*Refuted if|\bQUOTED-REFUTATION\b|"
    r"\bRefuted if\b|"
    # 🔴 THE VOCABULARY OF THE APPARATUS ITSELF, added by the self-audit that
    # p124 made part of the method: running this module over the sections the
    # CURRENT pass has just written. p125's own forms table
    # (`| 11 | prose naming a PRIOR PASS's reading (…"said AGPL-3 and was
    # superseded") | 🟢 p125 |`) and its own paragraph on discussion OF the
    # marker produced 8 false positives across 4 pages. A page that documents
    # the apparatus quotes every form it covers, so it will always trip a cue.
    r"\bFORM ?\d|\bsurface forms?\b|\bretraction cue\b|\bprose naming\b|"
    r"\bdiscussion OF\b|\bmarker\b|"
    # An ESCAPED quote appears only when a construction is being quoted
    # verbatim inside an already-quoted span -- `*"read *\"⚠️ **was X**\"*"*`.
    r'\\"')


def in_code_or_quote(line, pos):
    """Is `pos` inside a backtick span or a quotation?

    🔴 THIS IS WHAT SEPARATES A CORRECTION FROM PROSE ABOUT CORRECTIONS, and
    leaving it out put 6 of this build's first 93 rows on lines that merely
    DISCUSS the marker -- `(`⚠️ **was 🟢 MIT**` inside the cell)` and
    *"the superseded value as `"was MIT"`"*. p124 hit the same wall from the
    other side: its headline figure of 94 marked rows differed from a raw
    grep's 102 by exactly these lines.

    The test is on the CUE's position, not the token's. The understory row
    reads `🔴 **p123 published `MIT` for the whole repository.**` -- the token
    is inside backticks and the cue is not, and that row IS a correction.
    """
    ticks = 0
    for i, ch in enumerate(line):
        if i >= pos:
            break
        if ch == "`":
            ticks += 1
    if ticks % 2 == 1:
        return True
    # a quoted span: *"..."* or plain "..." / '...' around the cue
    for m in re.finditer(r"\*?[\"\u201c\u2018'](?:[^\"\u201d\u2019'\n]{0,160})"
                         r"[\"\u201d\u2019']\*?", line):
        if m.start() <= pos < m.end():
            return True
    return False


# A bare family token made precise is a RESOLUTION, not a correction. p124's
# `ACTION AD` resolved 41 bare `CC` grants to a version and did not call any
# of them a correction; the same must hold for `GPL` -> `GPL-3.0`. Without
# this rule 20 Moodle-plugin rows reading `| `GPL` | 🟢 **GPL-3.0** |` are
# marked as repairs that never happened.
FAMILY = ("AGPL", "LGPL", "GPL", "CC", "BSD", "Apache", "EUPL", "MPL", "EPL")


def is_resolution(old, new):
    o, n = norm_token(old), norm_token(new)
    if o == n:
        return True
    for fam in FAMILY:
        if o == fam and n.startswith(fam):
            return True
    return False


def _gate_ok(line, at, tok):
    """ACTION AG over a markdown line: is this token a CLAIM at all?"""
    lab = scope_gate.label_span(line, at, at + len(tok))
    return lab not in ("CONTRAST", "SECONDARY", "OUT-OF-TREE",
                       "RECOMMENDATION", "DOCUMENT-TEXT")


def cue_hits(line):
    """[(form, token, end_offset)] for every retraction cue on the line."""
    if MARKER in line or APPARATUS.search(line):
        return []
    out = []
    for form, pat in CUES:
        for m in pat.finditer(line):
            if form == "3" and REL.search(line[max(0, m.start() - 26):
                                               m.start() + 4]):
                continue
            if in_code_or_quote(line, m.start()):
                continue
            if not _gate_ok(line, m.start("tok"), m.group("tok")):
                continue
            out.append((form, m.group("tok"), m.end("tok")))
    return out


SEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")


def _is_header_row(lines, ln):
    """A header row is the one directly above a `|---|---|` separator."""
    return ln < len(lines) and SEP.match(lines[ln])


def table_hits(path):
    """FORM 2 and FORM 8: an OLD column under a correction-table header."""
    hits, hdr = [], None
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    for ln, line in enumerate(lines, 1):
        if not line.lstrip().startswith("|"):
            hdr = None
            continue
        if APPARATUS.search(line):
            continue
        # 🔴 A HEADER ROW MUST CLEAR THE PREVIOUS TABLE'S MAPPING, and not
        # doing so was this build's worst defect. `classify_header` returning
        # None left the preceding correction table's (old, new) columns in
        # force over an ORDINARY table, and
        # `repos/foundations.md`'s foundational shelf -- header
        # `| address | ★ | 🟢 licence, measured | region | ... |` -- had its
        # LIVE licence column marked as superseded on
        # `1EdTech/openbadges-validator-core`. A mapping that outlives its
        # table is worse than no mapping.
        if _is_header_row(lines, ln):
            hdr = classify_header(line)
            continue
        if re.match(r"^\s*\|[\s:|-]+\|\s*$", line) or hdr is None:
            continue
        cells = split_row(line)
        olds, j = hdr
        if j >= len(cells):
            continue
        new_cell = cells[j]
        new_toks = {norm_token(t) for t in LICENCE.findall(new_cell)}
        absent = bool(NO_GRANT.search(new_cell))
        for i in olds:
            if i >= len(cells) or MARKER in cells[i]:
                continue
            old = [t for t in LICENCE.findall(cells[i])
                   if norm_token(t) not in new_toks
                   and not any(is_resolution(t, n) for n in new_toks)]
            if not old:
                continue
            if new_toks:
                hits.append((ln, i, "2", ",".join(old)))
            elif absent:
                hits.append((ln, i, "8", ",".join(old)))
    return hits


def _past_emphasis(line, end):
    """Move `end` past a closing `*`/`**` that the cue opened.

    🔴 Inserting the marker straight after the token split the span:
    `⚠️ *was GPL<!--corrected-->*`. The span patterns require the marker
    AFTER the closing emphasis, so a marked row then read back as unmarked
    and the assertion re-raised it -- 3 rows on `repos/foundations.md` and
    `verticals/solutions.md`, every one of them already repaired.
    """
    m = re.match(r"\*{1,2}", line[end:])
    return end + len(m.group(0)) if m else end


def apply_marks(path, dry=True):
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    tbl = {}
    for ln, i, form, old in table_hits(path):
        tbl.setdefault(ln, (i, form, old))
    changed, byform = 0, {}
    for ln in range(1, len(lines) + 1):
        line = lines[ln - 1]
        if MARKER in line:
            continue
        hits = cue_hits(line)
        if hits:
            form, _tok, end = hits[0]
            end = _past_emphasis(line, end)
            lines[ln - 1] = line[:end] + MARKER + line[end:]
        elif ln in tbl:
            i, form, _old = tbl[ln]
            cells = line.rstrip("\n").split("|")
            k = i + 1                 # split("|") yields a leading "" cell
            if k >= len(cells):
                continue
            cells[k] = cells[k].rstrip() + MARKER + " "
            lines[ln - 1] = "|".join(cells) + "\n"
        else:
            continue
        changed += 1
        byform[form] = byform.get(form, 0) + 1
    if not dry and changed:
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(lines)
    return changed, byform


def main(argv):
    apply_ = "--apply" in argv
    paths = [a for a in argv if not a.startswith("-")]
    total, allforms = 0, {}
    for p in paths:
        n, bf = apply_marks(p, dry=not apply_)
        total += n
        for k, v in bf.items():
            allforms[k] = allforms.get(k, 0) + v
        print("%-26s %3d  %s" % (p, n, " ".join(
            "F%s=%d" % (k, v) for k, v in sorted(bf.items()))))
    print("TOTAL %d   %s" % (total, " ".join(
        "F%s=%d" % (k, v) for k, v in sorted(allforms.items()))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
