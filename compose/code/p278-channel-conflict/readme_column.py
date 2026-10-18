"""`ACTION p293` — the README channel as a COLUMN of `p278`'s sweep, not a hand-run.

`p288` built the README-claim classifier and `p289`-`p292` each carried *"wire the README channel
into `p278`'s sweep — one column in `sweep.sh`, classifier already written"* as the cheapest
unspent item on the backlog.  FIVE passes.  This file is that wire.

🔴 WHY IT KEPT NOT HAPPENING, visible in the Makefile's own header: an instrument that works
only when run by hand from its own directory never becomes a column.  `p293` hit the same thing
from the other side — it classified two live READMEs by hand, got the right answers
(`AGREE`/`BUILD-ON` for `tokenaii/Horus-Taleeq-0.2B-Base`, `DANGLING-CLAIM`/`ASK` for
`tokenaii/Horus-Lens-1.0`), and that hand-run is precisely the thing this column replaces.

🔵 THE LADDER IS NOT COPIED.  `--paths` prints `p288`'s `README_PATHS` so `sweep.sh` can walk the
ladder without a second copy of it.  A duplicated ladder is the `p283`/`p1057` defect waiting to
happen: `p282` found `README.MD` on `ls1intum/Pyris` only after `p268` published "neither
repository serves a README" off a ladder with no uppercase extension in it.  One ladder, one
place, and `sweep.sh` reads it rather than restating it.

Runs under `python3 -I`, which strips the script's own directory from `sys.path` — so the sibling
import is resolved from `__file__` explicitly.  That is `p355-cwd-portability`'s class, and it is
the reason the Makefile `cd`s into every instrument.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "p288-readme-channel"))

from readme_claim import README_PATHS, channel_verdict, readme_claim  # noqa: E402


def main(argv):
    if len(argv) >= 2 and argv[1] == "--paths":
        # The single source of truth for the ladder, emitted for the shell to walk.
        print("\n".join(README_PATHS))
        return 0
    if len(argv) < 3:
        sys.stderr.write("usage: readme_column.py (--paths | README_FILE PAYLOAD_FAMILY)\n")
        return 2
    path, payload_family = argv[1], argv[2]
    # `-` is sweep.sh's "no payload read" marker; the classifier wants None for that.
    fam = None if payload_family in ("-", "", "UNRESOLVED") else payload_family
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        # 🔴 Unreadable is NOT "no claim".  p278's own header makes the same distinction for
        # the manifest channel: a channel that did not measure is not a measured absence.
        print("\t".join(["READ-FAIL", "NO-CHANNEL"]))
        return 0
    kind, family = readme_claim(text)
    verdict = channel_verdict((kind, family), fam)
    claim = family if kind == "CLAIM" and family else kind
    print("\t".join([str(claim), str(verdict)]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
