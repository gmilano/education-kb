"""p541's controls for the grant-residue decomposition.

Every payload quoted is one of the 37 `UNKNOWN` rows in
`evidence/backlog-gated-slice2.2026-10-30-p540.tsv`, read first-hand from
`raw.githubusercontent.com` on 2026-10-30.  The class marked FP-1 is the false
positive this instrument's own draft had, recorded as a control.

🔵 No network: the payload text is inlined.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grant_residue as gr  # noqa: E402

# ── real payload openings, verbatim ──────────────────────────────────────────
ECL = ("Educational Community License Version 2.0, April 2007\n"
       "http://www.osedu.org/licenses/ECL-2.0\n\nTHE EDUCATIONAL COMMUNITY LICENSE\n")
SATA = ("The Star And Thank Author License (SATA)\n\nCopyright (c) <Qingdao University>\n\n"
        "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
        "of this software and associated documentation files (the \"Software\"), to deal\n")
OPEN_WEBUI = ("Open WebUI License\nCopyright (c) 2023- Open WebUI Inc.\n\n"
              "Redistribution and use in source and binary forms, with or without\n"
              "modification, are permitted provided that the following conditions are met:\n"
              "4. The \"Open WebUI\" name and branding may not be removed.\n")
PYSILICON = ("PySilicon Research License\nCopyright (c) 2026 Sundeep Rangan\n\n"
             "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
             "for NON-COMMERCIAL RESEARCH purposes only.\n")
KOSKI = ("Copyright (c) 2015 The Finnish National Board of Education - Opetushallitus\n\n"
         "This program is free software:  Licensed under the EUPL, Version 1.1 or - as\n"
         "soon as they will be approved by the European Commission - subsequent versions\n"
         "of the EUPL (the \"Licence\");\n\nYou may not use this work except in compliance "
         "with the Licence.\nYou may obtain a copy of the Licence at: "
         "https://joinup.ec.europa.eu/software/page/eupl\n")
GGCHECK = "YEAR: 2021\nCOPYRIGHT HOLDER: ggcheck authors\n"
PORTABILIS = ("LICENÇA PÚBLICA GERAL AFFERO GNU\nVersão 3, 19 de novembro de 2007\n\n"
              "Copyright (C) 2007 Free Software Foundation, Inc.\n" + ("x" * 35000))
NEW_BSD = ("New BSD License\nCopyright (c) 2012–2022 Educational Testing Service\n\n"
           "Redistribution and use in source and binary forms, with or without\n")
UNTITLED_MIT = ("Copyright (c) 2025 crewAI, Inc.\n\nPermission is hereby granted, free of "
                "charge, to any person obtaining a copy\nof this software\n")
ELASTIC = ("Elastic License 2.0\n\n## Acceptance\n\nBy using the software, you agree to all "
           "of the terms and conditions below.\n")
ZH_RESERVED = ("版权所有 (c) 2021，猿究生\n保留所有权利。\n\n感谢您选择 cloud-learning 在线教育产品。\n" + ("x" * 4000))


class TestBespokeGuard(unittest.TestCase):

    def test_fp1_a_stock_family_whose_name_contains_a_keyword_is_not_bespoke(self):
        """FP-1 — the draft matched a keyword list anywhere in the payload, so
        `Educational Community License` tripped on "Community License" and SIX
        ECL-2.0 payloads were graded bespoke.  ECL-2.0 is OSI-approved, is in
        both classifiers' tables, and is the Apereo sector's standard grant."""
        is_b, title = gr.bespoke_guard(ECL)
        self.assertFalse(is_b, title)

    def test_fp1b_a_cla_mentioned_in_prose_is_not_a_title(self):
        """The same draft caught `open-webui` on the string
        CONTRIBUTOR_LICENSE_AGREEMENT inside a sentence.  It IS bespoke, but
        for its title -- so the right answer reached the page for the wrong
        reason, which is the kind of luck a control should remove."""
        body = ("MIT License\n\nCopyright (c) 2026 X\n\nSee CONTRIBUTOR_LICENSE_AGREEMENT.md "
                "before submitting a pull request.\n")
        is_b, _ = gr.bespoke_guard(body)
        self.assertFalse(is_b)

    def test_a_bespoke_title_over_an_mit_body_is_flagged(self):
        is_b, title = gr.bespoke_guard(SATA)
        self.assertTrue(is_b)
        self.assertIn("Star And Thank Author", title)

    def test_open_webui_is_flagged_on_its_own_title(self):
        """No keyword list would have caught `Open WebUI License`; the
        title-block rule does.  This base has known the branding clause since
        p441 and both classifiers still answer BSD-3-Clause."""
        is_b, title = gr.bespoke_guard(OPEN_WEBUI)
        self.assertTrue(is_b)
        self.assertEqual(title, "Open WebUI License")

    def test_a_research_only_licence_over_an_mit_body_is_flagged(self):
        is_b, title = gr.bespoke_guard(PYSILICON)
        self.assertTrue(is_b)
        self.assertIn("Research License", title)

    def test_a_stock_title_in_portuguese_is_stock(self):
        """540-B's flagship example.  The title is Portuguese and the family is
        ordinary AGPL-3.0; `backlog-gate.spdx_of` already names it."""
        is_b, _ = gr.bespoke_guard(PORTABILIS)
        self.assertFalse(is_b)

    def test_an_untitled_body_is_not_bespoke(self):
        """p314's untitled-grant class: no title is not a bespoke title."""
        self.assertFalse(gr.bespoke_guard(UNTITLED_MIT)[0])
        self.assertFalse(gr.bespoke_guard(GGCHECK)[0])

    def test_new_bsd_is_stock(self):
        self.assertFalse(gr.bespoke_guard(NEW_BSD)[0])

    def test_markdown_heading_marks_are_stripped_from_the_title(self):
        is_b, title = gr.bespoke_guard("## ODC Open Database License (ODbL)\n\n### Preamble\n")
        self.assertTrue(is_b)
        self.assertTrue(title.startswith("ODC"), title)


class TestByReference(unittest.TestCase):

    def test_a_short_notice_naming_an_authority_is_by_reference(self):
        ref, authority = gr.by_reference(KOSKI)
        self.assertTrue(ref)
        self.assertIn("EUPL", authority)
        self.assertIn("1.1", authority)

    def test_the_version_is_read_off_the_notice_not_assumed(self):
        """The only EUPL title either classifier carries is 1.2; seven of these
        say 1.1.  A gate that assumes the version it knows publishes a date and
        a set of obligations the repository never granted."""
        _, authority = gr.by_reference(KOSKI)
        self.assertNotIn("1.2", authority)

    def test_a_reproduced_grant_is_not_by_reference(self):
        """35 kB of GPL text is the grant, not a pointer to it."""
        self.assertFalse(gr.by_reference(PORTABILIS)[0])

    def test_a_notice_with_no_url_is_not_by_reference(self):
        """Without somewhere to obtain the text, this is an assertion rather
        than a reference, and must not be graded as a citable grant."""
        self.assertFalse(gr.by_reference(
            "Copyright (c) 2020 X\nLicensed under the EUPL, Version 1.1\n")[0])


class TestStubPayload(unittest.TestCase):

    def test_the_r_usethis_stub_is_a_stub(self):
        """`usethis::use_mit_license()` writes the fill-in to LICENSE and the
        MIT text to LICENSE.md.  Confirmed first-hand at p541: all three of
        rstudio/ggcheck, rstudio/tblcheck and shmercer/writeAlizer serve
        `# MIT License` at LICENSE.md."""
        self.assertTrue(gr.stub_payload(GGCHECK))

    def test_a_short_real_notice_is_not_a_stub(self):
        """`opetushallitus/ataru` is 296 B and a real grant notice.  Size alone
        must not decide this."""
        self.assertFalse(gr.stub_payload(KOSKI))

    def test_a_full_grant_is_not_a_stub(self):
        self.assertFalse(gr.stub_payload(UNTITLED_MIT))


class TestResidueCause(unittest.TestCase):
    """The decomposition, on one payload per class."""

    def test_the_five_classes(self):
        cases = [
            (ECL, "ECL-2.0", "NAMED"),
            (PORTABILIS, "AGPL-3.0", "NAMED"),
            (UNTITLED_MIT, "MIT", "NAMED"),
            (SATA, "MIT", "BESPOKE-OVER-STOCK"),
            (OPEN_WEBUI, "BSD-3-Clause", "BESPOKE-OVER-STOCK"),
            (PYSILICON, "MIT", "BESPOKE-OVER-STOCK"),
            (ELASTIC, None, "BESPOKE"),
            (ZH_RESERVED, None, "BESPOKE"),
            (KOSKI, None, "BY-REFERENCE"),
            (GGCHECK, None, "LADDER-STUB"),
        ]
        for text, named, expected in cases:
            cause, _ = gr.residue_cause(text, named_family=named)
            self.assertEqual(cause, expected,
                             f"{expected} expected for {text.splitlines()[0][:40]!r}, got {cause}")

    def test_the_guard_runs_before_recall_because_of_what_an_error_costs(self):
        """A false permissive grant is the error a studio BUILDS on, so the
        bespoke guard must win over any family the body matched.  If this
        control ever fails, 540-B's patch has been applied without the guard
        and six refusals have become grants."""
        for text, named in ((SATA, "MIT"), (PYSILICON, "MIT"),
                            (OPEN_WEBUI, "BSD-3-Clause"), (ELASTIC, "MIT")):
            cause, _ = gr.residue_cause(text, named_family=named)
            self.assertTrue(cause.startswith("BESPOKE"), (cause, named))

    def test_every_cause_is_in_the_published_vocabulary(self):
        for text in (ECL, SATA, ELASTIC, KOSKI, GGCHECK, PORTABILIS, UNTITLED_MIT):
            cause, _ = gr.residue_cause(text, named_family="MIT")
            self.assertIn(cause, gr.CAUSES)


if __name__ == "__main__":
    unittest.main(verbosity=2)
