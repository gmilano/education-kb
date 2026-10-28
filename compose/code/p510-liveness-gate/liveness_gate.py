"""p510 — liveness instrument with a MANDATORY known-good/known-bad control.

`Gap 509-B` asked that the control stop being advisory. This module makes it
structural: `sweep()` cannot return a count unless `run_controls()` has passed
on this channel, in this session, first.

Channel facts measured in p510 (evidence/url-check-control.2026-10-28-p510.tsv):

  curl -sI https://github.com/<slug>      403 for LIVE *and* ABSENT  -> zero information.
  git ls-remote --symref <slug>           refs for live+public; a credential prompt for
                                          ABSENT *and* PRIVATE alike -> sound POSITIVE test only.
  raw.githubusercontent.com/<slug>/<br>/  200 live path / 404 absent path -> discriminates,
                                          but conflates "repo absent" with "path absent".

So LIVE is assertable and ABSENT is not. The classifier below never returns
"ABSENT"; the honest state is UNREADABLE_ABSENT_OR_PRIVATE, which a second
channel (the MCP GitHub channel) must resolve before any address is retired.
"""
from __future__ import annotations

import subprocess
from dataclasses import dataclass

LIVE = "LIVE"
LIVE_EMPTY = "LIVE_EMPTY"
UNREADABLE = "UNREADABLE_ABSENT_OR_PRIVATE"
ERROR = "ERROR"

KNOWN_GOOD = "HKUDS/DeepTutor"
KNOWN_BAD = "gmilano/definitely-not-a-real-repo-p510-control"


@dataclass(frozen=True)
class Read:
    state: str
    branch: str | None = None
    head: str | None = None


def classify(stdout: str, stderr: str) -> Read:
    """Pure classifier over `git ls-remote --symref <url> HEAD` output.

    Kept free of I/O so the controls can run against recorded fixtures offline.
    """
    branch = head = None
    for line in stdout.splitlines():
        if line.startswith("ref:"):
            branch = line.split()[1].removeprefix("refs/heads/")
        parts = line.split()
        if len(parts) == 2 and parts[1] == "HEAD":
            head = parts[0][:12]
    if head:
        return Read(LIVE, branch, head)
    blob = stderr + stdout
    if "could not read Username" in blob or "Authentication failed" in blob:
        # GitHub answers an absent repo and a private one identically here.
        return Read(UNREADABLE)
    if "empty repository" in blob:
        return Read(LIVE_EMPTY)
    return Read(ERROR)


def probe(slug: str, timeout: int = 60) -> Read:
    proc = subprocess.run(
        ["git", "ls-remote", "--symref", f"https://github.com/{slug}", "HEAD"],
        capture_output=True, text=True, timeout=timeout,
        env={"GIT_TERMINAL_PROMPT": "0", "GIT_ASKPASS": "/bin/true", "PATH": "/usr/bin:/bin"},
    )
    return classify(proc.stdout, proc.stderr)


class ControlFailure(RuntimeError):
    """Raised instead of returning a count the controls have not earned."""


def run_controls(probe_fn=probe) -> None:
    good = probe_fn(KNOWN_GOOD)
    bad = probe_fn(KNOWN_BAD)
    if good.state != LIVE:
        raise ControlFailure(f"known-good {KNOWN_GOOD} read {good.state}, not LIVE")
    if bad.state == LIVE:
        raise ControlFailure(f"known-bad {KNOWN_BAD} read LIVE; instrument cannot discriminate")


def sweep(slugs, probe_fn=probe) -> dict[str, Read]:
    """Probe every slug. Refuses to run at all until the controls pass."""
    run_controls(probe_fn)
    return {slug: probe_fn(slug) for slug in slugs}
