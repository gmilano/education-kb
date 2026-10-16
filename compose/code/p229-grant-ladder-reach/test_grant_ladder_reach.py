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
check('T229-M2 upstream skeleton is NOT attributable',
      mg.attributable('LMS-Laravel/LMS-Laravel', 'composer.json',
                      '{"name":"laravel/laravel","license":"MIT"}')[0], False)
check('T229-M2 magento fork is NOT attributable',
      mg.attributable('alfredang/ai-mms', 'composer.json',
                      '{"name":"openmage/magento-lts","license":["OSL-3.0"]}')[0], False)
check('T229-M2 CONTROL own name IS attributable',
      mg.attributable('ink-waffle/sisu-mcp', 'package.json',
                      '{"name":"sisu-mcp","license":"MIT"}')[0], True)
check('T229-M2 CONTROL npm scope IS attributable',
      mg.attributable('DMontgomery40/mcp-canvas-lms', 'package.json',
                      '{"name":"@dmontgomery40/mcp-canvas-lms"}')[0], True)
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
check('T272 reach is printable', out.startswith('tierA=16 tierB=15 tierC=10 total=41'), True)
check('T272 LICENSE-CODE is in the printed reach (p247)', 'LICENSE-CODE' in out, True)
check('T272 the code grant is probed BEFORE the bare LICENSE (p247)',
      out.index('LICENSE-CODE') < out.index('\nLICENSE\n'), True)

print('\n%s' % ('ALL CONTROLS PASS' if not FAILED else 'FAILURES:\n  ' + '\n  '.join(FAILED)))
sys.exit(1 if FAILED else 0)
