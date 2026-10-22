"""p392's controls.  Every control below is a shape this base has actually published, and the
four marked CLASS 1-4 are the four false-positive classes the draft of this instrument had
before it was published — recorded as controls rather than tidied away, so a successor cannot
re-widen the predicate without a red suite.

🔵 No network.  Each control builds a two-file corpus in a temp dir — one shelf, one harvest
log — because the predicate is about the RELATION between those two files and nothing else.
The real rows quoted here were read first-hand at `p392` on 2026-10-22.
"""

import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import capability_absence as ca  # noqa: E402

# Real harvest rows, as read at p392.  Evidence-complete: slug + licence + date-or-version.
ROW_DJANGO_LTI = ("| [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) "
                  "| 🟢 **MIT** (1,098 B) | 2026-10-20 | PyPI `django-lti` v0.10.1 | LTI Advantage for Django |")
ROW_LTIJS = ("| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** "
             "| 2026-10-13 | npm `ltijs` v7.0.7 | the Node LTI 1.3 tool provider |")
ROW_PROCTORING_JS = ("| [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) "
                     "| 🟢 **MIT** (1,069 B) | 2026-09-28 | npm `proctoring.js` v0.5.1 "
                     "| tab-switch, face detection and audio monitoring in the browser |")
ROW_MCP_BRASIL = ("- [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) — 🟢 **MIT** "
                  "(1,072 B, code only), 2026-08-18, PyPI v0.14.0 — INEP Censo Escolar and ENEM "
                  "microdata for Brazil, 66 keyless APIs |")


def corpus(shelf_text, harvest_text, shelf="verticals/solutions.md"):
    root = tempfile.mkdtemp(prefix="p392-")
    for rel, text in ((shelf, shelf_text), ("agents/trending.md", harvest_text)):
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    return root, shelf


def verdicts(shelf_text, harvest_text, shelf="verticals/solutions.md"):
    root, rel = corpus(shelf_text, harvest_text, shelf)
    try:
        index = ca.index_harvest(root, files=("agents/trending.md",))
        out = []
        for _, _, seg in ca.absence_claims(root, [rel]):
            keys = ca.capability_key(seg)
            if not ca.qualified(keys):
                out.append(("NO-KEY", keys, []))
                continue
            hits = ca.adjudicate(keys, index, seg)
            out.append((("REFUTED-CANDIDATE" if hits else "UNREFUTED"), keys, hits))
        return out
    finally:
        shutil.rmtree(root, ignore_errors=True)


class CapabilityMeeting(unittest.TestCase):
    """The point of the instrument: the two sides share NO distinctive token."""

    def test_python_lti_absence_is_refuted_by_a_django_row(self):
        # `Gap 391-A` verbatim.  The absence says "Python LTI 1.3"; the row says "django-lti
        # / LTI Advantage / PyPI".  No token in common — `gate-absence` cannot connect them.
        v = verdicts("🔴 There is **no maintained Python LTI library**, so the edge is Node in front.",
                     ROW_DJANGO_LTI)
        self.assertEqual([x[0] for x in v], ["REFUTED-CANDIDATE"])
        self.assertEqual(v[0][1], {"lti", "python"})

    def test_proctoring_absence_is_refuted_by_a_browser_toolkit_row(self):
        # `verticals/solutions.md`'s sentence, verbatim, and `Gap 391-C`.
        v = verdicts("- **Proctoring and AI-detection** have no credible permissive open-source option.",
                     ROW_PROCTORING_JS)
        self.assertEqual([x[0] for x in v], ["REFUTED-CANDIDATE"])

    def test_a_node_row_does_not_refute_a_python_claim(self):
        # The distinction `Gap 391-A` is ABOUT.  `{lti, python}` ⊄ `{lti, node}`.
        v = verdicts("🔴 There is **no maintained Python LTI library** on these shelves.", ROW_LTIJS)
        self.assertEqual([x[0] for x in v], ["UNREFUTED"])


class FalsePositiveClasses(unittest.TestCase):
    def test_class1_absence_and_capability_in_different_cells_is_not_a_claim(self):
        # The `pybryt` row: "has no PyPI release" in one cell, "assessment" in another.  Read
        # as a LINE this returned a candidate; read as SEGMENTS it does not.
        row = ("| [microsoft/pybryt](https://github.com/microsoft/pybryt) | 🟢 **MIT** "
               "| it has no release since 2022 | item bank and rubric grading |")
        v = verdicts(row, ROW_PROCTORING_JS)
        self.assertNotIn("REFUTED-CANDIDATE", [x[0] for x in v])

    def test_class2_a_region_alone_is_not_a_capability(self):
        # "Brazil has no AI statute in force" keyed `{r:latam}` and was "refuted" by any
        # granted Brazilian repository.  A place is not a capability.
        v = verdicts("- **Brazil has no AI statute in force.** PL 2338/2023 is not law.", ROW_MCP_BRASIL)
        self.assertEqual([x[0] for x in v], ["NO-KEY"])

    def test_class3_a_quoted_absence_is_not_a_published_absence(self):
        # p391's correction quotes the claim it refutes in the same segment.
        shelf = ('🟢 **There is a maintained Apache-2.0 LTI 1.3 library** — `p390` had concluded '
                 'LTI 1.3 is *"a spec reference to vendor, never a dependency to install."*')
        v = verdicts(shelf, ROW_DJANGO_LTI)
        self.assertEqual(v, [])

    def test_class4_a_negated_region_scope_needs_a_row_from_another_region(self):
        us_row = ("| [`pipeworx-io/mcp-education-data`](https://github.com/pipeworx-io/mcp-education-data) "
                  "| 🟢 **MIT** | 2026-10-21 | US district per-pupil spend and Title I child poverty |")
        claim = ("`Gap 391-B`: the district-targeting instrument is North America only, and there is "
                 "no analogue for any other region.")
        # The US row is what the claim is ABOUT — it must not refute it.
        self.assertEqual([x[0] for x in verdicts(claim, us_row)], ["UNREFUTED"])
        # A Brazilian row carrying the same capability DOES refute it.  This is the live
        # finding at p392: INEP Censo Escolar, already in this base's harvest log.
        self.assertEqual([x[0] for x in verdicts(claim, ROW_MCP_BRASIL)], ["REFUTED-CANDIDATE"])


class EvidenceCompleteness(unittest.TestCase):
    def test_a_row_without_a_licence_refutes_nothing(self):
        row = ("| [`someone/python-lti-thing`](https://github.com/someone/python-lti-thing) "
               "| 2026-10-20 | an LTI 1.3 tool for Django |")
        self.assertFalse(ca.evidence_complete(row))
        self.assertEqual([x[0] for x in verdicts("There is no maintained Python LTI library.", row)],
                         ["UNREFUTED"])

    def test_a_row_without_a_date_or_version_refutes_nothing(self):
        row = ("| [`someone/python-lti-thing`](https://github.com/someone/python-lti-thing) "
               "| 🟢 **MIT** | an LTI 1.3 tool for Django |")
        self.assertFalse(ca.evidence_complete(row))

    def test_the_real_rows_are_evidence_complete(self):
        for row in (ROW_DJANGO_LTI, ROW_LTIJS, ROW_PROCTORING_JS, ROW_MCP_BRASIL):
            self.assertTrue(ca.evidence_complete(row), row[:60])


class FatalArmScope(unittest.TestCase):
    def test_the_fatal_arm_fails_on_a_refuted_absence_and_the_census_never_does(self):
        root, rel = corpus("🔴 There is **no maintained Python LTI library**.", ROW_DJANGO_LTI)
        try:
            self.assertEqual(ca.main(["--root", root, "--fatal", rel]), 1)
            self.assertEqual(ca.main(["--root", root, "--census"]), 0)
        finally:
            shutil.rmtree(root, ignore_errors=True)




class ClassesFoundByFailingOnItsOwnAuthor(unittest.TestCase):
    """🔴 `p392` ran the fatal arm over its OWN draft of the shelves and it failed on four
    candidates. Two were real defects in this instrument; both are controls now."""

    def test_class3b_a_quote_spanning_a_segment_boundary_is_still_a_quote(self):
        # The segmenter cuts on ':' and '. ', so quote detection run per-segment lost the
        # closing quote and reported `p392`'s own WITHDRAWAL as an unchecked absence.
        shelf = ('🔴 `p391`\'s conclusion is withdrawn. It read *"so there is no maintained '
                 'in-process Python LTI option: the edge must be Node or PHP."*')
        self.assertEqual(verdicts(shelf, ROW_DJANGO_LTI), [])

    def test_class5_a_struck_through_absence_is_a_retraction_not_a_claim(self):
        # This base retracts by striking through and saying what replaced it.  Reporting that
        # as an unchecked absence punishes the correction.
        shelf = ("- 🔴 **~~Proctoring and AI-detection have no credible permissive open-source "
                 "option~~ — WITHDRAWN.** There are two granted components.")
        self.assertEqual(verdicts(shelf, ROW_PROCTORING_JS), [])


class Ledger(unittest.TestCase):
    """A gate that fails on candidates the gap log has already adjudicated gets switched off;
    one that filters them silently hides the measurement.  So a pass subtracts a candidate
    only by writing down file, line, verdict and REASON."""

    def test_an_adjudicated_candidate_does_not_fail_the_fatal_arm(self):
        root, rel = corpus("🔴 There is **no maintained Python LTI library**.", ROW_DJANGO_LTI)
        led = os.path.join(root, "adjudicated.tsv")
        try:
            self.assertEqual(ca.main(["--root", root, "--fatal", rel]), 1)
            with open(led, "w", encoding="utf-8") as fh:
                fh.write("# file\tline\tverdict\treason\n")
                fh.write(f"{rel}\t1\tFALSE-POSITIVE\ttest control, see Gap 392-A\n")
            self.assertEqual(ca.main(["--root", root, "--fatal", rel, "--ledger", led]), 0)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_an_unledgered_line_still_fails(self):
        root, rel = corpus("🔴 There is **no maintained Python LTI library**.", ROW_DJANGO_LTI)
        led = os.path.join(root, "adjudicated.tsv")
        try:
            with open(led, "w", encoding="utf-8") as fh:
                fh.write(f"{rel}\t99\tFALSE-POSITIVE\twrong line on purpose\n")
            self.assertEqual(ca.main(["--root", root, "--fatal", rel, "--ledger", led]), 1)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
