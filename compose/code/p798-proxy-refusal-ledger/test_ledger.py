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


if __name__ == "__main__":
    unittest.main(verbosity=1)
