#!/usr/bin/env python3
"""Controls for `p349-name-collision` — the pre-filter, its DECLARED blind spot, and the
alias gate's two findings.

The blind spot is asserted as a test on purpose (`C5`). A cost reduction with a known
hole is honest; the same reduction with the hole left in prose becomes, one pass later, a
proof of absence. A test is the only form of that sentence a successor cannot skip.
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from name_collision import harvest, name_groups  # noqa: E402
from alias_gate import gate, read_register  # noqa: E402

REGISTER = (
    "group\taddress\tstate\thead\tchannel\tlive_shelf_files\n"
    "demo\tcanon-org/demo\tCANONICAL\tabc123\tsearch-index-full_name\t—\n"
    "demo\told-user/demo\tSTALE\tabc123\tsearch-index-full_name\t—\n"
    "nocanon\ta-org/nocanon\tUNKNOWN\tdef456\thead-equality-only\t—\n"
    "nocanon\tb-org/nocanon\tUNKNOWN\tdef456\thead-equality-only\t—\n"
)


def write(tmp, name, text):
    p = os.path.join(tmp, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text)
    return p


class PreFilter(unittest.TestCase):
    def groups_of(self, text):
        with tempfile.TemporaryDirectory() as tmp:
            return name_groups(harvest([write(tmp, "s.md", text)]))

    def test_C1_two_owners_one_name_is_a_group(self):
        g = self.groups_of("github.com/a/thing and github.com/b/thing\n")
        self.assertEqual(sorted(g["thing"]), ["a/thing", "b/thing"])

    def test_C2_one_owner_is_not_a_group(self):
        self.assertEqual(self.groups_of("github.com/a/thing only\n"), {})

    def test_C3_casing_is_folded_before_grouping(self):
        # `A/Thing` and `a/thing` are ONE owner — p348's axis, not this one.
        self.assertEqual(self.groups_of("github.com/A/Thing github.com/a/thing\n"), {})

    def test_C4_three_owners_are_one_group_of_three(self):
        g = self.groups_of("github.com/a/x github.com/b/x github.com/c/x\n")
        self.assertEqual(len(g["x"]), 3)

    def test_C5_DECLARED_BLIND_SPOT_renamed_transfer_is_invisible(self):
        # One repository, transferred AND renamed. The pre-filter cannot see it; only a
        # payload digest (`p349-payload-digest`) or the full 2 462-probe run can.
        self.assertEqual(self.groups_of("github.com/old/alpha github.com/new/beta\n"), {})

    def test_C6_templates_are_not_addresses(self):
        self.assertEqual(self.groups_of("github.com/owner/repo github.com/org/repo\n"), {})

    def test_C7_refuses_empty_argument_list(self):
        r = subprocess.run([sys.executable, "-I",
                            os.path.join(HERE, "name_collision.py"), "census"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        self.assertIn("refusing", r.stderr)


class AliasGate(unittest.TestCase):
    def findings(self, shelf_text):
        with tempfile.TemporaryDirectory() as tmp:
            reg = write(tmp, "reg.tsv", REGISTER)
            return gate(reg, [write(tmp, "shelf.md", shelf_text)])

    def test_C8_stale_address_alone_is_a_finding(self):
        f = self.findings("## Pass 1\n\nrow: github.com/old-user/demo\n")
        self.assertEqual([x[1] for x in f], ["P349-STALE-ADDRESS"])

    def test_C9_canonical_address_alone_is_clean(self):
        self.assertEqual(self.findings("## Pass 1\n\nrow: github.com/canon-org/demo\n"), [])

    def test_C10_both_addresses_is_a_double_count_and_a_stale_row(self):
        f = self.findings("## Pass 1\n\nrow A: github.com/canon-org/demo\n"
                          "row B: github.com/old-user/demo\n")
        self.assertEqual(sorted(x[1] for x in f),
                         ["P349-ALIAS-DOUBLE-COUNT", "P349-STALE-ADDRESS"])

    def test_C11_stale_named_BESIDE_its_canonical_on_one_line_is_excused(self):
        self.assertEqual(self.findings(
            "## Pass 1\n\ngithub.com/old-user/demo is a stale address of "
            "github.com/canon-org/demo\n"), [])

    def test_C12_the_STALE_token_excuses_it_too(self):
        self.assertEqual(self.findings(
            "## Pass 1\n\ngithub.com/old-user/demo — STALE, see the register\n"), [])

    def test_C13_a_group_with_no_canonical_is_still_a_double_count(self):
        f = self.findings("## Pass 1\n\ngithub.com/a-org/nocanon and github.com/b-org/nocanon\n")
        self.assertEqual([x[1] for x in f], ["P349-ALIAS-DOUBLE-COUNT"])

    def test_C14_history_below_the_second_pass_heading_is_not_judged(self):
        self.assertEqual(self.findings(
            "## Pass 2\n\nclean: github.com/canon-org/demo\n\n"
            "## Pass 1\n\ninherited: github.com/old-user/demo\n"), [])

    def test_C15_register_reads_state_and_canonical_per_address(self):
        with tempfile.TemporaryDirectory() as tmp:
            reg = read_register(write(tmp, "reg.tsv", REGISTER))
        self.assertEqual(reg["old-user/demo"], ("demo", "STALE", "canon-org/demo"))
        self.assertEqual(reg["a-org/nocanon"][2], "")

    def test_C16_gate_refuses_a_register_without_shelves(self):
        r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "alias_gate.py"),
                            "only-a-register.tsv"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        self.assertIn("refusing", r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
