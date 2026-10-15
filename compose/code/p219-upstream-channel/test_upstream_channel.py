#!/usr/bin/env python3
"""The four rows p219 adjudicated by hand, as regression fixtures.

Two of them are the cases a token grep gets wrong, and they are the reason this
file exists. Excerpts are verbatim from the bodies read on 2026-10-15 over
raw.githubusercontent.com/<slug>/HEAD/README.md.
"""
import unittest
from upstream_channel import relation, upstream, channels, verdict

TUTOR_LMS_MCP = """# Tutor LMS MCP Server - WordPress Plugin

A WordPress plugin that turns your Tutor LMS site into a live MCP server,
## Installation
2. Go to **WordPress Admin -> Plugins -> Add New -> Upload Plugin**
3. Upload the zip and click **Install Now -> Activate**
This plugin uses **OAuth 2.0 with PKCE** - Claude.ai handles the full login flow automatically:
"""

LOYANIU_MOODLE_MCP = """# moodle-mcp
2. Assume you have `uv` installed, run `uv add "mcp[cli]"` to install the MCP CLI tools
3. Run `mcp install main.py -f .env` to add the moodle-mcp server to Claude app
        "MOODLE_URL": "https://{your-moodle-url}/webservice/rest/server.php",
1. Navigate to your Moodle token management page `https://{your-moodle-url}/user/managetoken.php`
"""

ONBIRDEV = """# Moodle MCP Web Service Plugin

A Moodle web service plugin that implements the **Model Context Protocol (MCP)**.
### Method 1: Via Moodle Plugin Directory (Recommended)
1. Visit **Site administration -> Plugins -> Install plugins**
3. The plugin will be installed as `webservice_mcp`
https://your-moodle-site.com/webservice/mcp/server.php?wstoken=YOUR_TOKEN
"""

AI_MMS = """**Tertiary Courses LMS** is a complete, production-grade course-registration and
learning-management platform built on OpenMage 1.x (Magento 1 LTS).
[![OpenMage](https://img.shields.io/badge/OpenMage-LTS%20v20.12.0-f46f25)](https://www.openmage.org/)
"""

BLACKBOARD = """# blackboard-mcp
An MCP server that connects Claude to Blackboard Learn (Aula Virtual).
Browse courses, check grades. Set your API token in .env.
"""


class TheTwoCasesATokenGrepGetsWrong(unittest.TestCase):

    def test_tutor_lms_mcp_is_a_derivative_despite_saying_mcp_server_and_oauth(self):
        # UNDER-FIRE case: "MCP server" + "OAuth" would read as INTEGRATION.
        # Its first line says WordPress Plugin and it installs into wp-content.
        self.assertEqual(relation(TUTOR_LMS_MCP, 'Hesham0-0Nasser/tutor-lms-mcp'), 'DERIVATIVE')
        v = verdict(TUTOR_LMS_MCP, 'Hesham0-0Nasser/tutor-lms-mcp')
        self.assertEqual(v['upstream'], 'WordPress')
        self.assertEqual(v['reciprocity'], 'RECIPROCAL')
        # and the channel it names is the one that actually held the grant
        self.assertIn('tutor-lms-mcp.php', v['read_first'])
        self.assertIn('readme.txt', v['read_first'])

    def test_loyaniu_moodle_mcp_is_an_integration_despite_the_moodle_slug_prefix(self):
        # OVER-FIRE case: the slug begins `moodle-`, which a prefix rule treats as a plugin.
        self.assertEqual(relation(LOYANIU_MOODLE_MCP, 'loyaniu/moodle-mcp'), 'INTEGRATION')
        v = verdict(LOYANIU_MOODLE_MCP, 'loyaniu/moodle-mcp')
        self.assertEqual(v['upstream'], 'Moodle')
        self.assertEqual(v['read_first'], [])
        self.assertIn('does NOT reach this work', v['instruction'])


class TheRowsThatWereAlreadyRight(unittest.TestCase):

    def test_onbirdev_is_a_moodle_plugin_and_version_php_is_named_first(self):
        v = verdict(ONBIRDEV, 'onbirdev/moodle-webservice_mcp')
        self.assertEqual(v['relation'], 'DERIVATIVE')
        self.assertEqual(v['upstream'], 'Moodle')
        # p187 recovered the grant from exactly these two files
        self.assertEqual(v['read_first'][:2], ['version.php', 'lib.php'])

    def test_ai_mms_is_vendored_openmage_and_composer_json_is_named_first(self):
        v = verdict(AI_MMS, 'alfredang/ai-mms')
        self.assertEqual(v['upstream'], 'OpenMage/Magento-1')
        self.assertEqual(v['reciprocity'], 'NET-RECIPROCAL')
        self.assertEqual(v['relation'], 'DERIVATIVE')
        self.assertEqual(v['read_first'][0], 'composer.json')


class ReciprocityIsNotTheOnlyRisk(unittest.TestCase):

    def test_a_proprietary_api_row_is_not_a_licence_gap(self):
        v = verdict(BLACKBOARD, 'P1ckle3/blackboard-mcp')
        self.assertEqual(v['reciprocity'], 'PROPRIETARY-API')
        self.assertIn('VENDOR API TERMS', v['instruction'])
        self.assertIn('not a licence', v['instruction'])


class ControlsThatMustNotFire(unittest.TestCase):

    def test_an_ecl_upstream_carries_no_reciprocity(self):
        # ECL-2.0 is Apache-derived. p200/p216 established this; it must not be
        # swept up as copyleft just because Sakai is an LMS.
        name, lic, rec = upstream('Built as a Sakai tool, see the Sakai developer guide.')
        self.assertEqual(name, 'Sakai')
        self.assertEqual(lic, 'ECL-2.0')
        self.assertEqual(rec, 'PERMISSIVE')

    def test_no_upstream_named_leaves_the_row_untouched(self):
        v = verdict('A PyTorch knowledge-tracing baseline. Run `python train.py`.', 'yxonic/DTransformer')
        self.assertIsNone(v['upstream'])
        self.assertIn('ordinary ACTION PH lead', v['instruction'])

    def test_channels_substitutes_the_repo_name_into_the_wordpress_main_file(self):
        self.assertIn('tutor-lms-mcp.php', channels('WordPress', 'Hesham0-0Nasser/tutor-lms-mcp'))
        self.assertIn('learnpress.php', channels('WordPress', 'LearnPress/learnpress'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
