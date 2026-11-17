#!/usr/bin/env python3
"""p882 — the acceptance test for `881-G3`.

`881-G3`'s test, in its own words:

> key both gates on the **normalised column set** — strip dates, backticks and case, compare
> the leading column names as a set — and prove it with a fixture pair that differs **only**
> in the embedded date and must grade identically. **One normalisation, two gates.**
> 🔴 If the fix leaves any date inside a signature, it is not fixed.

🔴 **And one clause of that test is REFUSED, with a measurement rather than an opinion.**
`881-G3` names `gate-cell-reproduction` as the second gate, on the grounds that it *"keys on
the same shapes"*. It does not. Its parser
(`compose/code/p442-shelf-tree-crosscheck/extract_published_cells.py`) keys on the PAYLOAD
CELL shape — `` `<path>` <bytes> B · `<sha256₁₂>` `` — and reads no column header at all.
`C13` below measures the real cause: the three sell shelves publish **zero** payload cells,
so its *"zero published cells parsed"* is the `p871`/`p877`-`p880` rewrite dropping the
payload-cell notation. That is `881-G2`'s cluster, not this one, and it makes the count of
instruments reporting that single habit **eight** rather than seven.

So: one normalisation, and the honest number of gates it belongs to is **one** —
`gate-derived-counts`, via `ingest/derive-counts.py`. `C13` is the control that keeps that
claim from being a guess.

Offline: the fixtures are committed bytes and the live reads are of committed shelves.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "ingest"))

from header_sig import norm_cell, sig_key, has_date  # noqa: E402

FAIL = []
N = [0]


def check(name, got, want):
    N[0] += 1
    if got != want:
        FAIL.append("%s\n     got:  %r\n     want: %r" % (name, got, want))


def check_true(name, cond, why=""):
    N[0] += 1
    if not cond:
        FAIL.append("%s%s" % (name, (" — " + why) if why else ""))


# --- C1/C2: 881-G3's named acceptance test -------------------------------------------------
A = os.path.join(HERE, "fixtures", "shelf-A-dated-2026-11-16.md")
B = os.path.join(HERE, "fixtures", "shelf-B-dated-2026-11-17.md")
a_txt = open(A, encoding="utf-8").read()
b_txt = open(B, encoding="utf-8").read()


def header_row(text):
    for line in text.split("\n"):
        if line.startswith("|") and "Licence" in line:
            return line.strip()
    raise AssertionError("fixture has no licence header")


# 🔴 The fixture pair is only evidence if it really differs in nothing else. This is the
# control on the CONTROL: p442's own suite found three defects in its own parser, and the
# lesson this base drew was to grade the instrument's inputs too.
_diff = [i for i, (x, y) in enumerate(zip(a_txt.split("\n"), b_txt.split("\n"))) if x != y]
check("C1 the fixture pair differs in exactly ONE line", len(_diff), 1)
check_true("C1a and that one line is the column header",
           bool(_diff) and a_txt.split("\n")[_diff[0]].strip().startswith("|"),
           "the differing line is not a table header: %r" % (_diff,))
check("C1c the files are the same length (no line added or removed)",
      len(a_txt.split("\n")), len(b_txt.split("\n")))
check("C1b and that line differs only in the date run",
      (header_row(a_txt).replace("2026-11-16", "DATE"),
       header_row(b_txt).replace("2026-11-17", "DATE")),
      (header_row(a_txt).replace("2026-11-16", "DATE"),) * 2)
check("C2 THE acceptance test: a date-only difference grades IDENTICALLY",
      sig_key(header_row(a_txt)), sig_key(header_row(b_txt)))
check_true("C2b and the key is not empty (an empty key would grade everything identically)",
           bool(sig_key(header_row(a_txt))),
           "frozenset() would make C2 pass vacuously")

# --- C3: no date survives into a key -------------------------------------------------------
check_true("C3 881-G3's red clause: no date or pass-id survives normalisation",
           not any(has_date(c) for c in sig_key(header_row(a_txt))))
check("C3b has_date is not vacuously false", has_date("byte-read `2026-11-16`"), True)
check("C3c has_date catches a pass-id too", has_date("★ `p879`"), True)
check("C3d and is false on a plain column", has_date("Pushed"), False)

# --- C4-C8: the three declared reductions --------------------------------------------------
check("C4 backticks and emphasis are stripped",
      norm_cell("**Licence (byte-read)**"), "license byte-read")
check("C5 licence/license fold (p811's recorded cause of RED)",
      norm_cell("License"), norm_cell("Licence"))
check("C6 case folds", norm_cell("PUSHED"), norm_cell("Pushed"))
check("C7 the compound columns keep their separators",
      norm_cell("★ / forks"), "★ / forks")
check("C8 a pass-id column normalises to nothing and is dropped from the set",
      sig_key("| Repo | ★ `p882` | `p879` | SPDX |"),
      frozenset({"repo", "★"}))

# --- C9-C11: what must NOT be folded -------------------------------------------------------
check_true("C9 provenance is NOT folded: 'as measured' != 'byte-read'",
           norm_cell("Licence, as measured") != norm_cell("Licence (byte-read)"))
check_true("C9b nor 're-read'",
           norm_cell("Licence, re-read") != norm_cell("Licence (byte-read)"))
check("C10 the final free-prose column is dropped",
      sig_key("| Repo | Licence | ★ | Why it is here |"),
      sig_key("| Repo | Licence | ★ | Role in an engagement |"))
check_true("C10b but a DIFFERENT leading column still separates two shapes",
           sig_key("| Repo | Licence | ★ | Pushed | Role |")
           != sig_key("| Repo | Licence | ★ | Created | Role |"))
check("C11 order is not meaning for a set",
      sig_key("| Repo | Licence | ★ | Pushed | Role |"),
      sig_key("| Repo | ★ | Licence | Pushed | Role |"))

# --- C12: non-headers are not keyable ------------------------------------------------------
check("C12 a separator row is not a header", sig_key("|---|---|"), frozenset({"", ""}) & set())
check("C12b prose is not a header", sig_key("Some prose line"), frozenset())
check("C12c a one-column row is not a header", sig_key("| Repo |"), frozenset())
check("C12d empty input is not a header", sig_key(""), frozenset())

# --- C13: the REFUSED clause of 881-G3, measured -------------------------------------------
# 🔴 881-G3 asserts gate-cell-reproduction "keys on the same shapes". It keys on payload
# cells. The real cause of its RED is that the sell shelves publish none.
PAYLOAD = re.compile(r"`[A-Za-z0-9._/-]+`[*_\s]*[\d  , ]+[*_\s]*B[*_\s]*·")
SELL = ("agents/top.md", "repos/foundations.md", "verticals/solutions.md")
payload_cells = sum(
    len(PAYLOAD.findall(open(os.path.join(REPO, f), encoding="utf-8").read())) for f in SELL)
check("C13 the sell shelves publish ZERO payload cells — 881-G3's second gate is "
      "881-G2's cluster, not this one", payload_cells, 0)
# And the positive control, so C13 cannot be passing because the regex is broken:
check("C13b the payload-cell regex does match a payload cell",
      bool(PAYLOAD.search("`main/LICENSE` 11 407 B · `596087a7f098`")), True)

# --- C14: the live shelves are located, which is the whole point ---------------------------
sys.path.insert(0, os.path.join(REPO, "ingest"))
ns = {}
exec(re.search(r"^SHELVES = \[.*?^\]\n",
               open(os.path.join(REPO, "ingest", "derive-counts.py"), encoding="utf-8").read(),
               re.S | re.M).group(0), ns)


def tables(lines):
    i = 0
    while i < len(lines) - 1:
        h, sep = lines[i].strip(), lines[i + 1].strip()
        if h.startswith("|") and re.match(r"^\|[\s:|-]+\|$", sep) and "-" in sep:
            j = i + 2
            body = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                body.append(lines[j])
                j += 1
            yield h, body
            i = j
        else:
            i += 1


collapse = []
for rel, sigs, excl in ns["SHELVES"]:
    keys = {sig_key(s) for s in sigs} - {frozenset()}
    exc = {sig_key(s) for s in excl} - {frozenset()}
    matched = unc = 0
    for h, body in tables(open(os.path.join(REPO, rel), encoding="utf-8").read().split("\n")):
        k = sig_key(h)
        if k and k in keys:
            matched += 1
        elif any("github.com/" in r for r in body) and k not in exc:
            unc += 1
    check_true("C14 %s is LOCATED (>=1 table matched)" % rel, matched > 0,
               "this was the 881-G3 RED: 'no table can be located'")
    check_true("C14b %s has no UNCOUNTED address-bearing table" % rel, unc == 0,
               "%d table(s) carry github.com rows under an undeclared key" % unc)
    # p813's ratchet, kept. The collapse is measured in AGGREGATE below, not per shelf:
    # 🔴 a per-shelf control here FAILED on agents/top.md on this suite's first run, because
    # that shelf's 9 literals happen to hold no date-variant pair. The control was wrong, not
    # the shelf — a normalisation is not obliged to collapse something on every file.
    collapse.append((rel, len(sigs), len(keys)))

# --- C15: the collapse, measured in aggregate ----------------------------------------------
_lits = sum(n for _, n, _ in collapse)
_keys = sum(k for _, _, k in collapse)
check_true("C15 the column-set key collapses literal variants across the shelves "
           "(%d literals -> %d keys, %d collapsed)" % (_lits, _keys, _lits - _keys),
           _lits - _keys >= 4,
           "fewer than the 4 pure date-variant pairs 881-G3 implies were collapsed")
for rel, n, k in collapse:
    print("   %-24s %2d declared literals -> %2d distinct keys" % (rel, n, k))

print("p882-header-signature: %d controls" % N[0])
if FAIL:
    print("\U0001f534 %d FAILED:" % len(FAIL))
    for f in FAIL:
        print("  - %s" % f)
    sys.exit(1)
print("\U0001f7e2 PASS")
