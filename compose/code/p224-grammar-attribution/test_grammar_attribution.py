"""Tests for p224's attribution instrument.

Controls that must NOT fire are marked CONTROL. Eight passes of this KB's history say
the instrument is likelier to be wrong than the shelf, so the controls outnumber the
positive assertions on purpose. Every fixture below is a real string shape taken from
these shelves or from p221/p222's own written-up defects.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grammar_attribution as g  # noqa: E402


class TestBareness(unittest.TestCase):
    def test_bare_token_is_bare(self):
        ms = g.mentions_in_line('| `openeducat/openeducat_erp` | `LGPL-3.0` | ERP |')
        self.assertEqual(len(ms), 1)
        self.assertTrue(ms[0]['bare'])

    def test_or_later_is_not_bare_CONTROL(self):
        ms = g.mentions_in_line('| `frappe/lms` | `AGPL-3.0-or-later` | LMS |')
        self.assertEqual(len(ms), 1)
        self.assertFalse(ms[0]['bare'])

    def test_only_is_not_bare_CONTROL(self):
        ms = g.mentions_in_line('| `oat-sa/tao-core` | `GPL-2.0-only` | QTI |')
        self.assertFalse(ms[0]['bare'])

    def test_prose_or_later_is_not_bare_CONTROL(self):
        ms = g.mentions_in_line('bycs-lp/moodle-local_ai_manager is GPL-3.0, or at your option any later version')
        self.assertFalse(ms[0]['bare'])

    def test_daycount_artefact_is_not_a_licence_CONTROL(self):
        """p221's census counted `AGPL-6 d` in a liveness table once. It must not recur."""
        ms = g.mentions_in_line('| row | AGPL-6 d | last commit |')
        self.assertEqual(ms, [])

    def test_non_gnu_token_ignored_CONTROL(self):
        self.assertEqual(g.mentions_in_line('| `shmercer/writeAlizer` | `MIT` | R |'), [])

    def test_span_not_line_p223_rule(self):
        """A bound belonging to a DIFFERENT token must not exonerate this one.

        This is p223's defect restated: a qualifier elsewhere on the line exonerated the
        line. The window is why the first token here stays bare.
        """
        line = ('| `a/one` | `LGPL-3.0` | x |' + ' ' * 80 +
                '| `b/two` | `GPL-3.0-or-later` | y |')
        ms = g.mentions_in_line(line)
        self.assertEqual(len(ms), 2)
        self.assertTrue(ms[0]['bare'])
        self.assertFalse(ms[1]['bare'])


class TestSlugs(unittest.TestCase):
    def test_bare_slug_and_url_are_one_row(self):
        line = '`openeducat/openeducat_erp` at https://github.com/openeducat/openeducat_erp'
        self.assertEqual(g.slugs_on(line), ['openeducat/openeducat_erp'])

    def test_case_variants_collapse(self):
        line = '`OpenEduCat/openeducat_erp` and `openeducat/openeducat_erp`'
        self.assertEqual(g.slugs_on(line), ['openeducat/openeducat_erp'])

    def test_evidence_path_is_not_a_row_CONTROL(self):
        self.assertEqual(g.slugs_on('see evidence/rh-range-census.2026-10-15-p221.tsv'), [])

    def test_doc_path_is_not_a_row_CONTROL(self):
        self.assertEqual(g.slugs_on('see compose/patterns.md and intel/market.md'), [])

    def test_raw_path_yields_the_row(self):
        line = 'https://raw.githubusercontent.com/dexter-psychometrics/dexter/master/DESCRIPTION'
        self.assertIn('dexter-psychometrics/dexter', g.slugs_on(line))


class TestAttribution(unittest.TestCase):
    GRAMMAR = {
        'dexter-psychometrics/dexter': 'cran',
        'openeducat/openeducat_erp': 'odoo',
        'frappe/lms': 'spdx',
    }

    def test_attributes_to_the_single_row(self):
        t = g.attribute(['| `openeducat/openeducat_erp` | `LGPL-3.0` |'], self.GRAMMAR)
        self.assertEqual(t['bare_attributed'], 1)
        self.assertEqual(t['by_grammar'], {'odoo': 1})

    def test_multi_slug_line_is_not_attributed_CONTROL(self):
        """p222 produced 2 false GRANT-CONFLICTs exactly this way: the token belonged to
        a comparison, not to the slug sharing its line."""
        line = '`academico-sis/academico` is MIT, unlike `wingkwong/react-quiz-component`: GPL-2.0 elsewhere'
        t = g.attribute([line], self.GRAMMAR)
        self.assertEqual(t['bare_attributed'], 0)
        self.assertEqual(t['bare_ambiguous_line'], 1)

    def test_no_slug_line_is_reported_not_dropped_CONTROL(self):
        t = g.attribute(['The GPL-3.0 family dominates this shelf.'], self.GRAMMAR)
        self.assertEqual(t['bare_no_slug_on_line'], 1)
        self.assertEqual(t['bare_attributed'], 0)

    def test_unmapped_row_is_unread_not_zero(self):
        t = g.attribute(['| `some/other` | `GPL-3.0` |'], self.GRAMMAR)
        self.assertEqual(t['by_grammar'], {'unread': 1})

    def test_mit_cran_row_never_enters_the_gnu_population_CONTROL(self):
        """7 of the 11 CRAN rows are MIT/BSD. A grammar map must not drag them in."""
        t = g.attribute(['| `shmercer/writeAlizer` | `MIT + file LICENSE` |'],
                        {'shmercer/writealizer': 'cran'})
        self.assertEqual(t['gnu_mentions'], 0)
        self.assertEqual(t['by_grammar'], {})

    def test_qualified_mentions_counted_separately(self):
        t = g.attribute(['| `frappe/lms` | `AGPL-3.0-or-later` |'], self.GRAMMAR)
        self.assertEqual(t['qualified_mentions'], 1)
        self.assertEqual(t['bare_mentions'], 0)


class TestVerdict(unittest.TestCase):
    def test_limb_1_at_threshold(self):
        v = g.verdict({'by_grammar': {'odoo': 50}})
        self.assertEqual(v['limb'], 1)

    def test_limb_2_below_threshold(self):
        v = g.verdict({'by_grammar': {'odoo': 20, 'cran': 29}})
        self.assertEqual(v['limb'], 2)

    def test_spdx_mentions_do_not_count_toward_the_limb_CONTROL(self):
        """Only the OMISSION grammars (CRAN, Odoo) make a bare token a positive grant.
        A bare SPDX token really is a silence and stays in p221's numerator."""
        v = g.verdict({'by_grammar': {'spdx': 900, 'unread': 900}})
        self.assertEqual(v['omission_grammar_bare_mentions'], 0)
        self.assertEqual(v['limb'], 2)




class TestDependencyScope(unittest.TestCase):
    """T224-3: the unit is the grant's SUBJECT, not the row sharing its line."""

    def test_dependency_licence_is_not_the_rows_grant_CONTROL(self):
        line = ('| [`CambridgeAssessmentResearch/KernEqWPS`](x) | `MIT` | read from '
                '`NAMESPACE`. **`Imports: MASS` = GPL-2 | GPL-3, and R itself is GPL** |')
        t = g.attribute([line], {'cambridgeassessmentresearch/kerneqwps': 'cran'})
        self.assertEqual(t['bare_attributed'], 0)
        self.assertEqual(t['dependency_scoped'], 2)
        self.assertEqual(t['by_grammar'], {})

    def test_vendored_grant_is_dependency_scoped_CONTROL(self):
        """ACTION RX's shape: Kolibri's wheel carries 80 vendored grants beside its own."""
        line = "| `learningequality/kolibri` | `MIT` | 80 vendored grants incl. GPL-3.0 |"
        t = g.attribute([line], {})
        self.assertEqual(t['dependency_scoped'], 1)
        self.assertEqual(t['bare_attributed'], 0)

    def test_the_rows_own_bare_grant_still_counts(self):
        line = "| `openeducat/openeducat_erp` | `LGPL-3.0` | Odoo ERP |"
        t = g.attribute([line], {'openeducat/openeducat_erp': 'odoo'})
        self.assertEqual(t['bare_attributed'], 1)
        self.assertEqual(t['dependency_scoped'], 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
