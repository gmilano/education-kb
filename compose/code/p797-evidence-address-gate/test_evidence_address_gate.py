#!/usr/bin/env python3
"""Offline controls for p797-evidence-address-gate (v3).

`p796-G`: the control set must span the population's KINDS. v1 of this gate had 21 controls
spanning 14 kinds, every one passed, and the gate was still wrong on 15,591 rows - because the
population held three kinds its author had not met (a URL in column 0, a prose sentence in
column 0, and a repository name legally ending in `-`). v2 met a fourth (a file path).

So these controls are written against v3's NARROWER contract, and the four kinds that broke v1
and v2 are present as MUST-PASS cases rather than as must-fail ones. A control that encodes an
abandoned predicate is worse than no control: it certifies the gate against a rule it no longer
claims to enforce.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence_address_gate import classify   # noqa: E402

CASES = [
    # (field, expect_ok, the KIND this control covers)
    ('HKUDS/DeepTutor',                  True,  'real address'),
    ('OS4ED/openSIS-Classic',            True,  'real address, dashed name'),
    ('h5p/h5p-php-library',              True,  'real address, multiple dashes'),
    ('european-commission-empl/European-Learning-Model', True, 'real address, dashed owner'),
    ('ILIAS-eLearning/ILIAS',            True,  'real address, mixed case'),
    ('DooWuy/AI-tutor-',                 True,  'KIND THAT BROKE v1: legal trailing dash'),
    ('alguarito/Conciencia-',            True,  'KIND THAT BROKE v1: legal trailing dash, 2'),
    ('shivanandmn/saint_plus-knowledge-tracing-', True, 'KIND THAT BROKE v1: underscore + dash'),
    ('https://github.com/moodle/moodle', True,  'KIND THAT BROKE v1: URL-form address'),
    ("The Ministere de l'Education published a 2026 edition of its guide", True,
     'KIND THAT BROKE v1: prose sentence in column 0'),
    ('OWNER/REPO',                       True,  'DELIBERATE NEGATIVE CONTROL - must survive'),
    ('owner/repo',                       True,  'prose-literal census row - must survive'),
    ('addr',                             True,  'header'),
    ('slug',                             True,  'header'),
    ('total',                            True,  'aggregate label'),
    ('',                                 True,  'empty column 0'),
    ('LICENSE',                          True,  'bare token, not an address'),
    ('NEW/ArnaudGuiovanna/tutor-mcp',    False, 'THE DEFECT - status marker on an address'),
    ('NEW/Ebimsv/AITutorAgent',          False, 'THE DEFECT, second instance'),
    ('NEW/rohitg00/ai-engineering-from-scratch', False, 'THE DEFECT, third instance'),
    ('CARRIED/moodle/moodle',            False, 'THE DEFECT, a different marker word'),
]

# The three kinds that broke v2 - a file path, a repo-local path, an `owner/repo/ref/path` - are
# excluded by SCOPE, not by the predicate, so they are controlled at the sweep level below. A
# control asserted at the wrong level is the defect `T921` describes: it certifies the artefact
# rather than the claim.
PATH_KINDS = [
    'modules/text/module_text_llm/pyproject.toml',
    'compose/code/p230-prose-path-ladder/probe.sh',
    'Scorpioyyy/verichalk/main/LICENSE',
]

fails = 0
for field, expect, kind in CASES:
    ok, why = classify(field)
    if ok != expect:
        print('RED %s: %r -> ok=%s (%s), expected ok=%s' % (kind, field, ok, why, expect))
        fails += 1
# SCOPE controls. Two fixture files, identical rows, different headers.
import tempfile                                                            # noqa: E402
from evidence_address_gate import sweep                                     # noqa: E402

with tempfile.TemporaryDirectory() as td:
    ev = os.path.join(td, 'evidence')
    os.makedirs(ev)
    with open(os.path.join(ev, 'declared.tsv'), 'w') as fh:
        fh.write('repo\tx\n')
        for row in PATH_KINDS + ['NEW/ArnaudGuiovanna/tutor-mcp']:
            fh.write(row + '\t1\n')
    with open(os.path.join(ev, 'undeclared.tsv'), 'w') as fh:
        fh.write('path\tx\n')
        for row in PATH_KINDS + ['NEW/ArnaudGuiovanna/tutor-mcp']:
            fh.write(row + '\t1\n')
    _all, in_scope, bad = sweep(td)
    if len(in_scope) != 1:
        print('RED scope control: %d files in scope, expected 1 (the `repo` header only)'
              % len(in_scope))
        fails += 1
    flagged = {b[2] for b in bad}
    if 'NEW/ArnaudGuiovanna/tutor-mcp' not in flagged:
        print('RED scope control: the status-marker row was not caught inside a declared file')
        fails += 1
    # NOT asserted: that a path-shaped row survives INSIDE a declared file. It does not - the
    # predicate cannot tell `Scorpioyyy/verichalk/main/LICENSE` from `NEW/owner/repo` by shape,
    # and pretending otherwise would be the false claim v2 made. What bounds this gate is the
    # measured fact that no declared-address file in this base contains one: 696 files in scope,
    # 0 violations once the 18 status-marker rows were fixed. That is a MEASUREMENT, and if a
    # future pass adds a declared-address file carrying `owner/repo/ref/path` rows, this gate
    # will go red and should: that column would be lying about what it holds.
    undeclared_rows = [b for b in bad if 'undeclared' in b[0]]
    if undeclared_rows:
        print('RED scope control: %d row(s) judged in a file that never declared an address '
              'column' % len(undeclared_rows))
        fails += 1

print('-- p797-evidence-address-gate controls: %d field cases + 3 scope assertions over 2 fixture '
      'files; 4 of the kinds present are ones that broke an earlier version' % len(CASES))
if fails:
    print('RED %d control(s) failed' % fails)
    sys.exit(1)
print('   PASS')
