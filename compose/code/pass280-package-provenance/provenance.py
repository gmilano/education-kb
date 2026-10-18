#!/usr/bin/env python3
"""pass280 — PER-PACKAGE PROVENANCE: what a manifest says about WHOSE manifest it is.

`p279` ended with this item ranked first, at zero searches:

    Give the manifest walk a KNOWN-THIRD-PARTY NAME channel.  The path vocabulary is a
    floor -- proved twice by one repository this pass -- and the residual
    (`ui/static/pyodide/`) is only reachable by name.

🔴 THE REMEDY AS REGISTERED NEEDS A LIST THIS BASE WOULD HAVE HAD TO INVENT, AND THE LIST
IS THE SAME DEFECT CLASS ONE LAYER OUT.  `p279` wrote it plainly about its own path
vocabulary -- *"a path vocabulary can only reject the conventions somebody enumerated"* --
and a name vocabulary can only reject the projects somebody enumerated.  A floor built to
replace a floor.

🟢 THE DURABLE CHANNEL NEEDS NO LIST, BECAUSE THE VENDORED MANIFEST DECLARES ITS OWN
PROVENANCE.  Read first-hand this pass:

    Open-TutorAi/open-tutor-ai-CE  ui/static/pyodide/package.json
        "name": "pyodide"
        "homepage": "https://github.com/pyodide/pyodide"
        "repository": { "url": "https://github.com/pyodide/pyodide" }
        "license": "Apache-2.0"

The payload that `p279` declared unreachable by any channel names the repository it belongs
to, in two fields, in its own bytes.

🔵 AND BOTH HALVES OF THAT CHANNEL WERE ALREADY ON THIS BASE'S SHELF:

    `lib/package_repo.sh::normalise_repo_url`  URL -> `owner/repo`, with the loud verdict
        vocabulary (`NO-REPO`, `NON-GITHUB`, `UNRESOLVABLE-HOST`).  Built pass 75,
        2026-10-09, for the REGISTRY channel.
    `p436-fork-hypothesis/resolve_homepage.py`  declared slug vs cited slug -> SELF /
        UPSTREAM, plus the measured warning that a difference has THREE causes and only
        one is a fork.

So this file writes neither parser.  It imports `p436`'s `SLUG_RE` and `p229`'s
`manifest_owner`, and `test_provenance.py` pins AGREEMENT with the shell normaliser over a
table of URL forms rather than trusting that two implementations stay equal.

🔴 THE DEPTH RULE, which is `p279`'s own lesson used constructively.  `p279` found that
`T229-M2`'s name check -- valid for *"is this ROOT manifest upstream's?"* -- rejected 12 of
`Athena`'s 14 workspace packages when applied at every depth, and recorded: *"a predicate is
valid at the depth it was built for."*  `p436` was likewise built for a ROOT manifest, where
a differing declaration is a fork hypothesis and NOT a vendoring finding.  So:

    depth 0   a differing declaration is RECORDED, never enforced.  `p436`'s three causes
              (fork lineage, sibling repo, name collision) all live here, and `p279` measured
              a fourth: naming a package differently from its repository is ordinary.
    depth > 0 a subpackage whose manifest declares ANOTHER REPOSITORY is vendored.  A
              workspace package has no reason to name a different project's repository;
              `pyodide` under `ui/static/` does exactly that.

Verdicts (the enforceable ones are the two THIRD-PARTY values):

    OWN-DECLARED        the manifest names THIS repository            -> the repository's own
    OWN-SUBPACKAGE      depth>0, declares no repository               -> the repository's own
    SILENT              no name and no repository field               -> silence is not a
                                                                         counter-claim (T229-M2)
    THIRD-PARTY         depth>0, declares a DIFFERENT repository      -> 🔴 vendored
    THIRD-PARTY-NAMED   depth>0, no repository field, name is a known
                        third-party project                          -> 🔴 vendored (the floor)
    ROOT-FOREIGN-DECLARED depth 0, declares a different repository    -> 🟡 recorded: fork?
    ROOT-NAME-DIFFERS   depth 0, name is neither owner nor repo       -> 🟡 recorded (p279)

   usage: provenance.py --row <slug> <ref> <path> <payload-file>
          provenance.py --list        print the third-party floor list (T272)
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# REUSE, not re-implementation.  `p436` owns the GitHub-URL -> slug regex and `p229` owns
# `manifest_owner` (the T229-M2 name reader).  Importing them by path is what makes
# `python3 -I` work from any cwd -- `p355-cwd-portability`'s class.
_p436 = _load(os.path.join(HERE, '..', 'p436-fork-hypothesis', 'resolve_homepage.py'),
              'p280_p436')
_p229 = _load(os.path.join(HERE, '..', 'p229-grant-ladder-reach', 'manifest_grant.py'),
              'p280_p229')
SLUG_RE = _p436.SLUG_RE
manifest_owner = _p229.manifest_owner
attributable = _p229.attributable

# 🟡 THE FLOOR, and it is declared as a floor.  Only reached when a vendored manifest carries
# NO repository or homepage field at all -- `tadreeblms`'s CKEditor builds are the measured
# case.  Every entry is a package name read first-hand from a manifest in this corpus, never
# a name recalled from general knowledge: a list of projects somebody enumerated can only
# reject the projects somebody enumerated, which is why it sits BELOW the declared channel.
KNOWN_THIRD_PARTY = {
    'moment', 'swiper', 'tailwindcss', 'prismjs', 'pyodide', 'jquery',
    'ckeditor', 'ckeditor4', 'ckeditor5',
    'wp-background-process',
}
# Scope prefixes: `@ckeditor/ckeditor5-build-classic` is CKEditor's, whatever the tail says.
KNOWN_THIRD_PARTY_SCOPES = {'ckeditor', 'tailwindcss', 'pyodide', 'swiper'}

_MANIFEST_NAMES = ('package.json', 'composer.json', 'pyproject.toml', 'Cargo.toml',
                   'setup.cfg', 'pom.xml')


def declared_repo(basename, payload):
    """-> the `owner/repo` this manifest declares it lives at, or None when it does not say.

    npm `repository` (string or object) and `homepage`; composer `support.source` and
    `homepage`; `pyproject.toml`'s `[project.urls]`; a pom's `<scm><url>`.  Only a
    github.com address resolves -- a GitLab or Bitbucket URL is a real declaration this
    channel cannot compare, and it is reported as such rather than silently dropped.
    """
    base = basename.rsplit('/', 1)[-1]
    urls = []
    if base in ('package.json', 'composer.json'):
        try:
            d = json.loads(payload) or {}
        except ValueError:
            d = {}
        if not isinstance(d, dict):
            d = {}
        repo = d.get('repository')
        if isinstance(repo, str):
            urls.append(repo)
        elif isinstance(repo, dict):
            urls.append(repo.get('url') or '')
        elif isinstance(repo, list):            # composer allows a list
            for r in repo:
                urls.append((r or {}).get('url') if isinstance(r, dict) else str(r or ''))
        sup = d.get('support')
        if isinstance(sup, dict):
            urls.append(sup.get('source') or '')
        urls.append(d.get('homepage') or '')
    else:
        # The TOML/INI/XML families: take every github.com address the payload carries and
        # let SLUG_RE pick the slug.  A regex over the whole payload would also match a
        # DEPENDENCY's URL, so the search is bounded to the url-ish lines.
        # 🔴 MEASURED BY THIS INSTRUMENT'S OWN CONTROLS, not read: passing the whole LINE to
        # `p436`'s `SLUG_RE` returns nothing for `Repository = "https://github.com/o/r"` and
        # for `<scm><url>https://github.com/o/r</url></scm>`, because the regex ends its
        # match on `[/#?]` or end-of-string and a TOML closing quote or an XML closing tag
        # is neither.  `p436` reads npm/PyPI JSON values, which arrive already unquoted --
        # the regex is right for the channel it was built for, and a TOML or XML line is
        # that channel one layer out.  So the URL TOKEN is isolated first and the shared
        # regex is left alone.
        for line in payload.splitlines():
            low = line.lower()
            if 'github.com' not in low:
                continue
            if any(k in low for k in ('repository', 'homepage', 'url', 'source', 'scm',
                                      '<url>', 'project.urls')):
                urls.extend(re.findall(r'[^\s"\'<>(),\]]*github\.com[^\s"\'<>(),\]]*',
                                       line))
    for u in urls:
        if not u:
            continue
        m = SLUG_RE.search(u)
        if m:
            return '%s/%s' % (m.group(1), m.group(2))
    for u in urls:
        low = (u or '').lower()
        for host in ('gitlab.com', 'bitbucket.org', 'codeberg.org'):
            if host in low:
                return 'NON-GITHUB'
    return None


def _norm_slug(s):
    return (s or '').lower().rstrip('/').removesuffix('.git')


def _is_known_third_party(name):
    if not name:
        return False
    n = name.lower().lstrip('@')
    if n in KNOWN_THIRD_PARTY:
        return True
    scope = n.split('/', 1)[0] if '/' in n else None
    return scope in KNOWN_THIRD_PARTY_SCOPES


def classify(slug, path, payload):
    """-> (verdict, declared_name, declared_repo, reason).  No network."""
    depth = path.count('/')
    base = path.rsplit('/', 1)[-1]
    name = manifest_owner(base, payload) if base in _MANIFEST_NAMES else None
    repo = declared_repo(base, payload)

    if repo and repo != 'NON-GITHUB':
        if _norm_slug(repo) == _norm_slug(slug):
            return ('OWN-DECLARED', name, repo,
                    'manifest declares this repository')
        if depth > 0:
            return ('THIRD-PARTY', name, repo,
                    'subpackage manifest declares a DIFFERENT repository -- vendored')
        return ('ROOT-FOREIGN-DECLARED', name, repo,
                'root manifest declares a different repository -- fork / sibling / '
                'collision (p436): RECORDED, not enforced')
    if repo == 'NON-GITHUB':
        return ('DECLARED-NON-GITHUB', name, 'NON-GITHUB',
                'declares a non-GitHub source this channel cannot compare')
    if depth > 0 and _is_known_third_party(name):
        return ('THIRD-PARTY-NAMED', name, None,
                'subpackage manifest names a known third-party project (the floor list)')
    if not name:
        return ('SILENT', None, None, 'no name and no repository field -- attributed here')
    if depth > 0:
        return ('OWN-SUBPACKAGE', name, None,
                'subpackage manifest declares no repository -- attributed here')
    ok, _ = attributable(slug, base, payload)
    if not ok:
        return ('ROOT-NAME-DIFFERS', name, None,
                'root manifest names neither the owner nor the repository -- RECORDED '
                '(p279: naming a package differently from its repository is ordinary)')
    return ('OWN-DECLARED', name, None, 'root manifest names this repository')


# The two verdicts a walk may act on.  Everything else is recorded.
ENFORCEABLE = ('THIRD-PARTY', 'THIRD-PARTY-NAMED')


def is_third_party(slug, path, payload):
    return classify(slug, path, payload)[0] in ENFORCEABLE


def _declares_licence(base, payload):
    b = base.rsplit('/', 1)[-1]
    if b in ('package.json', 'composer.json'):
        try:
            d = json.loads(payload) or {}
        except ValueError:
            return '-'
        v = d.get('license') or d.get('licenses')
        if isinstance(v, list):
            v = ' | '.join(str((x or {}).get('type') if isinstance(x, dict) else x)
                           for x in v)
        return str(v) if v else '-'
    m = re.search(r'^\s*license\s*=\s*["\']([^"\'\n]+)', payload, re.M)
    if m:
        return m.group(1)
    m = re.search(r'<licenses>.*?<name>([^<]*)</name>', payload, re.S)
    return m.group(1).strip() if m else '-'


def main():
    if '--list' in sys.argv:
        print('# pass280 third-party FLOOR list (reached only when a manifest declares no '
              'repository)')
        for n in sorted(KNOWN_THIRD_PARTY):
            print(n)
        print('# scopes')
        for n in sorted(KNOWN_THIRD_PARTY_SCOPES):
            print('@%s/*' % n)
        return 0
    if '--row' in sys.argv:
        i = sys.argv.index('--row')
        try:
            slug, ref, path, body = sys.argv[i + 1:i + 5]
        except ValueError:
            print('usage: provenance.py --row <slug> <ref> <path> <file>', file=sys.stderr)
            return 2
        payload = open(body, encoding='utf-8', errors='replace').read()
        v, name, repo, why = classify(slug, path, payload)
        print('\t'.join([slug, ref, path, str(path.count('/')), str(len(payload)),
                         name or '-', repo or '-', v, why,
                         _declares_licence(path, payload)]))
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main())
