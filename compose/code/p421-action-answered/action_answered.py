"""Does a pass DELIVER an action the corpus already answers?

`action-gap-crosscheck` (pase 59) is the instrument for this question.  It has
sat in `compose/code/` for ~360 passes **in no `make` target at all**, and
wiring it as-is would have bought nothing: run over the live corpus at p421 it
reports

    gap citations inside action blocks : 0

because it is calibrated to the retired Spanish-era ledger notation —
`^## ... acciones que el pase N deja escritas`, `gap 51`, `CERRADO`,
`al cierre del pase N` — while the register now writes `### 🟢 Actions`,
`ACTION p420-E` and `Gap 420-C`.  A gate whose denominator is zero PASSES for
the same reason a correct one does, which is `gate-backlog-denominator`'s
class.  So this module re-notates the question and adds the two arms that
catch the specimen that provoked it.

The specimen, measured first-hand at p421:

    ACTION p420-E — "Resolve first-hand whether any Open edX component or
    Sakai is Apache-2.0 ... p289 forbids writing either into a cell unread"

Both halves were already on these shelves when the action was written:
`verticals/solutions.md` carries `| **Sakai** | 🟡 **ECL-2.0**` and
`| **Open edX** | AGPL-3.0`, and `compose/patterns.md` has carried the
Apache-2.0 Open edX component (`openedx/XBlock`, `LICENSE.TXT`) since `p390`.

Three arms, each mechanical:

  STALE                 the clause cites a `Gap` the register declared CLOSED
                        in an EARLIER pass  (the ported arm)
  ANSWERED-BY-ADDRESS   the clause asks a licence question AND names an
                        `owner/repo` that a live shelf already grades
  ANSWERED-BY-PLATFORM  the clause asks a licence question AND names a
                        platform that `verticals/solutions.md` already grades

🔴 What NO arm here catches, stated rather than implied: an action whose
subject is a project named only in prose and absent from the platform
vocabulary.  A loose name-matcher would reproduce `Gap 420-A` exactly — the
defect `gate-absence` has, attributing a claim by TOKEN — so it is not built.
The vocabulary is CLOSED and derived from the base's own platform shelf.

`T103` is honoured throughout: a claim is attributed by its SENTENCE (here, by
its markdown table ROW when it sits in one), never by its line number.
"""

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "p351-address-shape"))
sys.path.insert(0, os.path.join(_HERE, os.pardir, "p348-fold-identity"))
from address_shape import classify   # noqa: E402  the shape rule is p351's, not rewritten
from fold_identity import slugs_in   # noqa: E402  the address CHANNEL is p348's, not rewritten

# 🔴 p421 measured why the channel must be p348's and not a bare `owner/repo` regex.
# A first draft harvested addresses with `\b(owner)/(repo)\b` and produced 194 findings
# whose subjects included `lang/en`, `docs/licence.html` — and `agents/top.md`,
# `intel/open-gaps.md`, `compose/patterns.md` and `verticals/solutions.md`, i.e. THIS
# BASE'S OWN SHELF PATHS.  `classify` returns None (may-be-an-address) for all four;
# `repos/foundations.md` is rejected only because GitHub happens to use `repos` as one
# of its own namespaces.  p348's `slugs_in` anchors on `github.com/`, so a file path
# cannot enter at all — the defect is excluded by construction rather than by a list.

# ── the register's section header, in BOTH notations it has used ──────────────
SECTION = re.compile(r"^##\s+(?:🆕\s+)?`p(\d+)`|^##\s+Pass\s+(\d+)\s+·", re.M)

# ── an action block: any `###` heading naming actions, in any of the three
#    phrasings the register has used (`Actions`, `Actions — ranked...`,
#    `The three registered actions...`, `` `ACTION p378-A`: ... ``).
ACTION_HEADING = re.compile(r"^###\s+.*\baction", re.M | re.I)

# ── an action id, in both notations: `ACTION p420-E` and `ACTION ZZ-ap` / `SH`
ACTION_ID = re.compile(r"ACTION\s+(p\d+-[A-Z]+|[A-Z]{1,3}\d*(?:-[a-z]{1,3})?)")

# ── a gap citation, in both notations: `Gap 420-C`, `Gap 539`, `gap 51`
GAP_CITE = re.compile(r"\b[Gg]ap\s+(\d+(?:-[A-Z])?)")

# ── closure vocabulary, in both notations
CLOSED_HEADING = re.compile(r"^###\s+.*(?:closed|CERRAD)", re.M | re.I)

# ── a licence question.  Deliberately narrow: a licence NAME or one of three
#    words.  `p289` is the rule this serves ("no restatement of an unreachable
#    authority is a verified grant"), so the markers are the ones that rule uses.
LICENCE_MARKER = re.compile(
    r"\b(?:MIT|Apache-2\.0|AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-3\.0|ECL-2\.0|"
    r"BSD-3-Clause|MPL-2\.0|NCSA|licen[cs]e|licen[cs]ed|grant|permissive|copyleft)\b",
    re.I)

LICENCE_TOKEN = re.compile(
    r"\b(?:MIT|Apache-2\.0|AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-3\.0|ECL-2\.0|"
    r"BSD-3-Clause|MPL-2\.0|NCSA)\b")

# 🔴 p421: an ASK, not a mention.  `ACTION p420-B` names `moodle/moodle` as a FIXTURE
# for a gate it asks to BUILD, and the shelf grading Moodle GPL-3.0 does not answer it.
# A licence token alone fired on the word "granted" inside a fixture list; the register's
# real licence questions all carry an interrogative verb.
ASK_VERB = re.compile(
    r"\b(?:resolve|resolved|whether|confirm|confirmed|establish|established|"
    r"determine|verify|verified|unread|re-?read|is it|which licen[cs]e)\b", re.I)

# 🔴 p421, the third and last amendment, and the one that made the arm shippable.
# Cell scoping cut 13 findings to 12: every residual was a licence question whose
# platform name was INCIDENTAL to the ask (`ACTION RV` asks for a LGPL version
# BOUND; `ACTION RQ` asks for a `GPL-2.0` population SWEEP and names Moodle in
# passing).  What separates the one true positive is grammatical, not lexical:
# in `ACTION p420-E` the subject is the OBJECT of the ask —
#     "whether any Open edX component or Sakai is Apache-2.0"
# ask verb, then subject, then a copula, then the licence token, in that ORDER
# and within one span.  A bound question and a population sweep cannot take that
# shape.  So the predicate is an ORDERED TEMPLATE over a bounded span, which is
# testable, rather than another word list, which would not be.
COPULA = re.compile(r"\b(?:is|are|was|were|carries|carry|uses|use|under|licen[cs]ed)\b", re.I)
ASK_SPAN = 240

SHELF_FILES = ("agents/top.md", "agents/trending.md", "repos/foundations.md",
               "repos/trending.md", "verticals/solutions.md", "intel/market.md",
               "intel/trends.md", "compose/patterns.md")


def sections(text):
    """[(pass_number, body)] over both header notations, newest first as written."""
    out = []
    marks = [(m.start(), int(m.group(1) or m.group(2))) for m in SECTION.finditer(text)]
    for i, (pos, num) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((num, text[pos:end]))
    return out


def _blocks(body, heading):
    """The text under each matching `###` heading, to the next `###` or section end."""
    out = []
    for m in heading.finditer(body):
        nxt = re.compile(r"^###\s", re.M).search(body, m.end())
        out.append(body[m.end():nxt.start() if nxt else len(body)])
    return out


def action_blocks(body):
    return _blocks(body, ACTION_HEADING)


def cells_of(clause):
    """A register row is `| action | ask | evidence |`, and the unit is the CELL.

    🔴 p421 measured why.  With the ROW as the unit, `ACTION RV` (*"resolve the
    `openeducat` RANGE-CONFLICT"*) matched because `LGPL-3.0` sits in the row's
    EVIDENCE cell, and `ACTION RQ` (*"sweep the GPL-2.0 sub-population"*) matched
    on platform names in its evidence half.  Eleven of thirteen findings were of
    that shape.  A table cell is where a sentence lives in this register, so
    requiring the ask verb, the licence token and the subject to co-occur in ONE
    cell is `T103`'s rule applied to the markup the register actually uses.
    """
    if clause.lstrip().startswith("|"):
        return [c.strip() for c in clause.strip().strip("|").split("|") if c.strip()]
    return [clause]


def clause_of(block, pos):
    """T103 — the ROW if the match sits in a markdown table row, else the SENTENCE.

    Never the line number, and never a fixed character window: `Gap 419-C`
    registered that a ±N-line window produces false refutations on this base,
    because its rows are single lines thousands of characters wide.
    """
    ls = block.rfind("\n", 0, pos) + 1
    le = block.find("\n", pos)
    le = len(block) if le == -1 else le
    line = block[ls:le]
    if line.lstrip().startswith("|"):
        return re.sub(r"\s+", " ", line).strip()
    # Outside a table: the sentence, bounded by `. ` / `! ` / `? ` or the line.
    lo = pos
    for sep in (". ", "! ", "? "):
        k = block.rfind(sep, ls, pos)
        if k != -1:
            lo = max(lo if lo != pos else ls, k + len(sep))
    lo = ls if lo == pos else lo
    hi = le
    for sep in (". ", "! ", "? "):
        k = block.find(sep, pos)
        if k != -1 and k < hi:
            hi = k + 1
    return re.sub(r"\s+", " ", block[lo:hi]).strip()


def closures(text):
    """gap id -> the EARLIEST pass that declared it closed.

    `Gap 419-C` is the reason the unit is the row: a closure block is a table,
    one gap per row, and a row-blind read attributes every gap in the block to
    every other one's disposition.
    """
    out = {}
    for num, body in sections(text):
        for block in _blocks(body, CLOSED_HEADING):
            for line in block.splitlines():
                if not line.lstrip().startswith("|"):
                    continue
                for g in GAP_CITE.findall(line):
                    if g not in out or num < out[g]:
                        out[g] = num
    return out


def platform_vocabulary(verticals_text):
    """platform name (folded) -> the licence its row carries.

    A CLOSED vocabulary, derived from the base's own platform shelf: the first
    cell of a row that also carries a licence token.  A row whose first cell is
    prose (`Inside`, `Export to one offline HTML file`) carries no licence
    token in this base's shelf and so never enters.
    """
    out, cand = {}, {}
    for line in verticals_text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        m = re.match(r"^\*\*([^*]+)\*\*$", cells[0])
        if not m:
            continue
        name = m.group(1).strip()
        if len(name) < 3 or len(name.split()) > 2:
            continue                      # a sentence is not a platform name
        tok = LICENCE_TOKEN.search(" | ".join(cells[1:]))
        if tok and name.lower() not in out:
            out[name.lower()] = tok.group(0)
    return out

    # 🟡 p421 — the known hole, PINNED AS A FIXTURE rather than guessed at, which is
    # `p364`'s disposition for the locale-prefixed docs path and
    # `action-gap-crosscheck`'s for its own absent fixture.
    # A one-word PROSE first cell (`Inside`, `Outside`) enters this vocabulary when
    # its row happens to carry a licence token.  It does NOT fire on the live shelf —
    # measured: the live vocabulary is 14 entries and contains no prose label — so the
    # hole is LATENT, and `test_the_prose_first_cell_hole_is_open` keeps it visible.
    # 🔴 The obvious closure was BUILT AND REFUTED in-pass: requiring the name to
    # co-occur with a `github.com/...` slug on this shelf drops the vocabulary to 12
    # and REMOVES `sakai`, the true positive's own subject, because this shelf grades
    # Sakai `ECL-2.0` on a row that carries no address at all.  A closure that deletes
    # the specimen is worse than the hole, and `p387-G` forbids the reverse trade too.


def shelf_graded_addresses(shelf_texts):
    """folded address -> a licence token a shelf row carries for it."""
    out = {}
    for text in shelf_texts:
        for line in text.splitlines():
            tok = LICENCE_TOKEN.search(line)
            if not tok:
                continue
            for folded in slugs_in(line):
                if classify(folded) is None and folded not in out:
                    out[folded] = tok.group(0)
    return out


def subjects_asked_about(cell, vocab, graded):
    """Subjects that are the OBJECT of a licence ask in this cell.

    The ordered template, within `ASK_SPAN` characters:
        ASK_VERB ... SUBJECT ... COPULA ... LICENCE_TOKEN
    and the licence asked about must DIFFER from the one the base already
    carries — otherwise the ask is a refinement of a known grade (a version
    bound, a scope) rather than a question the corpus has already answered.
    """
    out = []
    low = cell.lower()
    candidates = [(n, l, "ANSWERED-BY-PLATFORM") for n, l in sorted(vocab.items())]
    for folded in sorted(slugs_in(cell)):
        if classify(folded) is None and folded in graded:
            candidates.append((folded, graded[folded], "ANSWERED-BY-ADDRESS"))

    for ask in ASK_VERB.finditer(cell):
        window = cell[ask.end():ask.end() + ASK_SPAN]
        wlow = window.lower()
        for name, lic, arm in candidates:
            sm = re.search(r"(?<![a-z0-9])" + re.escape(name) + r"(?![a-z0-9])", wlow)
            if not sm:
                continue
            cop = COPULA.search(window, sm.end())
            if not cop:
                continue
            tok = LICENCE_TOKEN.search(window, cop.end())
            if not tok:
                continue
            if tok.group(0) == lic:
                continue                 # a refinement of a grade the base holds
            if (name, lic, arm) not in [(o[0], o[1], o[2]) for o in out]:
                out.append((name, lic, arm))
    return out


def grade(register_text, verticals_text, shelf_texts):
    """-> (findings, denominators).

    A finding is (pass, action_id, arm, subject, evidence, clause).
    The denominators are what makes a green run meaningful rather than empty.
    """
    closed = closures(register_text)
    vocab = platform_vocabulary(verticals_text)
    graded = shelf_graded_addresses(shelf_texts)

    findings = []
    n_blocks = n_actions = 0
    for num, body in sections(register_text):
        for block in action_blocks(body):
            n_blocks += 1
            seen_clause = set()
            for am in ACTION_ID.finditer(block):
                clause = clause_of(block, am.start())
                # 🔴 p421: a clause that cites a SECOND action ("build X, not to
                # `ACTION p419-A`") was graded as if that action had been delivered
                # with this clause's ask.  The subject of a register row is the FIRST
                # action id in it; later mentions are references, not deliveries.
                if clause in seen_clause:
                    continue
                seen_clause.add(clause)
                n_actions += 1
                aid = am.group(1)
                # The ask must be a licence question INSIDE ONE CELL.
                asking = [c for c in cells_of(clause)
                          if LICENCE_TOKEN.search(c) and ASK_VERB.search(c)]

                for g in GAP_CITE.findall(clause):
                    if g in closed and closed[g] < num:
                        findings.append((num, aid, "STALE", f"Gap {g}",
                                         f"closed at p{closed[g]}", clause))

                for cell in asking:
                    for subj, lic, arm in subjects_asked_about(cell, vocab, graded):
                        findings.append((num, aid, arm, subj,
                                         f"shelf grades it {lic}", cell))

    return findings, {"action_blocks": n_blocks, "actions": n_actions,
                      "closed_gaps": len(closed), "platforms": len(vocab),
                      "graded_addresses": len(graded)}


def read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return fh.read()


def run(root):
    register = read(root, "intel/open-gaps.md")
    verticals = read(root, "verticals/solutions.md")
    shelves = [read(root, p) for p in SHELF_FILES]
    return grade(register, verticals, shelves)


def main(argv):
    root = argv[1] if len(argv) > 1 else "../../.."
    findings, denom = run(root)
    tsv = "--tsv" in argv
    if tsv:
        print("pass\taction\tarm\tsubject\tevidence\tclause")
        for f in findings:
            print("\t".join(str(x) for x in f))
        return 0
    for k, v in denom.items():
        print(f"{k:20s}: {v}")
    print(f"{'findings':20s}: {len(findings)}")
    for num, aid, arm, subj, ev, clause in findings:
        print(f"\n  p{num} ACTION {aid} — {arm}")
        print(f"    subject : {subj}")
        print(f"    evidence: {ev}")
        print(f"    clause  : {clause[:220]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
