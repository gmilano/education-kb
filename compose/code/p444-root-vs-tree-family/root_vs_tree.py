#!/usr/bin/env python3
"""p444 — pass 26's action A: does the root licence file agree with the rest of the tree?

Pass 26's pre-registered action A, verbatim:

    Run `p441`'s tree enumeration over the 412 LICENSED rows, not the 87 -- the slugs
    where a root filename DID answer -- and compare the family read from the root file
    against every other licence text in the tree.
    PREDICTION: expect MORE THAN FIVE repositories to carry a second, different grant
    somewhere below the root that the rooted probe never saw, concentrated in the
    dual-licensed and monorepo tiers.  The interesting class is the inverse of this
    pass's: a repository whose root `LICENSE` is permissive and which ships a COPYLEFT
    text deeper in.

## Why the LICENSED side is the harder half

`p441` ran the enumeration over the 87 rows where the root probe found NOTHING, so
anything it found was new by construction.  Here the root probe already answered, and
the question is whether that answer is COMPLETE.  A root `LICENSE` is one file; a
repository is a tree; and nothing makes the two agree.

Every stage is imported from `p441` and `p436` rather than rewritten -- rule 1 of
**P126** -- so the family vocabulary, the bundled-path exclusions and the
multi-family mark counter are the same ones those passes published.  The only new
thing here is the COMPARISON.

Verdicts:
    ROOT-ONLY        the root file is the only licence text in the tree
    TREE-AGREES      other licence texts exist and every own one is the root's family
    TREE-ADDS        other OWN licence texts exist naming a family the root does not
                     <- the class the prediction is about
    BUNDLED-ONLY-EXTRA  the extra texts are all vendored dependencies' -- not a finding
                     about this project, and the single commonest shape
    ROOT-UNREADABLE  the root payload itself does not classify (RTF, images)

`escalation` marks the sub-case the prediction called interesting: a PERMISSIVE root
with a COPYLEFT text deeper in.  That direction is the one that reaches a client
contract, because the permissive root is what a proposal quotes.

TSV: slug, root_path, root_family, verdict, escalation, own_extra_families,
     own_extra_paths, bundled_extra, names_multiple, p436_skew
"""
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p441-tree-licence-enumeration"))
sys.path.insert(0, os.path.join(HERE, "..", "p436-fork-hypothesis"))
import enumerate_licence as E  # noqa: E402  -- tree_paths/read_blob/is_own_path/family_marks
from sweep_payload import family_of  # noqa: E402  -- the published family vocabulary

# A file NAMED for third-party licences is a NOTICE about other people's grants, not
# a second grant by this project.  P444's third defect: `dequelabs/axe-core`'s
# `LICENSE-3RD-PARTY.txt` sits at the ROOT, so `is_own_path` accepts it, and its body
# is a real MIT text -- it reads "Applies to: colorjs.io; core-js-pure;
# css-selector-parser".  That is `p441`'s BUNDLED class wearing a root path, and
# counting it reported axe-core as adding MIT to its own MPL-2.0.  One such path in
# 412, and it was in the escalation class, which is where a false positive costs most.
THIRD_PARTY_RE = __import__("re").compile(
    r'3rd[-_. ]?party|third[-_. ]?party|3rdparty', re.I)

COPYLEFT = {"GPL", "GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL", "LGPL-2.1", "LGPL-3.0",
            "EUPL-1.2", "MPL-2.0", "EPL-2.0", "CC-BY-SA", "OSL-3.0", "CPAL-1.0"}
PERMISSIVE = {"MIT", "Apache-2.0", "BSD", "BSD-2-Clause", "BSD-3-Clause", "ISC",
              "CC0-1.0", "Unlicense", "ECL-2.0", "NCSA", "Zlib", "OFL-1.1"}
# NOTE: bare `CC-BY` is deliberately in NEITHER set.  `p445` measured that `family_of`
# returns plain `CC-BY` for five CC-BY-**NC** payloads on this shelf, including
# `facebookresearch/seamless_communication`, which `agents/top.md` correctly calls a
# "hard reject for anything billable".  A `CC-BY` from this classifier therefore does
# not establish that commercial use is permitted, so it cannot be scored as
# permissive; rows carrying it escalate to SAME-CLASS and the commercial question is
# answered by `p445` instead.


def one(job):
    slug, root_path, inherited = job
    # P444's own first defect: the root family was taken from `p436`'s published TSV,
    # which was measured in pass 25 -- BEFORE pass 26 reordered `family_of` for the
    # licences that name other licences.  `dequelabs/axe-core` is MPL-2.0 and that
    # TSV records `GPL`, because MPL s.1.12 names GPL-2.0, LGPL-2.1 and AGPL-3.0.
    # Comparing a tree classified TODAY against a root classified LAST PASS reports
    # disagreements that are only version skew in the classifier.  So the root payload
    # is RE-READ and RE-CLASSIFIED here with the same `family_of` the tree side uses;
    # `inherited` is carried only to report where the two differ, which is itself a
    # measurement of how much pass 26's reordering changed.
    root_body = E.read_blob(slug, root_path)
    root_family = family_of(root_body) if root_body else "UNREADABLE"
    skew = "-" if root_family == inherited else "%s->%s" % (inherited, root_family)
    paths = E.tree_paths(slug)
    if paths is None:
        return (slug, root_path, root_family, "UNRESOLVABLE", "-", "-", "-", "-", "-", skew)
    cands = [p for p in paths if E.is_grant_path(p)]
    # The root file p436 read is not an "extra"; compare against everything else.
    extras = [p for p in sorted(cands) if p != root_path][:40]
    if not extras:
        return (slug, root_path, root_family, "ROOT-ONLY", "-", "-", "-", "-", "-", skew)
    own_f, own_p, bundled, multi = set(), [], 0, []
    for c in extras:
        body = E.read_blob(slug, c)
        fam = family_of(body)
        if fam == "UNKNOWN":
            # A path whose payload is not a licence text: a name containing the word.
            # P441's stage-2 rule, inherited rather than re-decided here.
            continue
        if not E.is_own_path(c) or THIRD_PARTY_RE.search(c):
            bundled += 1
            continue
        marks = E.family_marks(body)
        if len(marks) > 1:
            multi.append("%s=%s" % (c, "+".join(marks)))
        own_f.add(fam)
        own_p.append(c)
    new = sorted(own_f - {root_family})
    if not own_p:
        v = "BUNDLED-ONLY-EXTRA" if bundled else "ROOT-ONLY"
    elif new:
        v = "TREE-ADDS"
    else:
        v = "TREE-AGREES"
    esc = "-"
    if new:
        if root_family in PERMISSIVE and any(f in COPYLEFT for f in new):
            # The direction the prediction named: a proposal quotes the permissive
            # root and the obligation is deeper in.
            esc = "PERMISSIVE-ROOT-COPYLEFT-TREE"
        elif root_family in COPYLEFT and any(f in PERMISSIVE for f in new):
            esc = "COPYLEFT-ROOT-PERMISSIVE-TREE"
        else:
            esc = "SAME-CLASS"
    return (slug, root_path, root_family, v, esc, "+".join(new) or "-",
            ";".join(own_p[:5]) or "-", str(bundled), ";".join(multi[:3]) or "-", skew)


def main():
    jobs = []
    with open(sys.argv[1]) as f:
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) >= 5 and c[1] == "LICENSED":
                jobs.append((c[0], c[2], c[4]))
    if not jobs:
        sys.stderr.write("p444: empty denominator -- a path fault, not a clean tree "
                         "(P355)\n")
        return 2
    print("\t".join(["slug", "root_path", "root_family", "verdict", "escalation",
                     "own_extra_families", "own_extra_paths", "bundled_extra",
                     "names_multiple", "p436_skew"]))
    with ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(one, jobs):
            print("\t".join(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
