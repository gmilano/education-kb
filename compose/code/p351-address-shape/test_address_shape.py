#!/usr/bin/env python3
"""p351 — offline controls for the address-shape filter.

Every control is a shape this base actually harvested onto its own shelves, or the
exact false-positive class that would make the filter unusable.  No network.

🔴 The direction of the risk, stated first: this filter REMOVES rows from a
denominator, so a wrong rejection silently shrinks the base every identity
instrument here is quoted against.  Every class below is therefore pinned in both
directions — the shape that must be rejected, and the real address nearest to it
that must survive.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from address_shape import classify, partition  # noqa: E402


class TheEightNonAddressesP350Found(unittest.TestCase):
    """p350's sample, which is what ZZ-an was registered on."""

    def test_navigation_paths_are_rejected(self):
        for p in ("topics/ai-tutor", "topics/education", "orgs/moodle",
                  "repos/moodle", "trending/python"):
            self.assertEqual(classify(p), "NAV-NAMESPACE", p)

    def test_the_readme_placeholder_is_rejected(self):
        self.assertEqual(classify("your-username/safetutors"), "PLACEHOLDER-OWNER")

    def test_a_real_address_whose_owner_merely_starts_with_a_nav_word(self):
        # 🔴 The false positive a prefix match would buy: these are repositories.
        self.assertIsNone(classify("topicsdb/curriculum"))
        self.assertIsNone(classify("userland/sandbox"))
        self.assertIsNone(classify("newrelic/k8s-metadata-injection"))


class BothArmsAreLoadBearing(unittest.TestCase):
    """🟡 The honest half: neither arm alone reaches all 33.

    The shape rule needs no foresight but cannot see a legal shape that is not a
    repository; the namespace list sees those but is complete only against the
    examples that prompted it.  This control pins the published split.
    """

    def test_a_legal_shape_can_still_be_a_namespace(self):
        # `topics/education` passes GitHub's owner AND name rules outright.
        from address_shape import NAME_SHAPE, OWNER_SHAPE
        self.assertTrue(OWNER_SHAPE.match("topics"))
        self.assertTrue(NAME_SHAPE.match("education"))
        # ...and is still not a repository.
        self.assertEqual(classify("topics/education"), "NAV-NAMESPACE")

    def test_an_illegal_shape_needs_no_list(self):
        # Nothing enumerated `...` or `git_user_id` in advance.
        from address_shape import NAV_NAMESPACES
        self.assertNotIn("...", NAV_NAMESPACES)
        self.assertNotIn("git_user_id", NAV_NAMESPACES)
        self.assertEqual(classify(".../blob"), "OWNER-ELLIDED")
        self.assertEqual(classify("git_user_id/git_repo_id"), "OWNER-TEMPLATE-VAR")

    def test_the_published_split_is_six_by_shape_and_twenty_seven_by_list(self):
        shape_classes = {"OWNER-ELLIDED", "OWNER-TEMPLATE-VAR", "EMPTY-NAME",
                         "EMPTY-OWNER", "OWNER-ILLEGAL", "NAME-ILLEGAL",
                         "NO-SEPARATOR"}
        list_classes = {"NAV-NAMESPACE", "PLACEHOLDER-OWNER", "PLACEHOLDER-NAME"}
        self.assertEqual(shape_classes & list_classes, set(),
                         "a class must be attributable to exactly one arm")


class TheFiveZZanCouldNotSee(unittest.TestCase):
    """🔴 ZZ-an prescribed `topics/`, `orgs/`, `repos/`, `trending/` and placeholder
    owners.  Run shelf-wide that rejects 28 of 33 and misses these five, in three
    classes."""

    def test_a_fifth_namespace_zzan_did_not_name(self):
        self.assertEqual(classify("search/repositories"), "NAV-NAMESPACE")
        # 🔴 And it is rejected by the LIST arm, so ZZ-an's miss here is not a
        # shape failure — it is the blacklist being complete only against its
        # own examples.
        from address_shape import NAV_NAMESPACES
        self.assertIn("search", NAV_NAMESPACES)
        for named_by_zzan in ("topics", "orgs", "repos", "trending"):
            self.assertIn(named_by_zzan, NAV_NAMESPACES)

    def test_an_ellided_owner_is_rejected_and_named_as_such(self):
        # Prose writing `github.com/.../blob/main/LICENSE` leaves this behind.
        for p in (".../archive", ".../blob", ".../releases"):
            self.assertEqual(classify(p), "OWNER-ELLIDED", p)

    def test_a_codegen_template_variable_is_rejected_and_named_as_such(self):
        # The swagger / openapi-generator placeholder.  Not a placeholder WORD,
        # so no list of `your-`/`example-` prefixes reaches it.
        self.assertEqual(classify("git_user_id/git_repo_id"), "OWNER-TEMPLATE-VAR")

    def test_the_two_classes_are_reported_apart(self):
        # A successor must be able to tell a broken URL from a template.
        self.assertNotEqual(classify(".../blob"), classify("git_user_id/git_repo_id"))


class DegenerateComponents(unittest.TestCase):
    def test_an_empty_name_is_rejected(self):
        self.assertEqual(classify("repos/"), "EMPTY-NAME")
        self.assertEqual(classify("topics/"), "EMPTY-NAME")

    def test_an_empty_owner_is_rejected(self):
        self.assertEqual(classify("/moodle"), "EMPTY-OWNER")

    def test_a_bare_name_with_no_separator_is_rejected(self):
        self.assertEqual(classify("moodle"), "NO-SEPARATOR")

    def test_a_dot_name_is_rejected(self):
        self.assertEqual(classify("someowner/."), "NAME-ILLEGAL")


class RealAddressesSurvive(unittest.TestCase):
    """🟢 The half that matters more: the shapes GitHub actually allows, including
    the awkward ones this base holds."""

    def test_plain_addresses_survive(self):
        for p in ("moodle/moodle", "openedx/edx-platform", "jtylek/epesicrm",
                  "withmarbleapp/os-taxonomy", "oaknational/oak-curriculum-ontology"):
            self.assertIsNone(classify(p), p)

    def test_a_name_with_dots_and_underscores_survives(self):
        # Legal in a repository NAME, illegal in an owner.  Both are held here.
        self.assertIsNone(classify("pykt-team/pykt_toolkit"))
        self.assertIsNone(classify("sakaiproject/sakai.2.9"))

    def test_a_single_character_owner_and_name_survive(self):
        self.assertIsNone(classify("a/b"))

    def test_a_thirty_nine_character_owner_survives_and_forty_does_not(self):
        self.assertIsNone(classify("a" * 39 + "/x"))
        self.assertEqual(classify("a" * 40 + "/x"), "OWNER-ILLEGAL")

    def test_an_interior_hyphen_survives_but_an_edge_hyphen_does_not(self):
        self.assertIsNone(classify("gego-k12/gegok12"))
        self.assertEqual(classify("-lead/x"), "OWNER-ILLEGAL")
        self.assertEqual(classify("trail-/x"), "OWNER-ILLEGAL")

    def test_a_numeric_owner_survives(self):
        self.assertIsNone(classify("1edtech/openbadges-validator-core"))


class PartitionIsATotalSplit(unittest.TestCase):
    def test_every_harvested_shape_lands_in_exactly_one_side(self):
        idx = {"moodle/moodle": {"moodle/moodle"},
               "topics/education": {"topics/education"},
               ".../blob": {".../blob"},
               "a/b": {"a/b"}}
        addresses, rejected = partition(idx)
        self.assertEqual(len(addresses) + len(rejected), len(idx))
        self.assertEqual(addresses & set(rejected), set())
        self.assertEqual(addresses, {"moodle/moodle", "a/b"})


class TheRefusalP541Requires(unittest.TestCase):
    def test_no_input_is_refused_rather_than_answered(self):
        from address_shape import main
        self.assertEqual(main([]), 2)
        self.assertEqual(main(["census"]), 2)
        self.assertEqual(main(["reject"]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
