#!/usr/bin/env python3
"""agree.py -- does the lock AGREE with the manifest it reaches?

Reads a manifest and its reaching lockfile from paths given as ARGUMENTS
(never from cwd, never imported from the fetched tree) and reports, for one
(repo, ecosystem, manifest-dir) triple:

    declared   dependency names the MANIFEST asks for
    present    how many of those the LOCK actually contains
    missing    the names it does not  (the ones that make `npm ci` exit 1)

WHY NAMES AND NOT VERSIONS. A resolver fails closed on a name it cannot find
in the lock: `npm ci` refuses to run at all when package.json and
package-lock.json disagree on the dependency SET, and `composer install`
warns-then-resolves-stale on the same condition. A version that has drifted
still installs. So the name set is the hard edge, and it is the only part of
this comparison that is decidable from committed bytes alone -- which is the
whole reason this axis can be measured offline (P116-C).

ECOSYSTEM RULES (each one is the resolver's own rule, not ours):
  npm       package.json  dependencies + devDependencies + optionalDependencies
            THE NPM ECOSYSTEM HAS THREE LOCK FLAVOURS AND ALL THREE COUNT
            (P116-I). Reading only package-lock.json is how the first run of
            this census mis-scored 22 rows as undecidable: yarn and pnpm are
            not "no lock", they are a different grammar for the same fact.
              package-lock.json / npm-shrinkwrap.json
                  v2/v3: "node_modules/<name>" keys
                  v1:    "dependencies": {"<name>": ...}
              yarn.lock       v1:     `left-pad@^1.0.0:` entry heads
                              berry:  `"left-pad@npm:^1.0.0":`
              pnpm-lock.yaml  keys of the `packages:` / `snapshots:` blocks,
                              across the v5 `/name/version`, v6 `/name@version`
                              and v9 `name@version` spellings
            peerDependencies are EXCLUDED: npm does not require them in the
            lock tree, so counting them would manufacture drift (P116-E).
  composer  composer.json require + require-dev, minus the platform
            pseudo-packages php, hhvm, ext-*, lib-*, composer-* -- which have
            no lock entry BY DESIGN (P116-F).
            composer.lock  packages[].name + packages-dev[].name
  cargo     Cargo.toml [dependencies] [dev-dependencies] [build-dependencies]
            Cargo.lock [[package]] name =
            A workspace root whose deps are all `workspace = true` declares
            nothing itself -> empty, not drift (P116-G).

Exit status is always 0; an unparseable file is reported as a verdict, never
raised, because one bad JSON blob must not abort a 134-row census.
"""
import json, sys, os, re

def jload(p):
    with open(p, 'rb') as f:
        b = f.read()
    if not b.strip():
        return None, 'empty-file'
    try:
        return json.loads(b.decode('utf-8', 'replace')), None
    except Exception as e:
        return None, 'unparseable:%s' % type(e).__name__

PLATFORM = re.compile(r'^(php|hhvm)$|^(ext|lib|composer)-')

# A dependency resolved from somewhere other than the registry has no registry
# entry in the lock, and counting it would manufacture drift the same way the
# composer platform packages would (P116-J).
LOCAL_SPEC = re.compile(r'^(workspace:|link:|file:|portal:|\.{1,2}/)')

# Controls. PEER=1 counts peerDependencies, which npm does NOT require in the
# lock tree -- it is a POSITIVE control: it should manufacture drift, and how
# much it manufactures is the measure of what P116-E is suppressing.
# NO_DEV=1 drops devDependencies / require-dev, isolating their contribution.
PEER = os.environ.get('P116_PEER') == '1'
NO_DEV = os.environ.get('P116_NO_DEV') == '1'

def npm(man, lock):
    m, err = jload(man)
    if err: return None, None, err
    keys = ['dependencies', 'optionalDependencies']
    if not NO_DEV: keys.append('devDependencies')
    if PEER: keys.append('peerDependencies')
    declared = set()
    for k in keys:
        v = m.get(k)
        if isinstance(v, dict):
            declared |= {n for n, spec in v.items()
                         if not (isinstance(spec, str) and LOCAL_SPEC.match(spec))}
    # Workspace-internal packages (P116-L). A dependency satisfied by another
    # package IN THIS TREE is not in the lock because it is not fetched. The
    # exclusion set is not guessed from the `workspaces` globs: it is the set
    # of `name` fields of every other package.json in the tree, which is the
    # definition of a workspace-local dependency. agree.sh supplies it.
    declared -= WORKSPACE
    if blank(lock):
        return declared, None, 'empty-file'
    flavour = npm_flavour(lock)
    if flavour == 'yarn':
        try:
            return declared, yarn_names(lock), None
        except Exception as e:
            return declared, None, 'unparseable:%s' % type(e).__name__
    if flavour == 'pnpm':
        try:
            return declared, pnpm_names(lock), None
        except Exception as e:
            return declared, None, 'unparseable:%s' % type(e).__name__
    l, err = jload(lock)
    if err: return declared, None, err
    have = set()
    pkgs = l.get('packages')
    if isinstance(pkgs, dict):                      # lockfileVersion 2 / 3
        for key in pkgs:
            if key.startswith('node_modules/'):
                have.add(key.split('node_modules/')[-1])
    deps = l.get('dependencies')
    if isinstance(deps, dict):                      # lockfileVersion 1
        have |= set(deps.keys())
    return declared, have, None

def composer(man, lock):
    m, err = jload(man)
    if err: return None, None, err
    declared = set()
    for k in (('require',) if NO_DEV else ('require', 'require-dev')):
        v = m.get(k)
        if isinstance(v, dict):
            declared |= {n for n in v if not PLATFORM.match(n)}
    l, err = jload(lock)
    if err: return declared, None, err
    have = set()
    for k in ('packages', 'packages-dev'):
        v = l.get(k)
        if isinstance(v, list):
            have |= {p.get('name') for p in v if isinstance(p, dict) and p.get('name')}
    return declared, have, None

SEC = re.compile(r'^\s*\[(dependencies|dev-dependencies|build-dependencies)\]\s*$')
OTHERSEC = re.compile(r'^\s*\[')
KEY = re.compile(r'^\s*([A-Za-z0-9_.-]+)\s*=')
INLINE_WS = re.compile(r'workspace\s*=\s*true')

def cargo(man, lock):
    declared, insec = set(), False
    skip = ('dev-dependencies',) if NO_DEV else ()
    try:
        with open(man, 'r', errors='replace') as f:
            for line in f:
                ms = SEC.match(line)
                if ms: insec = ms.group(1) not in skip; continue
                if OTHERSEC.match(line): insec = False; continue
                if insec:
                    mm = KEY.match(line)
                    # a dep inherited from the workspace declares nothing here
                    if mm and not INLINE_WS.search(line):
                        declared.add(mm.group(1))
    except Exception as e:
        return None, None, 'unparseable:%s' % type(e).__name__
    if blank(lock):
        return declared, None, 'empty-file'
    have = set()
    try:
        with open(lock, 'r', errors='replace') as f:
            for line in f:
                mm = re.match(r'^name\s*=\s*"([^"]+)"', line)
                if mm: have.add(mm.group(1))
    except Exception as e:
        return declared, None, 'unparseable:%s' % type(e).__name__
    return declared, have, None

def _strip_spec(tok):
    """A lock entry head -> the dependency name it is keyed under.

      left-pad@^1.0.0                   -> left-pad
      @babel/core@npm:^7.0.0            -> @babel/core
      codemirror-v5.17.0@npm:codemirror@5.17.0
                                        -> codemirror-v5.17.0   (an ALIAS)

    `@npm:` is checked FIRST and is why this is not a one-line rfind (P116-K).
    An aliased dependency is keyed in the lock under the ALIAS, and the alias
    is the name package.json declares -- so splitting on the last `@` returns
    `codemirror-v5.17.0@npm:codemirror` and manufactures drift on every
    aliased dependency. The first run of this census reported exactly that on
    oppia/oppia and instructure/canvas-lms before the specs were read.
    """
    tok = tok.strip().strip('"\'').strip()
    if tok.startswith('/'):
        tok = tok[1:]
    i = tok.find('@npm:')
    if i > 0:
        return tok[:i]
    i = tok.rfind('@')
    if i > 0:
        return tok[:i]
    return tok

def yarn_names(path):
    """Entry heads of a yarn.lock: column-0 lines ending in `:`."""
    have = set()
    with open(path, 'r', errors='replace') as f:
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            if line[0] in ' \t':            # a field of the current entry
                continue
            line = line.rstrip('\n').rstrip()
            if not line.endswith(':'):
                continue
            head = line[:-1]
            if head in ('__metadata',):
                continue
            # one entry head may carry several comma-separated specs
            for tok in head.split(','):
                n = _strip_spec(tok)
                if n:
                    have.add(n)
    return have

DEPSEC = ('dependencies', 'devDependencies', 'optionalDependencies')

def pnpm_names(path):
    """Names a pnpm-lock.yaml accounts for, from TWO blocks, not one.

    `packages:` / `snapshots:`  the resolved package identities
    `importers:`                the dependency names each manifest in the
                                workspace declared, AS PNPM RECORDED THEM

    Both are needed, and the second is why (P116-Q). pnpm keys an ALIASED
    dependency in `packages:` under the dependency it RESOLVES TO, not under
    the alias -- the opposite of yarn, which keys it under the alias (P116-K).
    So `"@typescript/native": "npm:typescript@^7.0.2"` appears in `packages:`
    only as `typescript@7.0.2`, and a census reading `packages:` alone calls
    the alias missing. That is precisely what this instrument did to
    PrairieLearn/PrairieLearn before the lock was read by hand: it was the
    single `drift` row of the first clean census, and it was the instrument's
    error, not the repository's.

    The alias IS recorded under `importers:`, which is where pnpm writes what
    each manifest asked for. Scanning it also covers workspace-local
    dependencies for free.

    Nothing outside these two blocks is scanned: a whole-file scan would
    collect `specifier`, `version` and `resolution` as if they were package
    names, and junk in the `have` set can only ever MASK real drift.
    """
    have = set()
    block = None            # 'pkgs' | 'importers' | None
    key_indent = None       # depth of a package key inside `packages:`
    imp_indent = None       # depth of an importer path inside `importers:`
    sec_indent = None       # depth of a dependency SECTION inside an importer
    in_depsec = False
    with open(path, 'r', errors='replace') as f:
        for raw in f:
            line = raw.rstrip('\n')
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            lead = len(line) - len(line.lstrip())
            if lead == 0:
                head = line.rstrip().rstrip(':')
                if head in ('packages', 'snapshots'):
                    block, key_indent = 'pkgs', None
                elif head == 'importers':
                    block, imp_indent, sec_indent, in_depsec = 'importers', None, None, False
                else:
                    block = None
                continue
            if block is None or not line.rstrip().endswith(':'):
                continue
            key = line.strip()[:-1]

            if block == 'pkgs':
                if key_indent is None:
                    key_indent = lead
                if lead != key_indent:
                    continue
                bare = key.strip('"\'')
                if bare.startswith('/') and '@' not in bare[1:]:
                    n = bare[1:].rsplit('/', 1)[0]      # v5: /name/version
                else:
                    n = _strip_spec(key)
                if n:
                    have.add(n)
                continue

            # block == 'importers'
            if imp_indent is None:
                imp_indent = lead                        # the importer paths
            if lead == imp_indent:
                in_depsec, sec_indent = False, None      # a new importer
                continue
            if sec_indent is None and lead > imp_indent:
                sec_indent = lead                        # the section names
            if lead == sec_indent:
                in_depsec = key.strip('"\'') in DEPSEC
                continue
            if in_depsec and sec_indent is not None and lead > sec_indent:
                n = key.strip().strip('"\'')
                if n:
                    have.add(n)
    return have

NPM_LOCK = {
    'package-lock.json':   'json',
    'npm-shrinkwrap.json': 'json',
    'yarn.lock':           'yarn',
    'pnpm-lock.yaml':      'pnpm',
}

def blank(path):
    """True if the file has no non-whitespace bytes.

    An empty or truncated lock is NOT total drift (P116-N). The suite caught
    this: once flavour dispatch became content sniffing, a zero-byte lock fell
    through to the yarn grammar, produced an empty name set, and every declared
    dependency read as missing -- the single most alarming verdict this axis
    can emit, from a file that says nothing at all. It is reported as its own
    condition so it can never be counted as a shelf finding.
    """
    try:
        with open(path, 'rb') as f:
            return not f.read(65536).strip()
    except Exception:
        return False

def npm_flavour(path):
    """Which npm lock grammar is in this file?

    The basename is only a HINT (P116-M). It was the sole dispatch in the
    first draft, which made the comparator unable to read a lock committed
    under any other name -- and made the grammar untestable except through
    fixtures named exactly like the real thing. The file's own bytes decide:
    a lock that parses as JSON is npm's, one that declares `lockfileVersion:`
    unquoted-YAML-style or opens a `packages:`/`snapshots:` block is pnpm's,
    and anything else that looks like entry heads is yarn's.
    """
    try:
        with open(path, 'rb') as f:
            head = f.read(4096)
    except Exception:
        return NPM_LOCK.get(os.path.basename(path), 'json')
    stripped = head.lstrip()
    if stripped[:1] in (b'{', b'['):
        return 'json'
    text = head.decode('utf-8', 'replace')
    for ln in text.splitlines():
        if re.match(r'^lockfileVersion:', ln) or re.match(r'^(packages|snapshots|importers):\s*$', ln):
            return 'pnpm'
        if re.match(r'^__metadata:', ln) or 'yarn lockfile' in ln:
            return 'yarn'
    return NPM_LOCK.get(os.path.basename(path), 'yarn')

HANDLER = {'npm': npm, 'composer': composer, 'cargo': cargo}

WORKSPACE = set()

def main():
    global WORKSPACE
    if len(sys.argv) not in (5, 6):
        sys.stderr.write('usage: agree.py <eco> <manifest> <lock> <slug> [wsnames]\n')
        return 0
    eco, man, lock, slug = sys.argv[1:5]
    if len(sys.argv) == 6 and os.path.isfile(sys.argv[5]):
        with open(sys.argv[5], 'r', errors='replace') as f:
            WORKSPACE = {ln.strip() for ln in f if ln.strip()}
    h = HANDLER.get(eco)
    if not h:
        print('\t'.join([slug, eco, '-', '-', '-', 'unsupported-eco', '']))
        return 0
    for p in (man, lock):
        if not os.path.isfile(p):
            print('\t'.join([slug, eco, '-', '-', '-', 'blob-missing', '']))
            return 0
    declared, have, err = h(man, lock)
    if declared is None:
        print('\t'.join([slug, eco, '-', '-', '-', 'manifest-' + err, '']))
        return 0
    if not declared:
        print('\t'.join([slug, eco, '0', '0', '0', 'empty-manifest', '']))
        return 0
    if have is None:
        print('\t'.join([slug, eco, str(len(declared)), '-', '-', 'lock-' + err, '']))
        return 0
    missing = sorted(declared - have)
    verdict = 'agree' if not missing else 'drift'
    print('\t'.join([slug, eco, str(len(declared)), str(len(declared) - len(missing)),
                     str(len(missing)), verdict, ';'.join(missing[:12])]))
    return 0

if __name__ == '__main__':
    sys.exit(main())
