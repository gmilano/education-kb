#!/usr/bin/env python3
"""p779 named gate: gate-refs.

T804 established that a licence grade is unfalsifiable without `branch` · `HEAD`
cited beside it: without a ref, a reader cannot go back to the same tree and
re-read the same bytes. This gate does NOT re-grade anything. It measures how
large the unfalsifiable population is, per shelf, so the next pass knows whether
the branch-and-HEAD convention is real or aspirational.

A row is LICENCE-ASSERTING if it is a table row (leading `|`, not a separator,
not a header) and carries either
  (a) a POSITIVE grade: a licence identifier in LICENCE FORM, or
  (b) an ABSENCE grade: NO-GRANT / NONE-at-root style wording.
These are counted and reported separately, because an absence grade depends even
more sharply on which tree was read.

MIT is matched per the p778-F specification: it must appear in licence form
(`MIT License`, `MIT`, **MIT**, MIT-0) and the institutional uses
(mitodl, MIT Open Learning, MIT Media Lab, MIT App Inventor, "Harvard and MIT")
are excluded, because those are the one real extractor defect p778 left behind.

A row is FALSIFIABLE if it cites a ref: a backticked ref-like name followed by
` · ` and a backticked 12-hex code. The 12-hex body digest that follows a byte
count (`1,102 B` · `97952c3f6069`) is deliberately NOT accepted as a ref — it
identifies the blob, not the tree it was read from.
"""
import re, sys, os

SHELVES = ["README.md","agents/top.md","agents/trending.md","compose/patterns.md",
           "intel/market.md","intel/measured-unusable.md","intel/open-gaps.md",
           "intel/trends.md","repos/foundations.md","repos/trending.md",
           "verticals/solutions.md"]

# Positive licence identifiers, in licence form.
LIC = re.compile(r"""(?xi)
    \b(?: Apache-2\.0 | AGPL-3\.0(?:-only|-or-later)? | LGPL-(?:2\.1|3\.0)(?:-only|-or-later)?
        | GPL-(?:2\.0|3\.0)(?:-only|-or-later)? | BSD-(?:2|3|4)-Clause | MPL-2\.0
        | EPL-(?:1\.0|2\.0) | ECL-2\.0 | CDDL-1\.[01] | CECILL-2\.1 | Unlicense | ISC
        | CC0-1\.0 | CC-BY(?:-SA|-NC|-ND)*-[34]\.0 | Zlib | MS-PL | OSL-3\.0
        | NOASSERTION | Artistic-2\.0 | EUPL-1\.[12] | BSL-1\.0 | PostgreSQL
    )\b""")
MIT_LIC = re.compile(r"(?i)\bMIT(?:\s+Licen[cs]e|-0)?\b")
MIT_INSTITUTION = re.compile(r"(?i)mitodl|MIT\s+Open\s+Learning|MIT\s+Media\s+Lab|"
                             r"MIT\s+App\s+Inventor|Harvard\s+and\s+MIT|MIT\s+Sloan|"
                             r"MIT\s+Press|MIT\s+OpenCourseWare|MIT\s+Solve")
ABSENCE = re.compile(r"(?i)NO-GRANT|NO\s+GRANT|no\s+licen[cs]e\s+at\s+root|NONE-at-root")

# `ref` · `12hex` where ref is a ref name, not a byte count.
REFCITE = re.compile(r"`([A-Za-z][A-Za-z0-9._/\-]*)`\s*·\s*`([0-9a-f]{12})`")
BYTECOUNT = re.compile(r"(?i)^[\d,\.]+\s*(B|kB|KiB|MB)$")

def mit_in_licence_form(cell):
    stripped = MIT_INSTITUTION.sub(" ", cell)
    return bool(MIT_LIC.search(stripped))

def has_ref(row):
    for name, sha in REFCITE.findall(row):
        if not BYTECOUNT.match(name):
            return True
    return False

def classify(row):
    pos = bool(LIC.search(row)) or mit_in_licence_form(row)
    neg = bool(ABSENCE.search(row))
    return pos, neg

def is_data_row(line):
    s = line.strip()
    if not s.startswith("|"):
        return False
    if re.fullmatch(r"\|[\s\-:|]+\|", s):      # separator
        return False
    return True

def run(root, verbose=False):
    tot = {"pos":0,"neg":0,"pos_ok":0,"neg_ok":0}
    rows = []
    print(f"{'shelf':<30} {'lic rows':>8} {'with ref':>9} {'UNFALS':>7} {'absence':>8} {'abs+ref':>8} {'UNFALS':>7}")
    print("-"*86)
    for sh in SHELVES:
        p = os.path.join(root, sh)
        if not os.path.exists(p):
            print(f"{sh:<30} {'MISSING':>8}"); continue
        P=N=PO=NO=0
        for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
            if not is_data_row(line): continue
            pos, neg = classify(line)
            if not (pos or neg): continue
            r = has_ref(line)
            if pos:
                P += 1
                if r: PO += 1
                else: rows.append((sh,i,"positive",line.strip()[:150]))
            if neg:
                N += 1
                if r: NO += 1
                else: rows.append((sh,i,"absence",line.strip()[:150]))
        print(f"{sh:<30} {P:>8} {PO:>9} {P-PO:>7} {N:>8} {NO:>8} {N-NO:>7}")
        tot["pos"]+=P; tot["pos_ok"]+=PO; tot["neg"]+=N; tot["neg_ok"]+=NO
    print("-"*86)
    print(f"{'TOTAL':<30} {tot['pos']:>8} {tot['pos_ok']:>9} {tot['pos']-tot['pos_ok']:>7} "
          f"{tot['neg']:>8} {tot['neg_ok']:>8} {tot['neg']-tot['neg_ok']:>7}")
    den = tot['pos']+tot['neg']; num = tot['pos_ok']+tot['neg_ok']
    if den:
        print(f"\nfalsifiable share: {num}/{den} = {100.0*num/den:.1f}%")
    if verbose:
        print("\n--- sample unfalsifiable rows ---")
        for sh,i,k,t in rows[:25]:
            print(f"{sh}:{i} [{k}] {t}")
    return tot, rows

if __name__ == "__main__":
    run(sys.argv[1], "-v" in sys.argv)
