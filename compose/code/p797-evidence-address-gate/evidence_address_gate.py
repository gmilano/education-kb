#!/usr/bin/env python3
"""p797 - ACTION p796-E, with the action's premise CORRECTED by its own census, twice.

`p796` queued this as "clean the placeholder out of the published evidence set, then gate it",
naming `OWNER/REPO` and six `NEW/`-prefixed addresses, and proposing a gate that rejects `OWNER`,
`REPO`, `NEW` and `EXAMPLE` as literals.

CENSUS, FIRST CORRECTION - 47 candidate rows in 24 of the 2,093 evidence files, and read, they
are three different things of which one is a defect:

  1. HEADER rows and PROSE-LITERAL census rows. `address-census.2026-11-12-p781.tsv` lines 109
     and 625 carry `owner/repo  24` and `OWNER/REPO  6`: not placeholders, COUNTS of how often
     those literals occur in this base's own markdown. Correct data about a real problem.
  2. DELIBERATE NEGATIVE CONTROLS. `existence-three-state.2026-11-12-p794.tsv:41` is
     `OWNER/REPO  ABSENT  128  0  0` - the negative control `p796`'s own README cites approvingly
     ("with a NEGATIVE control that fails as required"). The gate `p796` specified would have
     deleted it.
  3. A REAL defect, 6 rows in 3 files: a STATUS MARKER glued onto the address -
     `NEW/ArnaudGuiovanna/tutor-mcp`. Three segments, so no consumer can resolve it. The rows
     carry real measurements, so the fix is to STRIP the prefix, not to delete the row.

SECOND CORRECTION, AND THE ONE WORTH KEEPING - three predicates in a row over-reported, and the
scope was the problem, not the predicate:
  * v1 asserted what an address field may CONTAIN: 15,591 rows where 6 are real (2,598x). Three
    false-alarm classes, all legitimate content - a URL in column 0 (a whole family of evidence
    files records addresses that way), a prose sentence in column 0 (the narrative artefacts),
    and a repository name ending in `-`, `.` or `_`, which is LEGAL on GitHub (12 real rows).
  * v2 asserted only that an `owner/name` may not wear a leading segment: 5,093 rows (849x),
    because a file PATH has the same shape - `modules/text/module_text_llm/pyproject.toml`,
    `compose/code/p230-prose-path-ladder/probe.sh`, `owner/repo/branch/LICENSE`.
  * v3 keys on the DECLARED HEADER instead. A file whose column 0 is headed `repo`, `addr`,
    `slug`, `address` or `repository` has promised what that column holds, and only there is a
    three-segment value a defect rather than a path.
All 21 of v1's controls passed, and all 21 pass here too, which is the point: `p796-G` says the
control set must span the population's KINDS, and a control set cannot span kinds the author has
not met. What bounded this gate was not a better predicate but a SMALLER, DECLARED scope.

No network. Exit 1 on any violation.
"""
import os
import re
import sys
import glob

# GitHub's real repository-name grammar. It ALLOWS a trailing `-`, `.` or `_`.
NAME = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$')
SCHEME_OR_HOST = re.compile(
    r'^(https?:|github\.com|www\.|[a-z0-9.-]+\.(com|org|net|io|dev|edu))$')


ADDRESS_HEADERS = {'repo', 'addr', 'address', 'slug', 'repository'}


def classify(field):
    """-> (ok, reason). Applied ONLY to a file that declares column 0 to be an address."""
    if field == '':
        return True, 'empty'
    parts = field.split('/')
    if len(parts) < 3:
        return True, 'bare-token-or-address'
    if any(p == '' for p in parts):
        return True, 'path-form'
    if SCHEME_OR_HOST.match(parts[0]) or parts[0].endswith(':'):
        return True, 'url-form-address'
    owner, name = parts[-2], parts[-1]
    if NAME.match(owner) and NAME.match(name) and ' ' not in field and len(field) < 120:
        return False, 'status-marker-prefix:' + parts[0]
    return True, 'prose-or-path'


def sweep(root):
    """Only files whose first line declares column 0 to be a repository address are in scope."""
    bad = []
    files = sorted(glob.glob(os.path.join(root, 'evidence', '*.tsv')))
    in_scope = []
    for fn in files:
        with open(fn, errors='replace') as fh:
            try:
                header = next(fh)
            except StopIteration:
                continue
            if header.split('\t')[0].strip().lower() not in ADDRESS_HEADERS:
                continue
            in_scope.append(fn)
            for ln, line in enumerate(fh, 2):
                field = line.split('\t')[0].strip()
                ok, why = classify(field)
                if not ok:
                    bad.append((os.path.relpath(fn, root), ln, field, why))
    return files, in_scope, bad


if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
    files, in_scope, bad = sweep(root)
    print('-- p797-evidence-address-gate: %d evidence files, %d declare column 0 an address'
          % (len(files), len(in_scope)))
    if bad:
        print('RED %d address field(s) carrying a status-marker prefix:' % len(bad))
        for fn, ln, field, why in bad[:60]:
            print('   %s:%d  %r  - %s' % (fn, ln, field, why))
        sys.exit(1)
    print('GREEN PASS - no published address wears a status marker')
