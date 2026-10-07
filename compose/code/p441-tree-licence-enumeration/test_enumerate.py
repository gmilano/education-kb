#!/usr/bin/env python3
"""Offline controls for p441. No network: the path classifier and the mark counter are
pure functions, and every case below is a real path or payload measured 2026-10-07.

Rule 2 of P126: each positive is paired with the false positive that would make the
output unreadable. Six of these controls exist because the first build published the
row they forbid.

Run: python3 test_enumerate.py
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p436-fork-hypothesis"))
import enumerate_licence as e  # noqa: E402

FAIL = []


def check(label, got, want):
    if got != want:
        FAIL.append("%s: got %r want %r" % (label, got, want))


# --- the positives: the four axes a filename list structurally cannot cover ---
check("LICENSE.TXT -- uppercase extension; this KB wrote the warning down and p436's "
      "14-name list still misses it", e.is_grant_path("LICENSE.TXT"), True)
check("copying.txt -- lowercase COPYING, which p436 has only in uppercase",
      e.is_grant_path("copying.txt"), True)
check("License -- capital L only, a third case p436 does not carry",
      e.is_grant_path("License"), True)
check("aoe-web-frontend/LICENSE -- DEPTH, where every rooted probe is blind",
      e.is_grant_path("aoe-web-frontend/LICENSE"), True)
check("LICENSE.GPL -- the family-suffixed form a DUAL-licensed project must use",
      e.is_grant_path("LICENSE.GPL"), True)
check("LICENSE/LICENSE.code -- a licence DIRECTORY holding several grants",
      e.is_grant_path("LICENSE/LICENSE.code"), True)
check("debian/copyright -- the grant of a packaging repository",
      e.is_grant_path("debian/copyright"), True)
check("COPYING.LESSER -- GNU's LGPL split", e.is_grant_path("COPYING.LESSER"), True)

# --- the negatives, each one a row the first build actually published ---------
check("an ICON component whose NAME is the word is not a grant",
      e.is_grant_path("lib/KIcon/precompiled-icons/material-icons/copyright/"
                      "baseline.vue"), False)
check("an XSLT transform for a metadata field is not a grant",
      e.is_grant_path("copyrightandotherrestrictions.xsl"), False)
check("a README BADGE IMAGE asserting EUPL-1.2 is an assertion, not a grant (P342)",
      e.is_grant_path("edci-issuer/licence-EUPL 1.2-brightgreen.svg"), False)
check("a codegen TEMPLATE is not a grant",
      e.is_grant_path("src/main/resources/typescript-codegen/licenseInfo.mustache"),
      False)
check("a vendored package manager's grant is not this project's",
      e.is_grant_path(".corepack/v1/pnpm/10.34.5/LICENSE"), False)
check("node_modules is somebody else's grant, 144 of them in one measured tarball",
      e.is_grant_path("node_modules/left-pad/LICENSE"), False)
check("a licence INVENTORY is not a licence text, carrying pass 52's rule forward",
      e.is_grant_path("licenses.json"), False)
# The pair that forced the inventory rule to be PLURAL-only.  The first build wrote the
# alternation with `txt|md` under `re.I`, and `LICENSE.TXT` -- the very name this
# instrument exists to catch -- was excluded as an inventory.
check("and the SINGULAR licence text in the same format is a grant",
      e.is_grant_path("LICENSE.txt"), True)
check("a plural inventory in a data format is still excluded",
      e.is_grant_path("licenses.yaml"), False)
check("and neither is a LICENSES/ directory of them",
      e.is_grant_path("LICENSES/MIT.txt"), False)
check("a SOURCE file named for the concept is code, e.g. this KB's own helper",
      e.is_grant_path("compose/code/lib/license_family.sh"), False)
check("a README is not a grant however much it talks about one",
      e.is_grant_path("README.md"), False)

# --- the bundled/own axis ----------------------------------------------------
check("a grant under libraries/ belongs to the library",
      bool(e.BUNDLED_SEG_RE.search("libraries/htmlpurifier/LICENSE")), True)
check("a grant under assets/.../plugins/ belongs to the plugin",
      bool(e.BUNDLED_SEG_RE.search(
          "assets/js/plugins/editors/ckeditor/plugins/pbckcode/LICENSE")), True)
check("a bundled FONT's COPYING is the font's",
      bool(e.BUNDLED_SEG_RE.search("source/fonts/freefont-20100919-ttf/COPYING")),
      True)
# The negatives that stop the bundled rule eating the project's OWN subtree grants.
check("aoe-web-backend/ is the project's own component, not a vendor directory",
      bool(e.BUNDLED_SEG_RE.search("aoe-web-backend/LICENSE")), False)
check("debian/ is the project's own packaging directory",
      bool(e.BUNDLED_SEG_RE.search("debian/copyright")), False)
check("LICENSE/ is the project's own licence directory",
      bool(e.BUNDLED_SEG_RE.search("LICENSE/LICENSE.code")), False)
check("and a root grant is never bundled",
      bool(e.BUNDLED_SEG_RE.search("LICENSE.GPL")), False)

# DEPTH, the rule that needs no vendor names.  A segment denylist alone let two
# vendored editors through as the project's own grant.
check("a root grant is the project's", e.is_own_path("LICENSE.TXT"), True)
check("one directory down is still the project's -- debian/, docs/, LICENSE/",
      e.is_own_path("debian/copyright"), True)
check("and so is a monorepo component's", e.is_own_path("aoe-web-backend/LICENSE"),
      True)
check("fckeditor's grant three levels into a static-assets tree is NOT the project's",
      e.is_own_path("public/javascripts/fckeditor/license.txt"), False)
check("nor is tinymce's", e.is_own_path("public/javascripts/tiny_mce/license.txt"),
      False)
check("nor is a vendored ontology tool's four levels down",
      e.is_own_path("src/ontology/utils/owl2shacl/LICENSE"), False)
check("the segment rule still fires inside the depth limit",
      e.is_own_path("libraries/htmlpurifier"), False)

# --- the mark counter: why ORDERING fixed two axes and cannot fix the third ---
MPL_12 = ('Mozilla Public License Version 2.0\n1.12. "Secondary License" means either '
          'the GNU General Public License, Version 2.0, the GNU Lesser General Public '
          'License, Version 2.1, the GNU Affero General Public License, Version 3.0.')
check("an MPL payload NAMES four families, which is why a substring probe mis-picks",
      e.family_marks(MPL_12), ["AGPL", "GPL", "LGPL", "MPL"])
NVDA = ("# NVDA License\n\nNVDA is available under the GNU General Public License "
        "version 2 or later, with two special exceptions.\nOne exception permits "
        "linking with code under the GNU Lesser General Public License.\n")
check("NVDA's GPL-2.0-with-exceptions payload names GPL AND LGPL, so one answer "
      "cannot be a verdict", e.family_marks(NVDA), ["GPL", "LGPL"])
check("a plain MIT payload names exactly one family and needs no caveat",
      e.family_marks("MIT License\n\nPermission is hereby granted, free of charge"),
      ["MIT"])
check("a plain Apache-2.0 payload names exactly one",
      e.family_marks("                                 Apache License\n"
                     "                           Version 2.0, January 2004"),
      ["Apache"])

# --- scope: a zero denominator is a path fault, not a clean tree (P355) -------
with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
    empty = f.name
r = subprocess.run([sys.executable, "-I",
                    os.path.join(HERE, "enumerate_licence.py"), empty],
                   capture_output=True, cwd=HERE)
os.unlink(empty)
check("exits 2 on an empty denominator", r.returncode, 2)

TOTAL = 40
if FAIL:
    print("FAIL (%d of %d)" % (len(FAIL), TOTAL))
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("%d/%d assertions pass, no network" % (TOTAL, TOTAL))
