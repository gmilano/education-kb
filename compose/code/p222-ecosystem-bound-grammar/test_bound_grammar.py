"""Tests for p222's ecosystem-grammar reading. 5 of the 28 are CONTROLS that must
not fire: the instrument's whole claim is that the same token means different
things in different grammars, so a test suite that only checked the new readings
would also pass if the module simply answered `only` everywhere."""

import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bound_grammar import (read_bound, reconcile, grammar_for,
                           blocks_gpl3_host, GRAMMARS)

# The verbatim grant header shipped in openeducat_core/__manifest__.py, read
# first-hand on 2026-10-15 via raw.githubusercontent.com.
OPENEDUCAT_HEADER = (
    "#    it under the terms of the GNU Lesser General Public License as\n"
    "#    published by the Free Software Foundation, either version 3 of the\n"
    "#    License, or (at your option) any later version.\n")


class TheSameTokenInFourGrammars(unittest.TestCase):
    """The claim. `LGPL-3` is not one state."""

    def test_spdx_bare_token_says_nothing(self):
        self.assertEqual(read_bound('LGPL-3', 'spdx')['bound'], 'unspecified')

    def test_cran_bare_token_is_a_positive_only(self):
        self.assertEqual(read_bound('LGPL-3', 'cran')['bound'], 'only')

    def test_odoo_bare_token_is_a_positive_only(self):
        self.assertEqual(read_bound('LGPL-3', 'odoo')['bound'], 'only')

    def test_cran_range_form_is_or_later(self):
        r = read_bound('GPL (>= 2)', 'cran')
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('GPL', '2.0', 'or-later'))

    def test_odoo_spelled_out_later_form(self):
        r = read_bound('LGPL-3 or any later version', 'odoo')
        self.assertEqual(r['bound'], 'or-later')

    def test_cran_disjunction_is_neither_bound(self):
        # `GPL-2 | GPL-3` offers a CHOICE of grants. Collapsing it onto a bound
        # would publish a licence the package never offered.
        self.assertEqual(read_bound('GPL-2 | GPL-3', 'cran')['bound'],
                         'disjunction')


class RealValuesReadThisPass(unittest.TestCase):
    """Every value here was read first-hand on 2026-10-15."""

    def test_overhangio_tutor_is_agpl_only(self):
        r = read_bound('AGPL-3.0-only', 'spdx')
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('AGPL', '3.0', 'only'))

    def test_oat_sa_tao_core_is_gpl2_only(self):
        r = read_bound('GPL-2.0-only', 'spdx')
        self.assertTrue(blocks_gpl3_host(r['family'], r['version'], r['bound']))

    def test_nvda_classifier_plus_is_or_later(self):
        r = read_bound('License :: OSI Approved :: GNU General Public '
                       'License v2 or later (GPLv2+)', 'classifier')
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('GPL', '2.0', 'or-later'))

    def test_tutor_classifier_without_plus_is_only(self):
        # overhangio/tutor ships BOTH: `license = {text = "AGPL-3.0-only"}` and
        # this classifier. They agree, and that agreement is what makes the
        # `AGPL-3.0-only` reading safe to publish.
        r = read_bound('License :: OSI Approved :: GNU Affero General Public '
                       'License v3', 'classifier')
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('AGPL', '3.0', 'only'))

    def test_openeducat_manifest_field(self):
        self.assertEqual(read_bound("'LGPL-3'", 'odoo')['bound'], 'only')

    def test_openeducat_header_is_or_later(self):
        r = read_bound(OPENEDUCAT_HEADER, 'prose')
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('LGPL', '3.0', 'or-later'))

    def test_dexter_cran_description_value(self):
        r = read_bound('LGPL-3', 'cran')
        self.assertEqual((r['family'], r['bound']), ('LGPL', 'only'))

    def test_ilias_value_is_not_a_valid_spdx_id_at_all(self):
        # ILIAS composer.json says `"GPL v3"` and INGInious's pyproject says
        # `"AGPL 3"`. Composer and PEP 621 both mandate an SPDX expression in
        # that field and neither string is one. The honest reading is that the
        # field is UNREADABLE as SPDX - not that it carries a bare bound - so
        # `gnu` comes back False and the row stays ungranted by this channel.
        for v in ('GPL v3', 'AGPL 3', 'GPL version 3'):
            self.assertFalse(read_bound(v, 'spdx')['gnu'], v)
        # ...and the same string DOES resolve when read as the prose it is.
        self.assertEqual(read_bound('GPL v3', 'prose')['family'], 'GPL')

    def test_citolab_gplv3_spelling(self):
        # `"GPLv3"` in package.json: the SPDX regex needs the hyphen, so this is
        # not an SPDX id at all and must not be read as one.
        self.assertFalse(read_bound('GPLv3', 'spdx')['gnu'])


class Reconciliation(unittest.TestCase):

    def test_openeducat_two_channels_are_a_range_conflict(self):
        v = reconcile([('__manifest__.py', "'LGPL-3'"),
                       ('version.php', OPENEDUCAT_HEADER)])
        self.assertEqual(v['state'], 'RANGE-CONFLICT')

    def test_moodle_plugin_single_channel_resolves(self):
        v = reconcile([('version.php',
                        'GNU General Public License as published by the Free '
                        'Software Foundation, either version 3 of the License, '
                        'or (at your option) any later version.')])
        self.assertEqual((v['state'], v['bound']), ('AGREE', 'or-later'))

    def test_classroomio_manifest_vs_licence_is_not_in_scope_here(self):
        # package.json `"MIT"` is not GNU, so this instrument says NO-GNU-CHANNEL
        # rather than inventing a conflict. The MIT-vs-AGPL finding is a FAMILY
        # question and belongs to p220's instrument, not this one.
        v = reconcile([('package.json', 'MIT')])
        self.assertEqual(v['state'], 'NO-GNU-CHANNEL')

    def test_unspecified_at_source(self):
        v = reconcile([('composer.json', 'GPL-3.0'), ('package.json', 'GPL-3.0')])
        self.assertEqual(v['state'], 'UNSPECIFIED-AT-SOURCE')

    def test_bound_resolved_when_one_channel_speaks(self):
        v = reconcile([('composer.json', 'GPL-3.0'),
                       ('pyproject.toml', 'GPL-3.0-or-later')])
        self.assertEqual((v['state'], v['bound']), ('BOUND-RESOLVED', 'or-later'))

    def test_grant_conflict_on_version(self):
        v = reconcile([('composer.json', 'GPL-2.0-or-later'),
                       ('package.json', 'GPL-3.0-or-later')])
        self.assertEqual(v['state'], 'GRANT-CONFLICT')

    def test_grammar_for_known_and_unknown_channels(self):
        self.assertEqual(grammar_for('DESCRIPTION'), 'cran')
        self.assertEqual(grammar_for('__manifest__.py'), 'odoo')
        self.assertIsNone(grammar_for('README.md'))


class GplThreeHostCompatibility(unittest.TestCase):

    def test_gpl2_only_is_blocked(self):
        self.assertIs(blocks_gpl3_host('GPL', '2.0', 'only'), True)

    def test_gpl3_only_is_fine(self):
        self.assertIs(blocks_gpl3_host('GPL', '3.0', 'only'), False)

    def test_or_later_is_always_fine(self):
        self.assertIs(blocks_gpl3_host('GPL', '2.0', 'or-later'), False)

    def test_lgpl_only_links_into_a_v3_host(self):
        self.assertIs(blocks_gpl3_host('LGPL', '2.1', 'only'), False)

    def test_unspecified_is_unknown_not_optimistic(self):
        self.assertIsNone(blocks_gpl3_host('GPL', '2.0', 'unspecified'))


class Controls(unittest.TestCase):
    """Five tests that must NOT fire. Without them an instrument that answered
    `only` everywhere, or `gnu=True` everywhere, would pass the suite above."""

    def test_control_mit_is_not_gnu_in_any_grammar(self):
        for g in GRAMMARS:
            self.assertFalse(read_bound('MIT', g)['gnu'], g)

    def test_control_cran_mit_idiom_is_not_gnu(self):
        # `MIT + file LICENSE` is R's standard idiom and appears on 5 rows here.
        self.assertFalse(read_bound('MIT + file LICENSE', 'cran')['gnu'])

    def test_control_odoo_proprietary_members_are_out_of_scope(self):
        for v in ('OEEL-1', 'OPL-1', 'Other proprietary',
                  'Other OSI approved licence'):
            self.assertFalse(read_bound(v, 'odoo')['gnu'], v)

    def test_control_empty_and_none_are_not_grants(self):
        for v in ('', None, '   '):
            self.assertFalse(read_bound(v, 'spdx')['gnu'], repr(v))

    def test_control_unknown_grammar_raises_rather_than_guessing(self):
        with self.assertRaises(ValueError):
            read_bound('GPL-3.0', 'maven-ish')


if __name__ == '__main__':
    unittest.main(verbosity=1)
