#!/usr/bin/env python3
"""`P798` -- a refusal is attributed to the layer that LOGGED it, not inferred from a 000.

Sixty-fifth pass, 2026-10-08. Single file ON PURPOSE: this tree's 44 other
suites import a sibling module at top level, which `python3 -I` cannot resolve
because `-I` implies `-P` and drops the script's directory from `sys.path[0]`.
A self-contained suite runs under BOTH `python3` and `python3 -I`, which is the
only mode this session is permitted to execute. See README.

    python3 test_ledger.py
    python3 -I test_ledger.py      # same result; this is the point

WHAT IT GUARDS.  `P797` (pass 64) said: write `EGRESS_DENIED (allowlist)`,
never `000` against a hostname.  That was right and it was an INFERENCE -- it
rested on Wikipedia-as-control (a host nobody believes is down) returning the
same error as four policy hosts.  This pass the refusing layer testifies in its
own words: the agent proxy's `recentRelayFailures` ledger names the host, the
timestamp and the mechanism (`gateway answered 403 to CONNECT`).  So the
verdict stops being an inference about a pattern and becomes a reading of a
first-party record.

THE TRAP THIS CLOSES, and it is the reason the file exists: `curl` reports
`000` for a proxy CONNECT denial and `000` for a genuinely unreachable host.
A sweep that writes the transport code publishes those two as the same fact.
They are not the same fact and they license opposite next actions.
"""
import json
import unittest

# The ledger as this pass read it, verbatim from `$HTTPS_PROXY/__agentproxy/status`
# on 2026-10-08. Four hosts, four denials, one minute.
LEDGER = json.loads("""
{"recentRelayFailures": [
 {"ts":"2026-10-08T19:52:02.128Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"en.wikipedia.org:443"},
 {"ts":"2026-10-08T19:52:02.419Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"digital-strategy.ec.europa.eu:443"},
 {"ts":"2026-10-08T19:52:02.679Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"www.iesalc.unesco.org:443"},
 {"ts":"2026-10-08T19:52:03.014Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"www.multistate.us:443"}],
 "noProxy":"localhost,127.0.0.1,registry.npmjs.org,jsr.io,pypi.org,files.pythonhosted.org,index.crates.io,proxy.golang.org"}
""")

# What curl reported for the same four hosts, same minute.
CURL = {"en.wikipedia.org": "000", "digital-strategy.ec.europa.eu": "000",
        "www.iesalc.unesco.org": "000", "www.multistate.us": "000"}

EGRESS_DENIED = "EGRESS_DENIED (allowlist)"
UNDETERMINED = "UNDETERMINED (transport)"


def refused_hosts(ledger):
    """Hostnames the proxy's own ledger records as CONNECT-rejected."""
    return {e["host"].rsplit(":", 1)[0]
            for e in ledger.get("recentRelayFailures", [])
            if e.get("kind") == "connect_rejected"}


def verdict(host, transport_code, ledger):
    """`P798`: the ledger decides. Transport code alone never does.

    A `000` with a matching ledger entry is a POLICY denial -- terminal here,
    and it says nothing against the source.  A `000` with no ledger entry is
    UNDETERMINED: it may be the host, the DNS, or a refusal that did not get
    logged.  Writing the second as the first is the defect `P797` named.
    """
    if host in refused_hosts(ledger):
        return EGRESS_DENIED
    if transport_code == "000":
        return UNDETERMINED
    return transport_code


def bypasses_proxy(host, ledger):
    """True when the host is in `noProxy` -- so it is NOT on the proxy's path."""
    entries = [h.strip() for h in ledger.get("noProxy", "").split(",") if h.strip()]
    return host in entries


class AttributionNamesTheLayer(unittest.TestCase):
    def test_the_four_denials_are_attributed_to_the_proxy(self):
        for host in CURL:
            self.assertEqual(verdict(host, CURL[host], LEDGER), EGRESS_DENIED,
                             f"{host} is in the proxy's own ledger")

    def test_wikipedia_is_the_control_and_it_is_denied_too(self):
        """A host nobody believes is down, refused identically -> the variable
        is the allowlist, not the source."""
        self.assertIn("en.wikipedia.org", refused_hosts(LEDGER))

    def test_an_unlogged_000_is_NOT_promoted_to_a_policy_denial(self):
        """The negative control, and it is the whole point of the file."""
        self.assertEqual(verdict("example.invalid", "000", LEDGER), UNDETERMINED)

    def test_a_real_code_passes_through_untouched(self):
        self.assertEqual(verdict("raw.githubusercontent.com", "200", LEDGER), "200")

    def test_the_ledger_carries_a_mechanism_not_just_a_flag(self):
        for e in LEDGER["recentRelayFailures"]:
            self.assertIn("403", e["detail"])
            self.assertIn("CONNECT", e["detail"])
            self.assertTrue(e["ts"].startswith("2026-10-08"))


class TheOracleMapIsTwoDifferentNetworks(unittest.TestCase):
    """The correction this pass owes its own instrument map.

    `pypi` and `npm` answer 200/404 cleanly -- and they are in `noProxy`, so
    they never traverse the gateway that refused the four policy hosts.  Their
    health is therefore NOT evidence that the allowlist is broad.  Two
    instruments, two network paths, and a map that conflates them over-reads
    every licence datum taken from a registry.
    """
    def test_pypi_and_npm_bypass_the_refusing_layer(self):
        self.assertTrue(bypasses_proxy("pypi.org", LEDGER))
        self.assertTrue(bypasses_proxy("registry.npmjs.org", LEDGER))

    def test_the_refused_hosts_do_NOT_bypass_it(self):
        for host in CURL:
            self.assertFalse(bypasses_proxy(host, LEDGER))

    def test_registry_success_does_not_license_an_allowlist_claim(self):
        """Stated as an assertion so it cannot be quietly forgotten."""
        registries_ok = all(bypasses_proxy(h, LEDGER)
                            for h in ("pypi.org", "registry.npmjs.org"))
        policy_denied = refused_hosts(LEDGER) >= set(CURL)
        self.assertTrue(registries_ok and policy_denied,
                        "both hold at once, which is exactly why neither "
                        "predicts the other")


class WhatThisPassDidNotMeasure(unittest.TestCase):
    def test_the_allowlist_is_still_not_enumerated(self):
        """`P744`: 4 of 4 denied is not a rate, and `noProxy` is a BYPASS list,
        not the allowlist. Nothing here says which hosts would be allowed."""
        self.assertEqual(len(refused_hosts(LEDGER)), 4)
        self.assertNotIn("allowlist", LEDGER)


# ---------------------------------------------------------------------------
# `P294` (pass 294, 2026-10-18) -- THE NEGATIVE CONTROL `P798` NEVER RAN.
#
# `P798` guards an UNLOGGED `000` against promotion to a policy denial, and its
# negative control is `example.invalid` -- a host it ASSERTED was absent from
# the ledger rather than one it probed.  Pass 294 probed one.
#
# 🔴 `this-host-does-not-exist-p294.example` -- an invented name, no DNS record
# anywhere -- curl `000`, and it IS IN THE LEDGER, with the byte-identical
# mechanism the seven real hosts got: `connect_rejected`, `gateway answered 403
# to CONNECT`.  The gateway refuses the CONNECT BEFORE any name resolution, so
# a ledger entry is written for a host that cannot exist.
#
# Two consequences, and the second is the one that reaches the shelves:
#
# 1. `P798`'s guarded branch is DEAD CODE on this channel.  Every HTTPS host
#    probed through the gateway is logged, so `verdict()` never reaches its
#    `UNDETERMINED` arm.  The control is sound as written and unreachable in
#    practice -- it was never falsifiable here.
#
# 2. 🔴 `EGRESS_DENIED (allowlist)` DOES NOT LICENSE AN EXISTENCE CLAIM.
#    `P798`'s README reads the two causes as licensing "opposite next actions
#    -- one says *the source is fine, this environment may not read it*".  A
#    ledger hit says neither.  It is a verdict about the CHANNEL and carries no
#    information about the host, because the invented host earns the same one.
#
# The repair is not a new folder: it is a SECOND verdict, named separately, so
# the channel reading can never be spent as an existence reading.
# ---------------------------------------------------------------------------

# Captured live, 2026-10-18, `$HTTPS_PROXY/__agentproxy/status` -- seven hosts
# from `p294`'s source-verification sweep, the invented control, and two hosts
# re-probed for the calibration.  Trimmed to the fields the suite reads.
LEDGER_P294 = json.loads("""
{"recentRelayFailures":[
 {"ts":"2026-10-18T14:44:35.943Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"unu.edu:443"},
 {"ts":"2026-10-18T14:44:36.243Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"educationforallinindia.com:443"},
 {"ts":"2026-10-18T14:44:36.551Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"sota.io:443"},
 {"ts":"2026-10-18T14:44:36.820Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"www.aigl.blog:443"},
 {"ts":"2026-10-18T14:44:37.117Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"conference.acuass.org:443"},
 {"ts":"2026-10-18T14:44:37.422Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"www.marketsandmarkets.com:443"},
 {"ts":"2026-10-18T14:44:37.691Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"nm-aist.ac.tz:443"},
 {"ts":"2026-10-18T14:45:00.141Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"this-host-does-not-exist-p294.example:443"},
 {"ts":"2026-10-18T14:45:00.538Z","kind":"connect_rejected",
  "detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "host":"en.wikipedia.org:443"}],
 "noProxy":"localhost,127.0.0.1,registry.npmjs.org,jsr.io,pypi.org,files.pythonhosted.org,index.crates.io,proxy.golang.org"}
""")

# The invented name.  No DNS record; it exists only in this fixture.
FAKE_P294 = "this-host-does-not-exist-p294.example"

# Hosts `p294` proved real on a DIFFERENT channel: their LICENSE blobs were
# read at a pin through `raw.githubusercontent.com`, which is allowlisted.
PROVEN_REAL_OFF_CHANNEL = ("github.com",)

EXISTENCE_UNMEASURED = "EXISTENCE-UNMEASURED (channel refused)"
EXISTENCE_CONFIRMED = "EXISTENCE-CONFIRMED (payload read)"

EXISTENCE_VOCABULARY = (EXISTENCE_UNMEASURED, EXISTENCE_CONFIRMED)


def existence_verdict(host, transport_code, ledger, payload_read=False):
    """`P294`: what the REFUSAL channel may say about whether a host exists.

    Answer: NOTHING, and the body says so by not branching on it.  `host`,
    `transport_code` and `ledger` are accepted and deliberately UNUSED -- that
    is the finding, not an oversight.  A `connect_rejected` entry is written
    before name resolution, so an invented host earns the same entry as a real
    one; any branch on those three arguments would return the same token on
    both sides.

    🔴 The first draft of this function DID branch on them, with identical
    tokens in both arms -- `p293`'s `C36` trap (`... or True`) arriving one
    pass later, a condition written from the author's intent rather than from
    the value.  It was caught by asking what could make the branch fail.
    Nothing could.  So the branch is gone and
    `test_the_verdict_is_INVARIANT_under_host_and_code` asserts its absence.

    The only token that asserts existence is reserved for a payload actually
    read, and `payload_read` must come from a channel that was NOT refused.
    """
    return EXISTENCE_CONFIRMED if payload_read else EXISTENCE_UNMEASURED


class TheLedgerDoesNotDiscriminateExistence(unittest.TestCase):
    """`P294`'s live negative control, and the five assertions that follow it."""

    def test_the_INVENTED_host_is_in_the_ledger(self):
        """The measurement `P798` is missing.  If this fails, the gateway has
        started resolving before refusing and `P798`'s reading is restored."""
        self.assertIn(FAKE_P294, refused_hosts(LEDGER_P294))

    def test_the_invented_host_earns_the_IDENTICAL_mechanism(self):
        """Not merely present -- indistinguishable."""
        entries = {e["host"].rsplit(":", 1)[0]: e["detail"]
                   for e in LEDGER_P294["recentRelayFailures"]}
        self.assertEqual(entries[FAKE_P294], entries["unu.edu"])

    def test_P798s_channel_verdict_still_fires_and_is_still_correct(self):
        """The repair takes nothing away: as a statement about the CHANNEL,
        `EGRESS_DENIED` is right for the invented host too -- the gateway did
        refuse it."""
        self.assertEqual(verdict(FAKE_P294, "000", LEDGER_P294), EGRESS_DENIED)

    def test_a_ledger_hit_does_NOT_license_an_existence_claim(self):
        """The assertion that reaches the shelves."""
        self.assertEqual(
            existence_verdict("unu.edu", "000", LEDGER_P294),
            EXISTENCE_UNMEASURED)

    def test_real_and_invented_are_INDISTINGUISHABLE_on_this_channel(self):
        """Stated as an equality so it cannot be read as a caveat."""
        self.assertEqual(
            existence_verdict("unu.edu", "000", LEDGER_P294),
            existence_verdict(FAKE_P294, "000", LEDGER_P294))

    def test_P798s_UNDETERMINED_arm_is_UNREACHABLE_on_this_channel(self):
        """Every HTTPS host probed through the gateway in `p294` was logged, so
        the arm `P798` exists to guard never ran.  Sound, and not falsifiable
        here -- which is why the defect survived a green suite."""
        probed = {e["host"].rsplit(":", 1)[0]
                  for e in LEDGER_P294["recentRelayFailures"]}
        self.assertEqual(
            [h for h in probed if verdict(h, "000", LEDGER_P294) == UNDETERMINED],
            [])


class ExistenceComesFromAPayloadOrFromNowhere(unittest.TestCase):
    def test_github_com_is_403_yet_PROVEN_real_off_channel(self):
        """`github.com` answers 403 to curl here.  `p294` nonetheless read five
        LICENSE blobs at pins via `raw.githubusercontent.com`.  The refusal was
        never evidence about the repositories."""
        for host in PROVEN_REAL_OFF_CHANNEL:
            self.assertEqual(
                existence_verdict(host, "403", LEDGER_P294, payload_read=True),
                EXISTENCE_CONFIRMED)

    def test_the_same_host_without_the_payload_falls_back_to_UNMEASURED(self):
        self.assertEqual(
            existence_verdict("github.com", "403", LEDGER_P294),
            EXISTENCE_UNMEASURED)

    def test_the_existence_vocabulary_is_CLOSED(self):
        """`C9` of `p293`'s oracle, carried: a token outside the list is a bug,
        and a bare `ABSENT` is not in it."""
        self.assertEqual(len(EXISTENCE_VOCABULARY), 2)
        self.assertNotIn("ABSENT", EXISTENCE_VOCABULARY)
        for host, code, payload in (("unu.edu", "000", False),
                                    (FAKE_P294, "000", False),
                                    ("github.com", "403", True),
                                    ("raw.githubusercontent.com", "200", False)):
            self.assertIn(existence_verdict(host, code, LEDGER_P294, payload),
                          EXISTENCE_VOCABULARY)

    def test_the_verdict_is_INVARIANT_under_host_and_code(self):
        """`P294`'s own trap, asserted rather than commented.  Vary the host,
        the transport code and the ledger; with no payload the token does not
        move.  A future branch on any of the three breaks this control, which
        is the point -- it would be claiming a discrimination this channel has
        been measured not to have."""
        baseline = existence_verdict("unu.edu", "000", LEDGER_P294)
        for host in (FAKE_P294, "github.com", "en.wikipedia.org", "nm-aist.ac.tz"):
            for code in ("000", "403", "200", "404"):
                for led in (LEDGER_P294, LEDGER, {"recentRelayFailures": []}):
                    self.assertEqual(
                        existence_verdict(host, code, led), baseline,
                        f"{host}/{code} moved the token without a payload")

    def test_the_two_verdicts_are_SEPARATE_functions(self):
        """The whole repair.  One call cannot return both, so a channel reading
        cannot be spent as an existence reading by accident."""
        self.assertNotEqual(verdict(FAKE_P294, "000", LEDGER_P294),
                            existence_verdict(FAKE_P294, "000", LEDGER_P294))


class WhatP294DidNotMeasure(unittest.TestCase):
    def test_the_allowlist_is_still_not_enumerated(self):
        """`P744`, carried: nine denials is not a rate, and this pass adds no
        enumeration either.  `raw.githubusercontent.com` answering 200 is
        evidence about `raw.githubusercontent.com`."""
        self.assertNotIn("allowlist", LEDGER_P294)
        self.assertNotIn("raw.githubusercontent.com", refused_hosts(LEDGER_P294))

    def test_a_DNS_only_probe_was_not_run(self):
        """The one experiment that WOULD separate absent from blocked is a name
        resolution off the proxy path.  `p294` did not run it, and the suite
        says so rather than implying the question is closed."""
        self.assertNotIn("dnsProbe", LEDGER_P294)


if __name__ == "__main__":
    unittest.main(verbosity=1)
