"""Tests for p147-scope-parity. Authored fixtures only; nothing is imported or executed."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scope_parity as S  # noqa: E402

SPECS = '''
TOOL_SPECS: list[ToolSpec] = [
    ToolSpec(name="list_courses", description="d", auth="public"),
    ToolSpec(name="ask_tutor", description="d"),
    ToolSpec(name="ingest_url_to_draft", description="d", auth="admin"),
]
'''
AUTH = '''
    return {
        "issuer": ISSUER,
        "scopes_supported": [
            "list_courses",
            "ask_tutor",
            "ingest_url_to_draft",
            WILDCARD_SCOPE,
        ],
    }
'''


class TestToolSpecs(unittest.TestCase):
    def test_names_and_auth_in_file_order(self):
        self.assertEqual(S.tool_specs(SPECS),
                         [("list_courses", "public"), ("ask_tutor", "user"),
                          ("ingest_url_to_draft", "admin")])

    def test_a_spec_omitting_auth_defaults_to_user(self):
        """🔴 Dropping it would under-count the posture census by one tool."""
        self.assertIn(("ask_tutor", "user"), S.tool_specs(SPECS))

    def test_no_tool_specs_is_empty_not_an_error(self):
        self.assertEqual(S.tool_specs("x = 1\n"), [])


class TestScopesSupported(unittest.TestCase):
    def test_wildcard_identifier_resolves_to_its_value(self):
        self.assertEqual(S.scopes_supported(AUTH),
                         ["list_courses", "ask_tutor", "ingest_url_to_draft", "*"])

    def test_missing_key_is_empty(self):
        self.assertEqual(S.scopes_supported("{}"), [])


class TestParity(unittest.TestCase):
    def setUp(self):
        self.tools = S.tool_specs(SPECS)
        self.scopes = S.scopes_supported(AUTH)

    def test_raw_equality_fails_and_that_is_correct(self):
        """🔴 `ACTION EG`'s test would fail on a correct repository."""
        p = S.parity(self.tools, self.scopes)
        self.assertFalse(p["equal_raw"])
        self.assertEqual((p["n_tools"], p["n_scopes"]), (3, 4))

    def test_equality_modulo_the_wildcard_holds(self):
        p = S.parity(self.tools, self.scopes)
        self.assertTrue(p["equal_modulo_wildcard"])
        self.assertEqual(p["scopes_without_tool"], [])
        self.assertEqual(p["tools_without_scope"], [])

    def test_a_scope_with_no_tool_is_caught(self):
        p = S.parity(self.tools, self.scopes + ["delete_everything"])
        self.assertFalse(p["equal_modulo_wildcard"])
        self.assertEqual(p["scopes_without_tool"], ["delete_everything"])

    def test_a_tool_with_no_scope_is_caught(self):
        """🟢 The direction lumen's own test already asserts, kept so both are pinned."""
        p = S.parity(self.tools + [("grade_review_card", "user")], self.scopes)
        self.assertFalse(p["equal_modulo_wildcard"])
        self.assertEqual(p["tools_without_scope"], ["grade_review_card"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
