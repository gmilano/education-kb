#!/usr/bin/env python3
"""p418's suite: every case names the defect it catches.

The load-bearing cases are the HISTORICAL ones — `p414`–`p416` really happened,
and a gate that cannot red-flag the exact shape of a failure this base already
paid for four times is not a control.
"""
# P115-AK. `python3 -I` drops the script's own directory from sys.path, so a
# sibling import fails under the very invocation this KB's gate READMEs
# prescribe.  Two lines make the documented invocation true.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import gate_register as m

ok, fail = 0, 0


def t(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


def lines(*hdrs):
    out = ["---", "industry: education", "---", ""]
    for h in hdrs:
        out += [h, "", "some prose", ""]
    return out


H = lambda n: f"## 🆕 `p{n}` · 2026-10-24 — headline text"

codes = lambda rows: {r[1] for r in rows}

# ---------------------------------------------------------------- the good case
t("current register reports nothing",
  codes(m.check("reg.md", lines(H(418), H(417)),
                [("top.md", lines(H(418), H(417)))])) == set())

t("register AHEAD of the shelf is fine — a register may lead, never lag",
  codes(m.check("reg.md", lines(H(419)),
                [("top.md", lines(H(418)))])) == set())

# ------------------------------------------------- the four historical failures
t("p411's shape: register one pass behind → STALE",
  codes(m.check("reg.md", lines(H(410)),
                [("top.md", lines(H(411)))])) == {"P418-REGISTER-STALE"})

t("p414-p416's shape: register THREE passes behind → STALE",
  codes(m.check("reg.md", lines(H(413)),
                [("top.md", lines(H(416)))])) == {"P418-REGISTER-STALE"})

t("the staleness DISTANCE is reported, not just the fact",
  "stale by 3 pass(es)" in m.check("reg.md", lines(H(413)),
                                   [("top.md", lines(H(416)))])[0][3])

# -------------------------------------------------------- multi-shelf behaviour
t("stale against ANY shelf is stale, even if current against another",
  codes(m.check("reg.md", lines(H(417)),
                [("top.md", lines(H(417))),
                 ("market.md", lines(H(418)))])) == {"P418-REGISTER-STALE"})

t("one finding per lagging shelf, so the report names every one",
  len(m.check("reg.md", lines(H(410)),
              [("a.md", lines(H(411))), ("b.md", lines(H(412)))])) == 2)

# ------------------------------------------------------------- missing headers
t("a register with no pass header is a finding, not a pass",
  "P418-NO-HEADER" in codes(m.check("reg.md", lines(),
                                    [("top.md", lines(H(418)))])))

t("a shelf with no pass header is named rather than silently skipped",
  codes(m.check("reg.md", lines(H(418)),
                [("top.md", lines())])) == {"P418-NO-HEADER"})

# ------------------------------------------------------ parser negative controls
t("a quoted header inside a table cell is NOT a section of the file",
  m.newest(["| cell | `## 🆕 `p999`` quoted in a row |", H(418)]) == 418)

t("an h3 is not an h2 — level is a type contract (p383)",
  m.newest(["### 🆕 `p999` subsection", H(418)]) == 418)

t("a header without the 🆕 marker is not a pass section",
  m.newest(["## `p999` superseded block", H(418)]) == 418)

t("the newest is a MAXIMUM, not the first seen — order must not matter",
  m.newest([H(400), H(418), H(409)]) == 418)

t("multi-digit pass numbers are not truncated",
  m.newest([H(1058)]) == 1058)

# --------------------------------------------------------------- p541 refusal
t("no input REFUSES rather than printing a clean total",
  m.main([]) == 2)

t("one path alone REFUSES — a register with nothing to compare against is not a measurement",
  m.main(["intel/open-gaps.md"]) == 2)

print(f"\n{ok} passed, {fail} failed")
_sys.exit(1 if fail else 0)
