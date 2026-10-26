#!/usr/bin/env python3
"""p453 — vocabulary spend ledger + two-probe promotion precondition.

Registered as the instrument `Gap 452-A` says does not exist ("No instrument
records which vocabularies have been spent, so the next pass will re-spend them
blind") and as the gate `Gap 452-B` says is missing ("no gate enforces that a
registry-sourced candidate be HEAD-probed before promotion").

Defect lessons from earlier passes are encoded here, not re-learnt:

  Gap 451-A  an address is taken ONLY from a record's own `repository`
             back-link, never derived from the package name. Deriving it
             produced 3 of 3 false DISAGREE verdicts in p452.
  Gap 452-B  a back-link proves an address EXISTED, never that it is
             reachable now. Both probes must pass independently.
  Gap 452-C  registry corroboration is ecosystem-specific: npm `repository`
             is near-universal, PyPI `project_urls` is optional and often
             null, so the ABSENT verdict is reported per ecosystem.
  Gap 452-F  identity keys are case-folded; GitHub resolves owner/repo
             case-insensitively, so two spellings are one address.
  p452       the URL normaliser is FORGE-QUALIFIED (github.com-only matching
             manufactured a false ABSENT for a correct GitLab back-link).
"""
import json, re, subprocess, sys, time, urllib.parse

UA = "globant-kb-p453/1.0"
TIMEOUT = "25"


def curl(url, head=False):
    cmd = ["curl", "-s", "-A", UA, "--max-time", TIMEOUT, "-w", "\n%{http_code}"]
    if head:
        cmd += ["-o", "/dev/null"]
    cmd.append(url)
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout.rsplit("\n", 1)
    if len(out) != 2:
        return None, "000"
    return out[0], out[1].strip()


def norm(url):
    """Forge-qualified identity: forge/owner/repo, case-folded (Gap 452-F).

    Returns None when no forge-qualified address can be read. Never guesses
    from a package name (Gap 451-A).
    """
    if not url or not isinstance(url, str):
        return None
    u = url.strip()
    u = re.sub(r"^git\+", "", u)
    u = re.sub(r"^(git|ssh)://", "https://", u)
    u = re.sub(r"^git@([^:]+):", r"https://\1/", u)
    # A GitHub *Pages* host asserts a published page, not a repository, and its
    # owner segment need not equal the repository owner (p452's PAGES_ONLY trap).
    # Graded BEFORE the two-segment match below, because a Pages URL usually
    # carries only ONE path segment -- requiring two made this class unreachable
    # in p453's own first cut, which is p452 defect (e) exactly.
    mp = re.match(r"^https?://([^/]+\.github\.io)(?:/([^/#?]+))?", u)
    if mp:
        return ("PAGES", mp.group(1).lower(), mp.group(1).split(".")[0].lower(),
                re.sub(r"\.git$", "", (mp.group(2) or "")).lower())
    m = re.match(r"^https?://(?:www\.)?([^/]+)/([^/]+)/([^/#?]+)", u)
    if not m:
        return None
    forge, owner, repo = m.group(1).lower(), m.group(2), m.group(3)
    repo = re.sub(r"\.git$", "", repo)
    if forge not in ("github.com", "gitlab.com", "bitbucket.org", "codeberg.org",
                     "git.sr.ht", "framagit.org", "salsa.debian.org"):
        return ("FOREIGN_FORGE", forge, owner, repo)
    return ("OK", forge, owner.lower(), repo.lower())


def live_probe(forge, owner, repo):
    """Two-stage reachability probe standing since p450.

    curl -sI github.com/{slug} is a CONSTANT 403 on this host class for real
    AND fabricated slugs alike (p449/p450, re-confirmed p453), so it carries
    zero bits and is not used. Stage 1 is the raw path; stage 2 escalates to
    ls-remote because raw is case-sensitive on the PATH and a repo may serve
    README.rst / readme.md / README.markdown (Gap 449-B, Gap 420-B).
    """
    if forge == "github.com":
        for path in ("README.md", "readme.md", "README.rst", "README.markdown", "LICENSE"):
            _, code = curl(f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/{path}", head=True)
            if code == "200":
                return "LIVE", f"raw:{path}"
    r = subprocess.run(["git", "ls-remote", "--heads", f"https://{forge}/{owner}/{repo}"],
                       capture_output=True, text=True, timeout=60,
                       env={"GIT_TERMINAL_PROMPT": "0", "PATH": "/usr/bin:/bin",
                            "HOME": "/root", "HTTPS_PROXY": __import__("os").environ.get("HTTPS_PROXY", "")})
    if r.returncode == 0 and r.stdout.strip():
        return "LIVE", "ls-remote"
    return "UNREACHABLE", "both-legs-failed"


def npm_search(term, size=25):
    body, code = curl("https://registry.npmjs.org/-/v1/search?text="
                      + urllib.parse.quote(term) + f"&size={size}")
    if code != "200" or not body:
        return None, code
    try:
        return json.loads(body), code
    except json.JSONDecodeError:
        return None, code


def npm_record(name):
    body, code = curl("https://registry.npmjs.org/" + urllib.parse.quote(name, safe="@/"))
    if code != "200" or not body:
        return None
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return None


def backlink_of(rec):
    """The declared repository back-link of a package's LATEST version."""
    if not rec:
        return None, None
    latest = (rec.get("dist-tags") or {}).get("latest")
    ver = (rec.get("versions") or {}).get(latest) or {}
    repo = ver.get("repository") or rec.get("repository")
    lic = ver.get("license") or rec.get("license")
    if isinstance(repo, dict):
        repo = repo.get("url")
    if isinstance(lic, dict):
        lic = lic.get("type")
    return repo, lic
