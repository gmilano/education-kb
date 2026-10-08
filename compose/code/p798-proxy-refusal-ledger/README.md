---
industry: education
region: Global
updated: 2026-10-08
---

# `P798` — the refusing layer testifies, so a refusal stops being an inference

Artefacts and suite of the **sixty-fifth pass (2026-10-08)**. 🟢 **9/9 green under `python3 -I`.**

## What changed against `P797`

🟢 Pass 64 closed `Gap 293` by a **control**: Wikipedia — not a policy host, not a regulator, not
down — refused identically to four policy hosts, so the variable had to be the channel's allowlist.
🔵 That was sound and it was an **inference from a pattern**.

🆕 **This pass read the refusing layer's own ledger.** `$HTTPS_PROXY/__agentproxy/status` returns
`recentRelayFailures`, and for each of the four hosts probed it carries a **host, a timestamp and a
mechanism**:

```
connect_rejected · gateway answered 403 to CONNECT (policy denial or upstream failure)
en.wikipedia.org:443 · digital-strategy.ec.europa.eu:443
www.iesalc.unesco.org:443 · www.multistate.us:443        all at 2026-10-08T19:52:0?Z
```

🟢 **So `EGRESS_DENIED (allowlist)` is now a reading of a first-party record, not a deduction.**

## The trap the suite guards

🔴 `curl` writes **`000`** for a proxy CONNECT denial **and** for a genuinely unreachable host.
🔵 Those are not the same fact and they license **opposite** next actions — one says *"the source is
fine, this environment may not read it"*, the other says *"retry, or doubt the source."*
🟢 `verdict()` therefore refuses to promote an **unlogged** `000` to a policy denial: it returns
`UNDETERMINED (transport)`. That negative control is `test_an_unlogged_000_is_NOT_promoted_to_a_policy_denial`.

## 🔴 The correction this pass owes its own oracle map

🟢 `pypi` and `npm` answer **200/404** cleanly, and this KB has leaned on that as calibration.
🔴 **They are in the proxy's `noProxy` list** — `pypi.org`, `files.pythonhosted.org`,
`registry.npmjs.org`, `jsr.io`, `index.crates.io`, `proxy.golang.org` — **so they never traverse the
gateway that refused the four policy hosts.**

🔵 **Two instruments, two network paths.** A healthy registry pair says nothing about how broad the
allowlist is, and a map that treats registry health as general reachability over-reads every datum
it takes from a registry. `TheOracleMapIsTwoDifferentNetworks` asserts both halves at once, because
it is their **co-occurrence** that proves neither predicts the other.

## 🔴 Still not measured

🔴 **The allowlist is not enumerated.** `P744` holds: four of four denied is **not a rate**, and
`noProxy` is a **bypass** list, not the allowlist. Nothing here says which hosts would be allowed.
