#!/usr/bin/env python3
"""`lib/slug_extract.py` — "which repositories does this shelf name?", asked ONCE.

Pass `p887` of 2026-11-18. 🔵 **This module exists because `P263`'s rule came due again.**
The rule is written in `lib/README.md`, in `lib/region.py` and in `lib/licence_identity.py`:

> *while the question does not live in `compose/code/lib/`, every new instrument
> reimplements it and chooses the bug again.*

🔴 **`886-G3` is that rule being paid, for the third time in this directory.** `p886`
extracted its shelf population with an inline

    grep -oE 'github\\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+'

re-written from scratch in the pass that needed it. `github.com/<a>/<b>` matches any two
path segments, so it returned **four non-repositories** — `search/repositories`,
`search/code`, `search/commits` (API endpoint paths quoted in METHOD PROSE on the shelves
themselves) and `advisories/GHSA-7pp5-29mw-9jq3` (a security-advisory URL). The population
was **163, not 167**.

🔵 **Why `p886` graded that 🟡 and not 🔴**: an independent channel caught it — those four
are exactly the slugs on which `search/repositories` answered `422` while the other 163
answered `200`. 🔴 **But a pass that trusted one channel would have published four KB
entities named after API endpoints**, which is the `nombre`-row class in a new shape: not a
table header read as data, but a URL *fragment* read as a repository.

🟢 **The contract, from `886-G3`'s acceptance test verbatim.** The extractor rejects a first
segment in `RESERVED_OWNERS` and any second segment matching `^GHSA-`.

🔵 **Two extras this module adds, because the inline grep got them wrong too and nobody
had written them down:** a trailing `.git`, and the sub-resource suffixes a prose URL
carries (`/blob/...`, `/tree/...`, `/issues/...`, `#anchor`, `?query`, `)`/`,`/`.` from
surrounding punctuation). Those do not change `p886`'s count — all 163 survivors were
already bare — but they are the next defect in the same class and cost one regex each.

    from slug_extract import extract_slugs, is_repo_slug

No network.  Controls: `python3 test_slug_extract.py`.
"""

import re

# `886-G3`'s list, verbatim, plus the GitHub first segments that are also not owners.
RESERVED_OWNERS = frozenset((
    'search', 'advisories', 'topics', 'orgs', 'users', 'apps', 'sponsors',
    'collections', 'features', 'settings', 'notifications', 'codespaces',
    'marketplace',
    # not in `886-G3`'s list; the same class, and free to add here once
    'about', 'contact', 'enterprise', 'pricing', 'security', 'site', 'readme',
    'login', 'join', 'new', 'explore', 'trending', 'dashboard', 'account',
    # 🔴 `900-G1`, added p900. `886-G3` reserved `search` because this KB quotes
    # `api.github.com/search/repositories` in its METHOD PROSE. It never reserved the
    # OTHER api.github.com path, `api.github.com/repos/<owner>/<repo>`, which this base
    # quotes **380 times** — and `github.com/repos/<owner>` matches the URL regex, so the
    # p900 ledger rebuild returned `repos/moodle` (14 files), `repos/hkuds` (13),
    # `repos/openedx` (11) and 15 more as promotable candidates. Same defect class as
    # `886-G3`, in the module written to fix `886-G3`.
    'repos', 'api', 'gists', 'licenses', 'repositories', 'gitignore',
))

# 🔴 `900-G2`, added p900. A slug that is syntactically valid and semantically a BLANK.
# `github.com/owner/repo` occurs in **22 files** of this base as the placeholder in prose
# describing the shelf's link format — and the p900 ledger ranked it **2nd**, above every
# real repository. This is the `nombre`-row class exactly: not a header read as data, but
# a TEMPLATE read as data. The trade-off is the one this module already documents — a
# real repository literally named `owner/repo` would be rejected, and a false ABSENCE is
# visible to the next pass's presence gate while a false PRESENCE becomes a KB entity
# nobody questions.
PLACEHOLDER_SLUGS = frozenset((
    'owner/repo', 'owner/name', 'owner/repository', 'org/repo', 'user/repo',
    'username/repo', 'owner/project', 'you/your-repo', 'your-org/your-repo',
))

# The sub-resource verbs a prose URL carries.  Reserved in BOTH positions: in the second
# because `github.com/<owner>/blob` is a truncation, and in the first because
# `github.com/blob/master` is one too.
#
# 🔵 THE TRADE-OFF, stated once and tested as control `S-2`: a real repository actually
# named `blob` or `tree` would be rejected.  That is accepted deliberately — `886-G3`'s
# defect published four entities that do not exist, and a false ABSENCE is visible to the
# next pass's presence gate while a false PRESENCE becomes a KB entity nobody questions.
RESERVED_NAMES = frozenset(('blob', 'tree', 'raw', 'releases', 'issues', 'pull', 'wiki',
                            'commits', 'commit', 'branches', 'tags', 'compare', 'actions'))

# 🔴 `900-G1`, second order. Reserving `repos` is necessary and NOT sufficient: the API
# path CONTAINS the real address one segment deeper, so a predicate that merely rejects
# `repos/moodle` consumes the text and the real `moodle/moodle` under it is never emitted.
# Measured as control `A-1`. The prefix must be CONSUMED, and `repos` must ALSO stay
# reserved — because `github.com/repos/moodle` with no third segment still backtracks into
# `owner=repos`. Both halves are load-bearing; neither alone is correct.
_URL = re.compile(
    r'(?:https?://)?(?:www\.|api\.)?github\.com/(?:repos/)?'
    r'(?P<owner>[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)/'
    r'(?P<name>[A-Za-z0-9._-]+)',
    re.IGNORECASE,
)

_GHSA = re.compile(r'^GHSA-', re.IGNORECASE)
# Markdown and prose punctuation that is NOT part of a repository name.  A name may end
# in a letter, digit or `_`; a trailing `.`, `-`, `)` or `,` came from the sentence.
_TRAILING = re.compile(r'[.,;:)\]}>\'"]+$')


def is_repo_slug(owner, name):
    """Is `owner/name` a REPOSITORY, as opposed to a GitHub URL that merely has two
    path segments?  This is `886-G3`'s predicate."""
    if not owner or not name:
        return False
    if owner.lower() in RESERVED_OWNERS or owner.lower() in RESERVED_NAMES:
        return False
    if name.lower() in RESERVED_NAMES:
        return False
    if _GHSA.match(name):
        return False
    # `.` and `..` are path traversal, never names; a bare `.git` is not a name either.
    if name in ('.', '..') or name.lower() == '.git':
        return False
    if ('%s/%s' % (owner, name)).lower() in PLACEHOLDER_SLUGS:
        return False
    return True


def _clean_name(name):
    name = _TRAILING.sub('', name)
    if name.lower().endswith('.git'):
        name = name[:-4]
    return name


def extract_slugs(text, keep_rejected=False):
    """Every `owner/repo` this text NAMES, de-duplicated, in first-appearance order.

    With `keep_rejected=True`, returns `(accepted, rejected)` where `rejected` is a list
    of `(slug, reason)` — because `886-G3`'s defect was invisible precisely while the
    rejections were thrown away.
    """
    seen, accepted, rejected = set(), [], []
    for m in _URL.finditer(text or ''):
        owner = m.group('owner')
        name = _clean_name(m.group('name'))
        slug = '%s/%s' % (owner, name)
        key = slug.lower()
        if key in seen:
            continue
        seen.add(key)
        if is_repo_slug(owner, name):
            accepted.append(slug)
        else:
            if _GHSA.match(name):
                reason = 'advisory-id'
            elif owner.lower() in RESERVED_OWNERS:
                reason = 'reserved-owner:%s' % owner.lower()
            elif name.lower() in RESERVED_NAMES:
                reason = 'sub-resource:%s' % name.lower()
            elif owner.lower() in RESERVED_NAMES:
                reason = 'sub-resource-owner:%s' % owner.lower()
            elif slug.lower() in PLACEHOLDER_SLUGS:
                reason = 'placeholder'
            else:
                reason = 'not-a-name'
            rejected.append((slug, reason))
    if keep_rejected:
        return accepted, rejected
    return accepted


if __name__ == '__main__':
    import sys
    body = sys.stdin.read()
    acc, rej = extract_slugs(body, keep_rejected=True)
    for s in acc:
        print(s)
    for s, why in rej:
        print('# REJECTED\t%s\t%s' % (s, why), file=sys.stderr)
    print('# accepted=%d rejected=%d' % (len(acc), len(rej)), file=sys.stderr)
