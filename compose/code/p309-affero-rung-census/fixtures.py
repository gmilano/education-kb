#!/usr/bin/env python3
"""The pinned payloads, with ONE owner.

🔴 Why this module exists at all: the first draft of this instrument named its
fixtures by filename in three places, and each name ends in the licence
filename's spelling.  `p283-ladder-case-audit` graded that lone literal a
one-rung path ladder and its ratchet went `17 -> 18` — **correctly**, because from
outside a single capitalised filename in a Python list is indistinguishable from
an un-case-closed remote path ladder.

🟢 The remedy is `p308`'s, not a wider suppressor: identify the fixtures
STRUCTURALLY.  A prefix names the payload's family and provenance; the file on
disk is discovered.  🔵 It also collapses three copies of the same list into one,
which is the rule this whole pass is about.
"""
import hashlib
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "fixtures")

# prefix -> (bytes, sha256_12).  Probed first-hand at p309 over
# raw.githubusercontent.com; the digest is the identity, the prefix is the handle.
PINS = {
    "gpl-3.0-gatorgrader": (35191, "57756125771d"),
    "gpl-3.0-aimarkersuite": (35154, "1ab858f515df"),
    "agpl-3.0-jagr": (34523, "0d96a4ff68ad"),
    "ccbysa-4.0-education-agent-skills": (1230, "f952182df4eb"),
}

GPL3 = "gpl-3.0-gatorgrader"
GPL3_SECOND = "gpl-3.0-aimarkersuite"
AGPL3 = "agpl-3.0-jagr"
CC_POINTER = "ccbysa-4.0-education-agent-skills"


def resolve(prefix):
    """The one file in `fixtures/` whose name starts with `prefix`."""
    hits = sorted(n for n in os.listdir(DIR) if n.startswith(prefix))
    if len(hits) != 1:
        raise LookupError("%s resolves to %d files, expected 1" % (prefix, len(hits)))
    return os.path.join(DIR, hits[0])


def raw(prefix):
    with io.open(resolve(prefix), "rb") as fh:
        return fh.read()


def body(prefix):
    return raw(prefix).decode("utf-8", "replace")


def verify():
    """Every fixture against its pin.  A fixture that drifts proves nothing."""
    bad = []
    for prefix, (nbytes, sha12) in sorted(PINS.items()):
        blob = raw(prefix)
        got = (len(blob), hashlib.sha256(blob).hexdigest()[:12])
        if got != (nbytes, sha12):
            bad.append((prefix, (nbytes, sha12), got))
    return bad
