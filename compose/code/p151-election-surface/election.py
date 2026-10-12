#!/usr/bin/env python3
"""p151-election-surface — `ACTION FO`: the `-only` / `-or-later` election.

> 🟡 **`ACTION FO`** — read the `-only` / `-or-later` election for the five GPL-family
> rows, from per-file headers rather than the licence body.
> 🔴 *Refuted if no row states an election anywhere* — which would establish that this
> shelf's copyleft rows are silent on the one term that decides what a derivative may
> relicense to, and `P38` step 4 must say so instead of implying the election is readable.

## Why this is `T77` one layer down, and why the body must be excluded

🔴 **Every GNU licence file contains the election.** GPL-3.0 ships an appendix, *"How to
Apply These Terms to Your New Programs"*, whose recommended notice reads *"either version
3 of the License, or (at your option) any later version"*. 🔴 **So a body search for the
election fires on every verbatim GNU file — including one whose author elected `-only`.**
That is exactly `T77`'s defect class: a phrase that is correct as a phrase and wrong as a
test, because it occurs inside the text it is meant to interrogate. 🆕 **`T81`.**

🟢 **The election lives on the per-file header surface**, which is where the GNU project's
own instructions put it, and on the SPDX identifier line. This module reads those two and
never the licence file — `walk_sources()` excludes a licence file at any depth.

## The positive control, which is the point of the module

🔴 **A null result from a matcher nobody has seen fire is not a measurement.** So
`control()` runs the SAME matcher over the licence BODIES that `measure()` excluded. If
the matcher cannot fire there, `SILENT` is an instrument artefact.

🟢 **Measured, 2026-10-12, pass 151, over the 7 GNU-family rows:**
**1 513 source files scanned, 0 `-or-later` headers, 0 `-only` statements, 0 SPDX
elections — and the control fires on 7 of 7 licence bodies.** 🔴 **`ACTION FO` is REFUTED
exactly as specified.** The matcher works; the rows are silent.

🔵 **What that means in a room.** For all seven rows the election is the GNU default for a
*silent* licensee: there is none, so a downstream relicensor cannot rely on "or later".
`P38` step 4 must say the election is UNSTATED on this shelf rather than imply it is
readable.

    python3 election.py /tmp/edu-trees
"""
import os
import re
import sys

# "either version 3 of the License, or (at your option) any later version" and its
# single-clause variants. 🔵 The `[^\n]{0,80}` windows keep the match inside one notice.
ELECTION_LATER = re.compile(
    r"(?:either\s+version\s+([\d.]+)[^\n]{0,80}?|version\s+([\d.]+)[^\n]{0,40}?)"
    r"or\s*\(?\s*at\s+your\s+option\s*\)?\s*,?\s*any\s+later\s+version", re.I | re.S)
# "version 3 of the License only", "GPL version 2 only", "version 3 only".
# 🔵 The licence-name words between "of the" and "License" are counted, not spelled: the
# wild forms are "of the License", "of the GNU General Public License" and "of the GPL",
# and a pattern that spells one of them misses the others — the mistake that made the
# first version of this module read an authored `-only` fixture as SILENT.
ELECTION_ONLY = re.compile(
    r"version\s+([\d.]+)(?:\s+of\s+the(?:\s+[A-Za-z]+){0,5}?\s+Licen[cs]e)?"
    r"\s+only\b", re.I)
# The machine-readable surface, which settles the question without prose.
SPDX_ID = re.compile(
    r"SPDX-Licen[cs]e-Identifier\s*:\s*((?:A|L)?GPL-[\d.]+(?:-only|-or-later)?)", re.I)

# 🔴 **A comment prefix breaks the match, and the first version of this module did not
# know it.** A GNU per-file notice in the wild is wrapped in a block comment:
#
#     * the Free Software Foundation, either version 3 of the License, or
#     * (at your option) any later version.
#
# so the two halves of the phrase are separated by `"\n * "`, which `\s*` does not cross.
# 🟢 The fixtures in `test_election.py` caught it before the sweep was published, and it
# is the reason `normalise()` exists: every line is stripped of its comment marker and the
# text is collapsed to single spaces BEFORE any election matcher runs.
COMMENT_PREFIX = re.compile(r"(?m)^[ \t]*(?:(?:\*|//|#|--|%|;|<!--|\*/)+)[ \t]?")


def normalise(text):
    """Comment markers stripped, whitespace collapsed. Run before every matcher."""
    return re.sub(r"\s+", " ", COMMENT_PREFIX.sub("", text))


# 🔴 The extension list is CLOSED, and it has to be. `edwyj/ddl-killer` ships
# `docs/assets/readme/license.svg` — a BADGE IMAGE. An open `(\.[A-Za-z0-9]+)?` suffix
# counted it as a licence file, which is why the positive control first reported "7 of 8"
# instead of 7 of 7: one of the eight was a picture.
LICENCE_FILE = re.compile(
    r"^(LICEN[CS]E|COPYING|UNLICEN[CS]E|LICENSE-MIT|LICENSE-APACHE)"
    r"(\.(md|txt|rst|html))?$", re.IGNORECASE)
SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", ".venv", "venv",
             "__pycache__", "target", ".next", "coverage"}
TEXTY = re.compile(r"\.(py|js|ts|tsx|jsx|java|kt|go|rs|c|h|cc|cpp|cs|php|rb|sh|sql|"
                   r"vue|svelte|html|css|scss|yml|yaml|toml|cfg|md|txt|xml|gradle|"
                   r"json|ini|pl|pm|lua|swift|m|mm|dart|ex|exs|erl|hs|scala|r)$", re.I)
# A GNU notice sits at the top of a file. 8 kB is generous for a header and keeps a
# 200 kB vendored blob from being read as one.
HEADER_BYTES = 8000

COLS = ("subject", "file_licence", "files_scanned", "hdr_or_later", "hdr_only",
        "spdx_elections", "election", "evidence")


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
    """The licence files the measurement excluded — the control's population."""
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if LICENCE_FILE.match(fn):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


def verdict(later, only, spdx_elections):
    """`OR_LATER`, `ONLY`, `BOTH_CONFLICT`, `SPDX_*` or `SILENT`.

    🔵 `BOTH_CONFLICT` is a reported state, not a resolved one: a tree whose headers say
    both things has no election this module may pick.
    """
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
    later, only, spdx, scanned = [], [], [], 0
    for p in walk_sources(root):
        scanned += 1
        t = normalise(head(p))
        rel = os.path.relpath(p, root)
        m = SPDX_ID.search(t)
        if m and m.group(1).lower().endswith(("-only", "-or-later")):
            spdx.append((rel, m.group(1)))
        if ELECTION_LATER.search(t):
            later.append(rel)
        elif ELECTION_ONLY.search(t):
            only.append(rel)
    return dict(scanned=scanned, later=later, only=only, spdx=spdx,
                election=verdict(later, only, [v for _, v in spdx]))


def control(root):
    """THE POSITIVE CONTROL: the same matcher over the licence bodies, which must fire.

    🔴 Returns (fired, total). A `SILENT` measurement alongside `fired == 0` is an
    instrument failure and must be reported as one, not as a finding about the rows.
    """
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
    scanned_total = ctrl_fired = ctrl_total = silent = 0
    for s in subjects:
        root = os.path.join(base, s)
        r = measure(root)
        f, t = control(root)
        ctrl_fired += f
        ctrl_total += t
        scanned_total += r["scanned"]
        silent += 1 if r["election"] == "SILENT" else 0
        ev = (r["later"][:2] or r["only"][:2] or [v for _, v in r["spdx"][:2]] or ["-"])
        print("\t".join((s, "-", str(r["scanned"]), str(len(r["later"])),
                         str(len(r["only"])), str(len(r["spdx"])), r["election"],
                         "; ".join(map(str, ev)))))
    e = sys.stderr.write
    e("subjects=%d  source files scanned=%d  SILENT=%d\n"
      % (len(subjects), scanned_total, silent))
    e("CONTROL: the same matcher fires on %d of %d licence BODIES\n"
      % (ctrl_fired, ctrl_total))
    if silent == len(subjects) and ctrl_fired == 0:
        e("🔴 INSTRUMENT FAILURE: silent everywhere and the control did not fire.\n")
        return 1
    e("ACTION FO falsifier (no row states an election anywhere): %s\n"
      % ("FIRED" if silent == len(subjects) else "SILENT"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
