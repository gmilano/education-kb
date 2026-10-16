#!/usr/bin/env python3
"""p233 — the response classifier this pass was built on, extracted so no later pass has to
re-learn it.

TWO FINDINGS, one per direction, and they are mirror images:

  p232: a `200` IS NOT A READ.      PyPI's search endpoint answers 200 with a
                                    "Client Challenge" body and zero results markup.
  p233: a `404` IS NOT AN ABSENCE.  repo1.maven.org answers 404 with a ONE-BYTE body when it
                                    is throttling. Measured: 200, 404 and 429 from the SAME
                                    url inside one minute.

A probe that keys on the status code alone publishes a measured absence that is really a rate
limit, or a measured presence that is really a bot wall. Both have happened on these shelves.

This module is offline and pure: it classifies a (status, body, control_passed) triple. It
imports nothing but the standard library so it runs from any working directory, which is
`p355-cwd-portability`'s lesson from p229.
"""

# A body at or under this size cannot carry a directory listing or a useful payload. The
# throttle-404 measured this pass was exactly 1 byte; Maven's own 429 body is 96.
#
# p237: this is now also the THROTTLE SIGNATURE threshold. Measured on repo1.maven.org in one
# window -- real miss = 554 bytes of nginx `404 Not Found`, throttled = 1 byte, rate-limited
# = 96 bytes of "Your ip has exceeded...". Three distinguishable states, and only the middle
# one was modelled before.
EMPTY_BODY_MAX = 8

# The 554-byte nginx document p237 measured, kept as the size of a KNOWN REAL miss so a later
# pass does not have to re-measure it to know that a real 404 on this channel is not empty.
REAL_MISS_BYTES_MEASURED = 554

PRESENT = "PRESENT"
NOT_ESTABLISHED = "NOT-ESTABLISHED"
ABSENT = "ABSENT"
THROTTLED = "THROTTLED"
CHALLENGED = "CHALLENGED"


def classify(status, body, expect_token=None, control_passed=False):
    """Classify one probe response.

    status        int HTTP status, or 0 for a transport failure.
    body          the response body as text (may be empty).
    expect_token  a substring whose presence PROVES the payload is the real thing.
    control_passed  True only if a KNOWN POSITIVE succeeded in the SAME window.

    ABSENT is returned ONLY when a real negative is distinguishable from a throttle, which
    requires a control that passed in the same window. Otherwise the honest answer is
    NOT-ESTABLISHED. These are different claims and this KB has conflated them before.
    """
    body = body or ""

    # transport never completed — says nothing about the resource
    if status == 0:
        return NOT_ESTABLISHED

    # explicit rate limiting
    if status == 429:
        return THROTTLED

    if status == 200:
        # p232: a 200 with no payload token is a challenge page or an empty shell, not a read
        if expect_token is not None and expect_token not in body:
            return CHALLENGED
        if len(body) <= EMPTY_BODY_MAX:
            return CHALLENGED
        return PRESENT

    if status == 404:
        # p233: a 404 with an empty body is indistinguishable from a throttle.
        #
        # p237 measured the thing p233 could only infer, and it CORRECTS p233's handling.
        # The SAME url -- the negative control `org/zzz-not-a-group-9f8e7d/` -- returned a
        # 554-byte nginx `404 Not Found` document and, minutes later, a ONE-BYTE 404. So the
        # one-byte body is not "a 404 that happens to be empty": it is the throttle's OWN
        # SIGNATURE, and a real miss on this channel is a 554-byte document.
        #
        # 🔴 Therefore a passing control must NOT promote a signature-shaped 404 to ABSENT,
        # which is what this branch used to do. A control proves the channel answered SOME
        # url in the window; it cannot turn a throttle signature into an absence.
        if len(body) <= EMPTY_BODY_MAX:
            return THROTTLED
        # A 404 carrying a real error document (the 554-byte nginx page, GCS's
        # `<Code>NoSuchKey</Code>`) is a genuine miss -- but only from a channel that is
        # demonstrably answering. p237's 554-byte real 404 arrived in a window whose positive
        # control had just returned 429, so even THAT reading could not be published as an
        # absence. Without a control in the same window the honest verdict is
        # NOT-ESTABLISHED, not ABSENT.
        return ABSENT if control_passed else NOT_ESTABLISHED

    # every other status: the channel answered something we did not model
    return NOT_ESTABLISHED
