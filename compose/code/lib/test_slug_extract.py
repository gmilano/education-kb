#!/usr/bin/env python3
"""Controls for `lib/slug_extract.py` — `886-G3`'s acceptance test, as a suite.

🟢 The four REJECTIONS below are not invented cases. They are the exact four strings
`p886`'s inline grep returned as repositories, named in `886-G3`.

Run: `python3 test_slug_extract.py`   (from this directory)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from slug_extract import extract_slugs, is_repo_slug, RESERVED_OWNERS  # noqa: E402

FAILED, PASSED = [], []


def check(name, got, want):
    (PASSED if got == want else FAILED).append(
        name if got == want else '%s: got %r want %r' % (name, got, want))


# ── ARM 1 — `886-G3`'s four, verbatim. Each one was published as a repository by p886's
#    extractor and is not one.
check('G3-1 search/repositories is an API endpoint, not a repo',
      is_repo_slug('search', 'repositories'), False)
check('G3-2 search/code likewise', is_repo_slug('search', 'code'), False)
check('G3-3 search/commits likewise — the one 884-G3 depends on',
      is_repo_slug('search', 'commits'), False)
check('G3-4 advisories/GHSA-7pp5-29mw-9jq3 is a security advisory',
      is_repo_slug('advisories', 'GHSA-7pp5-29mw-9jq3'), False)

# ── ARM 2 — the 163 that SURVIVED must still survive. These are real rows off this
#    base's live shelves; a filter that drops one of them is worse than the defect.
for owner, name in (
        ('HKUDS', 'DeepTutor'), ('openedx', 'XBlock'), ('openedx', 'xblock-sdk'),
        ('OS4ED', 'openSIS-Classic'), ('RWTH-OS', 'eduOS-rs'),
        ('portabilis', 'i-diario'), ('withmarbleapp', 'os-taxonomy'),
        ('frappe', 'education'), ('opendatalab', 'MinerU'),
        ('sudosylabs', 'proctor'), ('iiab', 'iiab'), ('ECNU', 'EduWork'),
        ('ox-it', 'wl-roster2'), ('yetanalytics', 'lrsql'),
        ('apereo', 'phpCAS'), ('HumanSignal', 'label-studio'),
        ('oppia', 'oppia-android'), ('DSpace', 'DSpace'),
        ('deepseek-ai', 'deepseek-harness'), ('Li-Evan', 'BloomTutor'),
        ('openeducat', 'openeducat_erp'), ('odoo', 'odoo'),
):
    check('KEEP %s/%s (a live shelf row)' % (owner, name),
          is_repo_slug(owner, name), True)

# ── ARM 3 — every name in `886-G3`'s reserved list is actually rejected.
for res in ('search', 'advisories', 'topics', 'orgs', 'users', 'apps', 'sponsors',
            'collections', 'features', 'settings', 'notifications', 'codespaces',
            'marketplace'):
    check('RESERVED %s is in the list 886-G3 specifies' % res, res in RESERVED_OWNERS, True)
    check('RESERVED %s/anything is rejected' % res, is_repo_slug(res, 'anything'), False)

# ── ARM 4 — extraction over PROSE, which is the form the shelves are actually in.
#    This paragraph is built to look like a shelf cell: a real row, an API endpoint in
#    method prose, an advisory, a markdown link with trailing punctuation, and a `.git`.
PROSE = """
The agent is [DeepTutor](https://github.com/HKUDS/DeepTutor) and the grant is at
https://github.com/openedx/XBlock/blob/master/LICENSE.TXT — read first-hand. Metadata came
from api.github.com/search/repositories, documented at github.com/search/repositories, and
the advisory github.com/advisories/GHSA-7pp5-29mw-9jq3 applies. Clone with
https://github.com/oppia/oppia.git. See also (https://github.com/iiab/iiab), and
github.com/apereo/cas.
"""
acc, rej = extract_slugs(PROSE, keep_rejected=True)
check('E-1 the five real repositories, in first-appearance order',
      acc, ['HKUDS/DeepTutor', 'openedx/XBlock', 'oppia/oppia', 'iiab/iiab', 'apereo/cas'])
check('E-2 exactly two rejections from that prose', len(rej), 2)
check('E-3 the rejection reasons are NAMED, not discarded',
      sorted(r[1] for r in rej), ['advisory-id', 'reserved-owner:search'])
check('E-4 a trailing `)` from a markdown link is not part of the name',
      'iiab/iiab' in acc, True)
check('E-5 a `.git` clone suffix is stripped to the repository name',
      'oppia/oppia' in acc, True)
check('E-6 `oppia/oppia.git` was NOT emitted as a separate entity',
      any(s.endswith('.git') for s in acc), False)

# ── ARM 5 — sub-resource verbs in the second position, the next defect in this class.
check('S-1 github.com/blob/master is not a repository',
      is_repo_slug('blob', 'master'), False)
check('S-2 a repo literally named `blob` under a real owner is still rejected, and that '
      'is the documented trade-off', is_repo_slug('someorg', 'blob'), False)
check('S-3 de-duplication is case-insensitive on the whole slug',
      extract_slugs('github.com/HKUDS/DeepTutor and github.com/hkuds/deeptutor'),
      ['HKUDS/DeepTutor'])

# ── ARM 6 — the RATCHET. `886-G3` closes only when this is a HELPER, not an inline grep.
check('RATCHET extract_slugs is importable and callable from another instrument',
      callable(extract_slugs), True)
check('RATCHET empty input is empty output, never a crash', extract_slugs(''), [])
check('RATCHET None is tolerated (a shelf cell can be missing)', extract_slugs(None), [])

print('lib/slug_extract — %d controls' % (len(PASSED) + len(FAILED)))
for f in FAILED:
    print('  FAIL  %s' % f)
if FAILED:
    print('RED: %d/%d' % (len(PASSED), len(PASSED) + len(FAILED)))
    sys.exit(1)
print('PASS: %d/%d' % (len(PASSED), len(PASSED)))
