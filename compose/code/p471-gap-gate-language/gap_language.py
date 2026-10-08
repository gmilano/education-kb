#!/usr/bin/env python3
"""`p471-gap-gate-language/` -- why `p370-gap-gate/` stopped catching anything.

Pass 35, 2026-10-07.

`p370-gap-gate/` was built to falsify a DECLARED gap against this KB's own index, and it
works: its suite is 27/27 and the pass that introduced it reported **29 gap sentences with
a region -> 2 CONTRADICHOS**.

Swept against the live tree on 2026-10-07 it reports **5 gap sentences -> 0 CONTRADICHOS,
all 5 NO-CLAIM / SIN-ALCANCE**. The KB did not stop declaring gaps in the meantime:
`repos/foundations.md` declared an EMEA gap for three consecutive passes (`P467`), and that
claim was FALSE -- `OpenOLAT/OpenOLAT` (Apache-2.0, Zurich/frentix) and `OpenOLAT/qtiworks`
(BSD-3-Clause, Edinburgh) were already on these shelves (`P469`).

What changed is the LANGUAGE the KB writes its gaps in. Two independent filters in
`gap_gate.py` are Spanish-only:

  1. `GAP_SENTENCE` -- the extractor used by `--sweep`. It matches only sentences containing
     `hueco`, `cero repositorios` or `sigue abierta`. Measured: it extracts NOTHING from the
     real `P467` sentence, so a sweep never even presents it for judgement.
  2. `INDEX_MARKERS` / `CHANNEL_MARKERS` -- the SCOPE classifier. Spanish-only, so an English
     gap sentence falls through to SIN-ALCANCE and the verdict is NO-CLAIM.

Measured on the real `P467` sentence, verbatim:

    verdict=NO-CLAIM  scope=SIN-ALCANCE  region=EMEA  contradicting_rows=0

Note `region=EMEA` resolved correctly -- `region_in_prose` is language-independent because
the five region names are the same in both languages. **So the gate knew which region the
claim was about, and still declined to judge it.** Meanwhile the tree carries **94 repo rows
that name EMEA next to a GitHub URL**, 77 of them PLACED (region heads the cell). The
contradiction material was abundant; the gate never reached the comparison step.

With English markers added, the same sentence returns:

    verdict=CONTRADICHO  scope=INDICE  region=EMEA  contradicting_rows=94  (77 placed)

and the CHANNEL-scoped English variant of the same gap still returns SOSTENIDO -- which is
the control that keeps this an extension of the gate rather than a counter of the word "no".

🔴 The transferable failure (`P471`): **NO-CLAIM is not a safe default.** A gate that cannot
parse its input returned the same verdict it returns for prose that is not a claim at all,
so a reader of the sweep sees "nothing to judge" where the truth was "I cannot read this."
An instrument whose coverage silently depends on the prose language of the corpus decays the
moment the corpus changes language, and reports full health while doing it.

🔵 This file does NOT replace `p370-gap-gate/`. It measures that gate's coverage over a
corpus and names the untested class. `MARKERS_EN` is the fix to fold back into it.

Usage:
    python3 gap_language.py --self-test
    python3 gap_language.py --coverage ROOT
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p370-gap-gate"))
import gap_gate as G  # noqa: E402  (P237: the gate is not reimplemented, it is measured)

# English equivalents of the gate's two Spanish marker sets. Deliberately NOT a translation
# of every phrase: only the forms this KB actually writes, so the extension cannot be
# accused of broadening the gate's reach beyond measured prose.
CHANNEL_MARKERS_EN = (
    r"this channel",
    r"this query",
    r"the sweep returned",
    r"not findable here",
    r"through the forges this environment can reach",
    r"an informed gap",
    r"declared gap",
    r"returned no \w+",
)
INDEX_MARKERS_EN = (
    r"no \w+-origin",
    r"zero repositories",
    r"this kb (?:does not|has no)",
    r"this shelf (?:does not|has no)",
    r"no such asset exists",
    r"remains? (?:an )?open gap",
)
# The extractor's English triggers, for --sweep parity.
GAP_SENTENCE_EN = re.compile(
    r"[^.\n]*(?:\bgap\b|no \w+-origin|zero repositories|remains open)[^.\n]*\.",
    re.IGNORECASE)


def with_english(mod=G):
    """Install the English markers on the gate. Idempotent."""
    for name, extra in (("CHANNEL_MARKERS", CHANNEL_MARKERS_EN),
                        ("INDEX_MARKERS", INDEX_MARKERS_EN)):
        cur = getattr(mod, name)
        missing = tuple(m for m in extra if m not in cur)
        setattr(mod, name, cur + missing)
    return mod


def scope_both(claim):
    """(scope_as_shipped, scope_with_english) for one sentence.

    Measured by saving and restoring the gate's module state, so a caller that wants the
    as-shipped behaviour afterwards still gets it. That matters: `with_english` mutates a
    module other instruments import.
    """
    saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
    try:
        as_shipped = G.scope_of(claim)
        with_english(G)
        extended = G.scope_of(claim)
    finally:
        G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved
    return as_shipped, extended


def extracted_by(text, pattern):
    return [" ".join(s.split()) for s in pattern.findall(text)]


# P472, measured on this same tree AFTER `P467` was withdrawn: of the 11 index-scoped gap
# claims the extended gate marks CONTRADICHO, **11 carry quotation or table-citation markers
# and 0 are bare live assertions.** The reason is structural and will recur in any corpus:
# *the correct way to retract a false gap is to quote it in the retraction*, and the quotation
# then trips the gate forever. A second class is narrowed by a qualifier the gate cannot see --
# "no LATAM-origin permissive education product **at production maturity**" is a claim about
# MATURITY, not about existence, and placed rows do not refute it.
# So a gate that failed the build on CONTRADICHO alone would have produced 11 false failures
# and 0 true ones here. Classify first, then fail.
QUOTE_MARKERS = re.compile("[\"“”«»]|^\\s*>|\\|\\s*[\"“]|\\*\"")
QUALIFIER_MARKERS = re.compile(
    r"production[- ]maturity|production[- ]ready|\bat scale\b|\bmaturity\b", re.IGNORECASE)

A_QUOTED = "QUOTED"        # a citation or retraction, not an assertion -> do NOT fail
A_QUALIFIED = "QUALIFIED"  # narrowed on a dimension the gate cannot measure -> do NOT fail
A_ASSERTED = "ASSERTED"    # a bare live claim -> the only class that fails a build


def assertion_class(claim):
    """Is this sentence ASSERTING a gap, QUOTING one, or narrowing it with a QUALIFIER?

    Order matters: quotation wins, because a retraction that quotes a qualified claim is
    still a retraction. Only ASSERTED may ever fail a build.
    """
    if QUOTE_MARKERS.search(claim):
        return A_QUOTED
    if QUALIFIER_MARKERS.search(claim):
        return A_QUALIFIED
    return A_ASSERTED


def build_verdict(claim, tree, gate=G):
    """The composed check `P45` actually prescribes: (fail, reason).

    `fail` is True only for an INDEX-scoped, CONTRADICHO, bare-ASSERTED claim.
    """
    v, scope, reg, rows = gate.verdict(claim, tree)
    cls = assertion_class(claim)
    if scope != gate.SCOPE_INDEX:
        return False, scope + "/not-an-index-claim"
    if v != gate.V_CONTRADICHO:
        return False, v + "/no-contradicting-rows"
    if cls != A_ASSERTED:
        return False, "CONTRADICHO-but-" + cls
    return True, "CONTRADICHO/%d-rows/%s" % (len(rows), reg)


def coverage(root):
    """Per-sentence coverage of the gate over a corpus.

    Returns rows (sentence, scope_shipped, scope_extended, language_blind) where
    `language_blind` is True when the gate cannot scope the sentence as shipped but CAN
    once the English markers are present. That boolean is the finding: it is the class of
    claim the gate silently declines to judge.
    """
    tree = G.read_tree(root)
    seen, rows = set(), []
    for _path, text in tree:
        for s in extracted_by(text, GAP_SENTENCE_EN) + extracted_by(text, G.GAP_SENTENCE):
            if len(s) < 40 or s in seen:
                continue
            seen.add(s)
            if G.region_claimed(s) is None:
                continue
            shipped, extended = scope_both(s)
            rows.append((s, shipped, extended,
                         shipped == G.SCOPE_UNDETERMINED
                         and extended != G.SCOPE_UNDETERMINED))
    return rows


def main(argv):
    # 🔴 `Gap 245` / `P541`, remediado en el pase 49 del 2026-10-08.
    # Sin argumentos esta compuerta imprimia su docstring y salia **0**: el barrido
    # `p542` la clasifico `P541-FALSE-PASS` con el oraculo de lectura — exit 0 habiendo
    # abierto CERO archivos del arbol, indistinguible de un arbol limpio. `Gap 245`
    # nombro estas dos compuertas como las PRIMERAS a arreglar, por lo que son: las que
    # existen para cachar huecos no declarados.
    if not argv:
        print(
            "P541-NO-INPUT\tREFUSED: esta compuerta no mide nada sin una RAIZ.  "
            "Salir 0 aca seria indistinguible de un arbol limpio.  "
            "Uso: %s --sweep RAIZ  |  --self-test" % 'gap_language.py',
            file=sys.stderr,
        )
        return 2
    if "--self-test" in argv:
        import test_gap_language
        return test_gap_language.run()
    if "--coverage" in argv:
        root = argv[argv.index("--coverage") + 1]
        rows = coverage(root)
        blind = [r for r in rows if r[3]]
        for s, shipped, extended, isblind in rows:
            print(f"{'LANG-BLIND' if isblind else 'covered   '} "
                  f"{shipped:<12} -> {extended:<12} {s[:96]}")
        print(f"\n# gap sentences with a region: {len(rows)}   "
              f"language-blind: {len(blind)}")
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
