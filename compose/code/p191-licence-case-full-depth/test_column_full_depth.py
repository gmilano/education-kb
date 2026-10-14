#!/usr/bin/env python3
"""Controls for `P1059` (p191). Offline: every fixture is authored here.

🔵 **The obligatory cases are the three this instrument's own first build got WRONG**, and
each one published a false accusation before it was caught by reading the row:

    1. a table row naming SEVERAL repos and SEVERAL ids was paired as a CROSS-PRODUCT
       (`AlexandreL0pes/q-scraper` accused of contradicting an `Apache-2.0` that belonged to
       `adiel-calixto/IFAcademico`, four cells away)
    2. an id named in the row's PROSE was read as the row's published id
       (`opencast/opencast` publishes `ECL-2.0` and EXPLAINS it as an *"OSI-approved
       Apache-2.0 derivative"*; the extractor saw `Apache-2.0`)
    3. the extractor's vocabulary and the comparator's family map DRIFTED
       (`ECL-2.0` was in one and not the other, so the row's real id was invisible)

A suite that only asserted "an MIT row with an MIT tree agrees" would pass with all three
defects in place, which is the mistake this file exists not to make.

    python3 test_column_full_depth.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from column_full_depth import PUBLISHED_FAMILY, compare  # noqa: E402
from published_rows import IDS, collect, row_pairs  # noqa: E402

PASS = FAIL = 0


def check(name, got, want):
    global PASS, FAIL
    if got == want:
        PASS += 1
    else:
        FAIL += 1
        print(f"FAIL {name}\n  got  {got!r}\n  want {want!r}")


# ── 1. the cross-product defect ───────────────────────────────────────────────────────
Q_ACADEMICO_ROW = (
    "| **Q-Acadêmico** | 🟢 **Brazil** | Best-licensed: "
    "[`adiel-calixto/IFAcademico`](https://github.com/adiel-calixto/IFAcademico) "
    "(**Apache-2.0**, 6★). Also [`AlexandreL0pes/q-scraper`]"
    "(https://github.com/AlexandreL0pes/q-scraper) and a GPL-3.0 fork |"
)
multi = collect({"verticals/solutions.md": Q_ACADEMICO_ROW})
check("multi-slug row attributes no id confidently",
      [multi[s]["confident"] for s in sorted(multi)], [False, False])
check("multi-slug row still RECORDS the ids it saw",
      sorted(multi["AlexandreL0pes/q-scraper"]["ids"]), ["Apache-2.0", "GPL-3.0"])

SOLE_ROW = ("| [`linyeping/GemMate`](https://github.com/linyeping/GemMate) | 🟢 MIT | "
            "**Dart** | On-device Gemma |")
sole = collect({"repos/trending.md": SOLE_ROW})
check("single-slug row IS confident", sole["linyeping/GemMate"]["confident"], True)
check("single-slug row keeps its id", sole["linyeping/GemMate"]["ids"], ["MIT"])

# A slug seen on BOTH shapes must take the confident attribution, not the cross-product one.
both = collect({"a.md": SOLE_ROW, "b.md": Q_ACADEMICO_ROW.replace(
    "AlexandreL0pes/q-scraper", "linyeping/GemMate")})
check("sole attribution wins over multi", both["linyeping/GemMate"]["ids"], ["MIT"])
check("sole attribution marks confident", both["linyeping/GemMate"]["confident"], True)

# ── 2. the prose-id defect ────────────────────────────────────────────────────────────
OPENCAST_ROW = (
    "| 🟢 **[`opencast/opencast`](https://github.com/opencast/opencast)** | 🟢 **`ECL-2.0`** "
    "*(`11 340` B, full text; OSI-approved `Apache-2.0` derivative for universities)* |")
oc = row_pairs(OPENCAST_ROW)
check("the row's OWN id is captured", ("opencast/opencast", "ECL-2.0") in oc, True)
check("the explained id is also captured, so BOTH are candidates",
      ("opencast/opencast", "Apache-2.0") in oc, True)
# The verdict must be AGREE: any published id matching the tree settles the row. This is
# what makes case 2 survivable without a prose parser.
check("ECL-2.0 tree + (ECL-2.0, Apache-2.0) published = AGREE",
      compare(["ECL-2.0", "Apache-2.0"],
              ("opencast/opencast", "OWN-GRANT-AT-ROOT", "9", "LICENSE", "ECL-2.0",
               "-", "-"))[0],
      "AGREE")
check("Apache-2.0 alone against an ECL-2.0 tree WOULD contradict (the old bug)",
      compare(["Apache-2.0"],
              ("opencast/opencast", "OWN-GRANT-AT-ROOT", "9", "LICENSE", "ECL-2.0",
               "-", "-"))[0],
      "CONTRADICTED")

# ── 3. the vocabulary-drift control ───────────────────────────────────────────────────
check("every extractor id has a family mapping",
      sorted(set(IDS) - set(PUBLISHED_FAMILY)), [])
check("ECL-2.0 is in the extractor vocabulary", "ECL-2.0" in IDS, True)
check("EUPL-1.2 is in the extractor vocabulary", "EUPL-1.2" in IDS, True)

# ── the verdict vocabulary ────────────────────────────────────────────────────────────
check("real contradiction fires",
      compare(["MIT"], ("linyeping/GemMate", "OWN-GRANT-AT-ROOT", "40", "LICENSE",
                        "Apache-2.0", "-", "-"))[0], "CONTRADICTED")
check("TEXT-ABSENT is NOT a contradiction",
      compare(["GPL-3.0"], ("frappe/education", "ABSENCE-ENUMERATED", "900", "-", "-",
                            "-", "-"))[0], "TEXT-ABSENT")
check("BUNDLED-ONLY is its own verdict",
      compare(["GPL-2.0"], ("OS4ED/openSIS-Classic", "BUNDLED-GRANT-ONLY", "5000",
                            "libraries/ckeditor/LICENSE.md", "LGPL", "-", "-"))[0],
      "BUNDLED-ONLY")
check("an ambiguous payload is handed over, never decided",
      compare(["MIT"], ("nvaccess/nvda", "OWN-GRANT-AT-ROOT", "80", "copying.txt",
                        "GPL?", "-", "copying.txt=GPL+LGPL"))[0], "FAMILY-AMBIGUOUS")
check("UNRESOLVABLE survives",
      compare(["MIT"], ("gone/gone", "UNRESOLVABLE", "0", "-", "-", "-", "-"))[0],
      "UNRESOLVABLE")
# Version is DELIBERATELY not discriminated here (declared limit): GPL-2.0 published
# against a GPL-3.0 tree is AGREE, because `family_of` cannot answer the version.
check("family-level comparison is the declared limit",
      compare(["GPL-2.0"], ("os4ed/openSIS-Classic", "OWN-GRANT-AT-ROOT", "900",
                            "LICENSE", "GPL", "-", "-"))[0], "AGREE")

# ── the population extractor's boundaries ─────────────────────────────────────────────
check("prose outside a table row is not a published row",
      collect({"x.md": "The repo [`a/b`](https://github.com/a/b) is MIT."}), {})
check("a row with no licence id yields nothing",
      collect({"x.md": "| [`a/b`](https://github.com/a/b) | 42★ |"}), {})
check("a .git suffix is stripped from the slug",
      row_pairs("| https://github.com/a/b.git | MIT |"), [("a/b", "MIT")])
check("AGPL-3.0 is not swallowed by GPL-3.0",
      row_pairs("| https://github.com/a/b | AGPL-3.0 |"), [("a/b", "AGPL-3.0")])
check("CC-BY-NC-SA-4.0 is not swallowed by CC-BY-4.0",
      row_pairs("| https://github.com/a/b | CC-BY-NC-SA-4.0 |"),
      [("a/b", "CC-BY-NC-SA-4.0")])

print(f"\nP1059 — {PASS} passed, {FAIL} failed  ({PASS + FAIL} controls)")
sys.exit(1 if FAIL else 0)
