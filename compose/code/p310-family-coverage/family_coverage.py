#!/usr/bin/env python3
"""p310 — FIXTURE COVERAGE: which licence families does this base PUBLISH, and
which of them does the dynamic arm's corpus actually exercise?

🔴 THE MEASUREMENT THIS PASS EXISTS FOR.  `p309` built the dynamic arm, ran every
declared classifier on pinned payloads, and reported `declared=11 CORRECT=11
DEFECT=0`.  One pass later the same ladder mis-graded a real `CC-BY-NC-4.0`
payload as `CC0-1.0` — a NonCommercial grant read as a public-domain dedication,
which is the one error direction that puts unusable supply INTO a deliverable.

🔵 Both facts are true, and the reconciliation is this file.  `p309`'s corpus held
three families.  A gate that runs real code on real payloads is still only a
statement about the families in its corpus, and `DEFECT=0` reads as a statement
about the classifier.  **The coverage ratio is the missing denominator, and
without it a green dynamic gate is an unbounded claim.**

🔵 The published set is MEASURED, not listed by hand.  `TOKENS` below is a
grammar for how a licence family is spelled on these shelves, not a roster of
which ones are there; the shelves supply the roster and its counts, so a family
this base starts publishing tomorrow appears in the denominator by itself.

Usage: family_coverage.py [repo-root]     (default: four levels up from here)
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, ".."))

# 🔴 THE SHELF LIST IS IMPORTED, AND THE FIRST BUILD OF THIS FILE RESTATED IT.
# That is `p308`'s rule — *"import the canonical list, never restate it"* — broken
# inside the instrument written to generalise `p309`'s failure to apply it.
# `p308-shelf-consistency` already imports `carried_index.SHELVES`; a hand-copied
# nine-file list here was both a second source of truth and ONE SHELF SHORT
# (`intel/open-gaps.md`, where 21 of this base's PolyForm cells live).
#
# 🔵 It also cleared a `p283-ladder-case-audit` false positive: the literal
# `"README.md"` in a restated list reads to that audit as a one-rung README-path
# ladder, and the STANDING ratchet went red at 19 against a ceiling of 17. The
# ratchet's own note warns that bumping the number is what eight passes were
# trained to do. Importing the list removed the literal and the cause together.
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "p235-carried-index")))
from carried_index import SHELVES  # noqa: E402

# 🔵 A GRAMMAR, not a roster: how a family is SPELLED when this base publishes a
# licence. Ordered longest-first within each family so `CC-BY-NC-SA-4.0` is not
# harvested as `CC-BY-SA-4.0` — `p124`'s `SUBSTRING` instance, which is the exact
# error class this whole file is about.
TOKENS = [
    ("CC-BY-NC-SA-4.0", r"CC[\s-]?BY[\s-]?NC[\s-]?SA[\s-]?4\.0"),
    ("CC-BY-NC-ND-4.0", r"CC[\s-]?BY[\s-]?NC[\s-]?ND[\s-]?4\.0"),
    ("CC-BY-NC-4.0",    r"CC[\s-]?BY[\s-]?NC[\s-]?4\.0"),
    ("CC-BY-SA-4.0",    r"CC[\s-]?BY[\s-]?SA[\s-]?4\.0"),
    ("CC-BY-4.0",       r"CC[\s-]?BY[\s-]?4\.0"),
    ("CC0-1.0",         r"CC0[\s-]?1\.0"),
    ("AGPL-3.0",        r"AGPL[\s-]?3(?:\.0)?"),
    ("LGPL-3.0",        r"LGPL[\s-]?3(?:\.0)?"),
    ("GPL-3.0",         r"(?<![AL])GPL[\s-]?3(?:\.0)?"),
    ("GPL-2.0",         r"(?<![AL])GPL[\s-]?2(?:\.0)?"),
    ("Apache-2.0",      r"Apache[\s-]?(?:License[\s-]?)?2\.0"),
    ("MPL-2.0",         r"MPL[\s-]?2\.0"),
    ("EPL-2.0",         r"EPL[\s-]?2\.0"),
    ("ECL-2.0",         r"ECL[\s-]?2\.0"),
    ("BSD-3-Clause",    r"BSD[\s-]?3[\s-]?Clause"),
    ("BSD-2-Clause",    r"BSD[\s-]?2[\s-]?Clause"),
    ("0BSD",            r"\b0BSD\b"),
    ("MIT",             r"\bMIT\b"),
    ("ISC",             r"\bISC\b"),
    ("Unlicense",       r"\bUnlicense\b"),
    ("PolyForm-Noncommercial-1.0.0", r"PolyForm[\s-]?Noncommercial"),
    ("proprietary",     r"\bproprietary\b|all[\s-]rights[\s-]reserved"),
    # 🔴 ADDED AT p311, AND THE REASON IS THE WHOLE POINT OF THIS FILE.
    # `P310` says the families a gate owes a payload to *"are not a matter of
    # taste — they are the ones the shelves publish"*, and that this module
    # DERIVES that set. It derives it through the grammar above, so what it
    # actually derives is **the set of families the grammar can spell**. Every
    # token below names a family this base publishes WITH FIRST-HAND EVIDENCE
    # and for which no token existed, so a perfectly good licence cell was
    # invisible to the denominator:
    #   EUPL      Finland's national education stack (`koski`), read at
    #             EUPL-1.1-or-later with 9 placed addresses across two versions
    #   BUSL-1.1  `sdv-dev/SDV`, `twentyhq/twenty` — source-available, NOT OSI
    #   Elastic   a cell carrying a probed `4 102` B payload
    #   SSPL      published on this base's own shelves
    #   LGPL-2.1  a vendored PHPMailer in a school SIS; the base records that
    #             its obligations DIFFER from LGPL-3.0's and that it could not
    #             tell them apart
    #   OSL, OFL  published, unbucketed
    # 🔵 Both ends of the risk spectrum were missing at once: the EU's own
    # public-sector licence, and the source-available family a studio must not
    # build on. → `P311-D`.
    ("EUPL-1.2",        r"EUPL[\s-]?1\.2"),
    ("EUPL-1.1",        r"EUPL[\s-]?1\.1"),
    ("BUSL-1.1",        r"BUSL[\s-]?1\.1|Business[\s-]Source[\s-]License"),
    ("Elastic-2.0",     r"Elastic[\s-]?License(?:[\s-]?2\.0)?"),
    ("SSPL-1.0",        r"\bSSPL\b"),
    ("LGPL-2.1",        r"LGPL[\s-]?2\.1"),
    ("OSL-3.0",         r"OSL[\s-]?3\.0"),
    ("OFL-1.1",         r"\bOFL\b|SIL[\s-]Open[\s-]Font"),
    # 🟡 A bare `BSD` is not BSD-2, BSD-3 or 0BSD, and it is how `p310` shelved
    # `TUBAF-IFI-DiPiT/github2pandas` — whose payload's own title line reads
    # `BSD 2-Clause License`. Ordered AFTER the specific BSD tokens so
    # longest-first still owns a versioned span. It is a real spelling carrying
    # real rows, so it gets a bucket rather than silence — and the bucket's name
    # says what is wrong with it.
    # 🔴 The first spelling of this token was a bare `\bBSD\b`, and it DOUBLE-
    # COUNTED: the suppression rule above skips a shorter family only when one
    # name contains the other, and neither `BSD-3-Clause` nor `BSD-UNVERSIONED`
    # contains the other, so every versioned BSD line was counted twice and this
    # bucket reported 575 cells — more than BSD-3-Clause and BSD-2-Clause
    # combined, which is what gave it away. 🔵 The family is *BSD with no
    # version*, so the version must be excluded in the PATTERN, not hoped for
    # from the loop. `0BSD` is already safe: the digit kills the leading \b.
    ("BSD-UNVERSIONED", r"\bBSD\b(?![\s-]*[0-9])"),
]

# 🔵 Licence-shaped spellings that STILL have no family token. This is a
# blind-spot report, not a roster: the point is that the list above is written by
# hand and therefore has an edge, and the only honest thing to do with an edge is
# measure it. 🔴 Counted in LINES THE GRAMMAR CLAIMS NOTHING FOR, which is an
# UPPER BOUND on cells — prose mentions are counted too, and this module does not
# distinguish a licence cell from a sentence about a licence.
UNBUCKETED_PROBES = [
    ("GPL unversioned",     r"(?<![AL])\bGPL\b(?![\s-]?[0-9])"),
    ("AGPL unversioned",    r"\bAGPL\b(?![\s-]?[0-9])"),
    ("LGPL unversioned",    r"\bLGPL\b(?![\s-]?[0-9])"),
    ("Apache unversioned",  r"\bApache\b(?![\s-]?(?:License[\s-]?)?[0-9])"),
    ("CC-BY unversioned",   r"\bCC[\s-]?BY\b(?![\s-]?[0-9A-Z])"),
    ("CC-BY-SA unversioned", r"\bCC[\s-]?BY[\s-]?SA\b(?![\s-]?[0-9])"),
    ("MPL unversioned",     r"\bMPL\b(?![\s-]?[0-9])"),
    ("EPL unversioned",     r"\bEPL\b(?![\s-]?[0-9])"),
    ("ECL unversioned",     r"\bECL\b(?![\s-]?[0-9])"),
    ("Sustainable Use",     r"Sustainable[\s-]?Use"),
    ("Prosperity",          r"\bProsperity[\s-]?Public"),
    ("CDDL",                r"\bCDDL\b"),
    ("zlib",                r"\bzlib[\s-]?license\b"),
    ("WTFPL",               r"\bWTFPL\b"),
    ("CeCILL",              r"\bCeCILL\b"),
]

# 🔴 `MIT` matches inside `LIMITED` and `ISC` inside `DISCLAIMED` — `p124`'s
# instance 5, found inside the very module written to prevent it. The word
# boundaries above handle those two; this guard handles the shelf-specific ones,
# where a token appears inside a slug or a URL rather than as a licence cell.
NOT_A_CELL = re.compile(r"github\.com/|https?://|`[a-z0-9_.-]*mit[a-z0-9_.-]*`", re.I)


def published(root):
    """{family: hits} over the live shelves, plus the files that were unreadable."""
    counts, missing = {}, []
    compiled = [(fam, re.compile(rx, re.I)) for fam, rx in TOKENS]
    for rel in SHELVES:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            missing.append(rel)
            continue
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if NOT_A_CELL.search(line):
                    # Keep only the part outside links/slugs: a licence cell and a
                    # repo URL routinely share one table row.
                    line = NOT_A_CELL.sub(" ", line)
                claimed = []
                for fam, rx in compiled:
                    if rx.search(line):
                        # longest-first: a longer family already matched on this
                        # line owns the span, so do not double-count the shorter.
                        if any(fam in c or c in fam for c in claimed):
                            continue
                        claimed.append(fam)
                        counts[fam] = counts.get(fam, 0) + 1
    return counts, missing


def corpus_families():
    """The families the dynamic arms actually hold a payload for.

    🔵 IMPORTED from each instrument's own fixture declaration, never listed here
    — the whole subject of this pass is that a restated list goes stale silently.
    """
    fams = {}
    # 🔴 `import fixtures` CANNOT be used here, and the reason is this base's own
    # `p150-identifier-collision`, met three times in one pass: `p309`'s arm does
    # `sys.path.insert(0, its own dir); import fixtures`, which registers ITS
    # `fixtures.py` in `sys.modules` under the bare name. Any later `import
    # fixtures` — from this file, from the test suite, from a hook — then gets
    # p309's module and dies on `no attribute 'DECLARED'`. 🔵 Two instruments, one
    # plausible filename, first loader wins. Every load is namespaced by pass.
    # 🟢 p311: the sibling instruments are DISCOVERED, not named. This function's
    # own docstring says a restated list goes stale silently — and it did, within
    # one pass: the next pass pinned `MIT` and `Apache-2.0`, the two biggest
    # families on this base, and this census would have gone on reporting them
    # uncovered because its loader named one instrument as a literal. 🔵 Any sibling
    # exporting `DECLARED` in the (prefix, family, commercial, why) form is read;
    # newest pass first, so the earliest pin keeps the attribution.
    import importlib.util

    def _load(dirname):
        path = os.path.join(CODE, dirname, "fixtures.py")
        if not os.path.exists(path):
            return None
        spec = importlib.util.spec_from_file_location(
            "%s_census" % dirname.replace("-", "_"), path)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception:                                # noqa: BLE001
            return None
        return mod

    # 🔴 p312: this sort was `reverse=True`, which with `setdefault` below gave
    # the attribution to the NEWEST instrument — the opposite of what the comment
    # above states (*"so the earliest pin keeps the attribution"*) and of what
    # `p311`'s own control asserts. It went unnoticed while `p311` was the newest
    # directory and broke the moment `p312` added one that sorts after it: the
    # census credited `p312-template-identity` with `MIT`, a family `p311` pinned
    # first. 🟢 Ascending, so the EARLIEST pin keeps the credit, which is also
    # what makes the census agree with `p311`'s `HISTORY` table.
    siblings = sorted(
        d for d in os.listdir(CODE)
        if os.path.isdir(os.path.join(CODE, d))
        and os.path.exists(os.path.join(CODE, d, "fixtures.py")))

    p310 = None
    for dirname in siblings:
        mod = _load(dirname)
        if mod is None or not hasattr(mod, "DECLARED"):
            continue
        if dirname.startswith("p310-"):
            p310 = mod
        for entry in mod.DECLARED:
            name, fam = entry[0], entry[1]
            fams.setdefault(fam, (dirname, name))

    # 🔵 p309 declares `PINS`, not `DECLARED`, and keeps its own key grammar.
    p309 = p310.p309_fixtures() if p310 is not None else _load("p309-affero-rung-census")
    if p309 is not None:
        for prefix, (fam, _n, _sha) in _p309_pins(p309).items():
            fams.setdefault(fam, ("p309-affero-rung-census", prefix))
    return fams



def unbucketed(root):
    """{probe: lines} for licence-shaped spellings no family token claims.

    🔴 The unit is LINES THE GRAMMAR CLAIMED NOTHING FOR — an upper bound on
    cells, stated as one. A line of prose about the GPL counts here exactly like
    a GPL licence cell, because this module cannot tell them apart. 🔵 The number
    is therefore evidence that the grammar HAS an edge, not a measurement of how
    many rows sit past it.
    """
    compiled = [(fam, re.compile(rx, re.I)) for fam, rx in TOKENS]
    probes = [(name, re.compile(rx, re.I)) for name, rx in UNBUCKETED_PROBES]
    hits = {}
    for rel in SHELVES:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if NOT_A_CELL.search(line):
                    line = NOT_A_CELL.sub(" ", line)
                if any(rx.search(line) for _fam, rx in compiled):
                    continue
                for name, rx in probes:
                    if rx.search(line):
                        hits[name] = hits.get(name, 0) + 1
    return hits


def _p309_pins(p309):
    """p309's PINS keyed to a family token, read from its own declaration."""
    out = {}
    for prefix, pin in getattr(p309, "PINS", {}).items():
        fam = prefix.split("-")[0].upper()
        if prefix.startswith("gpl-3.0"):
            fam = "GPL-3.0"
        elif prefix.startswith("agpl-3.0"):
            fam = "AGPL-3.0"
        elif prefix.startswith("ccbysa-4.0"):
            fam = "CC-BY-SA-4.0"
        out[prefix] = (fam, pin, prefix)
    return out


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(
        os.path.join(HERE, "..", "..", ".."))
    sys.path.insert(0, HERE)
    counts, missing = published(root)
    corpus = corpus_families()

    print("# p310 fixture coverage — the families this base PUBLISHES against the")
    print("# families the dynamic arms hold a PAYLOAD for.")
    print("#")
    if missing:
        print("# 🔴 shelves not readable from %s: %s" % (root, ", ".join(missing)))
    print("# %-32s %6s   %s" % ("family", "cells", "fixture"))
    covered = uncovered = 0
    rows = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    for fam, n in rows:
        if fam in corpus:
            inst, name = corpus[fam]
            print("  🟢 %-32s %6d   %s/%s" % (fam, n, inst, name))
            covered += 1
        else:
            print("  🔴 %-32s %6d   —" % (fam, n))
            uncovered += 1
    total = covered + uncovered
    print("#")
    print("# published families=%d  with a pinned payload=%d  WITHOUT=%d  coverage=%.0f%%"
          % (total, covered, uncovered, (100.0 * covered / total) if total else 0))
    print("#")
    print("# 🔵 This is EXPOSURE WITH A DENOMINATOR, not a list of findings. An")
    print("#    uncovered family means the dynamic arm has never run a single")
    print("#    classifier against that family's real legalcode — so `DEFECT=0`")
    print("#    says nothing about it either way. `p309` reported `11/11 CORRECT`")
    print("#    at %.0f%% coverage (3 of %d families) and the CC rungs were broken"
          % ((100.0 * 3 / total if total else 0), total))
    print("#    at the time.")
    print("#")
    print("# 🔴 p311 — AND THIS RATIO'S OWN DENOMINATOR IS NOT SAFE. The family set")
    print("#    above is derived through a HAND-WRITTEN grammar (`TOKENS`), so what")
    print("#    it derives is the set of families the grammar can SPELL. p311 added")
    print("#    9 tokens for families this base publishes with first-hand evidence")
    print("#    and had no bucket for at all — EUPL-1.1/1.2, BUSL-1.1, Elastic-2.0,")
    print("#    SSPL-1.0, LGPL-2.1, OSL-3.0, OFL-1.1, BSD-UNVERSIONED. → `P311-D`.")
    blind = unbucketed(root)
    if blind:
        print("#")
        print("# 🟡 licence-shaped spellings STILL unclaimed by any token, in LINES")
        print("#    (an UPPER BOUND on cells: prose is counted too):")
        for name, n in sorted(blind.items(), key=lambda kv: -kv[1]):
            print("#      %5d  %s" % (n, name))
        print("#    🔵 The edge is measured rather than denied. A coverage ratio")
        print("#       whose denominator comes from a restated grammar is as")
        print("#       unbounded as the `DEFECT=0` that `P310` was written to bound.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
