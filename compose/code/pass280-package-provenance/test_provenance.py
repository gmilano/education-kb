#!/usr/bin/env python3
"""Offline controls for `pass280-package-provenance`.  No network, so `make hooks` runs them.

Every control whose subject is a REAL repository reads a CAPTURED payload from
`fixtures/`, with `slug/ref/head_sha/bytes/sha256/date` in `fixtures/PROVENANCE.tsv`.
That is this instrument's own finding applied to itself: `p280` was built because four
controls in `p229` asserted payloads their repositories do not serve.

The controls that MUST NOT fire are the point.  A vendoring predicate that rejects a
monorepo's own workspace packages destroys the very count it was added to protect --
`p279` measured exactly that when `T229-M2`'s name check rejected 12 of `Athena`'s 14.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import provenance as pr          # noqa: E402

FIX = os.path.join(HERE, 'fixtures')
FAILED = []
CHECKS = [0]


def payload(name):
    try:
        return open(os.path.join(FIX, name), encoding='utf-8').read()
    except OSError as e:
        FAILED.append('fixture %s unreadable: %s' % (name, e))
        return ''


def check(name, got, expect):
    CHECKS[0] += 1
    ok = got == expect
    if not ok:
        FAILED.append('%s: got %r expected %r' % (name, got, expect))
    print('%s %-66s %s' % ('ok  ' if ok else 'FAIL', name,
                           '' if ok else '-> %r != %r' % (got, expect)))


def verdict(slug, path, body):
    return pr.classify(slug, path, body)[0]


print('-- THE RESIDUAL p279 DECLARED UNREACHABLE (the positive control) --')
# `p279`: "the residual is named: `ui/static/pyodide/`, which no path convention reaches.
# The durable channel reads a package `name` against a list of known third-party projects,
# and this base has no such list."  It needs no list: the payload names its own repository.
check('pyodide under ui/static/ is THIRD-PARTY (declared repository, no list)',
      verdict('Open-TutorAi/open-tutor-ai-CE', 'ui/static/pyodide/package.json',
              payload('open-tutor-ai-CE.pyodide.package.json')), 'THIRD-PARTY')
check('...and the repository it declares is recorded, not guessed',
      pr.classify('Open-TutorAi/open-tutor-ai-CE', 'ui/static/pyodide/package.json',
                  payload('open-tutor-ai-CE.pyodide.package.json'))[2], 'pyodide/pyodide')
check('...and its Apache-2.0 is the ARTEFACT licence p121/p278 typed by hand',
      pr._declares_licence('ui/static/pyodide/package.json',
                           payload('open-tutor-ai-CE.pyodide.package.json')), 'Apache-2.0')

print('\n-- THE NEGATIVE CONTROLS: a workspace package is NOT vendored --')
# 🔴 `p279`'s measured disaster: the name check at depth rejected 12 of Athena's 14.  The
# same shape here would be silent and would shrink every monorepo's declaration count.
check('the repo own ui/ subpackage (private, no repository field) is OWN-SUBPACKAGE',
      verdict('Open-TutorAi/open-tutor-ai-CE', 'ui/package.json',
              payload('open-tutor-ai-CE.ui.package.json')), 'OWN-SUBPACKAGE')
check('a subpackage DECLARING its own repository is OWN-DECLARED',
      verdict('codelitdev/courselit', 'packages/text-editor/package.json',
              '{"name":"@courselit/text-editor","repository":'
              '"https://github.com/codelitdev/courselit","license":"MIT"}'), 'OWN-DECLARED')
check('a subpackage whose name merely DIFFERS is not vendored',
      verdict('ls1intum/Athena', 'assessment_module_manager/package.json',
              '{"name":"assessment_module_manager","license":"MIT"}'), 'OWN-SUBPACKAGE')

print('\n-- THE ROOT IS RECORDED, NEVER ENFORCED (p279) --')
# 🟢 And the declared channel SETTLES one of the four cases `p279` could only record: the
# root name differs AND the manifest declares this very repository, in two fields.
check('mcp-canvas-lms root: canvas-mcp-server, but it DECLARES this repository',
      verdict('DMontgomery40/mcp-canvas-lms', 'package.json',
              payload('mcp-canvas-lms.root.package.json')), 'OWN-DECLARED')
check('...which is the name T229-M2 refuses to attribute, on the same bytes',
      pr.attributable('DMontgomery40/mcp-canvas-lms', 'package.json',
                      payload('mcp-canvas-lms.root.package.json'))[0], False)
check('a root manifest naming another project and declaring NOTHING stays RECORDED',
      verdict('alfredang/ai-mms', 'composer.json',
              payload('ai-mms.root.composer.json')), 'ROOT-NAME-DIFFERS')
check('...the laravel skeleton too -- a root FOREIGN verdict is never enforced here',
      verdict('LMS-Laravel/LMS-Laravel', 'composer.json',
              payload('LMS-Laravel.root.composer.json')), 'ROOT-NAME-DIFFERS')
check('a root declaring a DIFFERENT repository is ROOT-FOREIGN-DECLARED, not THIRD-PARTY',
      verdict('someone/fork-of-pyodide', 'package.json',
              payload('open-tutor-ai-CE.pyodide.package.json')),
      'ROOT-FOREIGN-DECLARED')

print('\n-- THE FLOOR LIST, and the bound on it --')
check('a vendored manifest with NO repository field falls to the name floor',
      verdict('a/b', 'public/assets/js/package.json',
              '{"name":"ckeditor5","license":"GPL-2.0-or-later"}'), 'THIRD-PARTY-NAMED')
check('a scoped third-party name is caught by its SCOPE',
      verdict('a/b', 'vendored/package.json',
              '{"name":"@ckeditor/ckeditor5-build-classic"}'), 'THIRD-PARTY-NAMED')
check('🔴 the floor cannot reach a name nobody enumerated -- and says so',
      verdict('a/b', 'static/leaflet/package.json', '{"name":"leaflet"}'),
      'OWN-SUBPACKAGE')
check('the floor NEVER fires at the root, whatever the name',
      verdict('a/b', 'package.json', '{"name":"pyodide"}'), 'ROOT-NAME-DIFFERS')

print('\n-- URL FORMS: agreement with lib/package_repo.sh, not a second parser --')
for url, want in (('git+https://github.com/DMontgomery40/mcp-canvas-lms.git',
                   'DMontgomery40/mcp-canvas-lms'),
                  ('https://github.com/pyodide/pyodide', 'pyodide/pyodide'),
                  ('git://github.com/o/r.git', 'o/r'),
                  ('https://github.com/o/r/tree/main/packages/x', 'o/r'),
                  ('https://github.com/o/r#readme', 'o/r')):
    check('declared_repo reads %s' % url,
          pr.declared_repo('package.json', '{"repository":{"url":"%s"}}' % url), want)
check('a GitLab source is a real declaration this channel cannot COMPARE',
      pr.declared_repo('package.json', '{"repository":"https://gitlab.com/o/r"}'),
      'NON-GITHUB')
check('silence is not a counter-claim (T229-M2, carried)',
      pr.declared_repo('package.json', '{"name":"x","license":"MIT"}'), None)

print('\n-- the pyproject/pom families --')
check('pyproject [project.urls] Repository is read',
      pr.declared_repo('pyproject.toml',
                       '[project.urls]\nRepository = "https://github.com/o/r"\n'), 'o/r')
check('a DEPENDENCY url on a non-url line is not a declaration',
      pr.declared_repo('pyproject.toml',
                       'dependencies = ["x @ https://github.com/other/dep"]\n'), None)
check('pom <scm><url> is read',
      pr.declared_repo('pom.xml', '<scm><url>https://github.com/o/r</url></scm>'), 'o/r')

print('\n-- the enforceable set is CLOSED (a walk may act on these two and no others) --')
check('ENFORCEABLE is exactly the two THIRD-PARTY verdicts',
      pr.ENFORCEABLE, ('THIRD-PARTY', 'THIRD-PARTY-NAMED'))
check('is_third_party agrees with classify on the residual',
      pr.is_third_party('Open-TutorAi/open-tutor-ai-CE', 'ui/static/pyodide/package.json',
                        payload('open-tutor-ai-CE.pyodide.package.json')), True)
check('is_third_party does NOT fire on a root name difference',
      pr.is_third_party('alfredang/ai-mms', 'composer.json',
                        payload('ai-mms.root.composer.json')), False)

print('\n-- every fixture a control reads has recorded provenance --')
prov = os.path.join(FIX, 'PROVENANCE.tsv')
rows = [l.split('\t') for l in open(prov, encoding='utf-8').read().splitlines()[1:] if l]
named = {r[4] for r in rows if len(r) > 4}
on_disk = {f for f in os.listdir(FIX) if f != 'PROVENANCE.tsv'}
check('no fixture without a PROVENANCE row', sorted(on_disk - named), [])
check('no PROVENANCE row without a fixture', sorted(named - on_disk), [])
check('every row carries a head_sha', [r[0] for r in rows if len(r) < 3 or r[2] == '-'], [])

print('\n%d checks, %d failed' % (CHECKS[0], len(FAILED)))
for f in FAILED:
    print('   🔴 %s' % f)
sys.exit(1 if FAILED else 0)
