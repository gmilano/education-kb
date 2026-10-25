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
"""
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import grant_presence as gp  # noqa: E402

FX = HERE / "fixtures"
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

if fails:
    print("🔴 p439-grant-presence: %d of %d controls FAILED" % (len(fails), n))
    for f in fails:
        print("   " + f)
    sys.exit(1)
print("🟢 p439-grant-presence: %d/%d controls pass" % (n, n))
