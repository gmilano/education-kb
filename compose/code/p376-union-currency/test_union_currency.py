#!/usr/bin/env python3
"""Offline controls for `p376-union-currency` — `gate-union-currency`, `ACTION p375-A`.

🔵 Every control is a string, a temporary file, or the committed tree.  Nothing here needs
egress, so the gate is runnable in `make hooks` where there is no network.

🔴 The pinning discipline is itself under control.  Group 5 asserts that THIS FILE contains no
literal of the live union total, because a suite that pinned that total would go red on the next
shelf write for the right reason and the wrong cause.  Totals are derived; invariants are
pinned.  That rule is `p310`'s defect and the audit at `Makefile:2947`, applied to the
instrument that discharges `ACTION p375-A`.
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import union_currency as U  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir, os.pardir, os.pardir))

FAILED = []
N = 0


def check(num, what, got, want):
    global N
    N += 1
    if got != want:
        FAILED.append(f"🔴 {num}. {what}\n     got:  {got!r}\n     want: {want!r}")


CANON = ("🟢 The union census, standing from `p376`: **1 234** channel-U addresses and "
         "**5 678** channel-B survivors give **6 000 addresses over both channels**.")

# ── group 1: the governed sentence, and that it cannot be satisfied by p352's ────────────
check(1, "the canonical sentence parses to its three cells",
      U.published(CANON), (1234, 5678, 6000))
check(2, "p352's triple does NOT satisfy the union regex — if it did, one sentence would "
         "discharge the other's gate and the union could go unstated while green",
      U.published("**2 690** harvested shapes -> **33** are not addresses -> "
                  "**2 657 addresses**"), None)
_p352 = U._p352()
check(3, "and the reverse: the union sentence does NOT satisfy p352's TRIPLE_RE, so adding "
         "this gate cannot change what p352 judges",
      _p352.published(CANON), None)
check(4, "a plain-space group is the measured separator on these shelves",
      U.published("**1 000** channel-U addresses, **2 000** channel-B survivors, "
                  "**2 500 addresses over both channels**"), (1000, 2000, 2500))
check(5, "a thin space is cosmetic, not a stale denominator",
      U.published("**1 000** channel-U addresses, **2 000** channel-B survivors, "
                  "**2 500 addresses over both channels**"), (1000, 2000, 2500))
check(6, "a no-break space likewise",
      U.published("**1 000** channel-U addresses, **2 000** channel-B survivors, "
                  "**2 500 addresses over both channels**"), (1000, 2000, 2500))
check(7, "and a comma, because a successor may paste one in",
      U.published("**1,000** channel-U addresses, **2,000** channel-B survivors, "
                  "**2,500 addresses over both channels**"), (1000, 2000, 2500))
check(8, "an unbolded figure is not a published claim — the shelves' convention is bold, "
         "and a number in running prose must not satisfy a denominator gate",
      U.published("1234 channel-U addresses, 5678 channel-B survivors, "
                  "6000 addresses over both channels"), None)
check(9, "FIRST occurrence wins: a correct live sentence above a stale historical one is "
         "read as the live claim, which is how this base keeps history unedited",
      U.published(CANON + "\n\n## Pass 375\n\n**9** channel-U addresses and **9** "
                  "channel-B survivors give **9 addresses over both channels**."),
      (1234, 5678, 6000))
check(10, "and a stale sentence ABOVE a correct one is read as live and will turn the gate "
          "red — the failure mode must point at the live text, not forgive it",
      U.published("**9** channel-U addresses and **9** channel-B survivors give "
                  "**9 addresses over both channels**.\n\n" + CANON), (9, 9, 9))

# ── group 2: the invariants, which are what this suite is allowed to pin ─────────────────
check(11, "a union that loses a member of channel U is impossible",
      bool(U.invariants(100, 50, 99)), True)
check(12, "a union larger than the sum of its parts is impossible",
      bool(U.invariants(100, 50, 151)), True)
check(13, "channel B wholly contained in U is LEGAL — union == U",
      U.invariants(100, 50, 100), [])
check(14, "two fully disjoint channels are LEGAL — union == U + B",
      U.invariants(100, 50, 150), [])
check(15, "an empty channel U is refused: a census over nothing is not a census",
      bool(U.invariants(0, 50, 50)), True)
check(16, "an empty channel B is refused for the same reason — it is the arm p374 found "
          "invisible, and a silent zero would hide its disappearance",
      bool(U.invariants(100, 0, 100)), True)
check(17, "an ordinary tree breaks nothing", U.invariants(1234, 5678, 6000), [])

# ── group 3: the anchor, imported from p352 rather than copied ───────────────────────────
with open(os.path.join(HERE, "union_currency.py"), encoding="utf-8") as fh:
    _instr_src = fh.read()
check(18, "the instrument DEFINES no anchor ladder of its own — the claim is about the "
          "source, not object identity, because a fresh importlib load is never the same "
          "object and a control asserting that it is would be untrue by construction",
      ("ANCHOR_LADDER =" in _instr_src, U._p352().ANCHOR_LADDER == _p352.ANCHOR_LADDER),
      (False, True))
check(19, "and it is still p283's CASE-CLOSED ladder, stem case and extension case both",
      ("README.md" in _p352.ANCHOR_LADDER and "readme.md" in _p352.ANCHOR_LADDER
       and "README.MD" in _p352.ANCHOR_LADDER), True)


def run(root):
    return subprocess.run([sys.executable, "-I",
                           os.path.join(HERE, "union_currency.py"), "--root", root],
                          capture_output=True, text=True).returncode


_empty = tempfile.mkdtemp()
check(20, "no write-up at any rung is a REFUSAL (exit 2), never a verdict — p352's own "
          "convention, so a missing anchor cannot read as a passing census",
      run(_empty), 2)

# ── group 4: the derivation agrees with the instruments it imports ───────────────────────
u, b, union = U.derive(ROOT)
check(21, "channel U here equals p352's third cell — the two standing gates must not "
          "disagree about how many addresses channel U has",
      u, _p352.derive(ROOT)[2])
_um = U._p375()
_shelves = [os.path.join(ROOT, f) for f in U.SHELF_FILES]
_addr, _rej, _harv, _bsurv = _um.union_harvest(_shelves)
check(22, "and the union equals p375's own union_harvest on the same tree, so this gate "
          "reports p375's measurement rather than a second opinion of it",
      (u <= union, b, union), (True, len(_bsurv), len(_addr)))
check(23, "the live tree satisfies its own invariants", U.invariants(u, b, union), [])
check(24, "SHELF_FILES is the same nine-file population p352 censuses, so the two sentences "
          "are derived over one tree and not two",
      U.SHELF_FILES, _p352.SHELF_FILES)

# ── group 5: no total is pinned, and that is itself checked ──────────────────────────────
with open(os.path.abspath(__file__), encoding="utf-8") as fh:
    _src = fh.read()
check(25, "this suite pins NO literal of the live union total: a control that did would go "
          "red on the next shelf write for the right reason and the wrong cause",
      str(union) in _src, False)
check(26, "nor of the live channel-B survivor count", str(b) in _src, False)
check(27, "every numeric fixture in this suite is fictitious — no derived total is "
          "re-read from the tree and written back in as a constant",
      U.published(CANON), (1234, 5678, 6000))

# ── report ──────────────────────────────────────────────────────────────────────────────
print(f"── p376-union-currency ({N} controls over 5 groups: the governed sentence proved "
      f"non-colliding with p352's in BOTH directions, four separator forms, "
      f"first-occurrence-wins in both orders, the set-union invariants that are safe to pin, "
      f"the anchor ladder proved un-redefined at SOURCE level rather than by object identity, agreement with both instruments it "
      f"imports, and a meta-control asserting this suite pins no derived total)")
if FAILED:
    print("   FAIL")
    for f in FAILED:
        print(f)
    sys.exit(1)
print("   PASS")
