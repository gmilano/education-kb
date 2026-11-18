"""p887 offline controls — the CONTRACT for `arity_map.py`.

🟢 `886-G2(b)` COMPLIANCE: no instrument may overwrite a shelf cell until it has been run
against a NAMED KNOWN-GOOD FIXTURE SET drawn from cells the shelf already established.
The fixture set here is exactly that, and every expectation below cites the shelf line or
the `p886` record it was taken from — so a regression names the row it broke.

Run: `python3 test_arity_map.py`   (from this directory; `p355-cwd-portability`'s class)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from arity_map import (  # noqa: E402
    determine_mode, is_payload, prefix_of, sha12, GRANT_NAME, POLICY_NAME,
)

FAILED = []
PASSED = []


def check(name, got, want):
    if got == want:
        PASSED.append(name)
    else:
        FAILED.append('%s: got %r want %r' % (name, got, want))


# ─────────────────────────────────────────────────────────────────────────────
# ARM 1 — the four spellings `p885`'s 8-path ladder could not see.
# Every one is a cell this KB already established; `886-G2` lists them.
# A FILTER over `ls-tree -r` must accept all four without naming any of them.
# ─────────────────────────────────────────────────────────────────────────────
check('G2-1 openedx/XBlock LICENSE.TXT  (foundations.md:408, Apache-2.0 11,358 B)',
      is_payload('LICENSE.TXT'), True)
check('G2-2 openSIS-Classic docs/License.txt  (886-G5: GPL-2.0 17,286 B, ~611 passes)',
      is_payload('docs/License.txt'), True)
check('G2-3 frappe/education license.txt  (19-byte declaration, still a payload)',
      is_payload('license.txt'), True)
check('G2-4 eduOS-rs LICENSE-MIT  (foundations.md:666, split-file OR)',
      is_payload('LICENSE-MIT'), True)
check('G2-5 eduOS-rs LICENSE-APACHE  (the other half of the same pair)',
      is_payload('LICENSE-APACHE'), True)

# ARM 2 — the per-directory case that forced `-r` onto `p370`'s root-only ls-tree.
check('G1-1 proctor packages/cache/LICENSE is a payload at depth 2',
      is_payload('packages/cache/LICENSE'), True)
check('G1-2 proctor server/internal/autocert/LICENSE at depth 3',
      is_payload('server/internal/autocert/LICENSE'), True)
check('G1-3 its prefix is the directory it governs',
      prefix_of('packages/cache/LICENSE'), 'packages/cache/')
check('G1-4 a root grant governs the repository',
      prefix_of('LICENSE'), '/')
check('G1-5 i-diario Portuguese AGPL body (LICENCA) is reached by the filter',
      is_payload('LICENCA'), True)

# ARM 3 — REJECTIONS. A filter that accepts prose re-creates the `nombre`-row class.
check('R-1 README.md is not a payload', is_payload('README.md'), False)
check('R-2 LICENSE.md is PROSE about a licence, per p427 sweep.py line',
      is_payload('LICENSE.md'), False)
check('R-3 LICENSING.md is a POLICY doc, never a payload (886-G1 part b)',
      is_payload('LICENSING.md'), False)
check('R-4 a licence-ish python module is not a payload',
      is_payload('compose/code/p228-shelf-gate/classify_grant.py'), False)
check('R-5 a path merely CONTAINING "license" mid-segment is not a payload',
      is_payload('src/license_checker.go'), False)
check('R-6 THIRD_PARTY_NOTICES.md is a policy doc, not a payload',
      is_payload('THIRD_PARTY_NOTICES.md'), False)

# ARM 4 — the POLICY filter, against the exact spellings `p886` recorded on 19 rows.
for spelling in ('LICENSING.md', 'NOTICE', 'NOTICE.txt', 'THIRD_PARTY_NOTICES.md'):
    check('P-%s recognised as a policy document (p886 record)' % spelling,
          bool(POLICY_NAME.search(spelling)), True)
check('P-neg NOTICE inside a vendor tree still matches (any depth)',
      bool(POLICY_NAME.search('vendor/foo/NOTICE')), True)
check('P-neg2 NOTICES.md is not one of the three spellings 886-G1 names',
      bool(POLICY_NAME.search('NOTICES.md')), False)

# ─────────────────────────────────────────────────────────────────────────────
# ARM 5 — the AND/OR determination, `886-G1` part (b).
# 🔴 `886-G4` is the reason UNDETERMINED must exist and must not be silently 'OR':
# `eduOS-rs` is OR and `EduWork` is AND and NO PROBER can tell them apart.
# ─────────────────────────────────────────────────────────────────────────────
check('M-1 Rust-convention OR (eduOS-rs Cargo.toml: license = "MIT/Apache-2.0")',
      determine_mode('Licensed under MIT/Apache-2.0 at your option.')[0], 'OR')
check('M-2 EduWork-shape AND (MulanPSL-2.0 AND MIT, both payloads byte-read at p886)',
      determine_mode('This project is dual-licensed under both the Mulan PSL v2 '
                     'and the MIT License.')[0], 'AND')
check('M-3 proctor-shape AND: a scope rider adding terms',
      determine_mode('The reusable packages are provided in addition to the terms '
                     'of the AGPL.')[0], 'AND')
check('M-4 a NOTICE that makes no determination is UNDETERMINED, never OR',
      determine_mode('Copyright 2026 The Apereo Foundation.\n'
                     'This product includes software developed at Apereo.')[0],
      'UNDETERMINED')
check('M-5 an empty document is UNDETERMINED', determine_mode('')[0], 'UNDETERMINED')
check('M-6 a document carrying BOTH markers is AMBIGUOUS, not a coin flip',
      determine_mode('Licensed under both the MIT License and Apache-2.0. '
                     'You may use either at your option.')[0], 'AMBIGUOUS')
check('M-7 the OR branch reports the MARK that decided it (886-G4 audit column)',
      determine_mode('at your option')[1:], (None, 'at your option'))

# ARM 6 — the byte identity every cell on these shelves is pinned with.
check('S-1 sha256_12 is 12 hex chars', len(sha12(b'x')), 12)
check('S-2 sha256_12 of the empty payload', sha12(b''), 'e3b0c44298fc')
check('S-3 byte-sensitivity: one trailing newline changes the pin',
      sha12(b'MIT License') == sha12(b'MIT License\n'), False)

# ─────────────────────────────────────────────────────────────────────────────
# ARM 7 — THE TWO DEFECTS THIS INSTRUMENT FOUND IN ITSELF ON ITS FIRST RUN.
# Both were measured on real repositories before any cell was written, which is the
# only reason neither reached a shelf.
# ─────────────────────────────────────────────────────────────────────────────
from arity_map import grant_class, POLICY_NAME as _PN, GRANT_NAME as _GN  # noqa: E402

# DEFECT A — `NOTICE` was in `GRANT_NAME` and `is_payload` was tested BEFORE `POLICY_NAME`,
# so every NOTICE was read as a grant.  Measured: `apereo/phpCAS` NOTICE 3,914 B and
# `yetanalytics/lrsql` NOTICE 19,985 B both classified BSD-3-Clause, and both repositories
# came back `arity=2 Apache-2.0+BSD-3-Clause`.  Both are Apache-2.0 at root.
check('A-1 NOTICE is NOT a grant payload (phpCAS 3,914 B / lrsql 19,985 B)',
      is_payload('NOTICE'), False)
check('A-2 NOTICE.txt likewise (openedx/* carry this spelling)',
      is_payload('NOTICE.txt'), False)
check('A-3 NOTICE is recognised as a POLICY document instead',
      bool(_PN.search('NOTICE')), True)
check('A-4 and `notice` is OUT of the grant filter entirely',
      'notice' in _GN.pattern.lower(), False)
check('A-5 LICENSE is still a grant payload (the fix must not be a blanket exclusion)',
      is_payload('LICENSE'), True)

# DEFECT B — a raw arity count conflates a VENDORED dependency's grant with the
# repository's own.  Measured: `HKUDS/DeepTutor` carries `web/vendor/thinking-orbs/LICENSE`
# (MIT, 1,070 B) and IS Apache-2.0; `deepseek-ai/deepseek-harness` carries fourteen
# vendored MIT copies and IS MIT at root.
check('B-1 a root grant is OWN', grant_class('LICENSE'), 'OWN')
check('B-2 DeepTutor web/vendor/thinking-orbs/LICENSE is VENDORED',
      grant_class('web/vendor/thinking-orbs/LICENSE'), 'VENDORED')
check('B-3 deepseek-harness vendor/cordis/LICENSE is VENDORED',
      grant_class('vendor/cordis/LICENSE'), 'VENDORED')
check('B-4 node_modules is VENDORED at any depth',
      grant_class('a/b/node_modules/c/LICENSE'), 'VENDORED')
check('B-5 a bundled FONT licence is VENDORED '
      '(openvidu-testapp/src/fonts/, MIT 4,394 B)',
      grant_class('openvidu-testapp/src/fonts/LICENSE'), 'VENDORED')
check('B-6 a monorepo PACKAGE is OWN, not vendored — this is the real per-directory '
      'arity deepseek-harness has (root MIT, native/system BSD-3-Clause, '
      'packages/experimental/subagent-oar Apache-2.0)',
      grant_class('packages/experimental/subagent-oar/LICENSE'), 'OWN')
check('B-7 third_party/ is VENDORED', grant_class('third_party/x/LICENSE'), 'VENDORED')

# ARM 8 — the RATCHET. `886-G2` exists because a new ladder shipped without this.
check('RATCHET the filter defines no path LIST: it is a regex over enumerated names',
      isinstance(GRANT_NAME.pattern, str) and 'ls-tree' not in GRANT_NAME.pattern, True)

print('p887-grant-arity-map — %d controls' % (len(PASSED) + len(FAILED)))
for f in FAILED:
    print('  FAIL  %s' % f)
if FAILED:
    print('RED: %d/%d' % (len(PASSED), len(PASSED) + len(FAILED)))
    sys.exit(1)
print('PASS: %d/%d' % (len(PASSED), len(PASSED)))
