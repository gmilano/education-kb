"""Tests for p147-guard-harness. Authored fixtures; the five instruments are the real ones."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guard_harness as G  # noqa: E402

SERVER_JS = ("import { Server } from '@modelcontextprotocol/sdk/server/index.js';\n"
             "const s = new Server();\n")


class Base(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def write(self, rel, body):
        p = os.path.join(self.d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)

    def git_init(self):
        env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@e",
                   GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@e")
        for args in (["init", "-q"], ["add", "-A"],
                     ["commit", "-qm", "f", "--no-gpg-sign"]):
            subprocess.run(["git", "-C", self.d] + args, check=True, env=env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def run_one(self, label):
        spec = next(a for a in G.AT_RISK if a[0] == label)
        return G.guarded_enumeration(spec[0], spec[1], spec[2], spec[3], self.d)


class TestPopulation(unittest.TestCase):
    def test_five_instruments_are_named(self):
        self.assertEqual(len(G.AT_RISK), 5)

    def test_every_one_loads_and_exposes_its_enumeration(self):
        """🟢 The harness calls the instrument's OWN function, so it must resolve."""
        for label, rel, fn_name, _excl in G.AT_RISK:
            mod = G.load(rel)
            self.assertTrue(callable(getattr(mod, fn_name, None)),
                            "%s has no callable %s" % (label, fn_name))

    def test_the_harness_carries_no_copy_of_any_exclusion_set(self):
        """🔴 `P146-D`: a census that carries the tokens it counts reads itself."""
        src = open(os.path.join(os.path.dirname(os.path.abspath(G.__file__)),
                                "guard_harness.py"), encoding="utf-8").read()
        body = src.split('"""', 2)[2]
        self.assertNotIn('"dist"', body)
        self.assertNotIn('"/dist/"', body)


class TestWalkInstruments(Base):
    def test_dist_only_payload_is_refused_by_both_walk_gates(self):
        self.write("package.json", '{"main":"dist/i.js"}')
        self.write("dist/i.js", SERVER_JS)
        for label in ("p141-surface-gate", "p143-surface-gate2"):
            status, n, _ = self.run_one(label)
            self.assertEqual((status, n), (G.NO_PAYLOAD_WALKED, 0), label)

    def test_same_bytes_at_root_are_walked(self):
        self.write("package.json", '{"main":"i.js"}')
        self.write("i.js", SERVER_JS)
        for label in ("p141-surface-gate", "p143-surface-gate2"):
            status, n, _ = self.run_one(label)
            self.assertEqual(status, G.WALKED, label)
            self.assertGreater(n, 0, label)

    def test_rust_only_payload_is_refused_for_a_different_reason(self):
        """🆕 `T64`: `.rs` is outside the gates' extension map, so the walk is empty."""
        self.write("Cargo.toml", '[package]\nname = "x"\n')
        self.write("src/main.rs", "fn main() {}\n")
        self.assertFalse(os.path.isdir(os.path.join(self.d, "dist")))
        for label in ("p141-surface-gate", "p143-surface-gate2"):
            status, n, _ = self.run_one(label)
            self.assertEqual((status, n), (G.NO_PAYLOAD_WALKED, 0), label)

    def test_the_refusal_detail_names_the_exclusion_owner(self):
        self.write("package.json", '{"main":"dist/i.js"}')
        self.write("dist/i.js", SERVER_JS)
        _s, _n, detail = self.run_one("p143-surface-gate2")
        self.assertIn("dist", detail)
        self.assertIn("T42", detail)


class TestGitInstruments(Base):
    def test_a_non_repository_is_refused_by_all_three_git_instruments(self):
        """🔴 `T59`: a tarball is not a git tree, so `ls-tree` yields nothing."""
        self.write("src/a.py", "x = 1\n")
        for label in ("p142-americas", "p142-schema-tiers", "p143-tenancy"):
            status, n, _ = self.run_one(label)
            self.assertEqual((status, n), (G.NO_PAYLOAD_WALKED, 0), label)

    def test_the_same_tree_under_git_is_walked(self):
        self.write("src/a.py", "x = 1\n")
        self.git_init()
        for label in ("p142-americas", "p142-schema-tiers", "p143-tenancy"):
            status, n, _ = self.run_one(label)
            self.assertEqual(status, G.WALKED, label)
            self.assertGreater(n, 0, label)


if __name__ == "__main__":
    unittest.main(verbosity=2)
