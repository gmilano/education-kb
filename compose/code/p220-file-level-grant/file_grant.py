"""p220 - ACTION RG's instrument, built for the unit a licence actually has.

`ACTION RG` asked: run `P219-A` over the `11` CLAIMED-IN-PROSE rows, on the premise that
reading the ecosystem channel beats asking the maintainer. It fires on the count (4 of 11)
and its CONCLUSION splits, because two different things were being called one state:

  * Moodle prescribes `version.php` and prescribes an `@license` docblock tag inside it.
    The file MUST exist and the field MUST be there. Reading beats asking.
  * npm prescribes `package.json` and does NOT prescribe `license`. PyPI, Go and
    HuggingFace are the same or worse. The file exists, is readable, and is EMPTY.
    Asking is the only route.

So the deciding property is not "does the ecosystem have a channel" but
"does the ecosystem MANDATE the field in a file that MUST exist" - the PRESCRIPTION TEST.

The second half is `T220-1`/`T220-2`: a repository-level grant and a file-level grant can
disagree, and in a drop-in wrapper or a Moodle plugin it is the FILE that ships. Fifth
consecutive unit mismatch in this KB's headline series:

    T218-1  token            vs  axis
    T218-3  heading level    vs  pass boundary
    T218-4  line             vs  sentence
    T219-5  token            vs  packaging mode
    T220    REPOSITORY       vs  FILE          <- this instrument
"""

# ---------------------------------------------------------------- prescription test

# field: 'mandatory' - the ecosystem requires a licence declaration in a file that must exist
#        'optional'  - the file must exist, the licence field in it does not
#        'absent'    - the ecosystem defines no licence field at all
_ECOSYSTEMS = {
    'moodle':      ('mandatory', ('version.php',)),
    'wordpress':   ('mandatory', ('readme.txt', '<plugin>.php')),
    'adl-scorm':   ('mandatory', ('<source>.js',)),
    'magento':     ('optional',  ('composer.json',)),
    'composer':    ('optional',  ('composer.json',)),
    'npm':         ('optional',  ('package.json',)),
    'pypi':        ('optional',  ('pyproject.toml', 'setup.py', 'setup.cfg')),
    'huggingface': ('optional',  ('README.md',)),
    'go':          ('absent',    ('go.mod',)),
    'none':        ('absent',    ()),
}

_VERDICT = {
    'mandatory': 'PRESCRIBED-CHANNEL',
    'optional':  'PERMISSIVE-MANIFEST',
    'absent':    'NO-CHANNEL',
}


def prescription(ecosystem):
    """Can this ecosystem's channel answer the licence question at all?

    PRESCRIBED-CHANNEL  -> read it; asking the maintainer first is the wrong order
    PERMISSIVE-MANIFEST -> read it, but an empty field is the EXPECTED case, not a defect
    NO-CHANNEL          -> there is nothing to read; a human is the only route
    """
    field, files = _ECOSYSTEMS.get(str(ecosystem).lower(), ('absent', ()))
    return {
        'ecosystem': str(ecosystem).lower(),
        'field': field,
        'read': list(files),
        'verdict': _VERDICT[field],
        'asking_is_premature': field == 'mandatory',
    }


# ---------------------------------------------------------------- registry identity gate

def identity_ok(registry_record, slug):
    """`T220-3`: a package registry answers about a PACKAGE, not about a repository.

    `registry.npmjs.org/canvas-lms-mcp` returns `license: MIT` and
    `repository.url: git+https://github.com/bruchris/canvas-lms-mcp`. The shelf row that
    declares that same npm `name` is `CreveXTech/canvas-lms-mcp`, which has no `license`
    field at all. Attributing the registry's MIT to it would write a stranger's grant onto
    an unlicensed row.

    So a registry grant is usable only when the record's own `repository` points back at
    the slug being asked about. Returns False when the record carries no repository at
    all - an unattributable grant is not a grant.
    """
    rec = registry_record or {}
    repo = rec.get('repository') or {}
    url = (repo.get('url') if isinstance(repo, dict) else repo) or ''
    if not url:
        return False
    owner_name = str(slug).strip('/').lower()
    url = url.lower().replace('git+', '').replace('.git', '')
    for host in ('github.com/', 'gitlab.com/', 'bitbucket.org/'):
        if host in url:
            return url.split(host, 1)[1].strip('/') == owner_name
    return False


# ---------------------------------------------------------------- repository vs file

_RECIPROCAL = ('gpl', 'agpl', 'lgpl', 'cc-by-sa', 'osl', 'epl', 'mpl', 'cddl')
_PERMISSIVE = ('mit', 'apache', 'bsd', 'isc', 'cc0', 'unlicense', 'zlib')


def _family(spdx):
    s = str(spdx or '').lower()
    for tok in _RECIPROCAL:
        if tok in s:
            return 'RECIPROCAL'
    for tok in _PERMISSIVE:
        if tok in s:
            return 'PERMISSIVE'
    return 'UNKNOWN' if s in ('', 'none', 'unknown') else 'OTHER'


def file_vs_repo(repo_grant, file_grants):
    """Compare a repository-level grant against the grants read in the files that ship.

    `file_grants` is a mapping {path: spdx-or-None}.

      AGREE          every file that carries a notice carries the repository's
      FILE-NARROWER  a shipped file is RECIPROCAL where the repository is PERMISSIVE
                     -> the repository-level grant must not be relied on
      FILE-WIDER     a shipped file is PERMISSIVE where the repository is RECIPROCAL
      FILE-SILENT    the repository declares and no shipped file carries any notice
      REPO-SILENT    a file carries a notice and the repository declares nothing
      UNDETERMINED   nothing declares anywhere
    """
    files = {p: g for p, g in (file_grants or {}).items()}
    carried = {p: g for p, g in files.items() if _family(g) not in ('UNKNOWN',)}
    rf = _family(repo_grant)

    if rf == 'UNKNOWN' and not carried:
        return 'UNDETERMINED'
    if rf == 'UNKNOWN':
        return 'REPO-SILENT'
    if not carried:
        return 'FILE-SILENT' if files else 'UNDETERMINED'

    fams = {_family(g) for g in carried.values()}
    if fams == {rf}:
        return 'AGREE'
    if 'RECIPROCAL' in fams and rf == 'PERMISSIVE':
        return 'FILE-NARROWER'
    if 'PERMISSIVE' in fams and rf == 'RECIPROCAL':
        return 'FILE-WIDER'
    return 'FILE-NARROWER' if 'OTHER' in fams else 'AGREE'


# ---------------------------------------------------------------- combined verdict

def verdict(ecosystem, repo_grant=None, file_grants=None, registry_record=None, slug=None):
    """What a studio may rely on, and what the next action is."""
    pre = prescription(ecosystem)
    cmp_ = file_vs_repo(repo_grant, file_grants)

    registry = None
    if registry_record is not None:
        registry = 'USABLE' if identity_ok(registry_record, slug) else 'IDENTITY-FAIL'

    if cmp_ in ('FILE-NARROWER', 'FILE-WIDER'):
        rely, action = 'NEITHER - the grants disagree', (
            'Do not ship against the repository grant. The unit is the FILE: read every '
            'file that would be redistributed and record the narrowest grant found.')
    elif cmp_ == 'REPO-SILENT':
        rely, action = 'the FILE grant', (
            'The repository is silent and a shipped file is not. Record the file path as '
            'the channel; no maintainer needs asking.')
    elif cmp_ == 'AGREE':
        rely, action = 'either - they agree', 'Record both channels and move on.'
    elif cmp_ == 'FILE-SILENT':
        rely, action = 'the REPOSITORY grant, with the gap stated', (
            'The repository declares and the shipped files carry no notice. Usable, but '
            'say so: a file lifted out of this repo travels with no grant on it.')
    elif pre['verdict'] == 'PRESCRIBED-CHANNEL':
        rely, action = 'nothing yet', (
            'READ %s FIRST - this ecosystem mandates the field. Asking the maintainer is '
            'premature.' % '/'.join(pre['read']))
    elif registry == 'USABLE':
        rely, action = 'the REGISTRY grant', (
            'The registry record points back at this slug, so its licence is this row s. '
            'Record the registry as the channel.')
    else:
        rely, action = 'nothing', (
            'The channel was read and is EMPTY, which is the expected case for this '
            'ecosystem. A human is the only route - this is a genuine ACTION PH lead.')

    return {
        'prescription': pre['verdict'],
        'comparison': cmp_,
        'registry': registry,
        'rely_on': rely,
        'next': action,
    }
