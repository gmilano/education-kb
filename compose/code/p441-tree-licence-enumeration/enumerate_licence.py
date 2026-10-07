#!/usr/bin/env python3
"""p441 -- stop enumerating FILENAMES and enumerate the TREE.

This KB has now found the same defect four times, and the fourth time it found it in
an instrument built one pass after it wrote the warning down:

    pass 52  `@learninglocker/xapi-agents` ships `package/license` -- lowercase,
             extensionless.  The pass-51 tarball anchor was case-sensitive.
    pass 52  trend 252: "a list of filenames is a cultural assumption."
    earlier  `openedx/XBlock` ships `LICENSE.TXT`.  `repos/foundations.md` recorded it
             AND the lesson: *"Found at LICENSE.TXT -- uppercase extension.  A nine-name
             lowercase probe reports this [as ungranted]... two characters away from a
             name the probe already tried."*
    pass 26  `p436`'s 14-name list still does not contain `LICENSE.TXT`, so XBlock was
             published UNLICENSED again -- and `p440`'s own 41-name WIDENING missed it a
             third time, because widening a list cannot fix a list.

`Opetushallitus/aoe` is the same hole by a different axis: its EUPL-1.2 grant is at
`aoe-web-frontend/LICENSE`, 303 B, in a SUBDIRECTORY, and every probe here is rooted.

**P441: a filename list can only FIND a licence. To sustain its ABSENCE you must
enumerate the tree.** This is `P275` -- which this KB already proved and applied to
directory listings -- carried to the licence layer, where it had not been applied.

The channel is the one P275 established, and it needs no API (`api.github.com` is 403
here):

    git clone --filter=blob:none --no-checkout --depth 1   # commit + trees, no blobs
    git ls-tree -r --name-only HEAD                        # the COMPLETE tree

Matching is a PATTERN over every path at any depth, case-insensitive, so `LICENSE.TXT`,
`licence`, `aoe-web-frontend/LICENSE` and `COPYING.LESSER` are all one rule instead of
41 names.

## Stage 2 exists because stage 1 overshoots, exactly as symmetrically as the list
## undershoots

A pattern over paths is a FINDING channel and its positives are a reading list.  Run
over the 87 it returned 14, and the first build published all 14.  Read, six of them
are not the repository's grant at all:

    learningequality/kolibri-design-system   lib/KIcon/.../material-icons/copyright/
                                             baseline.vue -- an ICON component whose
                                             name is the word
    Kennisnet/edurep-xslt                    copyrightandotherrestrictions.xsl -- an
                                             XSLT transform for a metadata field
    mendezjerick/ReaDirect-V2                .corepack/v1/pnpm/10.34.5/LICENSE -- a
                                             vendored package manager's grant
    dini-ag-kim/school-curriculum-pg         src/ontology/utils/owl2shacl/LICENSE -- a
                                             vendored tool's grant
    OS4ED/openSIS-Classic and -Responsive    ckeditor, codemirror and htmlpurifier
    european-commission-empl/...             "licence-EUPL 1.2-brightgreen.svg" -- a
                                             README BADGE IMAGE, which asserts a
                                             licence and is not one

So stage 2 READS each candidate blob and classifies it with the same `family_of` that
`p436` uses on the root probe.  A path is a grant only when its payload is a licence
TEXT; a path whose payload classifies UNKNOWN is a name that merely contains the word.
This is the `P342` rule -- *an assertion of a licence is not a grant* -- applied to a
path instead of a README badge, and the Commission's `.svg` is the cleanest example of
the badge class this KB has measured.

Excluded before any fetch, and each exclusion is a rule this KB already established:
    node_modules/, vendor/, third_party/, .corepack/   somebody else's grant
                                                       (pass 52, trend 259)
    LICENSES/, licenses.json, *.spdx       an INVENTORY is not a grant text (pass 52)
    *.py *.js *.vue *.xsl *.svg *.mustache a SOURCE, TEMPLATE or IMAGE file whose name
                                           contains the word is not a grant

Verdicts:
    OWN-GRANT-AT-ROOT     a confirmed licence TEXT at the repository root
    OWN-GRANT-IN-SUBTREE  a confirmed licence text in one of the project's OWN
                          component directories (`aoe-web-backend/`, `debian/`,
                          `LICENSE/`)
    BUNDLED-GRANT-ONLY    every confirmed grant belongs to a VENDORED dependency, so
                          the project's own grant is still absent
    ABSENCE-ENUMERATED    no path in the complete tree is a licence text
    UNRESOLVABLE          the repository does not resolve over `git`

TSV: slug, verdict, n_paths, confirmed_paths, families, rejected_paths,
     names_multiple   (a `?` on a family means the payload named more than one)

## Declared reading limits

- 🔴 **`docs/LICENSE.rtf` (`OS4ED/openSIS-*`) is RTF and is NOT read here.** `family_of`
  takes plain text, so an RTF grant classifies UNKNOWN and lands in `rejected_paths`.
  That is a LIMIT of this instrument, not an absence, and both openSIS rows are
  published `BUNDLED-GRANT-ONLY` with that limit attached rather than as unlicensed.
- ⚠️ A confirmed path proves a licence TEXT is present; it does not prove the project
  INTENDED it to govern the whole repository. `veraPDF`'s `LICENSE-HEADERS.md`
  classifies GPL and is a header-style guide, not the grant -- harmless there because
  `LICENSE.GPL` and `LICENSE.MPL` sit beside it, and recorded because the next tree may
  not be so forgiving.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "../p436-fork-hypothesis")
from sweep_payload import family_of  # noqa: E402

LICENCE_RE = re.compile(r"(?:^|/)(?:un)?licen[cs]e|(?:^|/)copying|(?:^|/)copyright",
                        re.I)
# An inventory, a manifest or a source file is not a grant.
EXCLUDE_DIR_RE = re.compile(
    r"(?:^|/)(?:node_modules|vendor|third_party|thirdparty|\.git|\.corepack"
    r"|bower_components|site-packages|dist-packages)/", re.I)
# Source, template and IMAGE extensions.  `.vue` and `.xsl` are here because the
# first run matched an icon component and an XSLT transform; `.svg` and `.png` because
# it matched the European Commission's EUPL README BADGE, which asserts a licence
# without being one.
SOURCE_EXT = (".py", ".js", ".ts", ".tsx", ".jsx", ".vue", ".svelte", ".go", ".java",
              ".rb", ".php", ".c", ".h", ".cpp", ".cs", ".rs", ".sh", ".bat", ".ps1",
              ".yml", ".yaml", ".json", ".xml", ".xsl", ".xslt", ".toml", ".cfg",
              ".ini", ".lock", ".sql", ".spdx", ".csv", ".tsv", ".po", ".pot",
              ".snap", ".svg", ".png", ".jpg", ".gif", ".ico", ".mustache", ".hbs",
              ".ejs", ".twig", ".scss", ".css", ".less", ".sol", ".h5p",
              # `.html` is here because `aoe-web-frontend/src/app/views/
              # educational-resource-form/tabs/license/license.component.html` is an
              # Angular template offering the author a CC licence to PICK for an OER,
              # and it classified CC-BY -- a licence-chooser UI read as the
              # repository's own grant.
              ".html", ".htm")
# An inventory is PLURAL and is a DATA format.  The first build wrote `licenses?\.`
# with `txt|md` in the alternation and `re.I`, which matched `LICENSE.TXT` -- the single
# most common licence filename there is, and the exact name this instrument was built
# to stop missing.  Caught by the control, not by the sweep: 87 trees would have come
# back one grant short and the TSV would have looked clean.
INVENTORY_RE = re.compile(r"(?:^|/)licenses\.(?:json|xml|csv|ya?ml|toml)$"
                          r"|(?:^|/)LICENSES/", re.I)
# Container segments: a grant under one of these is a DEPENDENCY's, not the project's.
# Derived from the rows that forced the distinction, not guessed.
BUNDLED_SEG_RE = re.compile(
    r"(?:^|/)(?:assets|libraries|library|plugins|plugin|lib|libs|utils|samples"
    r"|examples|fonts|specimens|external|externals|deps|packages|bundled)/", re.I)

# A segment denylist alone is a treadmill: `foradian/fedena` carries fckeditor's and
# tinymce's grants at `public/javascripts/fckeditor/license.txt`, which names no segment
# on the list above, and `dini-ag-kim/school-curriculum-pg` carries owl2shacl's at
# `src/ontology/utils/owl2shacl/LICENSE`.  DEPTH is the rule that needs no vendor names:
# a project states its own licence at the root or one directory down (`debian/`,
# `docs/`, `LICENSE/`, `aoe-web-backend/`); nothing states its own licence four levels
# into a static-assets tree.
OWN_MAX_DEPTH = 2


def is_own_path(path):
    """Is this confirmed grant the PROJECT's, rather than a vendored dependency's?"""
    return path.count("/") < OWN_MAX_DEPTH and not BUNDLED_SEG_RE.search(path)


def is_grant_path(path):
    if EXCLUDE_DIR_RE.search(path):
        return False
    if INVENTORY_RE.search(path):
        return False
    if path.lower().endswith(SOURCE_EXT):
        return False
    return bool(LICENCE_RE.search(path))


def tree_paths(slug, timeout=180):
    """Every path at HEAD, or None if the repository does not resolve."""
    tmp = tempfile.mkdtemp(prefix="p441-")
    try:
        r = subprocess.run(
            ["git", "clone", "--filter=blob:none", "--no-checkout", "--depth", "1",
             "--quiet", f"https://github.com/{slug}", tmp],
            capture_output=True, timeout=timeout)
        if r.returncode != 0:
            return None
        r = subprocess.run(["git", "-C", tmp, "ls-tree", "-r", "--name-only", "HEAD"],
                           capture_output=True, timeout=timeout)
        if r.returncode != 0:
            return None
        return r.stdout.decode("utf-8", "replace").splitlines()
    except subprocess.TimeoutExpired:
        return None
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# Every family mark a payload can carry, used to COUNT them rather than to pick one.
_MARKS = [
    ("AGPL", r"gnu affero general public licen[cs]e"),
    ("LGPL", r"gnu lesser general public licen[cs]e"),
    ("GPL", r"gnu general public licen[cs]e"),
    ("MPL", r"mozilla public licen[cs]e"),
    ("EPL", r"eclipse public licen[cs]e"),
    ("EUPL", r"european union public licen[cs]e|under the eupl\b"),
    ("Apache", r"apache licen[cs]e"),
    ("MIT", r"\bmit licen[cs]e|permission is hereby granted, free of charge"),
    ("BSD", r"redistribution and use in source and binary forms"),
    ("CC", r"creative commons"),
]


def family_marks(text):
    """Which licence families does this payload NAME, regardless of which it GRANTS?

    `family_of` picks ONE family by probing in a fixed order, and this pass had to
    reorder it twice because the families that NAME other families defeat that design:

        MPL-2.0 s.1.12   defines "Secondary License" by naming GPL-2.0, LGPL-2.1 and
                         AGPL-3.0, so every MPL payload carries three GNU marks.
        EUPL-1.2 App.    lists GPL-2.0, AGPL-3.0, LGPL-2.1, MPL-2.0 and EPL-1.0.
        GPL + exception  `nvaccess/nvda`'s `copying.txt` opens "NVDA is available under
                         the GNU General Public License version 2 or later, with two
                         special exceptions" and the exceptions name the LGPL --
                         so `family_of` returns LGPL for a GPL-2.0 project.

    Reordering fixed the first two because there the granting licence is identifiable.
    It CANNOT fix the third: deciding which named licence is GRANTED and which is merely
    REFERENCED is a reading task, and a substring classifier structurally cannot do it.
    So this function does not guess. It counts, and a count above one makes the row a
    reading list instead of a verdict -- which is the same move `p436` made for
    `UPSTREAM` and `p184` for `HOLDER-UNRELATED`.
    """
    # `P447` (pass 28): FLATTEN WHITESPACE BEFORE MATCHING.  Every pattern above is
    # written with literal spaces, and a licence payload wraps its prose at ~72
    # columns, so a family NAME that straddles a line break does not match.  Measured
    # on `dequelabs/axe-core`'s real MPL-2.0 payload:
    #
    #     line 74   "...the GNU General Public License, Version 2.0, the GNU Lesser"
    #     line 75   "      General Public License, Version 2.1, the GNU Affero General
    #     line 76    Public License, Version 3.0..."
    #
    # so LGPL and AGPL were both invisible and this function returned {MPL, GPL} where
    # the truth is {MPL, GPL, LGPL, AGPL}.  It UNDERCOUNTS, which matters because
    # counting is this function's entire purpose: pass 26 built it to replace a verdict
    # with a count, and then measured the count with literal spaces.
    #
    # Pass 26 diagnosed exactly this mechanism one function away -- *"which of the three
    # fired was decided by LINE WRAPPING"* -- and fixed `family_of` by REORDERING, which
    # cures the symptom there (the granting family's own title happens not to wrap) and
    # does nothing here.  The defect outlived its own diagnosis by one pass.
    t = re.sub(r"\s+", " ", text[:6000].lower())
    return sorted({name for name, pat in _MARKS if re.search(pat, t)})


def read_blob(slug, path, timeout=25):
    url = "https://raw.githubusercontent.com/%s/HEAD/%s" % (
        slug, urllib.parse.quote(path))
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p441"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return ""


def one(slug):
    paths = tree_paths(slug)
    if paths is None:
        return (slug, "UNRESOLVABLE", "0", "-", "-", "-", "-")
    candidates = [p for p in paths if is_grant_path(p)]
    if not candidates:
        # The ONLY verdict in this table that a filename list could not already reach,
        # and the only one P441 exists to make sayable.
        return (slug, "ABSENCE-ENUMERATED", str(len(paths)), "-", "-", "-", "-")
    confirmed, families, rejected, ambiguous = [], [], [], []
    for cand in sorted(candidates)[:40]:
        body = read_blob(slug, cand)
        fam = family_of(body)
        if fam == "UNKNOWN":
            rejected.append(cand)
            continue
        confirmed.append(cand)
        marks = family_marks(body)
        if len(marks) > 1:
            # Named more than one family.  `family_of`'s single answer is a reading
            # list here, not a verdict, and the row says so instead of hiding it.
            families.append("%s?" % fam)
            ambiguous.append("%s=%s" % (cand, "+".join(marks)))
        else:
            families.append(fam)
    if not confirmed:
        # Every candidate was a name containing the word, not a grant.  The absence
        # still holds, and the rejected list is why it is stronger than stage 1's.
        return (slug, "ABSENCE-ENUMERATED", str(len(paths)), "-", "-",
                ";".join(rejected[:6]), "-")
    own = [c for c in confirmed if is_own_path(c)]
    if not own:
        # Every confirmed grant belongs to a BUNDLED dependency.  `OS4ED/openSIS-*`
        # carry ckeditor's, codemirror's and htmlpurifier's; `dini-ag-kim/
        # school-curriculum-pg` carries `owl2shacl`'s.  The PROJECT's own grant is
        # still absent, and reporting these as the project's licence is the error
        # pass 52's trend 259 named (144 foreign licence files in one tarball).
        return (slug, "BUNDLED-GRANT-ONLY", str(len(paths)), ";".join(confirmed[:6]),
                ";".join(sorted(set(families))), ";".join(rejected[:4]) or "-",
                ";".join(ambiguous[:3]) or "-")
    own_fams = sorted({f for c, f in zip(confirmed, families)
                       if is_own_path(c)})
    rooted = [c for c in own if "/" not in c]
    verdict = "OWN-GRANT-AT-ROOT" if rooted else "OWN-GRANT-IN-SUBTREE"
    return (slug, verdict, str(len(paths)), ";".join(own[:6]),
            ";".join(own_fams), ";".join(rejected[:4]) or "-",
            ";".join(ambiguous[:3]) or "-")


def main():
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    if not slugs:
        sys.stderr.write("p441: empty denominator -- a path fault, not a clean tree "
                         "(P355)\n")
        sys.exit(2)
    print("slug\tverdict\tn_paths\tconfirmed_paths\tfamilies\trejected_paths\tnames_multiple")
    with ThreadPoolExecutor(max_workers=6) as ex:
        for row in ex.map(one, slugs):
            print("\t".join(row))


if __name__ == "__main__":
    main()
