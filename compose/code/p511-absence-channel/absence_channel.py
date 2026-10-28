"""p511-absence-channel — what each probe on this channel may and may not assert.

Written because `p510` prescribed two instruments and generalised one of them too far:

    "git ls-remote --symref for liveness, raw.githubusercontent.com for payloads
     (200 live / 404 absent)"

The `404 absent` half is false on this channel and the counter-population was already
enumerated by `p509` (`T34`: 18 shelf addresses carry no grant at all). Measured p511:

    eth-lre/mathtutorbench      ls-remote REF_OK   raw HEAD/LICENSE 404
    h9-tect/AI-Roadmaps         ls-remote REF_OK   raw HEAD/LICENSE 404
    zzzz-nonexistent-org-9931/  AUTH_PROMPT        raw HEAD/LICENSE 404   <- never existed

Three live repositories and one that never existed answer the prescribed probe with the
same byte, so the probe is undefined on the population p509 already listed.

This module therefore makes the refusal structural: `classify()` can return LIVE, can
return UNREADABLE_ABSENT_OR_PRIVATE, and has no code path that returns ABSENT.
`liveness_from_raw()` raises rather than answer at all.
"""

LIVE = "LIVE"
UNREADABLE = "UNREADABLE_ABSENT_OR_PRIVATE"
UNKNOWN = "UNKNOWN_NO_USABLE_OBSERVATION"

# Observation vocabulary, one value per channel.
LS_REF_OK = "REF_OK"            # a `ref: refs/heads/<x>\tHEAD` line came back
LS_AUTH_PROMPT = "AUTH_PROMPT"  # credential prompt: absent OR private-and-unreadable
MCP_ROW = "ROW_RETURNED"
MCP_NO_ROW = "NO_ROW"           # silent per-repository exclusion is indistinguishable from absence


class ControlFailure(RuntimeError):
    """Raised instead of returning a verdict when the instrument cannot discriminate."""


class UnsoundProbe(RuntimeError):
    """Raised when a caller asks a payload channel for a liveness verdict."""


def liveness_from_raw(status_code):
    """raw.githubusercontent.com is a PAYLOAD channel. 200 implies live; 404 implies nothing.

    A 404 conflates: repository absent, ref unresolvable, and path simply not present in a
    live public repository. oppia/oppia is live, public and 404s on README.md at two refs
    while serving LICENSE 200, so there is no path whose absence is informative.
    """
    if status_code == 200:
        return LIVE
    raise UnsoundProbe(
        "raw %s is not evidence about the repository; use the git channel for liveness"
        % status_code
    )


def classify(ls_remote, mcp=None):
    """Return LIVE / UNREADABLE / UNKNOWN. Never returns ABSENT, by construction."""
    if ls_remote == LS_REF_OK:
        return LIVE
    if mcp == MCP_ROW:
        return LIVE
    if ls_remote == LS_AUTH_PROMPT:
        # Both a never-existed repository and a private one land here. A private repository
        # inside this session's scope answers REF_OK because the proxy injects credentials,
        # so this bucket cannot be narrowed from here either.
        return UNREADABLE
    return UNKNOWN


CONTROLS = [
    # (name, ls_remote, mcp, expected)
    ("known_good_public", LS_REF_OK, MCP_ROW, LIVE),
    ("known_good_public_no_grant", LS_REF_OK, MCP_NO_ROW, LIVE),
    ("known_private_in_scope", LS_REF_OK, None, LIVE),
    ("known_bad_never_existed", LS_AUTH_PROMPT, MCP_NO_ROW, UNREADABLE),
    ("live_but_silently_excluded", LS_REF_OK, MCP_NO_ROW, LIVE),
    ("no_observation", None, None, UNKNOWN),
]


def run_controls():
    """Both a known-good and a known-bad input must grade correctly, per Gap 509-B."""
    for name, ls, mcp, expected in CONTROLS:
        got = classify(ls, mcp)
        if got != expected:
            raise ControlFailure("control %s: expected %s, got %s" % (name, expected, got))
    # and the payload channel must refuse rather than answer
    try:
        liveness_from_raw(404)
    except UnsoundProbe:
        pass
    else:
        raise ControlFailure("liveness_from_raw(404) answered instead of refusing")
    if liveness_from_raw(200) != LIVE:
        raise ControlFailure("liveness_from_raw(200) did not grade LIVE")
    return len(CONTROLS) + 2


def sweep(observations):
    """observations: {slug: (ls_remote, mcp)}. Runs controls first or returns nothing."""
    run_controls()
    return {slug: classify(ls, mcp) for slug, (ls, mcp) in observations.items()}
