"""`ACTION ZZ-bo` (p362) — the DEPENDENCY CLOSURE of a shelved platform row.

🔴 The gap, in the words that opened it: *"every grant instrument here takes ONE
repository's bytes."*  `p362` proved that is not enough with
`QingdaoU/OnlineJudge` — **MIT** in the headline, **SATA** in the two components
that actually execute student code, **no grant at all** in the documented deploy
repository, and **3 of 5 components absent from this corpus**.  A studio that
read the headline cell and shipped the platform would have shipped SATA.

🟢 `ZZ-bo` prescribed the cheap first cut and this file is it: *read the README of
every platform row for named companion repositories, then resolve each
companion's default ref and read its payload.*  The scope was recorded as
**unmeasured** — "how many of this corpus's platform rows name companions is not
known" — so the denominator is this instrument's first output.

🔵 **What a COMPANION is here, stated because the word does the work.**  A
companion is another GitHub address named in the platform's own README.  That is
a *syntactic* relation and it deliberately over-collects: a README names
components, but it also names dependencies, credits, unrelated demos and the
badge services.  So every companion carries a `relation`:

  `SAME-OWNER`   — the platform's own organisation.  This is the COMPONENT
                   candidate: `QingdaoU/Judger` is reached this way, and so is
                   every defect `p362` found.
  `THIRD-PARTY`  — a different owner.  Kept and counted, never promoted to a
                   component on the strength of a link alone.

🔴 **The relation is evidence, not a verdict.**  Same-owner does not prove a
component and third-party does not refute one; `overhangio/tutor` is a real
component of Open edX under a different owner.  What this instrument settles is
the *population* a human then grades, and the grants inside it.

🔵 Addresses are folded and shape-filtered through `p351-address-shape`, imported
rather than reimplemented, for the reason `p352` states: two copies of a shape
filter is this base's "second channel disagreeing with itself" defect.
"""
import argparse
import importlib.util
import os
import re
import sys

# 🔴 A README's own repository is not its companion.  Neither is a link back to
# the same address under a different case, which is why the self-test folds.
GITHUB_ADDRESS = re.compile(
    r"github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", re.IGNORECASE)

# 🟡 Trailing syntax that a markdown link leaves glued to the name.  `.git` is a
# real clone suffix and must fold to the same address as the bare name.
NAME_TRAILERS = re.compile(r"(?:\.git|\.svg|\.png|\.jpg|\.json|\.md)$", re.IGNORECASE)

# 🔴 `p283`'s ladder audit graded this file `SINGLE-SPELLING` on the `readme` family the
# moment it entered `HOOK_GATES`, and it was RIGHT to — exactly as it was right about
# `p352`'s census instrument.  The first draft named `README` once, as an argparse flag,
# and had no ladder at all: it could only be handed a path by its shell driver.  🔴 That is
# a real defect and not a scoping quibble.  An instrument that cannot find a README itself
# cannot be run against a checkout, and a one-spelling anchor cannot prove an absence —
# hand it a project whose anchor is `Readme.md` and it reports no README where one is
# sitting.
#
# 🟢 So the ladder was CLOSED rather than the gate excepted (`p352`'s precedent): stem case
# AND extension case both vary, the walk is first-hit-wins, and `resolve_readme` returning
# None is a REAL absence rather than a spelling miss.  The non-markdown rungs are not
# decoration — Moodle, this base's largest platform row, ships `README.txt`, and a
# markdown-only ladder would have reported it as having no README at all.
README_LADDER = (
    "README.md", "README.MD", "Readme.md", "readme.md", "ReadMe.md",
    "README.rst", "README.RST", "readme.rst",
    "README.txt", "README.TXT", "readme.txt",
    "README.markdown", "readme.markdown",
    "README", "readme", "Readme",
)


def resolve_readme(directory):
    """The first README spelling that exists in `directory`; None is a real absence."""
    for rung in README_LADDER:
        candidate = os.path.join(directory, rung)
        if os.path.isfile(candidate):
            return candidate
    return None


def _address_shape():
    """p351's classifier, resolved from THIS file's location — never from the data."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "..", "p351-address-shape", "address_shape.py")
    spec = importlib.util.spec_from_file_location("p351_address_shape", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fold(owner, name):
    """One address, one spelling.  `ZZ-x`/`gate-fold-identity`'s rule applied at source."""
    name = NAME_TRAILERS.sub("", name)
    return "%s/%s" % (owner.lower(), name.lower())


def extract_companions(readme_text, self_slug, shape=None):
    """[(address, relation)] — every shape-valid GitHub address but the row itself.

    🔵 Sorted and de-duplicated, so a README that names one component in nine
    places contributes one companion.
    """
    shape = shape or _address_shape()
    self_folded = fold(*self_slug.split("/", 1))
    self_owner = self_folded.split("/", 1)[0]
    found = {}
    for owner, name in GITHUB_ADDRESS.findall(readme_text or ""):
        folded = fold(owner, name)
        if folded == self_folded:
            continue
        if shape.classify(folded) is not None:
            continue  # 🔴 p351 rejected it by SHAPE: a nav namespace or a placeholder
        relation = "SAME-OWNER" if folded.split("/", 1)[0] == self_owner else "THIRD-PARTY"
        found[folded] = relation
    return sorted(found.items())


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self", dest="self_slug", required=True)
    ap.add_argument("--readme", required=True,
                    help="the fetched README payload, or a DIRECTORY to resolve it in "
                         "over README_LADDER")
    args = ap.parse_args(argv)
    target = args.readme
    if os.path.isdir(target):
        target = resolve_readme(target)
        if target is None:
            print("🔴 no README at any of %d spellings in %s"
                  % (len(README_LADDER), args.readme), file=sys.stderr)
            return 2
    with open(target, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    for address, relation in extract_companions(text, args.self_slug):
        print("%s\t%s" % (address, relation))
    return 0


if __name__ == "__main__":
    sys.exit(main())
