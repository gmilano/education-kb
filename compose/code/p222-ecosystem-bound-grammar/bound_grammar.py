"""p222 - ACTION RP's instrument, and it exists because RP's own premise was wrong.

`ACTION RP` (p221, highest-priority for p222) asked: republish the `-only` / `-or-later`
bound on every GNU cell whose prescribed channel can answer. Limb `1` was `20`+ of the
first `40` rows swept resolving to an explicit bound - which would have made p221's
`94.3%` bare share a reading backlog.

It fires limb `2`. Of the first `40` bare-GNU rows swept against their prescribed
channel, **`8`** resolved to an explicit bound in SPDX terms. Not a backlog.

But the sweep refuted the question rather than answering it, because `-only` /
`-or-later` is an SPDX spelling and SPDX is one ecosystem's grammar among several. The
same bound is encoded four different ways on these shelves:

    ecosystem        or-later is spelled            only is spelled
    ---------------------------------------------------------------------------
    SPDX             GPL-3.0-or-later               GPL-3.0-only
    (npm, composer,  AGPL-3.0-or-later              GPL-2.0-only
     pyproject)      ...and ABSENCE of a suffix means NOTHING WAS SAID
    ---------------------------------------------------------------------------
    CRAN             GPL (>= 3)                     GPL-3
    (DESCRIPTION)                                   ...absence of `(>= n)` is a
                                                    POSITIVE only, not a silence
    ---------------------------------------------------------------------------
    Odoo             'LGPL-3 or any later version'  'LGPL-3'
    (__manifest__)   closed vocabulary              ...same shape, same meaning:
                                                    bare is only, not unknown
    ---------------------------------------------------------------------------
    PyPI             GNU ... v3 or later (AGPLv3+)  GNU ... v3 (AGPLv3)
    classifiers      the `+` carries it             no `+` = only
    ---------------------------------------------------------------------------
    GNU header       "either version 3 ... or (at    "version 2 of the License
    (prose grant)     your option) any later"         (non-upgradable)"

p221's `parse_range()` reads a bare `GPL-3` as `bound='unspecified'` in every one of
them. For SPDX and for a prose grant that is correct. For CRAN and for Odoo it is
WRONG: those two ecosystems encode `only` by omission, so `unspecified` reports a
silence where the source made a positive statement.

So p221's census over-counts. `2 208` bare GNU cell-mentions is the right count of
BARE TOKENS; it is not the count of UNSPECIFIED GRANTS, because some of those tokens
came from an ecosystem in which bare means only.

Seventh consecutive unit mismatch in this KB's headline series:

    T218-1  token            vs  axis
    T218-3  heading level    vs  pass boundary
    T218-4  line             vs  sentence
    T219-5  token            vs  packaging mode
    T220    repository       vs  FILE
    T221    licence FAMILY   vs  licence VERSION RANGE
    T222    licence TOKEN    vs  the token's ECOSYSTEM GRAMMAR   <- this instrument

The consequence for a studio is not academic. `openeducat/openeducat_erp` is the
single most-mentioned GNU row on these shelves (`72` `LGPL-3.0` cells) and its two
module-level channels DISAGREE under this reading: `openeducat_core/__manifest__.py`
declares `'license': 'LGPL-3'` - Odoo's `only` - while the same file's header grants
"either version 3 ... or (at your option) any later version". Read without the
grammar, those two agree. Read with it, they are a RANGE-CONFLICT on the row every
Odoo-based education recipe here is built on.
"""

import re

# `GPL (>= 2)`, `LGPL (>= 2.1)`, `GPL (>=3)` - CRAN's range form. CRAN also accepts
# `GPL-2 | GPL-3`, a DISJUNCTION, which is neither bound: it is a choice of two
# grants and has to be reported as such rather than collapsed onto one.
_CRAN_RANGE = re.compile(r'\(\s*>=\s*([0-9](?:\.[0-9])?)\s*\)')
_CRAN_OR    = re.compile(r'\|')
_CRAN_TOKEN = re.compile(r'\b(A?GPL|LGPL)\s*-\s*([0-9](?:\.[0-9])?)\b', re.I)

# Odoo's manifest `license` key takes a CLOSED vocabulary. Only the members that can
# carry a GNU bound are listed; `OEEL-1` / `OPL-1` / `Other proprietary` are not GNU
# and must come back out of scope rather than as a silent grant.
_ODOO_VOCAB = {
    'gpl-2':                        ('GPL',  '2.0', 'only'),
    'gpl-2 or any later version':   ('GPL',  '2.0', 'or-later'),
    'gpl-3':                        ('GPL',  '3.0', 'only'),
    'gpl-3 or any later version':   ('GPL',  '3.0', 'or-later'),
    'agpl-3':                       ('AGPL', '3.0', 'only'),
    'lgpl-3':                       ('LGPL', '3.0', 'only'),
    'lgpl-3 or any later version':  ('LGPL', '3.0', 'or-later'),
}

# A PyPI trove classifier carries the bound in a `+` inside the parenthesis:
#   "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)"
#   "License :: OSI Approved :: GNU Affero General Public License v3"
_CLASSIFIER = re.compile(
    r'License\s*::\s*OSI Approved\s*::\s*GNU\s+(.+?)(?:\s*\(([^)]*)\))?\s*$', re.I)

_SPDX = re.compile(r'\b(A?GPL|LGPL)-([0-9](?:\.[0-9])?)(-only|-or-later)?\b', re.I)

GRAMMARS = ('spdx', 'cran', 'odoo', 'classifier', 'prose')

# Which file each grammar is read out of. This is the p221 prescription table's
# missing column: the table said WHERE the licence field is, not WHICH GRAMMAR the
# value is written in, and that is the column the bound actually lives in.
CHANNEL_GRAMMAR = {
    'composer.json':   'spdx',
    'package.json':    'spdx',
    'pyproject.toml':  'spdx',        # `license = {text = "AGPL-3.0-only"}`
    'DESCRIPTION':     'cran',
    '__manifest__.py': 'odoo',
    'setup.py':        'classifier',
    'setup.cfg':       'classifier',
    'version.php':     'prose',       # Moodle's mandated GPL header
    'pom.xml':         'prose',
}


def _family(tok):
    t = str(tok or '').lower()
    if 'affero' in t or re.search(r'\bagpl', t):
        return 'AGPL'
    if 'lesser' in t or re.search(r'\blgpl', t):
        return 'LGPL'
    if re.search(r'\bgpl', t) or 'general public license' in t:
        return 'GPL'
    return None


def _norm_ver(v):
    if v is None:
        return None
    v = str(v)
    return v if '.' in v else v + '.0'


def read_bound(value, grammar):
    """Read one licence DECLARATION under one ecosystem's GRAMMAR.

    Returns {'family', 'version', 'bound', 'grammar', 'gnu'} where bound is
    'or-later' / 'only' / 'unspecified' / 'disjunction'.

    The whole point of the instrument is that `value` alone does not determine
    `bound`: `'LGPL-3'` is `unspecified` under `spdx` and `only` under `cran` and
    `odoo`. A caller that does not know the grammar must not call this.
    """
    if grammar not in GRAMMARS:
        raise ValueError(f'unknown grammar: {grammar!r}')
    raw = re.sub(r'\s+', ' ', str(value or '')).strip()
    out = {'family': None, 'version': None, 'bound': None,
           'grammar': grammar, 'gnu': False}
    if not raw:
        return out

    if grammar == 'odoo':
        hit = _ODOO_VOCAB.get(raw.lower().strip('\'" '))
        if hit is None:
            return out                      # not a GNU member of the closed vocabulary
        fam, ver, bound = hit
        return {'family': fam, 'version': ver, 'bound': bound,
                'grammar': grammar, 'gnu': True}

    if grammar == 'cran':
        fam = _family(raw)
        if fam is None:
            return out
        m = _CRAN_TOKEN.search(raw)
        ver = _norm_ver(m.group(2)) if m else None
        rng = _CRAN_RANGE.search(raw)
        if rng:
            return {'family': fam, 'version': _norm_ver(rng.group(1)),
                    'bound': 'or-later', 'grammar': grammar, 'gnu': True}
        if _CRAN_OR.search(raw):
            # `GPL-2 | GPL-3` is a CHOICE of grants, not a bound on one
            return {'family': fam, 'version': ver, 'bound': 'disjunction',
                    'grammar': grammar, 'gnu': True}
        # bare token under CRAN's grammar is a POSITIVE only
        return {'family': fam, 'version': ver, 'bound': 'only',
                'grammar': grammar, 'gnu': True}

    if grammar == 'classifier':
        m = _CLASSIFIER.search(raw)
        if m is None:
            return out
        name, paren = m.group(1), m.group(2) or ''
        fam = _family(name)
        if fam is None:
            return out
        vm = re.search(r'\bv\s*([0-9](?:\.[0-9])?)', name, re.I)
        ver = _norm_ver(vm.group(1)) if vm else None
        later = ('or later' in name.lower()) or paren.strip().endswith('+')
        return {'family': fam, 'version': ver,
                'bound': 'or-later' if later else 'only',
                'grammar': grammar, 'gnu': True}

    if grammar == 'spdx':
        m = _SPDX.search(raw)
        if m is None:
            return out
        fam = _family(m.group(1))
        suffix = (m.group(3) or '').lower()
        bound = 'or-later' if suffix == '-or-later' else (
                'only' if suffix == '-only' else 'unspecified')
        return {'family': fam, 'version': _norm_ver(m.group(2)),
                'bound': bound, 'grammar': grammar, 'gnu': True}

    # grammar == 'prose': a GNU header's own words. Delegated in spirit to p221's
    # `parse_range`, kept here so this module is usable standalone.
    fam = _family(raw)
    if fam is None:
        return out
    vm = re.search(r'(?:version|v)\s*([0-9](?:\.[0-9])?)', raw, re.I)
    if vm is None:
        m = _SPDX.search(raw)
        vm = m
        ver = _norm_ver(m.group(2)) if m else None
    else:
        ver = _norm_ver(vm.group(1))
    if re.search(r'or\s*\(at\s*your\s*option\)\s*any\s*later|any\s+later\s+version'
                 r'|\bor[-\s]later\b', raw, re.I):
        bound = 'or-later'
    elif re.search(r'non[-\s]?upgrad|\bonly\b|\bno\s+later\s+version\b', raw, re.I):
        bound = 'only'
    else:
        bound = 'unspecified'
    return {'family': fam, 'version': ver, 'bound': bound,
            'grammar': grammar, 'gnu': True}


def grammar_for(filename):
    """Which grammar a value read out of `filename` is written in."""
    return CHANNEL_GRAMMAR.get(str(filename or '').strip())


def reconcile(readings):
    """Several channels on ONE row -> one verdict a studio can act on.

    `readings` is an iterable of (filename, value). Each is read under ITS OWN
    grammar, which is the whole correction this instrument makes; p221 read every
    channel under one.

      NO-GNU-CHANNEL   nothing GNU was readable - say so, do not guess
      AGREE            every GNU channel gives the same family, version and bound
      GRANT-CONFLICT   the channels differ on family or version
      RANGE-CONFLICT   same grant, channels differ on the bound  <- openeducat
      BOUND-RESOLVED   exactly one bound is stated and nothing contradicts it
      UNSPECIFIED-AT-SOURCE  every channel is silent on the bound; the gap is in
                             the SOURCE, and asking the maintainer is the only route
    """
    seen = []
    for fname, value in readings:
        g = grammar_for(fname)
        if g is None:
            continue
        r = read_bound(value, g)
        if r['gnu']:
            r['file'] = fname
            seen.append(r)
    if not seen:
        return {'state': 'NO-GNU-CHANNEL', 'readings': []}

    fams = {r['family'] for r in seen}
    vers = {r['version'] for r in seen if r['version']}
    if len(fams) > 1 or len(vers) > 1:
        return {'state': 'GRANT-CONFLICT', 'readings': seen}

    bounds = {r['bound'] for r in seen}
    stated = bounds - {'unspecified'}
    if len(stated) > 1:
        return {'state': 'RANGE-CONFLICT', 'readings': seen}
    if not stated:
        return {'state': 'UNSPECIFIED-AT-SOURCE', 'readings': seen}
    if len(bounds) == 1:
        return {'state': 'AGREE', 'bound': stated.pop(), 'readings': seen}
    return {'state': 'BOUND-RESOLVED', 'bound': stated.pop(), 'readings': seen}


def blocks_gpl3_host(family, version, bound):
    """May this row enter a GPLv3 host - Moodle, Chamilo, ILIAS?

    This is `ACTION RQ`'s question and the answer that earns the sweep: a
    `GPL-2.0-only` library CANNOT, and a bare `GPL-2.0` cell does not say so.
    Returns True (blocked), False (fine), or None (the bound is genuinely unknown,
    which is what an SOW must carry rather than an optimistic False).
    """
    if bound == 'or-later':
        return False
    if bound == 'only':
        if family == 'LGPL':
            return False                 # LGPL-any links into a GPLv3 host
        return _norm_ver(version) != '3.0'
    return None
