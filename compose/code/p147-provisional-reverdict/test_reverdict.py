"""Tests for p147-provisional-reverdict. Authored fixtures only; nothing is fetched."""
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reverdict as R  # noqa: E402


def tree(root, files):
    for rel, body in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)


SERVER = ("import { Server } from '@modelcontextprotocol/sdk/server/index.js';\n"
          "const s = new Server();\n")


class Base(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)


class TestArtefactMode(Base):
    def test_no_package_json_is_source(self):
        tree(self.d, {"src/a.py": "print(1)\n"})
        self.assertEqual(R.artefact_mode(self.d), ("SOURCE", "no declared entry point"))

    def test_no_declared_entry_is_source(self):
        tree(self.d, {"package.json": '{"name":"x"}', "src/a.js": "1\n"})
        mode, why = R.artefact_mode(self.d)
        self.assertEqual(mode, "SOURCE")
        self.assertIn("no declared entry", why)

    def test_all_entries_in_dist_is_payload(self):
        tree(self.d, {"package.json": '{"main":"dist/i.js","bin":{"x":"dist/i.js"}}'})
        mode, why = R.artefact_mode(self.d)
        self.assertEqual(mode, "PAYLOAD")
        self.assertIn("2/2", why)

    def test_mixed_entries_stay_source(self):
        tree(self.d, {"package.json": '{"main":"dist/i.js","module":"src/i.mjs"}'})
        self.assertEqual(R.artefact_mode(self.d)[0], "SOURCE")

    def test_payload_mode_is_decided_from_manifest_not_tree(self):
        """🔴 `T62`: PAYLOAD with no `dist/` in the tree. The rule reads the manifest."""
        tree(self.d, {"package.json": '{"main":"dist/i.js"}', "src/a.ts": SERVER})
        self.assertEqual(R.artefact_mode(self.d)[0], "PAYLOAD")
        self.assertFalse(os.path.isdir(os.path.join(self.d, "dist")))
        row = R.classify(self.d)
        self.assertEqual(row["walked_excl"], row["walked_all"])
        self.assertEqual(row["t42"], "INPUT_SEEN")


class TestGuardInteraction(Base):
    def test_dist_only_payload_is_a_t42_artefact(self):
        tree(self.d, {"package.json": '{"main":"dist/i.js"}', "dist/i.js": SERVER})
        row = R.classify(self.d)
        self.assertEqual(row["walked_excl"], 0)
        self.assertGreater(row["walked_all"], 0)
        self.assertEqual(row["t42"], "T42_ARTEFACT")
        self.assertEqual(row["guard"], "NO_PAYLOAD_WALKED")

    def test_same_bytes_at_root_read_as_a_server(self):
        """🟢 `P146-C`'s negative control, carried as a regression pin."""
        tree(self.d, {"package.json": '{"main":"i.js"}', "i.js": SERVER})
        row = R.classify(self.d)
        self.assertEqual(row["t42"], "INPUT_SEEN")
        self.assertEqual(row["verdict_now"], "IS_AN_MCP_SERVER")

    def test_input_seen_when_exclusion_never_fires(self):
        tree(self.d, {"src/a.py": "x = 1\n"})
        row = R.classify(self.d)
        self.assertEqual(row["t42"], "INPUT_SEEN")
        self.assertEqual(row["guard"], "WALKED")
        self.assertTrue(row["verdict_now"].startswith("NOT_AN_MCP_SERVER"))

    def test_empty_tree_is_not_a_t42_artefact(self):
        """An empty repository is a fact about the repository, not about the gate."""
        row = R.classify(self.d)
        self.assertEqual(row["t42"], "NO_SOURCE_AT_ALL")

    def test_rust_is_walked_here_unlike_the_shelf_gates(self):
        """🆕 `T64`: `.rs` is outside `surface_gate`'s map and inside this probe's."""
        tree(self.d, {"Cargo.toml": '[package]\nname="x"\n', "src/main.rs": "fn main(){}"})
        self.assertEqual(R.classify(self.d)["walked_excl"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
