#!/usr/bin/env python3
"""Unit controls for the p532 pass-heading reader and the promotion queue.

Every fixture below is a REAL heading taken from this repo's history files, or a
minimal synthetic case for a rule.  The point of the suite is the dialect table:
p530's matcher missed 403 of 1 532 candidate headings, p531's fix recovered 214
of them and then mis-read a further class, and both failures were invisible
because nothing asserted a heading's expected pass number anywhere.

Run from this directory:  python3 test_promotion_queue.py
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
for cand in (os.path.abspath(os.path.join(HERE, "..", "..", "..", "ingest")), HERE):
    if os.path.exists(os.path.join(cand, "pass_section.py")):
        sys.path.insert(0, cand)
        break
from pass_section import pass_of_heading  # noqa: E402

sys.path.insert(0, HERE)
from promotion_queue import is_permissive, verdict_of, norm  # noqa: E402

# (heading, expected pass, why this case exists)
HEADINGS = [
    # --- the modern backtick dialect -------------------------------------
    ("## 🆕 `p531` — `2026-10-29` — **TITLE**", 531,
     "backtick id, bold title"),
    ("## 🟢 2026-10-22 · `p375` — zero new agent rows for the third pass running", 375,
     "backtick id after a middot date; `third pass` in the prose is a STREAK"),
    # --- the numeric word-form dialects ----------------------------------
    ("## 2026-10-16 — Pass 250 — THE ROW CHANNEL IS DRY FOR THE TWELFTH PASS", 250,
     "id in the SECOND segment; `twelfth pass` in the title is a streak"),
    ("## Pass 262 — 2026-10-17 — `0` NEW AGENT ROWS FOR A NINTH PASS", 262,
     "id in the FIRST segment"),
    ("## 2026-10-18 (pass 283) — the agent channel returns nothing for the ninth pass running", 283,
     "parenthesised id; p530's matcher was case-sensitive and missed this whole dialect"),
    ("## 🟢 Pass 129 — 2026-10-11 (sixteenth pass of this date), 14:4x–15:3x UTC", 129,
     "a within-day counter must NOT win over the real id"),
    ("## 2026-10-13 — Pass 170 *(append-only; history below is preserved)*", 170,
     "a long italic aside after the id must not hide it"),
    ("## 2026-10-09 — pass 87 (APPEND-ONLY; nothing below this section was altered)", 87,
     "lower-case word form with a long parenthetical"),
    # --- the bare dialect -------------------------------------------------
    ("## 2026-10-13 — p180 — the week's movement is a RETRACTION", 180,
     "bare id as its own segment"),
    ("## 2026-10-13 — p175", 175, "bare id, no title at all"),
    # --- the ordinal-word dialect: invisible to BOTH earlier matchers -----
    ("## 🟢 Seventieth pass, 2026-10-09 — week of 2026-10-09, second reading", 70,
     "ordinal self-id; `second reading` must not win"),
    ("## 🔴 Fifty-eighth pass, 2026-10-08 — the mandated query is saturated for the ninth week", 58,
     "hyphenated tens+ones ordinal"),
    ("## 2026-10-07 — fortieth pass: one new permissive repo, the tier pass 39 said had one", 40,
     "exact-tens ordinal, and `pass 39` in the SAME title is a citation"),
    ("## 2026-10-07 — twenty-ninth pass: the classifier still carried every defect pass 28 had fixed", 29,
     "the p531 fold matched the cited `pass 28` here"),
    ("## 2026-10-07 — twenty-fifth pass: the answer to pass 24's headline gap was already a row", 25,
     "same defect: cited `pass 24` beat the real id"),
    ("## 🟢 Hundred-and-sixteenth pass, 2026-10-11 — **`Gap 404` CLOSED** p114's sizing was exact", 116,
     "hundred-and-X: an ordinal reader that stops at the tens returns 16"),
    ("## 🟢 Hundred-and-twenty-fourth pass, 2026-10-11 — x", 124,
     "hundred-and-tens-ones"),
    ("## 🔴 Hundred-and-second pass, 2026-10-10 — x", 102, "hundred-and-ones"),
    # --- things that are NOT pass sections --------------------------------
    ("## 🔴 🆕 `P125-A` — three live false claims, one on a page p124 read by hand", None,
     "a GAP registration: upper-case `P` is the proposal namespace, and `p124` is a citation"),
    ("## 🟢 `ACTION AF` — one retraction CUE, not thirteen regexes", None,
     "an action block"),
    ("## History (earlier passes, preserved verbatim)", None, "a rewrite divider"),
    ("## 2026-10-06", None, "a date-only heading carries no id"),
]

GRANTS = [
    ("MIT", True), ("Apache-2.0", True), ("BSD", True), ("ECL-2.0", True),
    ("CC0-1.0", True),
    ("AGPL-3.0", False), ("GPL-3.0", False), ("LGPL", False),
    ("MPL-2.0", False), ("CC-BY-SA", False), ("CC-BY", False),
    ("unstated", False), ("no-grant", False), ("absent", False),
    ("Elastic/SSPL/BUSL", False),
    # the conjunctive case: one copyleft token poisons the verdict
    ("AGPL-3.0|MIT", False), ("MIT|Apache-2.0", True), ("GPL-3.0|BSD", False),
]


def main():
    failures = []
    n = 0

    for heading, expected, why in HEADINGS:
        n += 1
        got, dialect = pass_of_heading(heading)
        if got != expected:
            failures.append(
                f"C{n} heading: expected {expected}, got {got} ({dialect})\n"
                f"      why: {why}\n      line: {heading[:100]}")

    for verdict, expected in GRANTS:
        n += 1
        got = is_permissive(verdict)
        if got != expected:
            failures.append(f"C{n} grant: is_permissive({verdict!r}) = {got}, expected {expected}")

    # verdict_of reads the prose, not the repo -- assert that contract plainly.
    n += 1
    if verdict_of("filed under the MIT License") != "MIT":
        failures.append(f"C{n} verdict_of failed on a plain MIT line")
    n += 1
    if verdict_of("a row with no grant named") == "MIT":
        failures.append(f"C{n} verdict_of invented a grant")

    # address normalisation: case-folded key, display preserved.
    n += 1
    key, disp = norm("HKUDS", "DeepTutor")
    if key != "hkuds/deeptutor" or disp != "HKUDS/DeepTutor":
        failures.append(f"C{n} norm gave {key!r}/{disp!r}")
    n += 1
    key, _ = norm("foo", "bar.git")
    if key != "foo/bar":
        failures.append(f"C{n} norm did not strip the .git suffix: {key!r}")

    if failures:
        print(f"🔴 FAIL — {len(failures)} of {n} controls")
        for f in failures:
            print("  " + f)
        return 1
    print(f"🟢 PASS — {n}/{n} controls")
    print(f"   {len(HEADINGS)} heading dialects · {len(GRANTS)} grant verdicts · 4 helpers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
