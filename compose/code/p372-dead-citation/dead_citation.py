#!/usr/bin/env python3
"""`p372-dead-citation` — the three questions `Gap 483` ran together.

🔴 `Gap 483` reads *"**46** addresses cited on these shelves answer `NO-REMOTE` — they do
not resolve at all."* 🟢 Re-derived at `p372` from a first-hand probe of all 46, **12 of
the 46 are not dead**: ten are not addresses at all and two are LIVE repositories that
hold no commits. The gap's own figure folds three different questions into one:

  1. **is the string an ADDRESS?**     — `classify_string`
  2. **does the address ANSWER?**      — `classify_liveness`
  3. **is a dead address being cited as a LIVE CLAIM, or as a recorded absence?**
                                        — `citation_is_a_live_claim`

🔵 Keeping them apart is the whole instrument. A negative control that does not resolve is
*working as designed*; a `repos/HKUDS` that does not resolve was never an address; an empty
repository that does not advertise refs is *alive*; and only the remainder is a defect.
"""
import re

#: 🔴 `p371`'s `D1` class, generalised. `D1` caught a RELATIVE path (`.../archive`).
#: `p372` found the same shape arriving a second way, and it is the more common one here:
#: a slug extractor matching INSIDE A URL PATH. `api.github.com/repos/HKUDS/DeepTutor`
#: yields `repos/HKUDS`; `api.github.com/repos/dodona-edu/dolos/git/trees/<sha>` yields
#: `repos/dodona-edu`. Four of `Gap 483`'s 46 are this one shape.
#: 🟢 `p283`'s ratchet caught this set on its first run as `SINGLE-SPELLING`, and it was
#: right to: a path vocabulary written in one casing is a hazard even when the comparison
#: happens to fold, because the fold sat FOUR lines away from the literal. The fold is now
#: AT the vocabulary, and it is `casefold()` rather than `lower()` — `lower()` is wrong for
#: a dotted Turkish `I`, and a GitHub owner may be any Unicode-adjacent spelling a URL carries.
_URL_PATH_SEGMENTS = {_s.casefold() for _s in (
    "repos", "orgs", "topics", "users", "search", "gists", "git",
    "trees", "blobs", "commits", "contents", "licenses", "rate_limit",
)}

#: Documentation placeholders. This base had ALREADY labelled `your-username/SafeTutors`
#: a "citation artefact, not a repository" (`agents/trending.md:26044`) and then counted it
#: as a dead address anyway — `p371`'s own "committed knowledge not wired in" failure mode.
_PLACEHOLDER_OWNERS = {
    "your-username", "your-org", "owner", "username", "user", "org",
    "yourname", "example", "my-org", "myorg", "<owner>", "ORG", "USER",
}

#: Slugs this base FABRICATED as negative controls for its own existence oracles. A
#: negative control that fails to resolve is the control PASSING. It is never a defect,
#: and it must never be retracted from the shelf that uses it.
_NEG_CONTROL_MARKERS = (
    "does-not-exist", "doesnotexist", "definitely-not-a-real-repo",
    "fake-repo", "nosuchrepo", "nope-nope-nope", "-zzz9", "zzz999",
    "xyz123",
)


def classify_string(s):
    """ADDRESS | URL-PATH-FRAGMENT | RELATIVE-PATH | PLACEHOLDER | NEG-CONTROL | MALFORMED."""
    if not s or s.count("/") != 1:
        return "MALFORMED"
    owner, repo = s.split("/")
    if not owner or not repo:
        return "MALFORMED"
    # 🔴 p371 D1: a GitHub owner cannot begin with a dot or contain `..`.
    if owner.startswith(".") or ".." in s:
        return "RELATIVE-PATH"
    low = s.lower()
    if any(m in low for m in _NEG_CONTROL_MARKERS):
        return "NEG-CONTROL"
    if owner.lower() in {p.lower() for p in _PLACEHOLDER_OWNERS}:
        return "PLACEHOLDER"
    # 🔴 the URL-path shape: the OWNER slot holds an API path segment.
    if owner.casefold() in _URL_PATH_SEGMENTS:
        return "URL-PATH-FRAGMENT"
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", owner):
        return "MALFORMED"
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", repo):
        return "MALFORMED"
    return "ADDRESS"


def classify_liveness(rc, stdout_bytes, stderr_text=""):
    """OK | EXISTS-EMPTY | ABSENT | PROXY-REFUSED | TRANSPORT-FAIL.

    🔴 **THE DEFECT THIS FUNCTION EXISTS TO PREVENT.** `p230` published
    `cdweaver1992/edfi-mcp-server` as `GONE` and `p371` published it as `NO-REMOTE`. It is
    LIVE: a repository with zero commits answers smart-HTTP with `rc=0` and an EMPTY ref
    advertisement, and `git clone` labels the class itself —
    *"warning: You appear to have cloned an empty repository."* 🔵 Any classifier that keys
    on "zero refs" folds a live repository into the absent bucket. `rc` comes first here,
    and `rc=0` can never return `ABSENT`.
    """
    err = (stderr_text or "").lower()
    if "connect tunnel failed" in err or "access denied" in err:
        return "PROXY-REFUSED"
    if rc == 0:
        # 🟢 rc=0 means the server ANSWERED. Zero bytes = a live, commitless repository.
        return "OK" if stdout_bytes > 0 else "EXISTS-EMPTY"
    if "authentication failed" in err or "repository not found" in err:
        return "ABSENT"
    return "TRANSPORT-FAIL"


#: Shelves on which a row is a LIVE RECOMMENDATION. A dead address here is a defect.
#: 🟢 Both tuples are CASEFOLDED at the point of definition, and the comparison folds too.
#: `p283`'s ratchet graded the first draft `SINGLE-SPELLING` for writing `README.md` in one
#: casing, and it was right to: this base's own `p191-licence-case-full-depth` and `p369`'s
#: rediscovered `LICENSE.TXT` are the same lesson on the licence family. A shelf filename is
#: a path, and a path read in one casing is a path that will be missed in another.
LIVE_SHELVES = tuple(_p.casefold() for _p in (
    "agents/top.md", "repos/foundations.md", "verticals/solutions.md",
))
#: Append-only histories and registers. A dead address here is a RECORD OF A MEASUREMENT,
#: 🟢 and rewriting it would destroy the trend the file exists to carry.
RECORD_FILES = tuple(_p.casefold() for _p in (
    "agents/trending.md", "repos/trending.md", "intel/open-gaps.md", "README.md",
))


def citation_is_a_live_claim(path):
    """True only where a row asserts the address is usable TODAY."""
    folded = path.casefold()
    return any(folded.endswith(s) for s in LIVE_SHELVES)
