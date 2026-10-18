"""Offline controls for `p229-grant-ladder-reach`. No network, so `make hooks` can run them.

Controls that must NOT fire are the point: a gate that fires on everything has found nothing.
"""
import re
import subprocess
import sys

HERE = __file__.rsplit('/', 1)[0]
sys.path.insert(0, HERE)
import manifest_grant as mg          # noqa: E402
import sx_withdrawn_gate as sx       # noqa: E402
import sz_query_key as sz            # noqa: E402

FAILED = []


def check(name, got, expect):
    ok = got == expect
    if not ok:
        FAILED.append('%s: got %r expected %r' % (name, got, expect))
    print('%s %-62s %s' % ('ok  ' if ok else 'FAIL', name, '' if ok else '-> %r != %r' % (got, expect)))


# ---- T229-M1: the Moodle bound must be reachable (the draft's lazy quantifier hid it) ----
MOODLE_LATER = ('$plugin->version = 2026; // GNU General Public License as published by the '
                'Free Software Foundation, either version 3 of the License, or (at your '
                'option) any later version.')
MOODLE_ONLY = ('// GNU General Public License, either version 2 of the License. '
               'Non-upgradable.')
check('T229-M1 or-later is reachable', mg.read('version.php', MOODLE_LATER)['value'], 'GPL-3.0-or-later')
check('T229-M1 only is not inflated', mg.read('version.php', MOODLE_ONLY)['value'], 'GPL-2.0')
check('T229-M1 no GNU header -> silent', mg.read('version.php', 'defined("MOODLE_INTERNAL");')['state'], 'NO-FIELD')

# ---- a 200 is not a grant -------------------------------------------------------------
check('manifest 200 without a licence key is SILENT',
      mg.read('package.json', '{"name":"x"}')['state'], 'NO-FIELD')
check('manifest with a licence key resolves',
      mg.read('package.json', '{"name":"x","license":"MIT"}')['value'], 'MIT')
check('composer array is a disjunction',
      mg.read('composer.json', '{"name":"x","license":["OSL-3.0","AFL-3.0"]}')['value'],
      'OSL-3.0 | AFL-3.0')

# ---- T229-M2: the foreign manifest ----------------------------------------------------
# 🔴 p280 (`p279`'s declared item 2): FOUR OF THESE CONTROLS NAMED A REAL REPOSITORY AND
# ASSERTED A PAYLOAD IT DOES NOT SERVE.  `p279` found the worst one: the scope control
# asserted `{"name":"@dmontgomery40/mcp-canvas-lms"}` and expected `True`, while the
# repository's real root `package.json` declares `"name": "canvas-mcp-server"` -- on which
# `attributable` returns **False**.  So the control that was supposed to prove
# *"a scoped npm name attributes fine"* passed on an invented payload while the real one
# exercised the opposite branch, which is exactly the false positive `p279` then had to
# neutralise by making the name RECORDED instead of ENFORCED.
#
# 🔵 THE DISTINCTION THAT MAKES THIS A CLASS AND NOT A TYPO.  A control whose subject is
# SYNTHETIC (`a/b`, `{"name":"x"}`) is a unit test of the predicate and is legitimate as
# written.  A control that NAMES A REAL SLUG makes a claim about that repository, and a
# claim about a repository has to come from the repository's bytes.  The four below are of
# the second kind, so they read CAPTURED PAYLOADS -- byte-for-byte, with
# `slug/ref/head_sha/sha256/date` recorded in `pass280-package-provenance/fixtures/
# PROVENANCE.tsv` -- and cannot drift from what the repository serves again.
FIXTURES = HERE + '/../pass280-package-provenance/fixtures'


def payload(name):
    """The captured bytes, or a LOUD failure.  A missing fixture must never read as a pass."""
    try:
        return open(FIXTURES + '/' + name, encoding='utf-8').read()
    except OSError as e:
        FAILED.append('fixture %s unreadable: %s' % (name, e))
        return ''


# 🟢 REAL, and it reproduces the finding `T229-M2` was built on: a fork serving upstream's
# manifest at its own root.  Captured 2026-10-18 at `55ad5acbc42e`.
check('T229-M2 upstream skeleton is NOT attributable (REAL payload)',
      mg.attributable('LMS-Laravel/LMS-Laravel', 'composer.json',
                      payload('LMS-Laravel.root.composer.json'))[0], False)
# 🟢 REAL.  `p229` asserted the licence array as `["OSL-3.0"]`; the repository serves TWO
# elements, so the disjunction is asserted here as well -- the truncated literal could not
# have caught a parser that drops the tail.
check('T229-M2 magento fork is NOT attributable (REAL payload)',
      mg.attributable('alfredang/ai-mms', 'composer.json',
                      payload('ai-mms.root.composer.json'))[0], False)
check('T229-M2 the REAL composer array is a two-term disjunction',
      mg.read('composer.json', payload('ai-mms.root.composer.json'))['value'],
      'OSL-3.0 | AFL-3.0')
# 🟢 REAL, and it is the genuine scoped-name case: `p229` asserted the UNSCOPED spelling
# `sisu-mcp`; the repository serves `@ink-waffle/sisu-mcp`.  Same verdict, real bytes --
# and this, not `mcp-canvas-lms`, is what exercises the `@scope/pkg` branch.
check('T229-M2 CONTROL scoped own name IS attributable (REAL payload)',
      mg.attributable('ink-waffle/sisu-mcp', 'package.json',
                      payload('sisu-mcp.root.package.json'))[0], True)
# 🔴 REAL, AND THE VERDICT IS THE OPPOSITE OF WHAT THE INVENTED CONTROL ASSERTED.  This is
# `attributable`'s documented FALSE POSITIVE when used as a REJECTION, pinned so that any
# future pass tempted to enforce the name channel meets it: naming a package differently
# from its repository is ordinary.
check('T229-M2 the REAL mcp-canvas-lms root name is NOT attributable',
      mg.attributable('DMontgomery40/mcp-canvas-lms', 'package.json',
                      payload('mcp-canvas-lms.root.package.json'))[0], False)
check('T229-M2 and the REAL declared name is canvas-mcp-server, not the scoped slug',
      mg.manifest_owner('package.json', payload('mcp-canvas-lms.root.package.json')),
      'canvas-mcp-server')
# 🟢 SYNTHETIC BY DESIGN and left as written: the subject is the predicate, not a repository.
check('T229-M2 CONTROL silence is not a counter-claim',
      mg.attributable('a/b', 'package.json', '{"license":"MIT"}')[0], True)

# ---- ACTION SX: the marker must stop suppressing, the five subjects must not ----------
print('\n-- ACTION SX gate (9 controls, 6 of which must NOT fire) --')
if sx.run_controls():
    FAILED.append('sx_withdrawn_gate controls')

# ---- T229-SX1: the positional rule ----------------------------------------------------
TOK = re.compile(r'`?\b((?:A?GPL|LGPL)-[0-9](?:\.[0-9])?(?:-only|-or-later)?|MIT|Apache-2\.0'
                 r'|CC-BY-SA-4\.0|Elastic-2\.0)\b`?')
print('\n-- T229-SX1 positional rule --')
check('T229-SX1 live value is the FIRST token, not the last',
      sx.cell_token('| `a/b` | **MIT** was GPL-3.0<!--corrected--> |', TOK), 'MIT')
check('T229-SX1 trailing narrative does not win',
      sx.cell_token('| `a/b` | **AGPL-3.0** <!--corrected--> | published `GPL-3.0` until p228 |', TOK),
      'AGPL-3.0')

# ---- ACTION SZ ------------------------------------------------------------------------
print('\n-- ACTION SZ query-key gate (6 controls) --')
if sz.main():
    FAILED.append('sz_query_key controls')

# ---- the ladder's reach must stay PRINTABLE (T272) ------------------------------------
print('\n-- reach --')
out = subprocess.run([HERE + '/ladder.sh', '--reach'], capture_output=True, text=True).stdout
# p247 widened Tier A by ONE name -- `LICENSE-CODE`, measured on `microsoft/autogen`, whose
# root `LICENSE` is CC-BY-4.0 (the DOCS licence, 18 650 B) and whose `LICENSE-CODE` is MIT
# (the CODE licence).  The count is re-asserted rather than loosened on purpose: a reach that
# grows silently is a reach nobody re-reads (T272).
# p256 widened Tier A by TEN names and SEVEN of them were already proven elsewhere in this
# base before being added here -- `LICENSE.TXT` is `P1057`'s own path, published at p189 with
# `openedx/XBlock` and still absent from this ladder 67 passes later, which is how p256 came
# within one keystroke of publishing `NO_LICENCE_FILE` on `openedx/xblock-sdk`.  The count is
# re-asserted and not loosened, for the reason above, and the JOIN that stops the ladder
# drifting from the proven set again is `compose/code/pass256-ladder-closure/`.
check('T272 reach is printable', out.startswith('tierA=26 tierB=15 tierC=10 total=51'), True)
check('T272 LICENSE-CODE is in the printed reach (p247)', 'LICENSE-CODE' in out, True)
check('T272 the code grant is probed BEFORE the bare LICENSE (p247)',
      out.index('LICENSE-CODE') < out.index('\nLICENSE\n'), True)

print('\n%s' % ('ALL CONTROLS PASS' if not FAILED else 'FAILURES:\n  ' + '\n  '.join(FAILED)))
sys.exit(1 if FAILED else 0)
