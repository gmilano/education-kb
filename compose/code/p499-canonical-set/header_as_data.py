#!/usr/bin/env python3
"""Header-row-as-data detector, third form (Gap 498-M, second half).

Form 1 (p498, naive): "first cell is Name/Repo/Licence."
   -> 100% false positive (40/40). That is what a legitimate HEADER looks like.
Form 2 (p499a, position-aware): "...and not followed by a |---| separator."
   -> still 48/48 false positive. This base uses TRANSPOSED property/value
      tables heavily, where a field name is a legitimate ROW LABEL:
          | | |
          |---|---|
          | licence | MIT |
Form 3 (this one): a leaked header row is one where EVERY cell is a bare field
      name -- "| Nombre | Repo | Licencia |" -- which is the actual defect the
      task description warns about. One field name plus a value is a row label.
"""
import re, sys, glob, tempfile, os

FIELD = re.compile(r'^(nombre|name|repo|repositorio|licencia|license|licence|agent|agente|'
                   r'platform|plataforma|example|ejemplo|placeholder|tbd|todo|xxx|'
                   r'descripcion|description|desc|layer|capa|stars|star|url|link|enlace|'
                   r'notes|notas|role|rol|why|type|tipo)$', re.I)

def cells(line):
    s = line.strip()
    if not (s.startswith('|') and s.endswith('|')):
        return None
    return [c.strip().strip('*`_ ') for c in s[1:-1].split('|')]

def scan(path):
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    hits, in_body, sep_seen = [], False, False
    for i, ln in enumerate(lines):
        c = cells(ln)
        if c is None:
            sep_seen = False
            continue
        if all(re.fullmatch(r'[:\-]{2,}|[:\-]?-+[:\-]?', x or '-') for x in c):
            sep_seen = True            # this is the |---| separator
            continue
        if not sep_seen:
            continue                   # header row (or pre-separator); not body
        named = sum(1 for x in c if x and FIELD.fullmatch(x))
        if named >= 2 and named == len([x for x in c if x]):
            hits.append((i + 1, ln[:120]))
    return hits

# ---- controls ----------------------------------------------------------
cases = {
  'known-good header+real row': ("| Name | Repo | Licence |\n|---|---|---|\n"
                                 "| Kolibri | learningequality/kolibri | MIT |\n", 0),
  'known-bad leaked header row': ("| Name | Repo | Licence |\n|---|---|---|\n"
                                  "| Nombre | Repo | Licencia |\n", 1),
  'known-good transposed labels': ("| | |\n|---|---|\n| licence | MIT |\n| repo | foo/bar |\n", 0),
}
ok = True
for label, (body, expect) in cases.items():
    fd, p = tempfile.mkstemp(suffix='.md'); os.write(fd, body.encode()); os.close(fd)
    got = len(scan(p)); os.unlink(p)
    flag = 'PASS' if got == expect else 'FAIL'
    if got != expect: ok = False
    print("CONTROL %-32s -> %d hits (expect %d)  %s" % (label, got, expect, flag))
if not ok:
    sys.exit("DETECTOR FAILED ITS CONTROLS -- results not trustworthy")
print("all 3 controls PASSED\n")

total = 0
for f in sorted(glob.glob('agents/*.md') + glob.glob('repos/*.md') + glob.glob('verticals/*.md')
                + glob.glob('intel/*.md') + glob.glob('compose/*.md') + ['README.md']):
    h = scan(f)
    if h:
        print("%s -- %d" % (f, len(h)))
        for ln, txt in h[:8]:
            print("   L%-6d %s" % (ln, txt))
    total += len(h)
print("\nTOTAL leaked header rows in a table body, across the live shelves: %d" % total)
