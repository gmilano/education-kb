#!/usr/bin/env python3
"""p255 — ACTION YE: the channel map as an INFERENCE RULE, not a network snapshot.

`ACTION YE` (p254) asked for the `(channel x transport)` table to become "a standing
instrument that a pass RUNS rather than retypes". A table of statuses cannot be standing:
it is stale the moment the hour rolls over. What IS standing is the rule a pass applies to
a status — and that rule is exactly what p254 got wrong.

p254 retracted the sixteen-pass `403` wall and replaced it, in the same pass, with:

    "Treat a 403 from this channel as *budget exhausted* until `rate_limit` says otherwise."

p255 measured the stated condition. `rate_limit` DID say otherwise — `core` `limit 60`,
`remaining 51`, `used 9` — while four `/repos/{slug}` requests on that same transport, in
that same minute, returned `403` and consumed none of it. A denial that does not bill is
not a budget.

So the discriminator is not the host and not the transport. It is whether anything on the
same host and transport was answered in the same window, and what the meter says. This
module is that discriminator, and it is OFFLINE: it grades a tuple a pass has already
measured, so it belongs in `make hooks` where there is no egress.

Verdicts
--------
OPEN              the channel answered
BUDGET-EXHAUSTED  refused AND the meter is empty
POLICY-DENIED     refused WHILE the meter has credit, or while a sibling endpoint on the
                  same (host, transport) answered -- the refusal is categorical
INDETERMINATE     refused and nothing discriminates.  p254 had exactly this and published
                  BUDGET-EXHAUSTED from it; naming the state is the whole point
"""

OPEN = "OPEN"
BUDGET_EXHAUSTED = "BUDGET-EXHAUSTED"
POLICY_DENIED = "POLICY-DENIED"
INDETERMINATE = "INDETERMINATE"

# A refusal.  000 is the proxy's own CONNECT failure, which never reaches the origin and so
# can never be a budget; 401/403/429 are origin-shaped refusals.
REFUSALS = (000, 401, 403, 429)

_UNSET = object()


def classify(status, budget_remaining=_UNSET, sibling_answered=_UNSET):
    """Grade one (endpoint, transport) measurement.

    status            int HTTP status, or 0 for a transport-layer refusal
    budget_remaining  int from the meter, or _UNSET when the pass did not read it
    sibling_answered  True when another endpoint on the SAME host and SAME transport
                      answered 200 in the same window, or _UNSET when unknown

    `budget_remaining` is deliberately `_UNSET`-defaulted rather than `None`-defaulted:
    p253 paid for a default that doubled as a sentinel, and "the pass did not read the
    meter" is a different fact from "the meter read zero".
    """
    if status == 0:
        # Never reached the origin.  A gateway or DNS refusal is categorical by
        # construction -- there is no bucket at the far end to have emptied.
        return POLICY_DENIED
    if status not in REFUSALS:
        return OPEN if 200 <= status < 400 else INDETERMINATE

    if budget_remaining is not _UNSET and budget_remaining is not None:
        if budget_remaining > 0:
            # The meter has credit and the request was still refused.  This is p255's
            # measurement and it is the one p254's rule cannot express.
            return POLICY_DENIED
        return BUDGET_EXHAUSTED

    if sibling_answered is True:
        # Same host, same transport, same window, answered.  A host-wide budget cannot be
        # empty for one path and full for another.
        return POLICY_DENIED
    return INDETERMINATE


def is_retryable_later(verdict):
    """Only an exhausted budget comes back on its own.  A POLICY-DENIED channel needs the
    egress or the scope to change, so a pass that keeps re-probing it is burning budget on
    a conclusion it already has -- and a pass that records it as a BUDGET is the mistake
    that cost sixteen passes."""
    return verdict == BUDGET_EXHAUSTED


def unsound_budget_claim(status, budget_remaining=_UNSET, sibling_answered=_UNSET):
    """TRUE when a pass would be asserting BUDGET-EXHAUSTED without the evidence for it.

    This is the falsifier limb `ACTION YE` needs: p254's published row must trip it, and a
    genuine exhaustion must not.
    """
    return classify(status, budget_remaining, sibling_answered) in (
        POLICY_DENIED,
        INDETERMINATE,
    )
