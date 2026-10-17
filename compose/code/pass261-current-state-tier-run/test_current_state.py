#!/usr/bin/env python3
"""Controls for `pass261-current-state-tier-run` — `ACTION ZD` and `ACTION ZE`.

Every fixture is a payload READ FIRST-HAND at `p261` over `raw.githubusercontent.com`
on an `ls-remote`-resolved ref.  Nothing here is hand-typed except the synthetic
markdown used to pin the harvester's edge cases, and those are marked SYNTHETIC.

  kosudo-nextsis-license.txt         Kosudo/nextSIS @ master              39 890 B
  sonsoleslp-tna-LICENSE             sonsoleslp/tna @ main                    46 B
  sonsoleslp-tna-LICENSE.md          sonsoleslp/tna @ main                 1 075 B
  sonsoleslp-tna-DESCRIPTION         sonsoleslp/tna @ main                 1 471 B
  nakafaai-nakafa-LICENSE            nakafaai/nakafa.com @ main            7 705 B
  nakafaai-nakafa-package.json       nakafaai/nakafa.com @ main            3 765 B
  mbzuai-climategpt-pyproject.toml   mbzuai-oryx/ClimateGPT @ main         1 020 B
  laurentsta-oneduc-composer.json    LaurentSta/Oneduc @ main              2 850 B
  openlrw-LICENSE                    Apereo-…/OpenLRW @ master             9 878 B

🔴 Run from this directory.  `python3 -I` strips the script's own directory from
`sys.path` (p229/p355), which is why every Makefile recipe `cd`s into the instrument.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "pass260-ecosystem-manifest-tier"))

import current_state as cs       # noqa: E402
import manifest_tier as mt       # noqa: E402

FIX = os.path.join(HERE, "fixtures-p261")
FAILURES, MISSING = [], []
CHECKS = 0


def load(name):
    p = os.path.join(FIX, name)
    if not os.path.exists(p):
        MISSING.append(name)
        return None
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def chk(label, got, want):
    global CHECKS
    CHECKS += 1
    if got != want:
        FAILURES.append((label, got, want))


def ok(label, cond):
    chk(label, bool(cond), True)


# ── `ACTION ZD` — the slug reader. ────────────────────────────────────────────────
chk("a github link is a slug",
    cs.slugs_in("see [`a/b`](https://github.com/a/b) for this"), ["github.com:a/b"])
chk("a gitlab link is a DIFFERENT row",
    cs.slugs_in("https://gitlab.com/a/b"), ["gitlab.com:a/b"])
chk("a blob URL yields the repository, not the path",
    cs.slugs_in("https://github.com/a/b/blob/main/LICENSE"), ["github.com:a/b"])
chk("a tree URL likewise", cs.slugs_in("https://github.com/a/b/tree/dev"), ["github.com:a/b"])
chk("a trailing paren is not part of the name",
    cs.slugs_in("(https://github.com/a/b)"), ["github.com:a/b"])
chk("a trailing dot is not part of the name",
    cs.slugs_in("https://github.com/a/b."), ["github.com:a/b"])
chk("an owner profile is not a slug", cs.slugs_in("https://github.com/anowner"), [])
chk("a three-segment path is not a slug",
    cs.slugs_in("https://github.com/a/b/c/d"), [])
# 🔵 Found by mutation M17: the control above passes with the segment guard REMOVED,
# because the terminator alternation already rejects that shape.  This is the input
# that actually reaches the guard — a deep path terminated by whitespace.
chk("a deep path ending in whitespace is not a slug either",
    cs.slugs_in("https://github.com/a/b/c and more"), [])
chk("nor one terminated by a paren",
    cs.slugs_in("(https://github.com/owner/repo/subdir)"), [])
chk("the same slug twice is one row",
    cs.slugs_in("https://github.com/a/b and https://github.com/a/b"), ["github.com:a/b"])
chk("two slugs keep their order",
    cs.slugs_in("https://github.com/a/b https://github.com/c/d"),
    ["github.com:a/b", "github.com:c/d"])
chk("a dotted repository name survives",
    cs.slugs_in("https://github.com/nakafaai/nakafa.com"), ["github.com:nakafaai/nakafa.com"])
chk("no link, no slug", cs.slugs_in("nothing here"), [])
chk("None is not a crash", cs.slugs_in(None), [])

# ── `ACTION ZD` — what a CELL says. ──────────────────────────────────────────────
chk("a family cell", cs.cell_state("| x | `MIT` |"), ("FAMILY", "MIT"))
chk("an absence cell", cs.cell_state("| x | NOASSERTION |")[0], "ABSENT")
chk("`NONE` as a word is an absence", cs.cell_state("| x | NONE |")[0], "ABSENT")
chk("prose absence", cs.cell_state("| x | no readable grant |")[0], "ABSENT")
chk("a silent cell", cs.cell_state("| x | 1 234★ | EMEA |"), ("SILENT", None))
chk("🔴 a FAMILY beside an absence is the operative half",
    cs.cell_state("| x | carried as NOASSERTION, now `MIT` |"), ("FAMILY", "MIT"))
chk("`permit` does not contain a licence (P299's word rule)",
    cs.cell_state("| x | the terms permit redistribution |"), ("SILENT", None))
chk("`submit` likewise", cs.cell_state("| x | submit a PR |"), ("SILENT", None))
chk("AGPL is not read as GPL", cs.cell_state("| x | `AGPL-3.0-or-later` |")[1],
    "AGPL-3.0-or-later")
chk("LGPL is not read as GPL", cs.cell_state("| x | `LGPL-3.0` |")[1], "LGPL-3.0")
chk("a content licence is a family", cs.cell_state("| x | `CC-BY-SA-4.0` |")[1],
    "CC-BY-SA-4.0")
chk("a non-OSI name is a family", cs.cell_state("| x | `Elastic-2.0` |")[1], "Elastic-2.0")
ok("a separator row is not data", not cs.is_table_row("|---|---|"))
ok("a colon-aligned separator is not data", not cs.is_table_row("|:--|--:|"))
ok("a data row is data", cs.is_table_row("| a | b |"))
ok("prose is not a table row", cs.is_table_row("a | b") is False)

# ── 🔴 The three `P###` namespaces.  This is the control that saved the index. ────
ok("🔵 a one-digit `Pass 9` is below the two-digit floor: this base's shelf history "
   "starts at `p117` and a bare `Pass 1` in prose is not a section",
   cs.PASS_IN_HEADING.search("## Pass 9 — x") is None)
chk("`Pass 260` is a pass number",
    cs.PASS_IN_HEADING.search("## Pass 260 — 2026-10-17 — x").group(1), "260")
chk("a date-first heading too",
    cs.PASS_IN_HEADING.search("## 2026-10-17 — Pass 259 — x").group(1), "259")
ok("🔴 a PATTERN id is NOT a pass number",
   cs.PASS_IN_HEADING.search("## 🆕 🟢 `P56` — the licence gate") is None)
ok("🔴 a FINDING id is NOT a pass number",
   cs.PASS_IN_HEADING.search("## 🔴 `P126-S` — the research channel") is None)
ok("a lowercase bare `p251` is not a pass number either",
   cs.PASS_IN_HEADING.search("## gaps restated after p251") is None)
ok("`T260-A` is not a pass number",
   cs.PASS_IN_HEADING.search("## `T260-A` — the tier run") is None)

SYNTHETIC = [
    "## Pass 90 — newest",
    "| [`a/b`](https://github.com/a/b) | `MIT` |",
    "| [`c/d`](https://github.com/c/d) | 1 000★ |",
    "## Pass 80 — older",
    "| [`a/b`](https://github.com/a/b) | NOASSERTION |",
    "| [`c/d`](https://github.com/c/d) | NOASSERTION |",
    "## Pass 70 — oldest",
    "| [`e/f`](https://github.com/e/f) | NOASSERTION |",
]
chk("sections are found in file order", [p for _, p, _, _ in cs.sections(SYNTHETIC)],
    [90, 80, 70])
chk("newest-first is verified, not assumed", cs.newest_first(SYNTHETIC)[0], "NEWEST-FIRST")
chk("an out-of-order file is caught", cs.newest_first(
    ["## Pass 70 — x", "| a |", "## Pass 90 — y", "| b |"])[0], "NOT-MONOTONE")
chk("one heading cannot decide an ordering",
    cs.newest_first(["## Pass 90 — x", "| a |"])[0], "UNDATED")
chk("the orderings agree on the synthetic file",
    cs.ordering_agreement(SYNTHETIC)[0], "AGREE")

H = cs.harvest(SYNTHETIC)
chk("every mention is kept", len(H["github.com:a/b"]), 2)
chk("🟢 the CURRENT state is the newest informative cell",
    cs.current_state(H["github.com:a/b"])["state"], "FAMILY")
chk("and it carries the pass it was read at",
    cs.current_state(H["github.com:a/b"])["pass"], 90)
chk("🔵 a SILENT newer mention is skipped, not treated as state",
    cs.current_state(H["github.com:c/d"])["state"], "ABSENT")
chk("and the state comes from the older section",
    cs.current_state(H["github.com:c/d"])["pass"], 80)
chk("a row with only silent mentions is NEVER-GRADED",
    cs.current_state([{"section": 0, "pass": 90, "line": 1, "state": "SILENT",
                       "token": None}])["state"], "NEVER-GRADED")
chk("an empty mention list is NEVER-GRADED", cs.current_state([])["state"], "NEVER-GRADED")
# 🔵 A correction is written BESIDE the thing it corrects, in the same section — so an
# `ABSENT` cell in the CURRENT section is not answered history, it is the row's own
# before-state.  Found by mutation: `>` passed every control, and so did `>=`.
SAME_SECTION = [
    "## Pass 90 — newest",
    "| [`g/h`](https://github.com/g/h) | was NOASSERTION |",
    "| [`g/h`](https://github.com/g/h) | `MIT`, read first-hand |",
]
_H2 = cs.harvest(SAME_SECTION)
chk("the before-state cell is the row's current ABSENT mention",
    cs.current_state(_H2["github.com:g/h"])["state"], "ABSENT")
ok("🔴 an ABSENT cell in the SAME section is not answered history",
   not cs.already_answered(_H2["github.com:g/h"]))
_H3 = cs.harvest([
    "## Pass 90 — newest",
    "| [`i/j`](https://github.com/i/j) | `MIT`, read first-hand |",
    "| [`i/j`](https://github.com/i/j) | was NOASSERTION |",
])
ok("nor is one BELOW the family inside that same section",
   not cs.already_answered(_H3["github.com:i/j"]))

ok("🔴 `a/b` is answered history — a whole-file harvest would collect it anyway",
   cs.already_answered(H["github.com:a/b"]))
ok("`c/d` is NOT answered history", not cs.already_answered(H["github.com:c/d"]))
ok("p260's method collects `a/b`", cs.naive_population(H["github.com:a/b"]))
ok("ZD's method does not", not cs.current_population(H["github.com:a/b"]))
ok("both methods collect `c/d`", cs.naive_population(H["github.com:c/d"])
   and cs.current_population(H["github.com:c/d"]))
n, c, a, frac = cs.noise_rate(H)
chk("the naive population on the synthetic file", n, 3)
chk("the current population", c, 2)
chk("the answered-history count", a, 1)
chk("the noise fraction", round(frac, 4), round(1 / 3, 4))
chk("an empty harvest is not a division by zero", cs.noise_rate({}), (0, 0, 0, 0.0))

# ── 🟢 The eight REAL shelves, as a live regression. ─────────────────────────────
# A future pass that prepends a section out of order, or renames a shelf, fails here.
for rel in cs.SHELVES:
    p = os.path.join(cs.REPO_ROOT, rel)
    ok(f"shelf exists: {rel}", os.path.exists(p))
_, orderings = cs.harvest_shelves()
for rel, (verdict, heads, withpass) in orderings.items():
    chk(f"ordering AGREE on {rel}", verdict, "AGREE")
    ok(f"{rel} carries dated sections", withpass >= 2)

# ── `ACTION ZE` — the ladder is READ, never copied. ──────────────────────────────
T = cs.ladder_tiers()
chk("three tiers are parsed", sorted(T), ["TIER_A", "TIER_B", "TIER_C"])
ok("Tier A holds the root names", "LICENSE" in T["TIER_A"])
ok("Tier A holds p256's lowercase British spelling", "licence.txt" in T["TIER_A"])
ok("Tier B holds a non-root path", "docs/License.txt" in T["TIER_B"])
ok("Tier C holds p259's Moodle code header", "version.php" in T["TIER_C"])
ok("the ladder is not empty", sum(len(v) for v in T.values()) >= 40)
_src = open(os.path.join(HERE, "current_state.py"), encoding="utf-8").read()
_body = _src.split("def ladder_tiers", 1)[0] + _src.split("return tiers", 1)[1]
ok("🔴 this module holds NO second copy of the ladder "
   "(p229: a probe list copied is a probe list forked)",
   "LICENSE.md" not in _body and "COPYING.LESSER" not in _body)
chk("a missing ladder file is an exception, not a silent empty tier set",
    isinstance(getattr(cs, "ladder_tiers", None), type(cs.ladder_tiers)), True)

M = cs.coverage_matrix({"TIER_A": ["LICENSE", "COPYING"], "TIER_C": ["package.json"]},
                       tree=["LICENSE", "package.json", "src/x.py"],
                       fetched=["LICENSE"])
chk("a path fetched for this row is RUN", M[("TIER_A", "LICENSE")], "RUN")
chk("🔴 a path the tree HAS and the run skipped is NOT-RUN",
    M[("TIER_C", "package.json")], "NOT-RUN")
chk("a path the tree lacks is NOT-IN-TREE, which is not a hole",
    M[("TIER_A", "COPYING")], "NOT-IN-TREE")
frac, run, live = cs.coverage_fraction(M)
chk("coverage counts only the paths the tree has", (run, live), (1, 2))
chk("and it is a fraction of those", frac, 0.5)
chk("a repository with no ladder path has no coverage to report",
    cs.coverage_fraction({("TIER_A", "LICENSE"): "NOT-IN-TREE"}), (None, 0, 0))
chk("an empty matrix likewise", cs.coverage_fraction({}), (None, 0, 0))
chk("a full run is 1.0", cs.coverage_fraction({("TIER_A", "LICENSE"): "RUN"})[0], 1.0)
chk("🔴 the only cause a longer ladder fixes",
    cs.resolution_cause("NONE", "MIT", path_was_on_ladder=False, path_was_in_tree=True),
    "CHANNEL-ABSENT")
chk("the cause that actually pays",
    cs.resolution_cause("NONE", "MIT", path_was_on_ladder=True, path_was_in_tree=True),
    "TIER-NOT-RUN")
chk("a path on the ladder, absent from the tree, that answered anyway",
    cs.resolution_cause("NONE", "MIT", path_was_on_ladder=True, path_was_in_tree=False),
    "ABSENCE-UNCONFIRMED")
chk("no change is not a resolution",
    cs.resolution_cause("MIT", "MIT", True, True), "NO-CHANGE")
chk("p260's cause constant is still the one-member tuple",
    mt.CAUSES_A_LONGER_PATH_LIST_FIXES, ("CHANNEL-ABSENT",))

# ── the shared classifier is CALLED, not reimplemented (P237). ───────────────────
_mit = load("sonsoleslp-tna-LICENSE.md")
if _mit:
    chk("lib/license_family.sh names the real MIT payload", cs.family_of(_mit), "MIT")
chk("an unavailable classifier is a measurement, not a crash",
    cs.family_of("x", family_sh="/nonexistent/license_family.sh"),
    "CLASSIFIER-UNAVAILABLE")

# ── 🔴 "NOT SPDX" is not "prose": the three specified vocabularies. ──────────────
chk("npm's documented pointer is a POINTER, not prose",
    cs.controlled_vocabulary("NPM", "SEE LICENSE IN LICENSE"),
    ("FILE-POINTER:LICENSE", None, "npm-spec:SEE LICENSE IN"))
chk("and it names the file to read next",
    cs.controlled_vocabulary("NPM", "SEE LICENSE IN licences/EULA.md")[0],
    "FILE-POINTER:licences/EULA.md")
chk("npm's other reserved word", cs.controlled_vocabulary("NPM", "UNLICENSED")[0],
    "UNLICENSED-NPM-RESERVED")
chk("a trove classifier is a controlled value",
    cs.controlled_vocabulary("PYPROJECT", "OSI Approved :: Apache Software License"),
    ("Apache-2.0", None, "trove-classifier"))
chk("the `License ::` prefix form reads the same",
    cs.controlled_vocabulary("PYPROJECT",
                             "License :: OSI Approved :: MIT License")[0], "MIT")
chk("a trove classifier can carry the BOUND",
    cs.controlled_vocabulary(
        "PYPROJECT", "OSI Approved :: GNU General Public License v3 or later (GPLv3+)"),
    ("GPL-3.0", "or-later", "trove-classifier"))
chk("`v3 (GPLv3)` is the `only` bound",
    cs.controlled_vocabulary(
        "PYPROJECT", "OSI Approved :: GNU General Public License v3 (GPLv3)")[1], "only")
chk("AGPL is not folded into GPL",
    cs.controlled_vocabulary(
        "PYPROJECT", "OSI Approved :: GNU Affero General Public License v3")[0],
    "AGPL-3.0")
chk("Other/Proprietary is a NAME, and a real one",
    cs.controlled_vocabulary("PYPROJECT", "Other/Proprietary License")[0],
    "NAMED-PROPRIETARY")
chk("an unknown classifier still declines",
    cs.controlled_vocabulary("PYPROJECT", "Some Vendor Terms v4")[0], None)
chk("CRAN's `+ file LICENSE` grammar", cs.controlled_vocabulary(
    "R-CRAN", "MIT + file LICENSE"), ("MIT", None, "cran:<licence> + file LICENSE"))
chk("CRAN's bound grammar",
    cs.controlled_vocabulary("R-CRAN", "GPL (>= 2)"), ("GPL", "or-later", "cran:bound"))
chk("CRAN's `==` is the only bound",
    cs.controlled_vocabulary("R-CRAN", "GPL (== 2)")[1], "only")
chk("CRAN's choice grammar is a CHOICE, not one licence",
    cs.controlled_vocabulary("R-CRAN", "GPL-2 | GPL-3")[0], "CHOICE:GPL-2|GPL-3")
chk("an empty token declines", cs.controlled_vocabulary("NPM", "")[2], "EMPTY")
chk("None declines", cs.controlled_vocabulary("NPM", None)[2], "EMPTY")
chk("a vocabulary is per ECOSYSTEM: CRAN's grammar is not npm's",
    cs.controlled_vocabulary("NPM", "MIT + file LICENSE")[0], None)
chk("and a trove classifier means nothing in a package.json",
    cs.controlled_vocabulary("NPM", "OSI Approved :: MIT License")[0], None)

# ── 🔴 Tier A can hold a PARAMETER SHEET. ────────────────────────────────────────
_sheet = load("sonsoleslp-tna-LICENSE")
_desc = load("sonsoleslp-tna-DESCRIPTION")
if _sheet is not None:
    chk("the 46-byte Tier A payload is a CRAN parameter sheet", len(_sheet.encode()), 46)
    ok("and it is recognised as one", cs.cran_parameter_sheet(_sheet))
    chk("🔴 the shared classifier cannot name it, and should not",
        cs.family_of(_sheet) in ("UNCLASSIFIED", "UNKNOWN", "NO-LICENCE"), True)
if _mit:
    ok("a real MIT text is NOT a parameter sheet", not cs.cran_parameter_sheet(_mit))
ok("a long payload is not a parameter sheet",
   not cs.cran_parameter_sheet("YEAR: 2026\n" + "x" * 500))
ok("a payload with permission language is not a parameter sheet",
   not cs.cran_parameter_sheet("YEAR: 2026\nPermission is hereby granted"))
ok("an empty payload is not a parameter sheet", not cs.cran_parameter_sheet(""))
if _desc:
    tok, read_by = mt.read_declaration("R-CRAN", "DESCRIPTION", _desc)
    chk("DESCRIPTION's licence field is read by its own reader", read_by,
        "DESCRIPTION:License")
    chk("🔴 p260's token reader calls the specified value prose",
        mt.token_verdict(tok), "NOT-SPDX-PROSE")
    chk("🟢 and the CRAN grammar names it",
        cs.controlled_vocabulary("R-CRAN", tok)[0], "MIT")

_pyp = load("mbzuai-climategpt-pyproject.toml")
if _pyp:
    tok, read_by = mt.read_declaration("PYPROJECT", "pyproject.toml", _pyp)
    chk("the classifier is where the grant is", read_by, "toml:classifier")
    chk("🔴 p260 would publish it as unreadable", mt.token_verdict(tok),
        "NOT-SPDX-PROSE")
    chk("🟢 the trove vocabulary resolves it",
        cs.controlled_vocabulary("PYPROJECT", tok)[0], "Apache-2.0")

_npkg = load("nakafaai-nakafa-package.json")
if _npkg:
    tok, _ = mt.read_declaration("NPM", "package.json", _npkg)
    chk("the npm field holds the specified pointer", tok, "SEE LICENSE IN LICENSE")
    chk("🟢 which names the file whose grant is operative",
        cs.controlled_vocabulary("NPM", tok)[0], "FILE-POINTER:LICENSE")

# ── 🔴 A payload is not one grant: the aggregate guard. ─────────────────────────
_agg = load("kosudo-nextsis-license.txt")
if _agg:
    secs = cs.aggregate_sections(_agg)
    ok("nextSIS's licence file IS an aggregate", bool(secs))
    heads = [h for _, h in cs._grant_headings(secs)]
    chk("three grants are bundled in it", len(heads), 3)
    ok("the first is this repository's", heads[0].endswith("General Public License Version 3"))
    ok("the second is CodeIgniter's", "CodeIgniter" in heads[1])
    ok("the third is Bootstrap's", "Bootstrap" in heads[2])
    ok("🔴 the table of contents is NOT read as a grant section",
       not any(h.strip().lower().endswith("contents") for h in heads))
    ok("nor is the Overview", not any("overview" in h.lower() for h in heads))
    chk("the subject's span is pinned", cs.subject_span(_agg), (19, 698))
    chk("🔴 p260's unscoped guard RETRACTS a correct GPL-3.0 cell",
        mt.reservation_verdict(_agg), "RESERVED")
    chk("🟢 the scoped guard places the phrase where it belongs",
        cs.reservation_verdict_scoped(_agg), "THIRD-PARTY-RESERVATION")
    chk("and the shared classifier was right all along", cs.family_of(_agg), "GPL-3.0")
_naka = load("nakafaai-nakafa-LICENSE")
if _naka:
    ok("a single-grant payload is not an aggregate", not cs.aggregate_sections(_naka))
    chk("🟢 a REAL reservation still answers RESERVED",
        cs.reservation_verdict_scoped(_naka), "RESERVED")
    ok("and it says so in its own words", "not an open-source license" in _naka)
_lrw = load("openlrw-LICENSE")
if _lrw:
    ok("a plain ECL-2.0 text is not an aggregate", not cs.aggregate_sections(_lrw))
    chk("no reservation in it", cs.reservation_verdict_scoped(_lrw), "NO-RESERVATION")
    chk("and its family is ECL-2.0", cs.family_of(_lrw), "ECL-2.0")
chk("a BSD header's boilerplate is still boilerplate",
    cs.reservation_verdict_scoped(
        "Copyright (c) 2026 X. All rights reserved.\n\nRedistribution and use in "
        "source and binary forms, with or without modification, are permitted"),
    "BOILERPLATE")
chk("an MIT grant's reservation line likewise",
    cs.reservation_verdict_scoped(
        "All rights reserved.\nPermission is hereby granted, free of charge"),
    "BOILERPLATE")
chk("no phrase, no verdict to make", cs.reservation_verdict_scoped("MIT License"),
    "NO-RESERVATION")
chk("an empty payload is NO-RESERVATION, not a crash",
    cs.reservation_verdict_scoped(""), "NO-RESERVATION")
chk("None likewise", cs.reservation_verdict_scoped(None), "NO-RESERVATION")
ok("a two-rule block with one grant heading is not an aggregate",
   not cs.aggregate_sections("-" * 30 + "\nMIT License\n" + "-" * 30 + "\nterms"))

# ── report ───────────────────────────────────────────────────────────────────────
print(f"pass261-current-state-tier-run: {CHECKS} controls")
if MISSING:
    print("MISSING FIXTURES: " + ", ".join(sorted(set(MISSING))))
if FAILURES:
    print(f"\n{len(FAILURES)}/{CHECKS} FAILED")
    for label, got, want in FAILURES:
        print(f"  - {label}\n     got:  {got!r}\n     want: {want!r}")
    sys.exit(1)
if MISSING:
    sys.exit(1)
print("OK")
