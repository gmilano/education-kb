#!/usr/bin/env python3
"""p397 controls. Offline, stdlib-only, fixtures inline — so this is runnable
wherever the repository is checked out, per `396-C`'s (now refuted) warning that
Python instruments should ship as specifications an operator can verify.
"""
import os, sys, tempfile, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import candidates


def U(*slugs):
    """p351's harvester reads CHANNEL U -- github.com URLs. Backticked bare slugs
    are channel B (p367), a different instrument. p397's first fixtures were bare
    slugs and harvested nothing: the instrument was right, the fixture was wrong.
    This is also why this instrument's denominator is the channel-U census."""
    return " ".join(f"[x](https://github.com/{s})" for s in slugs)


def shelf(text):
    fh = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
    fh.write(text)
    fh.close()
    return fh.name


class Candidates(unittest.TestCase):
    def groups(self, text):
        idx = candidates.address_shape.harvest([shelf(text)])
        addrs, _ = candidates.address_shape.partition(idx)
        out = {}
        for a in addrs:
            o, _, n = a.partition("/")
            out.setdefault(n, set()).add(o)
        return {n: sorted(o) for n, o in out.items() if len(o) > 1}

    # 🔵 Two fixture lessons from p397's own first draft, both the instrument
    # being right and the fixture being wrong: p351 REJECTS degenerate names, and
    # p351 harvests channel U (URLs) rather than channel B (backticked slugs).
    def test_C1_same_name_two_owners_is_a_candidate(self):
        g = self.groups(U("acme/ltijs", "bravo/ltijs"))
        self.assertEqual(g, {"ltijs": ["acme", "bravo"]})

    def test_C2_same_name_one_owner_is_NOT_a_candidate(self):
        self.assertEqual(self.groups(U("acme/ltijs", "acme/ltijs")), {})

    def test_C3_different_names_are_NOT_candidates(self):
        self.assertEqual(self.groups(U("acme/ltijs", "bravo/pylti")), {})

    def test_C4_casing_folds_before_grouping_so_a_fold_is_not_a_pair(self):
        # p348's fold and this instrument must agree, or a casing variant
        # would read as a second OWNER and manufacture a candidate pair.
        self.assertEqual(self.groups(U("Acme/ltijs", "acme/ltijs")), {})

    def test_C5_p351_rejection_classes_are_HONOURED_not_reimplemented(self):
        # `topics/education` is a NAV-NAMESPACE shape, not an address. If this
        # instrument re-implemented the filter it would drift from the census.
        g = self.groups(U("topics/education", "frappe/education"))
        self.assertEqual(g, {})

    def test_C6_three_owners_is_one_group_and_three_pairs(self):
        g = self.groups(U("acme/ltijs", "bravo/ltijs", "charlie/ltijs"))
        self.assertEqual(g, {"ltijs": ["acme", "bravo", "charlie"]})
        n = len(g["ltijs"])
        self.assertEqual(n * (n - 1) // 2, 3)


class Lineage(unittest.TestCase):
    """The verdict table `lineage.sh` implements, asserted as a pure function so
    the semantics are testable without the network."""

    @staticmethod
    def verdict(a_root, b_root, a_head, b_head):
        if a_root == "FAIL" or b_root == "FAIL":
            return "INCONCLUSIVE-UNRESOLVABLE"
        if a_root != b_root:
            return "INDEPENDENT"
        return "SAME-REPO-ALIAS" if a_head == b_head else "DIVERGENT-FORK"

    def test_C7_distinct_roots_are_independent(self):
        self.assertEqual(self.verdict("r1", "r2", "h1", "h2"), "INDEPENDENT")

    def test_C8_shared_root_same_head_is_ONE_artefact_not_a_fork(self):
        # p397's live finding: 8 of 15 shared-root pairs were this. `396-F`
        # labelled every one of them "FORK LINEAGE", which over-claims.
        self.assertEqual(self.verdict("r1", "r1", "h1", "h1"), "SAME-REPO-ALIAS")

    def test_C9_shared_root_different_head_is_a_real_fork(self):
        self.assertEqual(self.verdict("r1", "r1", "h1", "h2"), "DIVERGENT-FORK")

    def test_C10_an_unresolvable_side_is_never_called_independent(self):
        # apereo/opencast 404s. Calling that "INDEPENDENT" would publish a
        # distinctness claim from a failed read -- the p393 false-UNGRANTED class.
        self.assertEqual(self.verdict("FAIL", "r2", "-", "-"), "INCONCLUSIVE-UNRESOLVABLE")
        self.assertEqual(self.verdict("r1", "FAIL", "-", "-"), "INCONCLUSIVE-UNRESOLVABLE")

    def test_C11_negative_control_both_sides_dead(self):
        self.assertEqual(self.verdict("FAIL", "FAIL", "-", "-"), "INCONCLUSIVE-UNRESOLVABLE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
