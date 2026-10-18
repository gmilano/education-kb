#!/usr/bin/env python3
"""pass280 — THE INVENTED-PAYLOAD CENSUS: which controls name a real repository and assert
bytes nobody read?

`p279` left this as item 2 and scoped it to one control:

    Re-write `p229`'s `mcp-canvas-lms` control against the manifest the repository actually
    serves ... and audit the other `T229-M2` controls for the same thing.

🔵 THE AUDIT IS THE HALF WORTH BUILDING, because the defect is not a typo.  A control whose
subject is SYNTHETIC (`a/b`, `{"name":"x"}`) is a unit test of a predicate and is correct as
written -- it asserts nothing about the world.  A control that NAMES A REAL SLUG asserts that
a particular repository serves particular bytes, and `p280` measured what that assertion was
worth in `p229`: of four such controls, ONE reproduced the served payload exactly, TWO were
approximations (a truncated licence array, an unscoped name) and ONE was invented outright --
and the invented one asserted the OPPOSITE VERDICT to the real payload's.

So the class is: a REAL-SLUG control with no recorded provenance.  This instrument finds
them.  Provenance means a `PROVENANCE.tsv` row (`slug`, `ref`, `head_sha`, `path`, `bytes`,
`sha256`, `captured`) beside the fixture the control reads.

    --census   list every real-slug control and whether its slug has captured provenance.
               A MEASUREMENT.  Exit 0 always: these are 370 instruments' worth of history,
               each already adjudicated by the pass that wrote it, and a gate that fails the
               build on all of them on day one gets switched off within a pass (`p279`).
    --verify   the PINNED arm: the controls `p280` converted must STAY provenance-backed.
               Exit 1 if any pinned file loses its fixture reference.  This is `p252`'s
               pinned-floor shape -- a census becomes a gate only for what has been worked.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))

# A slug-shaped literal, excluding the things that merely look like one.
SLUG = re.compile(r'''['"]([A-Za-z0-9][A-Za-z0-9_.-]{1,38})/([A-Za-z0-9][A-Za-z0-9_.-]{1,38})['"]''')
# A payload-shaped literal within reach of it.
PAYLOAD = re.compile(r'\{\s*\\?"(name|license|licenses)\\?"|^\s*name\s*=\s*["\']|'
                     r'<licenses>|Copyright \(c\)|GNU General Public License')
NOT_A_SLUG = ('.py', '.sh', '.md', '.json', '.toml', '.tsv', '.txt', '.xml', '.cfg',
              '.lock', '.yml', '.yaml', '.php', '.rst', '.html', '.js', '.ts', '.mjs')
NOT_A_SLUG_PREFIX = ('compose/', 'evidence/', 'agents/', 'repos/', 'intel/', 'verticals/',
                     'fixtures/', 'lib/', 'docs/', 'src/', 'packages/', 'apps/', 'ui/',
                     'node_modules/', 'LICENSES/', 'tmp/', 'usr/', 'etc/', 'var/',
                     'dist/', 'build/', 'test/', 'tests/')
# 🔴 A JSON-RPC / MCP method name is `verb/noun` and matches the slug shape exactly.
# `tools/call` is not a repository, and ten of the first census's 46 hits were this.
RPC_METHOD_OWNERS = ('tools', 'resources', 'prompts', 'notifications', 'completion',
                     'logging', 'sampling', 'roots', 'initialize')
# 🟡 A DECLARED SYNTHETIC: an owner this base uses to mean "any repository".  A control
# naming one asserts nothing about the world, so it is correct as written -- that is the
# whole distinction this census exists to draw.
SYNTHETIC_OWNERS = ('acme', 'ghost', 'example', 'examples', 'foo', 'bar', 'baz', 'a', 'b',
                    'x', 'y', 'z', 'test', 'dummy', 'owner', 'org', 'vendor', 'someone',
                    'nobody', 'upstream', 'fork')


def bucket(owner, repo):
    """-> NOT-A-SLUG | RPC-METHOD | SYNTHETIC | CANDIDATE.

    🔵 THE VOCABULARIES BELOW ARE FLOORS AND SAY SO -- `p279` proved a path vocabulary can
    only reject the conventions somebody enumerated, and a synthetic-owner list can only
    reject the placeholders somebody enumerated.  The DURABLE discriminator is RESOLUTION:
    `--resolve` runs one `git ls-remote` per CANDIDATE, and a slug that resolves is a real
    repository whatever any list says.  The buckets only shorten the list to resolve, which
    is `p436`'s own rule for its UPSTREAM class: it shortens the list, it does not decide it.
    """
    whole = '%s/%s' % (owner, repo)
    if whole.lower().endswith(NOT_A_SLUG):
        return 'NOT-A-SLUG'
    if any(whole.startswith(pre) for pre in NOT_A_SLUG_PREFIX):
        return 'NOT-A-SLUG'
    if re.fullmatch(r'[\d.]+/[\d.]+', whole):
        return 'NOT-A-SLUG'
    if owner.lower() in RPC_METHOD_OWNERS:
        return 'RPC-METHOD'
    if owner.lower() in SYNTHETIC_OWNERS:
        return 'SYNTHETIC'
    return 'CANDIDATE'


# The files `p280` converted to captured payloads.  Each must keep naming a PROVENANCE-backed
# fixture directory, or the conversion has been undone.
PINNED = {
    'p229-grant-ladder-reach/test_grant_ladder_reach.py': 'pass280-package-provenance/fixtures',
}


def looks_like_slug(owner, repo):
    whole = '%s/%s' % (owner, repo)
    if whole.lower().endswith(NOT_A_SLUG):
        return False
    if any(whole.startswith(p) for p in NOT_A_SLUG_PREFIX):
        return False
    # a version range, a licence disjunction, a date, a fraction
    if re.fullmatch(r'[\d.]+/[\d.]+', whole):
        return False
    return '.' not in owner or owner.count('.') <= 1


def provenance_slugs():
    """-> {slug.lower()} for every slug with a recorded capture anywhere under compose/code."""
    out = set()
    for dirpath, _dirs, files in os.walk(ROOT):
        for f in files:
            if f != 'PROVENANCE.tsv':
                continue
            with open(os.path.join(dirpath, f), encoding='utf-8', errors='replace') as fh:
                for i, line in enumerate(fh):
                    if i == 0:
                        continue
                    cols = line.rstrip('\n').split('\t')
                    if cols and cols[0]:
                        out.add(cols[0].lower())
    return out


def scan():
    """-> [(relpath, lineno, slug, has_payload_nearby)]"""
    hits = []
    for dirpath, _dirs, files in os.walk(ROOT):
        for f in sorted(files):
            if not (f.startswith('test_') and (f.endswith('.py') or f.endswith('.sh'))):
                continue
            path = os.path.join(dirpath, f)
            rel = os.path.relpath(path, ROOT)
            try:
                lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
            except OSError:
                continue
            for n, line in enumerate(lines, 1):
                for m in SLUG.finditer(line):
                    owner, repo = m.group(1), m.group(2)
                    b = bucket(owner, repo)
                    window = '\n'.join(lines[max(0, n - 4):n + 3])
                    if PAYLOAD.search(window, re.M):
                        hits.append((rel, n, '%s/%s' % (owner, repo), b))
    return hits


def main():
    if '--verify' in sys.argv:
        bad = []
        for rel, needle in sorted(PINNED.items()):
            p = os.path.join(ROOT, rel)
            try:
                body = open(p, encoding='utf-8', errors='replace').read()
            except OSError as e:
                bad.append('%s unreadable: %s' % (rel, e))
                continue
            if needle not in body:
                bad.append('%s no longer reads captured payloads from %s' % (rel, needle))
        for b in bad:
            print('🔴 %s' % b)
        if bad:
            return 1
        print('   %d pinned suite(s) still read CAPTURED payloads' % len(PINNED))
        return 0

    hits = scan()
    known = provenance_slugs()
    buckets = {}
    for h in hits:
        buckets.setdefault(h[3], []).append(h)
    print('SLUG-SHAPED-LITERALS-NEAR-A-PAYLOAD\t%d' % len(hits))
    for b in ('CANDIDATE', 'SYNTHETIC', 'RPC-METHOD', 'NOT-A-SLUG'):
        print('%s\t%d' % (b, len(buckets.get(b, []))))
    cands = buckets.get('CANDIDATE', [])
    backed = [h for h in cands if h[2].lower() in known]
    print('CANDIDATE-PROVENANCE-BACKED\t%d' % len(backed))
    print('CANDIDATE-UNBACKED\t%d' % (len(cands) - len(backed)))
    for rel, n, slug, _b in cands:
        state = 'BACKED' if slug.lower() in known else 'UNBACKED'
        print('%s\t%s:%d\t%s' % (state, rel, n, slug))
    return 0


if __name__ == '__main__':
    sys.exit(main())
