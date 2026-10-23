"""`p405-group-lineage`'s controls.

Every measured number pinned here was read FIRST-HAND from a full clone on 2026-10-23 and is
reproducible from the committed evidence file
`evidence/group-lineage.2026-10-23-p405.tsv` without re-cloning: `run.py` re-grades a facts
cache, so the grading is testable offline and the measurement is testable from the TSV.

The load-bearing controls are the two that a plausible wrong instrument gets wrong:

  * `test_ancestry_is_asked_against_head_ancestors_not_all_refs` -- ancestry must be asked
    against the commits reachable from HEAD.  `rev-list --all` includes unmerged branches, so
    an instrument that tests membership in THAT set reports a fork as a superset.  The real
    specimen is `bibo242` (28 commits over all refs) -> `felipedias-ie` (21), where the side
    with FEWER total commits is the descendant.
  * `test_content_copy_direction_refuses_to_guess` -- the direction signal fires only when
    exactly ONE side's root tree is among the shared trees.  Two root trees shared is not a
    direction, and an instrument that picks one anyway publishes a provenance claim it did
    not measure.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grouplineage import Address, components, grade_group, pair  # noqa: E402
from run import ADDR_HEADER  # noqa: E402

EVIDENCE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        os.pardir, os.pardir, os.pardir,
                        "evidence", "group-lineage.2026-10-23-p405.tsv")

# Measured 2026-10-23.  group -> (addresses, resolved, pairs, projects, verdict counts)
MEASURED = {
    "canvas-mcp":             (23, 20, 190, 9,  {"DIVERGED-FORK": 39, "INDEPENDENT": 134,
                                                 "SUPERSET": 17}),
    "moodle-mcp":             (11, 10,  45, 10, {"INDEPENDENT": 45}),
    "blackboard-mcp":         (9,   8,  28, 6,  {"DIVERGED-FORK": 1, "INDEPENDENT": 26,
                                                 "SUPERSET": 1}),
    "brightspace-mcp-server": (4,   4,   6, 2,  {"DIVERGED-FORK": 3, "INDEPENDENT": 3}),
}


def addr(slug, commits, trees, head, roots=(), root_trees=(), ancestors=None):
    """A synthetic Address.  `ancestors` defaults to `commits`, i.e. a linear repository."""
    return Address(slug, commits, trees, head, roots, root_trees,
                   commits if ancestors is None else ancestors)


class GradingRule(unittest.TestCase):
    def test_independent_needs_zero_commits_AND_zero_trees(self):
        a = addr("x/a", ["c1"], ["t1"], "c1")
        b = addr("x/b", ["c2"], ["t2"], "c2")
        self.assertEqual(pair(a, b)[4], "INDEPENDENT")

    def test_shared_tree_alone_is_a_content_copy_never_independent(self):
        """0 shared commits with a shared tree must NEVER report INDEPENDENT.

        This is p404's load-bearing negative, re-asserted at group level because a
        group instrument that counted only commits would report a whole family absent.
        """
        a = addr("x/a", ["c1"], ["t1"], "c1")
        b = addr("x/b", ["c2"], ["t1"], "c2")
        self.assertEqual(pair(a, b)[4], "CONTENT-COPY")

    def test_content_copy_direction_names_the_root_tree_side(self):
        a = addr("x/copy", ["c1"], ["t1"], "c1", roots=["c1"], root_trees=["t1"])
        b = addr("x/origin", ["c2", "c3"], ["t1", "t2"], "c3", roots=["c2"],
                 root_trees=["t2"])
        verdict, direction = pair(a, b)[4:6]
        self.assertEqual((verdict, direction), ("CONTENT-COPY", "a"))

    def test_content_copy_direction_refuses_to_guess(self):
        """Both sides' root trees shared is not a direction.  Refuse, do not pick."""
        a = addr("x/a", ["c1"], ["t1"], "c1", roots=["c1"], root_trees=["t1"])
        b = addr("x/b", ["c2"], ["t1"], "c2", roots=["c2"], root_trees=["t1"])
        self.assertEqual(pair(a, b)[5], None)

    def test_ancestry_is_asked_against_head_ancestors_not_all_refs(self):
        """The `bibo242` -> `felipedias-ie` shape: the descendant has FEWER total commits.

        `a` carries 3 commits over all refs but only 2 are reachable from its HEAD; `b`
        carries 2 and its HEAD contains a's HEAD.  An instrument that tested membership
        in `rev-list --all` would find a's HEAD in b and b's HEAD in a and raise, or
        grade SAME-HEAD.  Asked correctly it is a clean SUPERSET with b the descendant.
        """
        a = addr("x/a", ["c1", "c2", "stray"], ["t1", "t2"], "c2", ancestors=["c1", "c2"])
        b = addr("x/b", ["c1", "c2", "c3"], ["t1", "t2", "t3"], "c3",
                 ancestors=["c1", "c2", "c3"])
        shared_c, _st, a_has_b, b_has_a, verdict, direction = pair(a, b)
        self.assertEqual((a_has_b, b_has_a), (False, True))
        self.assertEqual((verdict, direction), ("SUPERSET", "b"))
        self.assertEqual(shared_c, 2)


class Components(unittest.TestCase):
    def test_lineage_is_transitive_and_a_pair_test_is_not(self):
        """a~b and b~c makes ONE family of three even where a and c share nothing.

        🔵 This property did NOT bind on any of the four groups measured at p405: every
        within-family pair there was directly related, so the components are the same as a
        naive pair-clustering would give.  It is pinned anyway because the instrument claims
        it, and an unexercised claim is the thing that rots.
        """
        comps = components(["a", "b", "c", "d"], [("a", "b"), ("b", "c")])
        self.assertEqual(comps, [["a", "b", "c"], ["d"]])

    def test_a_group_with_no_related_pair_is_n_projects(self):
        """moodle-mcp's measured shape: 10 addresses, 45 pairs, 45 INDEPENDENT, 10 projects."""
        addrs = [addr("x/%d" % i, ["c%d" % i], ["t%d" % i], "c%d" % i) for i in range(10)]
        rows, comps, summary = grade_group(addrs)
        self.assertEqual(len(rows), 45)
        self.assertEqual(summary, {"INDEPENDENT": 45})
        self.assertEqual(len(comps), 10)


class EvidenceFile(unittest.TestCase):
    """The committed TSV is the claim.  These controls read it rather than restate it."""

    @classmethod
    def setUpClass(cls):
        with open(EVIDENCE, encoding="utf-8") as fh:
            cls.lines = [l.rstrip("\n") for l in fh]
        # The two legitimate header lines are identified FIRST, so the placeholder control
        # below is asking about data rows rather than re-finding the headers it expects.
        cls.headers = [l for l in cls.lines
                       if l.startswith("group\taddress\t") or l.startswith("group\taddr_a\t")]
        cls.data = [l for l in cls.lines
                    if l and not l.startswith("#") and l not in cls.headers]

    def test_every_group_result_matches_the_published_summary(self):
        text = "\n".join(self.lines)
        for group, (n, resolved, pairs, _projects, verdicts) in MEASURED.items():
            self.assertIn("# group=%s addresses=%d resolved=%d unresolved=%d pairs=%d"
                          % (group, n, resolved, n - resolved, pairs), text,
                          "%s's published summary line moved" % group)
            self.assertIn("# verdicts " + " ".join("%s=%d" % kv
                                                   for kv in sorted(verdicts.items())),
                          text, "%s's verdict census moved" % group)

    def test_pair_row_count_equals_the_sum_of_the_group_denominators(self):
        want = sum(v[2] for v in MEASURED.values())
        rows = [l for l in self.data if l.count("\t") == 10]
        self.assertEqual(len(rows), want, "269 pairs is the denominator the finding rests on")

    def test_no_header_or_placeholder_row_is_carried_as_data(self):
        """The brief's own standing rule: a header left in as a row compiles into an entity.

        Exactly two header lines are expected -- one per section -- and every other
        non-comment line must be a measured row.
        """
        self.assertEqual(len(self.headers), 2, "one header per section, no more, no fewer")
        for l in self.data:
            first = l.split("\t")[0]
            self.assertNotIn(first, ("group", "address", "addr_a", "Nombre", "nombre",
                                     "name", "repo", "-"),
                             "a header or placeholder row is carried as data: %r" % l[:80])

    def test_every_resolved_address_carries_a_measured_component(self):
        for l in self.data:
            f = l.split("\t")
            if len(f) == len(ADDR_HEADER) and f[2] == "OK":
                self.assertTrue(f[-1] == "SOLE" or f[-1].startswith("FAMILY-"),
                                "unlabelled component on %s" % f[1])

    def test_the_ref_column_is_named_so_it_cannot_be_diffed_against_p402(self):
        """Gap 400-A, as a meta-control.

        A clone-local `git show-ref` count and p402's `ls-remote` count measure different
        populations.  Naming this column `refs` invites exactly the cross-instrument diff the
        gap is about, so the NAME is pinned, not just the numbers.
        """
        self.assertIn("refs_clonelocal", ADDR_HEADER)
        self.assertNotIn("refs", ADDR_HEADER)
        self.assertTrue(any(l.startswith("group\taddress\t") and "refs_clonelocal" in l
                            for l in self.lines), "the TSV header lost the qualified name")


if __name__ == "__main__":
    r = unittest.main(exit=False, verbosity=2).result
    print("controls=%d failures=%d errors=%d"
          % (r.testsRun, len(r.failures), len(r.errors)))
    sys.exit(1 if (r.failures or r.errors) else 0)
