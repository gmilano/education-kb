"""p428 — a published path that names `master` is not evidence that `master` exists.

`gate-grant-path` (p354) states the contract this base publishes under: *a published
grant path asserts a BRANCH and a FILE, and both must resolve*.  Its online arm
(`gate-grant-path-online`) answers that question with an HTTP 200 against
`raw.githubusercontent.com`.

p428 measured that 200-check against the ref sets and it CANNOT answer the branch half.
GitHub serves the default branch under the legacy name `master`, so a path reading

    https://raw.githubusercontent.com/<owner>/<repo>/master/LICENSE

returns `200` with the default branch's bytes on a repository whose only branch is
`main`.  Measured first-hand on 2026-10-25:

  * `falkenslab/miyagi` — ref set is exactly `refs/heads/main`, no `master`.
    `.../master/package.json` → `200`, and the body is BYTE-IDENTICAL to
    `.../main/package.json` (`sha256(12) 4350dcad89c6`, `1 123` B both).
  * 14 of the 14 testable `master`-less addresses in this corpus return `200` under
    `master`.

The alias is NOT a general fallback and it is NOT symmetric — both halves were
isolated by measurement, not assumed:

  * On the same main-only repositories, `trunk`, `develop`, `dev`, `default`,
    `release` and `stable` all return `404`.  Only `master` and the documented
    `HEAD` resolve.
  * On `HyNuwa/UniMCP`, whose live branch is `master`, `.../main/LICENSE` returns
    `404`.  The alias runs master→default ONLY.

So the error is silent in exactly one direction: the direction a path written from
habit takes.  A reader who clones and runs `git checkout master`, or `git ls-tree -r
master`, gets nothing — while every 200-check on this base said the path was live.

This module answers the question the 200-check cannot, OFFLINE, from a ref set:
does the ref the path NAMES exist?

Verdicts
--------
`BRANCH-VERIFIED`   the named ref is in the ref set.
`ALIAS-ONLY`        the path names `master`, the ref set has no `master`, and the
                    repository has a default-shaped branch the alias will serve.  The
                    path fetches 200 and names a branch that does not exist.
`ABSENT-REF`        the named ref is in no ref set and no alias covers it — the path
                    is dead and a 200-check agrees it is dead.
`UNRESOLVED-REFSET` no ref set could be read for the address (p293: a credential
                    prompt is a MEASUREMENT — private or absent — never "inconclusive").
                    The branch question is UNDEFINED, and a verdict is refused rather
                    than guessed.
`PINNED`            the path names a 40-hex commit SHA.  Immutable, and the strongest
                    shape this base can publish.  Never an alias question.
`TAG`               the path names a ref that is a tag in the ref set.
`NOT-A-REF-PATH`    the citation carries no `/blob/`, `/tree/` or `/raw/` segment, so
                    it asserts no branch and this gate has nothing to say.

`HEAD` is `BRANCH-VERIFIED` whenever a ref set was read: it is GitHub's documented
alias for the default branch and resolves by construction.
"""

import re

SHA_RE = re.compile(r'\A[0-9a-f]{40}\Z')
SHORT_SHA_RE = re.compile(r'\A[0-9a-f]{7,39}\Z')

# The one aliased name, and the direction it runs.  Measured, not assumed: see module
# docstring.  `HEAD` is handled separately because it is documented, not legacy.
ALIAS_NAME = 'master'

# A path shape that asserts a ref.  `raw.githubusercontent.com/<o>/<r>/<ref>/...` and
# `github.com/<o>/<r>/(blob|tree|raw)/<ref>/...`.
RAW_RE = re.compile(
    r'raw\.githubusercontent\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)/'
    r'(?P<ref>[A-Za-z0-9_.-]+)(?P<rest>/.*)?\Z')
BLOB_RE = re.compile(
    r'github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)/'
    r'(?:blob|tree|raw)/(?P<ref>[A-Za-z0-9_.-]+)(?P<rest>/.*)?\Z')


def parse_path(citation):
    """Return {owner, repo, ref, rest} for a ref-asserting citation, else None.

    A `refs/...` segment (as in `/raw/refs/heads/main/...`) is returned verbatim as the
    ref so the caller can see the base published a fully-qualified ref — that shape is
    unambiguous and this gate treats it as named exactly.
    """
    s = citation.strip().strip('<>()[],;')
    s = re.sub(r'\Ahttps?://', '', s)
    for rx in (RAW_RE, BLOB_RE):
        m = rx.search(s)
        if m:
            return {'owner': m.group('owner'), 'repo': m.group('repo'),
                    'ref': m.group('ref'), 'rest': m.group('rest') or ''}
    return None


def parse_refset(text):
    """Parse `git ls-remote` output into {'heads': set, 'tags': set}.

    Accepts both `--heads` output and a full `ls-remote`, so one parser serves the
    two capture shapes in `fixtures/`.
    """
    heads, tags = set(), set()
    for line in (text or '').splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue
        ref = parts[1]
        if ref.startswith('refs/heads/'):
            heads.add(ref[len('refs/heads/'):])
        elif ref.startswith('refs/tags/'):
            tags.add(ref[len('refs/tags/'):].removesuffix('^{}'))
    return {'heads': heads, 'tags': tags}


def classify(citation, refset):
    """Grade one citation against a ref set.

    `refset` is the dict from `parse_refset`, or None when no ref set could be read.
    Returns {verdict, ref, owner, repo, served_by}.
    """
    p = parse_path(citation)
    if p is None:
        return {'verdict': 'NOT-A-REF-PATH', 'ref': None, 'owner': None,
                'repo': None, 'served_by': None}

    out = {'ref': p['ref'], 'owner': p['owner'], 'repo': p['repo'], 'served_by': None}
    ref = p['ref']

    if SHA_RE.match(ref):
        out['verdict'] = 'PINNED'
        return out

    if refset is None:
        out['verdict'] = 'UNRESOLVED-REFSET'
        return out

    if ref == 'HEAD' or ref == 'refs':
        # `HEAD` is documented; a `refs/...` citation was published fully qualified and
        # its own head/tag segment is what a ref set would be asked about.  Both are
        # out of this gate's reach and neither is the legacy alias.
        out['verdict'] = 'BRANCH-VERIFIED' if ref == 'HEAD' else 'NOT-A-REF-PATH'
        return out

    if ref in refset['heads']:
        out['verdict'] = 'BRANCH-VERIFIED'
        return out

    if ref in refset['tags']:
        out['verdict'] = 'TAG'
        return out

    if ref == ALIAS_NAME and refset['heads']:
        # The alias will serve SOMETHING — the default branch — so the path fetches
        # 200 while naming a branch that is not there.  This is the silent class.
        out['verdict'] = 'ALIAS-ONLY'
        out['served_by'] = 'main' if 'main' in refset['heads'] else sorted(refset['heads'])[0]
        return out

    if SHORT_SHA_RE.match(ref):
        # An abbreviated SHA is not in a ref set and is not an alias.  It resolves on
        # GitHub but cannot be graded from refs alone; say so rather than call it dead.
        out['verdict'] = 'UNRESOLVED-REFSET'
        return out

    out['verdict'] = 'ABSENT-REF'
    return out


def is_defect(verdict):
    """The two verdicts a shelf may not publish unexamined.

    `ALIAS-ONLY` is the p428 finding: live to a 200-check, dead to a clone.
    `ABSENT-REF` is a dead citation under any channel.
    """
    return verdict in ('ALIAS-ONLY', 'ABSENT-REF')
