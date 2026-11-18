"""p885 controls for the symref-first grant ladder (discharges `884-G2`).

These tests pin the LOGIC of the ladder against the measurements p885 recorded
first-hand, so a later edit cannot silently reintroduce the defect. The network
measurements themselves live in
`evidence/grant-ladder-controls.2026-11-18-p885.tsv` and
`evidence/default-branch-census.2026-11-18-p885.tsv`.

Run:  python3 -m pytest test_symref_ladder.py -q
  or: python3 test_symref_ladder.py
"""
import re
import subprocess
import unittest
from pathlib import Path

LADDER = Path(__file__).with_name("fetch_grants.sh")

# The 13 permissive repositories measured as having a non-standard default branch
# AND no `main`/`master` branch at all. The old two-name ladder reported
# NO-GRANT-FILE on every one; 12 carry a real grant on their default ref.
MANUFACTURED_ABSENCE = {
    "ImperialCollegeLondon/sam-ahadi": ("develop", "MIT", 1101),
    "ImperialCollegeLondon/pytest_template_application": ("develop", "MIT", 1080),
    "ImperialCollegeLondon/poetry_template": ("develop", "MIT", 1080),
    "UoA-eResearch/unity_vr_swim": ("quest", "MIT", 1101),
    "epfl-lasa/obstacleAvoidance_Cpp": ("Branch_August", "MIT", 1078),
    "eth-sri/abstraqt": ("publish", "MIT", 1054),
    "kmc-jp/reikai-log": ("trunk", "Apache-2.0", 11357),
    "ox-it/OxfordIDN_Shiny-App-Templates": ("gh-pages", "MIT", 1086),
    "ox-it/wl-roster2": ("sakai-10.x", "ECL-2.0", 11110),
    "pulibrary/scarlettiger": ("trunk", "BSD-2-Clause", 1338),
    "pulibrary/sipper": ("development", "BSD-2-Clause", 1312),
    "uspdev/laravel-printing": ("v1", "MIT", 1100),
}
# The one that is NOT a ladder failure: the field says MIT, the only branch has no
# licence file. Tracked as `885-G1`, not as a bug in this script.
METADATA_ASSERTS_PAYLOAD_DENIES = "ox-it/OxfordIDN_Case-Studies"


class TestLadderShape(unittest.TestCase):
    """The defect was structural, so these assertions are about structure."""

    def setUp(self):
        self.src = LADDER.read_text(encoding="utf-8")

    def test_shell_syntax_is_valid(self):
        r = subprocess.run(["sh", "-n", str(LADDER)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_resolves_default_branch_via_symref(self):
        """The whole point of p885: ask git what the default branch IS."""
        self.assertIn("ls-remote", self.src)
        self.assertIn("--symref", self.src)

    def test_symref_is_probed_before_the_two_guesses(self):
        """Order matters. `main`/`master` must be the FALLBACK, not the entry point."""
        first_probe = self.src.index('probe_ref "$slug" "$dref"')
        fallback = self.src.index("for ref in main master")
        self.assertLess(
            first_probe, fallback,
            "the resolved default ref must be probed before main/master",
        )

    def test_fallback_does_not_reprobe_the_resolved_ref(self):
        """A resolved ref of `main` must not be probed twice."""
        self.assertIn('[ "$ref" = "$dref" ] && continue', self.src)

    def test_dual_grant_arm_also_tries_the_resolved_ref(self):
        """p884's RWTH-OS/eduOS-rs split-file case must not regress to two names."""
        self.assertIn("for ref in $dref main master", self.src)

    def test_miss_reports_the_ref_it_resolved(self):
        """A 404 must never again be indistinguishable from 'no licence exists'."""
        self.assertIn("UNRESOLVED", self.src)
        self.assertIn("no-grant", self.src)

    def test_every_hit_is_byte_identified(self):
        """Bytes + sha256_12, because this KB does not carry unverifiable grants."""
        self.assertIn("sha256sum", self.src)
        self.assertIn("stat -c%s", self.src)


class TestMeasuredExposure(unittest.TestCase):
    """Pin p885's measured numbers so a later pass cannot quietly restate them."""

    def test_census_totals_are_internally_consistent(self):
        main, master, other, total = 3976, 2166, 344, 6486
        self.assertEqual(main + master + other, total)
        self.assertAlmostEqual(100 * other / total, 5.3, places=1)

    def test_manufactured_absence_rate(self):
        """13 of 49 permissive non-standard-default repos = 26.5%."""
        self.assertEqual(len(MANUFACTURED_ABSENCE) + 1, 13)
        self.assertAlmostEqual(100 * 13 / 49, 26.5, places=1)

    def test_recovery_rate_is_12_of_13(self):
        self.assertEqual(len(MANUFACTURED_ABSENCE), 12)
        self.assertNotIn(METADATA_ASSERTS_PAYLOAD_DENIES, MANUFACTURED_ABSENCE)

    def test_no_recovered_default_branch_is_main_or_master(self):
        """If one were, it would not have been a symref find at all."""
        for slug, (ref, _, _) in MANUFACTURED_ABSENCE.items():
            self.assertNotIn(ref, ("main", "master"), slug)

    def test_recovered_grants_are_permissive(self):
        """The exposure that matters is permissive code reported as unlicensed."""
        permissive = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ECL-2.0"}
        for slug, (_, spdx, _) in MANUFACTURED_ABSENCE.items():
            self.assertIn(spdx, permissive, slug)

    def test_the_subject_area_find_is_present(self):
        """ox-it/wl-roster2 is why this gap was worth discharging at all."""
        ref, spdx, size = MANUFACTURED_ABSENCE["ox-it/wl-roster2"]
        self.assertEqual((ref, spdx, size), ("sakai-10.x", "ECL-2.0", 11110))


class TestCalibration(unittest.TestCase):
    """The claim is bounded: this defect manufactured ABSENCE, not wrong grants."""

    # Fixtures that DO retain main/master: fallback bytes == default-ref bytes.
    IDENTICAL_ACROSS_REFS = {
        "odoo/odoo": ("20.0", "abc09dad5f84", 43529),
        "openeducat/openeducat_erp": ("19.0", "528f84036800", 8241),
        "cilt-uct/sakai-skin-vula": ("r/23.x", "0688f62d04f1", 11120),
        "ls1intum/Artemis": ("develop", "63a0a2b4d6d9", 1091),
        "vishalsachdev/canvas-mcp": ("main", "5385a26e2fac", 1071),
    }

    def test_five_fixtures_calibrate_the_claim(self):
        self.assertEqual(len(self.IDENTICAL_ACROSS_REFS), 5)

    def test_shas_are_well_formed_twelve_hex(self):
        for slug, (_, sha, _) in self.IDENTICAL_ACROSS_REFS.items():
            self.assertRegex(sha, r"^[0-9a-f]{12}$", slug)

    def test_release_branch_defaults_are_the_norm_for_mature_platforms(self):
        """odoo 20.0, openeducat 19.0, sakai r/23.x -- none is main/master."""
        for slug in ("odoo/odoo", "openeducat/openeducat_erp", "cilt-uct/sakai-skin-vula"):
            ref = self.IDENTICAL_ACROSS_REFS[slug][0]
            self.assertNotIn(ref, ("main", "master"), slug)

    def test_artemis_row_label_was_imprecise_not_wrong(self):
        """The KB row says `main/LICENSE`; the default branch is `develop`.

        Bytes are identical on main, master and develop, so the verdict (MIT)
        stands and only the ref label was imprecise. Pinned so the correction
        is not later mistaken for a licence change.
        """
        ref, sha, size = self.IDENTICAL_ACROSS_REFS["ls1intum/Artemis"]
        self.assertEqual(ref, "develop")
        self.assertEqual((sha, size), ("63a0a2b4d6d9", 1091))


if __name__ == "__main__":
    unittest.main(verbosity=2)
