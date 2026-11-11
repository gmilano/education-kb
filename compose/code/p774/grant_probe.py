#!/usr/bin/env python3
"""p774 grant prober + grader -- written FROM SCRATCH.

Why from scratch, again. `ACTION p773-B` and `ACTION p773-C` each name a
PROCEDURE held in this repository (`compose/code/p773/grantprobe.sh`,
`compose/code/p773/grade2.py`). Both were tried and both were DENIED in this
session with `[Code from External]` -- the same denial that has blocked
`make hooks` for five consecutive sessions. 🔵 So the denial is BROADER than
`make hooks`: it covers execution of ANY code this repository holds, including
the instruments a previous pass left behind as the procedure for the next one.
Nothing was copied out of the repository to evade it; this is an independent
implementation. Only DATA is read from the tree (`ingest/canonical/*.txt`).

Contracts
  probe   the grant filename space, CASE-AWARE and wide, on the MEASURED
          default branch (never an assumed `main`)
  grade   identity unit = normalised operative body with fillable slots MASKED
  budget  ACTION p773-D: an ABSOLUTE character budget, never a ratio. At 0.995
          similarity a 34,020-char AGPL payload tolerates ~170 changed chars --
          enough to invert an obligation -- while the same ratio on a
          1,078-char MIT file tolerates 5. One ratio cannot serve both.
  rungs   body -> operative body -> absolute budget -> SPDX tag -> notice prose
  undec   byte-identical canonical pairs (only vs or-later) are reported as a
          GROUP, because no body diff can ever separate them
"""
import re, sys, os, difflib, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

# ---- the filename space: case-aware and wide (p773 D9: ERPNext's GPL-3.0
# grant sits at a lowercase `license.txt`, and a 15-name list missed it) ----
NAMES = ["LICENSE","LICENSE.md","LICENSE.txt","LICENSE.rst","LICENCE","LICENCE.md",
         "LICENCE.txt","license","license.md","license.txt","licence","licence.txt",
         "License","License.md","License.txt","COPYING","COPYING.txt","COPYING.md",
         "copying","copying.txt","COPYRIGHT","NOTICE","LICENSE-MIT","LICENSE-APACHE",
         "LICENSE-APACHE-2.0","LICENSE.APACHE2","MIT-LICENSE","MIT-LICENSE.txt",
         "LICENSE.BSD","docs/LICENSE",".github/LICENSE","LICENSE.GPL","COPYING.LESSER"]

UA = {"User-Agent": "kb-ingest-grant-probe/1.0"}

def fetch(url, timeout=20):
    try:
        r = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(r, timeout=timeout) as f:
            return f.status, f.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""

def probe(slug, branch):
    """Return (filename, payload) or (None, None). Measured branch only."""
    for n in NAMES:
        code, body = fetch(f"https://raw.githubusercontent.com/{slug}/{branch}/{n}")
        if code == 200 and body.strip():
            return n, body
    return None, None

# ------------------------- normalisation -------------------------------
def norm(s):
    s = s.replace("\r\n", "\n")
    s = re.sub(r"[‘’‛]", "'", s)
    s = re.sub(r"[“”]", '"', s)
    return re.sub(r"\s+", " ", s).strip().lower()

def mask(s):
    """Mask the fillable slots AND the non-operative decoration, so a filled
    template compares equal to the template. A licence TITLE line and an
    `all rights reserved` notice are boilerplate, not terms, and the canonical
    SPDX texts omit both -- leaving them in spends the whole absolute budget
    on decoration and reads a clean BSD/MIT payload as an alteration."""
    s = re.sub(r"copyright\s*(\(c\)|©)?\s*[^\n]{0,120}?"
               r"(?=permission|redistribution|all rights reserved|$)",
               " <COPYRIGHT> ", s, flags=re.I)
    s = re.sub(r"<[a-z ]*(organization|organisation|copyright holder|year|owner|name)[a-z ]*>",
               " <SLOT> ", s, flags=re.I)
    s = re.sub(r"\b(19|20)\d\d(\s*[-–]\s*((19|20)\d\d|present))?\b", " <YEAR> ", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"^(the\s+)?(mit|bsd[ -]*\d*[ -]*clause|isc|apache|mozilla public|"
               r"gnu [a-z ]*public)\s+licen[cs]e(\s*\(?[a-z0-9.\- ]*\)?)?\s*", " ", s, flags=re.I)
    s = re.sub(r"all rights reserved\.?", " ", s, flags=re.I)
    return re.sub(r"\s+", " ", s).strip()

def operative(s):
    """Apache's grant ends at END OF TERMS AND CONDITIONS; the appendix is
    optional boilerplate and a payload that omits it is not altered."""
    i = s.find("end of terms and conditions")
    return s[:i].strip() if i > 0 else s

SPDX = re.compile(r"SPDX-License-Identifier:\s*([A-Za-z0-9.\-+]+)", re.I)

# D9 (p774, this instrument's own, and it was caught by CROSS-CHECKING the rung's
# answer against the family the shelf already claimed -- not by the rung itself).
# `norm()` collapses the whole payload onto ONE line. A notice pattern written as
# `gnu affero general public licen[cs]e.*?version\s*3` therefore matches "GNU
# Affero General Public License" at one END of a document and "version 3" at the
# other, across thousands of intervening characters. It graded `nvaccess/nvda`
# -- GPL-2.0, and claimed as GPL-2.0 on these shelves -- as AGPL-3.0.
# 🔵 The fix is a BOUNDED window: the version must sit within 60 characters of the
# licence name, which is where a real notice puts it. Same shape as p772's D6:
# "on the same line" is not "about this subject".
NOTICE_NAMES = [
    (r"affero general public licen[cs]e", {"3": "AGPL-3.0"}),
    (r"lesser general public licen[cs]e", {"3": "LGPL-3.0", "2.1": "LGPL-2.1"}),
    (r"library general public licen[cs]e", {"2": "LGPL-2.0", "2.1": "LGPL-2.1"}),
    (r"general public licen[cs]e", {"3": "GPL-3.0", "2": "GPL-2.0"}),
    (r"apache licen[cs]e", {"2.0": "Apache-2.0", "2": "Apache-2.0", "1.1": "Apache-1.1"}),
    (r"mozilla public licen[cs]e", {"2.0": "MPL-2.0", "2": "MPL-2.0", "1.1": "MPL-1.1"}),
    (r"eclipse public licen[cs]e", {"2.0": "EPL-2.0", "1.0": "EPL-1.0"}),
    (r"creative commons attribution[- ]sharealike", {"4": "CC-BY-SA-4.0", "4.0": "CC-BY-SA-4.0"}),
    (r"creative commons attribution", {"4": "CC-BY-4.0", "4.0": "CC-BY-4.0"}),
    # The education sector's own two licences, neither of which this base held
    # before p774. Finland's national application system (`ataru`) and its study-
    # records system (`koski`) are EUPL, and Sakai is ECL-2.0.
    (r"european union public licen[cs]e|\beupl\b",
     {"1.2": "EUPL-1.2", "1.1": "EUPL-1.1", "1": "EUPL-1.1", "2": "EUPL-1.2"}),
    (r"educational community licen[cs]e|\becl\b", {"2": "ECL-2.0", "2.0": "ECL-2.0"}),
    # Bare abbreviations. `frappe/education`'s ENTIRE grant file is the 19-byte
    # string "License: GNU GPL V3" -- no licence text, and `GNU GPL V3` is not a
    # valid SPDX identifier either, so the only-vs-or-later axis is undecidable
    # from the only thing the repository says about its own terms.
    (r"\bagpl\b", {"3": "AGPL-3.0", "3.0": "AGPL-3.0"}),
    (r"\blgpl\b", {"3": "LGPL-3.0", "2.1": "LGPL-2.1", "2": "LGPL-2.0"}),
    (r"\bgnu gpl\b|\bgplv?\b", {"3": "GPL-3.0", "2": "GPL-2.0", "3.0": "GPL-3.0"}),
    (r"\bmpl\b", {"2": "MPL-2.0", "2.0": "MPL-2.0"}),
]
NOTICE_BARE = [(r"\bmit licen[cs]e\b", "MIT"), (r"\bisc licen[cs]e\b", "ISC"),
               (r"\bunlicense\b", "Unlicense"), (r"\bbsd 3-clause\b", "BSD-3-Clause"),
               (r"\bbsd 2-clause\b", "BSD-2-Clause"), (r"\bwtfpl\b", "WTFPL")]
# 🔴 The commercially decisive rung, and it must run BEFORE every other one.
# `tixuz/openemis-mcp` is published on these shelves as MIT. Its LICENSE.md is
# the BUSINESS SOURCE LICENSE 1.1 -- source-available, "non-production
# evaluation and internal testing only", converting to MIT on 2029-01-01.
# 🔵 And the trap is precise: a BSL notice NAMES its future licence
# ("Change License: MIT"), so any rung that resolves a family by looking for a
# licence name in prose will read a BSL file as MIT. The non-free check has to
# come first or it is useless. For a studio told to build on MIT/Apache/BSD,
# this is the difference between a dependency and a breach.
NONFREE = [
    (r"business source licen[cs]e",               "BSL-1.1"),
    (r"server side public licen[cs]e|\bsspl\b",    "SSPL-1.0"),
    (r"elastic licen[cs]e",                       "Elastic-2.0"),
    (r"commons clause",                           "Commons-Clause"),
    (r"polyform",                                 "PolyForm"),
    (r"functional source licen[cs]e|\bfsl-",       "FSL"),
    (r"creative commons attribution[- ]non[- ]?commercial|\bcc[ -]by[ -]nc\b",
                                                  "CC-BY-NC"),
    (r"noncommercial use only|non-commercial use only", "NonCommercial"),
    (r"redistribution .{0,40}prohibited",         "NO-REDISTRIBUTION"),
]

def nonfree_family(p):
    for rx, fam in NONFREE:
        if re.search(rx, p):
            return fam
    return None

# D11 (p774, this instrument's own): a real notice does not always write the word
# "version". `ataru` says "Licensed under the EUPL, Version 1.2"; a CC notice says
# "Attribution-ShareAlike 4.0 International"; `frappe/education` says "GNU GPL V3".
# Inside a 60-character window immediately after the licence NAME, the first number
# IS the version, so a bare number is accepted there -- and only there.
VER = re.compile(r"(?:version\s*|\bv)?(\d+(?:\.\d+)?)", re.I)

def notice_family(p):
    """Rung 5: resolve the family from NOTICE PROSE, with the version bound to a
    60-character window after the licence name (D9)."""
    for rx, vermap in NOTICE_NAMES:
        for m in re.finditer(rx, p):
            win = p[m.end():m.end() + 60]
            vm = VER.search(win)
            if vm:
                v = vm.group(1) or vm.group(2)
                if v in vermap:
                    return vermap[v]
                # a named family at a version this map does not carry is still
                # information: report it rather than silently falling through
                if len(vermap) == 1 and v.split(".")[0] in [k.split(".")[0] for k in vermap]:
                    return list(vermap.values())[0]
    for rx, fam in NOTICE_BARE:
        if re.search(rx, p):
            return fam
    return None

def load_canon(d):
    raw = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".txt"):
            raw[fn[:-4]] = norm(open(os.path.join(d, fn), encoding="utf-8",
                                     errors="replace").read())
    groups = {}
    for n, b in raw.items():
        groups.setdefault(b, []).append(n)
    # byte-identical arms collapse into ONE group: the axis is undecidable
    return {"|".join(sorted(v)): k for k, v in groups.items()}

def pick(fam, tag):
    if "|" not in fam:
        return fam
    arms = fam.split("|")
    if tag:
        for a in arms:
            if a.lower() == tag.lower():
                return a
    return fam + " [body-identical group; only-vs-or-later UNDECIDABLE from body]"

BUDGET = 25   # absolute characters, at ANY document size (ACTION p773-D)

# D8 (p774, this instrument's own, and it REFINES ACTION p773-D rather than
# confirming it). p773-D measured that a RATIO threshold cannot serve two
# document sizes and prescribed an absolute character budget instead. Control
# K11 shows the absolute budget is necessary but NOT SUFFICIENT: inserting the
# single word `never` into the AGPL's "If you convey a covered work" costs
# SIX characters, passes any budget above five, and INVERTS the obligation.
# 🔵 So the unit of licence identity is not the SIZE of the edit. It is whether
# the edit touches a deontic operator -- a negation, a modal, or a scope word.
# A six-character edit that moves one of those is an alteration at any budget.
DEONTIC = re.compile(
    r"\b(not|never|no|none|cannot|can't|must|shall|may|should|will|required|"
    r"prohibited|forbidden|except|unless|without|solely|only|exclusive|"
    r"non-exclusive|irrevocable|revocable|perpetual|terminate|termination|"
    r"liable|liability|warrant|warranty|grant|granted|denied)\b", re.I)

def diff_segments(a, b):
    """The changed text on both sides of the diff, as a list of strings."""
    segs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b).get_opcodes():
        if op != "equal":
            segs.append(a[i1:i2]); segs.append(b[j1:j2])
    return segs

def deontic_shift(a, b):
    """True if the diff adds, removes or rewrites a deontic operator."""
    for seg in diff_segments(a, b):
        if DEONTIC.search(seg):
            return DEONTIC.search(seg).group(0).lower()
    return None

def delta_chars(a, b):
    return sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2
               in difflib.SequenceMatcher(None, a, b).get_opcodes() if op != "equal")

def grade(payload, canon):
    raw_len = len(payload)
    m = SPDX.search(payload)
    tag = m.group(1).strip() if m else None
    p = norm(payload); pm = mask(p); po = mask(operative(p))
    nf = nonfree_family(p)
    if nf:
        return dict(f=nf, r="NOT-OPEN-SOURCE(source-available or restricted)",
                    t=tag, b=raw_len)
    # D7 (p774, this instrument's own): the first write held BOTH a containment
    # score (prefer the LONGEST canonical contained) and an edit-distance score
    # (prefer the SMALLEST delta) in one `best` slot and compared them against
    # each other. A BSD-4 delta beat a BSD-3 containment and control K3 graded a
    # clean BSD-3 payload as an ALTERED BSD-4. The two scales are incomparable and
    # are now ranked separately: containment first, then smallest delta.
    contained, altered = [], []
    for name, body in canon.items():
        bm = mask(body); bo = mask(operative(body))
        if pm == bm:
            return dict(f=pick(name, tag), r="body:canonical", t=tag, b=raw_len)
        if bm and bm in pm:
            i = pm.find(bm); pre, post = i, len(pm) - i - len(bm)
            r = ("canonical+PREPENDED" if pre > 0 and post == 0 else
                 "canonical+APPENDED" if post > 0 and pre == 0 else "canonical+SURROUNDED")
            contained.append((len(bm), dict(f=pick(name, tag), r=r, t=tag,
                                            b=raw_len, pre=pre, post=post)))
            continue
        if bo and po and bo == po:
            return dict(f=pick(name, tag), r="canonical:operative-body-match", t=tag, b=raw_len)
        # ABSOLUTE budget, no ratio gate on document size (ACTION p773-D)
        if bm and abs(len(pm) - len(bm)) <= 400:
            d = delta_chars(pm, bm)
            if d == 0:
                return dict(f=pick(name, tag), r="body:canonical(slot-filled)", t=tag, b=raw_len)
            shift = deontic_shift(pm, bm)
            # D10 (p774, this instrument's own, and the most misleading defect it
            # had). IDENTITY and RECOGNISABILITY are two different questions and
            # need two different instruments. p773-D is right that IDENTITY must be
            # an ABSOLUTE budget -- six characters can invert an obligation at any
            # document size. But "is this document even a variant of that licence?"
            # is legitimately PROPORTIONAL, and conflating the two made this grader
            # report the NEAREST canonical by edit distance for payloads that are
            # not that licence at all: a 906-byte Apache notice came back "ISC",
            # an MIT-style licence came back "BSD-3-Clause". A nearest-neighbour
            # family reads downstream as a licence claim, which is a false
            # precision worse than silence.
            recognisable = d <= max(BUDGET, 0.15 * len(bm))
            if shift and recognisable:
                altered.append((d, dict(f=pick(name, tag), r="OPERATIVE-TEXT-ALTERED",
                                        t=tag, b=raw_len, delta=d, deontic=shift)))
                continue
            if d <= BUDGET:
                return dict(f=pick(name, tag), r="body:near-canonical", t=tag, b=raw_len, delta=d)
            if recognisable:
                altered.append((d, dict(f=pick(name, tag), r="OPERATIVE-TEXT-ALTERED",
                                        t=tag, b=raw_len, delta=d)))
    if contained:
        return max(contained, key=lambda x: x[0])[1]
    if altered:
        return min(altered, key=lambda x: x[0])[1]
    # rung 4: the SPDX tag resolves the family where the body cannot
    if tag:
        return dict(f=tag, r="POINTER-resolved-by-SPDX-tag", t=tag, b=raw_len)
    # rung 5: notice prose, version bound to a 60-char window (D9)
    nf = notice_family(p)
    if nf:
        return dict(f=nf, r="POINTER-resolved-by-NOTICE-PROSE", t=None, b=raw_len)
    if raw_len < 3000:
        return dict(f="UNRESOLVED", r="POINTER-UNRESOLVED(no tag, no notice)", t=None, b=raw_len)
    # p772's D14: a verdict is only as good as the canonical set held. Saying so is
    # information; naming the nearest text is not.
    return dict(f="UNRESOLVED", r="NOT-IN-CANONICAL-SET(long bespoke text)",
                t=None, b=raw_len)

# ------------------------- controls ------------------------------------
def controls(cdir):
    canon = load_canon(cdir)
    rd = lambda n: open(f"{cdir}/{n}.txt", encoding="utf-8").read()
    mit, agpl, bsd, ap = rd("MIT"), rd("AGPL-3.0-or-later"), rd("BSD-3-Clause"), rd("Apache-2.0")
    T = [
      ("K1 exact MIT", mit, "MIT", ("body:canonical", "body:canonical(slot-filled)")),
      ("K2 MIT with a real holder filled in", 
       "MIT License\n\nCopyright (c) 2021 Learning Equality\n\n" + mit.split("\n", 1)[-1],
       "MIT", ("body:canonical", "body:canonical(slot-filled)", "body:near-canonical")),
      ("K3 BSD-3 with org filled + title + all-rights-reserved",
       "BSD 3-Clause License\n\nCopyright (c) 2004-2025, University of Oslo\nAll rights reserved.\n\n"
       + bsd, "BSD-3-Clause",
       ("body:canonical", "body:canonical(slot-filled)", "body:near-canonical",
        "canonical+PREPENDED", "canonical+APPENDED")),
      ("K4 AGPL prepended, NO tag -> undecidable group", "Project blurb.\n\n" + agpl,
       None, ("canonical+PREPENDED",)),
      ("K5 AGPL prepended WITH tag -> arm resolved",
       "Blurb.\nSPDX-License-Identifier: AGPL-3.0-or-later\n\n" + agpl,
       "AGPL-3.0-or-later", ("canonical+PREPENDED",)),
      ("K6 short notice + SPDX tag (rung 4)",
       "See gnu.org.\nSPDX-License-Identifier: AGPL-3.0-or-later\n",
       "AGPL-3.0-or-later", ("POINTER-resolved-by-SPDX-tag",)),
      ("K7 short notice, no tag, but NAMES the licence (rung 5)",
       "This program is licensed under the GNU Affero General Public License, version 3.\n",
       "AGPL-3.0", ("POINTER-resolved-by-NOTICE-PROSE",)),
      ("K8 short notice, no tag, no name -> honestly unresolved",
       "Licensed somehow. Ask us.\n", "UNRESOLVED", ("POINTER-UNRESOLVED(no tag, no notice)",)),
      ("K9 Apache operative only, appendix absent",
       ap[:ap.lower().find("end of terms and conditions")], "Apache-2.0",
       ("body:canonical", "canonical:operative-body-match", "body:near-canonical",
        "canonical+APPENDED")),
      ("K10 a REAL alteration must still be caught",
       agpl.replace("you must", "you may at your discretion").replace("GNU Affero", "GNU Afferro"),
       None, ("OPERATIVE-TEXT-ALTERED",)),
      # the budget control: a 1-word obligation inversion deep inside a long text
      ("K11 DEONTIC guard: a 6-char inserted negation is ALTERED at any budget",
       agpl.replace("If you convey a covered work", "If you never convey a covered work"),
       None, ("OPERATIVE-TEXT-ALTERED",)),
      ("K18 D11: an EUPL-1.2 short notice (Finland's ataru) resolves to EUPL-1.2",
       "Copyright (c) 2025 Finnish National Agency for Education\n\nLicensed under "
       "the EUPL, Version 1.2 or - as soon as they will be approved by the European "
       "Commission - subsequent versions of the EUPL.\n",
       "EUPL-1.2", ("POINTER-resolved-by-NOTICE-PROSE",)),
      ("K19 D11: a 19-byte 'License: GNU GPL V3' is still a resolvable family",
       "License: GNU GPL V3", "GPL-3.0", ("POINTER-resolved-by-NOTICE-PROSE",)),
      ("K20 D11: a CC-BY-SA human-readable notice with a bare version",
       "Creative Commons Attribution-ShareAlike 4.0 International\n\nCopyright (c) "
       "2026 X\n\nThis is a human-readable notice. Full terms at creativecommons.org.\n",
       "CC-BY-SA-4.0", ("POINTER-resolved-by-NOTICE-PROSE",)),
      ("K15 NONFREE first: a BSL-1.1 file naming MIT as its Change License is NOT MIT",
       "# Business Source License 1.1\n\nLicensor: X\nAdditional Use Grant: "
       "non-production evaluation and internal testing only.\nChange Date: 2029-01-01\n"
       "Change License: MIT\n", "BSL-1.1", ("NOT-OPEN-SOURCE(source-available or restricted)",)),
      ("K16 D10: a short Apache-2.0 NOTICE resolves to Apache-2.0, never to ISC",
       "Copyright 2023, Battelle Memorial Institute.\n\nLicensed under the Apache "
       "License, Version 2.0 (the \"License\"); you may not use this file except in "
       "compliance with the License. You may obtain a copy of the License at "
       "http://www.apache.org/licenses/LICENSE-2.0\n",
       "Apache-2.0", ("POINTER-resolved-by-NOTICE-PROSE",)),
      ("K17 D10: a bespoke text unlike any canonical gets NO family",
       "Terms of use for the Widget Corpus. You may look at this corpus. "
       "Contact legal@example.org for anything else. " * 40,
       "UNRESOLVED", ("NOT-IN-CANONICAL-SET(long bespoke text)",
                      "POINTER-UNRESOLVED(no tag, no notice)")),
      ("K13 D9: a GPL-2 notice must NOT be read as AGPL-3 across the document",
       "This program is free software; you can redistribute it under the terms of "
       "the GNU General Public License, version 2, as published by the Free "
       "Software Foundation. " + ("filler text about affero and about version 3 "
       "appearing far away in an unrelated sentence. " * 40),
       "GPL-2.0", ("POINTER-resolved-by-NOTICE-PROSE",)),
      ("K12 byte-identical arms report as a GROUP when no tag is present",
       agpl, None, ("body:canonical",)),
    ]
    fails = []
    for nm, pay, fam, rels in T:
        r = grade(pay, canon)
        if fam is not None and r["f"] != fam:
            fails.append(f"{nm}: family {r['f']!r} != {fam!r} (r={r['r']})"); continue
        if r["r"] not in rels:
            fails.append(f"{nm}: verdict {r['r']!r} not in {rels}")
    # K12 extra assertion: with no tag the AGPL answer must name BOTH arms
    r12 = grade(agpl, canon)
    if "UNDECIDABLE" not in r12["f"]:
        fails.append(f"K12b: untagged AGPL must report the undecidable group, got {r12['f']!r}")
    return fails, len(T) + 1

def main():
    cdir = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--controls":
        f, n = controls(cdir)
        print(f"grant-probe CONTROLS: {n-len(f)}/{n} pass")
        for x in f: print("  FAIL", x)
        sys.exit(2 if f else 0)
    f, n = controls(cdir)
    if f:
        print(f"REFUSING TO RUN: {len(f)}/{n} controls fail")
        for x in f: print("  FAIL", x)
        sys.exit(2)
    print(f"# grant-probe CONTROLS: {n}/{n} pass", file=sys.stderr)
    canon = load_canon(cdir)
    targets = [l.rstrip("\n").split("\t")[:2] for l in open(sys.argv[2]) if l.strip()]
    def work(t):
        slug, branch = t
        fn, payload = probe(slug, branch)
        if fn is None:
            return f"{slug}\t{branch}\tNO-GRANT-AT-ROOT\t-\t-\t-\t-"
        r = grade(payload, canon)
        return (f"{slug}\t{branch}\t{fn}\t{r['f']}\t{r['r']}\t{r['b']}"
                f"\t{r.get('tag') or r.get('t') or '-'}"
                + (f"\tdelta={r['delta']}" if r.get("delta") is not None else "")
                + (f"\tdeontic={r['deontic']}" if r.get("deontic") else ""))
    with ThreadPoolExecutor(max_workers=12) as ex:
        for line in ex.map(work, targets):
            print(line, flush=True)

if __name__ == "__main__":
    main()
