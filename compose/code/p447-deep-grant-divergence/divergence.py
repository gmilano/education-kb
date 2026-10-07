#!/usr/bin/env python3
"""p444 -- the rooted probe answered, and the answer is not the whole grant.

Pass 26 proved a FILENAME LIST cannot sustain a licence's ABSENCE (`P441`): nine of
the 87 rows it had published `UNLICENSED` carried a grant the rooted probe never
reached -- `openedx/XBlock` at `LICENSE.TXT`, `Opetushallitus/aoe` at
`aoe-web-frontend/LICENSE`.

This pass asks the symmetric question, and it is the one nobody asked in 26 passes:

    when the rooted probe DID answer, is its answer the repository's whole grant?

`p436` published 412 `LICENSED` rows. Every one of them is a single family read from a
single file at the root. A monorepo, a dual-licensed project or a re-licensed
component states a SECOND grant somewhere below that root, and a rooted probe is
structurally blind to it in exactly the way the filename list was blind to absence.

## Stage 0 exists because pass 26's own lesson demands it

Pass 26 closed with: *"before executing an action over a published set, re-measure the
set."* It learned that from being sent at "the 87" when the 87 was an overcount.

The pre-registration for this pass says "the 412 `LICENSED` rows". So the 412 is
re-measured here before anything is built on it -- and the re-measure is not a
reachability check, because presence is robust in the way absence is not. A grant that
was found stays found. What is NOT robust is the FAMILY attributed to it: pass 26
reordered `family_of` twice, for MPL/EPL and for EUPL, and never re-ran it over the
412. The symptom is visible without a single fetch:

    the published family distribution over the 412 contains ZERO MPL-2.0 rows
    and ZERO EUPL rows

for two of the most common licences in this corpus -- one of which eight Finnish
national education services on this very shelf are published under in prose.

So stage 0 re-reads all 412 root payloads and re-classifies them with the CORRECTED
`family_of`, and publishes the count of rows whose family MOVES. Those are published
verdicts in this KB that are wrong today.

## Stage 1 is pre-registered action B

`family_marks()` counts the families a payload NAMES, rather than picking one. Run over
all 412 it answers whether the coarse `p170` vocabulary is fit for this shelf: a payload
naming two or more families is a reading list, not a verdict.

## Stage 2 is pre-registered action A

Enumerate the COMPLETE tree of each of the 412 (the `P275` channel: blobless clone +
`git ls-tree -r`, because `api.github.com` is 403 here), confirm each candidate path by
READING it (`P342`: a path whose payload classifies UNKNOWN is a name containing the
word, not a grant), and compare every confirmed family against the family at the root.

Verdicts:
    ROOT-ONLY           the root file is the only confirmed grant in the tree
    CONCORDANT          deeper grants exist and every one is the root's family
    DIVERGENT-OWN       a deeper grant of a DIFFERENT family at own-project depth
                        (`P441`'s `is_own_path`: depth < 2, no bundled segment)
    DIVERGENT-BUNDLED   divergence exists but only in vendored/bundled paths, so it is
                        somebody else's grant and not this project's second licence
    UNRESOLVABLE        the repository does not resolve over `git`

and the pre-registered INTERESTING class is flagged separately on the own-divergent
rows: a PERMISSIVE root with a COPYLEFT grant deeper, which is the inverse of pass 26's
`Opetushallitus/aoe` and the direction that costs a Globant engagement money.

## Declared limits, inherited and new

- `docs/LICENSE.rtf` is RTF and classifies UNKNOWN (`P441`'s limit, unchanged).
- A confirmed deeper grant proves a licence TEXT is present at that path. It does NOT
  prove the project intends it to govern that subtree. The verdict is a READING LIST.
- `is_own_path`'s depth rule is a heuristic this KB adopted in pass 26, not a fact
  about projects. It is applied here unchanged precisely so this pass does not get to
  tune it toward its own prediction.
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

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p436-fork-hypothesis"))
sys.path.insert(0, os.path.join(HERE, "..", "p441-tree-licence-enumeration"))
from sweep_payload import family_of  # noqa: E402
from enumerate_licence import (  # noqa: E402
    family_marks, is_grant_path, is_own_path, tree_paths,
)

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"

# `P448` (pass 28): the WINDOW is the second undercount, and it is not a rounding error.
# `family_marks` reads `text[:6000]`.  The EUPL-1.2 Appendix -- the one section on this
# shelf that names five other families -- begins at character **5964** of the European
# Commission's own 13,699-character payload.  The window lands **36 characters** inside
# the heading and every name in the list falls outside it:
#
#     window 6000   ['EUPL']
#     full text     ['AGPL', 'CC', 'EPL', 'EUPL', 'GPL', 'LGPL', 'MPL']
#
# A truncation window is a sampling decision, and `p441` chose 6000 to bound the cost of
# a classifier that only had to pick ONE family -- where reading further cannot change
# the answer, because the granting family is named in the first lines.  Carried over to a
# function whose job is to COUNT, the same constant silently caps the count.
#
# Both windows are published here, because the pre-registered question ("the count of
# payloads naming more than one family") has two different true answers depending on a
# constant neither the action nor `p441` ever stated.
_MARKS_RE = [(n, re.compile(p, re.I)) for n, p in __import__(
    "enumerate_licence")._MARKS]


def family_marks_full(text):
    """`family_marks` with NO truncation window.  See `P448`."""
    t = re.sub(r"\s+", " ", text.lower())
    return sorted({n for n, rx in _MARKS_RE if rx.search(t)})

# The commercial axis. A family is placed here only if this KB already placed it:
# these are the two buckets `intel/market.md` and `compose/patterns.md` have used
# since `p170`, and the point of naming them is that the PERMISSIVE-root/COPYLEFT-deeper
# class was pre-registered before the sweep ran and must not be re-cut afterwards.
PERMISSIVE = {"MIT", "Apache-2.0", "BSD", "ISC", "Unlicense", "CC0-1.0", "ECL-2.0",
              "MulanPSL"}
COPYLEFT = {"GPL", "AGPL-3.0", "LGPL", "MPL-2.0", "EPL", "EUPL", "CC-BY"}

# `P441`'s `is_own_path` decides ownership by DEPTH alone, and depth cannot see a file
# that says in its own NAME that it is about other people's licences.  The first build
# of this instrument published `dequelabs/axe-core` as `DIVERGENT-OWN` on
# `LICENSE-3RD-PARTY.txt` -- a THIRD-PARTY NOTICE at the repository root.  Root depth,
# so `is_own_path` returns True; MIT, so it diverges from the MPL-2.0 root; and it is
# not axe-core's second grant in any sense.  A notice ABOUT dependencies is the `P342`
# class again (an assertion is not a grant) on the axis of the FILENAME.
#
# Declared against my own interest: this rule can only REMOVE rows from
# `DIVERGENT-OWN`, which is the bucket this pass PRE-REGISTERED a ">5" prediction over.
# It is applied anyway, and the prediction is scored after it.
THIRD_PARTY_NAME_RE = re.compile(
    r"3rd[-_. ]?party|third[-_. ]?party|dependenc|notice|attribution|credits?"
    r"|acknowledge?ments?|vendor|bundled", re.I)


def is_own_grant(path):
    """Own-project grant: `P441`'s depth rule AND the filename does not disclaim it."""
    return is_own_path(path) and not THIRD_PARTY_NAME_RE.search(path)


def read_blob(slug, path, timeout=25):
    url = RAW.format(slug=slug, path=urllib.parse.quote(path))
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p447"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return ""


def one(row):
    """(slug, root_path, published_family) -> the full p444 record."""
    slug, root_path, _size, published = row

    # --- stage 0 + 1: the root payload, re-read and re-classified -----------------
    root_text = read_blob(slug, root_path)
    if not root_text:
        return dict(slug=slug, verdict="UNRESOLVABLE", root_path=root_path,
                    published=published, remeasured="(unreadable)", marks=[],
                    marks_full=[], confirmed=[], diverging=[],
                    own_divergence=False, interesting=False)
    remeasured = family_of(root_text)
    marks = family_marks(root_text)
    marks_full = family_marks_full(root_text)

    # --- stage 2: the complete tree ----------------------------------------------
    paths = tree_paths(slug)
    if paths is None:
        return dict(slug=slug, verdict="UNRESOLVABLE", root_path=root_path,
                    published=published, remeasured=remeasured, marks=marks,
                    marks_full=marks_full, confirmed=[], diverging=[],
                    own_divergence=False, interesting=False)

    # Everything that LOOKS like a grant and is not the root file we already read.
    candidates = [p for p in paths if is_grant_path(p) and p != root_path]
    confirmed = []
    for p in candidates:
        text = read_blob(slug, p)
        if not text:
            continue
        fam = family_of(text)
        if fam == "UNKNOWN":
            continue          # P342: a name containing the word is not a grant
        confirmed.append((p, fam, is_own_grant(p)))

    diverging = [(p, f, own) for (p, f, own) in confirmed if f != remeasured]
    own_div = [(p, f) for (p, f, own) in diverging if own]

    if not confirmed:
        verdict = "ROOT-ONLY"
    elif not diverging:
        verdict = "CONCORDANT"
    elif own_div:
        verdict = "DIVERGENT-OWN"
    else:
        verdict = "DIVERGENT-BUNDLED"

    # The pre-registered interesting class, cut on the OWN divergences only.
    interesting = bool(remeasured in PERMISSIVE
                       and any(f in COPYLEFT for _p, f in own_div))

    return dict(slug=slug, verdict=verdict, root_path=root_path,
                published=published, remeasured=remeasured, marks=marks,
                marks_full=marks_full, confirmed=confirmed, diverging=diverging,
                own_divergence=bool(own_div), interesting=interesting)


def main():
    src = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else HERE
    rows = [l.rstrip("\n").split("\t") for l in open(src) if l.strip()]
    with ThreadPoolExecutor(max_workers=12) as ex:
        recs = list(ex.map(one, rows))

    with open(os.path.join(outdir, "divergence.tsv"), "w") as f:
        f.write("slug\tverdict\troot_path\tpublished_family\tremeasured_family"
                "\tfamily_moved\tn_marks\tmarks\tn_marks_full\tmarks_full"
                "\tn_confirmed_deeper"
                "\tdiverging_paths\tinteresting\n")
        for r in recs:
            moved = ("MOVED" if r["remeasured"] != r["published"] else "same")
            div = ";".join("%s=%s%s" % (p, fam, "" if own else "(bundled)")
                           for p, fam, own in r["diverging"]) or "-"
            f.write("\t".join([
                r["slug"], r["verdict"], r["root_path"], r["published"],
                r["remeasured"], moved, str(len(r["marks"])),
                ",".join(r["marks"]) or "-", str(len(r["marks_full"])),
                ",".join(r["marks_full"]) or "-", str(len(r["confirmed"])), div,
                "INTERESTING" if r["interesting"] else "-",
            ]) + "\n")

    # ---- the three stage summaries, each printed with its denominator ------------
    n = len(recs)
    moved = [r for r in recs if r["remeasured"] != r["published"]
             and r["verdict"] != "UNRESOLVABLE"]
    print("## stage 0 -- re-measure of the published set (n=%d)" % n)
    print("rows whose family MOVES under the corrected family_of: %d" % len(moved))
    from collections import Counter
    print("  transitions:", Counter("%s -> %s" % (r["published"], r["remeasured"])
                                    for r in moved).most_common())
    print("  new distribution:", Counter(r["remeasured"] for r in recs).most_common())

    multi = [r for r in recs if len(r["marks"]) > 1]
    multi_full = [r for r in recs if len(r["marks_full"]) > 1]
    print("\n## stage 1 / action B -- payloads naming more than one family (n=%d)" % n)
    print("count naming >1, window 6000 (p441 as built): %d (%.1f%%)"
          % (len(multi), 100.0 * len(multi) / n))
    print("count naming >1, FULL text   (p446 corrected): %d (%.1f%%)"
          % (len(multi_full), 100.0 * len(multi_full) / n))
    widened = [r for r in recs if len(r["marks_full"]) > len(r["marks"])]
    print("rows the window UNDERCOUNTED: %d" % len(widened))
    for r in sorted(widened, key=lambda r: len(r["marks"]) - len(r["marks_full"]))[:12]:
        print("    %-52s %d -> %d  %s" % (r["slug"], len(r["marks"]),
                                          len(r["marks_full"]),
                                          ",".join(r["marks_full"])))
    print("  by combination (FULL):", Counter(",".join(r["marks_full"])
                                              for r in multi_full).most_common(14))
    print("  by granting family (FULL):", Counter(r["remeasured"]
                                                  for r in multi_full).most_common())

    print("\n## stage 2 / action A -- deep-tree divergence (n=%d)" % n)
    print("  verdicts:", Counter(r["verdict"] for r in recs).most_common())
    own = [r for r in recs if r["verdict"] == "DIVERGENT-OWN"]
    print("  DIVERGENT-OWN: %d" % len(own))
    for r in own:
        print("    %-55s root %-12s deeper %s" % (
            r["slug"], r["remeasured"],
            ";".join("%s=%s" % (p, f) for p, f, o in r["diverging"] if o)))
    inter = [r for r in recs if r["interesting"]]
    print("  INTERESTING (permissive root, copyleft own-deeper): %d" % len(inter))
    for r in inter:
        print("    %-55s %s" % (r["slug"], r["remeasured"]))


if __name__ == "__main__":
    main()
