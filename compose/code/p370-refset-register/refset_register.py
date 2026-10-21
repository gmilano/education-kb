#!/usr/bin/env python3
"""`p370-refset-register` — a HEAD sha is not an identity proof, and 22 register rows rest on one.

WHY THIS EXISTS, measured at p370 and not suspected:

`gate-alias-canonical` was RED at `p369`'s HEAD with one finding —
`Dymayo/moodler-mcp` published as a live row while
`evidence/alias-register.2026-10-20-p349.tsv` calls that address `STALE` of
`GhaithAlHallak8/moodler-mcp`. The obvious discharge is to rewrite the shelf.

🔴 The register row is the thing that is wrong. One `ls-remote` pair refutes it:

    Dymayo/moodler-mcp            3 refs  (HEAD, main, fix/accept-token-without-privatetoken)
    GhaithAlHallak8/moodler-mcp  63 refs  (7 heads + 55 refs/pull/*/head + HEAD)
    both at HEAD 4e6139eb9c6b

`p349`'s own module docstring states the mechanism it is catching: GitHub keeps every
FORMER address of a renamed or transferred repository answering forever, BY REDIRECT.
A redirect serves ONE repository, so the old address must answer with the SAME ref set.
🔴 Three refs against sixty-three is not one repository under two addresses. It is a
FORK whose default branch happens to sit on its parent's HEAD — and this base already
recorded GitHub's own `forked from` label for that pair (`agents/trending.md` §36078).

Every `STALE` row in the register carries `identity_proof = head-p349`, i.e. HEAD
equality and nothing else. `p367`'s `ACTION ZZ-bw` had already measured that HEAD
equality is insufficient (26 collisions -> 23 SAME-REF-SET + 3 SAME-HEAD-ONLY) and
registered the obligation to re-derive. It was never re-derived, so a gate has been
enforcing a refuted proof onto correct shelves.

THE FINGERPRINT (this module), offline and total:

    fingerprint(refs)  -> a stable digest of the SET of ref NAMES, HEAD excluded
    classify(a, b)     -> SAME-REF-SET | SAME-HEAD-ONLY | DIFFERENT-HEAD | ONE-SIDE-DEAD

Only `SAME-REF-SET` may stand as `STALE` in the register. `SAME-HEAD-ONLY` is the fork
class and must be demoted to `DISTINCT` — the two addresses are two repositories, both
citable, and the shelf that cites either is correct.

🔵 Why names and not shas: a redirect serves identical names AND shas, so names are
sufficient and are stable across a fetch that races a push. `refs/pull/*` is KEPT —
it is the strongest fork discriminator on GitHub, because pull refs accrue to the
repository that receives the pull requests and a fork starts with none.

No network in this module. The caller supplies `ls-remote` output text
(`gap 139` — this harness installs nothing).
"""

import hashlib


def parse_ls_remote(text):
    """`git ls-remote` output text -> {ref_name: sha}. Tolerates the `ref:` symref line."""
    out = {}
    for line in (text or "").splitlines():
        line = line.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith("ref:"):
            # `ref: refs/heads/main\tHEAD` — a symref, not a ref of its own
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            parts = line.split(None, 1)
        if len(parts) < 2:
            continue
        sha, name = parts[0].strip(), parts[1].strip()
        if not sha or not name:
            continue
        out[name] = sha
    return out


def ref_names(refs):
    """The SET of ref names, HEAD excluded. HEAD is a symref and carries no identity."""
    return frozenset(n for n in refs if n != "HEAD")


def fingerprint(refs):
    """A stable digest of the ref-NAME set. Empty set -> the empty fingerprint."""
    names = sorted(ref_names(refs))
    if not names:
        return ""
    h = hashlib.sha256("\n".join(names).encode("utf-8")).hexdigest()
    return h[:12]


def head_sha(refs):
    """The sha HEAD points at, or '' when the remote did not answer."""
    return refs.get("HEAD", "")


def classify(a, b):
    """Two parsed ref maps -> the identity verdict.

    SAME-REF-SET    one repository under two addresses (a redirect). STALE is correct.
    SAME-HEAD-ONLY  same HEAD sha, different ref sets -> a fork. STALE is WRONG.
    DIFFERENT-HEAD  not the same repository and not even the same tip.
    ONE-SIDE-DEAD   at least one address did not answer; no verdict is available.
    """
    if not a or not b:
        return "ONE-SIDE-DEAD"
    fa, fb = fingerprint(a), fingerprint(b)
    if fa and fa == fb:
        return "SAME-REF-SET"
    ha, hb = head_sha(a), head_sha(b)
    if ha and ha == hb:
        return "SAME-HEAD-ONLY"
    return "DIFFERENT-HEAD"


#: the only verdict under which a register row may keep the `STALE` state
STALE_IS_SOUND = ("SAME-REF-SET",)


def register_verdict(verdict, state):
    """Does a register row's STATE survive the ref-set verdict?

    -> ("KEEP", reason) | ("DEMOTE", reason) | ("UNPROVEN", reason)
    """
    state = (state or "").upper()
    if state != "STALE":
        return ("KEEP", "row is not STALE; this instrument judges STALE only")
    if verdict in STALE_IS_SOUND:
        return ("KEEP", "ref sets identical — a redirect serves one repository")
    if verdict == "SAME-HEAD-ONLY":
        return ("DEMOTE", "same HEAD, different ref sets — a fork, not a redirect")
    if verdict == "DIFFERENT-HEAD":
        return ("DEMOTE", "neither ref set nor HEAD agrees — two repositories")
    return ("UNPROVEN", "an address did not answer; the row cannot be judged")
