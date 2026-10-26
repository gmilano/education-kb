#!/usr/bin/env python3
"""p456 -- the ref axis is RESOLVED, not guessed.

Every pass from `p449` to `p455` read grants by GUESSING refs: a fixed list
(`HEAD`, `main`, `master`, `develop`, `dev`, `development`, `trunk`) walked
until something served 200. `Gap 455-A` found the first failure of that design
-- `HEAD` is not always the default branch -- and fixed it by walking MORE
refs and accepting the first grant found.

🔴 That fix is unsound, and this file is the measurement that shows why.

`git ls-remote` WORKS from this host against arbitrary public GitHub
repositories. It was never tried: `Gap 449-A` established that
`curl -sI https://github.com/...` returns 403 here, and every pass since has
read that as "github.com is closed", so the ref axis was guessed for seven
passes while the authoritative answer was one command away.

What it establishes on `lanis-mobile/LanisAPI` (shelved by `p455` as
`kurwjan/LanisAPI`, MIT, grant read at `master`):

    $ git ls-remote --symref .../LanisAPI HEAD
    ref: refs/heads/deprecation-notice   HEAD

    refs/heads/  ->  deprecated-0.4.1, deprecation-notice      <- NO master
    raw .../master/LICENSE     200  1 076 B  sha 0bc449776673
    raw .../deprecated-0.4.1/LICENSE  200  1 076 B  sha 0bc449776673   <- same

🔴 `master` IS NOT A BRANCH OF THIS REPOSITORY. raw.githubusercontent serves
it because GitHub keeps a rename redirect, and it resolves to a branch whose
own name says `deprecated`. The repository's real default branch carries a
331-byte README that says, in German, that the project IS DEPRECATED and
development has moved to `lanis-mobile/liblanis-for-python`.

So `p455` published, as a usable EMEA dependency, a grant that the project has
WITHDRAWN -- read from a ref that no longer exists, in a repository whose HEAD
says do not use it. A ladder that accepts the first ref serving a grant cannot
tell a current grant from an abandoned one, because a stale alias answers 200
exactly like a live branch.

This file therefore gives the reader a verdict the shelves have never had:

  GRANT_AT_DEFAULT          the grant is at the resolved default branch -- the
                            only class that may be shelved as a dependency
  GRANT_OFF_DEFAULT         grant on a live non-default branch; real, but it
                            is that branch's grant and must be cited as such
  GRANT_ONLY_AT_ALIAS       grant readable ONLY at a ref in NO ref list -- a
                            rename redirect. The LanisAPI class. NOT shelveable
  LIVE_NO_GRANT             default branch resolves, no grant at any path
  ADDRESS_DEAD              ls-remote resolves nothing (`Gap 454-H`'s split)

`ADDRESS_DEAD` is now decided by ls-remote rather than by a 404 sweep, which
is both cheaper (1 request, not 91) and stronger: it distinguishes "no such
repository" from "repository with no licence file" WITHOUT guessing paths.
"""
import re
import subprocess

from fetch import raw, digest, GRANT_PATHS

UA = "globant-kb-education-research/p456"


def ls_remote(owner_repo, timeout=60, want_sha=False):
    """(default_branch, heads, tags) read from the remote itself.

    Returns (None, [], []) when the remote resolves nothing -- which is the
    authoritative ADDRESS_DEAD, not an inference from 404s.

    With `want_sha`, returns (default, heads, tags, head_sha, head_shas) where
    `head_shas` maps branch -> commit. That pair settles `Gap 455-A` for free:
    HEAD's own commit is in the SAME ls-remote response as every branch's, so
    "does HEAD follow the default branch?" is answerable with NO extra request
    and no byte-level comparison of READMEs.
    """
    url = f"https://github.com/{owner_repo}"
    try:
        p = subprocess.run(["git", "ls-remote", "--symref", url],
                           capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return (None, [], [], "", {}) if want_sha else (None, [], [])
    if p.returncode != 0:
        return (None, [], [], "", {}) if want_sha else (None, [], [])
    default, heads, tags = None, [], []
    head_sha, head_shas = "", {}
    for line in p.stdout.decode("utf-8", "replace").splitlines():
        m = re.match(r"^ref:\s+refs/heads/(\S+)\s+HEAD$", line)
        if m:
            default = m.group(1)
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        sha, ref = parts[0].strip(), parts[1].strip()
        if ref == "HEAD":
            head_sha = sha
        elif ref.startswith("refs/heads/"):
            heads.append(ref[len("refs/heads/"):])
            head_shas[ref[len("refs/heads/"):]] = sha
        elif ref.startswith("refs/tags/") and not ref.endswith("^{}"):
            tags.append(ref[len("refs/tags/"):])
    if want_sha:
        return (default, heads, tags, head_sha, head_shas)
    return (default, heads, tags)


def _grant_at(owner_repo, ref):
    """First readable grant payload at ONE ref. Status gated (`Gap 453-E`)."""
    for path in GRANT_PATHS:
        st, body = raw(owner_repo, ref, path)
        if st == 200 and body.strip():
            return {"ref": ref, "path": path, "bytes": len(body),
                    "sha": digest(body),
                    "text": body.decode("utf-8", "replace")}
    return None


def grant(owner_repo, alias_probe=("master", "main")):
    """Resolve the ref axis, then read the grant on it.

    `alias_probe` refs are read ONLY to detect the stale-alias class. A hit
    there is never promoted to a grant: that is the whole point of this pass.
    """
    default, heads, tags = ls_remote(owner_repo)
    if default is None and not heads:
        return {"verdict": "ADDRESS_DEAD", "default": "", "heads": [],
                "bytes": 0, "sha": "", "text": "", "path": "", "ref": ""}

    if default:
        g = _grant_at(owner_repo, default)
        if g:
            g.update({"verdict": "GRANT_AT_DEFAULT", "default": default,
                      "heads": heads})
            return g

    # Not on the default branch. Any OTHER live branch is a real ref, but the
    # grant it serves is that branch's, and it is reported as such.
    for h in [h for h in heads if h != default]:
        g = _grant_at(owner_repo, h)
        if g:
            g.update({"verdict": "GRANT_OFF_DEFAULT", "default": default or "",
                      "heads": heads})
            return g

    # Nothing on any live branch. If a guessed alias still serves a grant,
    # that grant lives at a ref the repository no longer lists.
    for a in alias_probe:
        if a in heads:
            continue
        g = _grant_at(owner_repo, a)
        if g:
            g.update({"verdict": "GRANT_ONLY_AT_ALIAS",
                      "default": default or "", "heads": heads})
            return g

    return {"verdict": "LIVE_NO_GRANT", "default": default or "",
            "heads": heads, "bytes": 0, "sha": "", "text": "", "path": "",
            "ref": default or ""}
