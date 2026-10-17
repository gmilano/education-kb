#!/usr/bin/env python3
"""Controls for `ACTION YE`'s discriminator.

The control that matters is the ADVERSARIAL one: p254's own published row must NOT grade
as `BUDGET-EXHAUSTED`, because p254 published exactly that from a tuple that could not
support it. If this suite ever blesses that row, the instrument has inherited the defect
it was built to catch.

Every row of `measured.2026-10-16-p255.tsv` is replayed through the rule, so the pinned
table and the rule cannot drift apart.
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import channel_map as cm  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PINS = os.path.join(HERE, "measured.2026-10-16-p255.tsv")

FAILS = 0
RUN = 0


def check(name, got, want):
    global FAILS, RUN
    RUN += 1
    if got != want:
        print(f"FAIL {name}\n  got:  {got!r}\n  want: {want!r}")
        FAILS += 1


# ---------------------------------------------------------------- the rule itself
check("200 is OPEN", cm.classify(200), cm.OPEN)
check("204 is OPEN", cm.classify(204), cm.OPEN)
check("404 is not a refusal", cm.classify(404), cm.INDETERMINATE)

# 🔴 p255's measurement, and the one p254's rule cannot express.
check("403 with credit is POLICY-DENIED", cm.classify(403, 51), cm.POLICY_DENIED)
check("403 with a full meter", cm.classify(403, 14996), cm.POLICY_DENIED)
check("429 with credit", cm.classify(429, 51), cm.POLICY_DENIED)

# A genuine exhaustion must still be reachable, or the rule has merely inverted the error.
check("403 at zero is BUDGET-EXHAUSTED", cm.classify(403, 0), cm.BUDGET_EXHAUSTED)
check("429 at zero is BUDGET-EXHAUSTED", cm.classify(429, 0), cm.BUDGET_EXHAUSTED)

# The state p254 was actually in, named rather than guessed.
check("403, meter unread", cm.classify(403), cm.INDETERMINATE)
check("403, meter None", cm.classify(403, None), cm.INDETERMINATE)

# The sibling discriminator: a host-wide bucket cannot be empty for one path and full for
# another in the same window.
check("403 beside a 200 sibling", cm.classify(403, sibling_answered=True), cm.POLICY_DENIED)
check("403, sibling unknown", cm.classify(403, sibling_answered=cm._UNSET), cm.INDETERMINATE)

# A CONNECT-layer refusal never reaches the origin, so it can never be a budget.
check("status 0 is categorical", cm.classify(0), cm.POLICY_DENIED)
check("status 0 outranks an empty meter", cm.classify(0, 0), cm.POLICY_DENIED)

# ---------------------------------------------------------------- the falsifier
# 🔴 THE ADVERSARIAL CONTROL.  p254 published, for api.github.com/repos/{slug} on WebFetch:
#     "200 then 403 — LIVE until the 60/h unauthenticated budget is spent"
# It had no meter reading at the moment of the 403.  The rule must refuse to call that a
# budget, and must flag the claim as unsound.
check(
    "p254's published row grades INDETERMINATE, not BUDGET-EXHAUSTED",
    cm.classify(403),
    cm.INDETERMINATE,
)
check("p254's claim is unsound", cm.unsound_budget_claim(403), True)
check("p255's measurement is also not a budget", cm.unsound_budget_claim(403, 51), True)
check("a real exhaustion is a sound budget claim", cm.unsound_budget_claim(403, 0), False)

# Only an exhausted budget comes back on its own.
check("exhausted is retryable", cm.is_retryable_later(cm.BUDGET_EXHAUSTED), True)
check("policy-denied is NOT retryable", cm.is_retryable_later(cm.POLICY_DENIED), False)
check("indeterminate is NOT retryable", cm.is_retryable_later(cm.INDETERMINATE), False)
check("open is NOT retryable", cm.is_retryable_later(cm.OPEN), False)

# ---------------------------------------------------------------- the pinned table
def _opt(cell):
    return cm._UNSET if cell.strip().upper() in ("", "UNKNOWN") else int(cell)


def _sib(cell):
    c = cell.strip().upper()
    return True if c == "TRUE" else (False if c == "FALSE" else cm._UNSET)


with open(PINS, encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh, delimiter="\t"))

check("the pin file is present and non-trivial", len(rows) >= 20, True)

for row in rows:
    got = cm.classify(int(row["status"]), _opt(row["budget_remaining"]), _sib(row["sibling_answered"]))
    check(f"pinned: {row['endpoint']} via {row['transport']}", got, row["verdict"])

# The two mechanisms are BOTH present in the pinned table, or it is not a discriminating
# measurement -- it is a list of one outcome.
verdicts = {r["verdict"] for r in rows}
check("the table exhibits OPEN", cm.OPEN in verdicts, True)
check("the table exhibits POLICY-DENIED", cm.POLICY_DENIED in verdicts, True)

# 🔴 And the finding this pass exists to pin: ONE host, ONE transport, two verdicts.
webfetch = [r for r in rows if r["transport"] == "WebFetch" and r["endpoint"].startswith("api.github.com")]
check("WebFetch answers api.github.com", any(r["verdict"] == cm.OPEN for r in webfetch), True)
check("WebFetch is refused by api.github.com", any(r["verdict"] == cm.POLICY_DENIED for r in webfetch), True)

print(f"{RUN} controls, {FAILS} failure(s)")
sys.exit(1 if FAILS else 0)
