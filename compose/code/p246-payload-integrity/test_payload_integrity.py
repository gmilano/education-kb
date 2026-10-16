#!/usr/bin/env python3
"""Controls for `p246-payload-integrity`.

Runs from ANY cwd (`p355-cwd-portability`): the module is loaded from this file's own
directory by path, never by `import`, because `python3 -I` strips the script directory from
`sys.path` and `make hooks` is not run from here.

Every fixture is a REAL payload read first-hand from `raw.githubusercontent.com` on
2026-10-16, at the branch `git ls-remote --symref` reported, with its `HEAD` pinned:

    ia-para-todos.conflicted-apache.txt    0xnavarro/IA-PARA-TODOS        main    11 471 B
    iaga-sentinel.busl-1.1.txt             IAGA-TEAM/IAGA-Sentinel        main     4 913 B
    mvps-cenia.apache-one-deviation.txt    CENIA-DEV/mvps-cenia           main    11 361 B
    euconform.mit.txt                      Hiepler/EuConform              main     1 073 B
    opensalt.mit-published-apache.txt      opensalt/opensalt              develop  1 080 B
    ifes-academico.gpl3-published-apache.txt MuriloCalegari/Ifes-Academico QAcad   35 149 B
    govllm.eupl-1.2.txt                    JehanneDussert/govllm          main    13 599 B
    apache-2.0.canonical.txt               apache.org                             11 358 B
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_FIX = os.path.join(_HERE, "fixtures")

_src = os.path.join(_HERE, "payload_integrity.py")
_ns = {"__name__": "payload_integrity_under_test", "__file__": _src}
with open(_src, "r", encoding="utf-8") as _fh:
    exec(compile(_fh.read(), _src, "exec"), _ns)  # noqa: S102
verdict = _ns["verdict"]
conflicted = _ns["conflicted"]
conflict_sides = _ns["conflict_sides"]
holder_ambiguous = _ns["holder_ambiguous"]
parameter_roles = _ns["parameter_roles"]
governing_family = _ns["governing_family"]
names_but_does_not_grant = _ns["names_but_does_not_grant"]

_FAILED = []
_RUN = 0


def check(label, expected, actual):
    global _RUN
    _RUN += 1
    if expected != actual:
        _FAILED.append("%s\n    expected: %r\n    actual:   %r" % (label, expected, actual))


def fixture(name):
    with open(os.path.join(_FIX, name), "r", encoding="utf-8") as fh:
        return fh.read()


CONFLICTED = fixture("ia-para-todos.conflicted-apache.txt")
BUSL = fixture("iaga-sentinel.busl-1.1.txt")
CENIA = fixture("mvps-cenia.apache-one-deviation.txt")
MIT = fixture("euconform.mit.txt")
OPENSALT = fixture("opensalt.mit-published-apache.txt")
GPL3 = fixture("ifes-academico.gpl3-published-apache.txt")
EUPL = fixture("govllm.eupl-1.2.txt")
CANONICAL = fixture("apache-2.0.canonical.txt")

# ── THE STATE FINDING: the real conflicted payload ─────────────────────────────────────────
check("IA-PARA-TODOS is conflicted", True, conflicted(CONFLICTED))
check("IA-PARA-TODOS carries exactly one hunk", 1, conflict_sides(CONFLICTED))
check("IA-PARA-TODOS holder is ambiguous", True, holder_ambiguous(CONFLICTED))
check(
    "IA-PARA-TODOS verdict names both facts",
    "CONFLICTED:hunks=1;holder-ambiguous",
    verdict(CONFLICTED),
)

# ── no false positive on any resolved payload ──────────────────────────────────────────────
for _name, _text in (
    ("apache.org canonical", CANONICAL),
    ("mvps-cenia (non-canonical but resolved)", CENIA),
    ("EuConform MIT", MIT),
    ("opensalt MIT", OPENSALT),
    ("Ifes-Academico GPL-3.0", GPL3),
    ("govllm EUPL-1.2", EUPL),
    ("IAGA-Sentinel BSL", BUSL),
):
    check("%s is NOT conflicted" % _name, False, conflicted(_text))
    check("%s has 0 hunks" % _name, 0, conflict_sides(_text))

# 🟢 The pristine ASF appendix carries the TEMPLATE holder and NO real holder, so it is not
# ambiguous — which is exactly why `p241`'s exclusion is right on a pristine payload.
check("pristine ASF appendix is not holder-ambiguous", False, holder_ambiguous(CANONICAL))
# 🟢 A real MIT carries a real holder and NO template, so it is not ambiguous either.
check("EuConform MIT is not holder-ambiguous", False, holder_ambiguous(MIT))

# ── THE ROLE FINDING: the real BSL payload ─────────────────────────────────────────────────
check("IAGA-Sentinel governing family is BUSL", "BUSL", governing_family(BUSL))
check(
    "IAGA-Sentinel names Apache-2.0 WITHOUT granting it",
    ["Apache License, Version 2.0"],
    names_but_does_not_grant(BUSL),
)
check(
    "IAGA-Sentinel verdict is source-available and says what it only NAMES",
    "SOURCE-AVAILABLE:BUSL;names-but-does-not-grant=Apache License, Version 2.0",
    verdict(BUSL),
)
_roles = dict(parameter_roles(BUSL))
check("IAGA-Sentinel Change Date is read", "2030-05-03", _roles.get("change-date"))
check(
    "IAGA-Sentinel Change License is read",
    "Apache License, Version 2.0",
    _roles.get("change-license"),
)

# ── the role axis is NOT Apache-specific: the same shape with a copyleft change licence ────
_BSL_GPL = BUSL.replace("Apache License, Version 2.0", "GNU General Public License, Version 2.0")
check("BSL naming GPL still governs as BUSL", "BUSL", governing_family(_BSL_GPL))
check(
    "BSL naming GPL reports the named-not-granted licence",
    ["GNU General Public License, Version 2.0"],
    names_but_does_not_grant(_BSL_GPL),
)

# ── a real OSI payload governs itself: no parameter role, no source-available verdict ──────
for _name, _text in (
    ("apache.org canonical", CANONICAL),
    ("EuConform MIT", MIT),
    ("Ifes-Academico GPL-3.0", GPL3),
    ("govllm EUPL-1.2", EUPL),
):
    check("%s has no governing source-available family" % _name, None, governing_family(_text))
    check("%s -> SINGLE-RESOLVED-GRANT" % _name, "SINGLE-RESOLVED-GRANT", verdict(_text))
    check("%s names nothing it fails to grant" % _name, [], names_but_does_not_grant(_text))

# 🔵 `mvps-cenia` is the control that keeps the two axes apart: `p245` grades it NON-CANONICAL
# on the TEXT axis, and it is still ONE resolved grant that governs itself.
check("mvps-cenia -> SINGLE-RESOLVED-GRANT", "SINGLE-RESOLVED-GRANT", verdict(CENIA))

# ── the other source-available families, so the gate is not BSL-only ───────────────────────
check("Elastic License is governed as Elastic", "Elastic", governing_family("Elastic License 2.0\n\nTerms"))
check(
    "PolyForm Noncommercial is governed as PolyForm",
    "PolyForm",
    governing_family("PolyForm Noncommercial License 1.0.0"),
)
check("SSPL is governed as SSPL", "SSPL", governing_family("Server Side Public License\nVERSION 1"))
check(
    "CAL is governed as CAL",
    "CAL",
    governing_family("Cryptographic Autonomy License version 1.0"),
)

# ── empty and whitespace payloads (p1058's class, kept consistent here) ────────────────────
check("empty payload -> EMPTY", "EMPTY", verdict(""))
check("whitespace-only payload -> EMPTY", "EMPTY", verdict("   \n\t\n"))
check("empty is not conflicted", False, conflicted(""))
check("None-safe: governing_family", None, governing_family(""))
check("None-safe: parameter_roles", [], parameter_roles(""))
check("None-safe: holder_ambiguous", False, holder_ambiguous(""))

# ── the marker discipline: an underline is not a conflict ──────────────────────────────────
check(
    "a heading underlined with = is not a conflict",
    False,
    conflicted("MIT License\n=======\n\nPermission is hereby granted"),
)
check(
    "an opening marker alone is not a conflict",
    False,
    conflicted("<<<<<<< HEAD\nsome text with no closing marker\n"),
)
check(
    "a closing marker alone is not a conflict",
    False,
    conflicted("some text\n>>>>>>> abc123\n"),
)
check(
    "both markers present IS a conflict",
    True,
    conflicted("<<<<<<< HEAD\na\n=======\nb\n>>>>>>> abc123\n"),
)
check(
    "two hunks are counted",
    2,
    conflict_sides("<<<<<<< HEAD\na\n=======\nb\n>>>>>>> x\n<<<<<<< HEAD\nc\n=======\nd\n>>>>>>> y\n"),
)
# 🔵 A marker that is NOT at line start is prose about conflicts, not a conflict.
check(
    "an inline mention of the markers is not a conflict",
    False,
    conflicted("This licence does not use <<<<<<< or >>>>>>> anywhere in its text.\n"),
)

# ── the parameter grammar: label variants seen in the wild ─────────────────────────────────
check(
    "Change License with extra spacing is read",
    "Apache License, Version 2.0",
    dict(parameter_roles("Change License:      Apache License, Version 2.0\n")).get("change-license"),
)
check(
    "lowercase change license is read",
    "MIT",
    dict(parameter_roles("change license: MIT\n")).get("change-license"),
)
check(
    "a Change License mid-line is NOT a parameter",
    None,
    dict(parameter_roles("see the Change License: MIT clause above\n")).get("change-license"),
)
# 🔴 The honest limit, asserted so a later pass does not assume otherwise: a payload with a
# `Change License` parameter and NO source-available title is not claimed by this instrument.
check(
    "a parameter without a governing family yields no named-not-granted list",
    [],
    names_but_does_not_grant("Change License: Apache License, Version 2.0\n"),
)

if _FAILED:
    sys.stderr.write("\n%d of %d controls FAILED\n\n" % (len(_FAILED), _RUN))
    for _f in _FAILED:
        sys.stderr.write("  %s\n" % _f)
    sys.exit(1)
sys.stdout.write("%d/%d controls pass\n" % (_RUN, _RUN))
