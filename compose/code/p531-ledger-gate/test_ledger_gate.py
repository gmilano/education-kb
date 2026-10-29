#!/usr/bin/env python3
"""Unit controls for `p531-ledger-gate` over SYNTHETIC headings.

`ledger_gate.py` asserts over the real corpus; this file asserts the matcher
itself, so a future edit to the dialect regex cannot pass by accident.  Run from
this directory (`p355-cwd-portability`: `-I` strips the script's directory from
`sys.path`, so the import below only resolves from here).
"""

import sys

from ledger_gate import heading_pass, KNOWN_VIOLATIONS, PASS_IN_HEAD

CASES = [
    # (heading, expected pass or None, what it pins)
    ("## 🆕 `p531` — `2026-10-29` — the headline", 531,
     "the backticked dialect, which is the current one"),
    ("## 2026-10-16 - Pass 248 — a title", 248, "the capitalised word form"),
    ("## 2026-10-18 (pass 295) — the nil is TWENTY-ONE deep", 295,
     "the lower-case word form: 234 headings the p530 matcher dropped"),
    ("## 🟢 2026-10-05 — pase 126 (lectura `23:56Z`)", 126,
     "the Spanish dialect"),
    ("## p239 — a bare token", 239, "the bare lower-case token"),
    ("## 2026-10-17 (pass 277) — refuted `p276`'s own expected result", 277,
     "C3: the heading's OWN pass beats a pass it merely cites"),
    # The namespace separation.  Upper-case P is a PROPOSAL, never a pass.
    ("## 🟢 `P553` — consolidate the Moodle bridges", None,
     "upper-case P is the proposal namespace and must not be read as a pass"),
    ("## 🔵 P1024 — a proposal with a four-digit number", None,
     "the same, unbackticked -- this is what a blanket re.I broke"),
    # Roll-ups and forward registrations name a pass without being its section.
    ("## 🆕 Actions opened by p133", None, "C2: the roll-up dialect p531 added"),
    ("## 🟢 Live gaps declared by pass 42 — remedy *and* cost", None,
     "C2: the second roll-up dialect p531 added"),
    ("## 🟢 The rows pass 40 changed, 2026-10-07", None, "C2: the rows roll-up"),
    ("## 🔜 Registered for p540", None, "C2: forward registration"),
    ("## Gaps CLOSED by p529", None, "C2: the closed roll-up"),
    # Non-sections.
    ("### 🆕 `p530` — a sub-heading", None, "a `###` is not a section"),
    ("## History (earlier passes, preserved verbatim)", None,
     "a divider carries no pass"),
    ("## 2026-10-06", None, "a bare date carries no pass"),
    ("Plain prose mentioning `p530`", None, "prose is not a heading"),
]


def main():
    failures = []
    for heading, expected, why in CASES:
        got = heading_pass(heading)
        if got != expected:
            failures.append(f"expected {expected!r}, got {got!r} — {why}\n"
                            f"      {heading!r}")

    # The allowlist is a claim about the corpus; keep it honest about its shape.
    if len(KNOWN_VIOLATIONS) != 2:
        failures.append(
            f"KNOWN_VIOLATIONS holds {len(KNOWN_VIOLATIONS)} entries, not 2. "
            "Two of `530-C`'s four were instrument defects and were FIXED, not "
            "allowlisted; a change here needs a stated reason in the README.")
    for v in KNOWN_VIOLATIONS:
        if not (isinstance(v, tuple) and len(v) == 3 and isinstance(v[0], str)
                and v[1] < v[2]):
            failures.append(f"malformed allowlist entry {v!r} — want "
                            "(file, prev_pass, this_pass) with prev < this")
        if any(isinstance(x, int) and x > 10000 for x in v[1:]):
            failures.append(
                f"allowlist entry {v!r} looks like it carries a LINE NUMBER. "
                "These files are append-only at the top, so a line-keyed "
                "allowlist goes stale once per pass — key on the pass pair.")

    # `pase`/`pass` must not fire on a plural: "passes 277" is not "pass 277".
    if PASS_IN_HEAD.search("## the base passes 277 checks") is not None:
        failures.append("the word form matched a plural ('passes 277')")

    print(f"── p531-ledger-gate unit controls: {len(CASES) + 2} checks over "
          "synthetic headings (every dialect, both roll-up dialects p531 added, "
          "the upper-case proposal namespace, and the allowlist's shape)")
    if failures:
        print("🔴 FAILED")
        for f in failures:
            print(f"   {f}")
        return 1
    print("   PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
