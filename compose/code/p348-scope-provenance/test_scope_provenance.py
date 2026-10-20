#!/usr/bin/env python3
"""p348 -- offline controls for ACTIONs ZZ-z, ZZ-u, ZZ-y, ZZ-ab and ZZ-w.

No network.  Every fixture is the shape of a payload this base has actually read: the
NCSA grant inside `cs341-illinois/coursebook`'s `LICENSE` DIRECTORY, the ECL-2.0 of the
Sakai/Apereo stack, the BOM-prefixed MIT of `zaikaman/SGU-Academic-MCP`, the vendored
Apache-2.0 at `.agents/skills/skill-creator/LICENSE.txt` in `likr/canvas-lms-agent`, and
the Bootstrap grant that this instrument's OWN first run graded as
`AcademicsToday/academicstoday-django`'s.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scope_provenance as sp  # noqa: E402

MIT = ("MIT License\n\nCopyright (c) 2026 %s\n\nPermission is hereby granted, free of "
       "charge, to any person obtaining a copy of this software, to deal in the "
       "Software without restriction, including without limitation the rights to use, "
       "copy, modify, merge, publish, distribute, sublicense, and/or sell copies.\n\n"
       "The above copyright notice and this permission notice shall be included in all "
       "copies.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND. IN "
       "NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, "
       "DAMAGES OR OTHER LIABILITY.\n")
APACHE = ("                                 Apache License\n"
          "                           Version 2.0, January 2004\n"
          "   Licensed under the Apache License, Version 2.0 (the \"License\");\n"
          "   Copyright [yyyy] [name of copyright owner]\n")
ECL = ("Educational Community License, Version 2.0\n\nThe Educational Community License "
       "version 2.0 is an Apache License, Version 2.0 derivative. Licensed under the "
       "Apache License, Version 2.0 with the following modification.\n"
       "Copyright (c) 2024 Apereo Foundation\n")
NCSA = ("University of Illinois/NCSA Open Source License\n\nCopyright (c) 2026 "
        "University of Illinois at Urbana-Champaign. All rights reserved.\n\n"
        "Redistribution and use in source and binary forms, with or without "
        "modification, are permitted provided that the following conditions are met:\n"
        "Neither the names of the University of Illinois nor NCSA may be used.\n")
BSD3 = ("BSD 3-Clause License\n\nCopyright (c) 2024 Jupyter Development Team\n\n"
        "Redistribution and use in source and binary forms, with or without "
        "modification, are permitted provided that the following conditions are met:\n"
        "Neither the name of the copyright holder nor the names of its contributors.\n")


class FamilyVocabulary(unittest.TestCase):
    """ACTION ZZ-ab: NCSA enters the vocabulary, and ORDER is the whole function."""

    def test_ncsa_is_read_as_ncsa(self):
        self.assertEqual(sp.family_of(NCSA), "NCSA")

    def test_ncsa_is_NOT_read_as_MIT_and_that_is_the_whole_point(self):
        # Measured, not assumed.  `cs341-illinois/coursebook` -> `LICENSE/LICENSE.code`
        # (1 698 B, read at the pin) was graded MIT by the canonical p436 detector,
        # because NCSA's permission clause is MIT-PHRASED.  NCSA carries a BSD-style
        # no-endorsement clause naming the University of Illinois and NCSA; MIT carries
        # only the notice.  Grading NCSA as MIT UNDERSTATES what a client owes, which is
        # the UNSAFE direction -- p347 expected an abstention, and an abstention fails
        # safe under P250.
        ncsa_with_mit_phrasing = (
            "University of Illinois/NCSA Open Source License\n\n"
            "Copyright (c) 2018-2019 University of Illinois. All rights reserved.\n\n"
            "Permission is hereby granted, free of charge, to any person obtaining a "
            "copy of this software and associated documentation files, to deal with the "
            "Software without restriction, including without limitation the rights to "
            "use, copy, modify, merge, publish, distribute, sublicense.\n"
            "Neither the names of the University of Illinois nor NCSA, nor the names of "
            "its contributors may be used to endorse or promote products.\n")
        self.assertEqual(sp.family_of(ncsa_with_mit_phrasing), "NCSA")

    def test_the_mit_rung_still_answers_MIT_on_an_actual_mit_payload(self):
        # the other direction of the same ordering: teaching NCSA must not cost MIT
        self.assertEqual(sp.family_of(MIT % "ACME"), "MIT")

    def test_bsd_still_reads_as_bsd(self):
        # the other direction of the same ordering: teaching NCSA must not cost BSD
        self.assertEqual(sp.family_of(BSD3), "BSD-3-Clause")

    def test_ecl_is_not_apache_even_in_the_variant_that_names_apache(self):
        # ACTION ZZ-ab also asked for ECL-2.0 to be re-checked.  🟡 The re-check found NO
        # defect: `sakaiproject/sakai`'s real 11 120-byte LICENSE names "apache license"
        # ZERO times, so the canonical detector grades it correctly where it already sits.
        # This fixture is the SHORT derivative-preamble variant, which does name Apache --
        # so the ordering here is a guard against a shape that exists, not a fix for a
        # measured failure.  Recorded as a precaution, not as a finding.
        self.assertEqual(sp.family_of(ECL), "ECL-2.0")

    def test_apache_is_still_apache(self):
        self.assertEqual(sp.family_of(APACHE), "Apache-2.0")

    def test_mit(self):
        self.assertEqual(sp.family_of(MIT % "ACME"), "MIT")

    def test_a_byte_order_mark_does_not_hide_a_stock_grant(self):
        # ACTION ZZ-w: `zaikaman/SGU-Academic-MCP` opens EF BB BF then "MIT License"
        self.assertEqual(sp.family_of("﻿" + MIT % "Saigon University"), "MIT")

    def test_not_a_grant_text_reads_UNKNOWN(self):
        # a path whose NAME contains the word is not a grant (p441's icon component)
        self.assertEqual(sp.family_of("<template><Icon name='copyright'/></template>"),
                         "UNKNOWN")


class HolderChannel(unittest.TestCase):
    """ACTION ZZ-y, and the defect this instrument's own first run shipped."""

    def test_the_holder_line_is_the_holder_line(self):
        self.assertEqual(sp.holder_of(MIT % "Twitter, Inc"), ["Twitter, Inc"])

    def test_mit_boilerplate_is_NOT_a_holder(self):
        # "The above copyright notice..." and "...OR COPYRIGHT HOLDERS BE LIABLE..."
        # both contain the word.  Reading them imports {notice, permission, shall,
        # holders, liable, claim, damages} into EVERY MIT payload's token set, which is
        # how the first run graded Twitter's vendored Bootstrap grant as the
        # repository's own.
        toks = sp.holder_tokens(sp.holder_of(MIT % "Twitter, Inc"))
        for word in ("notice", "permission", "shall", "holders", "liable", "claim",
                     "damages"):
            self.assertNotIn(word, toks)

    def test_apache_appendix_template_is_a_FORM_not_a_holder(self):
        self.assertEqual(sp.holder_of(APACHE), [])

    def test_a_bom_does_not_hide_the_holder_either(self):
        self.assertEqual(sp.holder_of("﻿" + MIT % "Saigon University"),
                         ["Saigon University"])

    def test_multiple_holder_lines_are_all_kept(self):
        # ls1intum/Ares2 ships five copyright lines in 1 345 B of verbatim MIT, and
        # GitHub's own licence API reports NOASSERTION on it
        txt = ("MIT License\n\nCopyright (c) 2019 Technical University of Munich\n"
               "Copyright (c) 2024 TUM School of Computation, Information and "
               "Technology\n" + MIT % "Research Group of Applied Education Technologies")
        self.assertEqual(len(sp.holder_of(txt)), 3)

    def test_an_institution_in_the_holder_line_is_a_PLACEMENT_channel(self):
        # public, aggregate text -- it survives the PII refusal that took author
        # e-mail domains away from p346
        got = sp.institution_of(["Technical University of Munich", "Twitter, Inc",
                                 "Universidade de São Paulo", "Dodona"])
        self.assertEqual(got, ["Technical University of Munich",
                               "Universidade de São Paulo"])

    def test_a_company_name_is_not_an_institution(self):
        self.assertEqual(sp.institution_of(["PT Motiolabs Digital Indonesia"]), [])


class Provenance(unittest.TestCase):
    """ACTION ZZ-u: root grants the repository, a subtree grants itself, and a vendored
    path grants nothing -- decided by the PAYLOAD, never by a directory blacklist."""

    def test_vendored_grant_is_FOREIGN(self):
        self.assertEqual(
            sp.provenance("AcademicsToday/academicstoday-django",
                          sp.holder_of(MIT % "Twitter, Inc"), set()),
            "FOREIGN")

    def test_a_vendored_path_NOT_on_any_blacklist_is_still_FOREIGN(self):
        # `.agents/skills/skill-creator/` is in no blacklist in this repository, which
        # is exactly why p441's EXCLUDE_DIR_RE missed it: widening a list cannot fix a
        # list (p441's own docstring, first paragraph)
        self.assertEqual(sp.provenance("likr/canvas-lms-agent",
                                       sp.holder_of(MIT % "Anthropic"), set()),
                         "FOREIGN")

    def test_the_projects_own_subtree_grant_is_OWN_via_the_root_holder(self):
        root = sp.holder_tokens(sp.holder_of(MIT % "Dodona"))
        self.assertEqual(sp.provenance("dodona-edu/dolos",
                                       sp.holder_of(MIT % "Dodona"), root), "OWN")

    def test_containment_folds_an_owner_handle(self):
        self.assertEqual(sp.provenance("dodona-edu/dolos", ["Dodona"], set()), "OWN")

    def test_a_holderless_payload_is_HOLDER_ABSENT_not_FOREIGN(self):
        self.assertEqual(sp.provenance("x/y", [], set()), "HOLDER-ABSENT")

    def test_scope_is_decided_by_position(self):
        self.assertEqual(sp.scope_of("LICENSE"), "ROOT")
        self.assertEqual(sp.scope_of("LICENSE.md"), "ROOT")
        self.assertEqual(sp.scope_of("packages/xapi/LICENSE"), "SUBTREE")
        self.assertEqual(sp.scope_of(".agents/skills/skill-creator/LICENSE.txt"),
                         "SUBTREE")


class CandidatePaths(unittest.TestCase):
    """The finding channel: a PATTERN over every path at any depth, never a name list."""

    def test_uppercase_extension_is_found(self):
        # openedx/XBlock ships LICENSE.TXT and three successive name-list widenings
        # missed it (p436's 14 names, p440's 41)
        self.assertIn("LICENSE.TXT", sp.candidate_paths(["LICENSE.TXT", "setup.py"]))

    def test_british_spelling_and_lowercase_are_found(self):
        self.assertEqual(sp.candidate_paths(["licence.md"]), ["licence.md"])

    def test_depth_is_found(self):
        self.assertEqual(sp.candidate_paths(["aoe-web-frontend/LICENSE"]),
                         ["aoe-web-frontend/LICENSE"])

    def test_a_licence_DIRECTORY_s_children_are_found(self):
        # ACTION ZZ-v: `LICENSE` can be a directory
        self.assertEqual(sorted(sp.candidate_paths(
            ["LICENSE/LICENSE.code", "LICENSE/README.md"])),
            ["LICENSE/LICENSE.code", "LICENSE/README.md"])

    def test_a_badge_image_is_not_a_grant(self):
        self.assertEqual(sp.candidate_paths(
            ["docs/licence-EUPL 1.2-brightgreen.svg"]), [])

    def test_a_source_file_named_for_the_word_is_not_a_grant(self):
        self.assertEqual(sp.candidate_paths(
            ["lib/KIcon/material-icons/copyright/baseline.vue",
             "src/copyrightandotherrestrictions.xsl"]), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
