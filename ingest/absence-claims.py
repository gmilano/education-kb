#!/usr/bin/env python3
"""absence-claims.py -- re-check this KB's ABSENCE claims against its own shelf.

Registered as `568-A`: this base publishes sentences of the form "no X exists" /
"still missing" / "nothing permissive", a client is told to BUILD rather than
ADOPT on the strength of one, and nothing verifies them.  `crosspage-figure-claims.py`
compares figures; existence claims were the only class with no instrument.

Two checks, deliberately separated:

  1. DATED?        -- does the claim carry a pass id (`p123`) or an ISO date on
                      its own line/row?  An undated absence claim written into an
                      append-only page keeps being read as current.  This is the
                      cheap half of `568-A`'s ask and it is decidable.
  2. CONTRADICTED? -- do the claim's content tokens all appear on a line that
                      also carries a `github.com/owner/repo` address (i.e. a
                      shelf row)?  This FLAGS CANDIDATES for adjudication; it
                      does not adjudicate.  A hit means a human must read the
                      row and the claim together, which is exactly what nobody
                      did for `openfun/warren` (the `568-A` founding case).

Exit status: 0 always.  This reports; it does not gate.  A gate needs a baseline
of accepted claims first, and that baseline does not exist yet -- see the note
printed at the end.

Authored and run at p569.  Reads only markdown; executes nothing.
"""
import os
import re
import sys
from collections import OrderedDict

PAGES = [
    "README.md",
    "agents/top.md", "agents/trending.md",
    "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md", "intel/trends.md", "intel/open-gaps.md",
    "intel/measured-unusable.md",
    "compose/patterns.md",
]

# Absence triggers.  English and Spanish: this base's prose is bilingual and the
# Spanish rows were invisible to every English-only check written before now.
TRIGGERS = [
    r"there (?:is|are|was|were) (?:still )?no\b",
    r"\bstill no\b",
    r"\bstill missing\b",
    r"\bstill absent\b",
    r"\bno longer exists\b",
    r"\bdoes(?:n't| not) exist\b",
    r"\bdo(?:n't| not) exist\b",
    r"\bno open[- ]source\b",
    r"\bno permissive\b",
    r"\bno education[- ]specific\b",
    r"\bno dominant\b",
    r"\bno single\b",
    r"\bnothing permissive\b",
    r"\bnothing open\b",
    r"\bnothing education[- ]specific\b",
    r"\bnone (?:of them )?(?:is|are) permissive\b",
    r"\bno (?:such )?(?:repository|repositories|library|libraries|platform|tool|agent|dashboard|detector|generator)\b",
    r"\bnot one\b",
    r"\bzero (?:permissive|open|education|placed|institutional)\b",
    # Spanish
    r"\bno existe\b",
    r"\bno existen\b",
    r"\bsigue sin\b",
    r"\bsiguen sin\b",
    r"\bno hay (?:ning[uú]n|ninguna|nada)\b",
    r"\bninguno de\b",
]
TRIG_RE = re.compile("|".join("(?:%s)" % t for t in TRIGGERS), re.I)

# A SUPPLY claim asserts that the FIELD lacks something buildable-on.  Those are
# the claims that send a client to build instead of adopt, and they are the only
# ones worth gating.  "not one word of prose changed" is an absence sentence and
# is nobody's procurement decision; the narrow tier exists to separate the two.
SUPPLY_NOUN_RE = re.compile(
    r"\b(repositor\w+|librar\w+|platform\w*|framework\w*|dashboard\w*|detector\w*|"
    r"generator\w*|engine\w*|tool\w*|agent\w*|asset\w*|plugin\w*|server\w*|sdk|"
    r"implementation\w*|alternative\w*|equivalent\w*|competitor\w*|project\w*|"
    r"package\w*|suite\w*|stack\w*|solution\w*|option\w*|candidate\w*)\b", re.I)
# Triggers that are rhetorical in this corpus far more often than they are
# supply claims.  Excluded from the narrow tier, kept in the broad one.
RHETORICAL = re.compile(r"^(not one|no single)$", re.I)

DATE_RE = re.compile(r"\bp\d{2,4}\b|\b20\d\d-\d\d-\d\d\b", re.I)
ADDR_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")

STOP = set("""a an the and or of for in on to with without is are was were be been
no not nor none nothing still yet only just any some all every each this that these
those it its there their they them we our us you your i as at by from into over
under than then so such but if when while which who whom whose what why how
exists exist existing does do did doesn don t has have had can could would should
will shall may might must open source permissive licence license licensed
repository repositories repo repos library libraries tool tools platform platforms
one two three four five six seven eight nine ten first second third base pass
sigue siguen existe existen hay ningun ninguna ninguno nada de la el los las un una
y o en con sin para por que se es son del al lo mas más este esta eso aun aún
""".split())

# Tokens too generic to carry a contradiction on their own.  Kept separate from
# STOP so the report can say WHY a claim was not checkable.
WEAK = set("""education educational learning student students teacher teachers
school schools course courses agent agents data model models ai oss""".split())


def tokens(text):
    raw = re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", text.lower())
    return [t for t in raw if t not in STOP]


def sentence_at(line, mstart):
    """The claim's own sentence, or its table cell if the line is a table row."""
    if line.lstrip().startswith("|"):
        cells = line.split("|")
        pos = 0
        for c in cells:
            if pos <= mstart < pos + len(c) + 1:
                return c.strip()
            pos += len(c) + 1
        return line.strip()
    left = max(line.rfind(". ", 0, mstart), line.rfind("; ", 0, mstart)) + 1
    right = line.find(". ", mstart)
    right = len(line) if right == -1 else right + 1
    return line[left:right].strip()


def strip_md(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"https?://\S+", " ", s)
    s = re.sub(r"[`*_#>🔴🟢🟡🔵⛔🆕⚠️]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    root = os.environ.get("KB_ROOT", root)

    # ---- shelf index: every line that carries an address is a candidate row ----
    rows = []            # (page, lineno, lowered text, address set)
    addrs = OrderedDict()
    for page in PAGES:
        p = os.path.join(root, page)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            for n, line in enumerate(fh, 1):
                found = ADDR_RE.findall(line)
                if found:
                    rows.append((page, n, strip_md(line).lower()))
                    for o, r in found:
                        addrs.setdefault("%s/%s" % (o, r.rstrip(".,)")), (page, n))

    claims = []
    for page in PAGES:
        p = os.path.join(root, page)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            for n, line in enumerate(fh, 1):
                for m in TRIG_RE.finditer(line):
                    sent = strip_md(sentence_at(line, m.start()))
                    if len(sent) < 12:
                        continue
                    trig = m.group(0).strip()
                    # A QUOTATION of a refuted claim is byte-identical to the
                    # claim.  p568 refuted "no open-source learning-analytics
                    # dashboard" by quoting it, and this instrument's first run
                    # flagged the refutation as the offence.  A markdown
                    # blockquote is the one half of that distinction that is
                    # DECIDABLE; the rest is registered as a known limit.
                    quoted = line.lstrip().startswith(">")
                    # p569: a STRUCK claim is not a live claim.  Append-only pages
                    # cannot be rewritten, so this base's convention for a false
                    # claim already in history is strike-through + a dated note --
                    # an addition, not a rewrite.  That convention is only worth
                    # anything if an instrument honours it, so this one does, and
                    # the first run of this script flagged a sentence THIS pass had
                    # already struck.  `~~` anywhere on the line is enough: the
                    # claim and its strike markers share a line by construction.
                    struck = "~~" in line
                    quoted = quoted or struck
                    claims.append({
                        "page": page, "line": n, "trigger": trig,
                        "sentence": sent,
                        "quoted": quoted,
                        "struck": struck,
                        "supply": bool(SUPPLY_NOUN_RE.search(sent))
                                  and not RHETORICAL.match(trig)
                                  and not quoted,
                        "dated": bool(DATE_RE.search(line)),
                        # a claim that names an address is self-evidencing, not an
                        # absence claim about the field
                        "self_addressed": bool(ADDR_RE.search(line)),
                    })

    # ---- check 2: candidate contradictions ----
    for c in claims:
        toks = [t for t in tokens(c["sentence"]) if t not in WEAK]
        c["tokens"] = toks[:6]
        c["hits"] = []
        if len(c["tokens"]) < 2:
            c["checkable"] = False
            continue
        c["checkable"] = True
        need = set(c["tokens"])
        for page, n, text in rows:
            if page == c["page"] and n == c["line"]:
                continue
            got = sum(1 for t in need if t in text)
            if got == len(need):
                c["hits"].append((page, n, "ALL"))
            elif got >= max(2, len(need) - 1):
                c["hits"].append((page, n, "%d/%d" % (got, len(need))))
        c["hits"] = c["hits"][:4]

    # ---------------------------- report ----------------------------
    total = len(claims)
    undated = [c for c in claims if not c["dated"]]
    uncheck = [c for c in claims if not c["checkable"]]
    contra = [c for c in claims if any(h[2] == "ALL" for h in c["hits"])]
    partial = [c for c in claims
               if c not in contra and c["hits"]]

    print("absence-claims.py -- %d pages, %d shelf rows, %d distinct addresses"
          % (len([p for p in PAGES if os.path.exists(os.path.join(root, p))]),
             len(rows), len(addrs)))
    print("=" * 78)
    supply = [c for c in claims if c["supply"]]
    s_undated = [c for c in supply if not c["dated"]]
    s_contra = [c for c in supply if any(h[2] == "ALL" for h in c["hits"])]

    print("BROAD tier -- every absence sentence")
    print("absence claims found          : %d" % total)
    print("  UNDATED (no p-id / ISO date): %d  (%.1f%%)   <- 568-A's cheap half"
          % (len(undated), 100.0 * len(undated) / max(1, total)))
    print("  not checkable (<2 tokens)   : %d" % len(uncheck))
    print("  FULL-token shelf collision  : %d" % len(contra))
    print("  partial collision           : %d" % len(partial))
    print()
    print("NARROW tier -- SUPPLY claims only (names a buildable-on noun; the class")
    print("that sends a client to build instead of adopt).  THIS is the gateable set.")
    print("  supply absence claims       : %d" % len(supply))
    print("  (quoted/struck, excluded)   : %d   <- quotation != claim;"
          " struck != live" % len([c for c in claims if c["quoted"]]))
    print("    of which struck           : %d" %
          len([c for c in claims if c["struck"]]))
    print("  UNDATED                     : %d  (%.1f%%)"
          % (len(s_undated), 100.0 * len(s_undated) / max(1, len(supply))))
    print("  FULL-token shelf collision  : %d   <- read these first" % len(s_contra))
    print()

    print("## NARROW-tier FULL-token collisions (candidate published-but-closed gaps)")
    print("-" * 78)
    if not s_contra:
        print("(none)")
    for c in s_contra[:40]:
        print("%s:%d  [%s]%s" % (c["page"], c["line"], c["trigger"],
                                 "" if c["dated"] else "  !UNDATED"))
        print("    claim : %s" % c["sentence"][:220])
        print("    tokens: %s" % " ".join(c["tokens"]))
        for page, n, kind in c["hits"]:
            if kind == "ALL":
                print("    HIT   : %s:%d" % (page, n))
        print()

    print("## Undated absence claims, by page (counts)")
    print("-" * 78)
    by_page = {}
    for c in undated:
        by_page[c["page"]] = by_page.get(c["page"], 0) + 1
    for page in PAGES:
        if page in by_page:
            print("  %-30s %4d" % (page, by_page[page]))
    print()
    print("NOTE: no accepted-claims baseline exists, so this instrument REPORTS and")
    print("does not gate.  Making it a gate requires a reviewed list of claims that")
    print("are correct-and-current; until then a non-zero count is not a failure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
