#!/usr/bin/env python3
"""p459 — ONE verdict from BOTH classifiers, over the roots AND the tree payloads.

**P459: a shelf consulted by two classifiers needs one verdict function, and the
layer below the root is where nobody had looked with both.**

Pass 27 (`p445`) measured that this KB has two licence classifiers and that each is
blind where the other sees: `lib/license_family.sh` knew NonCommercial and the
non-OSI restriction families, `sweep_payload.family_of` knew the EUPL.  Pass 28 taught
each the other's axis, and the divergence over the 412 roots fell from 43 rows to 3.

This instrument answers the question that remains after that: **the roots were
re-measured, but every payload BELOW a root was classified by `family_of` alone** --
by `p441`'s tree enumeration and `p444`'s root-vs-tree comparison, both of which call
it and only it.  The pre-registered prediction for this pass was that the tree carries
MORE NonCommercial than the roots do, because a `docs/`, `data/` or `assets/` grant is
where CC-BY-NC lives by convention.

## The verdict function, and why it is shaped this way

    family      the FINE classifier (shell) wins wherever it names one; the coarse
                one is the fallback.  Not because it is better -- because neither is
                a superset of the other (P445), so declining is the only safe reason
                to defer.

    commercial  ALLOWED only if BOTH sides allow it.  The shell's `commercial_use_ok`
                is the authority by construction (P250 built family and commercial use
                as two independent axes), and a NonCommercial token in the coarse
                family is corroboration -- but for a BILLABLE deliverable the
                conservative composition is the correct one: one classifier saying
                "you may not sell this" is enough to stop.  Every row where the two
                disagree is counted and printed, never silently resolved.

TSV: slug, path, layer, bytes, py_family, sh_family, sh_commercial, family, commercial, flags
"""
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "p436-fork-hypothesis"))
sys.path.insert(0, os.path.join(HERE, "..", "p441-tree-licence-enumeration"))
from sweep_payload import family_of  # noqa: E402
import enumerate_licence as E  # noqa: E402

LIB = os.path.join(HERE, "..", "lib", "license_family.sh")

# NC as a licence-name TOKEN, never as a substring: `"NC" in "UNCLASSIFIED"` is True,
# and in pass 27 that put 11 false rows -- eight of them Finnish national-agency
# repositories -- into the class meaning "forbids commercial use".
NC_TOKEN = re.compile(r'(?:^|[^A-Za-z])NC(?:[^A-Za-z]|$)|NON-?COMMERCIAL', re.I)

_SH = (
    '. "$1"\n'
    'T=$(cat)\n'
    'F=$(osi_family_of "$T")\n'
    # `commercial_use_ok` signals through its EXIT STATUS, not stdout.  Capturing
    # stdout returned "" for all 412 rows in pass 27, MIT included, and read as
    # "commercial use not permitted" for the entire shelf.
    'if commercial_use_ok "$T"; then C=YES; else C=NO; fi\n'
    'printf "%s\\t%s\\n" "$F" "$C"\n'
)


def shell_classify(text):
    """(family, commercial) from the shell classifier, on the SAME bytes.

    stdin, not argv: several payloads exceed 35 kB and an argv list has a hard limit,
    so passing the text as an argument would silently truncate it and the failure would
    look like a classifier disagreement rather than a plumbing fault.
    """
    try:
        p = subprocess.run(["sh", "-c", _SH, "sh", LIB], input=text,
                           capture_output=True, text=True, timeout=60)
        out = (p.stdout or "").strip("\n").split("\t")
        return (out[0] if out else ""), (out[1] if len(out) > 1 else "")
    except Exception:
        return "", ""


def unified(text):
    """One family + one commercial verdict, consulting both classifiers.

    Returns (family, commercial, py, sh, sh_com, flags).
    """
    if not text:
        return "UNREADABLE", "UNDETERMINED", "-", "-", "-", ["UNREADABLE"]
    # -----------------------------------------------------------------------
    # P460 (pass 29).  A MARKUP CONTAINER DEFEATS THE TITLE RULE, AND THAT OPENS THE
    # TOKEN-MATCH PATH.  Measured, and it is the only thing this pass's tree sweep
    # flagged: `OS4ED/openSIS-Classic` and `OS4ED/openSIS-Responsive-Design` both ship
    # `docs/LICENSE.rtf` -- the same 61,575-byte file -- and it came back
    # commercial-use PROHIBITED from both repositories.
    #
    # It is a FALSE POSITIVE, and the chain has three sound links:
    #   1. the payload is RTF, so its first two non-blank lines are
    #      `{\rtf1\adeflang1025\ansi...` and a font table -- the title block is markup;
    #   2. with no readable title, every family probe declines, so the family is
    #      UNCLASSIFIED;
    #   3. P250's gate only short-circuits an IDENTIFIED family, so an UNCLASSIFIED one
    #      falls through to the token-match over the body -- and the body is GPL-2.0,
    #      whose section 3(c) says "this alternative is allowed only for noncommercial
    #      distribution".
    #
    # That phrase is a CONDITION on one distribution option, not a restriction on the
    # licensee -- which is EXACTLY what P250's own header already says about
    # "occasionally and noncommercially" in GPL-3.0 section 6.  The guarantee was in
    # place; the container walked around it.
    #
    # Verified first-hand: the same two repositories carry `docs/License.txt`, 17,286
    # bytes, opening on a plain `GNU GENERAL PUBLIC LICENSE / Version 2, June 1991`.
    # The licence is GPL-2.0 and commercial use is ALLOWED, so the false positive cost
    # an opportunity on a real SIS platform rather than creating a false permission.
    #
    # The fix DECLINES rather than guesses.  De-marking RTF well enough to recover a
    # title means parsing a font table, and a half-parsed container would reopen exactly
    # the token-match path this closes.  Saying "this toolchain cannot read this
    # payload" is an answer; inventing a verdict from its markup is not.
    _head = text.lstrip("\ufeff \t\r\n")[:16].lower()
    if _head.startswith("{\\rtf") or _head.startswith("%pdf-"):
        kind = "RTF" if "rtf" in _head else "PDF"
        return ("CONTAINER-%s (no legible)" % kind, "UNDETERMINED",
                "-", "-", "-", ["CONTAINER-" + kind])
    py = family_of(text)
    sh, sh_com = shell_classify(text)
    flags = []

    named_sh = bool(sh) and sh != "UNCLASSIFIED"
    named_py = py != "UNKNOWN"
    if named_sh:
        family = sh
    elif named_py:
        family = py
        flags.append("SHELL-DECLINED")
    else:
        family = "UNDETERMINED"
        flags.append("BOTH-DECLINED")

    nc_py = bool(NC_TOKEN.search(py))
    nc_sh = (sh_com == "NO")
    if nc_sh and not nc_py and named_py:
        flags.append("NC-ONLY-SHELL")
    if nc_py and not nc_sh:
        flags.append("NC-ONLY-PYTHON")
    # Conservative composition: one side forbidding is enough to forbid.
    #
    # AND THE NEGATIVE GOES BEFORE THE GATE.  The first cut of this function asked
    # `if family == "UNDETERMINED"` first and answered UNDETERMINED -- which HID three
    # root payloads whose family neither classifier can name and whose TEXT forbids
    # commercial use (`AStheTECH/mewcp-google-classroom`,
    # `Khan/tutoring-accuracy-dataset`, `leemonade/leemons`).  Measured: the PROHIBITED
    # count came out 8 when the shell's own axis says 11.
    #
    # It is P299's lesson committed inside a function written to compose the fix for it:
    # family and commercial use are INDEPENDENT axes (P250), so an unnameable family
    # still carries whatever its text restricts.  "We could not name this licence" must
    # never be allowed to overwrite "this licence forbids what you want to do with it".
    if nc_sh or nc_py:
        commercial = "PROHIBITED"
    elif family in ("UNDETERMINED", "UNREADABLE"):
        commercial = "UNDETERMINED"
    else:
        commercial = "ALLOWED"
    return family, commercial, py, sh or "-", sh_com or "-", flags


def one(job):
    slug, path, layer = job
    body = E.read_blob(slug, path)
    fam, com, py, sh, shc, flags = unified(body)
    return (slug, path, layer, str(len(body)), py, sh, shc, fam, com,
            ",".join(flags) if flags else "-")


def main():
    jobs = []
    # roots: the p445 denominator, so the two tables are comparable row for row
    with open(sys.argv[1]) as f:
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) >= 3 and c[1] == "LICENSED" and c[2] not in ("-", ""):
                jobs.append((c[0], c[2], "root"))
    # tree payloads: every path p441 and p444 actually read
    with open(sys.argv[2]) as f:
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) >= 2 and c[1]:
                jobs.append((c[0], c[1], "tree"))
    if not jobs:
        sys.stderr.write("p459: empty denominator -- a path fault (P355)\n")
        return 2
    print("\t".join(["slug", "path", "layer", "bytes", "py_family", "sh_family",
                     "sh_commercial", "family", "commercial", "flags"]))
    with ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(one, jobs):
            print("\t".join(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
