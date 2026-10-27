#!/usr/bin/env python3
"""Controls for the p467 grant-class axis.

Two legs. The SYNTHETIC leg fixes the shape of each class, including the three
`Gap 466-A` rows and the one direction that must never fail (a permissive
payload graded UNSELLABLE, which would discard real supply). The LIVE leg is run
by sweep.py against payloads fetched first-hand this pass.
"""
import sys
from grant_class import grade, sellable

C = []  # (label, payload, expect_family_prefix, expect_class, expect_line1)

def add(label, payload, fam, cls, line1=None):
    C.append((label, payload, fam, cls, line1))

# --- the three Gap 466-A rows, by payload shape -----------------------------
add("CC-BY-NC-4.0 (cn-math-taxonomy shape)",
    "Creative Commons Attribution-NonCommercial 4.0 International\n\nBy exercising...",
    "CC-BY-NC", "UNSELLABLE", 1)
add("CC-BY-SA-4.0 (education-agent-skills shape)",
    "Creative Commons Attribution-ShareAlike 4.0 International\n\nBy exercising...",
    "CC-BY-SA", "CONTENT_NOT_SOFTWARE", 1)
add("Elastic-2.0 (advisingapp shape)",
    "Elastic License 2.0\n\nURL: https://www.elastic.co/licensing/elastic-license\n",
    "Elastic-2.0", "UNSELLABLE", 1)

# --- the classes that must stay sellable ------------------------------------
add("MIT, titled", "MIT License\n\nCopyright (c) 2026 X\n\nPermission is hereby granted, free of charge,",
    "MIT", "PERMISSIVE", 1)
add("MIT, untitled (bare copyright first)",
    "Copyright (c) 2026 Somebody\n\nPermission is hereby granted, free of charge, to any person",
    "MIT", "PERMISSIVE", 0)
add("Apache-2.0 (version on line 2 -- the under-specification)",
    "                                 Apache License\n                           Version 2.0, January 2004\n",
    "Apache-2.0", "PERMISSIVE", 1)
add("Apache-2.0 short-form header",
    "Copyright 2026 X\n\nLicensed under the Apache License, Version 2.0 (the \"License\");",
    "Apache-2.0", "PERMISSIVE", 0)
add("BSD-3-Clause", "BSD 3-Clause License\n\nCopyright (c) 2026\n\nRedistribution and use in source and binary forms",
    "BSD", "PERMISSIVE", 1)
add("BSD, untitled", "Copyright (c) 2026\n\nRedistribution and use in source and binary forms, with or without",
    "BSD", "PERMISSIVE", 0)
add("ISC", "ISC License\n\nCopyright (c) 2026\n\nPermission to use, copy, modify, and/or distribute",
    "ISC", "PERMISSIVE", 1)
add("Unlicense", "This is free and unencumbered software released into the public domain.\n",
    "Unlicense", "PUBLIC_DOMAIN", 1)
add("CC0-1.0", "Creative Commons CC0 1.0 Universal\n\nStatement of Purpose\n",
    "CC0-1.0", "PUBLIC_DOMAIN", 1)
add("MPL-2.0", "Mozilla Public License Version 2.0\n\n1. Definitions\n", "MPL-2.0", "WEAK_COPYLEFT", 1)

# --- the copyleft ladder, version-graded where the payload states it --------
add("AGPL-3.0", "                    GNU AFFERO GENERAL PUBLIC LICENSE\n                       Version 3, 19 November 2007\n",
    "AGPL-3.0", "NETWORK_COPYLEFT", 1)
add("GPL-3.0", "                    GNU GENERAL PUBLIC LICENSE\n                       Version 3, 29 June 2007\n",
    "GPL", "STRONG_COPYLEFT", 1)
add("GPL-2.0", "                    GNU GENERAL PUBLIC LICENSE\n                       Version 2, June 1991\n",
    "GPL", "STRONG_COPYLEFT", 1)
add("LGPL (not GPL -- p454's defect 1)",
    "                   GNU LESSER GENERAL PUBLIC LICENSE\n                       Version 3, 29 June 2007\n",
    "LGPL", "WEAK_COPYLEFT", 1)
add("EUPL", "European Union Public Licence v. 1.2\n\nEUPL (c) the European Union 2007, 2016\n",
    "EUPL", "WEAK_COPYLEFT", 1)

# --- the rest of the UNSELLABLE set the gap names ---------------------------
add("BUSL-1.1", "Business Source License 1.1\n\nParameters\n", "BUSL-1.1", "UNSELLABLE", 1)
add("SSPL", "Server Side Public License\nVERSION 1, October 16, 2018\n", "SSPL", "UNSELLABLE", 1)
add("PolyForm Noncommercial", "PolyForm Noncommercial License 1.0.0\n\n<https://polyformproject.org>\n",
    "PolyForm-NC", "UNSELLABLE", 1)
add("Commons Clause", "Commons Clause License Condition v1.0\n\nThe Software is provided to you",
    "CommonsClause", "UNSELLABLE", 1)
add("bespoke source-available (nakafa shape)",
    "Nakafa Source Available License 2.0\n\nIt is not open source, and it is not free to reuse.\n",
    "NOT-OSI", "UNSELLABLE", 1)

# --- absence and the UNSTATED floor -----------------------------------------
add("no payload at any root path", None, "NO-ROOT-GRANT", "NO_GRANT", 0)
add("payload served, nothing matched", "Thanks for reading this repository.\n\nHave a nice day.\n",
    "UNSTATED", "UNSTATED", 0)

# --- the false-positive direction that costs supply -------------------------
add("MIT whose first line is 'All rights reserved' (p454's near-miss)",
    "Copyright (c) 2026 X. All rights reserved.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy",
    "MIT", "PERMISSIVE", 0)
add("CC-BY (attribution only) is NOT unsellable",
    "Creative Commons Attribution 4.0 International\n\nBy exercising the Licensed Rights\n",
    "CC-BY", "CONTENT_NOT_SOFTWARE", 1)
add("ODbL is content, not unsellable",
    "ODC Open Database License (ODbL)\n\nPreamble\n", "ODbL", "CONTENT_NOT_SOFTWARE", 1)

# --- v2: the six defect classes, each as a control -------------------------
# Defect 1: the MIT grant SENTENCE inside a bespoke restrictive licence.
add("PageLM Community License (MIT sentence + NC + revenue share)",
    "# PageLM Community License\n\n**Copyright (c) 2025 nullure & recabasic**\n\n"
    "Permission is hereby granted, free of charge, to any person obtaining a copy of this "
    "software and associated documentation files (the \"Software\"), to use, copy, modify, "
    "and run the Software for **personal, educational, or non-commercial research purposes**, "
    "subject to the terms and conditions set forth herein.\n\n"
    "### 4. Revenue Sharing Requirement\nIf the Software is used for Commercial Use a "
    "revenue-sharing agreement must be executed with the copyright holders.\n",
    "NOT-OSI", "UNSELLABLE", 0)
add("stock MIT is NOT caught by the restriction override",
    "MIT License\n\nCopyright (c) 2026 X\n\nPermission is hereby granted, free of charge, to any "
    "person obtaining a copy of this software, to deal in the Software without restriction, "
    "including without limitation the rights to use, copy, modify, merge, publish, distribute, "
    "sublicense, and/or sell copies of the Software\n",
    "MIT", "PERMISSIVE", 1)
add("untitled MIT with no restriction stays PERMISSIVE",
    "Copyright (c) 2026 Somebody\n\nPermission is hereby granted, free of charge, to any person "
    "obtaining a copy of this software and associated documentation files, to deal in the "
    "Software without restriction\n",
    "MIT", "PERMISSIVE", 0)
# Defect 2: pointers, in-repo and cross-repo.
add("cross-repo pointer (aimmo shape)",
    "# License\n\nFind our license [here](https://github.com/ocadotechnology/codeforlife-workspace/blob/main/LICENSE.md).\n",
    "POINTER_CROSS_REPO", "POINTER_CROSS_REPO", 0)
add("in-repo pointer (ckeditor shape)",
    "# Software License Agreement\n\nThe license for this repository is maintained in [`packages/ckeditor5/LICENSE.md`](packages/ckeditor5/LICENSE.md).\n",
    "POINTER_IN_REPO", "POINTER_IN_REPO", 0)
# Defect 3: CERN-OHL is free and reciprocal, never a refusal.
add("CERN-OHL-S (nimble shape)",
    "CERN Open Hardware Licence Version 2 - Strongly Reciprocal\n\nPreamble\n\nCERN has developed this licence to promote collaboration\n",
    "CERN-OHL-S", "STRONG_COPYLEFT", 1)
add("CERN-OHL-P is permissive",
    "CERN Open Hardware Licence Version 2 - Permissive\n\nPreamble\n",
    "CERN-OHL-P", "PERMISSIVE", 1)
# Defect 4: the bare Creative Commons title form.
add("bare 'Attribution-ShareAlike 4.0 International' (awesome-lti shape)",
    "Attribution-ShareAlike 4.0 International\n\n====\n\nCreative Commons Corporation is not a law firm\n",
    "CC-BY-SA", "CONTENT_NOT_SOFTWARE", 1)
add("bare 'Attribution-NonCommercial-ShareAlike 4.0' (SocraticNovel shape)",
    "Attribution-NonCommercial-ShareAlike 4.0 International\n\n====\n",
    "CC-BY-NC-SA", "UNSELLABLE", 1)
# Defect 5: ND is its own clause and bars adaptation.
add("CC BY-NC-ND stated in body, bilingually (visible-ai shape)",
    "\u300a\u770b\u5f97\u89c1\u7684 AI\u300b\nCopyright (c) 2026 All rights reserved by the author.\n\n"
    "Licensed under the Creative Commons\nAttribution-NonCommercial-NoDerivatives 4.0 International License\n(CC BY-NC-ND 4.0).\n",
    "CC-BY-NC", "UNSELLABLE", 0)
# Defect 6: a per-asset grant surface.
add("per-asset grant surface (learning-commons knowledge-graph shape)",
    "This page explains the licensing framework. For the license that applies to a specific "
    "dataset, check that dataset's page in the Dataset Catalog. For example, **Open + Gated** and "
    "**Gated** content are not covered by CC BY 4.0, CC0, or any other open license referenced here.\n\n"
    "## Code\n\nCode is licensed under [MIT](https://opensource.org/license/mit).\n\n"
    "## Data\n\nDatasets are **not all licensed the same way**. Each dataset is labeled with an access type.\n",
    "COMPOSITE_PER_ASSET", "COMPOSITE_PER_ASSET", 0)

add("MIT code + CC BY content + CC BY-NC-SA corpus in one payload (evaluators shape)",
    "The Evaluator code is licensed under [MIT](https://opensource.org/license/mit).\n\n"
    "Evaluators content (including the prompt and settings information) is provided by Learning "
    "Commons under the CC BY 4.0 International license.\n\n"
    "Annotated CLEAR Corpus is provided by Learning Commons under CC BY-NC-SA 4.0.\n",
    "COMPOSITE_PER_ASSET", "COMPOSITE_PER_ASSET", 0)

add("explicitly undecided reservation (pianojacq shape, GitLab)",
    "I haven't decided on whether to release this as open source or not so for now this software is\n"
    "(C) Jacques Mattheij, The Modular Company BV, All rights reserved.\n",
    "RESERVED_UNDECIDED", "RESERVED_UNDECIDED", 0)

def main():
    passed = failed = 0
    for label, payload, fam, cls, line1 in C:
        g = grade(payload)
        ok = g["family"].startswith(fam) and g["grant_class"] == cls
        if line1 is not None:
            ok = ok and g["line1"] == line1
        if ok:
            passed += 1
        else:
            failed += 1
            print(f"FAIL  {label}\n      got {g}\n      want family~{fam} class={cls} line1={line1}")
    # the one-bit contract
    assert sellable("PERMISSIVE") and sellable("PUBLIC_DOMAIN")
    for c in ("UNSELLABLE", "CONTENT_NOT_SOFTWARE", "NETWORK_COPYLEFT",
              "STRONG_COPYLEFT", "WEAK_COPYLEFT", "NO_GRANT", "UNSTATED",
              "POINTER_IN_REPO", "POINTER_CROSS_REPO", "COMPOSITE_PER_ASSET",
              "RESERVED_UNDECIDED"):
        assert not sellable(c), c
    print(f"\ncontrols: {passed}/{passed+failed} pass")
    # version axis, carried forward from p455
    v = grade("                    GNU GENERAL PUBLIC LICENSE\n   Version 2, June 1991\n"
              "\nsomething something either version 2 of the License, or (at your option) any later version")
    print(f"version axis: GPL-2.0 or-later -> {v['version']}")
    v3 = grade("                    GNU GENERAL PUBLIC LICENSE\n                       Version 3, 29 June 2007\n")
    print(f"version axis: GPL-3.0 only     -> {v3['version']}")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
