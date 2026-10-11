#!/usr/bin/env python3
"""ACTION AI — the permissiveness tiers, and a token reader that uses them.

A "more permissive" answer is not a nicer answer: it is a LOWER DUTY. The
tiers below are ordered by what a studio must give up to ship a closed or
hosted product on the code, which is the only ordering that makes
"false-permissive" an error with a cost attached:

  0  public domain      CC0-1.0, Unlicense              -- no duty
  1  permissive         MIT, BSD, ISC, Apache-2.0, CC-BY -- attribution
  2  weak copyleft      MPL-2.0, EPL-2.0, LGPL, EUPL     -- publish changed files
  3  strong copyleft    GPL-2.0, GPL-3.0                 -- publish the product
  4  network copyleft   AGPL-3.0                         -- publish it when HOSTED
  5  not open source    Elastic-2.0, BUSL, CC-BY-NC, EULA -- cannot ship at all

A guess is FALSE-PERMISSIVE when it returns a STRICTLY LOWER tier than the
real default branch does, and that is the one direction of error that costs
money rather than opportunity. The reverse (false-restrictive) costs a
shortlist, which p125's own `intel/trends.md` trend 1 already names.

Offline. No network, no clock.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scope_gate                                        # noqa: E402

TIER = {
    "CC0-1.0": 0, "Unlicense": 0,
    "MIT": 1, "BSD-3-Clause": 1, "BSD-2-Clause": 1, "BSD": 1, "ISC": 1,
    "Apache-2.0": 1, "ECL-2.0": 1, "CC-BY-4.0": 1, "CC-BY-3.0": 1,
    "MPL-2.0": 2, "EPL-2.0": 2, "LGPL": 2, "LGPL-2.1": 2, "LGPL-3.0": 2,
    "EUPL-1.1": 2, "EUPL-1.2": 2, "CC-BY-SA-4.0": 2, "CC-BY-SA-3.0": 2,
    "GPL": 3, "GPL-2.0": 3, "GPL-3.0": 3,
    "AGPL-3.0": 4, "AGPL": 4,
    "Elastic-2.0": 5, "BUSL-1.1": 5, "MulanPSL-2.0": 2,
    "CC-BY-NC-4.0": 5, "CC-BY-NC-SA-4.0": 5, "CC-BY-NC-ND-4.0": 5,
    "PROPRIETARY": 5,
}
NAME = {0: "public-domain", 1: "permissive", 2: "weak-copyleft",
        3: "strong-copyleft", 4: "network-copyleft", 5: "not-open-source"}

# Title-line reading, because p124's ACTION AD established that the title is
# the only channel a document's own boilerplate cannot poison.
TITLES = (
    (re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I), "AGPL-3.0"),
    (re.compile(r"GNU LESSER GENERAL PUBLIC LICENSE", re.I), "LGPL-3.0"),
    (re.compile(r"GNU GENERAL PUBLIC LICENSE.{0,40}Version 3", re.I | re.S),
     "GPL-3.0"),
    (re.compile(r"GNU GENERAL PUBLIC LICENSE.{0,40}Version 2", re.I | re.S),
     "GPL-2.0"),
    (re.compile(r"Apache License.{0,40}Version 2", re.I | re.S), "Apache-2.0"),
    (re.compile(r"Mozilla Public License Version 2", re.I), "MPL-2.0"),
    (re.compile(r"Eclipse Public License.{0,20}v?\s*2", re.I | re.S),
     "EPL-2.0"),
    (re.compile(r"European Union Public Licence.{0,20}1\.2", re.I | re.S),
     "EUPL-1.2"),
    (re.compile(r"European Union Public Licence", re.I), "EUPL-1.1"),
    (re.compile(r"Attribution[- ]NonCommercial[- ]ShareAlike 4\.0", re.I),
     "CC-BY-NC-SA-4.0"),
    (re.compile(r"Attribution[- ]NonCommercial[- ]NoDerivatives 4\.0", re.I),
     "CC-BY-NC-ND-4.0"),
    (re.compile(r"Attribution[- ]NonCommercial 4\.0", re.I), "CC-BY-NC-4.0"),
    (re.compile(r"Attribution[- ]ShareAlike 4\.0", re.I), "CC-BY-SA-4.0"),
    (re.compile(r"Attribution 4\.0 International", re.I), "CC-BY-4.0"),
    (re.compile(r"CC0 1\.0 Universal", re.I), "CC0-1.0"),
    (re.compile(r"Elastic License 2\.0", re.I), "Elastic-2.0"),
    (re.compile(r"Business Source License", re.I), "BUSL-1.1"),
    (re.compile(r"BSD 3[- ]Clause", re.I), "BSD-3-Clause"),
    (re.compile(r"BSD 2[- ]Clause", re.I), "BSD-2-Clause"),
    (re.compile(r"\bMIT License\b", re.I), "MIT"),
    (re.compile(r"\bISC License\b", re.I), "ISC"),
    (re.compile(r"Mulan Permissive Software License", re.I),
     "MulanPSL-2.0"),
    (re.compile(r"Educational Community License", re.I), "ECL-2.0"),
    (re.compile(r"This is free and unencumbered software", re.I),
     "Unlicense"),
)
# Body phrases that identify a grant whose title line is absent or generic.
BODY = (
    (re.compile(r"Permission is hereby granted, free of charge", re.I), "MIT"),
    (re.compile(r"Redistribution and use in source and binary forms.{0,600}"
                r"name of the copyright holder", re.I | re.S),
     "BSD-3-Clause"),
    (re.compile(r"Redistribution and use in source and binary forms", re.I),
     "BSD-2-Clause"),
    (re.compile(r"Licensed under the Apache License, Version 2\.0", re.I),
     "Apache-2.0"),
    (re.compile(r"affero", re.I), "AGPL-3.0"),
)


def classify(text):
    """-> an SPDX-ish token, or NO-TOKEN. Title first, then body."""
    if text[:1] == "﻿":
        text = text[1:]
    head = "\n".join(text.splitlines()[:12])
    for pat, tok in TITLES:
        if pat.search(head):
            return tok
    for pat, tok in TITLES:
        if pat.search(text[:4000]):
            return tok
    for pat, tok in BODY:
        if pat.search(text):
            return tok
    # Last resort: the gate's own grant set, if it is unambiguous.
    g = {t for t, _ in scope_gate.grants(text)}
    if len(g) == 1:
        return next(iter(g))
    return "NO-TOKEN"


def tier(tok):
    return TIER.get(tok)


def compare(real_tok, guess_tok):
    """What a branch-guessing probe does to a studio, in one word.

    NO-GRANT on the real default and a grant from a guess is the severe case
    and is reported separately, because the error is not "wrong tier" -- it is
    a licence asserted where the repository grants none.
    """
    if guess_tok in (None, "NO-FILE"):
        return "GUESS-MISSES-GRANT" if real_tok not in (
            None, "NO-FILE") else "BOTH-ABSENT"
    if real_tok in (None, "NO-FILE"):
        return "GUESS-INVENTS-GRANT"
    if real_tok == guess_tok:
        return "AGREE"
    rt, gt = tier(real_tok), tier(guess_tok)
    if rt is None or gt is None:
        return "UNRANKED"
    if gt < rt:
        return "FALSE-PERMISSIVE"
    if gt > rt:
        return "FALSE-RESTRICTIVE"
    return "SAME-TIER"
