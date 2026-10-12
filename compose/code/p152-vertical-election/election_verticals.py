#!/usr/bin/env python3
"""p152-vertical-election — `ACTION GA`: the election over the SIX vertical platforms.

> 🟢 **`ACTION GA`** — run `p151-election-surface` over the SIX vertical platforms.
> 🔴 *Refuted if the verticals are also silent, 6 of 6* — which would promote `T81` from
> "true of this shelf's small rows" to a property of education copyleft generally, and
> make the "ask the author" advice in `P38` universal rather than row-specific.

## 🔴 Why this is a RE-IMPLEMENTATION and not p151's module, said first

🔴 **p151's `election.py` could not be executed in this pass's sandbox.** The attempt was
refused with `[Code from External]` — the limit this KB recorded at pass 94 as `P970` and
then stopped restating. 🟢 **So the matcher semantics are re-implemented here**, and the
claim this module makes about its own independence is deliberately WEAK:

🔴 **This is a REPRODUCTION control, NOT an independent second surface.** The regexes
carry p151's semantics on purpose, so agreement on the seven rows proves the
re-implementation is faithful — it does **not** corroborate the semantics themselves.
🔵 An independent surface would need a different matcher, and `ACTION GB2` registers it.

## 🟢 The axis this module ADDS, which is why it is not only a port — `P42`

🔴 **p151 published "0 elections over 1 513 files" with no NOTICE denominator.** A tree
with 1 513 files and **zero** GNU per-file notices is silent for a completely different
reason than a tree with 1 513 notices that each decline to elect — and p151's instrument
reports the two identically. 🟢 **`notice_files` is that denominator**: files whose header
names a GNU licence at all. 🔵 Same defect class as the `LINK LAYER`/`PROMPT LAYER` split
at `T84`: two populations reading zero on one instrument for different reasons.

    python3 election_verticals.py <clones-dir> [subject ...]
    python3 test_election_verticals.py        # authored fixtures, offline
"""
import os
import re
import sys

# ── p151's matchers, re-implemented with the same semantics ────────────────────────────
ELECTION_LATER = re.compile(
    r"(?:either\s+version\s+([\d.]+)[^\n]{0,80}?|version\s+([\d.]+)[^\n]{0,40}?)"
    r"or\s*\(?\s*at\s+your\s+option\s*\)?\s*,?\s*any\s+later\s+version", re.I | re.S)
ELECTION_ONLY = re.compile(
    r"version\s+([\d.]+)(?:\s+of\s+the(?:\s+[A-Za-z]+){0,5}?\s+Licen[cs]e)?"
    r"\s+only\b", re.I)
SPDX_ID = re.compile(
    r"SPDX-Licen[cs]e-Identifier\s*:\s*((?:A|L)?GPL-[\d.]+(?:-only|-or-later)?)", re.I)

# 🆕 THE NOTICE DENOMINATOR (`P42`). A file carries a GNU per-file notice when its header
# names a GNU licence. 🔵 Deliberately WIDER than the election matchers: the question it
# answers is "was there a notice that COULD have elected", so a notice that elects nothing
# must still count. 🔴 `license.svg`-style badge text cannot reach here — the extension
# list below is closed, exactly as p151's is.
GNU_NOTICE = re.compile(
    r"GNU\s+(?:Affero\s+General\s+Public|Lesser\s+General\s+Public|General\s+Public)"
    r"\s+Licen[cs]e|\b(?:A|L)?GPL-[\d.]+\b", re.I)

COMMENT_PREFIX = re.compile(r"(?m)^[ \t]*(?:(?:\*|//|#|--|%|;|<!--|\*/)+)[ \t]?")


def normalise(text):
    """Comment markers stripped, whitespace collapsed. Run before every matcher."""
    return re.sub(r"\s+", " ", COMMENT_PREFIX.sub("", text))


LICENCE_FILE = re.compile(
    r"^(LICEN[CS]E|COPYING|UNLICEN[CS]E|LICENSE-MIT|LICENSE-APACHE)"
    r"(\.(md|txt|rst|html))?$", re.IGNORECASE)
SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", ".venv", "venv",
             "__pycache__", "target", ".next", "coverage"}
TEXTY = re.compile(r"\.(py|js|ts|tsx|jsx|java|kt|go|rs|c|h|cc|cpp|cs|php|rb|sh|sql|"
                   r"vue|svelte|html|css|scss|yml|yaml|toml|cfg|md|txt|xml|gradle|"
                   r"json|ini|pl|pm|lua|swift|m|mm|dart|ex|exs|erl|hs|scala|r)$", re.I)
HEADER_BYTES = 8000

COLS = ("subject", "files_scanned", "notice_files", "hdr_or_later", "hdr_only",
        "spdx_elections", "election", "notice_rate_pct", "evidence")


def head(path, n=HEADER_BYTES):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(n)
    except OSError:
        return ""


def walk_sources(root):
    """Every text source file in the tree EXCEPT a licence file, at any depth."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if LICENCE_FILE.match(fn) or not TEXTY.search(fn):
                continue
            yield os.path.join(dirpath, fn)


def licence_bodies(root):
    """The licence files the measurement excluded — the positive control's population."""
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if LICENCE_FILE.match(fn):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


def verdict(later, only, spdx_elections):
    """`OR_LATER`, `ONLY`, `BOTH_CONFLICT`, `SPDX_*` or `SILENT` — p151's ladder."""
    if later and only:
        return "BOTH_CONFLICT"
    if later:
        return "OR_LATER"
    if only:
        return "ONLY"
    if spdx_elections:
        return "SPDX_" + sorted(spdx_elections)[0].split("-")[-1].upper()
    return "SILENT"


def measure(root):
    """The election over the per-file header surface. Never reads a licence file."""
    later, only, spdx, notices, scanned = [], [], [], 0, 0
    for p in walk_sources(root):
        scanned += 1
        t = normalise(head(p))
        rel = os.path.relpath(p, root)
        if GNU_NOTICE.search(t):
            notices += 1
        m = SPDX_ID.search(t)
        if m and m.group(1).lower().endswith(("-only", "-or-later")):
            spdx.append((rel, m.group(1)))
        if ELECTION_LATER.search(t):
            later.append(rel)
        elif ELECTION_ONLY.search(t):
            only.append(rel)
    return dict(scanned=scanned, notices=notices, later=later, only=only, spdx=spdx,
                election=verdict(later, only, [v for _, v in spdx]))


def control(root):
    """THE POSITIVE CONTROL: the same matcher over the licence bodies, which must fire."""
    bodies = licence_bodies(root)
    fired = sum(1 for p in bodies
                if ELECTION_LATER.search(normalise(head(p, 400000))))
    return fired, len(bodies)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    base = argv[1]
    subjects = sorted(d for d in os.listdir(base)
                      if os.path.isdir(os.path.join(base, d)))
    if len(argv) > 2:
        subjects = [s for s in subjects if s in set(argv[2:])]
    print("\t".join(COLS))
    scanned_total = notice_total = ctrl_fired = ctrl_total = silent = 0
    for s in subjects:
        root = os.path.join(base, s)
        r = measure(root)
        f, t = control(root)
        ctrl_fired += f
        ctrl_total += t
        scanned_total += r["scanned"]
        notice_total += r["notices"]
        silent += 1 if r["election"] == "SILENT" else 0
        rate = (100.0 * r["notices"] / r["scanned"]) if r["scanned"] else 0.0
        ev = (r["later"][:2] or r["only"][:2] or [v for _, v in r["spdx"][:2]] or ["-"])
        print("\t".join((s, str(r["scanned"]), str(r["notices"]), str(len(r["later"])),
                         str(len(r["only"])), str(len(r["spdx"])), r["election"],
                         "%.1f" % rate, "; ".join(map(str, ev)))))
    e = sys.stderr.write
    e("subjects=%d  source files scanned=%d  GNU-notice files=%d  SILENT=%d\n"
      % (len(subjects), scanned_total, notice_total, silent))
    e("CONTROL: the same matcher fires on %d of %d licence BODIES\n"
      % (ctrl_fired, ctrl_total))
    if silent == len(subjects) and ctrl_fired == 0:
        e("🔴 INSTRUMENT FAILURE: silent everywhere and the control did not fire.\n")
        return 1
    e("ACTION GA falsifier (the verticals are also silent, 6 of 6): %s\n"
      % ("FIRED" if silent == len(subjects) else "SILENT"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
