"""`p253` — catch a pass that RE-OPENS a question an earlier pass of this same base
already settled.

What it is for.  `p233` established, and `p241` relied on, that the Digital Omnibus on AI
is `Regulation (EU) 2026/1744` — OJ `2026-07-24`, in force `2026-07-27` — and that Annex
III education high-risk duties therefore bind on `2027-12-02`, with `2026-08-02`
reclassified as the Article `50` transparency date.  `p241` went further and began
COUNTING re-services of `2026-08-02` as a superseded date, reaching *"at least the
fifth"*.  Ten passes later `p251` published the same question as a live disjunction
*"pending formal adoption"* and recorded it in `intel/open-gaps.md` as **NOT
ESTABLISHABLE**; `p252` re-published it as *"STILL a disjunction"*.  The cost was not
cosmetic: `compose/patterns.md` told the studio not to sell an Annex III readiness
programme because the date was unknown.

Why it happened, and why prose cannot prevent it.  These shelves are append-at-top and
run to ~160 000 lines.  The settled reading sits 500–6 900 lines down; the carried ACTION
ledger is what a new pass actually reads, and once the re-opened form entered the ledger
it propagated forward under its own momentum.  `p252` found the mirror image of this from
the supply side — it checked candidate slugs against the carried index instead of treating
them as new — and recorded that `make carried` could not be run.  A base that cannot query
what it already knows will keep paying for knowledge twice.

The rule.  For each pinned settled fact, a SCOPE that names the subject and hedges about
it is a regression, UNLESS the scope also cites the authority that settled it.  A pass
narrating the history ("the superseded `2026-08-02` date, against `Reg. (EU) 2026/1744`")
cites and passes; a pass re-opening it ("still a disjunction — `2026-08-02` or the
Omnibus deferral, pending formal adoption") does not and fails.

Scope.  A scope is a blank-line-separated block, except that a contiguous run of
`|`-prefixed lines is ONE scope — which is `ACTION XT`'s ask, since a hedge in a table row
is argued by its neighbouring rows and not by the paragraph it sits in.

What this does NOT do.  It does not decide truth.  It compares a pass against this base's
own pinned findings, so a settled fact that is WRONG will be defended by this gate until
the pin is changed — deliberately, because the alternative is a base that silently
re-litigates. `--pin` is how a fact's settled value is revised, and it is a visible edit.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# three levels: instrument -> compose/code -> compose -> repo root.  Two levels landed on
# `compose/`, the gate found every shelf absent, and reported OK — a silent pass, which is
# `p250`/`p251`'s class in a new instrument.  The suite pins the resolved path.
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
PINS = os.path.join(HERE, "settled.tsv")
SHELVES = (
    "README.md",
    "agents/top.md",
    "agents/trending.md",
    "repos/foundations.md",
    "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md",
    "intel/trends.md",
    "intel/open-gaps.md",
    "compose/patterns.md",
)

HEDGES = (
    "disjunction",
    "pending formal adoption",
    "not establishable",
    "not closable",
    "unresolved",
    "two candidates",
    "cannot be closed",
    # p256: the hedge that defeated this instrument ONE PASS after it was built.  p255 did
    # not re-open the EU date; it published `openedx/edx-platform`'s star cell as
    # `UNMEASURABLE` because `edx-platform in:name` returns 217 forks -- while this base had
    # SETTLED at p225 (`ACTION SD`) that the project's canonical name is
    # `openedx/openedx-platform`, which the same query shape resolves on the first row
    # (8 203 stars, measured p256).  An inability is a claim like any other, and a claim this
    # base has already settled may not be re-published without citing what settled it.
    "unmeasurable",
)


def scopes(text):
    """Blank-line blocks, with a contiguous `|` table treated as ONE scope (`ACTION XT`)."""
    out = []
    buf = []
    table = False
    for line in text.splitlines():
        stripped = line.strip()
        is_row = stripped.startswith("|")
        if is_row and not table and buf:
            out.append("\n".join(buf))
            buf = []
        if not is_row and table and buf:
            out.append("\n".join(buf))
            buf = []
        table = is_row
        if not stripped and not table:
            if buf:
                out.append("\n".join(buf))
                buf = []
            continue
        buf.append(line)
    if buf:
        out.append("\n".join(buf))
    return out


def current_section(text):
    """The text of the newest `## ` section — what a pass has just written."""
    lines = text.splitlines()
    start = None
    for i, l in enumerate(lines):
        if l.startswith("## "):
            if start is None:
                start = i
            else:
                return "\n".join(lines[start:i])
    return "\n".join(lines[start:]) if start is not None else text


def hedges_in(scope):
    low = scope.lower()
    return [h for h in HEDGES if h in low]


def grade_scope(scope, subject, authority):
    """REGRESSION, ANNOTATED or CLEAR for one scope against one pinned fact."""
    if not re.search(subject, scope, re.I):
        return "CLEAR", []
    hits = hedges_in(scope)
    if not hits:
        return "CLEAR", []
    if re.search(authority, scope, re.I):
        return "ANNOTATED", hits
    return "REGRESSION", hits


def read_pins(path=None):
    src = path or PINS
    if not os.path.exists(src):
        return None
    rows = []
    with open(src, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if line.strip():
                rows.append(dict(zip(head, line.rstrip("\n").split("\t"))))
    return rows


_UNSET = object()


def scan(repo=None, pins=_UNSET, current_only=True):
    """Findings across the shelves.  `current_only` grades only each file's newest section.

    `None` means *the pin file is absent*, a state distinct from *not supplied*.  Using
    `None` for both was written TWICE in this one pass, here and in
    `p253-captured-body-census`, which says more about the shape than about the hand: a
    default that doubles as a sentinel makes the one control that tests the absent case
    silently test the present one.
    """
    root = repo or REPO
    pins = read_pins() if pins is _UNSET else pins
    if pins is None:
        return [{"shelf": "-", "fact": "-", "verdict": "UNPINNED",
                 "hedges": [], "scope": "settled.tsv is absent"}]
    found = []
    for shelf in SHELVES:
        p = os.path.join(root, shelf)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        body = current_section(text) if current_only else text
        for sc in scopes(body):
            for fact in pins:
                v, hits = grade_scope(sc, fact["subject"], fact["authority"])
                if v == "REGRESSION":
                    found.append({"shelf": shelf, "fact": fact["key"], "verdict": v,
                                  "hedges": hits, "scope": sc[:240]})
    return found


def main(argv):
    args = argv[1:]
    everywhere = "--all" in args
    found = scan(current_only=not everywhere)
    if "--verify" in args:
        for f in found:
            print("%s\t%s\t%s\t%s" % (f["verdict"], f["shelf"], f["fact"], ",".join(f["hedges"])))
        if found:
            print("FAIL: %d scope(s) re-open a settled fact without citing what settled it"
                  % len(found))
            return 1
        print("OK: no settled fact is re-opened in the current pass sections")
        return 0
    pins = read_pins() or []
    print("pinned facts\t%d" % len(pins))
    for f in found:
        print("%s\t%s\t%s\t%s" % (f["verdict"], f["shelf"], f["fact"], ",".join(f["hedges"])))
        print("   %s" % f["scope"].replace("\n", " ")[:200])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
