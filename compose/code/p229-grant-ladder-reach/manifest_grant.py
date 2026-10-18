"""`ACTION SW`, step 2 — read the DECLARATION out of a manifest payload.

p222 established that a licence value is written in one of five ecosystem grammars and
shipped `bound_grammar.py` to read a VALUE under a GRAMMAR. What it does not do — on
purpose, because it is a grammar library and not a parser — is get the value out of the
FILE. That extraction is the vocabulary this pass adds, and it is the reason a tier-C hit
is not yet a grant:

    a manifest returns `200` whether or not it declares a licence at all.

So `NO-FIELD` is a first-class outcome here. Counting a 200 as a resolution would repeat
p228's own headline (a token whose subject is not a grant) one layer down.

P237: no classifier is written here. Bodies go to `lib/license_family.sh`; GNU bounds go to
p222's `read_bound`. This file only locates the value.
"""
import json
import re
import sys

sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/p222-ecosystem-bound-grammar')
import bound_grammar  # noqa: E402

# Moodle's mandated plugin header. `version.php` carries no licence FIELD: it carries the
# GNU prose block, which is p222's `prose` grammar, and the bound lives in the same words.
#
# 🔴 `T229-M1` — a defect this file's FIRST draft shipped, caught by a control before any
# cell was published. The or-later clause was a trailing OPTIONAL group behind a LAZY
# `.{0,120}?`:
#
#     either\s+version\s+(\d).{0,120}?(any\s+later\s+version)?
#
# A lazy quantifier stops at the earliest position where the REST of the pattern can
# match, and a trailing optional group matches the empty string right there — so the
# clause was unreachable and every Moodle plugin read `unspecified`. That is the same
# shape as the harvester defect this pass found upstream (`T229-1`, a non-greedy repo
# name against a terminator class containing `.`): a lazy quantifier against a permissive
# terminator always stops early. So the bound gets its OWN anchored probe inside a
# measured window, never a tail of the version match.
_MOODLE_VER = re.compile(
    r'GNU\s+General\s+Public\s+License.{0,400}?either\s+version\s+(\d)', re.I | re.S)
_MOODLE_LATER = re.compile(r'any\s+later\s+version', re.I)
_MOODLE_WINDOW = 200
_TROVE = re.compile(r'License\s*::\s*OSI Approved\s*::\s*([^\'"\n]+)')
_KV = re.compile(r'''^\s*licen[cs]e\s*[:=]\s*['"]?([^'"\n,}]+)''', re.I | re.M)


def extract(filename, payload):
    """-> (value, grammar, note). `value is None` means the channel is SILENT."""
    name = filename.rsplit('/', 1)[-1]

    if name in ('package.json', 'composer.json'):
        try:
            d = json.loads(payload)
        except ValueError:
            return (None, 'spdx', 'unparseable JSON')
        v = d.get('license') or d.get('licence')
        if isinstance(v, list):              # composer allows a DISJUNCTION as an array
            return (' | '.join(str(x) for x in v), 'spdx', 'array = disjunction')
        if isinstance(v, dict):              # npm's deprecated {type, url} form
            v = v.get('type')
        if not v and isinstance(d.get('licenses'), list):
            ls = [x.get('type', '') if isinstance(x, dict) else str(x) for x in d['licenses']]
            return (' | '.join(filter(None, ls)) or None, 'spdx', 'deprecated `licenses` array')
        return (v or None, 'spdx', '' if v else 'no `license` key')

    if name == 'version.php':
        m = _MOODLE_VER.search(payload)
        if not m:
            return (None, 'prose', 'no GNU header in version.php')
        ver = m.group(1)
        window = payload[m.end():m.end() + _MOODLE_WINDOW]
        later = bool(_MOODLE_LATER.search(window))
        return ('GPL-%s.0%s' % (ver, '-or-later' if later else ''), 'prose',
                'Moodle mandated header; bound probed in a %d B window' % _MOODLE_WINDOW)

    if name in ('setup.py', 'setup.cfg', 'pyproject.toml'):
        m = _TROVE.search(payload)
        if m:
            return (m.group(1).strip(), 'classifier', 'trove classifier')
        m = _KV.search(payload)
        return ((m.group(1).strip() if m else None),
                'spdx', 'license key' if m else 'no licence field')

    if name == 'DESCRIPTION':
        m = re.search(r'^License:\s*(.+)$', payload, re.I | re.M)
        return ((m.group(1).strip() if m else None), 'cran', '' if m else 'no License: field')

    if name == '__manifest__.py':
        m = re.search(r'''['"]license['"]\s*:\s*['"]([^'"]+)''', payload)
        return ((m.group(1).strip() if m else None), 'odoo', '' if m else 'no license key')

    if name in ('Cargo.toml', 'pubspec.yaml'):
        m = _KV.search(payload)
        return ((m.group(1).strip() if m else None), 'spdx', '' if m else 'no licence field')

    return (None, None, 'channel not in the grammar table')


def read(filename, payload):
    """-> dict with the declared value, its grammar and, for GNU, p222's bound."""
    value, grammar, note = extract(filename, payload)
    out = {'file': filename, 'value': value, 'grammar': grammar, 'note': note}
    if value is None:
        out['state'] = 'NO-FIELD'
        return out
    if grammar in bound_grammar.GRAMMARS:
        r = bound_grammar.read_bound(value, grammar)
        out['state'] = 'GNU' if r['gnu'] else 'NON-GNU'
        out['family'], out['version'], out['bound'] = r['family'], r['version'], r['bound']
    else:
        out['state'] = 'NON-GNU'
    return out


# 🔵 p279: this block is now gated on the flag's ABSENCE.  `attributable` is defined
# BELOW it (the `T229-M2` section), so the new mode cannot be served from here -- and a
# second `if __name__` block appended at EOF cannot be reached either, because this one
# reads `sys.argv[1]` as a file and dies on the flag first.  Two drafts of the p279 CLI
# failed that way: dead code, then a NameError.  Gating here is what makes EOF reachable.
if __name__ == '__main__' and '--attributable' not in sys.argv:
    print('\t'.join(['slug', 'file', 'state', 'value', 'family', 'bound', 'note']))
    for line in open(sys.argv[1], encoding='utf-8'):
        slug, path, body_path = line.rstrip('\n').split('\t')
        try:
            payload = open(body_path, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        r = read(path, payload)
        print('\t'.join([slug, path, r['state'], str(r.get('value') or '-'),
                         str(r.get('family') or '-'), str(r.get('bound') or '-'), r['note']]))


# ---------------------------------------------------------------------------------------
# 🔴 `T229-M2` — THE FOREIGN MANIFEST, a SEVENTH non-grant subject, found by the only
# disagreement this pass's `ACTION SW` gate produced.
#
# `alfredang/ai-mms` carries a cell reading `MIT`. Its root `composer.json` declares
# `"license": ["OSL-3.0", "AFL-3.0"]`, which looks like a live, commercially expensive
# defect in the permissive direction — until the SAME file's second line is read:
#
#     "name": "openmage/magento-lts"
#
# The repository is a Magento fork and the manifest it serves at its root is UPSTREAM's.
# The licence is real, first-hand and correctly parsed; it is simply not a statement about
# `alfredang/ai-mms`. p224's `T224-3` is the same unit error one channel over (a token
# belonging to an R dependency); p228 enumerated five subjects a licence token can have
# and this is the manifest-channel member of that family.
#
# The control is nearly free and nothing in this base had it: a manifest's `name` is a
# claim about WHOSE manifest it is, so compare it with the slug before attributing.
def manifest_owner(filename, payload):
    """-> the project this manifest claims to BE, or None when it does not say."""
    name = filename.rsplit('/', 1)[-1]
    if name in ('package.json', 'composer.json'):
        try:
            return (json.loads(payload) or {}).get('name') or None
        except ValueError:
            return None
    if name in ('pyproject.toml', 'setup.cfg', 'Cargo.toml'):
        m = re.search(r'''^\s*name\s*=\s*['"]?([^'"\n]+)''', payload, re.M)
        return m.group(1).strip() if m else None
    return None


def _norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def attributable(slug, filename, payload):
    """-> (ok, declared_name). False when the manifest names a DIFFERENT project.

    Deliberately permissive: a manifest that does not name itself is attributed to the
    repository, because silence is not a counter-claim. Only a NAME that matches neither
    the owner nor the repository half of the slug refuses attribution.
    """
    declared = manifest_owner(filename, payload)
    if not declared:
        return (True, None)
    owner, _, repo = slug.partition('/')
    d = _norm(declared)
    # `@scope/pkg` and `vendor/pkg` forms: compare both halves independently.
    parts = [p for p in re.split(r'[/@]', declared) if p]
    if _norm(repo) in d or d in _norm(repo) or any(_norm(p) == _norm(repo) for p in parts):
        return (True, declared)
    if any(_norm(p) == _norm(owner) for p in parts):
        return (True, declared)
    return (False, declared)


# 🟢 p279: the `attributable` CLI, so a SHELL instrument can REUSE `T229-M2` instead of
# re-implementing the name check.  `p279` built the per-package manifest walk and counted a
# monorepo's VENDORED dependency manifests as the repository's own declarations -- `moment`,
# `swiper`, `tailwindcss` and three CKEditor builds under `public/assets/libs/`, plus a
# bundled `pyodide` under `ui/static/`.  `T229-M2` already answers that question -- *"a
# manifest's `name` is a claim about whose manifest it is"* -- and it answers it by NAME,
# which catches a vendored directory that no path vocabulary enumerates.
# 🔵 It sits at EOF because `attributable` is defined above it and not above the other block.
#   usage: manifest_grant.py --attributable <slug> <manifest-basename> <file>
#   exit 0 = attributable to this repository, 1 = FOREIGN, 2 = usage
if __name__ == '__main__' and '--attributable' in sys.argv:
    import pathlib as _pl
    _i = sys.argv.index('--attributable')
    try:
        _slug, _fname, _path = sys.argv[_i + 1], sys.argv[_i + 2], sys.argv[_i + 3]
    except IndexError:
        print('usage: manifest_grant.py --attributable <slug> <basename> <file>',
              file=sys.stderr)
        sys.exit(2)
    _ok, _declared = attributable(
        _slug, _fname, _pl.Path(_path).read_text(encoding='utf-8', errors='replace'))
    print(_declared or '-')
    sys.exit(0 if _ok else 1)
