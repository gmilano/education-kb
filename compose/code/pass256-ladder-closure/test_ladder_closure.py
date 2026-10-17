#!/usr/bin/env python3
"""Suite for `pass256-ladder-closure`.

Explicit pass/fail accounting and an explicit `sys.exit`, NOT `unittest.main()` — that is
`ACTION XR`'s silent-zero mode, and this base has 71 suites pinned as carrying it.  Proven
able to fail before entering the gate: `closure_gaps` is run against the PRE-p256 ladder as
a fixture, and must name the two paths that cost p256 two false verdicts.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ladder_closure as L  # noqa: E402

t = p = 0
def chk(name, want, got):
    global t, p
    t += 1
    if want == got:
        p += 1
    else:
        print(f"FAIL {name}: want={want!r} got={got!r}")

def ok(name, cond):
    chk(name, True, bool(cond))

# --- 1. the JOIN, on the live artefacts ------------------------------------------------
live_ladder = L.tier_a()
live_proven = L.proven_root_forms()
ok("the ladder parses to a non-empty TIER_A", len(live_ladder) >= 23)
ok("the suite parses to a non-empty proven set", len(live_proven) >= 10)
chk("closure holds on the live artefacts", [], L.closure_gaps(live_ladder, live_proven))

# --- 2. the FALSIFIER: the pre-p256 ladder must fail the same control -------------------
PRE_P256_TIER_A = ("LICENSE-CODE LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.txt COPYING "
                   "COPYING.txt COPYING.md COPYING.LESSER license.txt license.md License.txt "
                   "copying.txt LICENSE.rst NOTICE").split()
chk("the pre-p256 ladder had 16 root names", 16, len(PRE_P256_TIER_A))
pre_gaps = L.closure_gaps(PRE_P256_TIER_A, live_proven)
ok("the control FAILS against the pre-p256 ladder", len(pre_gaps) > 0)
ok("and it names LICENSE.TXT — P1057's own path, absent for 67 passes",
   "LICENSE.TXT" in pre_gaps)
ok("and it names MIT-LICENSE — openstax/fine_print's real grant path",
   "MIT-LICENSE" in pre_gaps)
# An EMPTY ladder may never grade as closure: `p146`/`p542`'s empty-input floor.
ok("an empty ladder does not grade as closure", len(L.closure_gaps([], live_proven)) > 0)
chk("an empty proven set is refused by the floor above, not by closure",
    [], L.closure_gaps(live_ladder, []))

# --- 3. the exemption is an exact SET, so it cannot quietly grow ------------------------
chk("exactly one named exemption", ["third-party-licenses.txt"], sorted(L.LADDER_EXEMPT))
ok("and it carries its reason", len(L.LADDER_EXEMPT["third-party-licenses.txt"]) > 40)

# --- 4. AGREEMENT: every TIER_A entry satisfies the shared predicate --------------------
PRED = os.path.join(HERE, "..", "lib", "licence_path.sh")
def is_licence_path(path):
    r = subprocess.run(["bash", "-c",
                        f'. "{PRED}"; is_licence_path "$1" && echo YES || echo NO', "_", path],
                       capture_output=True, text=True)
    return r.stdout.strip() == "YES"

disagree = [a for a in live_ladder if not is_licence_path(a)]
chk("no TIER_A entry is rejected by is_licence_path", [], disagree)

# --- 5. CASE: two addresses, not two spellings of one ----------------------------------
ok("LICENSE.txt is in the ladder", "LICENSE.txt" in live_ladder)
ok("LICENSE.TXT is in the ladder", "LICENSE.TXT" in live_ladder)
chk("they are distinct entries", 2, len({"LICENSE.txt", "LICENSE.TXT"} & set(live_ladder)))
for added in L.P256_ADDED:
    ok(f"p256's addition survives: {added}", added in live_ladder)

# --- 6. REFUSAL: a captured 404 body is not a grant ------------------------------------
ok("the 404 body grades as a refusal", L.is_refusal(b"404: Not Found"))
ok("...as str too", L.is_refusal("404: Not Found"))
ok("...and with a trailing newline", L.is_refusal(b"404: Not Found\n"))
ok("an MIT body does not", not L.is_refusal(b"MIT License\n\nCopyright (c) 2016"))
ok("a DIFFERENT 14-byte body does not", not L.is_refusal(b"MIT License\n\n\n"))
ok("None does not", not L.is_refusal(None))
chk("the refusal is 14 bytes", 14, L.REFUSAL_BYTES)
chk("the refusal body hashes to the pinned value", "d5558cd419c8d46b", L.REFUSAL_SHA16)
ok("no pinned payload is the refusal size",
   all(b != L.REFUSAL_BYTES for _, b, _ in L.PINNED_PAYLOADS.values()))

# --- 7. the pinned payloads, and the ONE legitimate twin -------------------------------
by_sha = {}
for slug, (_path, nbytes, sha) in L.PINNED_PAYLOADS.items():
    by_sha.setdefault((nbytes, sha), []).append(slug)
twins = {k: sorted(v) for k, v in by_sha.items() if len(v) > 1}
chk("exactly one twin pair among the pinned payloads",
    {(11358, "cfc7749b96f63bd3"): ["openedx/edx-lint", "openedx/xblock-sdk"]}, twins)
chk("and the twins differ in PATH CASE, which is the whole point",
    ("LICENSE.TXT", "LICENSE.txt"),
    (L.PINNED_PAYLOADS["openedx/xblock-sdk"][0], L.PINNED_PAYLOADS["openedx/edx-lint"][0]))

# --- 8. ACTION XW: the MIT band, re-measured against payloads --------------------------
# p253 closed the band at 1 056-1 085 with its HIGH end resting on a single 1 111 B figure.
# p256 read four more MIT bodies first-hand; THREE sit above 1 085 and one sits BELOW 1 056.
mit = {s: b for s, (_p, b, _h) in L.PINNED_PAYLOADS.items() if b < 2000}
chk("four MIT bodies measured this pass", 4, len(mit))
chk("the low end moves down to openstax/fine_print", 1055, min(mit.values()))
chk("the high end moves up to 1EdTech/cert-schema", 1096, max(mit.values()))
ok("three of the four sit ABOVE p253's 1 085 high end",
   sum(1 for b in mit.values() if b > 1085) == 3)
ok("and one sits BELOW p253's 1 056 low end",
   sum(1 for b in mit.values() if b < 1056) == 1)

print(f"{p}/{t}")
sys.exit(0 if p == t else 1)
