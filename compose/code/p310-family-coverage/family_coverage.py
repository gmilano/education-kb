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
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "p310_fixtures_census", os.path.join(HERE, "fixtures.py"))
    p310 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p310)
    for name, fam, _com, _why in p310.DECLARED:
        fams[fam] = ("p310-family-coverage", name)
    p309 = p310.p309_fixtures()
    if p309 is not None:
        for prefix, (fam, _n, _sha) in _p309_pins(p309).items():
            fams.setdefault(fam, ("p309-affero-rung-census", prefix))
    return fams


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
    print("#    at the time. This pass takes it to %.0f%%." % (100.0 * covered / total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
