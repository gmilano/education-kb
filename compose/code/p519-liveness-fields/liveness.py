"""`p519-liveness-fields` — which GitHub repository fields actually carry liveness.

🔴 The defect this exists for. `p518` retracted `microsoft/autogen` from three consecutive
education cycles because it was ARCHIVED while looking alive. `p519` found the same class in
LATAM-adjacent supply: `menthorlabs/menthor` (Apache-2.0, 582 stars) is archived, its last
`pushed_at` is 2024-04-21 — and its `updated_at` is 2026-10-12. A shelf built on `updated_at`
calls that repo live. `updated_at` moves when metadata moves (stars, topics, description), so it
is NOT a liveness signal. `archived` and `pushed_at` are.

🔵 No network. Pure functions over fields a caller already read, so this is runnable where
there is no egress (`Gap 511`'s lesson: a refusal of one channel is not a refusal of the check).
"""

ARCHIVED = "ARCHIVED"
LIVE = "LIVE"
STALE = "STALE"


def days_between(earlier, later):
    """Whole days between two YYYY-MM-DD strings. Neither is parsed as a date object so the
    instrument has no dependency and no locale behaviour."""
    from datetime import date

    def d(s):
        y, m, dd = (int(x) for x in s[:10].split("-"))
        return date(y, m, dd)

    return (d(later) - d(earlier)).days


def classify(archived, pushed_at, today, stale_after_days=365):
    """Grade one repository's liveness from the two fields that carry it.

    `archived` wins outright: an archived repository is not live however recent its push.
    Otherwise a push older than `stale_after_days` is STALE, and anything else is LIVE.
    🔴 `updated_at` is deliberately NOT a parameter — see `updated_at_is_not_liveness`.
    """
    if archived:
        return ARCHIVED
    age = days_between(pushed_at, today)
    if age < 0:
        raise ValueError("pushed_at %s is after today %s" % (pushed_at, today))
    return STALE if age > stale_after_days else LIVE


def updated_at_is_not_liveness(archived, pushed_at, updated_at, today,
                               stale_after_days=365):
    """Return True when grading on `updated_at` would DISAGREE with the sound grade.

    This is the measurement, not a helper: it names the rows where a shelf that trusted
    `updated_at` would have published a dead repository as live.
    """
    sound = classify(archived, pushed_at, today, stale_after_days)
    naive_age = days_between(updated_at, today)
    naive = STALE if naive_age > stale_after_days else LIVE
    return sound != naive


def permissive(spdx_id):
    """🔵 Permissive means a closed client derivative is permitted. ECL-2.0 is an Apache-2.0
    derivative and is included; `NOASSERTION` is NOT a licence and is never permissive."""
    return spdx_id in ("MIT", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause", "ECL-2.0",
                       "ISC", "Unlicense", "CC0-1.0")


def readable_grant(spdx_id):
    """🔴 `NOASSERTION` and an absent licence are UNREADABLE from a classifier alone. A pass
    that cannot read the served bytes must say so rather than grade the row either way."""
    return spdx_id not in ("NOASSERTION", "NONE", "", None)
