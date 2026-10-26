#!/usr/bin/env python3
"""p452 — Gap 450-C: extract every carried LICENSE/COPYING byte-count cell.

p450 registered the open question: "how many byte counts already on these shelves
were produced by the uncorrected method?" (command substitution strips a trailing
newline, so every such cell runs exactly ONE byte low). Answering it needs the
carried population, and this is the extractor.

🔴 It took FOUR cuts, and every wrong cut produced a confident phantom-drift list:

  cut 1  `(\\d(?:SEP?\\d{3})*)` — unanchored, separator OPTIONAL: on "11 408 B" the
         engine skipped the leading digit and returned 1408. 200/395 phantom drifts.
         Caught only because a hand-written control row said DeepTutor is 11 408 B.
  cut 2  added a negative lookbehind and a mandatory separator — but the separator
         class held only SPACES. On "1,070 B" it matched "070". 104 phantom drifts,
         all of them exactly +1000, +11000, +35000 — the shape of a lost leading group.
  cut 3  added the comma. One cell still failed: "**1.071 B**", a PERIOD separator.
  cut 4  this file.

🟢 The underlying finding, which is why no earlier pass built this census: across 451
passes the shelves group thousands FOUR different ways — U+202F narrow no-break space,
plain space, comma, and period. Any single-separator reader silently truncates the
others and reports the truncation as upstream drift.

🟢 Only lines naming exactly ONE address are used: pairing a byte count with one of
several addresses on a line is a guess, and `Gap 451-A` is precisely about not
treating a guess as evidence.
"""
import re, sys

SEP = '[    ,.]'
NUM = r'(?<![\d,.   ])(\d{1,3}(?:' + SEP + r'\d{3})+|\d+)'
SLUG = re.compile(r'github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+?)(?:[)\s`,.]|$)')
BYTES = re.compile(
    r'`?(LICENSE[A-Za-z0-9._-]*|COPYING[A-Za-z0-9._-]*|license\.html)`?,?'
    r'[^|\n]{0,40}?\*{0,2}' + NUM + SEP + r'?B\b')

def extract(files):
    seen = {}
    for f in files:
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            slugs = SLUG.findall(line)
            if not slugs:
                continue
            cells = BYTES.findall(line)
            if not cells:
                continue
            uniq = {f"{o}/{r}" for o, r in slugs}
            if len(uniq) != 1:
                continue
            slug = uniq.pop()
            for path, num in cells:
                n = int(re.sub(r'[^0-9]', '', num))
                seen.setdefault((slug, path), (n, f, i))
    return seen

# Self-check, run on import: eight cells read by hand out of the shelf text, chosen to
# cover all four separators. A reader that cannot reproduce these must not be trusted
# to report drift — cuts 1-3 each passed a SUBSET of them, which is why all eight run.
CHECKS = [("HKUDS/DeepTutor", "LICENSE", 11408),
          ("learningequality/kolibri", "LICENSE", 1097),
          ("FiredMosquito831/ase-moodle-mcp", "LICENSE", 11358),
          ("withmarbleapp/os-taxonomy", "LICENSE", 25289),
          ("gradescope/gradescope-utils", "LICENSE", 1070),
          ("ucfopen/canvasapi", "LICENSE", 1130),
          ("vishalsachdev/canvas-mcp", "LICENSE", 1071),
          ("moodle/moodle", "COPYING.txt", 35147)]

if __name__ == "__main__":
    files = sys.argv[1:]
    seen = extract(files)
    bad = [(s, p, w, seen.get((s, p), (None,))[0]) for s, p, w in CHECKS
           if seen.get((s, p), (None,))[0] != w]
    for s, p, w, got in bad:
        print(f"SELF-CHECK FAIL {s} {p}: got {got}, want {w}", file=sys.stderr)
    if bad:
        sys.exit(1)
    print(f"self-check 8/8 OK; extracted {len(seen)} cells", file=sys.stderr)
    for (slug, path), (n, f, i) in seen.items():
        print(f"{slug}\t{path}\t{n}\t{f}:{i}")
