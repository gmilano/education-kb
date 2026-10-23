#!/usr/bin/env python3
"""Suite for `p406-carried-existence`. Prints its own total (`P126`'s rule, point 3).

🔵 **The obligatory controls of this suite are the ones where counting `CHANNEL-ERROR` as
decay would CHANGE the published rate.** A suite that only asserted "an absent address is
absent" would pass with the throttling defect fully in place, and that defect is the whole
reason this module is not a `for` loop around `p293`. `C12` is the mutation control: it
constructs the population where the two readings disagree and pins the disagreement.

No network. Every probe is injected via `probe_fn`; every fixture is authored here.

    python3 test_carried_existence.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carried_existence import (INCONCLUSIVE, RESOLVED, SHELF_FILES,  # noqa: E402
                               UNRESOLVED, decay_rate, head_collisions,
                               population, repo_root, sweep)
from slug_oracle import VERDICTS  # noqa: E402

n = ok = 0


def check(label, got, want):
    global n, ok
    n += 1
    if got == want:
        ok += 1
        return
    print("  🔴 %s\n     got  %r\n     want %r" % (label, got, want))


# ── the fake channel ──────────────────────────────────────────────────────────────────
# Keyed on the URL so a fixture can make the SAME address answer differently on a retry,
# which is the only way to exercise the retry arm offline.
class Channel:
    def __init__(self, script):
        # A value is either one (text, rc) answer or a LIST of them to serve in order.
        # Normalising here is load-bearing: `list(("text", 0))` flattens the pair.
        self.script = {}
        for k, v in script.items():
            self.script[k] = list(v) if isinstance(v, list) else [v]
        self.calls = []

    def __call__(self, url):
        self.calls.append(url)
        q = self.script.get(url)
        if not q:
            return ("fatal: could not read Username for 'https://github.com'", 128)
        return q.pop(0) if len(q) > 1 else q[0]


# The real channel is `git ls-remote --symref <url> HEAD`, so its body carries a symref
# line and a sha line whose ref name is exactly `HEAD`.  A fixture that wrote
# `refs/heads/main` instead would pass every verdict control and still not exercise
# `head_sha`, which is how a collision arm gets shipped untested.
REFS = ("ref: refs/heads/main\tHEAD\n"
        "1111111111111111111111111111111111111111\tHEAD\n", 0)
REFS2 = ("ref: refs/heads/main\tHEAD\n"
         "2222222222222222222222222222222222222222\tHEAD\n", 0)
ABSENT = ("fatal: could not read Username for 'https://github.com'", 128)
THROTTLED = ("fatal: unable to access 'x': Too many concurrent requests", 128)
EMPTY = ("", 0)


# ── C1-C4: the decay rate's two sides ─────────────────────────────────────────────────
print("C1-C4  decay_rate: what is on each side")
check("C1 plain 1-absent-in-4",
      decay_rate(["EXISTS-PUBLIC"] * 3 + ["ABSENT-OR-PRIVATE"]), (3, 1, 0, 25.0))
check("C2 EXISTS-NO-REFS counts as RESOLVED (an empty repo EXISTS)",
      decay_rate(["EXISTS-NO-REFS", "ABSENT-OR-PRIVATE"]), (1, 1, 0, 50.0))
# 🔴 The defect this module exists not to commit: the inconclusive row is on NEITHER side.
check("C3 CHANNEL-ERROR is excluded from numerator AND denominator",
      decay_rate(["EXISTS-PUBLIC", "ABSENT-OR-PRIVATE", "CHANNEL-ERROR"]), (1, 1, 1, 50.0))
check("C4 MALFORMED likewise",
      decay_rate(["EXISTS-PUBLIC", "ABSENT-OR-PRIVATE", "MALFORMED"]), (1, 1, 1, 50.0))

# ── C5-C6: the rate must refuse to exist rather than read 0% ──────────────────────────
print("C5-C6  an ungraded population has NO rate")
check("C5 all-inconclusive -> rate is None, NOT 0.0",
      decay_rate(["CHANNEL-ERROR", "MALFORMED"]), (0, 0, 2, None))
check("C6 the empty population -> None", decay_rate([]), (0, 0, 0, None))

# ── C7: the token bound, re-asserted at the CENSUS layer ──────────────────────────────
# p293's C9 forbids a bare `ABSENT` in the oracle's vocabulary.  A census is where the
# token gets rounded off in prose, so the bound is pinned again here.
print("C7     p293's C9', at this layer")
check("C7a bare ABSENT is not a verdict", "ABSENT" in VERDICTS, False)
check("C7b the unresolved side is exactly the undecidable token",
      sorted(UNRESOLVED), ["ABSENT-OR-PRIVATE"])
# 🟡 And the bound this pass MEASURED: `apereo/opencast` is neither absent nor private, it
# MOVED, and this channel cannot say so.  No `MOVED` token may be invented from a sweep.
check("C7c MOVED is not in the vocabulary either", "MOVED" in VERDICTS, False)
check("C7d the three sides partition the vocabulary",
      sorted(RESOLVED | UNRESOLVED | INCONCLUSIVE), sorted(VERDICTS))

# ── C8-C11: the sweep, the cache and the retry ────────────────────────────────────────
print("C8-C11 sweep / cache / retry")
ch = Channel({"https://github.com/a/live": REFS, "https://github.com/a/dead": ABSENT})
res = sweep(["a/live", "a/dead"], workers=2, probe_fn=ch, retry=False)
check("C8a live verdict", res["a/live"][0], "EXISTS-PUBLIC")
check("C8b dead verdict", res["a/dead"][0], "ABSENT-OR-PRIVATE")
check("C8c head sha captured", res["a/live"][1], "1" * 40)

ch2 = Channel({"https://github.com/a/live": REFS})
res2 = sweep(["a/live"], workers=1, probe_fn=ch2, cache={"a/live": ("EXISTS-PUBLIC", "x", "cached")},
             retry=False)
check("C9 a cached address is NOT re-probed", ch2.calls, [])

# The retry arm: the SAME address answers THROTTLED then REFS.  A sweep without the retry
# publishes a CHANNEL-ERROR; with it, the row is graded.
ch3 = Channel({"https://github.com/a/flaky": [THROTTLED, REFS]})
res3 = sweep(["a/flaky"], workers=1, probe_fn=ch3, retry=True)
check("C10a a throttled row is re-probed serially and graded", res3["a/flaky"][0], "EXISTS-PUBLIC")
check("C10b the retry is recorded in the detail",
      "serial retry after CHANNEL-ERROR" in res3["a/flaky"][2], True)

ch4 = Channel({"https://github.com/a/live": REFS})
res4 = sweep(["a/live"], workers=1, probe_fn=ch4, retry=True)
check("C11 a GRADED row is not re-probed by the retry arm", len(ch4.calls), 1)

# ── C12: THE MUTATION CONTROL ─────────────────────────────────────────────────────────
# 🔴 The population where the two readings disagree.  Under 12 workers a sweep throttles;
# if `CHANNEL-ERROR` were counted as unresolvable, the SAME shelves would publish a decay
# rate that climbs with the worker count.  This control pins the number that must not move.
print("C12    the defect, constructed")
pop = ["EXISTS-PUBLIC"] * 90 + ["ABSENT-OR-PRIVATE"] * 10 + ["CHANNEL-ERROR"] * 100
_r, _u, _i, rate_correct = decay_rate(pop)
rate_if_counted = 100.0 * (10 + 100) / len(pop)          # the defect's answer
rate_if_resolved = 100.0 * 10 / len(pop)                 # the opposite defect's answer
check("C12a the published rate is over the graded half only", round(rate_correct, 2), 10.0)
check("C12b counting inconclusive as decay would say 55%", round(rate_if_counted, 2), 55.0)
check("C12c counting it as live would say 5%", round(rate_if_resolved, 2), 5.0)
check("C12d so the three readings genuinely differ",
      len({round(rate_correct, 2), round(rate_if_counted, 2), round(rate_if_resolved, 2)}), 3)

# ── C13-C15: HEAD collisions are a FINDING, not a verdict (p283) ───────────────────────
print("C13-C15 head collisions")
rows = {"a/one": ("EXISTS-PUBLIC", "1" * 40, ""), "a/two": ("EXISTS-PUBLIC", "1" * 40, ""),
        "a/three": ("EXISTS-PUBLIC", "2" * 40, "")}
check("C13 two names at one HEAD collide", head_collisions(rows), {"1" * 40: ["a/one", "a/two"]})
check("C14 a lone sha is not a collision",
      "2" * 40 in head_collisions(rows), False)
rows2 = {"a/x": ("ABSENT-OR-PRIVATE", "-", ""), "a/y": ("ABSENT-OR-PRIVATE", "-", "")}
check("C15 absent rows share the sentinel '-' and must NOT collide", head_collisions(rows2), {})

# ── C16-C18: the population is p351's, and the root is found from anywhere ────────────
print("C16-C18 population and cwd-portability")
root = repo_root()
check("C16 the root holds every shelf",
      all(os.path.exists(os.path.join(root, p)) for p in SHELF_FILES), True)
pop_live = population(root)
check("C17 the population is non-empty", len(pop_live) > 1000, True)
# p351's rejection arm is load-bearing: a navigation path is not an address, so a sweep
# must never probe `topics/ai-tutor` and record it as decay.
check("C18a a nav namespace is not in the population", "topics/ai-tutor" in pop_live, False)
check("C18b nor an ellided owner", ".../blob" in pop_live, False)
check("C18c every address names at least one shelf",
      all(v for v in pop_live.values()), True)

print("\n%d/%d controls pass" % (ok, n))
sys.exit(0 if ok == n else 1)
