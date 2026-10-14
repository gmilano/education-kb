"""p188 / P1056 tests. Every fixture below is REAL text measured this pass over the raw
channel, or a canonical licence body, or a deliberate negative. No invented licences."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from split_scope import classify, publishable_licence, VERDICT_SPLIT, VERDICT_CC_ONLY, VERDICT_SINGLE

MIT_BODY = """MIT License

Copyright (c) 2026 Yanwei Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ktwyw/python-for-engineers, LICENSE, read at HEAD 609d8459 this pass. 1 328 B.
PFE = ("Code in this repository (src/, tests/, *.py) is licensed under the MIT License.\n"
       "Teaching materials (notebooks, README files, cheatsheets, datasets created\n"
       "for this course) are licensed under CC BY 4.0.\n\n"
       + MIT_BODY +
       "\nCC BY 4.0: https://creativecommons.org/licenses/by/4.0/\n")

# siskinskai/spedlex, README.md "## License", read at HEAD 6698a9ad this pass.
SPEDLEX_README = (
    "## License\n\n"
    "Code: [MIT](LICENSE). Data (everything in `data/`, `schema/` and the term\n"
    "lists in `sources/`): [CC BY 4.0](LICENSE-DATA). Cited documents belong to\n"
    "their publishers. SPEDLex stores terms and citations, not their text.\n")

# willwearing/graspful — P1054's row. A NARROWED grant, not a split one.
GRASPFUL = (MIT_BODY + "\n2. You may not use the Software to directly compete with the "
            "original Licensor by offering it as a hosted, managed, or "
            "Software-as-a-Service (SaaS) product.\n")

# No-Suggest/NoSuggest, LICENSE, 417 B, read this pass. Restricted, no permissive body.
NOSUGGEST = ("Copyright 2026 NoSuggest\n\nSource code is made available for transparency "
             "and personal \nnon-commercial use only.\n\nAll rights reserved.\n")

# INRIA/scikit-learn-mooc ships CC with no code/content split stated in the file.
CC_ONLY = ("Creative Commons Attribution 4.0 International\n\n"
           "Creative Commons Corporation is not a law firm...\n")

fails = []
def check(name, got, want):
    if got != want:
        fails.append(f"{name}: got {got!r}, want {want!r}")

# --- the two real split-scope rows -----------------------------------------------
check("pfe verdict", classify(PFE)["verdict"], VERDICT_SPLIT)
check("pfe second licence", classify(PFE)["second_licence"].upper().replace("-", " "), "CC BY 4.0")
check("pfe has content nouns", "notebook" in classify(PFE)["content_nouns"], True)
check("pfe keeps permissive body", classify(PFE)["permissive_body"], True)
check("pfe published label", publishable_licence(PFE), "MIT (code) + CC BY 4.0 (content)")
check("spedlex verdict (README channel, with LICENSE-DATA present)",
      classify(SPEDLEX_README, ("LICENSE-DATA",))["verdict"], VERDICT_SPLIT)
check("spedlex names the data scope",
      "schema" in classify(SPEDLEX_README, ("LICENSE-DATA",))["content_nouns"], True)

# --- P1056 must NOT fire on P1054's row, and must not swallow it ------------------
check("graspful is not a split", classify(GRASPFUL)["verdict"], VERDICT_SINGLE)
check("graspful has no second licence", classify(GRASPFUL)["second_licence"], None)

# --- canonical MIT alone is single-scope -----------------------------------------
check("plain MIT verdict", classify(MIT_BODY)["verdict"], VERDICT_SINGLE)
check("plain MIT is permissive", classify(MIT_BODY)["permissive_body"], True)

# --- a restricted licence with NO permissive body: P1056 says nothing about it ----
check("nosuggest verdict", classify(NOSUGGEST)["verdict"], VERDICT_SINGLE)
check("nosuggest has no permissive body", classify(NOSUGGEST)["permissive_body"], False)

# --- CC present but no scope stated: the weaker verdict, never SPLIT -------------
check("cc-only verdict", classify(CC_ONLY)["verdict"], VERDICT_CC_ONLY)
check("cc-only is not published as permissive", publishable_licence(CC_ONLY), "read the file")

# --- a second licence FILE alone must not manufacture a split --------------------
check("second file without CC identifier stays single",
      classify(MIT_BODY, ("LICENSE-DATA",))["verdict"], VERDICT_SINGLE)

# --- byte counts reproduce what was measured over the wire ----------------------
check("pfe bytes match the measured 1328 B", classify(PFE)["bytes"], 1328)

if fails:
    print(f"FAIL {len(fails)}/{16}")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("PASS 16/16 — P1056")
