#!/usr/bin/env python3
"""Suite for `p444`'s README-claim channel.  Offline; fixtures captured first-hand.

The MANDATORY case is `ipti/br.tag`: README states BSD-3-Clause, payload is GPL-2.0.  It is
mandatory because it is the case `Gap 443-C` was declared for, and because it is the
EXPENSIVE direction — the README is the permissive one.

The NEGATIVE cases are the ones that earn the instrument: a README that NAMES a licence
without CLAIMING it must grade SILENT.  Without those, this channel is a licence-word grep.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from readme_claim import claims_in, TIER, foreign_subject  # noqa: E402
from compare import verdict, _norm  # noqa: E402

PASS = FAIL = 0


def check(name, got, want):
    global PASS, FAIL
    if got == want:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL {name}\n       got  {got!r}\n       want {want!r}")


def fams(text):
    return sorted(c.family for c in claims_in(text))


def ctxs(text):
    return sorted(c.context for c in claims_in(text))


# --- 1. the mandatory real fixture ------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
FX = os.path.join(HERE, "fixtures", "ipti_br.tag.README.md")
if os.path.exists(FX):
    with open(FX, encoding="utf-8", errors="replace") as fh:
        brtag = fh.read()
    check("br.tag claims BSD-3-Clause", fams(brtag), ["BSD-3-Clause"])
    # 🔴 The load-bearing assertion: the claim must come from the SECTION, because the
    # repository's BSD badge is HTML-COMMENTED OUT.  If this ever reads BADGE, the comment
    # stripper has regressed and the instrument is reporting a dead shield as a live claim.
    check("br.tag claim is SECTION not BADGE", ctxs(brtag), ["SECTION"])
    check("br.tag verdict", verdict(claims_in(brtag), "GPL-2.0")[0], "README-MORE-PERMISSIVE")
else:
    print(f"  SKIP missing fixture {FX}")

# --- 1b. the SUBJECT gate, from the defect this instrument's own first live run found ---
# `jeanhrm/siagie-analytics` ships an unmodified Laravel skeleton README and NO grant file.
# Subject-blind, the claim gate read "The Laravel framework is open-sourced software
# licensed under the MIT license" as the repository's own MIT claim, and the comparator
# published `NO-PAYLOAD` — "states MIT, never made the grant".  Laravel stated it.
FX2 = os.path.join(HERE, "fixtures", "jeanhrm_siagie-analytics.README.md")
if os.path.exists(FX2):
    with open(FX2, encoding="utf-8", errors="replace") as fh:
        skel = fh.read()
    # Subject-blind (no slug): the claim is found, which is what made the false row.
    check("laravel skeleton: subject-blind still sees MIT", fams(skel), ["MIT"])
    # With the slug, it must be attributed to Laravel and NOT to the repository.
    cs2 = claims_in(skel, "jeanhrm/siagie-analytics")
    check("laravel skeleton: claim is FOREIGN",
          sorted(c.context for c in cs2), ["FOREIGN:Laravel"])
    own2 = [c for c in cs2 if not c.context.startswith("FOREIGN")]
    check("laravel skeleton: repository claims nothing of its own", own2, [])
    check("laravel skeleton verdict is SILENT not NO-PAYLOAD",
          verdict(own2, "NO-PAYLOAD")[0], "README-SILENT")
else:
    print(f"  SKIP missing fixture {FX2}")

# A repository whose OWN name is the subject keeps its claim: the gate must not eat it.
check("own-name subject is not foreign",
      sorted(c.context for c in claims_in(
          "The Moodle framework is open-sourced software licensed under the GPL-3.0 license.",
          "moodle/moodle")), ["SECTION"] if False else ["PROSE"])

# --- 2. comment stripping, isolated -----------------------------------------------------
check("commented badge alone is SILENT",
      fams("<!-- [![License](https://img.shields.io/badge/License-MIT-green.svg)](x) -->"), [])
check("live badge is a claim",
      fams("[![License](https://img.shields.io/badge/License-MIT-green.svg)](x)"), ["MIT"])

# --- 3. the negative cases: a NAME is not a CLAIM ---------------------------------------
check("comparison prose claims nothing",
      fams("Unlike the GPL-3.0 projects in this space, we move fast."), [])
check("dependency table claims nothing",
      fams("| dep | licence |\n|---|---|\n| left-pad | MIT |\n| foo | Apache-2.0 |"), [])
check("prose claim is caught",
      fams("This project is licensed under the MIT License."), ["MIT"])
check("spanish prose claim is caught",
      fams("Este proyecto se distribuye bajo la licencia Apache-2.0."), ["Apache-2.0"])
check("portuguese prose claim is caught",
      fams("Distribuido sob a licença MIT."), ["MIT"])

# --- 4. P171, through the README instead of the payload ---------------------------------
# GPL-3.0's section 13 is titled "Use with the GNU Affero General Public License", so a
# README that INLINES a GPL-3.0 body must not be read as AGPL.  Same defect class as P171,
# different channel; the section reader is capped at 8 lines for exactly this reason.
gpl3_section = ("## License\n\nGNU General Public License v3.0\n\n" + "body line\n" * 6 +
                "  13. Use with the GNU Affero General Public License.\n")
check("inlined GPL-3.0 body is not AGPL", fams(gpl3_section), ["GPL-3.0"])

# --- 5. longest-name-first ordering -----------------------------------------------------
check("AGPL beats GPL", fams("Licensed under the AGPL-3.0 licence."), ["AGPL-3.0"])
check("LGPL beats GPL", fams("Licensed under the LGPL-3.0 licence."), ["LGPL-3.0"])

# --- 6. the tier comparison, which is the verdict ---------------------------------------
class C:
    def __init__(s, f):
        s.family, s.tier, s.context, s.evidence = f, TIER[f], "PROSE", ""


check("MIT README over GPL payload", verdict([C("MIT")], "GPL-3.0")[0], "README-MORE-PERMISSIVE")
check("GPL README over MIT payload", verdict([C("GPL-3.0")], "MIT")[0], "README-MORE-RESTRICTIVE")
check("MIT over MIT agrees", verdict([C("MIT")], "MIT")[0], "AGREE")
check("MIT README over BSD payload is same tier",
      verdict([C("MIT")], "BSD")[0], "DIVERGE-SAME-TIER")
# 🟢 The normalisation case: `family_of` says `BSD`, the README says `BSD-3-Clause`.  Same
# grant, and grading that DIVERGE would make the instrument cry wolf on every BSD row.
check("BSD-3-Clause README over BSD payload AGREES",
      verdict([C("BSD-3-Clause")], "BSD")[0], "AGREE")
check("claim with no payload is NO-PAYLOAD", verdict([C("MIT")], "NO-PAYLOAD")[0], "NO-PAYLOAD")
check("no claim and no payload is SILENT", verdict([], "NO-PAYLOAD")[0], "README-SILENT")
check("most permissive claim is the one that counts",
      verdict([C("GPL-3.0"), C("MIT")], "GPL-3.0")[0], "AGREE")
check("norm collapses BSD variants", _norm("BSD-2-Clause"), "BSD")

# --- 7. the UNMAPPED-FAMILY defect, found by the first shelf run -----------------------
# `TIER.get(fam, 9)` made every unmapped payload family maximally restrictive, so any README
# claim became README-MORE-PERMISSIVE.  Two of the shelf's four such verdicts were this
# artefact.  A missing map entry must accuse the MAP, never the repository.
from readme_claim import tier_of  # noqa: E402

check("unmapped payload family is not a finding",
      verdict([C("MIT")], "SOME-NEW-LICENCE-9.9")[0], "PAYLOAD-FAMILY-UNMAPPED")
check("tier_of returns None when unmapped", tier_of("SOME-NEW-LICENCE-9.9"), None)
# The two real shelf payloads that triggered it, now mapped rather than defaulted.
check("MPL-1.1 is mapped (weak copyleft)", tier_of("MPL-1.1"), 1)
check("ODbL is mapped (share-alike)", tier_of("ODbL-UNVERSIONED"), 2)
check("openSIS case: GPL README over MPL-1.1 payload is MORE RESTRICTIVE, not permissive",
      verdict([C("GPL-3.0")], "MPL-1.1")[0], "README-MORE-RESTRICTIVE")
# And the one that must SURVIVE the fix: a genuinely mapped, genuinely permissive claim over
# a genuinely non-OSI payload stays a finding.
check("MIT badge over a NONCOMMERCIAL payload is still the expensive verdict",
      verdict([C("MIT")], "NONCOMMERCIAL-NOT-OSI")[0], "README-MORE-PERMISSIVE")

# --- 8. SCOPED DUAL LICENSING is a correct README, not a finding ------------------------
# The `pengusto/google-classroom-mcp` case: badge "Commercial extensions / MIT upstream",
# tree carries `LICENSE` + `LICENSES/MIT-upstream.txt`.  Two claims + two grant paths.
check("dual grant declared is not an accusation",
      verdict([C("MIT"), C("PROPRIETARY")], "NONCOMMERCIAL-NOT-OSI", n_grants=2)[0],
      "DUAL-GRANT-DECLARED")
# ...and a SINGLE-grant tree with one permissive claim over a non-OSI payload still fires.
check("one grant path keeps the expensive verdict",
      verdict([C("MIT")], "NONCOMMERCIAL-NOT-OSI", n_grants=1)[0], "README-MORE-PERMISSIVE")
# ipti/br.tag must survive: ONE grant path, one claim, genuine divergence.
check("br.tag survives the dual-grant exemption",
      verdict([C("BSD-3-Clause")], "GPL-2.0", n_grants=1)[0], "README-MORE-PERMISSIVE")

# --- 9. the BUNDLED surface form, and unversioned family matching -----------------------
# os-taxonomy's exemplary multi-licence table closes with "Bundled Three.js and Baloo 2
# retain their separate MIT and OFL licenses" — the MIT is three.js's.
from readme_claim import bundled_claim  # noqa: E402

check("bundled-retains is detected",
      bundled_claim("Bundled Three.js and Baloo 2 retain their separate MIT and OFL licenses."), True)
tax = ("## License\n\nThis dataset is multi-licensed.\n\n"
       "The database is under ODbL 1.0; Marble-authored content under CC BY-SA 4.0. "
       "Bundled Three.js and Baloo 2 retain their separate MIT and OFL licenses and notices.\n")
own_tax = [c for c in claims_in(tax, "withmarbleapp/os-taxonomy")
           if not c.context.startswith("FOREIGN")]
check("os-taxonomy claims no MIT of its own", [c.family for c in own_tax if c.family == "MIT"], [])
# A project really claiming MIT must still be caught.
check("a real MIT claim survives the bundled gate",
      [c.family for c in claims_in("## License\n\nMIT. See LICENSE.", "x/y")], ["MIT"])

# Unversioned claims: "GPL" in prose vs a GPL-2.0 payload is not a divergence...
check("bare GPL claim matches GPL-2.0 payload",
      verdict([C("GPL")], "GPL-2.0")[0], "AGREE")
check("bare BSD claim matches BSD-3-Clause payload",
      verdict([C("BSD")], "BSD-3-Clause")[0], "AGREE")
# ...but GPL must NOT swallow AGPL or LGPL, which are different obligations (P171's spirit).
check("bare GPL claim does NOT match AGPL-3.0 payload",
      verdict([C("GPL")], "AGPL-3.0")[0], "README-MORE-PERMISSIVE")
check("bare GPL claim does NOT match LGPL-3.0 payload",
      verdict([C("GPL")], "LGPL-3.0")[0], "README-MORE-RESTRICTIVE")

print(f"\n{PASS}/{PASS + FAIL} passed")
sys.exit(1 if FAIL else 0)
