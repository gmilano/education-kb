"""Tests for p150-identifier-collision. Authored fixtures, offline. `ACTION FM`."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import identifier_collision as C  # noqa: E402

FIRST_A = "## 🆕 🟢 `P30` — the all-permissive education stack *(new, p146 — all regions)*"
FIRST_B = "## 🆕 🔴 `P30` — the jurisdiction gate: build against the clock *(new, p146)*"
SAME_AS_A = "## 🆕 `P30` — the all-permissive education stack *(new, p146 — all regions)*"
REVISIT = "## 🔁 `P30` AMENDED at step 1 — the tree to measure is declared *(p147)*"
UNMARKED = "## P1 — Auditable AI tutor on an existing LMS *(the default engagement)*"
UNMARKED_2 = "## P1 — Offline-first tutor for low-connectivity deployments"


class HeadingClassification(unittest.TestCase):
    def test_first_allocation(self):
        pid, kind, _t = C.classify(FIRST_A)
        self.assertEqual((pid, kind), ("P30", "FIRST"))

    def test_revisit_is_not_a_first_allocation(self):
        pid, kind, _t = C.classify(REVISIT)
        self.assertEqual((pid, kind), ("P30", "REVISIT"))

    def test_unmarked_heading_counts_as_an_allocation(self):
        pid, kind, _t = C.classify(UNMARKED)
        self.assertEqual((pid, kind), ("P1", "UNMARKED"))

    def test_amended_in_the_title_is_a_revisit(self):
        pid, kind, _t = C.classify("## `P21` RECAVEATED — most pins are one-directional")
        self.assertEqual((pid, kind), ("P21", "REVISIT"))

    def test_rewritten_is_a_revisit(self):
        pid, kind, _t = C.classify("## 🔁 `P13` rewritten — the grant goes in the store")
        self.assertEqual(kind, "REVISIT")

    def test_renumbered_is_a_revisit_not_a_second_allocation(self):
        # 🔵 p149's own fix must not be flagged as the collision it resolved.
        line = ("## 🆕 🟢 `P35` — the manifest-contract CI gate "
                "*(p148, RENUMBERED by p149 — Global)*")
        _pid, kind, _t = C.classify(line)
        self.assertEqual(kind, "REVISIT")

    def test_non_heading_lines_are_ignored(self):
        self.assertIsNone(C.classify("This paragraph mentions `P18` in prose."))
        self.assertIsNone(C.classify("| `P30` | a table row |"))
        self.assertIsNone(C.classify(""))

    def test_h3_subsections_are_NOT_read_as_allocations(self):
        # 🔵 "What `P36` does NOT solve" is a subsection of P36, not a second P36.
        # The word before the id is what rules it out.
        self.assertIsNone(C.classify("### 🔴 What `P36` does NOT solve — nothing"))
        self.assertIsNone(C.classify("### 🔴 `P35` does NOT reach the data layer"))

    def test_h3_allocation_would_be_read(self):
        pid, kind, _t = C.classify("### 🆕 `P40` — a third-level pattern *(new, p150)*")
        self.assertEqual((pid, kind), ("P40", "FIRST"))

    def test_mid_text_before_the_dash_is_searched_for_revisit_verbs(self):
        line = "## 🔁 `P18` AMENDED at steps 2 and 5 — measure the shipped tree *(p144)*"
        pid, kind, _t = C.classify(line)
        self.assertEqual((pid, kind), ("P18", "REVISIT"))


class CollisionDetection(unittest.TestCase):
    def test_two_different_first_allocations_collide(self):
        found = C.collisions(C.scan_patterns("\n".join([FIRST_A, FIRST_B])))
        self.assertEqual(len(found), 1)
        self.assertEqual((found[0]["id"], found[0]["kind"]), ("P30", "COLLISION"))

    def test_a_first_plus_a_revisit_is_clean(self):
        found = C.collisions(C.scan_patterns("\n".join([FIRST_A, REVISIT])))
        self.assertEqual(found, [])

    def test_five_revisits_are_clean(self):
        page = "\n".join([FIRST_A] + [REVISIT] * 5)
        self.assertEqual(C.collisions(C.scan_patterns(page)), [])

    def test_identical_titles_are_a_duplicate_heading_not_a_collision(self):
        found = C.collisions(C.scan_patterns("\n".join([FIRST_A, SAME_AS_A])))
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["kind"], "DUPLICATE_HEADING")

    def test_two_unmarked_headings_collide(self):
        found = C.collisions(C.scan_patterns("\n".join([UNMARKED, UNMARKED_2])))
        self.assertEqual((found[0]["id"], found[0]["kind"]), ("P1", "COLLISION"))

    def test_clean_page_is_clean(self):
        page = "\n".join([FIRST_A, REVISIT,
                          "## 🆕 `P31` — something else *(new, p147)*"])
        self.assertEqual(C.collisions(C.scan_patterns(page)), [])

    def test_empty_page_is_not_a_crash(self):
        self.assertEqual(C.collisions(C.scan_patterns("")), [])

    def test_ids_are_reported_in_numeric_not_lexical_order(self):
        page = "\n".join([
            "## 🆕 `P9` — a *(new, p1)*", "## 🆕 `P9` — b *(new, p1)*",
            "## 🆕 `P10` — c *(new, p1)*", "## 🆕 `P10` — d *(new, p1)*"])
        ids = [f["id"] for f in C.collisions(C.scan_patterns(page))]
        self.assertEqual(ids, ["P9", "P10"])


class GateExitCode(unittest.TestCase):
    def test_collision_fails_the_gate(self):
        code, lines = C.gate("\n".join([FIRST_A, FIRST_B]))
        self.assertEqual(code, 1)
        self.assertTrue(any("COLLISION" in ln for ln in lines))

    def test_clean_page_passes_the_gate(self):
        code, _lines = C.gate("\n".join([FIRST_A, REVISIT]))
        self.assertEqual(code, 0)

    def test_duplicate_heading_alone_does_not_fail_the_gate(self):
        # 🔵 Reported, but it is a deletion not a renumber, so it is not stop-ship.
        code, lines = C.gate("\n".join([FIRST_A, SAME_AS_A]))
        self.assertEqual(code, 0)
        self.assertTrue(any("DUPLICATE_HEADING" in ln for ln in lines))

    def test_empty_page_passes(self):
        self.assertEqual(C.gate("")[0], 0)


class RegisterSurface(unittest.TestCase):
    def test_a_thesis_defined_twice_is_caught(self):
        text = "\n".join([
            "| `T74` | the ladder is inverted |",
            "| `T74` | something completely different |",
            "Prose mentioning `T74` again does not count.",
        ])
        self.assertEqual(list(C.register_collisions(text, C.THESIS)), ["T74"])

    def test_a_thesis_defined_once_is_clean(self):
        text = "| `T74` | the ladder is inverted |\nprose about `T74`\n"
        self.assertEqual(C.register_collisions(text, C.THESIS), {})

    def test_prose_mentions_alone_never_collide(self):
        text = "`T1` here.\nand `T1` there.\n"
        self.assertEqual(C.register_collisions(text, C.THESIS), {})

    def test_heading_definitions_count(self):
        text = "## `T80` — one thing\n## `T80` — another thing\n"
        self.assertEqual(list(C.register_collisions(text, C.THESIS)), ["T80"])

    def test_finding_ids_use_the_same_machinery(self):
        text = "| `P149-A` | x |\n| `P149-A` | y |\n"
        self.assertEqual(list(C.register_collisions(text, C.FINDING)), ["P149-A"])


class TitleNormalisation(unittest.TestCase):
    def test_emoji_and_markdown_do_not_create_false_collisions(self):
        a = C.classify("## 🆕 🟢 `P5` — **the stack**, end to end *(new, p1)*")[2]
        b = C.classify("## `P5` — the stack, end to end *(new, p2 — LATAM)*")[2]
        self.assertEqual(a, b)

    def test_different_titles_stay_different(self):
        a = C.classify(FIRST_A)[2]
        b = C.classify(FIRST_B)[2]
        self.assertNotEqual(a, b)

    def test_trailing_parenthetical_is_stripped(self):
        self.assertNotIn("new", C.classify(FIRST_A)[2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
