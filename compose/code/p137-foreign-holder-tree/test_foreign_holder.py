#!/usr/bin/env python3
"""Own runner: pytest is not installed in this channel (channel state, p136)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from foreign_holder import (  # noqa: E402
    family_of, first_copyright_line, holder_of, is_foreign, is_grant,
    licence_paths, repo_verdict)

MIT = ('MIT License\n\nCopyright (c) 2024 Fonticons, Inc. (https://fontawesome.com)\n\n'
       'Permission is hereby granted, free of charge, to any person obtaining a copy\n')
LGPL = ('                   GNU LESSER GENERAL PUBLIC LICENSE\n'
        '                       Version 3, 29 June 2007\n\n'
        ' Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>\n')
SAKAI_BUNDLE = ('# SAK-39953 - define your custom copyright options here.\n'
                'hold_copyright=Tinc els drets d’autor.\n')

CASES = []


def case(fn):
    CASES.append(fn)
    return fn


@case
def empty_in_empty_out():
    """The bug this instrument exists to not repeat: no paths means zero, not one."""
    assert licence_paths([]) == ([], [])
    assert licence_paths(['src/index.ts']) == ([], [])


@case
def root_and_nonroot_split():
    root, non_root = licence_paths(
        ['LICENSE', 'src/a.ts', 'gems/lti-advantage/LICENSE.txt', 'fonts/OFL.txt'])
    assert root == ['LICENSE'], root
    assert non_root == ['gems/lti-advantage/LICENSE.txt'], non_root


@case
def casefold_is_the_point():
    """`kstateome/lti-launch` serves `License.txt`; a four-name probe called it absent."""
    root, non_root = licence_paths(['License.txt', 'a/COPYING.LESSER', 'b/licence'])
    assert root == ['License.txt']
    assert len(non_root) == 2, non_root


@case
def debian_copyright_file_counts():
    root, non_root = licence_paths(['platforms/debian-server/debian/copyright'])
    assert non_root and not root


@case
def family_detection():
    assert family_of(MIT) == 'MIT'
    assert family_of(LGPL) == 'LGPL'
    assert family_of('') == ''


@case
def holder_extraction():
    assert holder_of(MIT).startswith('Fonticons, Inc.')
    assert holder_of(LGPL).startswith('Free Software Foundation, Inc.')
    assert holder_of('no notice here') == ''


@case
def i18n_bundle_is_not_a_grant():
    assert is_grant('content-copyright/bundle/messages.properties', SAKAI_BUNDLE) is False
    assert first_copyright_line(SAKAI_BUNDLE) == ''


@case
def payload_without_year_or_family_is_not_a_grant():
    assert is_grant('vendor/NOTICE', 'See the website for terms.') is False


@case
def foreign_is_about_the_holder_not_the_path():
    assert is_foreign('Fonticons, Inc.', ['moodle']) is True
    assert is_foreign('Moodle Pty Ltd', ['moodle']) is False
    assert is_foreign('', ['moodle']) is False


@case
def canvas_lti_advantage_row_is_the_worked_example():
    """AGPL at the root, MIT four levels down, held by a named individual."""
    v = repo_verdict(
        'instructure/canvas-lms',
        [('LICENSE', 'GNU AFFERO GENERAL PUBLIC LICENSE\nCopyright (C) 2011 Instructure\n'),
         ('gems/lti-advantage/LICENSE.txt',
          'MIT License\n\nCopyright (c) 2018 Nathan Mills\n'
          'Permission is hereby granted, free of charge, to any person obtaining a copy\n')],
        ['instructure', 'canvas'])
    assert v['verdict'] == 'FOREIGN_HOLDER_IN_TREE', v
    assert v['root_licence'] == 1
    assert v['nonroot_grants'] == 1
    assert v['foreign'][0][1] == 'Nathan Mills', v['foreign']
    assert v['foreign'][0][2] == 'MIT'


@case
def root_only_repo_is_not_a_finding():
    v = repo_verdict('overhangio/tutor',
                     [('LICENSE', 'GNU AFFERO GENERAL PUBLIC LICENSE\n')],
                     ['overhang'])
    assert v['verdict'] == 'ROOT_ONLY', v
    assert v['foreign'] == []


@case
def own_holder_in_tree_is_not_foreign():
    v = repo_verdict('oppia/oppia',
                     [('LICENSE', 'Apache License\nVersion 2.0\n'),
                      ('core/LICENSE', 'Apache License\nCopyright 2024 The Oppia Authors\n')],
                     ['oppia'])
    assert v['verdict'] == 'OWN_HOLDER_ONLY', v


def main():
    failed = 0
    for fn in CASES:
        try:
            fn()
            print(f'  ok   {fn.__name__}')
        except AssertionError as exc:
            failed += 1
            print(f'  FAIL {fn.__name__}: {exc}')
    print(f'\n{len(CASES) - failed}/{len(CASES)} passed')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
