#!/usr/bin/env python3
"""`P800` -- a region comes from an INSTITUTION the artifact names, never from a person's name.

Sixty-fifth pass, 2026-10-08. Single file on purpose (see `p798`/`p799`).

    python3 test_region_provenance.py
    python3 -I test_region_provenance.py

WHY.  This pass admitted three rows whose maintainers carry names that a
reader could file under a country in about a second, and in every one of the
three the repository itself says NOTHING about where it is built or deployed.
Filing them by the shape of a surname would have produced three regional
placements out of thin air -- and `region` is a CLOSED field this KB filters
on, so a guess does not read as a guess downstream: it reads as data.

THE CONTRAST THAT MAKES THE RULE, and both halves were measured:

  * `educredentials/ec-issuer` is EMEA because its own README points
    deployment at `git.ia.surfsara.nl/surf-internal/...`, which is SURF, the
    Dutch national education-ICT cooperative, and because it implements the
    European Learner Model.  An INSTITUTION and a STANDARD placed it.
  * `GhaithAlHallak8/moodler-mcp`, `Jawadh-Salih/moodle-mcp-server` and
    `TanimowoObaloluwaDavid/credential-lens` name no institution, no
    jurisdiction, no deployment, and no regional standard.  Grepped, not
    assumed: the probe looked for `universit|ministr|government|deploy|
    country|region|instituti|EU|GDPR|FERPA|AI Act|.edu|.ac.` and the three
    READMEs returned nothing placing them.  So all three are `Global`.

AND IT IS NOT ONLY AN ACCURACY RULE.  Inferring a person's nationality from
their name to fill a business field is wrong twice over: unreliable, and not
this shelf's business.  `Global` is the honest value and it costs nothing.
"""
import unittest

# Measured this pass. `placed_by` is the string IN THE ARTIFACT that places it;
# None means the grep came back empty.
ROWS = {
    "educredentials/ec-issuer": {
        "region": "EMEA",
        "placed_by": "README deployment target git.ia.surfsara.nl (SURF, NL) + European Learner Model",
        "maintainer_name_suggests": "Bèr Kessels",
    },
    "GhaithAlHallak8/moodler-mcp": {
        "region": "Global",
        "placed_by": None,
        "maintainer_name_suggests": "Ghaith AlHallak",
    },
    "Jawadh-Salih/moodle-mcp-server": {
        "region": "Global",
        "placed_by": None,
        "maintainer_name_suggests": "Jawadh",
    },
    "TanimowoObaloluwaDavid/credential-lens": {
        "region": "Global",
        "placed_by": None,
        "maintainer_name_suggests": "Tanimowo Obaloluwa David",
    },
}

CLOSED_VOCABULARY = ("North America", "EMEA", "APAC", "LATAM", "Global")


def region_of(row):
    """`P800`: placed by an institution the artifact names, else `Global`."""
    return row["region"] if row.get("placed_by") else "Global"


def is_placed(row):
    return row.get("placed_by") is not None


class RegionIsClosedAndEarned(unittest.TestCase):
    def test_every_region_is_in_the_closed_vocabulary(self):
        for repo, row in ROWS.items():
            self.assertIn(row["region"], CLOSED_VOCABULARY, repo)

    def test_the_only_placed_row_is_the_one_naming_an_institution(self):
        placed = [r for r, v in ROWS.items() if is_placed(v)]
        self.assertEqual(placed, ["educredentials/ec-issuer"])

    def test_an_unplaced_row_resolves_to_Global(self):
        for repo, row in ROWS.items():
            if not is_placed(row):
                self.assertEqual(region_of(row), "Global", repo)

    def test_a_maintainer_name_never_moves_a_region(self):
        """The negative control, and it is the whole file.

        Every unplaced row carries a personal name. If a name could place a
        row, these three would not all be `Global` -- so the assertion that
        they ARE all `Global` is the guard."""
        unplaced = [v for v in ROWS.values() if not is_placed(v)]
        self.assertEqual(len(unplaced), 3)
        self.assertTrue(all(v["maintainer_name_suggests"] for v in unplaced),
                        "all three do carry a personal name")
        self.assertEqual({region_of(v) for v in unplaced}, {"Global"})

    def test_placing_a_row_requires_a_quotable_string(self):
        for repo, row in ROWS.items():
            if is_placed(row):
                self.assertTrue(len(row["placed_by"]) > 20,
                                f"{repo}: a placement must cite what placed it")


class TheVocabularyDoesNotDrift(unittest.TestCase):
    def test_country_names_are_not_regions(self):
        for bad in ("Netherlands", "NL", "Nigeria", "Sri Lanka", "Europe",
                    "Latam", "Brazil", "Syria"):
            self.assertNotIn(bad, CLOSED_VOCABULARY)

    def test_the_vocabulary_is_exactly_five(self):
        self.assertEqual(len(CLOSED_VOCABULARY), 5)

    def test_EMEA_is_the_bucket_and_the_country_lives_in_prose(self):
        """SURF is Dutch; the field says EMEA and the prose says NL."""
        row = ROWS["educredentials/ec-issuer"]
        self.assertEqual(row["region"], "EMEA")
        self.assertIn("NL", row["placed_by"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
