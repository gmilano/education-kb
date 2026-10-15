"""p220 tests. Fixtures are verbatim readings taken on 2026-10-15 over
raw.githubusercontent.com, registry.npmjs.org and proxy.golang.org.

Three tests are CONTROLS that must NOT fire: a row whose channels agree must not be
reported as a conflict, a registry record that does point back at its slug must pass the
identity gate, and an ecosystem whose field is merely optional must not be called a defect
when the field is missing.
"""
import unittest

from file_grant import prescription, identity_ok, file_vs_repo, verdict


class PrescriptionTest(unittest.TestCase):
    def test_moodle_is_prescribed_so_asking_is_premature(self):
        p = prescription('moodle')
        self.assertEqual(p['verdict'], 'PRESCRIBED-CHANNEL')
        self.assertTrue(p['asking_is_premature'])
        self.assertIn('version.php', p['read'])

    def test_npm_is_permissive_not_prescribed(self):
        # CONTROL. CreveXTech/canvas-lms-mcp, tianshuo/trainingllm and barneslardo/sis-demo
        # all have a readable package.json with no `license` key. That is npm behaving
        # normally, not three broken repos: the instrument must not call it a defect.
        p = prescription('npm')
        self.assertEqual(p['verdict'], 'PERMISSIVE-MANIFEST')
        self.assertFalse(p['asking_is_premature'])

    def test_go_declares_no_licence_field_at_all(self):
        # haanhtuandev/vgu-mcp: go.mod carries a module path and requirements, never a
        # licence. pkg.go.dev -> 404, so Go's own detector has nothing either.
        self.assertEqual(prescription('go')['verdict'], 'NO-CHANNEL')

    def test_unknown_ecosystem_degrades_to_no_channel(self):
        # mabdulre9/electrical-engineering is a curated link list: no manifest of any kind.
        self.assertEqual(prescription('')['verdict'], 'NO-CHANNEL')


class IdentityGateTest(unittest.TestCase):
    NPM_CANVAS = {
        'name': 'canvas-lms-mcp',
        'license': 'MIT',
        'repository': {'type': 'git',
                       'url': 'git+https://github.com/bruchris/canvas-lms-mcp.git'},
    }

    def test_registry_grant_is_refused_for_a_different_owner(self):
        # T220-3. The shelf row CreveXTech/canvas-lms-mcp declares npm name
        # `canvas-lms-mcp`; the registry record for that name belongs to bruchris.
        self.assertFalse(identity_ok(self.NPM_CANVAS, 'CreveXTech/canvas-lms-mcp'))

    def test_registry_grant_is_accepted_for_the_owner_it_names(self):
        # CONTROL: the gate must not refuse the row the record actually describes.
        self.assertTrue(identity_ok(self.NPM_CANVAS, 'bruchris/canvas-lms-mcp'))

    def test_record_without_repository_is_unattributable(self):
        self.assertFalse(identity_ok({'license': 'MIT'}, 'bruchris/canvas-lms-mcp'))


class FileVsRepoTest(unittest.TestCase):
    def test_scorm_wrapper_file_is_narrower_than_its_readme(self):
        # T220-1. README `## License` quotes Apache-2.0 in full. The two files the project
        # tells you to drop into every SCO carry, in their own headers, a custom ADL
        # non-disparagement grant AND CC BY-SA 3.0. SCORMToXAPIFunctions.js carries none.
        self.assertEqual(
            file_vs_repo('Apache-2.0', {
                'SCORM2004/APIWrapper.js': 'CC-BY-SA-3.0',
                'SCORM1.2/APIWrapper.js': 'CC-BY-SA-3.0',
                'SCORMToXAPIFunctions.js': None,
            }),
            'FILE-NARROWER')

    def test_microsoft_moodle_plugin_file_is_narrower_than_its_license(self):
        # T220-2. Root LICENSE is MIT; local/aichat/version.php carries the Moodle GPL
        # header and `@license ... GNU GPL v3 or later`.
        self.assertEqual(
            file_vs_repo('MIT', {'local/aichat/version.php': 'GPL-3.0-or-later'}),
            'FILE-NARROWER')

    def test_moodle_row_whose_channels_agree_is_not_a_conflict(self):
        # CONTROL. saylordotorg/moodle-local_ai_course_assistant: LICENSE 35 149 B GPLv3
        # and version.php `@license ... GNU GPL v3 or later`. Must come back AGREE.
        self.assertEqual(
            file_vs_repo('GPL-3.0-or-later',
                         {'version.php': 'GPL-3.0-or-later', 'LICENSE': 'GPL-3.0-or-later'}),
            'AGREE')

    def test_repo_silent_file_answers(self):
        # yedidiaklein/moodle-local_aiquestions has no root LICENSE; version.php answers.
        self.assertEqual(
            file_vs_repo(None, {'version.php': 'GPL-3.0-or-later'}), 'REPO-SILENT')

    def test_nothing_anywhere_is_undetermined(self):
        self.assertEqual(file_vs_repo(None, {}), 'UNDETERMINED')


class VerdictTest(unittest.TestCase):
    def test_disagreement_blocks_reliance_on_either_grant(self):
        v = verdict('adl-scorm', 'Apache-2.0',
                    {'SCORM2004/APIWrapper.js': 'CC-BY-SA-3.0'})
        self.assertEqual(v['comparison'], 'FILE-NARROWER')
        self.assertIn('disagree', v['rely_on'])

    def test_permissive_manifest_with_empty_field_is_a_genuine_PH_lead(self):
        v = verdict('npm', None, {}, None, 'tianshuo/trainingllm')
        self.assertEqual(v['prescription'], 'PERMISSIVE-MANIFEST')
        self.assertIn('ACTION PH', v['next'])

    def test_prescribed_channel_unread_says_read_before_asking(self):
        v = verdict('moodle', None, None, None, 'bycs-lp/moodle-block_ai_chat')
        self.assertIn('version.php', v['next'])
        self.assertIn('premature', v['next'])


if __name__ == '__main__':
    unittest.main()
