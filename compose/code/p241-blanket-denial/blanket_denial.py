#!/usr/bin/env python3
"""`p241-blanket-denial` — the axis `p240` diagnosed one language short.

`p240` found `commercial_use_ok` returning ALLOWED on a Chinese payload whose first
operative clause is 禁止商业使用.  It read the defect as LANGUAGE and fixed it with 35
restriction phrases across 9 languages, then built `p240-grant-language` to refuse to
clear a payload written in a script the token match cannot read.

🔴 `p241` found the same function returning ALLOWED on two payloads written in ENGLISH:

  Samielakkad/AI-EdTech-Sovereign-School-OS   688 B
      "NO PERMISSION is granted to use, copy, modify, merge, publish, distribute,
       sublicense, sell, train machine-learning models on, or create derivative works
       from any part of this repository -- for personal, academic, or commercial
       purposes -- WITHOUT the author's explicit prior WRITTEN permission."

  snflwr-ai/snflwr.ai                        2 833 B
      "snflwr.ai — Proprietary Software License / All rights reserved."

Neither contains `non-commercial`, `noncommercial`, `not-for-profit` or `obtain a
commercial license`.  The first uses the word *commercial* inside a DENIAL; the token
list only knows it inside the compound.  `p240-grant-language` returns `LATIN-SCRIPT`
on both — 🔴 it affirmatively certifies that the English token match APPLIES, on the
two payloads that defeat it.

So the defect class is not the language of the restriction.  It is that **every one of
these matchers enumerates ways of saying "restricted" and treats the absence of its own
vocabulary as permission.**  A denial it has not seen before reads as a grant.

The predicate here does not enumerate restrictions.  It asks the question a grant
exists to answer:

    DOES THIS PAYLOAD GRANT ANYTHING AT ALL?

A licence's whole function is to grant.  `MIT` says *permission is hereby granted*;
`BSD` says *redistribution and use ... are permitted*; `Apache-2.0` says *hereby grants*;
`GPL` says *this program is free software*.  A payload that reserves rights and grants
none is not an unrecognised licence — it is a refusal, and it is detectable WITHOUT
knowing how its author chose to phrase the refusal.

🟡 THE ONE FALSE-POSITIVE MODE, AND THE DISCRIMINATOR.  `All rights reserved.` is a line
in `BSD-2-Clause`, `BSD-3-Clause` and many `MIT` headers — followed by a grant.  So
`all rights reserved` ALONE NEVER CONVICTS.  It convicts only in the ABSENCE of any
grant phrase, which is exactly the `p238` self-host-exemption shape: the cheap signal is
kept, and a second predicate stops it firing on the honest case.

usage:  blanket_denial.py <payload-path> | --reach | --selftest
"""
import sys

# A grant verb.  These are the phrases by which the permissive and copyleft families
# actually convey permission; the list is PRINTABLE (`--reach`) per T272 so the next pass
# extends it instead of copying it.
GRANT = (
    "permission is hereby granted",
    "permission to use, copy, modify",
    "redistribution and use",
    "redistribution, with or without modification",
    "hereby grants",
    "grants you a",
    "grants to you",
    "is hereby granted",
    "licensed under the apache license",
    "you may obtain a copy of the license",
    "you may not use this file except in compliance",
    "this program is free software",
    "this library is free software",
    "free software: you can redistribute",
    "permitted provided that",
    "subject to the terms and conditions of this license",
    "you are free to",
    "we hereby grant",
    "granted a perpetual",
    "do what the fuck you want",
)

# An EXPLICIT denial of permission.  These convict on their own.
DENIAL = (
    "no permission is granted",
    "no permission whatsoever",
    "no permission has been granted",
    "permission is not granted",
    "no license is granted",
    "no licence is granted",
    "no rights are granted",
    "no rights whatsoever are granted",
    "not granted any rights",
    "proprietary software license",
    "proprietary software licence",
    "proprietary license",
    "proprietary licence",
    "all rights are reserved",
    "is not open source",
    "is not an open-source",
    "unauthorized copying",
    "unauthorised copying",
    "strictly prohibited",
)

# Convicts only when NO grant phrase is present.  `BSD` carries this line and grants.
RESERVED_WEAK = (
    "all rights reserved",
)


def _norm(text):
    return " ".join(text.lower().split())


def grants_found(text):
    d = _norm(text)
    return [g for g in GRANT if g in d]


def denials_found(text):
    d = _norm(text)
    return [x for x in DENIAL if x in d]


def reserved_found(text):
    d = _norm(text)
    return [x for x in RESERVED_WEAK if x in d]


def verdict(text):
    """GRANT-PRESENT | BLANKET-DENIAL | NO-GRANT-LANGUAGE

    BLANKET-DENIAL  an explicit denial fired, or rights are reserved with no grant
    GRANT-PRESENT   a grant verb is present -- the token matchers may be trusted
    NO-GRANT-LANGUAGE  neither.  A REFUSAL TO CLEAR, never a permission
    """
    g = grants_found(text)
    d = denials_found(text)
    r = reserved_found(text)
    if d:
        return "BLANKET-DENIAL"
    if r and not g:
        return "BLANKET-DENIAL"
    if g:
        return "GRANT-PRESENT"
    return "NO-GRANT-LANGUAGE"


def may_publish(text):
    """A row may be published as permissive ONLY on GRANT-PRESENT.

    Both other states are refusals.  `NO-GRANT-LANGUAGE` is not a soft pass: it is
    `p240`'s `UNREAD` in the other axis -- no vocabulary this KB owns has found a grant
    in this payload, which is not the same as the payload granting something.
    """
    return verdict(text) == "GRANT-PRESENT"


def main(argv):
    if len(argv) >= 2 and argv[1] == "--reach":
        print("grant=%d denial=%d reserved-weak=%d  states=3"
              % (len(GRANT), len(DENIAL), len(RESERVED_WEAK)))
        print("--- GRANT (a licence's own verb)")
        for g in GRANT:
            print(g)
        print("--- DENIAL (convicts alone)")
        for d in DENIAL:
            print(d)
        print("--- RESERVED-WEAK (convicts only with NO grant phrase)")
        for r in RESERVED_WEAK:
            print(r)
        return 0
    if len(argv) >= 2 and argv[1] == "--selftest":
        import test_blanket_denial  # noqa: F401
        return 0
    if len(argv) < 2:
        sys.stderr.write("usage: blanket_denial.py <payload-path> | --reach | --selftest\n")
        return 2
    with open(argv[1], "rb") as fh:
        text = fh.read().decode("utf-8", "replace")
    v = verdict(text)
    print("%s\t%s\tgrants=%d denials=%d reserved=%d"
          % (v, argv[1], len(grants_found(text)), len(denials_found(text)),
             len(reserved_found(text))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
