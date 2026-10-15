#!/usr/bin/env python3
"""p219 - ACTION QV's instrument, built for the unit the thing actually has.

ACTION QV asked a RISK question: does a licence-unknown repo sit on a reciprocal
upstream, making it a dead end even if the author answers?

p219's answer is that the question has a cheaper half, and it must be asked first.
An upstream is a CHANNEL HINT before it is a risk: the ecosystem that makes a repo
reciprocal is the same ecosystem that prescribes WHERE its licence goes. On 3 of the
4 derivative rows found this pass, reading that channel returned a grant, so the
"dead end" never arose and no issue needed opening.

Two functions, in the order they must be called:

    relation(readme, slug)  -> how the repo stands to the upstream
    channels(upstream, slug)-> which paths to read BEFORE asking a maintainer anything

RELATION is the field p218's naive token grep would have got wrong twice, in opposite
directions, and that is why it exists:

  * `loyaniu/moodle-mcp` - slug begins `moodle-`, so a slug-prefix rule calls it a
    Moodle plugin. It is a Python MCP server that calls `webservice/rest/server.php`
    with a token. It derives nothing. OVER-FIRE.
  * `Hesham0-0Nasser/tutor-lms-mcp` - README says "MCP server" and "API", so a
    keyword rule calls it an integration. Its first line says "WordPress Plugin",
    it installs into wp-content, and `tutor-lms-mcp.php` carries
    ` * License:     GPL-2.0+` in the plugin header. UNDER-FIRE.

The deciding evidence in both cases is the PACKAGING MODE - does the code get
installed INTO the upstream, or does it call the upstream over a network - which is
neither a token nor a slug. Same defect family as T218-1/-3/-4: the instrument's unit
was wrong for the thing it measured.
"""

import re

# upstream -> (token regex, upstream licence, reciprocity)
UPSTREAMS = [
    ('OpenMage/Magento-1', r'openmage|\bmagento\b',      'OSL-3.0 + AFL-3.0',  'NET-RECIPROCAL'),
    ('Canvas LMS',         r'canvas[- ]lms|instructure',  'AGPL-3.0',           'NET-RECIPROCAL'),
    ('Open edX',           r'open\s?edx|edx-platform',    'AGPL-3.0',           'NET-RECIPROCAL'),
    ('Moodle',             r'\bmoodle\b',                 'GPL-3.0-or-later',   'RECIPROCAL'),
    ('WordPress',          r'wordpress|woocommerce|tutor[- ]lms', 'GPL-2.0-or-later', 'RECIPROCAL'),
    ('Drupal',             r'\bdrupal\b|\bopigno\b',      'GPL-2.0-or-later',   'RECIPROCAL'),
    ('Chamilo',            r'\bchamilo\b',                'GPL-3.0',            'RECIPROCAL'),
    ('Odoo',               r'\bodoo\b',                   'LGPL-3.0',           'WEAK-RECIPROCAL'),
    # control tokens: named upstreams that carry NO reciprocity. They must not fire.
    ('Sakai',             r'\bsakai\b',                   'ECL-2.0',            'PERMISSIVE'),
    ('Opencast',          r'\bopencast\b',                'ECL-2.0',            'PERMISSIVE'),
    ('Blackboard Learn',  r'\bblackboard\b|\bd2l\b|brightspace', 'proprietary SaaS', 'PROPRIETARY-API'),
    ('PowerSchool',       r'\bpowerschool\b',             'proprietary SaaS',   'PROPRIETARY-API'),
]

# The ecosystem's own declaration channel. This is the whole point of the instrument:
# an upstream names the paths to read before a maintainer is asked for anything.
CHANNELS = {
    'WordPress':          ['readme.txt', '{name}.php', 'plugin.php', 'composer.json'],
    'Moodle':             ['version.php', 'lib.php', 'classes/*.php', 'composer.json'],
    'OpenMage/Magento-1': ['composer.json', 'app/etc/modules/*.xml'],
    'Drupal':             ['{name}.info.yml', 'composer.json'],
    'Open edX':           ['setup.py', 'pyproject.toml'],
    'Canvas LMS':         ['package.json', 'Gemfile'],
    'Chamilo':            ['composer.json'],
    'Odoo':               ['__manifest__.py'],
}

# installed INTO the upstream -> the upstream licence reaches the work
_INSTALLS_INTO = re.compile(
    r'wp-content|upload plugin|admin\s*[>→-]+\s*plugins|site administration\s*[>→-]+\s*plugins|'
    r'\bplugin directory\b|copy the plugin|\bis a (wordpress|moodle|drupal) plugin\b|'
    r'\b(wordpress|moodle|drupal) plugin\b|local/[a-z_]+|mod/[a-z_]+|'
    r'fork(ed)? (of|from)|built (on|upon|on top of)|based (on|upon)|drop in replacement', re.I)

# calls the upstream ACROSS a boundary -> the upstream licence does NOT reach the work
_CALLS_ACROSS = re.compile(
    r'webservice/rest|/api/|rest api|graphql|wstoken|managetoken|'
    r'\bapi (token|key)\b|oauth|client (for|library)|connects? (claude|an? (ai|llm)) to', re.I)


def relation(readme: str, slug: str = '') -> str:
    """DERIVATIVE | INTEGRATION | UNDECIDED, from the packaging mode.

    Installation beats calling: a WordPress plugin that also calls a REST API is
    still a WordPress plugin. That ordering is what tutor-lms-mcp turns on.
    """
    head = '\n'.join(readme.splitlines()[:40])
    into = bool(_INSTALLS_INTO.search(head)) or bool(_INSTALLS_INTO.search(readme))
    across = bool(_CALLS_ACROSS.search(readme))
    if into:
        return 'DERIVATIVE'
    if across:
        return 'INTEGRATION'
    return 'UNDECIDED'


def upstream(readme: str):
    """Strongest-reciprocity upstream named in the README, or None."""
    order = {'NET-RECIPROCAL': 0, 'RECIPROCAL': 1, 'WEAK-RECIPROCAL': 2,
             'PROPRIETARY-API': 3, 'PERMISSIVE': 4}
    hits = [(n, l, r) for n, rx, l, r in UPSTREAMS if re.search(rx, readme, re.I)]
    if not hits:
        return None
    hits.sort(key=lambda h: order[h[2]])
    return hits[0]


def channels(up_name: str, slug: str = ''):
    """The paths to read before asking a maintainer for a LICENSE file."""
    name = slug.split('/')[-1] if slug else 'plugin'
    return [c.replace('{name}', name) for c in CHANNELS.get(up_name, [])]


def verdict(readme: str, slug: str = ''):
    """One row's standing instruction. Channels FIRST; the risk line only after."""
    up = upstream(readme)
    if up is None:
        return {'upstream': None, 'relation': None, 'reciprocity': None,
                'read_first': [], 'instruction': 'no upstream named - ordinary ACTION PH lead'}
    name, lic, rec = up
    rel = relation(readme, slug)
    read = channels(name, slug) if rel == 'DERIVATIVE' else []
    if rel == 'DERIVATIVE' and rec in ('NET-RECIPROCAL', 'RECIPROCAL', 'WEAK-RECIPROCAL'):
        ins = (f'READ {read} FIRST - {name} prescribes where its licence goes. '
               f'Only if those are all silent is this a {lic} dead end.')
    elif rel == 'DERIVATIVE':
        ins = f'derivative of {name} ({lic}) - no reciprocity; ordinary lead'
    elif rec == 'PROPRIETARY-API':
        ins = (f'calls {name} over its API: the constraint is VENDOR API TERMS, '
               f'not a licence. Do not file this as a licence gap')
    else:
        ins = (f'calls {name} over its API - {lic} does NOT reach this work. '
               f'The author grant is the only question; ordinary ACTION PH lead')
    return {'upstream': name, 'relation': rel, 'reciprocity': rec,
            'read_first': read, 'instruction': ins}
