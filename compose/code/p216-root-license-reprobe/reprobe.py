#!/usr/bin/env python3
"""ACTION QH — test the 18-form root probe itself, rather than trusting it a nineteenth time.

p211 recorded 94 shelf repositories as ABSENT: no licence blob at HEAD after 18 root path
forms. p215 recovered 25 of them through `git ls-tree`, leaving 63. T215-2 then observed two
repositories — thm-mni-ii/feedbacksystem and skhdemo/uoft-quercus-mcp — that serve a PLAIN
`LICENSE` AT ROOT and were nevertheless recorded ABSENT after all 18 forms.

If a plain-root-`LICENSE`-only re-probe recovers 2+ more of the remaining 63, the probe has a
loss mode that is independent of path reach, and every ABSENT figure this KB has published
measured the INSTRUMENT rather than the population.

Method, deliberately minimal so that only one variable moves:
  1. `git ls-remote --symref <url> HEAD`  -> the TRUE default branch name.
     (p205's ACTION PC established that guessing `main`/`master` is itself a loss mode.)
  2. ONE GET of raw.githubusercontent.com/<repo>/<branch>/LICENSE.
     No case variants, no extensions, no subdirectories, no manifests. Those channels are
     p215's; this pass tests the single most obvious path only.

Channel control (re-tested this pass, eleventh time): api.github.com -> 403,
raw.githubusercontent.com -> 200, git ls-remote -> works. See ACTION PD / Gap 241.
"""

import subprocess
import sys
import urllib.request

RAW = "https://raw.githubusercontent.com/{repo}/{branch}/LICENSE"
TIMEOUT = 30


def default_branch(repo):
    """The repository's true default branch, from the remote's symref, or None."""
    try:
        out = subprocess.run(
            ["git", "ls-remote", "--symref", f"https://github.com/{repo}", "HEAD"],
            capture_output=True, text=True, timeout=60,
        ).stdout
    except subprocess.TimeoutExpired:
        return None
    for line in out.splitlines():
        if line.startswith("ref:"):
            return line.split()[1].rsplit("/", 1)[-1]
    return None


def probe(repo, branch):
    """(status, bytes) for a single GET of the plain root LICENSE."""
    url = RAW.format(repo=repo, branch=branch)
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
            return r.status, len(r.read())
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception as e:                                  # noqa: BLE001
        return f"ERR:{type(e).__name__}", 0


def main(path):
    with open(path) as fh:
        repos = [l.strip() for l in fh if l.strip() and not l.startswith("#")]

    print("repo\tdefault_branch\tstatus\tbytes")
    for repo in repos:
        branch = default_branch(repo)
        if branch is None:
            print(f"{repo}\tNO-SYMREF\t-\t0", flush=True)
            continue
        status, size = probe(repo, branch)
        print(f"{repo}\t{branch}\t{status}\t{size}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
