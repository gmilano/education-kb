#!/usr/bin/env python3
"""p423 -- controls for the declaration contract.

Every control is a statement measured against this base's real Makefile and real register,
or a fixture built to make one arm fire.  The load-bearing one is
`test_an_undeclared_red_gate_is_not_quietly_excused`: the whole point of this instrument is
that quieting a gate has to cost a registered gap.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import commit_gate as cg  # noqa: E402

PASS = FAIL = 0


class Parser(unittest.TestCase):
    def test_a_list_variable_is_read_across_backslash_continuations(self):
        text = "HOOK_GATES = gate-a gate-b \\\n             gate-c \\\n             gate-d\n\nnext:\n"
        self.assertEqual(cg._makefile_list("HOOK_GATES", text),
                         ["gate-a", "gate-b", "gate-c", "gate-d"])

    def test_an_absent_variable_is_empty_not_an_error(self):
        self.assertEqual(cg._makefile_list("NOPE", "HOOK_GATES = gate-a\n\nx:\n"), [])

    def test_the_parser_stops_at_the_next_recipe(self):
        text = "HOOK_GATES = gate-a\n\nsome-target: ## doc\n\tgate-should-not-be-read\n"
        self.assertEqual(cg._makefile_list("HOOK_GATES", text), ["gate-a"])

    def test_recount_is_kept_because_the_real_list_carries_it(self):
        # `recount` is in HOOK_GATES and is not named `gate-*`; dropping it would
        # under-count the blocking set and the gate would be measuring the wrong suite.
        self.assertIn("recount", cg._makefile_list("HOOK_GATES",
                      "HOOK_GATES = gate-offline recount gate-tables\n\nx:\n"))


class LiveMakefile(unittest.TestCase):
    def test_the_live_lists_load_and_are_not_empty(self):
        """🔴 The zero-denominator control.  A parser that silently returns [] makes this
        gate green for the same reason a correct run is green, which is the class
        `gate-backlog-denominator` exists for and which `p423` tripped over once already
        in `fold_identity`'s register loader."""
        hooks, red = cg.read_sets()
        self.assertGreater(len(hooks), 40, "HOOK_GATES did not parse")
        self.assertEqual(red, ["gate-census-union"])

    def test_the_blocking_set_is_the_hook_set_minus_the_declared_reds(self):
        hooks, red = cg.read_sets()
        self.assertEqual(sorted(cg.blocking_set()), sorted(set(hooks) - set(red)))
        self.assertEqual(len(cg.blocking_set()), len(hooks) - len(red))

    def test_this_instrument_is_itself_in_the_blocking_set(self):
        """🟢 So the declaration cannot be widened quietly by the same commit it guards."""
        self.assertIn("gate-commit-gate", cg.blocking_set())

    def test_the_live_declaration_is_registered(self):
        """🟢 `Gap 400-B` cites `gate-census-union` by name in `intel/open-gaps.md`."""
        self.assertEqual(cg.gate(), [])

    def test_the_deliberate_red_is_NOT_in_the_blocking_set(self):
        """🔴 The finding this instrument was built from: `make hooks` has exited non-zero
        since `p398`, so it could never have blocked a commit."""
        self.assertNotIn("gate-census-union", cg.blocking_set())


class Contract(unittest.TestCase):
    def _root(self, makefile, register):
        d = tempfile.mkdtemp()
        os.makedirs(os.path.join(d, "intel"))
        with open(os.path.join(d, "Makefile"), "w", encoding="utf-8") as fh:
            fh.write(makefile)
        with open(os.path.join(d, "intel", "open-gaps.md"), "w", encoding="utf-8") as fh:
            fh.write(register)
        return d

    def test_an_undeclared_red_gate_is_not_quietly_excused(self):
        """🔴 THE load-bearing control: a gate carried red with nothing registered."""
        d = self._root("HOOK_GATES = gate-a gate-b\n\nDECLARED_RED = gate-b\n\nx:\n",
                       "nothing registered here\n")
        rows = cg.gate(d)
        self.assertEqual([r[1] for r in rows], ["P423-UNREGISTERED-RED"])
        self.assertEqual(rows[0][2], "gate-b")

    def test_a_registered_declaration_passes(self):
        d = self._root("HOOK_GATES = gate-a gate-b\n\nDECLARED_RED = gate-b\n\nx:\n",
                       "| `Gap 400-B` | gate-b is red on purpose |\n")
        self.assertEqual(cg.gate(d), [])

    def test_a_citation_without_a_gap_id_is_not_a_registration(self):
        """🟡 Prose mentioning the gate is not a registration — the register has to carry
        a gap id, because that is what a later pass can close."""
        d = self._root("HOOK_GATES = gate-a gate-b\n\nDECLARED_RED = gate-b\n\nx:\n",
                       "gate-b is red and we know about it\n")
        self.assertEqual([r[1] for r in cg.gate(d)], ["P423-UNREGISTERED-RED"])

    def test_declaring_a_gate_the_suite_does_not_run_is_its_own_finding(self):
        d = self._root("HOOK_GATES = gate-a\n\nDECLARED_RED = gate-zzz\n\nx:\n",
                       "| `Gap 1-A` | gate-zzz |\n")
        self.assertEqual([r[1] for r in cg.gate(d)], ["P423-UNDECLARED-RED"])

    def test_no_declared_red_is_green(self):
        d = self._root("HOOK_GATES = gate-a gate-b\n\nx:\n", "")
        self.assertEqual(cg.gate(d), [])
        self.assertEqual(sorted(cg.blocking_set(d)), ["gate-a", "gate-b"])


class CloneSurvival(unittest.TestCase):
    def test_the_installed_state_is_a_census_and_names_its_remedy(self):
        """🟡 Gap 423-B: `git clone` does not copy `.git/hooks`, so the installed
        state is per-working-copy and is REPORTED, never gated — a fresh clone must not go
        red for a file git never gave it."""
        ok, why = cg.hook_installed()
        self.assertIsInstance(ok, bool)
        if not ok:
            self.assertIn("install-hooks", why)

    def test_the_hook_script_itself_is_in_the_tree_and_runs_the_blocking_suite(self):
        """🟢 What DOES survive a clone: the script.  Gated, because it is a file."""
        p = os.path.join(cg.ROOT, "ingest", "pre-commit")
        self.assertTrue(os.path.exists(p), "ingest/pre-commit is missing")
        with open(p, encoding="utf-8") as fh:
            body = fh.read()
        self.assertIn("commit-gates", body)
        self.assertIn("SKIP_COMMIT_GATES", body)


if __name__ == "__main__":
    unittest.main(verbosity=2)
