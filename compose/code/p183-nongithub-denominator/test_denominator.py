#!/usr/bin/env python3
"""Controls for P183.  Rule 3 of P126: a suite that does not print its own total invites a
hand-rolled instrument, so this one prints `N/N checks passed`.

Rule 2 of P126: a positive control only enables an instrument if it exercises the case where
the instrument can FAIL.  The case here is D4 -- a backticked token that has npm/PyPI SHAPE
and is not a package (an MCP tool name, a Moodle setting, a branch, a repo short name).  The
controls below assert that the DECLARATION build rejects each of those AND that it accepts a
real registry citation in each of the four forms this KB actually writes.
"""
import sys
from denominator import pkg_names, tables, ENTITY_HDR

ACCEPT = [
    ('npmjs.com/package with a scope',
     '| x | [`@ink-waffle/moodle-mcp`](https://www.npmjs.com/package/@ink-waffle/moodle-mcp) | MIT |',
     '@ink-waffle/moodle-mcp'),
    ('pypi.org/project',
     '| x | [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) (oficial) | AGPL-3.0 |',
     'openedx-mcp'),
    ('registry.npmjs.org with percent-encoded scope',
     '| **`@eduware/oneroster`** | [registry.npmjs.org](https://registry.npmjs.org/@eduware%2Foneroster) |',
     '@eduware/oneroster'),
    ('the explicit channel marker form this KB writes',
     '| `bruchris/canvas-lms-mcp` | **8** | `canvas-lms-mcp` (npm) | **62** |',
     'canvas-lms-mcp'),
    ('registry.npmjs.org with a /latest suffix, which must be stripped',
     '| opencode-sit | npm [`opencode-sit`](https://registry.npmjs.org/opencode-sit/latest) |',
     'opencode-sit'),
]

# D4 -- every one of these has npm/PyPI shape and is NOT a package.  Each was returned by the
# shape-only build, which is kept beside this file as a dated negative control.
REJECT = [
    ('D4 MCP tool name', '| `server_status` | `GET /api/ping` | `fields` | — | true |'),
    ('D4 MCP tool name with underscores', '| `record_evidence` | `POST /api/xapi/statement` |'),
    ('D4 Moodle setting', '| Consultas de `post_manually` / `posting_policy` | **0** | **0** |'),
    ('D4 Moodle setting, negated form', '| Si `use_rubric_for_grading` es falso | aborta |'),
    ('D4 git branch name', '| `upgrade-mcp-v2`, activo | FRIO |'),
    ('D4 repo short name', '| **canvas-mcp** | `BartMassey-upstream` · `lindsay-cheng` |'),
    ('D4 a bare dashed word in prose', '| la capa de `knowledge-tracing` se mide aparte |'),
]

TABLE = '''| Pieza | Licencia | ★ |
|---|---|---|
| a | MIT | 1 |
| b | MIT | 2 |

| Magnitud | Valor |
|---|---|
| filas | 578 |
'''

def main():
    n = ok = 0
    for name, row, want in ACCEPT:
        n += 1
        got = pkg_names(row)
        if want in got:
            ok += 1; print(f'PASS accept: {name}')
        else:
            print(f'FAIL accept: {name}: want {want!r} in {got!r}')

    for name, row in REJECT:
        n += 1
        got = pkg_names(row)
        if got == []:
            ok += 1; print(f'PASS reject: {name}')
        else:
            print(f'FAIL reject: {name}: expected nothing, got {got!r}')

    # LAYER 2 -- an entity table is told from a method table by its HEADER, and counting the
    # method rows is what inflated the 249 figure.
    blocks = list(tables(TABLE.split('\n')))
    n += 1
    if len(blocks) == 2:
        ok += 1; print('PASS layer: two tables parsed from header+separator pairs')
    else:
        print(f'FAIL layer: parsed {len(blocks)} tables, want 2')
    n += 1
    if ENTITY_HDR.search(blocks[0][1]) and not ENTITY_HDR.search(blocks[1][1]):
        ok += 1; print('PASS layer: `Pieza · Licencia · ★` is an entity table, `Magnitud · Valor` is not')
    else:
        print('FAIL layer: entity/method classification wrong')

    # The negative control, as its own assertion: the shape-only build accepts what the
    # declaration build rejects.  Without this, "the controls pass" would not show that the
    # two builds differ -- which is the whole finding of D4.
    n += 1
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            'shapeonly', 'shape-only.NEGATIVE-CONTROL-2026-10-03.py')
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        leaked = [nm for nm, row in REJECT if m.pkg_names(row)]
        if len(leaked) >= 5:
            ok += 1
            print(f'PASS negative control: the shape-only build leaks {len(leaked)} of '
                  f'{len(REJECT)} non-packages that this build rejects')
        else:
            print(f'FAIL negative control: shape-only leaked only {len(leaked)}')
    except Exception as e:
        print(f'FAIL negative control: {e}')

    print(f'\n{ok}/{n} checks passed')
    return 0 if ok == n else 1

if __name__ == '__main__':
    sys.exit(main())
