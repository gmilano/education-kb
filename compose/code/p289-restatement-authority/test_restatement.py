"""Controls for `ACTION p289` — RESTATEMENT vs AUTHORITATIVE BODY.

The real fixtures are quoted VERBATIM from payloads fetched on 2026-10-18 from
`raw.githubusercontent.com/oaknational/oak-curriculum-ontology/main/...`, with their
byte counts and sha256 prefixes recorded in
`evidence/curriculum-licence-restatement.2026-10-18-p289.tsv`.
A fixture paraphrased is a fixture that stops reproducing.

`p283`'s ratchet rejects a single-axis instrument, so the generality arm (controls 20-23)
exercises the SAME classifier on a Creative Commons restatement with no OGL vocabulary in
it at all, and the failure-capability arm (controls 30-35) mutates each real fixture and
asserts the verdict MOVES.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from restatement import (
    attribution_verdict,
    body_vs_summary_attribution,
    claims_to_be_full_text,
    classify_payload,
    named_external_authority,
    posture,
    required_attributions,
    self_contained_family,
    self_description_verdict,
)

FAIL = []


def check(name, got, want):
    if got != want:
        FAIL.append(f"{name}: got {got!r}, want {want!r}")


# ================================================================ the real fixtures
# 1. DATA-LICENSE.md -- 2 408 B, sha256(12) c117e319f357.  Oak's RESTATEMENT of OGL v3.0.
#    L19 prescribes the OGL statement; L54, in the summary block, asks for a bare credit.
DATA_LICENCE = """## Open Government Licence v3.0

You are encouraged to use and re-use the information in this publication freely. This work is made available under the Open Government Licence v3.0.

To view this licence, visit <https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/>

### Using this information

Under the Open Government Licence, you are free to:

* copy, publish, distribute and transmit the information
* adapt the information
* exploit the information commercially and non-commercially, for example, by combining it with other information, or by including it in your own product or application

You must, where you do any of the above:

* acknowledge the source of the information by including the following attribution statement:

  > Contains public sector information licensed under the Open Government Licence v3.0.

### Exemptions

This licence does not cover the use of:

* personal data in the information
* the Oak National Academy logo, any other logo, or the Royal Arms
* third party rights Oak National Academy is not authorised to license

### No warranty

The information is licensed 'as is' and Oak National Academy excludes all representations, warranties, obligations and liabilities in relation to the information to the maximum extent permitted by law.

### Governing law

This licence is governed by the laws of England and Wales.

---

**What you can do:**
* Use for any purpose (commercial or non-commercial)
* Copy, modify, and redistribute
* Must provide attribution: "Oak National Academy"
"""

check("data/family", self_contained_family(DATA_LICENCE), None)
check(
    "data/authority",
    named_external_authority(DATA_LICENCE),
    ("open government licence", "nationalarchives.gov.uk"),
)
check("data/classify", classify_payload(DATA_LICENCE), "RESTATEMENT")
check(
    "data/attribution-forms",
    required_attributions(DATA_LICENCE),
    frozenset({"PRESCRIBED-STATEMENT", "BARE-CREDIT"}),
)
check("data/attribution-verdict", attribution_verdict(DATA_LICENCE), "DISAGREEMENT")
check(
    "data/body-vs-summary",
    body_vs_summary_attribution(DATA_LICENCE),
    "SUMMARY-REPLACES-PRESCRIBED",
)
# The authority is MEASURED unreachable from this environment (11/11 POLICY-REFUSED).
check(
    "data/posture",
    posture(classify_payload(DATA_LICENCE), False).split(" ")[0],
    "USE-WITH-RECORDED-BOUND",
)
# ...and the posture MUST differ when the authority can be reached.  Same payload.
check(
    "data/posture-if-reachable",
    posture(classify_payload(DATA_LICENCE), True).split(" ")[0],
    "VERIFY",
)
check(
    "data/posture-if-unprobed",
    posture(classify_payload(DATA_LICENCE), None).split(" ")[0],
    "UNPROBED",
)

# 2. LICENSE.md -- 1 867 B, sha256(12) 98ac0c16f708.  The dual-licence splitter.
#    It calls DATA-LICENSE.md the "Full OGL 3.0 License", and DATA-LICENSE.md is a
#    RESTATEMENT -- the authoritative text is at the National Archives.
SPLITTER = """# License

This repository uses **dual licensing** to appropriately cover different types of content.

## Part 1: Data and Ontology - Open Government Licence v3.0

You are free to:

- Copy, publish, distribute and transmit the information
- Adapt the information
- Exploit the information commercially and non-commercially

**You must:**

- Acknowledge the source with the attribution: "Contains public sector information licensed under the Open Government Licence v3.0."

### Full OGL 3.0 License

For complete Open Government Licence v3.0 terms including exemptions, warranties, and governing law, see **[DATA-LICENSE](DATA-LICENSE.md)**.

**Official license:** <https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/>

## Attribution

When using this work, please credit **"Oak National Academy"**.
"""

check("splitter/classify", classify_payload(SPLITTER), "RESTATEMENT")
check("splitter/attribution-verdict", attribution_verdict(SPLITTER), "DISAGREEMENT")
check(
    "splitter/body-vs-summary",
    body_vs_summary_attribution(SPLITTER),
    "SUMMARY-REPLACES-PRESCRIBED",
)
check("splitter/claims-full", claims_to_be_full_text(SPLITTER), True)
check(
    "splitter/self-description",
    self_description_verdict(SPLITTER, classify_payload(DATA_LICENCE)),
    "OVERSTATED",
)
# The same claim over a payload that really IS the body is ACCURATE, not a defect.
check(
    "splitter/self-description-accurate",
    self_description_verdict(SPLITTER, "AUTHORITATIVE-BODY"),
    "ACCURATE",
)

# 3. CODE-LICENSE.md -- 1 491 B, sha256(12) 427f1d8b0cc1.  A VERBATIM MIT body whose
#    trailing summary asks for a credit string MIT itself does not require.  This is the
#    COLLISION ARM: the repo names OGL elsewhere and this file must still grade MIT.
CODE_LICENCE = """## **MIT License**

Copyright (c) 2026 Oak National Academy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

---

All Python scripts, GitHub Actions workflows, and software tools are licensed under this MIT License.

**Applies to:**

- `scripts/` - Python utilities

**What you can do:**

- Use, modify, and redistribute freely
- Use in commercial projects

**Attribution:** When using this work, please credit **"Oak National Academy"**
"""

check("code/family", self_contained_family(CODE_LICENCE), "MIT")
check("code/classify", classify_payload(CODE_LICENCE), "AUTHORITATIVE-BODY")
check("code/posture", posture(classify_payload(CODE_LICENCE), False).split(" ")[0], "VERIFIED")
check(
    "code/body-vs-summary",
    body_vs_summary_attribution(CODE_LICENCE),
    "SUMMARY-ADDS-OBLIGATION",
)

# 4. oak-open-curriculum-ecosystem/LICENCE -- 1 086 B, sha256(12) 02c5a8e84229.
#    A plain MIT body, no summary block at all: the clean case must stay clean.
PLAIN_MIT = """MIT License

Copyright (c) 2024-present Oak National Academy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

check("plain-mit/classify", classify_payload(PLAIN_MIT), "AUTHORITATIVE-BODY")
check("plain-mit/attribution", attribution_verdict(PLAIN_MIT), "NONE")
check("plain-mit/body-vs-summary", body_vs_summary_attribution(PLAIN_MIT), "NO-SUMMARY")

# ================================================================ negative controls
# 10. A BARE reference names the licence and links it and states NO terms.  It must not
#     be promoted to RESTATEMENT -- that is the whole distinction.
BARE = """# Licence

This dataset is licensed under the Open Government Licence v3.0.
See <https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/>
"""
check("bare/classify", classify_payload(BARE), "BARE-REFERENCE")
check("bare/posture", posture(classify_payload(BARE), False).split(" ")[0], "STOP")

# 11. No grant at all.
check("empty/classify", classify_payload(""), "NO-GRANT")
check("none/classify", classify_payload("# Readme\n\nA curriculum tool.\n"), "NO-GRANT")
check("none/posture", posture(classify_payload(""), None).split(" ")[0], "STOP")

# 12. An AGPL body is self-contained even though it is long and copyleft.
AGPL = """GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007

Copyright (C) 2007 Free Software Foundation, Inc.
Everyone is permitted to copy and distribute verbatim copies of this license
document, but changing it is not allowed.
"""
check("agpl/family", self_contained_family(AGPL), "GPL-family")
check("agpl/classify", classify_payload(AGPL), "AUTHORITATIVE-BODY")

# ================================================================ generality arm
# 20-23. `p283`'s ratchet rejects an instrument that only works on the axis it was built
#        for.  Same classifier, a Creative Commons restatement, zero OGL vocabulary.
CC_RESTATEMENT = """# Copyright and terms of use

This material is licensed under a Creative Commons Attribution 4.0 International licence.

You are free to:

* copy, share and adapt the material
* use it commercially and non-commercially

You must:

* acknowledge the source of the information

For the full licence terms see <https://creativecommons.org/licenses/by/4.0/>

**What you can do:**

* Must provide attribution: "the Authority"
"""
check(
    "cc/authority",
    named_external_authority(CC_RESTATEMENT),
    ("creative commons", "creativecommons.org"),
)
check("cc/classify", classify_payload(CC_RESTATEMENT), "RESTATEMENT")
check(
    "cc/posture",
    posture(classify_payload(CC_RESTATEMENT), False).split(" ")[0],
    "USE-WITH-RECORDED-BOUND",
)
# A CC restatement with no prescribed statement in the body: the summary ADDS, it does
# not REPLACE.  The two defect shapes must stay distinguishable outside the OGL axis.
check(
    "cc/body-vs-summary",
    body_vs_summary_attribution(CC_RESTATEMENT),
    "SUMMARY-ADDS-OBLIGATION",
)

# ================================================================ failure capability
# 30-35. Every real fixture, mutated.  If the verdict does not move, the control above it
#        was not measuring anything.
_m1 = DATA_LICENCE.replace(
    "> Contains public sector information licensed under the Open Government Licence v3.0.",
    "> (see the licence)",
)
check("mut/data-no-prescribed", attribution_verdict(_m1), "SINGLE")
check("mut/data-no-prescribed-summary", body_vs_summary_attribution(_m1), "SUMMARY-ADDS-OBLIGATION")

_m2 = DATA_LICENCE
for _term in (
    "You are encouraged to use and re-use the information in this publication freely. ",
    "copy, publish, distribute and transmit the information",
    "adapt the information",
    "exploit the information commercially and non-commercially, for example, by combining it with other information, or by including it in your own product or application",
    "You must, where you do any of the above:",
    "acknowledge the source of the information by including the following attribution statement:",
    "This licence does not cover the use of:",
    "Exemptions",
    "Must provide attribution: \"Oak National Academy\"",
    "you are free to",
):
    _m2 = _m2.replace(_term, "")
check("mut/data-stripped-of-terms", classify_payload(_m2), "BARE-REFERENCE")

_m3 = CODE_LICENCE.replace("Permission is hereby granted, free of charge", "Permission is withheld")
check("mut/code-no-mit-anchor", self_contained_family(_m3), None)
check("mut/code-no-mit-anchor-classify", classify_payload(_m3), "NO-GRANT")

_m4 = SPLITTER.replace("### Full OGL 3.0 License", "### Where to read the licence").replace(
    "For complete Open Government Licence v3.0 terms including exemptions, warranties, and governing law, see",
    "The licence is published at",
)
check("mut/splitter-no-full-claim", claims_to_be_full_text(_m4), False)
check(
    "mut/splitter-no-full-claim-verdict",
    self_description_verdict(_m4, "RESTATEMENT"),
    "NO-CLAIM",
)

# ================================================================
if FAIL:
    print(f"FAIL ({len(FAIL)}):")
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("p289-restatement-authority: all controls PASS")
