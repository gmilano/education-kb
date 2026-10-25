"""p428 — controls for the branch-alias grader.

Every ref set in `fixtures/` is a `git ls-remote --heads` capture this pass took
FIRST-HAND on 2026-10-25.  Nothing here is synthesised except the three citation
strings marked SYNTHETIC, which exercise shapes the live corpus does not carry.

Runs from this directory (`p355-cwd-portability`: the Makefile recipe cd's in).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from branch_alias import (  # noqa: E402
    classify,
    is_defect,
    parse_path,
    parse_refset,
)

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')

FAILURES = []


def refset(name):
    path = os.path.join(FIX, name + '.heads')
    if not os.path.exists(path):
        return None
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    # p293: an empty capture is a MEASUREMENT (the address refused us), not a repo
    # with zero branches.  `1EdTech/spec-central` is captured that way on purpose.
    return parse_refset(text) if text.strip() else None


def check(label, got, want):
    if got == want:
        print('   ok   %-62s %r' % (label, got))
    else:
        print('   FAIL %-62s got=%r want=%r' % (label, got, want))
        FAILURES.append(label)


# ─────────────── C1-C4: the finding itself, on the specimen it was found on.
# `falkenslab/miyagi` has exactly one branch, `main`.  A `master` path 200s anyway.
MIYAGI = refset('falkenslab_miyagi')
check('C1  miyagi ref set is main-only', sorted(MIYAGI['heads']), ['main'])
r = classify('https://raw.githubusercontent.com/falkenslab/miyagi/master/package.json', MIYAGI)
check('C2  miyagi /master/ verdict', r['verdict'], 'ALIAS-ONLY')
check('C3  miyagi /master/ is served by', r['served_by'], 'main')
r = classify('https://raw.githubusercontent.com/falkenslab/miyagi/main/package.json', MIYAGI)
check('C4  miyagi /main/ verdict', r['verdict'], 'BRANCH-VERIFIED')

# ─────────────── C5-C7: the ASYMMETRY, which is what makes the defect silent.
# `HyNuwa/UniMCP` lives on `master`.  A `main` path is NOT aliased — it 404s — so the
# grader must call it dead, not alias it back.  Measured 2026-10-25.
UNIMCP = refset('HyNuwa_UniMCP')
check('C5  UniMCP has master', 'master' in UNIMCP['heads'], True)
check('C6  UniMCP has no main', 'main' in UNIMCP['heads'], False)
r = classify('https://raw.githubusercontent.com/HyNuwa/UniMCP/main/LICENSE', UNIMCP)
check('C7  UniMCP /main/ is dead, not aliased', r['verdict'], 'ABSENT-REF')

# ─────────────── C8-C11: the live corpus's own defect population, four real members.
for key, slug in (('microsoft_ML-For-Beginners', 'microsoft/ML-For-Beginners'),
                  ('overhangio_tutor', 'overhangio/tutor'),
                  ('learningequality_ricecooker', 'learningequality/ricecooker'),
                  ('preactjs_preact', 'preactjs/preact')):
    rs = refset(key)
    r = classify('https://github.com/%s/blob/master/README.md' % slug, rs)
    check('C8-11 %-34s /blob/master/' % slug, r['verdict'], 'ALIAS-ONLY')

# ─────────────── C12-C13: the negatives.  A repository that REALLY has `master`
# must never be graded a defect, or the gate is a tax on correct citations.
for key, slug in (('Azure_Moodle', 'Azure/Moodle'), ('openedx_XBlock', 'openedx/XBlock')):
    rs = refset(key)
    r = classify('https://github.com/%s/blob/master/LICENSE' % slug, rs)
    check('C12-13 %-33s /blob/master/' % slug, r['verdict'], 'BRANCH-VERIFIED')

# ─────────────── C14: `master` is the ONLY aliased name.  p428 probed
# trunk/develop/dev/default/release/stable against two main-only repositories and every
# one returned 404.  The grader must call them dead, or it would excuse a real typo.
for bad in ('trunk', 'develop', 'dev', 'default', 'release', 'stable'):
    r = classify('https://raw.githubusercontent.com/falkenslab/miyagi/%s/package.json' % bad, MIYAGI)
    check('C14 miyagi /%s/ is dead' % bad, r['verdict'], 'ABSENT-REF')

# ─────────────── C15: `HEAD` resolves by construction and is not the legacy alias.
r = classify('https://raw.githubusercontent.com/CAHLR/OATutor-Content/HEAD/x.json', MIYAGI)
check('C15 HEAD is verified, not aliased', r['verdict'], 'BRANCH-VERIFIED')

# ─────────────── C16-C17: a 40-hex SHA is PINNED and is never an alias question.
# Both citations below are live in this corpus.
r = classify('https://github.com/evidentlyai/docs/blob/eb1630cdd80d31d55921ff4d34fc7b5e6e9c9f90/x.md', MIYAGI)
check('C16 40-hex SHA is PINNED', r['verdict'], 'PINNED')
r = classify('https://raw.githubusercontent.com/JuliaPluto/Pluto.jl/'
             '580ab811f13d565cc81ebfa70ed36c84b125f55d/demo/plutodemo.gif', MIYAGI)
check('C17 raw 40-hex SHA is PINNED', r['verdict'], 'PINNED')

# ─────────────── C18: a tag, graded as a tag.  `v7.13.4` is live in this corpus.
TAGGED = {'heads': {'main'}, 'tags': {'v7.13.4'}}
r = classify('https://github.com/elastic/elasticsearch-py/blob/v7.13.4/README.rst', TAGGED)
check('C18 a tag is TAG, not ABSENT-REF', r['verdict'], 'TAG')

# ─────────────── C19: UNRESOLVED-REFSET.  `1EdTech/spec-central` answered this pass's
# `ls-remote` with a CREDENTIAL PROMPT while the control `moodle/moodle` resolved
# anonymously — so the address is private or gone (p293), and the branch question is
# UNDEFINED.  Refusing a verdict is the point: the alternative is to call a path dead
# on evidence that only says we could not look.
check('C19a spec-central ref set is unreadable', refset('1EdTech_spec-central'), None)
r = classify('https://github.com/1EdTech/spec-central/blob/master/x.md',
             refset('1EdTech_spec-central'))
check('C19b and its verdict is refused', r['verdict'], 'UNRESOLVED-REFSET')
check('C19c a refused verdict is not a defect', is_defect(r['verdict']), False)

# ─────────────── C20-C21: this gate asserts nothing about citations that name no ref.
r = classify('https://github.com/falkenslab/miyagi', MIYAGI)
check('C20 a bare address asserts no branch', r['verdict'], 'NOT-A-REF-PATH')
r = classify('see the repository for details', MIYAGI)
check('C21 prose is not a path', r['verdict'], 'NOT-A-REF-PATH')

# ─────────────── C22: the two defect verdicts, and only those two.
check('C22a ALIAS-ONLY is a defect', is_defect('ALIAS-ONLY'), True)
check('C22b ABSENT-REF is a defect', is_defect('ABSENT-REF'), True)
check('C22c BRANCH-VERIFIED is not', is_defect('BRANCH-VERIFIED'), False)
check('C22d PINNED is not', is_defect('PINNED'), False)
check('C22e TAG is not', is_defect('TAG'), False)

# ─────────────── C23: the parser, on the two live path shapes plus a trailing-comma
# citation — SYNTHETIC string, real shape (the shelves end paths inside sentences).
p = parse_path('https://github.com/openedx/XBlock/tree/master/docs,')
check('C23a tree path owner/repo', (p['owner'], p['repo']), ('openedx', 'XBlock'))
check('C23b tree path ref', p['ref'], 'master')
p = parse_path('raw.githubusercontent.com/learningequality/le-utils/master/a/b.json')
check('C23c scheme-less raw path ref', p['ref'], 'master')

# ─────────────── C24: a fully-qualified `refs/heads/...` citation is unambiguous and
# this gate stands down on it.  Live in this corpus
# (`digitalcredentials/vc-test-fixtures/raw/refs`).
r = classify('https://github.com/digitalcredentials/vc-test-fixtures/raw/refs/heads/main/x.json',
             MIYAGI)
check('C24 fully-qualified refs/ path is out of scope', r['verdict'], 'NOT-A-REF-PATH')

# ─────────────── C25: the ref-set parser reads a full `ls-remote` (heads AND tags),
# not only a `--heads` capture, so one parser serves both capture shapes.
mixed = parse_refset('aaa\trefs/heads/main\nbbb\trefs/tags/v1.0\nccc\tHEAD\n')
check('C25a parser heads', sorted(mixed['heads']), ['main'])
check('C25b parser tags', sorted(mixed['tags']), ['v1.0'])
check('C25c parser drops HEAD line', 'HEAD' in mixed['heads'], False)

# ─────────────── C26: an empty ref set is NOT a main-only repository.  Without this
# guard the grader would alias `master` onto a repository it never read — inventing a
# served_by out of nothing.  SYNTHETIC input, real failure mode.
r = classify('https://github.com/x/y/blob/master/LICENSE', {'heads': set(), 'tags': set()})
check('C26 empty ref set cannot be aliased', r['verdict'], 'ABSENT-REF')

print()
if FAILURES:
    print('🔴 %d control(s) FAILED: %s' % (len(FAILURES), ', '.join(FAILURES)))
    sys.exit(1)
print('🟢 p428-branch-alias — all controls pass')
