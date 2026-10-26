#!/usr/bin/env python3
"""p455 -- the same read channel as `fetch.py`, with the probe LADDER made
cheap enough to run over a 481-cell population.

`fetch.grant()` sweeps refs x paths = up to 7 x 13 = 91 requests for a dead
address. Correct, and unusable at this denominator: the first run of
`sweep.py` was killed after ten minutes without reaching its first verdict.

The ladder here spends requests in proportion to what is still unknown, and it
preserves both properties the earlier gaps paid for:

  `Gap 454`'s non-`main` refs -- 13 of 58 live addresses on these shelves are
  not on `main`. The first cut of this ladder assumed `HEAD` on
  raw.githubusercontent follows the repository's own default branch, so that
  ONE probe would cover every one of them. 🔴 THAT ASSUMPTION IS FALSE, and
  this pass measured it first-hand on `kurwjan/LanisAPI`:

      HEAD/LICENSE    404  (14 B)      HEAD/README.md    200  (331 B)
      master/LICENSE  200  (1 076 B)   master/README.md  200  (3 554 B)

  Two different READMEs of two different sizes: `HEAD` and `master` are
  different commits, and the substantive tree -- including the MIT grant -- is
  on `master` only. So a ladder that takes the FIRST ref whose README resolves
  publishes `REPO_LIVE_NO_GRANT` for a repository that carries an MIT licence
  one ref over. That is a false "ungranted", and it fails in the direction
  that DISCARDS a usable permissive dependency.

  `Gap 454-H`'s split -- "repository exists without a licence file" and
  "repository is gone" both return 404 on every grant path, so liveness is
  asked on a NON-licence path before `ADDRESS_DEAD` is published.

Rung 1: HEAD x 5 commonest grant paths     (hit: 1 round of 5)
Rung 2: HEAD x README etc                  (liveness)
Rung 3: HEAD x 8 remaining grant paths     (live, no grant at the common paths)
Rung 4: named refs, same ladder
"""
from concurrent.futures import ThreadPoolExecutor
from fetch import raw, digest

COMMON = ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "LICENCE"]
RARE = ["LICENCE.md", "COPYING.txt", "COPYING.LESSER", "LICENSE-MIT",
        "license", "License", "LICENSE.rst", "docs/License.txt"]
LIVE = ["README.md", "readme.md", "README", "package.json", "pyproject.toml",
        "Cargo.toml", "composer.json"]
ALT_REFS = ["master", "main", "develop", "dev", "development", "trunk"]


def _first_hit(owner_repo, ref, paths, workers=5):
    """First path in `paths` serving 200 with a body. Probed concurrently, but
    the VERDICT is taken in list order, so the result does not depend on which
    thread finished first."""
    with ThreadPoolExecutor(max_workers=workers) as ex:
        results = list(ex.map(lambda p: (p,) + raw(owner_repo, ref, p), paths))
    for path, st, body in results:
        if st == 200 and body.strip():
            return (path, body)
    return (None, None)


def grant(owner_repo):
    live_but_ungranted = None
    for ref in ["HEAD"] + ALT_REFS:
        path, body = _first_hit(owner_repo, ref, COMMON)
        if body is None:
            live_path, _ = _first_hit(owner_repo, ref, LIVE)
            if live_path is None:
                continue            # this ref does not resolve; try the next
            path, body = _first_hit(owner_repo, ref, RARE)
            if body is None:
                # Live here, no grant HERE. That is not a verdict: remember it
                # and keep walking the refs (the kurwjan/LanisAPI case above).
                live_but_ungranted = live_but_ungranted or (ref, live_path)
                continue
        return {"verdict": "READ", "ref": ref, "path": path,
                "bytes": len(body), "sha": digest(body),
                "text": body.decode("utf-8", "replace")}
    if live_but_ungranted:
        ref, live_path = live_but_ungranted
        return {"verdict": "REPO_LIVE_NO_GRANT", "ref": ref,
                "live_path": live_path, "bytes": 0, "sha": "", "text": "",
                "path": ""}
    return {"verdict": "ADDRESS_DEAD", "ref": "", "bytes": 0, "sha": "",
            "text": "", "path": ""}
