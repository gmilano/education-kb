"""Controls for `p253-settled-fact-regression`.

Explicit non-zero exit and a reported check count: it cannot pass while asserting nothing.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import settled_fact as sf  # noqa: E402

FAILED = []
RAN = 0


def chk(name, got, want):
    global RAN
    RAN += 1
    if got != want:
        FAILED.append("  FAIL %s\n       got  %r\n       want %r" % (name, got, want))
    else:
        print("  OK   %s" % name)


PINS = sf.read_pins()
chk("settled.tsv exists — a missing pin file is never silence", PINS is not None, True)
FACT = PINS[0]
chk("the pinned fact is the EU Annex III date", FACT["key"], "eu-annexiii-date")
chk("its settled value is the Omnibus date", FACT["settled_value"], "2027-12-02")

# ── the mandated falsifier: a pass NARRATING the history must pass ──────────────────────
# `agents/top.md` line 1220, p241, verbatim.  It names `2026-08-02`, calls it superseded,
# and cites the regulation.  A gate that flags this is useless, because correcting a
# re-service REQUIRES quoting the wrong date.
P241 = ('| 🔴 *"From 2 August 2026, the AI Office and national authorities started to '
        'enforce the AI Act"*, with education access/assessment as high-risk | 🔴 **At '
        'least the FIFTH recorded re-service of the superseded date.** Annex III education '
        'high-risk applies **`2027-12-02`** under `Reg. (EU) 2026/1744`; `2026-08-02` is '
        'Article `50` transparency, a different obligation. |')
chk("ACTION-grade falsifier: p241 narrating the superseded date is NOT a regression",
    sf.grade_scope(P241, FACT["subject"], FACT["authority"])[0], "CLEAR")

# A scope that hedges but cites the authority is ANNOTATED — history, not re-litigation.
ANNOTATED = ('🟡 Earlier passes carried the Annex III high-risk date as a disjunction; '
             '`Reg. (EU) 2026/1744` closed it at `2027-12-02`.')
chk("a hedge that cites what settled the fact is ANNOTATED, not REGRESSION",
    sf.grade_scope(ANNOTATED, FACT["subject"], FACT["authority"])[0], "ANNOTATED")

# ── and the three real scopes it must catch ─────────────────────────────────────────────
P252_MARKET = ('🟡 **The EU high-risk date is still a disjunction** — `2026-08-02` or a '
               'deferral under the *"AI Omnibus"* — served in both forms by this pass\'s '
               'channel, 🔴 **and still not closable from this session**')
v, hits = sf.grade_scope(P252_MARKET, FACT["subject"], FACT["authority"])
chk("p252's market.md scope is a REGRESSION", v, "REGRESSION")
chk("and both of its hedges are named", sorted(hits), ["disjunction", "not closable"])

P251_GAP = ('| 🔴 **No resolution of the EU Annex III date** | 🔴 the channel served both '
            '`2026-08-02` and the Omnibus deferral *"pending formal adoption"* | 🔴 **NOT '
            'ESTABLISHABLE** |')
chk("p251's open-gaps row is a REGRESSION", 
    sf.grade_scope(P251_GAP, FACT["subject"], FACT["authority"])[0], "REGRESSION")

P251_PATTERNS = ('🔴 **Do not sell an Annex III readiness programme this quarter.** The '
                 'high-risk date is a live disjunction — `2026-08-02` or `2027-12-02` '
                 '*(Omnibus, pending formal adoption)*.')
chk("p251's patterns.md advice is a REGRESSION — and it is the one with a commercial cost",
    sf.grade_scope(P251_PATTERNS, FACT["subject"], FACT["authority"])[0], "REGRESSION")

chk("a scope about something else entirely is CLEAR",
    sf.grade_scope("🟢 `pyKT` ships four new knowledge-tracing models.",
                   FACT["subject"], FACT["authority"])[0], "CLEAR")
chk("naming the subject WITHOUT hedging is CLEAR",
    sf.grade_scope("Annex III education duties bind on `2027-12-02`.",
                   FACT["subject"], FACT["authority"])[0], "CLEAR")

# ── scoping: `ACTION XT`'s table-block ask ──────────────────────────────────────────────
TABLE = "| a | b |\n|---|---|\n| Annex III | still a disjunction |\n"
chk("a contiguous table is ONE scope, so a hedge is argued by its neighbouring rows",
    len(sf.scopes(TABLE)), 1)
chk("and the table-block hedge is therefore caught",
    sf.grade_scope(sf.scopes(TABLE)[0], FACT["subject"], FACT["authority"])[0], "REGRESSION")
chk("a paragraph and the table after it are DIFFERENT scopes",
    len(sf.scopes("prose about Annex III\n| a |\n| still a disjunction |\n")), 2)

# ── p308: the row window (`ACTION p307-R` item 3a) ─────────────────────────────────────
# `ACTION XT` is right about the CITATION and wrong about the SUBJECT.  A subject in one
# row and a hedge in another are not one claim; all four findings this gate carried at
# `p307` were that collision.
COLLIDE = ("| row | note |\n|---|---|\n"
           "| a row about Annex III and nothing else | 🟢 fine |\n"
           "| an unrelated row about `StudentStore` | 🔴 **unresolved** |\n")
chk("a table is still ONE scope (ACTION XT is kept)", len(sf.scopes(COLLIDE)), 1)
chk("but it grades as one unit PER ROW, header excluded",
    len(sf.graded_units(sf.scopes(COLLIDE)[0])), 2)
chk("so a subject in row 1 and a hedge in row 2 is NOT a regression",
    [sf.grade_scope(u, FACT["subject"], FACT["authority"], c)[0]
     for u, c in sf.graded_units(sf.scopes(COLLIDE)[0])],
    ["CLEAR", "CLEAR"])
TOGETHER = ("| row | note |\n|---|---|\n"
            "| Annex III | 🔴 **still a disjunction** |\n")
chk("a subject and a hedge in the SAME row is still caught",
    [sf.grade_scope(u, FACT["subject"], FACT["authority"], c)[0]
     for u, c in sf.graded_units(sf.scopes(TOGETHER)[0])],
    ["REGRESSION"])
CITED = ("| row | note |\n|---|---|\n"
         "| Annex III | 🔴 **still a disjunction** |\n"
         "| the authority | settled by `Regulation (EU) 2026/1744` |\n")
chk("an authority cited in ANOTHER row of the same table still annotates (XT's intent)",
    [sf.grade_scope(u, FACT["subject"], FACT["authority"], c)[0]
     for u, c in sf.graded_units(sf.scopes(CITED)[0])][0],
    "ANNOTATED")
chk("item 3b is answered by NOT dropping open-gaps.md from SHELVES",
    "intel/open-gaps.md" in sf.SHELVES, True)

# ── the root path, which silently broke this gate on its first run ──────────────────────
chk("REPO resolves to the repository root, not to compose/",
    os.path.exists(os.path.join(sf.REPO, "agents", "top.md")), True)
chk("every shelf this gate claims to scan exists",
    [s for s in sf.SHELVES if not os.path.exists(os.path.join(sf.REPO, s))], [])

# ── and an absent pin file is a finding, never an OK ────────────────────────────────────
chk("an absent pin file reports UNPINNED rather than clean",
    sf.scan(pins=None)[0]["verdict"], "UNPINNED")

print()
if FAILED:
    print("\n".join(FAILED))
    print("test_settled_fact.py: %d/%d checks passed, %d FAILED"
          % (RAN - len(FAILED), RAN, len(FAILED)))
    sys.exit(1)
print("test_settled_fact.py: %d/%d checks passed" % (RAN, RAN))
sys.exit(0)
