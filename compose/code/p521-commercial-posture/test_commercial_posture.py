"""Offline suite for commercial_posture. No network.

    python3 test_commercial_posture.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import commercial_posture as cp

CHECKS = []
def check(name, got, want):
    CHECKS.append((name, got == want, got, want))

MIT = ("MIT License\n\nCopyright (c) 2026 Someone\n\nPermission is hereby granted, free of "
       "charge, to any person obtaining a copy of this software and associated documentation "
       "files (the \"Software\"), to deal in the Software without restriction, including "
       "without limitation the rights to use, copy, modify, merge, publish, distribute, "
       "sublicense, and/or sell copies of the Software.")

# The shape pass 521 found at CaviraOSS/PageLM: MIT incipit, restrictions below.
CAMOUFLAGE = ("# Project Community License\n\nCopyright (c) 2026 Someone\n\nPermission is hereby "
              "granted, free of charge, to any person obtaining a copy of this software, to use, "
              "copy, modify, and run the Software for personal, educational, or non-commercial "
              "research purposes.\n\n## Conditions\n\nRedistribution of the Software, in whole or "
              "in part, is strictly prohibited without express written permission. If the "
              "Software is used for Commercial Use, a revenue-sharing agreement must be executed.")

# GPLv3 section 13 names the AGPL. A body-wide grep calls this AGPL; the title decides.
GPL3 = ("                    GNU GENERAL PUBLIC LICENSE\n                       Version 3, 29 June "
        "2007\n\n  Copyright (C) 2007 Free Software Foundation, Inc.\n\n" + ("x" * 900) +
        "\n  13. Use with the GNU Affero General Public License.\n\n  Notwithstanding any other "
        "provision of this License, you have permission to link or combine any covered work with "
        "a work licensed under version 3 of the GNU Affero General Public License.")

AGPL3 = ("                    GNU AFFERO GENERAL PUBLIC LICENSE\n                       Version 3, "
         "19 November 2007\n\n  Copyright (C) 2007 Free Software Foundation, Inc.")

APACHE = ("                                 Apache License\n                           Version "
          "2.0, January 2004\n\n   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION")

ECL = ("Educational Community License, Version 2.0\n\nLicensed under the Educational Community "
       "License, Version 2.0 (the \"License\"); you may not use this file except in compliance.")

CC_NC = ("Creative Commons Attribution-NonCommercial 4.0 International\n\nBy exercising the "
         "Licensed Rights, You accept these terms. NonCommercial means not primarily intended "
         "for commercial advantage.")

CC_BY = ("Creative Commons Attribution 4.0 International\n\nYou are free to share and adapt for "
         "any purpose, even commercially, under the following terms: Attribution.")

CC_SA = ("Creative Commons Attribution-ShareAlike 4.0 International\n\nIf you remix or build "
         "upon the material, you must distribute under the same licence. ShareAlike applies.")

BSD = ("BSD 3-Clause License\n\nRedistribution and use in source and binary forms, with or "
       "without modification, are permitted provided that the following conditions are met.")

LGPL = ("                   GNU LESSER GENERAL PUBLIC LICENSE\n                       Version 3, "
        "29 June 2007")

# --- defect class 1: MIT-incipit camouflage -------------------------------------------------
check("camouflage is not MIT",        cp.posture_of(CAMOUFLAGE)[0], "BESPOKE-restricted")
check("camouflage posture",           cp.posture_of(CAMOUFLAGE)[1], "BESPOKE-RESTRICTED")
check("camouflage not buildable",     cp.buildable_in_paid_engagement(CAMOUFLAGE)[0], False)
check("camouflage cites a clause",    "revenue-sharing requirement" in cp.posture_of(CAMOUFLAGE)[2], True)
check("camouflage cites redistrib",   "redistribution prohibited" in cp.posture_of(CAMOUFLAGE)[2], True)

# --- control: a real MIT must still pass ----------------------------------------------------
check("MIT family",                   cp.posture_of(MIT)[0], "MIT")
check("MIT posture",                  cp.posture_of(MIT)[1], "PERMISSIVE")
check("MIT buildable",                cp.buildable_in_paid_engagement(MIT)[0], True)
check("MIT has no restrictions",      cp.restrictions_in(MIT), [])

# --- defect class 2: CC variant must be resolved, never the bare family ---------------------
check("CC BY-NC variant",             cp.cc_variant(CC_NC), "CC-BY-NC")
check("CC BY-NC posture",             cp.posture_of(CC_NC)[1], "NON-COMMERCIAL")
check("CC BY-NC not buildable",       cp.buildable_in_paid_engagement(CC_NC)[0], False)
check("CC BY variant",                cp.cc_variant(CC_BY), "CC-BY")
check("CC BY posture",                cp.posture_of(CC_BY)[1], "PERMISSIVE")
check("CC BY buildable",              cp.buildable_in_paid_engagement(CC_BY)[0], True)
check("CC BY-SA variant",             cp.cc_variant(CC_SA), "CC-BY-SA")
check("CC BY-SA posture",             cp.posture_of(CC_SA)[1], "WEAK-COPYLEFT")
check("non-CC returns None",          cp.cc_variant(MIT), None)

# --- the GPLv3 section-13 trap --------------------------------------------------------------
check("GPLv3 is GPL not AGPL",        cp.posture_of(GPL3)[0], "GPL")
check("GPLv3 copyleft",               cp.posture_of(GPL3)[1], "COPYLEFT")
check("AGPLv3 is AGPL",               cp.posture_of(AGPL3)[0], "AGPL-3.0")
check("AGPLv3 copyleft",              cp.posture_of(AGPL3)[1], "COPYLEFT")
check("copyleft is buildable",        cp.buildable_in_paid_engagement(AGPL3)[0], True)

# --- remaining families ---------------------------------------------------------------------
check("Apache family",                cp.posture_of(APACHE)[0], "Apache-2.0")
check("Apache permissive",            cp.posture_of(APACHE)[1], "PERMISSIVE")
check("ECL family",                   cp.posture_of(ECL)[0], "ECL-2.0")
check("ECL permissive",               cp.posture_of(ECL)[1], "PERMISSIVE")
check("BSD family",                   cp.posture_of(BSD)[0], "BSD")
check("BSD permissive",               cp.posture_of(BSD)[1], "PERMISSIVE")
check("LGPL weak copyleft",           cp.posture_of(LGPL)[1], "WEAK-COPYLEFT")

# --- degenerate input -------------------------------------------------------------------------
check("empty is UNKNOWN",             cp.posture_of("")[1], "UNKNOWN")
check("whitespace is UNKNOWN",        cp.posture_of("   \n ")[1], "UNKNOWN")
check("unknown text is UNKNOWN",      cp.posture_of("All rights reserved.")[1], "UNKNOWN")
check("UNKNOWN not buildable",        cp.buildable_in_paid_engagement("")[0], False)

# --- live payload fixtures (bytes read 2026-10-29, stored so the suite stays offline) --------
HERE = os.path.dirname(os.path.abspath(__file__))
for fixture, want_family, want_posture, want_buildable in [
    ("pagelm.LICENSE.md.txt",   "BESPOKE-restricted", "BESPOKE-RESTRICTED", False),
    ("cn-math-taxonomy.LICENSE.txt", "CC-BY-NC",      "NON-COMMERCIAL",     False),
]:
    path = os.path.join(HERE, "fixtures", fixture)
    if os.path.exists(path):
        payload = open(path, encoding="utf-8").read()
        f, p, _ = cp.posture_of(payload)
        check("fixture %s family" % fixture, f, want_family)
        check("fixture %s posture" % fixture, p, want_posture)
        check("fixture %s buildable" % fixture,
              cp.buildable_in_paid_engagement(payload)[0], want_buildable)

failed = [c for c in CHECKS if not c[1]]
for name, ok, got, want in CHECKS:
    if not ok:
        print("FAIL %-34s got=%r want=%r" % (name, got, want))
print("%d/%d checks green" % (len(CHECKS) - len(failed), len(CHECKS)))
sys.exit(1 if failed else 0)
