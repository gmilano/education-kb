#!/usr/bin/env python3
"""Discrimination tests for two_channel.py - offline, injected channels.

These are not smoke tests. Each asserts that the gate SEPARATES two cases that
a single-channel method collapses, using the real p331 measurements.
"""
import unittest

from two_channel import gate, verdict


class TestDissociation(unittest.TestCase):
    """The ltijs/pylti1.3 pair is the whole reason this module exists."""

    def test_ltijs_alive_despite_stale_tags(self):
        # git tags stop at v5.9.5 2024-05-01; npm says 7.0.7 2026-10-06
        self.assertEqual(
            verdict("Cvmcosta/ltijs", pkg="ltijs", registry="npm",
                    git_ok=True, release=("7.0.7", "2026-10-06")),
            "GRADED:7.0.7@2026-10-06")

    def test_pylti13_dead_on_both(self):
        self.assertEqual(
            verdict("dmitry-viskov/pylti1.3", pkg="PyLTI1p3", registry="pypi",
                    git_ok=True, release=("2.0.0", "2022-11-20")),
            "GRADED:2.0.0@2022-11-20")

    def test_the_two_are_distinguishable(self):
        """A single-channel method called both abandoned. This one does not."""
        live = verdict("Cvmcosta/ltijs", pkg="ltijs", registry="npm",
                       git_ok=True, release=("7.0.7", "2026-10-06"))
        dead = verdict("dmitry-viskov/pylti1.3", pkg="PyLTI1p3", registry="pypi",
                       git_ok=True, release=("2.0.0", "2022-11-20"))
        self.assertNotEqual(live, dead)


class TestUnpublished(unittest.TestCase):
    def test_ltikit_sdk_alive_on_git_absent_from_npm(self):
        self.assertEqual(
            verdict("Liberate-Labs/ltikit-sdk", pkg="ltikit-sdk", registry="npm",
                    git_ok=True, release=None),
            "UNPUBLISHED")

    def test_unpublished_is_not_noref(self):
        self.assertNotEqual(
            verdict("Liberate-Labs/ltikit-sdk", pkg="ltikit-sdk", registry="npm",
                    git_ok=True, release=None),
            "NO-REF")


class TestControls(unittest.TestCase):
    def test_bogus_slug_is_noref(self):
        self.assertEqual(verdict("bogus-control-p331/zz", git_ok=False), "NO-REF")

    def test_unpackaged_row_grades_on_one_channel_legitimately(self):
        """os-taxonomy ships no package; the citing channel is the whole story."""
        self.assertEqual(
            verdict("withmarbleapp/os-taxonomy", git_ok=True),
            "ALIVE-CITING-ONLY")


class TestGate(unittest.TestCase):
    def test_gate_blocks_single_channel_packaged_row(self):
        rows = [{"slug": "Cvmcosta/ltijs", "pkg": "ltijs", "release": None}]
        self.assertEqual(gate(rows), ["Cvmcosta/ltijs"])

    def test_gate_passes_two_channel_row(self):
        rows = [{"slug": "Cvmcosta/ltijs", "pkg": "ltijs",
                 "release": ("7.0.7", "2026-10-06")}]
        self.assertEqual(gate(rows), [])

    def test_gate_ignores_unpackaged_row(self):
        rows = [{"slug": "withmarbleapp/os-taxonomy", "pkg": None, "release": None}]
        self.assertEqual(gate(rows), [])

    def test_gate_names_every_offender(self):
        rows = [{"slug": "a/b", "pkg": "p1", "release": None},
                {"slug": "c/d", "pkg": "p2", "release": "-"},
                {"slug": "e/f", "pkg": None, "release": None}]
        self.assertEqual(gate(rows), ["a/b", "c/d"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
