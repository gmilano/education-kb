#!/usr/bin/env python3
"""P118 ACTION E repair. Rewrites the licence token in exactly the rows the sweep
scored WRONG, and nowhere else.

Driven by verdict2.*.tsv, so the repair cannot touch a row the measurement did
not reach. The two addresses whose WRONG verdict is this instrument's own fault
(microsoft/autogen and bncc-dev/bncc-pacotes, both split-licence repositories
where the KB's MIT is right for the CODE) are excluded by name and corrected in
prose instead -- an automated repair must never propagate a known false verdict.
"""
import sys, re, collections

EXCLUDE = {"microsoft/autogen", "bncc-dev/bncc-pacotes"}
# The KB's own colour grammar: green permissive, red copyleft, amber content terms.
MARK = {"MIT": "🟢", "Apache-2.0": "🟢", "BSD": "🟢", "BSD-3": "🟢", "ECL-2.0": "🟢",
        "MPL-2.0": "🟢", "ISC": "🟢", "Unlicense": "🟢",
        "AGPL-3.0": "🔴", "GPL-3.0": "🔴", "GPL-2.0": "🔴", "LGPL-3.0": "🟡",
        "CC-BY": "🟡", "CC0-1.0": "🟢",
        # Not open source at all: use restrictions, not just copyleft.
        "ElasticLicense-2.0-NOT-OSS": "🔴"}
TOKEN = re.compile(r"AGPL-3(?:\.0)?|LGPL-[0-9]+(?:\.[0-9]+)?|GPL-3(?:\.0)?|GPL-2(?:\.0)?"
                   r"|Apache-2(?:\.0)?|BSD-[234](?:-Clause)?|ECL-2(?:\.0)?|MPL-2(?:\.0)?"
                   r"|EPL-[12](?:\.0)?|CC-BY-SA|CC-BY-NC|CC-BY|CC0-1\.0|CC0|Unlicense|MIT|AGPL|LGPL|GPL|BSD")

# What goes in the table cell. "ElasticLicense-2.0-NOT-OSS" is the measurement's
# label; the cell says "Elastic-2.0 (not OSS)", which a reader skimming a licence
# column cannot mistake for a permissive grant.
DISPLAY = {"ElasticLicense-2.0-NOT-OSS": "Elastic-2.0 (not OSS)"}

def canon(t):
    m = re.fullmatch(r"(A?GPL|LGPL|Apache|ECL|MPL|EPL)-([0-9]+)", t)
    return f"{m.group(1)}-{m.group(2)}.0" if m else t

jobs = collections.defaultdict(list)
for ln in open(sys.argv[1]):
    f = ln.rstrip("\n").split("\t")
    if len(f) < 6 or f[0] != "WRONG":
        continue
    verdict, path, lineno, slug, toks, meas = f[0], f[1], int(f[2]), f[3], f[4], f[5]
    if slug in EXCLUDE or meas.startswith("MULTI-GRANT:"):
        continue
    jobs[path].append((lineno, slug, toks.split(","), meas))

dry = "--apply" not in sys.argv
total = skipped = 0
for path, rows in sorted(jobs.items()):
    lines = open(path, encoding="utf-8").read().split("\n")
    for lineno, slug, toks, meas in sorted(rows):
        orig = lines[lineno - 1]
        # Only rewrite a token that is NOT already the measured value, and only
        # one that the row actually published as this repo's licence.
        def sub(m):
            global total
            t = canon(m.group(0))
            if t == canon(meas) or t not in [canon(x) for x in toks]:
                return m.group(0)
            total += 1
            return DISPLAY.get(meas, meas)
        new = TOKEN.sub(sub, orig, count=1)
        if new == orig:
            skipped += 1
            print(f"  SKIP {path}:{lineno} {slug}")
            continue
        # Re-colour the marker immediately preceding the token we replaced.
        want = MARK.get(meas)
        if want:
            new = re.sub(r"[🟢🔴🟡🔵](\s*\**\s*)" + re.escape(DISPLAY.get(meas, meas)),
                         want + r"\g<1>" + DISPLAY.get(meas, meas), new, count=1)
        if dry:
            print(f"  {path}:{lineno} {slug}\n    - {orig.strip()[:150]}\n    + {new.strip()[:150]}")
        lines[lineno - 1] = new
    if not dry:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
print(f"\n{'DRY RUN' if dry else 'APPLIED'}: {total} tokens rewritten, {skipped} rows skipped")
