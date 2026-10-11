#!/usr/bin/env python3
"""p137-foreign-holder-tree -- ACTION BY.

`p444-root-vs-tree-family` asked whether the licence FAMILY read from a root file
is the family of the whole tree, and answered 92% yes.  This instrument asks the
other half of the question: whose COPYRIGHT does the tree carry?

A root `LICENSE` names a grant and a holder.  A tree can carry further licence
files whose holder is somebody else entirely -- a vendored font, an editor, a
charting library, an agent-skills pack.  Those are the obligations a client
inherits and that a slug-level licence cell cannot see.

Three steps, each separately testable:

1. `tree_paths()`    -- paths from a blobless shallow clone (callers supply them;
                        the clone itself is `probe.sh`, so this file stays offline).
2. `licence_paths()` -- the licence-shaped subset, split root vs non-root.
                        CASE-INSENSITIVE on purpose: pass 137 lost a real
                        `License.txt` to a case-sensitive four-name probe
                        (`kstateome/lti-launch`), which is `p288-agpl-casefold`
                        biting the same KB a second time.
3. `holder_of()` / `is_foreign()` -- read the payload's first copyright line and
                        decide whether the holder is the repository's own.

Precision rules learned from the first run, each with a test below:
  * an i18n bundle (`*.properties`) or a template (`*.php`, `*.html`) whose text
    merely contains the WORD "copyright" is not a grant -- `sakaiproject/sakai`
    produced 7 such false positives from `content-copyright` message bundles;
  * a payload only counts as a grant if a licence family is recognisable in it
    or the copyright line carries a year;
  * an EMPTY path list must count as 0, not 1.  The first run of `probe.sh`
    printed `nonroot_licence=1` for seven repositories that have none, because
    `printf '%s\n' "$empty" | grep -c ''` counts the one empty line it is given.
    Seven of twenty rows were wrong in the direction of a finding, which is the
    direction that gets published.
"""

import re

LICENCE_NAME = re.compile(
    r'(^|/)(licen[cs]e|copying|notice|copyright)([._-][a-z0-9.+-]*)?$|\.licen[cs]e$',
    re.IGNORECASE)

NOT_A_GRANT_SUFFIX = ('.properties', '.php', '.html', '.png', '.jpg', '.gif',
                      '.svg', '.json', '.xml')

FAMILIES = (
    ('MIT', 'permission is hereby granted, free of charge'),
    ('Apache-2.0', 'apache license'),
    ('AGPL', 'gnu affero general public'),
    ('LGPL', 'gnu lesser general public'),
    ('GPL', 'gnu general public license'),
    ('BSD', 'redistributions of source code must retain'),
    ('MPL', 'mozilla public license'),
    ('ISC', 'permission to use, copy, modify, and/or distribute'),
    ('OFL', 'sil open font license'),
)

COPYRIGHT_LINE = re.compile(r'copyright', re.IGNORECASE)
HAS_YEAR = re.compile(r'(19|20)\d{2}')
HOLDER = re.compile(
    r'(?:copyright|\(c\)|©)[\s:]*(?:\(c\)|©)?[\s:]*'
    r'(?:(?:19|20)\d{2}(?:\s*[-–,]\s*(?:19|20)?\d{2,4})?)?[\s,:.]*(.+)',
    re.IGNORECASE)


def licence_paths(paths):
    """Split licence-shaped paths into (root, non_root). Empty in, empty out."""
    lic = [p for p in paths if LICENCE_NAME.search(p)]
    return [p for p in lic if '/' not in p], [p for p in lic if '/' in p]


def family_of(body):
    low = (body or '').lower()
    for name, anchor in FAMILIES:
        if anchor in low:
            return name
    return ''


def first_copyright_line(body):
    for line in (body or '').splitlines():
        if COPYRIGHT_LINE.search(line) and HAS_YEAR.search(line):
            return line.strip()
    return ''


def is_grant(path, body):
    """A licence-shaped path is only a GRANT if its payload reads like one."""
    if path.lower().endswith(NOT_A_GRANT_SUFFIX):
        return False
    return bool(family_of(body)) or bool(first_copyright_line(body))


def holder_of(body):
    line = first_copyright_line(body)
    if not line:
        return ''
    m = HOLDER.search(line)
    if not m:
        return ''
    return m.group(1).strip(' .,;<>-').strip()


def is_foreign(holder, own_names):
    """Foreign = the holder names none of the repository's own identities."""
    if not holder:
        return False
    low = holder.lower()
    return not any(n.lower() in low for n in own_names if n)


def repo_verdict(slug, payloads, own_names):
    """payloads: iterable of (path, body). Returns the row this instrument publishes."""
    root, non_root = licence_paths([p for p, _ in payloads])
    grants, foreign = [], []
    bodies = dict(payloads)
    for path in non_root:
        body = bodies.get(path, '')
        if not is_grant(path, body):
            continue
        grants.append(path)
        holder = holder_of(body)
        if is_foreign(holder, own_names):
            foreign.append((path, holder, family_of(body)))
    return {
        'slug': slug,
        'root_licence': len(root),
        'nonroot_licence_shaped': len(non_root),
        'nonroot_grants': len(grants),
        'foreign': foreign,
        'verdict': 'FOREIGN_HOLDER_IN_TREE' if foreign
                   else ('OWN_HOLDER_ONLY' if grants else 'ROOT_ONLY'),
    }
