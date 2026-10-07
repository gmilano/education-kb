#!/usr/bin/env python3
"""p445 — this KB has TWO licence classifiers and only one of them knows NonCommercial.

**P445: a hardened classifier that is not wired into the newer path protects nothing.**

Measured on the same 19,333 bytes of
`facebookresearch/seamless_communication`'s root `LICENSE`:

    lib/license_family.sh   osi_family_of    -> CC-BY-NC-4.0   commercial_use_ok -> (empty)
    p436/sweep_payload.py   family_of        -> CC-BY          <-- the NC is GONE

The shell classifier is the hardened one: **106/106** on its own suite, and `P312`'s
`test_nc_gate.sh` (**21/21**) exists specifically to assert that *"a payload with a
NonCommercial restriction answers PROHIBITED on the commercial-use axis **and keeps
the NC attribute in its family**"*.

The Python `family_of` has no NC concept at all.  And `family_of` is what
**`p436`** (the 503-slug payload sweep), **`p441`** (pass 26's tree enumeration) and
**`p444`** (pass 27's root-vs-tree comparison) all call.  So every family verdict those
three instruments published passed through a classifier that **cannot express the one
attribute that decides whether Globant may bill for the work.**

`agents/top.md` carries the correct verdict for the specimen — *"**CC BY-NC-4.0** in
`main/LICENSE` — **non-commercial. Hard reject** for anything billable"* — so the shelf
is right and the instrument is blind.  That is the same direction as pass 26's best
finding, which is why it is worth counting rather than fixing quietly.

## What this measures

Both classifiers over the **same bytes** of every root licence payload on the
`LICENSED` side, and the divergences classified:

    AGREE                both name the same family
    NC-ERASED            🔴 shell says NonCommercial, python names a family that does
                         not -- the class that reaches a client invoice
    VOCABULARY           they disagree on the name without disagreeing on the class
                         (e.g. `GPL` vs `GPL-2.0`, `EUPL` vs `EUPL-1.2`)
    PYTHON-UNKNOWN       python declines, shell names one
    SHELL-UNKNOWN        shell declines, python names one

TSV: slug, path, bytes, python_family, shell_family, shell_commercial_ok, verdict
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
import enumerate_licence as E  # noqa: E402  -- read_blob, one implementation

LIB = os.path.join(HERE, "..", "lib", "license_family.sh")

# Families that permit commercial use.  Used only to decide whether an NC payload was
# classified into a commercially-usable bucket -- never to assert a licence.
NC_TOKEN = re.compile(r'(?:^|[^A-Za-z])NC(?:[^A-Za-z]|$)|NON-?COMMERCIAL', re.I)

COMMERCIAL_OK = {
    "MIT", "Apache-2.0", "BSD", "BSD-2-Clause", "BSD-3-Clause", "ISC", "CC0-1.0",
    "Unlicense", "ECL-2.0", "NCSA", "Zlib", "OFL-1.1", "MPL-2.0", "EPL-2.0",
    "GPL", "GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL", "LGPL-2.1", "LGPL-3.0",
    "EUPL", "EUPL-1.2", "CC-BY", "CC-BY-4.0", "CC-BY-SA",
}


def shell_classify(text):
    """(family, commercial_ok) from lib/license_family.sh, on the SAME bytes.

    The payload is passed on stdin, not as an argv string: several of these are
    >35 kB and an argv list has a hard limit, which would silently truncate the
    text and change the verdict -- the failure mode would look like a classifier
    disagreement rather than a plumbing fault.
    """
    # P445's own second defect: `commercial_use_ok` signals through its EXIT STATUS
    # (`return 0` / `return 1`), not through stdout.  Capturing stdout returned the
    # empty string for all 412 rows -- MIT included -- which read as "commercial use
    # not permitted" for the entire shelf.  A column that is constant across every
    # row is not a measurement, and this one was constant at the alarming value.
    script = (
        '. "$1"\n'
        'T=$(cat)\n'
        'F=$(osi_family_of "$T")\n'
        'if commercial_use_ok "$T"; then C=YES; else C=NO; fi\n'
        'printf "%s\\t%s\\n" "$F" "$C"\n'
    )
    try:
        p = subprocess.run(["sh", "-c", script, "sh", LIB], input=text,
                           capture_output=True, text=True, timeout=60)
        out = (p.stdout or "").strip("\n").split("\t")
        return (out[0] if out else ""), (out[1] if len(out) > 1 else "")
    except Exception:
        return "", ""


def one(job):
    slug, path = job
    body = E.read_blob(slug, path)
    if not body:
        return (slug, path, "0", "-", "-", "-", "UNREADABLE")
    py = family_of(body)
    sh, com = shell_classify(body)
    # P445's own FIRST defect, and the funnier one: `"NC" in "UNCLASSIFIED"` is True.
    # A bare substring test put 11 rows in the NC-ERASED class whose shell verdict was
    # `UNCLASSIFIED` -- including eight Finnish national-agency repositories -- and the
    # class that is supposed to mean "this forbids commercial use" was 73% noise.
    # NC is a licence-name TOKEN, so it is matched as one.
    # The COMMERCIAL AXIS decides this, not the family name.  `P250` built the two as
    # independent axes and `commercial_use_ok` is the one that answers the question;
    # measured here, it says NO for 11 of 412 payloads while the family string carries
    # a visible `NC` token for only 5 of them.  The remaining 6 are `Elastic`,
    # `PolyForm` and three payloads whose family is UNCLASSIFIED but whose text
    # restricts commercial use -- all of which the name token would have missed.
    # NC_TOKEN is kept as corroboration and reported, never as the gate.
    shell_nc = (com == "NO")
    if shell_nc and py in COMMERCIAL_OK:
        # The class that reaches an invoice: the shell knows the payload bars
        # commercial use, and the python side asserts a POSITIVELY commercially-usable
        # family.  A python `UNKNOWN` is excluded on purpose -- declining to answer is
        # not the same error as answering "permissive", and only the second one gets
        # quoted into a proposal.
        v = "NC-ERASED"
    elif not sh and py != "UNKNOWN":
        v = "SHELL-UNKNOWN"
    elif sh and py == "UNKNOWN":
        v = "PYTHON-UNKNOWN"
    elif sh.upper().startswith(py.upper()) or py.upper().startswith(sh.upper()):
        v = "AGREE"
    elif sh == py:
        v = "AGREE"
    else:
        v = "VOCABULARY"
    return (slug, path, str(len(body)), py, sh or "-", com or "NO", v)


def main():
    jobs = []
    with open(sys.argv[1]) as f:
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) >= 3 and c[1] == "LICENSED" and c[2] not in ("-", ""):
                jobs.append((c[0], c[2]))
    if not jobs:
        sys.stderr.write("p445: empty denominator -- a path fault (P355)\n")
        return 2
    print("\t".join(["slug", "path", "bytes", "python_family", "shell_family",
                     "shell_commercial_ok", "verdict"]))
    with ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(one, jobs):
            print("\t".join(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
