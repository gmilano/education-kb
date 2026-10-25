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
"""
import pathlib
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

if fails:
    print("🔴 p439-grant-presence: %d of %d controls FAILED" % (len(fails), n))
    for f in fails:
        print("   " + f)
    sys.exit(1)
print("🟢 p439-grant-presence: %d/%d controls pass" % (n, n))
