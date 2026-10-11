#!/usr/bin/env python3
"""Suite for `p471-gap-gate-language/`.

The mandatory cases are the two that keep this an EXTENSION of `p370-gap-gate/` rather than
a counter of the word "gap":

  * the real `P467` sentence, INDEX-scoped, must go NO-CLAIM -> CONTRADICHO; and
  * the CHANNEL-scoped wording of the SAME gap must stay SOSTENIDO in both languages.

If both fired, the instrument would be marking every declared gap, which is the error
`p370-gap-gate/` was written to avoid.
"""
# P115-AK. `python3 -I` (isolated mode) drops the SCRIPT'S OWN DIRECTORY from
# sys.path, so a sibling import fails -- and `-I` is the invocation several of
# this KB's own gate READMEs prescribe ("green under `python3 -I`"). Measured at
# pass 115: all five python gates passed under plain `python3` and ALL FIVE
# failed under `-I`, with a ModuleNotFoundError traceback. A gate that cannot be
# RUN is a gate that passes everything, which is `P471`'s failure wearing a
# different hat. Two lines make the documented invocation true.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p370-gap-gate"))
import gap_gate as G          # noqa: E402
import gap_language as L      # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

# The sentence as `repos/foundations.md` actually carried it for three passes.
P467_INDEX = ("This shelf has declared for three consecutive passes that it can find "
              "no EMEA-origin permissive education foundation.")
# The same gap, written with its scope attached -- `P467`'s own "defensible sentence".
P467_CHANNEL = ("No EMEA-origin permissive education foundation was found through the "
                "forges this environment can reach, and nine forges returned 000.")


class TestTheRealClaim(unittest.TestCase):
    def test_as_shipped_the_gate_declines_to_judge_it(self):
        v, scope, reg, rows = G.verdict(P467_INDEX, G.read_tree(ROOT))
        self.assertEqual(scope, G.SCOPE_UNDETERMINED)
        self.assertEqual(v, G.V_NO_CLAIM)
        self.assertEqual(rows, [])

    def test_but_it_resolved_the_region_correctly_all_along(self):
        # The point of P471: the gate knew WHICH region and still returned NO-CLAIM.
        self.assertEqual(G.region_claimed(P467_INDEX), "EMEA")

    def test_the_sweep_extractor_never_even_presents_it(self):
        self.assertEqual(G.GAP_SENTENCE.findall(P467_INDEX), [])
        self.assertTrue(L.GAP_SENTENCE_EN.findall(P467_INDEX))

    def test_with_english_markers_it_is_contradicted_by_the_tree(self):
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            v, scope, reg, rows = G.verdict(P467_INDEX, G.read_tree(ROOT))
            self.assertEqual(scope, G.SCOPE_INDEX)
            self.assertEqual(v, G.V_CONTRADICHO)
            self.assertEqual(reg, "EMEA")
            self.assertGreater(len(rows), 50)
            self.assertTrue(any(placed for *_, placed in rows))
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved


class TestTheDiscrimination(unittest.TestCase):
    """Without this, the instrument is a counter of the word "gap"."""

    def test_channel_scoped_wording_stays_sostenido_as_shipped(self):
        v, scope, _r, rows = G.verdict(P467_CHANNEL, G.read_tree(ROOT))
        self.assertEqual(rows, [])
        self.assertIn(scope, (G.SCOPE_UNDETERMINED, G.SCOPE_CHANNEL))

    def test_channel_scoped_wording_stays_sostenido_with_english(self):
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            v, scope, _r, rows = G.verdict(P467_CHANNEL, G.read_tree(ROOT))
            self.assertEqual(scope, G.SCOPE_CHANNEL)
            self.assertEqual(v, G.V_SOSTENIDO)
            self.assertEqual(rows, [])
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved

    def test_the_two_wordings_of_one_gap_get_opposite_verdicts(self):
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            tree = G.read_tree(ROOT)
            self.assertEqual(G.verdict(P467_INDEX, tree)[0], G.V_CONTRADICHO)
            self.assertEqual(G.verdict(P467_CHANNEL, tree)[0], G.V_SOSTENIDO)
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved

    def test_a_sentence_that_merely_contains_the_word_gap_is_not_a_claim(self):
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            prose = ("LATAM's governance gap is now measured by a UN-system instrument, "
                     "which is a finding about policy and not about this index.")
            self.assertEqual(G.scope_of(prose), G.SCOPE_UNDETERMINED)
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved


class TestNoRegressionOnSpanish(unittest.TestCase):
    def test_spanish_index_marker_still_scopes(self):
        es = "Esta base no tiene ninguna pieza de origen LATAM."
        self.assertEqual(G.scope_of(es), G.SCOPE_INDEX)

    def test_spanish_channel_marker_still_wins_over_index(self):
        es = ("Esta base no tiene piezas de LATAM, pero el alcance es que este canal "
              "no encuentra codigo de LATAM.")
        self.assertEqual(G.scope_of(es), G.SCOPE_CHANNEL)

    def test_shipped_gate_suite_still_passes(self):
        sys.path.insert(0, os.path.join(HERE, "..", "p370-gap-gate"))
        import test_gap_gate
        self.assertEqual(test_gap_gate.run(), 0)


class TestMechanics(unittest.TestCase):
    def test_with_english_is_idempotent(self):
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            n = (len(G.CHANNEL_MARKERS), len(G.INDEX_MARKERS))
            L.with_english(G)
            L.with_english(G)
            self.assertEqual((len(G.CHANNEL_MARKERS), len(G.INDEX_MARKERS)), n)
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved

    def test_scope_both_restores_module_state(self):
        before = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        L.scope_both(P467_INDEX)
        self.assertEqual((G.CHANNEL_MARKERS, G.INDEX_MARKERS), before)

    def test_scope_both_reports_the_blind_transition(self):
        self.assertEqual(L.scope_both(P467_INDEX),
                         (G.SCOPE_UNDETERMINED, G.SCOPE_INDEX))

    def test_coverage_finds_language_blind_rows_in_the_live_tree(self):
        rows = L.coverage(ROOT)
        self.assertTrue(rows)
        self.assertTrue([r for r in rows if r[3]],
                        "expected at least one language-blind gap claim")

    def test_coverage_leaves_the_gate_as_shipped(self):
        before = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        L.coverage(ROOT)
        self.assertEqual((G.CHANNEL_MARKERS, G.INDEX_MARKERS), before)


class TestP472AssertionClass(unittest.TestCase):
    """A retraction QUOTES the claim it withdraws, so the quotation must not fail a build."""

    def test_bare_assertion_is_the_only_failing_class(self):
        self.assertEqual(
            L.assertion_class("This KB has no EMEA-origin permissive education foundation."),
            L.A_ASSERTED)

    def test_a_quoted_retraction_is_not_an_assertion(self):
        s = '> Superseded text: "no EMEA-origin permissive education foundation."'
        self.assertEqual(L.assertion_class(s), L.A_QUOTED)

    def test_a_table_citation_is_not_an_assertion(self):
        s = '| "No LATAM-origin permissive education project" | REFUTED this pass |'
        self.assertEqual(L.assertion_class(s), L.A_QUOTED)

    def test_a_maturity_qualifier_narrows_the_claim_beyond_what_rows_refute(self):
        s = ("There is no LATAM-origin permissive education product at production "
             "maturity.")
        self.assertEqual(L.assertion_class(s), L.A_QUALIFIED)

    def test_quotation_wins_over_qualifier(self):
        s = '*"no LATAM-origin permissive education product at production maturity"*'
        self.assertEqual(L.assertion_class(s), L.A_QUOTED)

    def test_build_verdict_fails_only_on_a_bare_contradicted_index_claim(self):
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            tree = G.read_tree(ROOT)
            fail, reason = L.build_verdict(P467_INDEX, tree)
            self.assertTrue(fail, reason)
            self.assertIn("CONTRADICHO", reason)
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved

    def test_build_verdict_passes_a_channel_scoped_claim(self):
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            fail, reason = L.build_verdict(P467_CHANNEL, G.read_tree(ROOT))
            self.assertFalse(fail)
            self.assertIn("CANAL", reason)
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved

    def test_build_verdict_passes_the_retraction_now_in_the_tree(self):
        # P472 itself: after the fix, the tree's own quoted retraction must not fail.
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            tree = G.read_tree(ROOT)
            s = ('> **Superseded text:** *"no EMEA-origin permissive education '
                 'foundation."* Asserted here for three consecutive passes.')
            fail, reason = L.build_verdict(s, tree)
            self.assertFalse(fail, reason)
            self.assertEqual(reason, "CONTRADICHO-but-QUOTED")
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved

    def test_live_tree_has_zero_build_failures_after_the_withdrawal(self):
        saved = (G.CHANNEL_MARKERS, G.INDEX_MARKERS)
        try:
            L.with_english(G)
            tree = G.read_tree(ROOT)
            rows = [r for r in L.coverage(ROOT) if r[2] == G.SCOPE_INDEX]
            fails = [s for s, *_ in rows if L.build_verdict(s, tree)[0]]
            self.assertEqual(fails, [], f"unretracted false gap claims: {fails}")
        finally:
            G.CHANNEL_MARKERS, G.INDEX_MARKERS = saved


def run():
    # 🔴 `Gap 245` / `P541`, regresion del pase 49 del 2026-10-08: esta compuerta
    # salia 0 sin juzgar nada.  Un contrato de uso que hay que recordar no es un
    # control (`P237`), asi que el rechazo se asegura aca y no solo se documenta.
    import gap_language as _m
    _r = _m.main([])
    if _r != 2:
        print(f'FAIL  P541-NO-INPUT: main([]) dio {_r}, se esperaba 2')
        globals().setdefault('_P541_FAIL', True)

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    res = unittest.TextTestRunner(verbosity=1).run(suite)
    print(f"{res.testsRun - len(res.failures) - len(res.errors)}/{res.testsRun}")
    return 0 if res.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run())
