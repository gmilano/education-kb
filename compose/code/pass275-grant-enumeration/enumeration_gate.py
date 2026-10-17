#!/usr/bin/env python3
"""p275 — the OFFLINE half of ACTION p275: no shelf may assert a negative licence
verdict that an enumeration refutes, and no negative verdict may rest on a path ladder
that was never enumerated.

WHY THIS EXISTS.  p274 found `gegok12` refuted twice by probing a slug that does not
exist, and ranked "re-probe every negative licence verdict with ls-remote as a positive
control" as p275's highest-value item.  The control passed on every row -- and running it
exposed that the LADDER, not the slug, is the defect:

  * `os4ed/openSIS-Classic` was carried licence-UNVERIFIED for multiple passes.  Its grant
    is at `docs/License.txt` (GPL-2.0, 17 286 B).  The 19-path ladder never tried that
    spelling, so every one of its 76 probes was guaranteed to miss.
  * `ls1intum/Athena` was carried "no grant, treat as all-rights-reserved, ask TUM in
    writing" across three passes.  12 of its 14 manifests declare `license = "MIT"`.  The
    ladder probed the ROOT `pyproject.toml` -- the one manifest in the repo that is silent.

A ladder can only ever refute the paths it tried.  This gate makes that unfalsifiable
state visible instead of letting it read as a finding.  No network: it reads the shelves
and the enumeration ledgers already committed to `evidence/`.

    python3 -I enumeration_gate.py --root /path/to/education-kb
"""
import argparse
import glob
import os
import re
import sys

SHELVES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md", "compose/patterns.md",
]

# A shelf is ASSERTING an absent grant when one of these appears on the line.
NEGATIVE = re.compile(
    r"no licen[cs]e payload|no payload|no grant|serves no grant|PRE-LICEN[CS]E|"
    r"licen[cs]e[- ]unverified|licen[cs]e UNVERIFIED|all rights reserved|"
    r"treat as all-rights-reserved",
    re.I,
)

# ...but these mark the line as NARRATING a verdict that has since been overturned.
# Greedy by construction (ACTION TB): no lazy quantifiers anywhere in this module.
RETRACTION = re.compile(
    # 🟢 p275 correction 3a: the STEM, not the past participle.  A cell that says it
    # "retracts" an earlier verdict is narrating one just as much as a "RETRACTED" banner.
    r"retract|RESOLVED|REFUTED|refuted|NOW READ|does not exist|UPHELD|"
    r"was FALSE|FALSE in both|no longer|correction|CORRECTED|"
    # 🟢 p275: `trending.md` is APPEND-ONLY, so a wrong cell there is annotated in place
    # with a dated supersede marker rather than rewritten.  The original claim STAYS on
    # the line by design -- so the marker, not the absence of the claim, is what tells the
    # gate the line is narration.
    r"SUPERSEDED|was wrong|"
    # 🔴 p276 D3d: `withdrawn` is this base's own word for retracting published ADVICE
    # ("*Do not use* is WITHDRAWN"), and the vocabulary did not list it -- so a pass's own
    # correction prose read as a live negative verdict.  Same species as D3a-c: the
    # predicate was written from an idea of the house style rather than measured against it.
    r"withdrawn|WITHDRAWN",
    re.I,
)

# 🟢 p275: a line cannot coherently assert "there is no grant" AND publish the grant.
# When it does both, it is a CORRECTION narrating the claim it replaces -- which is the
# idiom this base writes corrections in, and the shape of every line this predicate was
# added for.  Requires an SPDX-ish token AND concrete grant evidence (a licence-bearing
# path or a byte count), so "MIT" appearing alone in prose is not enough to silence a row.
SPDX = re.compile(
    r"\b(MIT|Apache-2\.0|BSD-[23]-Clause|BSD|GPL-[23]\.0|GPL-2|AGPL-3\.0|LGPL-3\.0|"
    r"CC0-1\.0|CC-BY(-NC)?(-SA)?-4\.0|MPL-2\.0|EUPL)\b")
# 🔴 p275: NO global re.I here, and the reason is a defect this predicate caused.
# With re.I the `\bLICEN[CS]E\b` alternative -- meant to match a FILENAME in caps --
# matched a vendor's marketing prose, *"free core is free forever under the MIT licence"*,
# and silenced two live stale claims about `Gego-K12/gegok12`.  A predicate that
# suppresses rows must be narrower than the rows it suppresses.  Case is load-bearing:
# `LICENSE` is a filename; `licence` is a word.
GRANT_EVIDENCE = re.compile(
    r"[Ll]icen[cs]e\.(txt|md|rtf)"      # License.txt, LICENSE.md, LICENSE.rtf
    r"|/[Ll]icen[cs]e\b"                # a PATH ending in a licence file
    r"|\bLICEN[CS]E\b"                  # the bare filename, in caps
    # 🔴 p276 D3a: the old token was r"\d[\d\u00a0 ]*B\b" and it could not cross a
    # markdown backtick -- but THE HOUSE WRITES BYTE COUNTS AS `1 531` B, with the
    # closing backtick BETWEEN the digits and the unit.  361 lines on these shelves
    # carry a measured count this predicate was written to see and could not.
    r"|\d[\d\u00a0 ]*[`*_]*\s*B\b"     # a measured byte count, e.g. "17 286 B", `1 531` B
    r"|(?i:manifests? declare)"         # the metadata channel, stated
    r"|(?i:read at payload)"
    # 🔴 p276 D3b: the house also asserts a first-hand read in PROSE, and the old
    # vocabulary listed only one phrasing of it.  verticals/solutions.md:39 publishes
    # a correct BSD-3-Clause grade and was queued as a live negative verdict.
    r"|(?i:payload is|payload-read|reproduced to the byte|verbatim [A-Z])"
    # 🔴 p276 D3c, and this is D1's defect showing up inside the VOCABULARY.  A row whose
    # grant lives in metadata publishes it by NAMING THE MANIFEST -- "Apache-2.0, per-file
    # headers + pom.xml <licenses> + README", "MIT (metadata)".  That is a published grant in
    # this base's own idiom, and the predicate did not list it, so three rows that are RIGHT
    # read as live negative verdicts.  The file channel was the only channel the vocabulary knew.
    r"|(?i:pom\.xml|package\.json|composer\.json|pyproject\.toml|readme\.txt|<licenses>)"
    r"|(?i:metadata grade|metadata\)|manifest grade)")


def states_a_grant(line):
    """Does this line publish a grant, as well as quoting an absence?"""
    return bool(SPDX.search(line) and GRANT_EVIDENCE.search(line))


SLUG = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

# 🔴 p276 D5a: `frappe/lms` has the basename `lms`, which is an ordinary English noun on
# every shelf in this base.  Bare-name attribution below is a FALLBACK for a project named
# in prose without a link; it must never fire on a word.  Athena (6) and Artemis (7) -- the
# cases the fallback exists for -- are both well clear of this floor.
MIN_BARE_NAME = 4

# p276: an absence marker in a manifest-channel ledger, matched as a PREDICATE.
ABSENT_KEY = re.compile(r"no licen[cs]e key|^-+$|^none$", re.I)

# Directories whose licence files belong to a VENDORED dependency, not to the repo.
VENDORED = re.compile(
    r"(^|/)(vendor|node_modules|custompackages|libraries|third_party|thirdparty|"
    r"precompiled-icons|plugins|samples)(/|$)",
    re.I,
)
# Extensions that make a licence-like path a SOURCE FILE, not a grant.
SOURCEY = re.compile(r"\.(php|java|vue|py|js|ts|jsx|tsx|go|rb|cs|png|svg|jpg|gif)$", re.I)
# 🔴 p276 D2: a licence-like path is not automatically THIS REPO'S CODE GRANT, and the
# first version of this module had no scope test at all.  Three species, each with a
# control from p276's enumeration:
#   * ASSET-scoped   -- mendezjerick/ReaDirect-V2 carries 22 licence-like paths and ALL 22
#                       licence game art, CC0 sprites and OFL fonts.  Not one covers code.
#   * DATASET-scoped -- open-spaced-repetition/srs-benchmark's dataset/LICENSE is 144 B and
#                       says "request permission" -- the inverse of a grant.
#   * TRANSLATION    -- formalms ships license_english.txt ... license_tamil.txt, twelve
#                       translations of the SAME GPL-2.0 whose real payload is html/license.txt.
# Without this test both asset rows report REFUTED, and a REFUTED row FAILS the gate: the
# instrument built to stop false absences would have manufactured two false presences.
SCOPED = re.compile(
    r"(^|/)(assets?|dataset|datasets|fonts?|icons?|images?|media|javascripts|\.corepack)(/|$)",
    re.I,
)
TRANSLATION = re.compile(r"(^|/)licen[cs]e_[a-z]+\.(txt|md)$", re.I)
LICENCEY = re.compile(
    r"(^|/)(licen[cs]e|copying|notice|unlicense|eupl|copyright)", re.I
)


def candidate_grants(paths):
    """Of the licence-like paths an enumeration found, which could be THE repo's grant?"""
    out = []
    for p in paths:
        p = p.strip()
        if not p or p == "NONE_IN_TREE":
            continue
        if not LICENCEY.search(p):
            continue
        if VENDORED.search(p) or SOURCEY.search(p):
            continue
        if SCOPED.search(os.path.dirname(p)) or TRANSLATION.search(p):
            continue  # p276 D2: licences art/data/translations, not this repo's code
        out.append(p)
    return out


def load_ledgers(root):
    """slug -> list of licence-like paths, from every committed enumeration ledger."""
    ledger, dead = {}, set()
    pattern = os.path.join(root, "evidence", "tree-enumeration.*.tsv")
    for path in sorted(glob.glob(pattern)):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#") or not line.strip():
                    continue
                cols = line.rstrip("\n").split("\t")
                if len(cols) < 5 or cols[0] == "slug":
                    continue
                slug, paths_cell = cols[0].strip(), cols[4]
                # 🔴 p275: a slug that does not RESOLVE must never be attributed a shelf's
                # claim about a real project.  `gegok12/gegok12` (dead) and
                # `Gego-K12/gegok12` (real, MIT at root) share the basename `gegok12`, and
                # attributing the dead one LAUNDERED a false "NOT ESTABLISHED" claim about
                # the real repo into a VERIFIED-ABSENT pass.  p251-prefix-collision's class.
                if re.search(r"\bFAIL\b|DOES_NOT_RESOLVE", cols[1] + paths_cell):
                    dead.add(slug)
                    continue
                # the cell is a comma-separated enumeration, or a NONE marker
                if re.search(r"\bNONE\b|NONE_IN_TREE", paths_cell):
                    ledger[slug] = []
                else:
                    ledger[slug] = [c.strip() for c in paths_cell.split(",")]
    return ledger, dead


def load_manifest_ledgers(root):
    """slug -> SPDX-ish licence key, from every committed MANIFEST-channel ledger.

    🔴 p276 D1 -- THE DEFECT THIS FUNCTION EXISTS FOR.  p275's headline case was
    `ls1intum/Athena`: no licence FILE anywhere in the tree, and `license = "MIT"` in 12 of
    its 14 manifests.  p275 found that BY HAND, wrote it up as the pass's central finding --
    and then built this module to read `git ls-tree` FILE paths only.  **The instrument did
    not implement the finding that motivated it.**

    p276 enumerated 30 queue rows in both channels.  Three carry a grant no file enumeration
    can see, and all three would have been stamped VERIFIED-ABSENT by this gate as built:

      * `DMontgomery40/mcp-canvas-lms`  package.json `"license": "MIT"`, and npm
        `canvas-mcp-server` MIT across 19 published versions.  The shelf said *"no LICENSE on
        any branch, no licence statement"* -- the FILE limb true, the STATEMENT limb false.
      * `meyerjp3/psychometrics`        pom.xml `<licenses>` Apache-2.0.
      * `LearnPress/learnpress`         readme.txt `License: GPLv3` + composer.json
        `GPL-3.0-or-later`.

    Column 4 is the licence key as the manifest spells it; `-` and `<no license key>` mean the
    manifest was READ and carries none, which is what makes a two-channel absence sayable.
    """
    man = {}
    pattern = os.path.join(root, "evidence", "manifest-channel.*.tsv")
    for path in sorted(glob.glob(pattern)):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#") or not line.strip():
                    continue
                cols = line.rstrip("\n").split("\t")
                if len(cols) < 5 or cols[0] == "slug":
                    continue
                key = cols[4].strip()
                # 🔴 p276 self-correction, earned by RUNNING this against the live shelves:
                # the first version tested `key not in ("-", "<no license key>")` -- an exact
                # match on a FREE-TEXT cell -- and `Nasus20202/MoodleMCP`, whose cell reads
                # "<no license key in any>" (it has five package.json files), was read as a
                # DECLARED GRANT.  An absence marker must be matched by predicate, not by
                # equality, or the gate manufactures a presence out of prose.
                if key and not ABSENT_KEY.search(key):
                    man[cols[0].strip()] = key
    return man


def attribute(line, names=()):
    """Which slug does each negative phrase on this line actually refer to?

    🔴 p275, two corrections, both found by running the gate on the live shelves:

    1. The first version attributed every negative phrase to every slug on the line, and
       reported `ls1intum/Artemis` -- an MIT row with a root LICENSE -- as refuting
       itself.  The phrase on that line is about `ls1intum/Athena`, named four slugs later
       in the same cell.  One line can carry two subjects.
    2. Nearest-preceding-slug alone was still wrong on `verticals/solutions.md:28`, where
       the subject is the bare word **Athena** in bold PROSE and the only slug on the line
       is Artemis.  A project does not have to be hyperlinked to be the subject.

    Rule: a negative phrase belongs to the nearest project named before it -- whether that
    name arrives as a slug or as a bare repo name the enumeration ledger already knows.
    """
    marks = [(m.start(), m.group(1).rstrip(".")) for m in SLUG.finditer(line)]
    for slug in names:
        base = slug.split("/")[-1]
        # 🔴 p276 D5a: A BASENAME SHORTER THAN FOUR CHARACTERS IS A NOUN, NOT A NAME.
        if len(base) < MIN_BARE_NAME:
            continue
        # 🟢 p275 correction 3b: a POSSESSIVE mention is a modifier, not the subject.
        # "Artemis's feedback-suggestion engine ... treat as all-rights-reserved" is a
        # sentence about ATHENA; `Artemis's` only says whose engine it is.  Reported
        # ls1intum/Artemis -- which has a root LICENSE -- as refuting itself, again.
        #
        # 🔴 p276 D5b: THE TWO GUARDS BELOW, AND WHY THEY COST THIRTEEN FALSE REFUTATIONS.
        # This loop used `\b...\b` with a global re.I.  Enumerating `frappe/lms` -- one
        # ordinary row of p275's own backlog -- then attributed FOURTEEN lines across FIVE
        # shelves to it, and THIRTEEN were about other projects entirely:
        #   `mcp-canvas-lms`, `canvas-lms-mcp`, `AI-LMS-TMS`, `tutor-lms-mcp`  (\b does not
        #       stop at a hyphen, because `-` is itself a non-word character), and
        #   "the LMS-side MCP servers", "a proprietary LMS"                    (re.I makes a
        #       common noun match a repository name).
        # 🔵 The fix is this base's OWN p275 lesson -- *"case is load-bearing: `LICENSE` is a
        # filename, `licence` is a word"* -- applied to ATTRIBUTION instead of suppression.
        # p275 wrote that sentence about the predicate that SUPPRESSES rows and never carried
        # it to the predicate that ASSIGNS them.  A name is matched as the author spelled it,
        # and a name inside a longer token is not a mention.
        for m in re.finditer(r"(?<![-_/A-Za-z0-9])" + re.escape(base)
                             + r"(?![-_/A-Za-z0-9])(?!'s|\u2019s)", line):
            marks.append((m.start(), slug))
    if not marks:
        return []
    marks.sort()
    owners = set()
    for phrase in NEGATIVE.finditer(line):
        before = [s for s in marks if s[0] < phrase.start()]
        owners.add(before[-1][1] if before else marks[0][1])
    return sorted(owners)


def scan(root):
    ledger, dead = load_ledgers(root)
    manifests = load_manifest_ledgers(root)   # p276 D1: the second channel
    refuted, verified, unenumerated = [], [], []
    for shelf in SHELVES:
        full = os.path.join(root, shelf)
        if not os.path.exists(full):
            continue
        with open(full, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                if not NEGATIVE.search(line):
                    continue
                if RETRACTION.search(line) or states_a_grant(line):
                    continue  # narration of an overturned verdict, not a live claim
                for slug in attribute(line, ledger.keys()):
                    if slug not in ledger:
                        unenumerated.append((shelf, n, slug))
                        continue
                    grants = candidate_grants(ledger[slug])
                    # p276 D1: an absence is only sayable when BOTH channels are empty.
                    if not grants and slug in manifests:
                        grants = ["(manifest) " + manifests[slug]]
                    if grants:
                        refuted.append((shelf, n, slug, grants))
                    else:
                        verified.append((shelf, n, slug))
    return refuted, verified, unenumerated


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    refuted, verified, unenumerated = scan(args.root)

    print("# p275 -- enumeration gate.  A negative licence verdict is only a finding if the")
    print("# tree was ENUMERATED.  Otherwise it is the state of a path ladder.")
    print("# p276 -- and the tree is only ONE CHANNEL: a grant can live in a manifest, which is")
    print("# what p275's own headline case (Athena) was.  Both channels must be empty.")
    for shelf, n, slug, grants in refuted:
        print(f"REFUTED\t{shelf}:{n}\t{slug}\tenumeration found a candidate grant: {','.join(grants)}")
    for shelf, n, slug in verified:
        print(f"VERIFIED-ABSENT\t{shelf}:{n}\t{slug}\tenumerated, no candidate grant in tree")
    for shelf, n, slug in unenumerated:
        print(f"QUEUE-UNENUMERATED\t{shelf}:{n}\t{slug}\tnegative verdict rests on a path ladder")
    print(f"# REFUTED={len(refuted)} VERIFIED-ABSENT={len(verified)} "
          f"QUEUE-UNENUMERATED={len(unenumerated)}")
    if refuted:
        print("# FAIL: a shelf asserts an absent grant that an enumeration refutes.")
        return 1
    print("# PASS: no live negative verdict is contradicted by an enumeration.")
    print("#   (QUEUE rows are NOT a failure signal -- they are the enumeration backlog.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
