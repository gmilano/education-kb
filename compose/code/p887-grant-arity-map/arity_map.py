"""p887 — `886-G1`'s acceptance test: a licence is a SET, so every shelf row carries a MAP.

WHAT `886-G1` ASKS FOR, verbatim: every shelf row carries (a) a grant **map** from path
prefix to family rather than a scalar, derived by enumerating the tree with
`git clone --depth 1 --filter=blob:none --no-checkout` + `git ls-tree -r`, and (b) where a
`LICENSING.md`/`NOTICE`/`THIRD_PARTY_NOTICES.md` exists, an `AND`/`OR` determination read
from it and recorded with its byte count and `sha256_12`.

🟢 `886-G2(a)` COMPLIANCE — the reuse record this instrument is REQUIRED to carry.
`make ladder-audit` was run BEFORE a line of this file was written: **919 ladders across
510 instruments, 37 of them `TREE-ENUMERATED`** (`/tmp/p887-ladder-full.tsv`, this pass).
What is reused, and what is not:

  REUSED, unmodified
    `p427-conjunctive-grant/conjunctive_grant.py::classify`  -> the AND/OR determination.
        This is `886-G1`'s part (b) and it was already built, with 24 passing controls.
    `p228-shelf-gate/classify_grant.py::classify`            -> family per payload.
    `p370-git-tree-payload/probe_tree.sh`                    -> the TRANSPORT, verbatim:
        blobless partial clone at depth 1, no checkout. `p370`'s own header already
        records why this is the right transport ("raw cannot list a directory: every raw
        licence probe is a GUESS AT A FILENAME").

  NOT REUSED, with the reason `886-G2(a)` demands
    `p370`'s ENUMERATION is `git ls-tree --name-only HEAD` — ROOT ONLY. `886-G1`'s
    acceptance test requires a map from PATH PREFIX to family, which a root listing
    cannot express: `sudosylabs/proctor`'s Apache-2.0 grant lives at
    `packages/{cache,mail,vfs}/LICENSE` and is invisible to it. This file therefore adds
    `-r` to `p370`'s ls-tree and changes NOTHING else about the transport.

  🔴 NO NEW PATH LADDER IS DEFINED IN THIS FILE. That is the whole point of `886-G2`:
    `p885` shipped an 8-path root-only ladder and regressed against `gate-ladder-case`
    and `gate-enumeration`. A ladder can only refute the paths it tried; an enumeration
    has no paths to miss. Selection below is a FILTER OVER THE ENUMERATED TREE, applied
    to names git reported, never a list of names to probe.

Offline controls: `python3 test_arity_map.py`.
Online arm:      `python3 -I arity_map.py --slugs slugs.txt --out <tsv> --work <dir>`
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, '..', '..', '..'))

sys.path.insert(0, os.path.join(_ROOT, 'compose', 'code', 'p427-conjunctive-grant'))
sys.path.insert(0, os.path.join(_ROOT, 'compose', 'code', 'p228-shelf-gate'))

from conjunctive_grant import classify as conj_classify  # noqa: E402
from classify_grant import classify as fam_classify      # noqa: E402

# 🟢 A FILTER over enumerated names, not a ladder of names to probe.  Case-folded, and
# it matches at ANY depth because `886-G1`'s four known cases include a per-directory
# grant.  `p886` recorded the four spellings `p885`'s ladder could not see
# (`LICENSE.TXT`, a Portuguese AGPL body, ODbL, a 19-byte declaration); a filter over
# `ls-tree -r` output sees all four because it never had to name them.
GRANT_NAME = re.compile(
    r'(?:^|/)(?:licen[cs]e|licencia|licenca|copying|unlicen[cs]e)'
    r'(?:[-_.][A-Za-z0-9]+)*$',
    re.IGNORECASE,
)

# 🔴 A DEFECT THIS INSTRUMENT'S OWN CONTROL CAUGHT, recorded rather than quietly fixed.
# The first form of `GRANT_NAME` accepted `src/license_checker.go`: `_checker` matched its
# suffix group and `.go` matched its extension group.  That is the `nombre`-row class in a
# third shape — a Go SOURCE FILE published as a licence grant.  Control `R-5` is the one
# that failed, and it failed BEFORE this filter ever ran online, which is the whole value
# of `886-G2(b)` asking for a known-good fixture set up front.
#
# The fix is a TYPE filter on the final dotted segment, and it FAILS CLOSED: an unknown
# extension is not a payload.  That direction is deliberate — missing an exotic licence
# filename is recoverable from the policy document (`886-G1` part b), whereas publishing a
# source file as a grant is a wrong cell on a client-facing shelf.
TEXTISH_EXT = frozenset((
    'txt', 'text', 'rtf', 'asc', 'rst', 'first', 'doc', 'docs',
    'license', 'licence', 'apache', 'apache2', 'mit', 'bsd', 'gpl', 'lgpl', 'agpl',
    'mpl', 'epl', 'cddl', 'isc', 'zlib', 'ofl', 'ccby', 'mulan',
    'lesser', 'lib', 'libre', 'gpl2', 'gpl3', 'v2', 'v3', 'header', 'template',
    'orig', 'old', 'new', 'en', 'es', 'pt', 'br', 'fr', 'de', 'it', 'nl',
    'zh', 'cn', 'ja', 'ko', 'ru', 'tr', '0', '1', '2', '3',
))


def _ext_ok(name):
    # The final dotted segment must be a TEXT-ish one, or absent entirely.
    #   `LICENSE-MIT`        -> no dot          -> True
    #   `docs/License.txt`   -> `txt`           -> True
    #   `LICENSE.TXT`        -> `txt` (folded)  -> True
    #   `COPYING.LESSER`     -> `lesser`        -> True
    #   `license_checker.go` -> `go`            -> False   (control `R-5`)
    base = name.rsplit('/', 1)[-1]
    if '.' not in base:
        return True
    return base.rsplit('.', 1)[-1].lower() in TEXTISH_EXT

# The three policy-document spellings `886-G1` names, plus the `.txt` variant `p886`
# recorded on `openedx/*`.  These are matched against the ENUMERATION too.
POLICY_NAME = re.compile(
    r'(?:^|/)(?:licensing\.md|notice|notice\.txt|notice\.md|third_party_notices\.md|'
    r'third_party_notices\.txt|third-party-notices\.md)$',
    re.IGNORECASE,
)

# 🔴 THE SECOND DEFECT THIS INSTRUMENT'S FIRST RUN FOUND IN ITSELF, recorded in full
# because it is the finding, not a footnote.
#
# `notice` and `copyright` were in the first form of `GRANT_NAME`, and `is_payload` was
# tested BEFORE `POLICY_NAME`.  So every `NOTICE` file was routed into the GRANT branch,
# handed to `classify_grant.classify`, and whatever licence title it happened to quote was
# published as a family the repository grants under.  Measured on the first run:
#
#   apereo/phpCAS      LICENSE=Apache-2.0 11,357 B   NOTICE=3,914 B  -> read as BSD-3-Clause
#   yetanalytics/lrsql LICENSE=Apache-2.0 11,357 B   NOTICE=19,985 B -> read as BSD-3-Clause
#
# Both came back `arity=2  Apache-2.0+BSD-3-Clause`. 🔴 **Both are Apache-2.0 projects.**
# An Apache-2.0 `NOTICE` exists to discharge §4(d) attribution for BUNDLED code; it is the
# one file in the tree that is GUARANTEED to quote licences the project does not grant
# under. `886-G1` already said so — a `NOTICE` is part (b) of its test, the policy document,
# never part (a). The ordering bug made it both.
#
# 🔵 And a raw arity count conflates a THIRD thing with the first two: a grant under
# `vendor/` is a dependency's grant, not the repository's. `HKUDS/DeepTutor` carries
# `web/vendor/thinking-orbs/LICENSE` (MIT) and IS Apache-2.0; `deepseek-ai/deepseek-harness`
# carries fourteen vendored MIT copies and IS MIT. Publishing either as a two-family grant
# would be a wrong cell on a client-facing shelf.
#
# So the map is keyed on path and every entry is TYPED. `arity_own` is the number this KB's
# licence cell may be derived from; `arity_all` is the notice-obligation surface.
VENDOR_SEG = (
    'vendor', 'vendors', 'third_party', 'third-party', 'thirdparty', '3rdparty',
    'node_modules', 'external', 'externals', 'deps', 'dependencies', 'bundled',
    'contrib', 'submodules', 'fonts', 'webfonts', 'assets/fonts',
)


def grant_class(path):
    """OWN | VENDORED — whose grant is this?

    A root grant is always OWN.  Anything under a vendoring segment is VENDORED, at any
    depth, because that is where a bundled dependency's own licence file lives.
    """
    parts = path.split('/')[:-1]
    if not parts:
        return 'OWN'
    low = [p.lower() for p in parts]
    if any(seg in low for seg in VENDOR_SEG):
        return 'VENDORED'
    return 'OWN'


# A `.md`/`.rst` under a grant name is prose ABOUT a licence, not a payload — `p427`'s
# `sweep.py` already draws this line and we draw it identically.
PROSE_EXT = ('.md', '.rst', '.html', '.py', '.tsv', '.json', '.yml', '.yaml')

# 🔴 `886-G4`: a policy document is not self-verifying.  These are the markers that make
# a determination READABLE; every one is recorded with the line it came from so the
# shelf can carry the adjudication column `886-G4` requires.
AND_MARK = re.compile(
    r'\b(?:dual[- ]licen[cs]ed under both|licensed under both|'
    r'and\s+(?:the\s+)?(?:MIT|Apache|BSD|GPL)|'
    r'subject to both|must comply with both|both licen[cs]es apply|'
    r'in addition to the terms)\b', re.IGNORECASE)
OR_MARK = re.compile(
    r'\b(?:at your option|either .{0,40}\bor\b|dual[- ]licen[cs]ed under either|'
    r'MIT\s*(?:/|\bor\b)\s*Apache|Apache-2\.0\s+OR\s+MIT|'
    r'you may choose|your choice of)\b', re.IGNORECASE)


def sha12(data):
    return hashlib.sha256(data).hexdigest()[:12]


def is_payload(path):
    if not _ext_ok(path):
        return False
    if not GRANT_NAME.search(path):
        return False
    return not path.lower().endswith(PROSE_EXT)


def prefix_of(path):
    """The PATH PREFIX a grant governs: its directory, or `/` at the root.

    This is the key of `886-G1`'s map.  A grant at `packages/cache/LICENSE` governs
    `packages/cache/`; one at `LICENSE` governs the repository.
    """
    d = os.path.dirname(path)
    return (d + '/') if d else '/'


def determine_mode(body):
    """AND / OR / UNDETERMINED from a policy document's own words.

    🔴 `886-G4` is why this returns UNDETERMINED rather than guessing: the two shapes are
    indistinguishable to any prober, so an unreadable document must say so.
    """
    hits_and = AND_MARK.search(body)
    hits_or = OR_MARK.search(body)
    if hits_and and hits_or:
        return ('AMBIGUOUS', hits_and.group(0), hits_or.group(0))
    if hits_and:
        return ('AND', hits_and.group(0), None)
    if hits_or:
        return ('OR', None, hits_or.group(0))
    return ('UNDETERMINED', None, None)


def git(args, cwd=None, binary=False):
    r = subprocess.run(['git'] + args, cwd=cwd, stdout=subprocess.PIPE,
                       stderr=subprocess.DEVNULL, timeout=300)
    if r.returncode != 0:
        return None
    return r.stdout if binary else r.stdout.decode('utf-8', 'replace')


def probe(slug, work):
    """Enumerate one repository's tree and map every grant it carries."""
    key = slug.replace('/', '%')
    d = os.path.join(work, key)
    out = {'slug': slug, 'status': 'OK', 'head': '-', 'grants': [], 'policies': []}

    # A cached clone from an earlier run of this same pass is reused: the transport is
    # pinned by HEAD and re-cloning 22,127 paths to re-read the same blobs is waste.
    if os.path.isdir(os.path.join(d, '.git')) and git(['rev-parse', 'HEAD'], cwd=d):
        ok = subprocess.CompletedProcess([], 0)
    else:
        ok = subprocess.run(
            ['git', 'clone', '--quiet', '--depth', '1', '--filter=blob:none',
             '--no-checkout', '--single-branch', 'https://github.com/%s' % slug, d],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=900)
    if ok.returncode != 0:
        out['status'] = 'CLONE-FAILED'
        return out

    head = git(['rev-parse', 'HEAD'], cwd=d)
    if not head:
        out['status'] = 'NO-HEAD'
        return out
    out['head'] = head.strip()

    tree = git(['ls-tree', '-r', '--name-only', 'HEAD'], cwd=d)
    if tree is None:
        out['status'] = 'NO-TREE'
        return out
    paths = [p for p in tree.splitlines() if p]
    out['tree_size'] = len(paths)

    for p in paths:
        # 🔴 POLICY FIRST. A `NOTICE` is `886-G1` part (b) and never part (a); testing
        # `is_payload` first is exactly the defect recorded at the top of this file.
        if POLICY_NAME.search(p):
            blob = git(['cat-file', '-p', 'HEAD:%s' % p], cwd=d, binary=True)
            if blob is None:
                continue
            body = blob.decode('utf-8', 'replace')
            mode, am, om = determine_mode(body)
            out['policies'].append({
                'path': p, 'bytes': len(blob), 'sha12': sha12(blob),
                'mode': mode, 'and_mark': am or '-', 'or_mark': om or '-',
            })
            continue
        if is_payload(p):
            blob = git(['cat-file', '-p', 'HEAD:%s' % p], cwd=d, binary=True)
            if blob is None:
                continue
            body = blob.decode('utf-8', 'replace')
            fam, chan, note = fam_classify(body)
            cj = conj_classify(body)
            out['grants'].append({
                'path': p, 'prefix': prefix_of(p), 'bytes': len(blob),
                'sha12': sha12(blob), 'klass': grant_class(p),
                'family': fam or 'UNRECOGNISED',
                'payload_mode': cj['mode'],
                'payload_families': '+'.join(cj['families']) or '-',
                'note': note or '-',
            })

    return out


def arity(row):
    """The two arities `886-G1` needs kept apart.

    `arity_own`  — distinct families among OWN grants.  THIS is the number a licence cell
                   on these shelves may be derived from.
    `arity_all`  — distinct families across the whole tree, vendored included.  This is the
                   NOTICE-OBLIGATION surface: what a distributor owes attribution for.

    🔴 `p887`'s first run reported only the second and called it the arity.  On
    `deepseek-ai/deepseek-harness` that is `3`; the repository's own grant is `MIT`, arity
    `1`, and `Apache-2.0+BSD-3-Clause+MIT` would have been a wrong cell.
    """
    own = {g['family'] for g in row['grants']
           if g['family'] != 'UNRECOGNISED' and g['klass'] == 'OWN'}
    allf = {g['family'] for g in row['grants'] if g['family'] != 'UNRECOGNISED'}
    return len(own), sorted(own), len(allf), sorted(allf)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--slugs', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--work', required=True)
    a = ap.parse_args(argv)

    os.makedirs(a.work, exist_ok=True)
    with open(a.slugs, encoding='utf-8') as fh:
        slugs = [l.strip() for l in fh if l.strip() and not l.startswith('#')]

    rows = []
    with open(a.out, 'w', encoding='utf-8') as w:
        w.write('slug\tstatus\thead\ttree_paths\tarity_own\tfamilies_own\t'
                'arity_all\tfamilies_all\tgrant_map\tpolicy_docs\n')
        for s in slugs:
            r = probe(s, a.work)
            n_own, f_own, n_all, f_all = arity(r)
            gmap = ';'.join('%s[%s]=%s(%dB,%s)'
                            % (g['path'], g['klass'][0], g['family'], g['bytes'],
                               g['sha12'])
                            for g in sorted(r['grants'], key=lambda x: x['path']))
            pols = ';'.join('%s(%dB,%s,%s)' % (p['path'], p['bytes'], p['sha12'],
                                               p['mode'])
                            for p in sorted(r['policies'], key=lambda x: x['path']))
            w.write('%s\t%s\t%s\t%s\t%d\t%s\t%d\t%s\t%s\t%s\n' % (
                r['slug'], r['status'], r['head'][:12], r.get('tree_size', '-'),
                n_own, '+'.join(f_own) or '-', n_all, '+'.join(f_all) or '-',
                gmap or '-', pols or '-'))
            rows.append((r, n_own, f_own, n_all, f_all))
            print('%-30s %-11s own=%d %-26s all=%d %-34s paths=%-6s pol=%d'
                  % (s, r['status'], n_own, '+'.join(f_own) or '-',
                     n_all, '+'.join(f_all) or '-',
                     r.get('tree_size', '-'), len(r['policies'])), flush=True)

    multi_own = [r for r, n, _, _, _ in rows if n > 1]
    multi_all = [r for r, _, _, n, _ in rows if n > 1]
    print('')
    print('# rows=%d  arity_own>1=%d  arity_all>1=%d  policy-docs=%d  failed=%d'
          % (len(rows), len(multi_own), len(multi_all),
             sum(len(r['policies']) for r, _, _, _, _ in rows),
             sum(1 for r, _, _, _, _ in rows if r['status'] != 'OK')))
    for r, n, f, na, fa in rows:
        if n > 1:
            print('#   OWN arity>1: %-30s %s' % (r['slug'], '+'.join(f)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
