"""`P176-B` — ONE ordered grant-path vocabulary, so that an absence claim names
the vocabulary it was reached with.

The defect this exists for, measured at p176: `compose/code/` contains `76`
independent hardcoded grant-path probe lists. `48` carry the British `LICENCE`.
`3` carry `COPYING.md`. So "extend the probe list" is not an edit, it is a
migration across 76 call sites (`T272`).

The rule, stated before it is coded:

  A licence-ABSENCE claim is a claim about the PATHS PROBED and the REF probed,
  never about the repository (`P50`, `T209`). This module therefore exports a
  VERSIONED vocabulary, and `absence_claim()` renders a sentence that carries
  the version with it. A claim written this way is falsifiable by a later pass
  that grows the vocabulary; "no grant file" is not.

  Order matters and is part of the vocabulary: the canonical American spellings
  first, because they are overwhelmingly the most common and a probe that stops
  at the first hit should stop early; then the British spellings; then the
  `COPYING` family, which is where GPL projects put the body; then the
  capitalised and lowercase variants; then the split `LICENSE-<FAMILY>` shapes;
  then `NOTICE`, which is NOT a grant and is probed only so that finding one can
  be reported as "a notice, not a grant".

  `NOTICE` is deliberately last and deliberately flagged. An `Apache-2.0`
  project with a `NOTICE` and no `LICENSE` has an attribution file and no grant,
  and a vocabulary that silently counted it as a hit would convert a true
  absence into a false licence.

The stronger test, when the tree is small enough to afford it, is to ENUMERATE
rather than probe: `ACTION KJ` settled a shelf row by listing all 5 branches of
a 12-file repository, which is a claim no longer path-list-dependent at all.
`enumeration_beats_probing()` states that boundary in code.
"""

from __future__ import annotations

VERSION = "v1"

AMERICAN = ("LICENSE", "LICENSE.md", "LICENSE.txt")
BRITISH = ("LICENCE", "LICENCE.md", "LICENCE.txt")
COPYING = ("COPYING", "COPYING.md", "COPYING.txt")
CASE_VARIANTS = ("License", "License.md", "license", "license.md")
SPLIT_FAMILY = ("LICENSE-MIT", "LICENSE-APACHE")
NOT_A_GRANT = ("NOTICE",)

VOCABULARY: tuple[str, ...] = (
    AMERICAN + BRITISH + COPYING + CASE_VARIANTS + SPLIT_FAMILY + NOT_A_GRANT
)

#: Paths that, if they are the ONLY hit, do not support a licence verdict.
NON_GRANT_HITS = frozenset(NOT_A_GRANT)

#: Trees at or below this many tracked files should be ENUMERATED, not probed.
ENUMERATION_THRESHOLD = 200


def is_grant_path(path: str) -> bool:
    """True when a 200 at this path supports a licence verdict."""
    return path in VOCABULARY and path not in NON_GRANT_HITS


def enumeration_beats_probing(tracked_files: int) -> bool:
    """A 12-file repository should be listed, not probed. The threshold is a
    judgement about cost, not a measurement, and it is named so it can be
    argued with."""
    return tracked_files <= ENUMERATION_THRESHOLD


def absence_claim(repo: str, ref: str, probed: int, hits: int) -> str:
    """Render an absence claim that carries its own falsifier."""
    if hits:
        raise ValueError("not an absence claim: there were hits")
    return (
        f"{repo}: 0 of {probed} grant paths at ref {ref} "
        f"(vocabulary {VERSION}) — an absence AT THESE PATHS ON THIS REF"
    )


def exhaustive_claim(repo: str, refs: tuple[str, ...], paths_seen: int) -> str:
    """The only claim entitled to the word 'exhaustive': every ref the remote
    advertises was ENUMERATED, so no path list is involved."""
    if not refs:
        raise ValueError("exhaustive needs at least one ref")
    return (
        f"{repo}: 0 grant-shaped paths in {paths_seen} file-paths across "
        f"{len(refs)} branches ({', '.join(refs)}) — exhaustive by ENUMERATION"
    )


if __name__ == "__main__":
    print(f"vocabulary {VERSION}: {len(VOCABULARY)} paths")
    for path in VOCABULARY:
        flag = "" if is_grant_path(path) else "   (NOT a grant)"
        print(f"  {path}{flag}")
