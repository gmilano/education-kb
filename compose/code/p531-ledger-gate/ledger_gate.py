#!/usr/bin/env python3
"""`Gap 530-C` instrument: the control in front of the address ledger.

`p530` built `ingest/address-ledger.py`, put it in front of every pass, and ran
its only correctness check -- section-pass monotonicity -- **by hand, once,
inline in the pass**.  This is that check as a test, plus the three ledger
properties a silent regression would break first.

Why monotonicity is the right check.  The history files run newest-first, so the
pass number of successive `##` sections must DESCEND.  `p530`'s first draft read
the pass from any heading containing `` `pNNN` ``; a `###` sub-heading citing
`p209` in passing then captured 26 000 following lines and `first_seen_pass` came
back `p209` for nearly every address in the base.  Monotonicity is what caught
it, and nothing re-runs it.

🔴 What `p531` found on the first automated run, which is why the allowlist is
three and not the four `530-C` asked for:

  * `intel/open-gaps.md:17901` -- `## Actions opened by p133` is a ROLL-UP
    heading, not p133's section.  `NOT_A_SECTION` excluded `gaps opened` and
    `Gaps CLOSED` by name and missed this dialect, so a roll-up was counted as a
    section and its ascent was about to be allowlisted as history.  **Fixed in
    the matcher, not allowlisted** -- an allowlist entry would have made the
    defect permanent.
  * `repos/trending.md:16626` -- `## 2026-10-17 (pass 277) - ... refuted
    `p276`'s own expected result`.  `\\bPass\\s+` was case-SENSITIVE, so it
    missed the lower-case `pass 277` and the first token it did match was the
    `` `p276` `` CITED IN THE SAME TITLE.  🔴 **That dialect is not an edge
    case: `## ... (pass N) ...` and `## Live gaps declared by pass N` account
    for 234 `##` headings across the three history files, and the instrument
    matched NONE of them.**  A heading it does not recognise does not reset the
    section pointer, so every address first described under one was attributed
    to the newer pass above it.  Counting them takes the corpus from 1 128
    sections to 1 340 -- 🔴 **212 sections, 15.8% of the file, carried the wrong
    pass** -- and this "violation" disappears, because the section above p277 is
    then correctly a higher pass.  `C3` pins the dialect.

Controls:
  C1  the 3 genuine ascending violations are reproduced EXACTLY -- none missing
      (the check still works) and none extra (no new disorder slipped in).
  C2  no roll-up or forward-registration heading is counted as a section.
  C3  a heading whose own pass is written `(pass NNN)` resolves to NNN, even
      when it cites another `pNNN` later in the same line.
  C4  a known-filed address reports `filed_on` non-empty.
  C5  a known history-only address reports `-`.  The fixture is AGPL-3.0, so no
      pass can shelve it and the control cannot rot.
  C6  RATCHET: the ledger's address count does not fall between passes without a
      stated reason (`LEDGER_RATCHET_REASON=...`).

Usage:
    python3 -I compose/code/p531-ledger-gate/ledger_gate.py --repo-root .
"""

import argparse
import os
import re
import sys

HISTORY = ["agents/trending.md", "repos/trending.md", "intel/open-gaps.md"]
LEDGER = "evidence/address-ledger.tsv"
RATCHET = "compose/code/p531-ledger-gate/ratchet.txt"

# Four heading dialects are in use: `` `p529` ``, `Pass 248`, `p239` and the
# Spanish `pase 2`.  The WORD forms are case-folded on their first letter only;
# the bare token stays case-SENSITIVE, and that is load-bearing.  `p531` tried
# a blanket `re.I` here and `C1` refuted it on the first run: this base writes
# PASSES as lower-case `p530` and PROPOSALS as upper-case `P553`, two distinct
# namespaces.  `re.I` merged them -- 1 128 sections became 1 375 and the
# violation set went from 4 to 13, with "ascents" to `p795`, `p865`, `p1024`
# that are proposal numbers, not passes.  🔵 The case of the `p` carries
# meaning in this corpus; only the word forms may be folded.
PASS_IN_HEAD = re.compile(
    r"`p(\d{1,4})`|\b[Pp]ass\s+(\d{1,4})\b|\b[Pp]ase\s+(\d{1,4})\b|\bp(\d{1,4})\b")
# Headings that NAME a pass without BEING that pass's section: forward
# registrations, and the roll-up blocks that sit inside a section.
# `Actions opened by pN` is p531's addition; see the docstring.
NOT_A_SECTION = re.compile(
    r"(🔜|Registered for|Pre-registered|Gaps OPEN after|Gaps CLOSED|"
    r"gaps opened|(Actions|Gaps)\s+(opened|closed)\s+(by|after)|"
    r"(Live\s+)?gaps\s+declared\s+(by|after)|"
    r"Verdicts on|rows pass|The rows? \S+ changed|one row pass)", re.I)

# C1.  (file, previous pass, this pass).  TWO, not the four `530-C` asked for --
# see the module docstring.  Both are genuine: the Spanish `pase 126` sections
# sit below a `## History (earlier passes, preserved verbatim)` divider, which
# is a rewrite boundary by construction.
#
# 🔴 NOT keyed on the line number, and that is deliberate.  p531's first draft
# was, and it failed on p531's own write: these files are APPEND-ONLY at the
# top, so every pass shifts every line below its new section and the allowlist
# would go stale once per pass -- a gate that cries wolf every time it is run
# teaches the next pass to ignore it.  The pass PAIR at a rewrite boundary is
# the invariant; the line number is not.  Lines are still reported, as context.
KNOWN_VIOLATIONS = {
    ("agents/trending.md", 24, 126),
    ("repos/trending.md", 28, 126),
}
FILED_FIXTURE = "HKUDS/DeepTutor"
HISTORY_ONLY_FIXTURE = "HugeCatLab/ChatTutor"


def heading_pass(line):
    """The pass a `##` section belongs to, or None if the line is not one."""
    if not line.startswith("## ") or line.startswith("### "):
        return None
    if NOT_A_SECTION.search(line):
        return None
    m = PASS_IN_HEAD.search(line)
    if not m:
        return None
    return int(next(g for g in m.groups() if g))


def scan_sections(root):
    """Every counted section, every ascending violation, and where each is.

    A violation is keyed (file, prev_pass, this_pass) -- see KNOWN_VIOLATIONS on
    why the line number is reported but not part of the key.
    """
    sections, violations, lines = 0, set(), {}
    for rel in HISTORY:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            return None, None, None, f"missing history file: {rel}"
        prev = None
        with open(path, encoding="utf-8", errors="replace") as fh:
            for ln, line in enumerate(fh, 1):
                n = heading_pass(line)
                if n is None:
                    continue
                sections += 1
                if prev is not None and n > prev:
                    violations.add((rel, prev, n))
                    lines.setdefault((rel, prev, n), []).append(ln)
                prev = n
    return sections, violations, lines, None


def read_ledger(root):
    path = os.path.join(root, LEDGER)
    if not os.path.exists(path):
        return None, f"missing ledger: {LEDGER}"
    rows = {}
    with open(path, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        if header[:4] != ["address", "first_seen_pass", "last_verdict", "filed_on"]:
            return None, f"unexpected ledger header: {header}"
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) >= 4:
                rows[f[0]] = f
    return rows, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--bless-ratchet", action="store_true",
                    help="write the current address count as the new floor")
    args = ap.parse_args()
    root = args.repo_root
    failures = []
    report = []

    sections, violations, lines, err = scan_sections(root)
    if err:
        failures.append(err)
    else:
        report.append(f"C1/C2  sections counted: {sections}")
        missing = KNOWN_VIOLATIONS - violations
        extra = violations - KNOWN_VIOLATIONS
        if missing:
            failures.append(
                "C1 a known violation is no longer reproduced -- the check has "
                f"stopped working, or history was edited: {sorted(missing)}")
        if extra:
            failures.append(
                "C1 NEW ascending section(s): history is no longer newest-first, "
                f"or the pass dialect mis-read a heading: {sorted(extra)}")
        if not missing and not extra:
            where = "; ".join(f"{v[0]}:{lines[v][0]} p{v[1]}→p{v[2]}"
                              for v in sorted(violations))
            report.append(f"C1     {len(violations)}/{len(KNOWN_VIOLATIONS)} known "
                          f"ascending violations reproduced, no new ones — {where}")

    # C2 -- a roll-up heading must never be counted.
    for probe in ["## 🆕 Actions opened by p133",
                  "## 🔜 Registered for p540",
                  "## Gaps CLOSED by p529"]:
        if heading_pass(probe) is not None:
            failures.append(f"C2 roll-up heading counted as a section: {probe!r}")
    # C3 -- the heading's OWN pass wins over a pass it merely cites.
    c3 = heading_pass("## 2026-10-17 (pass 277) — refuted `p276`'s expected result")
    if c3 != 277:
        failures.append(f"C3 own-pass resolution: expected 277, got {c3}")
    else:
        report.append("C2/C3  roll-up headings skipped; own-pass beats cited pass")

    rows, err = read_ledger(root)
    if err:
        failures.append(err)
    else:
        report.append(f"C4/C5  ledger rows: {len(rows)}")
        f = rows.get(FILED_FIXTURE)
        if not f:
            failures.append(f"C4 filed fixture absent from ledger: {FILED_FIXTURE}")
        elif f[3] in ("", "-"):
            failures.append(f"C4 {FILED_FIXTURE} is on a curated file but "
                            f"filed_on reads {f[3]!r}")
        h = rows.get(HISTORY_ONLY_FIXTURE)
        if not h:
            failures.append(
                f"C5 history-only fixture absent from ledger: {HISTORY_ONLY_FIXTURE}")
        elif h[3] != "-":
            failures.append(
                f"C5 {HISTORY_ONLY_FIXTURE} is AGPL-3.0 and unshelvable, so "
                f"filed_on must read '-', not {h[3]!r}")
        if not failures:
            report.append(f"C4     {FILED_FIXTURE} filed on {f[3]}")
            report.append(f"C5     {HISTORY_ONLY_FIXTURE} history-only")

        # C6 -- the ratchet.
        rpath = os.path.join(root, RATCHET)
        floor = None
        if os.path.exists(rpath):
            with open(rpath, encoding="utf-8") as fh:
                for line in fh:
                    line = line.split("#")[0].strip()
                    if line.isdigit():
                        floor = int(line)
        if args.bless_ratchet:
            with open(rpath, "w", encoding="utf-8") as fh:
                fh.write(f"# Gap 530-C ratchet: the ledger's address count must not fall\n"
                         f"# below this without a stated reason.  Raise it with\n"
                         f"#   python3 -I compose/code/p531-ledger-gate/ledger_gate.py --bless-ratchet\n"
                         f"{len(rows)}\n")
            report.append(f"C6     ratchet floor set to {len(rows)}")
        elif floor is None:
            failures.append(f"C6 no ratchet floor recorded in {RATCHET}")
        elif len(rows) < floor:
            reason = os.environ.get("LEDGER_RATCHET_REASON", "").strip()
            if not reason:
                failures.append(
                    f"C6 the ledger lost addresses: {len(rows)} < floor {floor}. "
                    "A decline is a finding, not a default -- re-run with "
                    "LEDGER_RATCHET_REASON='...' once the cause is stated.")
            else:
                report.append(f"C6     decline {floor} -> {len(rows)} accepted: {reason}")
        else:
            report.append(f"C6     {len(rows)} >= floor {floor}")

    for line in report:
        print(line)
    if failures:
        print("🔴 p531-ledger-gate FAILED")
        for f in failures:
            print(f"   {f}")
        return 1
    print("── p531-ledger-gate (6 controls: monotonicity against the 2 genuine "
          "violations, roll-up exclusion, own-pass resolution, filed and "
          "history-only ledger fixtures, address-count ratchet)")
    print("   PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
