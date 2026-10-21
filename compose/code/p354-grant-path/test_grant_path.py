#!/usr/bin/env python3
"""Controls for `p354-grant-path` — ACTION ZZ-au.

🔵 Every control is OFFLINE and runs from this directory (`p355-cwd-portability`'s class --
`python3 -I` strips the script's directory from `sys.path`, so the suite only resolves its own
module when invoked from here, which is why the Makefile recipe `cd`s in).

🟢 The controls bind the EXTRACTOR, because that is the half that can be wrong silently.  A
claim the parser fails to see is a claim the online arm never probes, so an under-counting
parser would make this gate report green over an unchecked corpus -- the masking shape `p300`'s
runner exists to prevent, pointed inwards.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grant_path as gp  # noqa: E402

# ── Fixtures taken VERBATIM from the live shelves, so the controls are measured rather than
#    imagined.  A paraphrased fixture proves the parser handles the paraphrase.

# agents/top.md, Build-on-this tier, the anchor row.
ROW_PLAIN = ("| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | `main/LICENSE` "
             "| Lifelong personalised tutoring with bounded tutoring memory |")

# agents/top.md, MCP tier -- the `master`-default row p353 names as the prior art.
ROW_MASTER = ("| google-classroom-mcp | https://github.com/pengusto/google-classroom-mcp | MIT "
              "| `master/LICENSE` | **Google Classroom, teacher-side**. 🟡 **Note the branch: "
              "`master`, not `main`** |")

# 🔴 THE ROW THIS GATE EXISTS FOR.  p353's corrective cell, verbatim from agents/top.md.
# It names TWO paths and the SECOND is named in order to be REFUTED.
ROW_P353_CORRECTED = (
    "| classroom-mcp (sandraschi) | https://github.com/sandraschi/classroom-mcp | MIT "
    "| 🔴 **`master/LICENSE`** — corrected at p353; this cell read `main/LICENSE`, which is "
    "**404**. Default branch is `master`; grant is stock MIT, `1 071 B`, holder "
    "`Sandra Schipal`, 2026 | **No external platform** — a self-contained SIS |")

# agents/top.md, the AGPL row -- a copyleft grant is still a grant path.
ROW_AGPL = ("| openedx-mcp | https://github.com/blend-ed/openedx-mcp | AGPL-3.0 "
            "| `master/LICENSE` | **Open edX.** 🔴 **AGPL-3.0** |")

HEADER = "| Agent | Repo | Licence | Grant read at | What it does |"
SEP = "|---|---|---|---|---|"


def table(*rows):
    """A fixture row only means anything UNDER its header, now that the parse is bound to
    the `Grant read at` column.  🔵 This helper exists so no control can accidentally test
    the parser against a grammar the shelves never use."""
    return "\n".join([HEADER, SEP, *rows])


class TheFirstWinsContract(unittest.TestCase):
    """🔴 The parse that decides whether this gate accuses p353's own repair."""

    def test_p353s_corrected_cell_parses_to_the_ASSERTED_path_not_the_refuted_one(self):
        got = gp.extract(table(ROW_P353_CORRECTED), "agents/top.md")
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["slug"], "sandraschi/classroom-mcp")
        self.assertEqual(got[0]["branch"], "master")
        self.assertEqual(got[0]["path"], "LICENSE")

    def test_the_refuted_path_is_NOT_emitted_as_a_second_claim(self):
        # 🔴 A parser that took ALL paths would probe `main/LICENSE`, get the 404 p353
        # documented, and report a defect against the one cell that was just repaired.
        got = gp.extract(table(ROW_P353_CORRECTED), "agents/top.md")
        self.assertNotIn("main", [c["branch"] for c in got])

    def test_the_byte_count_in_the_same_cell_is_not_mistaken_for_a_path(self):
        # `1 071 B` and `Sandra Schipal` are backticked in that cell and neither is a path.
        got = gp.extract(table(ROW_P353_CORRECTED), "agents/top.md")
        self.assertEqual(got[0]["path"], "LICENSE")


class ThePlainRows(unittest.TestCase):
    def test_a_main_LICENSE_row_parses(self):
        got = gp.extract(table(ROW_PLAIN), "agents/top.md")
        self.assertEqual((got[0]["slug"], got[0]["branch"], got[0]["path"]),
                         ("HKUDS/DeepTutor", "main", "LICENSE"))

    def test_a_master_default_row_parses_and_keeps_its_branch(self):
        # 🔵 p353: 2 of 31 rows are `master`-default, so the `main` assumption is wrong ~6 %
        # of the time.  The branch is DATA, never a default.
        got = gp.extract(table(ROW_MASTER), "repos/foundations.md")
        self.assertEqual(got[0]["branch"], "master")

    def test_the_trailing_note_naming_master_again_does_not_double_count(self):
        got = gp.extract(table(ROW_MASTER), "repos/foundations.md")
        self.assertEqual(len(got), 1)

    def test_a_copyleft_grant_is_still_a_grant_path(self):
        # A gate that only checked permissive rows would leave the AGPL row's path unprobed,
        # and a 404 there is the same defect with a worse consequence.
        got = gp.extract(table(ROW_AGPL), "agents/top.md")
        self.assertEqual((got[0]["branch"], got[0]["path"]), ("master", "LICENSE"))

    def test_a_multi_segment_path_survives(self):
        # 🔵 p275 found a REAL grant at `docs/License.txt` (os4ed/openSIS-Classic, GPL-2.0,
        # 17 286 B).  A parser that assumed one segment would miss it.
        row = ("| openSIS | https://github.com/os4ed/openSIS-Classic | GPL-2.0 "
               "| `master/docs/License.txt` | SIS |")
        got = gp.extract(table(row), "verticals/solutions.md")
        self.assertEqual((got[0]["branch"], got[0]["path"]), ("master", "docs/License.txt"))

    def test_an_uppercase_extension_survives(self):
        # p283's ladder-case axis: stem case AND extension case both vary.
        row = "| x | https://github.com/a/b | MIT | `main/LICENSE.TXT` | y |"
        got = gp.extract(table(row), "agents/top.md")
        self.assertEqual(got[0]["path"], "LICENSE.TXT")

    def test_COPYING_is_a_grant_basename(self):
        row = "| x | https://github.com/a/b | GPL-2.0 | `main/COPYING` | y |"
        self.assertEqual(gp.extract(table(row), "x")[0]["path"], "COPYING")


class TheRejections(unittest.TestCase):
    def test_the_table_HEADER_is_not_a_claim(self):
        # 🟢 p353 scanned all six shelves for rows rendering as headers and found zero; the
        # protection is ACTION p277 / gate-tables.  This parser must not re-introduce the
        # hazard from the other side by reading a header as data.
        self.assertEqual(gp.extract(HEADER, "agents/top.md"), [])

    def test_the_separator_row_is_not_a_claim(self):
        self.assertEqual(gp.extract(SEP, "agents/top.md"), [])

    def test_a_command_TEMPLATE_is_rejected_rather_than_probed(self):
        # agents/top.md publishes `raw.githubusercontent.com/<slug>/<branch>/<path>` as a
        # command template.  p351's address_shape rejects these on the slug side with a
        # published denominator; the same shapes are rejected here on the path side.
        row = ("| how | https://github.com/OWNER/REPO | n/a | `<branch>/<path>` | the "
               "template |")
        got = gp.extract(table(row), "agents/top.md")
        self.assertEqual([c["verdict"] for c in got], ["NO-PATH"])

    def test_a_refs_heads_token_is_not_a_grant_path(self):
        # `ls-remote --symref` output appears in prose: `ref: refs/heads/master`.
        row = "| x | https://github.com/a/b | MIT | `refs/heads/master` | y |"
        self.assertEqual([c["verdict"] for c in gp.extract(table(row), "x")], ["NO-PATH"])

    def test_a_companion_SLUG_in_the_grant_cell_is_not_a_path(self):
        # The anki row backticks `ankimcp/anki-mcp-server-addon` -- a slug, not a path.
        row = ("| anki-mcp-server | https://github.com/ankimcp/anki-mcp-server | MIT "
               "| `ankimcp/anki-mcp-server-addon` | Anki |")
        self.assertEqual([c["verdict"] for c in gp.extract(table(row), "x")], ["NO-PATH"])

    def test_a_row_with_no_github_slug_is_not_a_claim(self):
        row = "| Moodle | https://moodle.org | GPL-3.0 | `main/COPYING.txt` | LMS |"
        self.assertEqual(gp.extract(table(row), "verticals/solutions.md"), [])

    def test_prose_outside_a_table_is_not_a_claim(self):
        prose = ("🔴 One returned `404`: [`sandraschi/classroom-mcp`]"
                 "(https://github.com/sandraschi/classroom-mcp), published here as **MIT, "
                 "read at `main/LICENSE`**.")
        # 🔴 This is p353's own WRITE-UP sentence, which names the refuted path in prose.
        # A parser that read prose would probe it and accuse the pass that fixed it.
        self.assertEqual(gp.extract(prose, "agents/top.md"), [])


class TheNoPathDeclaration(unittest.TestCase):
    def test_a_slug_row_without_a_path_is_DECLARED_not_dropped(self):
        row = "| x | https://github.com/a/b | 🔴 no licence path in the tree | — | y |"
        got = gp.extract(table(row), "agents/trending.md")
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["verdict"], "NO-PATH")

    def test_NO_PATH_rows_carry_their_file_and_line(self):
        text = "\n".join(["prose", HEADER, SEP, ROW_PLAIN,
                          "| x | https://github.com/a/b | none | — | y |"])
        got = gp.extract(text, "repos/trending.md")
        nop = [c for c in got if c["verdict"] == "NO-PATH"]
        self.assertEqual((nop[0]["file"], nop[0]["line"]), ("repos/trending.md", 5))


class TheSubjectOfARow(unittest.TestCase):
    def test_the_FIRST_slug_is_the_rows_subject(self):
        # 🔴 p343 corrected a row that named a FORK (`kvnloo/tutor-mcp`) while the upstream
        # was the subject; p351's THIRD_PARTY_SCOPE is the same confusion on a licence.
        row = ("| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT "
               "| `main/LICENSE` | 🔴 this row named the FORK "
               "(https://github.com/kvnloo/tutor-mcp) |")
        got = gp.extract(table(row), "agents/top.md")
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["slug"], "ArnaudGuiovanna/tutor-mcp")


class TheHarvestOverATree(unittest.TestCase):
    def _root(self, **files):
        root = tempfile.mkdtemp()
        for rel, body in files.items():
            full = os.path.join(root, rel)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8") as fh:
                fh.write(body)
        return root

    def test_claims_are_harvested_across_several_shelves(self):
        root = self._root(**{
            "agents/top.md": "\n".join([HEADER, SEP, ROW_PLAIN, ROW_P353_CORRECTED]),
            "repos/foundations.md": "\n".join([HEADER, SEP, ROW_MASTER]),
        })
        claims = [c for c in gp.harvest(root) if c["verdict"] == "CLAIM"]
        self.assertEqual(len(claims), 3)
        self.assertEqual({c["file"] for c in claims},
                         {"agents/top.md", "repos/foundations.md"})

    def test_a_shelf_absent_from_the_tree_is_skipped_not_fatal(self):
        root = self._root(**{"agents/top.md": "\n".join([HEADER, SEP, ROW_PLAIN])})
        self.assertEqual(len(gp.harvest(root)), 1)

    def test_offline_run_passes_on_a_tree_with_claims(self):
        root = self._root(**{"agents/top.md": "\n".join([HEADER, SEP, ROW_PLAIN])})
        self.assertEqual(gp.main(["--root", root]), 0)

    def test_offline_run_FAILS_on_a_tree_with_ZERO_claims(self):
        # 🔴 Zero is not green.  Either the shelves stopped publishing grant paths or this
        # parser broke -- both are findings, and a gate that passed here would hide the
        # second one, which is the failure mode this whole suite is about.
        root = self._root(**{"agents/top.md": "no tables here\n"})
        self.assertEqual(gp.main(["--root", root]), 1)

    def test_no_root_is_REFUSED_with_2_not_1(self):
        # P541: a measurement over nothing is a refusal, distinguishable from a defect.
        self.assertEqual(gp.main([]), 2)

    def test_a_nonexistent_root_is_REFUSED_with_2(self):
        self.assertEqual(gp.main(["--root", "/nonexistent-tree-p354"]), 2)


class TheUrlForm(unittest.TestCase):
    def test_the_raw_url_is_assembled_exactly(self):
        self.assertEqual(
            gp.raw_url("sandraschi/classroom-mcp", "master", "LICENSE"),
            "https://raw.githubusercontent.com/sandraschi/classroom-mcp/master/LICENSE")

    def test_the_p353_defect_reproduces_as_a_DIFFERENT_url(self):
        # 🔴 The two URLs differ in one token and that token was the whole defect.
        self.assertNotEqual(
            gp.raw_url("sandraschi/classroom-mcp", "master", "LICENSE"),
            gp.raw_url("sandraschi/classroom-mcp", "main", "LICENSE"))


class TheColumnBinding(unittest.TestCase):
    """🔴 The three cells this instrument's FIRST run accused, pinned as controls.

    All three are TRUE, first-hand, REPO-RELATIVE paths published in a pass write-up's table.
    A `branch/path` parser reads their first segment as a branch (`tests`, `canvas-lms-mcp`,
    `packages`), probes a raw URL that 404s, and reports a defect against a correct cell.
    🟢 The fix is that a claim is taken ONLY from a `Grant read at` column, which these
    tables do not have.  Verbatim from `agents/top.md` at p353's HEAD.
    """

    PIN_HEADER = ("| Address | Grant, read at the pin | Commits | Placement |")
    PIN_SEP = "|---|---|---|---|"

    FP_QTI = ("| [`examplary/qti`](https://github.com/examplary/qti) | 🟢 **MIT** at ROOT. "
              "`tests/stubs/LICENSE.md` reads `NOT-A-GRANT-TEXT` — a stub, correctly not "
              "counted as a second grant | 39 c · 2 authors | **EMEA** |")
    FP_CANVAS = ("| [`likr/canvas-lms-agent`](https://github.com/likr/canvas-lms-agent) | 🟡 "
                 "**MIT at `canvas-lms-mcp/LICENSE`**, *Copyright (c) 2026 likr-sandbox* | 🟢 "
                 "TREE | 🔴 **Depth.** |")
    FP_XAPI = ("| [`studiolxd/xapi`](https://github.com/studiolxd/xapi) | 🟡 **MIT at "
               "`packages/xapi/LICENSE`**, *Copyright (c) 2026 Studio LXD* | 🟢 TREE | 🔴 "
               "**Depth.** |")

    def _pin_table(self, *rows):
        return "\n".join([self.PIN_HEADER, self.PIN_SEP, *rows])

    def test_the_qti_stub_path_is_NOT_read_as_a_branch_called_tests(self):
        self.assertEqual(gp.extract(self._pin_table(self.FP_QTI), "agents/top.md"), [])

    def test_the_canvas_lms_agent_subdirectory_grant_is_NOT_a_branch(self):
        self.assertEqual(gp.extract(self._pin_table(self.FP_CANVAS), "agents/top.md"), [])

    def test_the_xapi_packages_grant_is_NOT_a_branch(self):
        self.assertEqual(gp.extract(self._pin_table(self.FP_XAPI), "agents/top.md"), [])

    def test_all_three_together_yield_ZERO_claims(self):
        # 🔴 The exact run that produced three false positives, as one control.
        text = self._pin_table(self.FP_QTI, self.FP_CANVAS, self.FP_XAPI)
        self.assertEqual(gp.extract(text, "agents/top.md"), [])

    def test_a_pin_column_is_not_a_grant_path_column(self):
        # 🔵 `Grant, read at the pin` holds a FAMILY and a byte count (`MIT, 1 068 B`), not a
        # path.  Eight live tables use that header; none of them publishes a raw-read path.
        self.assertNotIn("grant, read at the pin", gp.GRANT_COLUMN_HEADERS)

    def test_the_bound_column_survives_bold_and_backtick_furniture(self):
        hdr = "| Agent | Repo | Licence | **`Grant read at`** | What it does |"
        text = "\n".join([hdr, SEP, ROW_PLAIN])
        self.assertEqual(gp.extract(text, "agents/top.md")[0]["branch"], "main")

    def test_a_table_with_no_grant_column_contributes_nothing(self):
        hdr = "| Agent | Repo | Licence | What it does |"
        row = ("| x | https://github.com/a/b | MIT | note the path `packages/x/LICENSE` |")
        self.assertEqual(gp.extract("\n".join([hdr, "|---|---|---|---|", row]), "x"), [])

    def test_the_column_index_does_NOT_leak_into_the_next_table(self):
        # 🔴 Without a reset at the table boundary, table 2's fourth cell would be read with
        # table 1's grammar -- one table's meaning imported into another.
        text = "\n".join([
            HEADER, SEP, ROW_PLAIN,
            "",
            "| Address | Grant, read at the pin | Commits | Placement |",
            "|---|---|---|---|",
            self.FP_XAPI,
        ])
        got = gp.extract(text, "agents/top.md")
        self.assertEqual([c["slug"] for c in got], ["HKUDS/DeepTutor"])

    def test_a_second_grant_column_table_is_picked_up_again(self):
        text = "\n".join([HEADER, SEP, ROW_PLAIN, "", HEADER, SEP, ROW_MASTER])
        got = gp.extract(text, "agents/top.md")
        self.assertEqual(len(got), 2)


class TheLiveRegionScope(unittest.TestCase):
    def test_everything_below_the_carried_history_marker_is_OUT_of_scope(self):
        text = "\n".join([
            HEADER, SEP, ROW_PLAIN,
            "## ⏷ Carried history — everything below this line predates Pass 339 and was "
            "NOT rewritten",
            HEADER, SEP, ROW_MASTER,
        ])
        got = gp.extract(gp.live_region(text), "agents/top.md")
        self.assertEqual([c["slug"] for c in got], ["HKUDS/DeepTutor"])

    def test_the_marker_is_matched_on_its_token_not_on_a_pass_number(self):
        # 🔵 Five shelves say "predates Pass 339"; `compose/patterns.md` says 340.  Binding
        # to the number would silently unscope one shelf.
        for n in (339, 340, 999):
            text = "## ⏷ Carried history — everything below this line predates Pass %d\nx" % n
            self.assertEqual(gp.live_region(text).strip(), "")

    def test_a_shelf_with_NO_marker_is_judged_WHOLE(self):
        # 🔴 The alternative fails open: deleting one heading would remove a file from this
        # gate's scope, and a gate whose coverage shrinks when a line is dropped is not one.
        text = "\n".join([HEADER, SEP, ROW_PLAIN])
        self.assertEqual(gp.live_region(text), text)

    def test_the_append_only_trending_shelves_are_excluded_whole(self):
        # 🟢 p352's "only the live occurrence is judged", applied to a whole file: every
        # section of these two is a dated record and none is ever rewritten.
        for f in ("agents/trending.md", "repos/trending.md"):
            self.assertIn(f, gp.HISTORY_ONLY_SHELVES)
            self.assertNotIn(f, gp.SHELF_FILES)


class TheCalibrationPair(unittest.TestCase):
    def test_the_control_pair_has_a_positive_AND_a_negative(self):
        # 🔵 p293: a channel that answered 404 for everything would report every row dead.
        # A one-sided control cannot detect that, so the pair is asserted structurally.
        wants = {w for _, _, _, w in [(a, b, c, d) for a, b, c, d in gp.CALIBRATION]}
        self.assertIn(200, wants)
        self.assertIn(404, wants)

    def test_the_negative_control_is_p353s_own_documented_404(self):
        # Drawn from measured history rather than invented, so it stays falsifiable.
        self.assertIn(("sandraschi/classroom-mcp", "main", "LICENSE", 404), gp.CALIBRATION)


if __name__ == "__main__":
    unittest.main(verbosity=0)
