#!/usr/bin/env python3
"""Controls for `p247-keyed-grant`.

Runs from ANY directory under `python3 -I` -- `ACTION VW`'s rule, which this base paid 53
passes to learn (`p1054` classified correctly since p188 and `make hooks` never ran it
because its suite died under the exact invocation its own docstring prescribed).

The adversarial half is the point.  `GPL-3.0` and `AGPL-3.0` are read FIRST-HAND from this
repo's own fixtures, not paraphrased: GPL-3.0's text contains "authorization key" once,
"Installation Information" four times and "technological measures" twice, so an instrument
with this artefact vocabulary and no shield WOULD call the GNU GPL a keyed grant.  Those two
payloads are the controls that forbid it.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)  # `-I` strips the script's own directory -- P355 / ACTION VW

from keyed_grant import (  # noqa: E402
    SHARED_CLASSIFIER_WINDOW,
    keyed_grant,
    name_anywhere,
    parameter_file,
    sentences,
    verdict,
)

FIX = os.path.join(HERE, "fixtures")
OK = 0
BAD = []


def check(label, got, want):
    global OK
    if got == want:
        OK += 1
        print("ok   %-62s ok" % label[:62])
    else:
        BAD.append((label, got, want))
        print("FAIL %-62s got=%r want=%r" % (label[:62], got, want))


def fx(name):
    with open(os.path.join(FIX, name), encoding="utf-8", errors="replace") as fh:
        return fh.read()


# =======================================================================================
# 1. The three real source-available payloads, and the three DIFFERENT causes
# =======================================================================================
csl = fx("cockroachdb.csl-2024.txt")
check("CSL: verdict is KEYED-GRANT", verdict(csl)[0], "KEYED-GRANT")
check("CSL: all three artefact kinds fire", verdict(csl)[1],
      "COUNTERMEASURE,LICENCE-KEY,TELEMETRY")
check("CSL: its own name is at offset 0 (VOCABULARY gap, not window)",
      name_anywhere(csl)[0], ("CockroachDB-CSL", 0))
check("CSL: nothing beyond the window", verdict(csl)[3], "-")
check("CSL: the word 'commercial' appears ZERO times", csl.lower().count("commercial"), 0)
check("CSL: 'License Key' is the keyed artefact", "LICENCE-KEY" in keyed_grant(csl)[1], True)
check("CSL: telemetry is a condition of OPERATING", "TELEMETRY" in keyed_grant(csl)[1], True)

iaga = fx("iaga-sentinel.busl-1.1.txt")
check("BSL(IAGA): named, not keyed", verdict(iaga)[0], "NAMED-SOURCE-AVAILABLE")
check("BSL(IAGA): BUSL at offset 0 -> the ORDER case", name_anywhere(iaga)[0], ("BUSL", 0))
check("BSL(IAGA): reach is in-window", verdict(iaga)[4], "in-window")

red = fx("redpanda.community-license.txt")
check("Redpanda: named", verdict(red)[0], "NAMED-SOURCE-AVAILABLE")
check("Redpanda: own name at 2, BSL reference at 4969",
      name_anywhere(red), [("RedpandaCommunity", 2), ("BUSL", 4969)])
check("Redpanda: the BSL reference is BEYOND the shared window", verdict(red)[3], "BUSL")
check("Redpanda: reach says partly-beyond-window", verdict(red)[4], "partly-beyond-window")
check("Redpanda: 4969 >= the window the classifier truncates at",
      name_anywhere(red)[1][1] >= SHARED_CLASSIFIER_WINDOW, True)

poly = fx("polyform-noncommercial.txt")
check("PolyForm: named", verdict(poly)[0], "NAMED-SOURCE-AVAILABLE")
check("PolyForm: name found", [n for n, _ in name_anywhere(poly)], ["PolyForm"])

# =======================================================================================
# 2. THE ADVERSARIAL CONTROLS — the GNU family must NOT read as keyed
# =======================================================================================
gpl = fx("gpl-3.0.txt")
agpl = fx("agpl-3.0.txt")
check("GPL-3.0 really does contain 'authorization key'",
      "authorization key" in gpl.lower(), True)
check("GPL-3.0 really does contain 'Installation Information'",
      gpl.lower().count("installation information") >= 4, True)
check("GPL-3.0 really does contain 'technological measures'",
      "technological measures" in gpl.lower(), True)
check("GPL-3.0: NOT a keyed grant (the shield holds)", verdict(gpl)[0], "NO-KEYED-CONDITION")
check("GPL-3.0: no artefact kind survives", keyed_grant(gpl)[1], [])
check("AGPL-3.0: NOT a keyed grant", verdict(agpl)[0], "NO-KEYED-CONDITION")
check("AGPL-3.0: no artefact kind survives", keyed_grant(agpl)[1], [])

apache = fx("apache-2.0.canonical.txt")
mit = fx("mit-canonical.txt")
check("Apache-2.0 canonical: NO-KEYED-CONDITION", verdict(apache)[0], "NO-KEYED-CONDITION")
check("Apache-2.0 canonical: no name", verdict(apache)[2], "-")
check("MIT canonical: NO-KEYED-CONDITION", verdict(mit)[0], "NO-KEYED-CONDITION")
check("MIT canonical: no name", verdict(mit)[2], "-")

# =======================================================================================
# 3. The shield discards the HIT, not the payload
# =======================================================================================
both = (
    "The Corresponding Source includes the Installation Information, which means any "
    "methods, procedures and authorization keys required to install and execute modified "
    "versions. You will not operate the Software without a License Key provisioned by "
    "Licensor."
)
check("shield is per-sentence: a keyed sentence beside a GNU sentence still fires",
      verdict(both)[0], "KEYED-GRANT")
check("shield is per-sentence: only the keyed kind is reported",
      keyed_grant(both)[1], ["LICENCE-KEY"])

gnu_only = (
    "Installation Information includes any methods, procedures, authorization keys or other "
    "information required to install and execute modified versions of a covered work."
)
check("a GNU installation-information sentence alone does not fire",
      verdict(gnu_only)[0], "NO-KEYED-CONDITION")
waiver = (
    "You waive any legal power to forbid circumvention of technological measures to the "
    "extent such circumvention is effected by exercising rights under this License."
)
check("the GPL anti-circumvention WAIVER does not fire", verdict(waiver)[0],
      "NO-KEYED-CONDITION")

# =======================================================================================
# 4. The NOTICE shield — an artefact word inside a copyright line
# =======================================================================================
holder = (
    "MIT License Copyright (c) 2026 Keystone Telemetry Ltd, all rights reserved in the name "
    "only. Permission is hereby granted, free of charge, to any person obtaining a copy of "
    "this software to deal in the Software without restriction."
)
check("a holder named '... Telemetry Ltd' is not a keyed grant",
      verdict(holder)[0], "NO-KEYED-CONDITION")
notice_and_condition = (
    "Copyright (c) 2026 Acme Inc. You may not operate the Software without a valid license "
    "key issued to You by Acme."
)
check("a sentence that both notices AND conditions still fires",
      verdict(notice_and_condition)[0], "KEYED-GRANT")

# =======================================================================================
# 5. The CONDITIONING requirement — a bare mention is not a condition
# =======================================================================================
check("a definitions-only mention with no conditioning cue does not fire",
      verdict("Appendix A. Glossary. Telemetry. Protective Measures. License Key.")[0],
      "NO-KEYED-CONDITION")
check("'requires a valid license key' fires",
      verdict("Use of the Software requires a valid license key.")[0], "KEYED-GRANT")
check("'subject to an active subscription' fires ENTITLEMENT",
      keyed_grant("Your rights are subject to a subscription that must be active.")[1],
      ["ENTITLEMENT"])
check("'must not disable the telemetry' fires TELEMETRY",
      keyed_grant("You must not disable the telemetry built into the Software.")[1],
      ["TELEMETRY"])
check("'designed to enforce the terms' fires COUNTERMEASURE",
      keyed_grant("You will not alter elements designed to enforce the terms hereof.")[1],
      ["COUNTERMEASURE"])
check("'seats licensed' fires ENTITLEMENT",
      keyed_grant("Use may not exceed the number of seats licensed to You.")[1],
      ["ENTITLEMENT"])
check("'activation code' is an artefact spelling",
      keyed_grant("The Software will not run without an activation code.")[1],
      ["LICENCE-KEY"])
check("'product key' is an artefact spelling",
      keyed_grant("A product key is required for production use.")[1], ["LICENCE-KEY"])
check("'phones home' is a telemetry spelling",
      keyed_grant("The Software phones home and You may not block it.")[1], ["TELEMETRY"])

# =======================================================================================
# 6. The NAME channel — full names only, never a bare acronym (the P312 criterion)
# =======================================================================================
check("bare 'BSL' is NOT a name match", name_anywhere("Licensed under the BSL."), [])
check("bare 'SSPL' is NOT a name match", name_anywhere("See SSPL for details."), [])
check("'Business Source License' IS a name match",
      [n for n, _ in name_anywhere("This is the Business Source License 1.1")], ["BUSL"])
check("'Server Side Public License' IS a name match",
      [n for n, _ in name_anywhere("Server Side Public License, version 1")], ["SSPL"])
check("'Elastic License 2.0' IS a name match",
      [n for n, _ in name_anywhere("Elastic License 2.0 (ELv2)")], ["Elastic"])
check("'Commons Clause' IS a name match",
      [n for n, _ in name_anywhere('The Software is subject to the "Commons Clause".')],
      ["CommonsClause"])
check("'Functional Source License' IS a name match",
      [n for n, _ in name_anywhere("Functional Source License, Version 1.1")], ["FSL"])
check("'Cryptographic Autonomy License' IS a name match",
      [n for n, _ in name_anywhere("Cryptographic Autonomy License v1.0")], ["CAL"])
check("'Sustainable Use License' IS a name match",
      [n for n, _ in name_anywhere("n8n Sustainable Use License")], ["SUL"])
check("'fair-code' IS a name match",
      [n for n, _ in name_anywhere("This project is fair-code distributed")], ["FAIRCODE"])
check("'PolyForm' needs its variant word",
      name_anywhere("A polyform is a plane figure built of congruent cells."), [])
check("'PolyForm Noncommercial' matches",
      [n for n, _ in name_anywhere("PolyForm Noncommercial License 1.0.0")], ["PolyForm"])
check("case does not matter", [n for n, _ in name_anywhere("business source licence")],
      ["BUSL"])
check("the British spelling 'licence' matches",
      [n for n, _ in name_anywhere("Elastic Licence 2.0")], ["Elastic"])

# =======================================================================================
# 7. THE WINDOW AXIS — the measurement no anchor ORDER can make
# =======================================================================================
filler = "This Agreement sets forth the terms and conditions of use. " * 120
beyond = filler + " The License for the Community Edition is the Business Source License 1.1."
off = dict(name_anywhere(beyond))["BUSL"]
check("the synthetic payload puts BUSL beyond the window",
      off >= SHARED_CLASSIFIER_WINDOW, True)
check("verdict reports it as beyond_window", verdict(beyond)[3], "BUSL")
check("reach says unreachable-by-order", verdict(beyond)[4], "unreachable-by-order")
check("truncating at the shared window LOSES the name (the defect, restated as a control)",
      name_anywhere(beyond[:SHARED_CLASSIFIER_WINDOW]), [])
check("this instrument does NOT truncate", len(name_anywhere(beyond)), 1)

# =======================================================================================
# 8. Shapes that must not crash, and must not read as permission
# =======================================================================================
check("empty payload", verdict("")[0], "NO-KEYED-CONDITION")
check("whitespace-only payload", verdict("   \n\t  ")[0], "NO-KEYED-CONDITION")
check("empty payload reports no name", verdict("")[2], "-")
check("a 404 body is not a keyed grant", verdict("404: Not Found")[0], "NO-KEYED-CONDITION")
check("the negative verdict is NOT spelled 'OPEN' or 'ALLOWED'",
      verdict(mit)[0] in ("OPEN", "ALLOWED", "PERMISSIVE"), False)

# =======================================================================================
# 9. Sentence splitting — a section number must not split a sentence
# =======================================================================================
check("'4.1' does not split", len(sentences("Section 4.1 applies")), 1)
check("a real sentence boundary does split", len(sentences("One thing. Another thing")), 2)
check("semicolons split", len(sentences("first; second")), 2)
check("a condition split away from its artefact is not lost by over-splitting",
      verdict("Under section 4.1 You will not operate the Software without a License Key")[0],
      "KEYED-GRANT")

# =======================================================================================
# 10. THE FOUR PAYLOADS THE `ACTION XB` SWEEP TURNED UP, each a control for a different
#     reason.  All four are first-hand payloads from the 821 the sweep read.
# =======================================================================================
autogen = fx("autogen.cc-by-4.0.txt")
check("CC-BY-4.0 (autogen's root LICENSE) is NOT a keyed grant",
      verdict(autogen)[0], "NO-KEYED-CONDITION")
check("the CC-BY ETM sentence really is in the payload",
      "effective technological measures" in autogen.lower(), True)
check("CC-BY-4.0: no artefact kind survives the shield", keyed_grant(autogen)[1], [])

ggcheck = fx("ggcheck.cran-parameters.txt")
check("CRAN parameter file -> PARAMETER-FILE", verdict(ggcheck)[0], "PARAMETER-FILE")
check("CRAN parameter file is recognised by shape", parameter_file(ggcheck), True)
check("a real licence is NOT a parameter file", parameter_file(mit), False)
check("an empty payload is NOT a parameter file", parameter_file(""), False)
check("a parameter file with a grant sentence is not a parameter file",
      parameter_file("YEAR: 2026\nPermission is hereby granted, free of charge"), False)
check("the CRAN vocabulary covers the 'Person:' spelling",
      parameter_file("YEAR: 2026\nPERSON: Someone"), True)

sdv = fx("sdv.busl-1.1.txt")
check("sdv-dev/sdv: BUSL named at offset 0", name_anywhere(sdv)[0], ("BUSL", 0))
check("sdv-dev/sdv: verdict is NAMED-SOURCE-AVAILABLE",
      verdict(sdv)[0], "NAMED-SOURCE-AVAILABLE")

leemons = fx("leemons.faircode.txt")
check("leemonade/leemons: fair-code AND Sustainable Use both named",
      [n for n, _ in name_anywhere(leemons)], ["FAIRCODE", "SUL"])

# =======================================================================================
# 11. Idempotence / determinism
# =======================================================================================
check("verdict is deterministic", verdict(csl), verdict(csl))
check("name_anywhere is deterministic", name_anywhere(red), name_anywhere(red))
check("kinds come back sorted", keyed_grant(csl)[1], sorted(keyed_grant(csl)[1]))

print("\n%d/%d" % (OK, OK + len(BAD)))
if BAD:
    for label, got, want in BAD:
        print("  FAILED: %s  got=%r want=%r" % (label, got, want))
    raise SystemExit(1)
