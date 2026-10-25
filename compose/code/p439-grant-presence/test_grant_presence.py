#!/usr/bin/env python3
"""p439 — controls for `grant_presence.py`.  OFFLINE: every fixture is committed beside
this file with its sha256₁₂ in the table below.

🔵 THE CONTROLS THAT CARRY THIS SUITE ARE THE NEGATIVES.  Two of them are defects this
instrument ACTUALLY HAD, caught by this base's own corpus before the gate was wired:

  C3  the FULL Apache-2.0 text (11 357 B · `c71d239df917`) carries all three
      REFERENCE_MARKERS, because the APPENDIX notice is PART OF the licence.  An
      instrument keyed on those markers alone condemns every valid Apache-2.0 payload in
      existence.  This is `P171`'s shape exactly — the discriminator for "the grant is
      elsewhere" appears verbatim inside the grant — and it is why clause presence is
      asked FIRST and the markers only break the tie.
  C6  `mit-curly-quotes-1096.LICENSE` (1 096 B · `e1d1fa9f3a8d`) is a COMPLETE MIT
      licence from a load-bearing dependency, and the first profile written here graded
      it GRANT-TRUNCATED because it typesets “AS IS” with U+201C/U+201D.  A real grant
      condemned by a punctuation character.

| fixture | sha256₁₂ | why it is here |
|---|---|---|
| `vercel-notice-552.LICENSE` | `5809eb2eab28` | the live specimen: Apache-2.0 APPENDIX notice, holder **Vercel, Inc.** |
| `apache2-full-11357.LICENSE` | `c71d239df917` | C3's negative — markers present, grant present |
| `mit-full-1077.LICENSE` | `4679aa0db6a3` | stock MIT, must not be flagged |
| `mit-curly-quotes-1096.LICENSE` | `e1d1fa9f3a8d` | C6's negative — typographic quotes |
| `mit-no-liability-cap-797.LICENSE` | `ec4ab498897e` | keeps "AS IS", drops "IN NO EVENT SHALL" |
| `apache2-appendix-only-311.txt` | `f40ea994b54e` | appendix with NO url — TRUNCATED, not BY-REFERENCE |
| `ccbyncsa-uncalibrated-936.LICENSE` | `86d64326f24d` | a family with no profile: declines to judge |

🆕 `p440` — the GPL family group (`Gap 439-B`).  Each is a copy of a payload already
committed elsewhere on this tree, brought beside this suite so the controls are offline
and the digests pinned here.  🔴 `C17`'s pair is the load-bearing one: the two licences
share nearly all their text and differ on the clause the whole family question turns on.

| fixture | sha256₁₂ | why it is here |
|---|---|---|
| `gpl3-full-35147.LICENSE` | `8ceb4b9ee5ad` | 🔴 `C17`'s negative — stock GPL-3.0, which names Affero in its own §13 heading and must NOT satisfy the AGPL profile |
| `agpl3-full-34523.LICENSE` | `8486a10c4393` | `C17`'s positive — stock AGPL-3.0, all eight clauses including the operative §13 |
| `gpl2-full-18092.LICENSE` | `8177f9751321` | 🔴 `C18`'s negative — a COMPLETE GPL-2.0 licence, missing four of GPL-3.0's six clauses |
| `gpl3-section13-470.txt` | `4703727d5a66` | `C20` — 470 B of GPL-3.0 §13 that `titled_family()` reads as AGPL: a fragment, not a grant |
| `agpl3-narrative-1930.LICENSE` | `bde7d05790a0` | `C20b` — an AGPL narrative summary, no operative clauses |
| `lgpl3-full-7378.txt` | `dc1ab8bc8b6a` | `C21` — stock LGPL-3.0, which carries none of GPL-3.0's headings because it incorporates them BY REFERENCE by design (`Gap 440-B`) |

🆕 `p441` — the BSD family (`Gap 440-A`).  Five of the seven are **live payloads from this
base's own published shelves**, probed 2026-10-25 and committed here with the digest the
probe recorded, so every control below runs offline against the bytes a client would get.
🔴 `C26`'s pair is the load-bearing one, and it refutes the gap's own prescription.

| fixture | sha256₁₂ | why it is here |
|---|---|---|
| `bsd3-full-1514.LICENSE` | `1bdccc1d297a` | stock BSD-3, all eight clauses — `C23`, and the parent of both `C26` mutants |
| `bsd2-full-1340.LICENSE` | `9564f738acee` | 🔴 `C24` — a COMPLETE BSD-2 licence, which has no endorsement clause and must not be condemned for lacking one |
| `bsd3-stub-164.txt` | `03a5ccada796` | `C25` — 164 B: a BSD-3 title and the opening of the grant, nothing more |
| `bsd3-untitled-jupyterhub-1475.LICENSE` | `7069c7e8d60e` | 🔴 `C27` — live `jupyterhub/jupyterhub`: a COMPLETE BSD-3 grant with **no title line at all**, so `titled_family()` answers None |
| `bsd-r-manifest-stub-108.LICENSE` | `de5d9459d263` | 🔴 `C28` — live `ucbds-infra/ottr` `LICENSE`: 108 B of `YEAR:` / `COPYRIGHT HOLDER:`, the R convention, with the grant itself at `LICENSE.md` |
| `bsd3-reverse-declaration-qtiworks-2058.LICENSE.txt` | `a5c692f12090` | `C29` — live `OpenOLAT/qtiworks`: declares *"the 3-clause BSD license"*, variant before family |
| `bsd3-plus-branding-openwebui-2819.LICENSE` | `5f1bd74c48bf` | 🔴 `C30` — live `open-webui/open-webui`: stock BSD-3 **plus** a branding restriction and a CLA.  `GRANT-PRESENT` is not `GRANT-UNMODIFIED`, and this is the specimen that says so |
"""
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import grant_presence as gp  # noqa: E402

sys.path.insert(0, str(HERE.parent / "p341-bespoke-instrument-census"))
import bespoke_census as bc  # noqa: E402

FX = HERE / "fixtures"


def bc_titled(path):
    """The TITLED family of a payload — the answer `p441` found is None for four of this
    base's eleven published BSD rows."""
    return bc.titled_family(pathlib.Path(path).read_text(errors="replace"))
fails = []
n = 0


def check(label, got, want):
    global n
    n += 1
    if got != want:
        fails.append("%s: got %r, want %r" % (label, got, want))


def verdict(name, family):
    return gp.classify((FX / name).read_text(errors="replace"), family)["verdict"]


# C1 — the live specimen.  A 552 B payload naming Apache-2.0 is a pointer, not a grant.
check("C1 vercel notice is BY-REFERENCE",
      verdict("vercel-notice-552.LICENSE", "Apache-2.0"), "GRANT-BY-REFERENCE")

# C2 — and the holder it names is a third party, which is the half a licence verdict
# cannot carry.  Asserted on the payload text so the claim cannot rot.
check("C2 vercel notice names Vercel, not the repo author",
      "Vercel, Inc." in (FX / "vercel-notice-552.LICENSE").read_text(), True)

# C3 — 🔴 THE LOAD-BEARING NEGATIVE.  Full Apache-2.0 must pass DESPITE the markers.
check("C3 full Apache-2.0 is PRESENT",
      verdict("apache2-full-11357.LICENSE", "Apache-2.0"), "GRANT-PRESENT")
check("C3b full Apache-2.0 does carry the reference markers",
      len(gp.references_found((FX / "apache2-full-11357.LICENSE").read_text())) >= 3, True)

# C4 — stock MIT, untouched.
check("C4 full MIT is PRESENT", verdict("mit-full-1077.LICENSE", "MIT"), "GRANT-PRESENT")

# C5 — the liability cap is its own clause.  "AS IS" present, "IN NO EVENT SHALL" gone.
check("C5 MIT without the liability cap is TRUNCATED",
      verdict("mit-no-liability-cap-797.LICENSE", "MIT"), "GRANT-TRUNCATED")
check("C5b and the missing clause is named",
      gp.classify((FX / "mit-no-liability-cap-797.LICENSE").read_text(), "MIT")["missing"],
      ["liability-cap"])

# C6 — 🔴 THE SECOND LOAD-BEARING NEGATIVE: typographic quotes are not a defect.
check("C6 curly-quoted MIT is PRESENT",
      verdict("mit-curly-quotes-1096.LICENSE", "MIT"), "GRANT-PRESENT")

# C7 — TRUNCATED and BY-REFERENCE are different answers, and the discriminator is
# whether the payload says where the grant went.
check("C7 appendix with no url is TRUNCATED",
      verdict("apache2-appendix-only-311.txt", "Apache-2.0"), "GRANT-TRUNCATED")

# C8 — declining to judge is a THIRD answer, not a pass.  `P250`.
check("C8 a family with no profile is UNCALIBRATED",
      verdict("ccbyncsa-uncalibrated-936.LICENSE", "CC-BY-NC-SA-4.0"), "GRANT-UNCALIBRATED")
check("C8b an unknown family is UNCALIBRATED, not PRESENT",
      gp.classify("whatever", None)["verdict"], "GRANT-UNCALIBRATED")

# C9 — an UNCALIBRATED row raises no finding, so the gate cannot be made green by
# feeding it families it does not know.
check("C9 UNCALIBRATED is not a finding",
      gp.FINDING.get("GRANT-UNCALIBRATED", ""), "")

# C10 — the byte count comes from the untouched payload (`P834`), not the normalised one.
check("C10 bytes are the payload's own",
      gp.classify((FX / "vercel-notice-552.LICENSE").read_text(), "Apache-2.0")["bytes"], 552)

# C11 — `P541`: measuring nothing is a REFUSAL, exit 2, not a clean tree.
r = subprocess.run([sys.executable, "-I", str(HERE / "grant_presence.py")],
                   capture_output=True, text=True)
check("C11 no input refuses with exit 2", r.returncode, 2)
check("C11b and says so", "P439-NO-INPUT" in r.stderr, True)

# C12 — a path that is not a file is a refusal too, never a zero-finding pass.
r = subprocess.run([sys.executable, "-I", str(HERE / "grant_presence.py"),
                    str(HERE / "does-not-exist")], capture_output=True, text=True)
check("C12 missing file refuses with exit 2", r.returncode, 2)

# C13 — the CLI exits 1 when it finds something, so a `make` target can gate on it.
r = subprocess.run([sys.executable, "-I", str(HERE / "grant_presence.py"),
                    str(FX / "vercel-notice-552.LICENSE")], capture_output=True, text=True)
check("C13 a finding exits 1", r.returncode, 1)
check("C13b and names the finding", "P439-BY-REFERENCE" in r.stdout, True)

# C14 — and exits 0 on a clean payload, so the gate is not a constant.
r = subprocess.run([sys.executable, "-I", str(HERE / "grant_presence.py"),
                    str(FX / "mit-full-1077.LICENSE")], capture_output=True, text=True)
check("C14 a clean payload exits 0", r.returncode, 0)

# C15 — 🔴 EVERY REFERENCE MARKER MUST BE ABLE TO FIRE.  The first draft of this
# instrument wrote two of its five markers with uppercase `LICEN[SC]E` / `COPYING`
# literals and matched them against text `_norm()` had already lowercased, so they were
# dead code that still read as coverage.  One specimen per marker, asserted by name.
_SPECIMENS = {
    "apache-appendix": 'You may obtain a copy of the License at http://x.example/l',
    "compliance-notice": 'you may not use this file except in compliance with the License',
    "licence-url": "see https://opensource.org/licenses/MIT for terms",
    "see-file": "See LICENSE for the full terms.",
    "md-link": "Released under [the MIT License](./LICENSE).",
}
for _marker, _text in _SPECIMENS.items():
    check("C15 marker %s fires" % _marker, _marker in gp.references_found(_text), True)
check("C15b no marker is unreachable",
      sorted(_SPECIMENS) == sorted(lbl for lbl, _ in gp.REFERENCE_MARKERS), True)

# ---------------------------------------------------------------- p440
# 🟢 `Gap 439-B`'s first family group.  The controls below are mostly NEGATIVES, because
# the entire risk in profiling the GPL family is condemning a VALID grant: AGPL-3.0 and
# GPL-3.0 share nearly all of their text, and GPL-2.0 shares almost none of GPL-3.0's.

# C16 — the three new profiles accept their own stock text.  Nothing subtle: if these
# fail, the profiles are simply wrong.
check("C16 stock GPL-3.0 is PRESENT",
      verdict("gpl3-full-35147.LICENSE", "GPL"), "GRANT-PRESENT")
check("C16b stock AGPL-3.0 is PRESENT",
      verdict("agpl3-full-34523.LICENSE", "AGPL"), "GRANT-PRESENT")
check("C16c stock GPL-2.0 is PRESENT",
      verdict("gpl2-full-18092.LICENSE", "GPL"), "GRANT-PRESENT")

# C17 — 🔴 THE LOAD-BEARING NEGATIVE OF THIS PASS, AND IT IS `P171` BY NAME.  Stock
# GPL-3.0 carries `GNU Affero General Public License` in its own §13 HEADING and
# `interaction through a network` in that section's body, so a detector keyed on either
# phrase calls all 18 of this base's GPL-3.0 payloads AGPL.  The operative AGPL §13
# sentence must be ABSENT from GPL-3.0 — asserted on the CLAUSE directly, not inferred
# from a verdict, so the claim cannot survive the clause being quietly weakened.
_gpl3 = (FX / "gpl3-full-35147.LICENSE").read_text()
# 🔵 `or []` so that REMOVING the AGPL profile altogether reports a clean red here
# rather than a traceback.  A control that crashes still stops a commit, but it reports
# the wrong thing: the next reader sees a broken test, not a withdrawn guard.
check("C17 GPL-3.0 lacks AGPL's operative §13 clause",
      "remote-network-grant" in (gp.clause_report(_gpl3, "AGPL")[1] or []), True)
check("C17b so GPL-3.0 read as AGPL is NOT a grant",
      gp.classify(_gpl3, "AGPL")["verdict"] != "GRANT-PRESENT", True)
check("C17c and GPL-3.0 DOES name Affero — which is why the name cannot be the test",
      "affero" in _gpl3.lower(), True)
check("C17d while real AGPL-3.0 does carry the clause",
      gp.clause_report((FX / "agpl3-full-34523.LICENSE").read_text(), "AGPL")[1], [])

# C18 — 🔴 THE SECOND NEGATIVE: the VERSION, not the family, selects the clauses.  A
# complete GPL-2.0 licence is missing four of GPL-3.0's six clauses — it never claimed
# them.  A single naive "GPL" profile would condemn all 19 stock GPL-2.0 payloads on
# this tree, which is the cost `Gap 439-B` priced and declined to pay at `p439`.  Held
# as a control so it stays paid.
_gpl2 = (FX / "gpl2-full-18092.LICENSE").read_text()
_g2_flat = gp._norm(_gpl2)
_missing_under_30 = sorted(lbl for lbl, rx in gp.CLAUSE_PROFILE["GPL-3.0"]
                           if not re.search(rx, _g2_flat))
check("C18 a COMPLETE GPL-2.0 licence fails the 3.0 profile", len(_missing_under_30), 4)
check("C18b and the structural clauses are the ones it lacks",
      "basic-permissions" in _missing_under_30
      and "conveying-modified" in _missing_under_30, True)
check("C18c but it is graded against its own version and passes",
      gp.classify(_gpl2, "GPL")["profile"], "GPL-2.0")
check("C18d and GPL-3.0 is graded against GPL-3.0",
      gp.classify(_gpl3, "GPL")["profile"], "GPL-3.0")

# C19 — the version resolver REFUSES rather than guessing (`P250`).
check("C19 an undeclared version is unresolvable", gp.resolve_version("GNU GPL"), None)
check("C19b two declared versions REFUSE — it does not take the first",
      gp.resolve_version("version 3 and also version 2"), None)
check("C19c an unresolvable version yields no profile",
      gp.profile_key("GNU General Public License", "GPL"), None)
check("C19d and therefore UNCALIBRATED, never a silent pass",
      gp.classify("GNU General Public License, see the file COPYING", "GPL")["verdict"],
      "GRANT-UNCALIBRATED")

# C20 — 🔴 THE SPECIMEN THAT READS AS AGPL AND IS A FRAGMENT OF GPL.
# `gpl3-section13-470.txt` is 470 B of GPL-3.0's §13, and `titled_family()` answers
# AGPL because the Affero name is the most title-shaped thing in it.  It carries none of
# AGPL's operative clauses, so it must not be graded a grant in either direction.
check("C20 a 470 B GPL-3.0 §13 excerpt titled AGPL is not a grant",
      verdict("gpl3-section13-470.txt", "AGPL") in
      ("GRANT-TRUNCATED", "GRANT-BY-REFERENCE"), True)
check("C20b a 1 930 B AGPL narrative summary is not a grant either",
      verdict("agpl3-narrative-1930.LICENSE", "AGPL") in
      ("GRANT-TRUNCATED", "GRANT-BY-REFERENCE"), True)

# C21 — 🔴 LGPL DECLINES ON PURPOSE, AND THAT IS A REGISTERED FINDING.  LGPL-3.0
# incorporates GPL-3.0 by reference by its own design, so a profile built from GPL-3.0's
# clauses would grade every valid LGPL-3.0 payload BY-REFERENCE — formally true and
# commercially useless.  `Gap 440-B`.  This control pins the DECISION: adding an LGPL
# profile without a verdict for incorporation-by-design now breaks a test instead of
# shipping a wrong answer to a client.
check("C21 stock LGPL-3.0 is UNCALIBRATED, deliberately",
      verdict("lgpl3-full-7378.txt", "LGPL"), "GRANT-UNCALIBRATED")
check("C21b and no LGPL profile exists, so that cannot become accidental",
      [k for k in gp.CLAUSE_PROFILE if k.startswith("LGPL")], [])

# C22 — the pre-`p440` families are untouched: versioning must not have reached them.
check("C22 MIT still resolves to its own profile", gp.profile_key("x", "MIT"), "MIT")
check("C22b Apache-2.0 is not treated as versioned despite naming a version",
      gp.profile_key("Apache License Version 2.0", "Apache-2.0"), "Apache-2.0")

# ─────────────────────────────────────────────────────────────────── 🆕 p441 · BSD
# `Gap 440-A`, bought — and its prescription ("the variant resolved from the clause
# structure") refuted at `C26`.

_b3 = (FX / "bsd3-full-1514.LICENSE").read_text()
_b2 = (FX / "bsd2-full-1340.LICENSE").read_text()

# C23 — stock BSD-3 passes, and the profile that judged it is NAMED in the row.
check("C23 stock BSD-3 is PRESENT",
      verdict("bsd3-full-1514.LICENSE", "BSD"), "GRANT-PRESENT")
check("C23b and it was graded against BSD-3, not against 'BSD'",
      gp.classify(_b3, "BSD")["profile"], "BSD-3")

# C24 — 🔴 THE FIRST LOAD-BEARING NEGATIVE.  A complete BSD-2 licence lacks the
# endorsement clause BY DESIGN.  One undifferentiated "BSD" profile written from the
# 3-clause text condemns it, which is `P171`'s shape in a new family and the cost
# `Gap 439-B` priced.
check("C24 a COMPLETE BSD-2 licence is PRESENT, not TRUNCATED",
      verdict("bsd2-full-1340.LICENSE", "BSD"), "GRANT-PRESENT")
check("C24b graded against BSD-2", gp.classify(_b2, "BSD")["profile"], "BSD-2")
check("C24c and it genuinely does not carry the discriminator",
      bool(re.search(gp.BSD_DISCRIMINATOR, gp._norm(_b2))), False)
check("C24d under BSD-3's profile it would fail on exactly one clause",
      sorted(lbl for lbl, rx in gp.CLAUSE_PROFILE["BSD-3"]
             if not re.search(rx, gp._norm(_b2))), ["no-endorsement"])

# C25 — the 164 B title-and-opening stub is an excerpt of its own grant.
check("C25 a 164 B BSD-3 stub is TRUNCATED",
      verdict("bsd3-stub-164.txt", "BSD"), "GRANT-TRUNCATED")

# C26 — 🔴 THE CONTROL THIS WHOLE DESIGN EXISTS FOR, AND THE REFUTATION OF `Gap 440-A`'s
# OWN PRESCRIPTION.  The mutants are DERIVED from `C23`'s pinned fixture rather than
# committed separately, so they cannot drift away from the licence they are a mutation of.
#
#   `_mut`          stock BSD-3 with clause 3 (the endorsement clause) CUT OUT.  Its
#                   title still says BSD-3, so the declaration arm answers BSD-3 and the
#                   payload is correctly 🟢 TRUNCATED on the clause it is missing.
#   `_mut_untitled` the same payload with the TITLE LINE ALSO removed.  Now nothing
#                   independent of the graded clauses says which variant it is: it is
#                   byte-for-byte a plausible complete BSD-2 and a plausible truncated
#                   BSD-3.  🔴 A resolver that reads the variant off the clause structure
#                   answers BSD-2 and returns GRANT-PRESENT — a FALSE PASS on the exact
#                   shape this instrument exists to catch.  It must DECLINE.
_mut = re.sub(r"3\. Neither the name.*?prior written permission\.", "", _b3, flags=re.S)
_mut_untitled = "\n".join(_mut.splitlines()[1:])
check("C26 the mutant really did lose the endorsement clause",
      bool(re.search(gp.BSD_DISCRIMINATOR, gp._norm(_mut))), False)
check("C26b with its title intact, the declaration arm answers BSD-3",
      gp.resolve_bsd_variant(_mut), "BSD-3")
check("C26c so a BSD-3 truncated at the endorsement clause is TRUNCATED",
      gp.classify(_mut, "BSD")["verdict"], "GRANT-TRUNCATED")
check("C26d on exactly that clause", gp.classify(_mut, "BSD")["missing"],
      ["no-endorsement"])
check("C26e 🔴 UNTITLED, the variant is UNRESOLVABLE — it must not be guessed",
      gp.resolve_bsd_variant(_mut_untitled), None)
check("C26f and the verdict is UNCALIBRATED, never a silent pass",
      gp.classify(_mut_untitled, "BSD")["verdict"], "GRANT-UNCALIBRATED")
check("C26g the false pass the structural resolver WOULD have produced, kept "
      "reproducible: under BSD-2's profile this payload is complete",
      sorted(lbl for lbl, rx in gp.CLAUSE_PROFILE["BSD-2"]
             if not re.search(rx, gp._norm(_mut_untitled))), [])

# C27 — 🔴 LIVE SUPPLY, AND IT CORRECTS `Gap 440-A`'s DIAGNOSIS.  `jupyterhub/jupyterhub`
# ships a COMPLETE BSD-3 grant with no title line, so the TITLE-based family answer is
# None and no BSD profile can be reached at all.  Four of this base's eleven published BSD
# rows are shaped this way.  The remedy is the hardened family owner's answer passed in,
# never a second family classifier here (`P171`).
check("C27 an untitled complete BSD-3 has no TITLED family",
      bc_titled(FX / "bsd3-untitled-jupyterhub-1475.LICENSE"), None)
check("C27b so by default it declines rather than lying",
      gp.classify((FX / "bsd3-untitled-jupyterhub-1475.LICENSE").read_text(),
                  bc_titled(FX / "bsd3-untitled-jupyterhub-1475.LICENSE"))["verdict"],
      "GRANT-UNCALIBRATED")
check("C27c and with the family supplied by its hardened owner it is PRESENT",
      verdict("bsd3-untitled-jupyterhub-1475.LICENSE", "BSD"), "GRANT-PRESENT")
check("C27d resolved by the discriminator, the one sound structural direction",
      gp.resolve_bsd_variant(
          (FX / "bsd3-untitled-jupyterhub-1475.LICENSE").read_text()), "BSD-3")

# C27e — 🔴 AND THE OVERRIDE IS EXERCISED THROUGH `main()`, BECAUSE MUTATION TESTING SAID
# IT WAS NOT.  `C27c` calls `classify()` with the family already in hand, so DELETING the
# `--family` plumbing in `main()` left all 82 controls green — a path with no control, in a
# suite whose own header says a control that cannot fail is not a control (`P237`).  These
# two run the file.
def _run(args):
    r = subprocess.run([sys.executable, "-I", str(HERE / "grant_presence.py")] + args,
                       capture_output=True, text=True)
    return [ln.split("\t") for ln in r.stdout.splitlines()
            if ln and not ln.startswith(("payload", "#"))]


_untitled = str(FX / "bsd3-untitled-jupyterhub-1475.LICENSE")
check("C27e through main(), the untitled payload declines by default",
      _run([_untitled])[0][4], "GRANT-UNCALIBRATED")
check("C27f and --family BSD reaches a clause profile and passes it",
      _run(["--family", "BSD", _untitled])[0][4], "GRANT-PRESENT")

# C28 — 🔴 THE R CONVENTION, ON A PUBLISHED ROW.  `ucbds-infra/ottr`'s `LICENSE` is 108 B
# of `YEAR:` / `COPYRIGHT HOLDER:` because `DESCRIPTION` says `BSD_3_clause + file
# LICENSE`; the licence TEXT is at `LICENSE.md` (1 555 B · `1677c5307530`, re-read at the
# pinned commit `693b3df` this hour, matching `evidence/verified-repos.2026-10-22-p394.tsv`
# exactly).  🟡 The published row is RIGHT.  What is wrong is any probe that takes the
# FIRST filename-ladder hit: it returns the stub and the repository reads as ungranted.
# `Gap 441-A`.
check("C28 the 108 B R stub carries no BSD clause of any variant",
      sorted(lbl for lbl, rx in gp.CLAUSE_PROFILE["BSD-2"]
             if re.search(rx, gp._norm(
                 (FX / "bsd-r-manifest-stub-108.LICENSE").read_text()))), [])
check("C28b and no variant can be resolved from it",
      gp.resolve_bsd_variant(
          (FX / "bsd-r-manifest-stub-108.LICENSE").read_text()), None)
check("C28c so even with the family forced it DECLINES — conservative to a fault, and "
      "registered as `Gap 441-C` rather than tightened by assuming no untitled 0BSD "
      "payload exists",
      verdict("bsd-r-manifest-stub-108.LICENSE", "BSD"), "GRANT-UNCALIBRATED")

# C29 — the declaration's word order is reversed on live supply, so both orders are read.
check("C29 'the 3-clause BSD license' resolves BSD-3",
      gp.resolve_bsd_variant(
          (FX / "bsd3-reverse-declaration-qtiworks-2058.LICENSE.txt").read_text()),
      "BSD-3")
check("C29b and the payload is a complete grant",
      verdict("bsd3-reverse-declaration-qtiworks-2058.LICENSE.txt", "BSD"),
      "GRANT-PRESENT")
# C29d — 🔴 WHAT THE REVERSED WORD ORDER IS ACTUALLY WORTH, pinned after mutation testing
# said the first version of `C29` was not load-bearing: on a COMPLETE payload the
# structural arm answers BSD-3 anyway, so deleting the reversed patterns changed nothing.
# It is the TRUNCATED reverse-declared payload where the declaration is the only thing
# left, and that is the shape a client is exposed to.
_qti = (FX / "bsd3-reverse-declaration-qtiworks-2058.LICENSE.txt").read_text()
_qti_cut = re.sub(r"3\. Neither the name.*?prior written permission\.", "", _qti,
                  flags=re.S)
check("C29d the reverse-declared payload really carries no canonical declaration",
      "bsd 3-clause" in gp._norm(_qti), False)
check("C29e and truncated at the endorsement clause it is TRUNCATED, not UNCALIBRATED",
      gp.classify(_qti_cut, "BSD")["verdict"], "GRANT-TRUNCATED")
check("C29f on exactly that clause", gp.classify(_qti_cut, "BSD")["missing"],
      ["no-endorsement"])

check("C29c two different declarations REFUSE rather than taking the first",
      gp.resolve_bsd_variant("BSD 2-Clause License ... see also the 3-clause BSD license"),
      None)

# C30 — 🔴 THE SCOPE BOUNDARY, STATED AS A CONTROL.  `open-webui/open-webui` is stock
# BSD-3 PLUS a branding restriction and a Contributor Licence Agreement, and it grades
# GRANT-PRESENT because every clause really is present.  This instrument answers "is the
# grant HERE", not "is the grant UNMODIFIED" — that is the `Gap 438-A` / `Gap 439-A`
# addition axis, and `agents/top.md` already carries the warning by hand.
check("C30 BSD-3 plus a branding clause and a CLA is still GRANT-PRESENT",
      verdict("bsd3-plus-branding-openwebui-2819.LICENSE", "BSD"), "GRANT-PRESENT")
check("C30b and the addition is real, so the row's hand-written warning stands",
      "CONTRIBUTOR_LICENSE_AGREEMENT"
      in (FX / "bsd3-plus-branding-openwebui-2819.LICENSE").read_text(), True)

# C31 — the BSD disclaimer clauses carry NO quote character, so `C6`'s defect class
# (a complete grant condemned by punctuation) cannot recur in this family.
check("C31 no BSD clause pattern contains a quote character",
      [lbl for key in ("BSD-2", "BSD-3")
       for lbl, rx in gp.CLAUSE_PROFILE[key] if '"' in rx or "'" in rx], [])

# C32 — the families that existed before `p441` are untouched.
check("C32 MIT is not variant-resolved", gp.profile_key("x", "MIT"), "MIT")
check("C32b GPL still goes through the VERSION resolver",
      gp.profile_key("version 3 of the GNU General Public License", "GPL"), "GPL-3.0")
check("C32c and BSD is the only variant family",
      sorted(gp.VARIANT_FAMILIES), ["BSD"])

# C33 — 🔵 BSD-0 and BSD-4 are RECOGNISED and UNPROFILED, on purpose (`Gap 441-B`): there
# are zero payloads of either on this tree, so a profile would be written from reputation
# instead of measurement.  Recognising them is what keeps them from being graded against a
# neighbour's clauses.
check("C33 a declared BSD Zero Clause resolves to its own key",
      gp.resolve_bsd_variant("BSD Zero Clause License"), "BSD-0")
check("C33b which has no profile, so it declines",
      gp.classify("BSD Zero Clause License\nPermission to use ...", "BSD")["verdict"],
      "GRANT-UNCALIBRATED")
check("C33c same for BSD-4, whose advertising clause nothing here models",
      gp.resolve_bsd_variant("BSD 4-Clause License"), "BSD-4")
check("C33d and neither is approximated by BSD-2",
      [k for k in gp.CLAUSE_PROFILE if k in ("BSD-0", "BSD-4")], [])

# C34 — `P541`: the new input path refuses rather than reporting a clean nothing.
check("C34 --family with no payload still refuses",
      gp.main(["--family", "BSD"]), 2)
check("C34b --family with no VALUE refuses", gp.main(["--family"]), 2)

if fails:
    print("🔴 p439-grant-presence: %d of %d controls FAILED" % (len(fails), n))
    for f in fails:
        print("   " + f)
    sys.exit(1)
print("🟢 p439-grant-presence: %d/%d controls pass" % (n, n))
